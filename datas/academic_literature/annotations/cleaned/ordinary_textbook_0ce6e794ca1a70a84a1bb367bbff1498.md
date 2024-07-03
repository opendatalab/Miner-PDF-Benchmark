# 2019 IMO 预选题及其解答 

陈锐㭏舀 ${ }^{1}$, 田葆华 ${ }^{1}$, 郭尧昱 ${ }^{1}$, 张潇瀚 $^{2}$

(1. 中国人民大学附属中学, 100080, 2. 北京市实验中学, 100089)

指导老师: 陈晨 (学而思数学竞赛主教练)

这是 2019 年IMO的预选题及解答. 每年的 IMO 六道试题都是各国领队从当年的 IMO 预选题中通过投票选出来的, 而预选题是由主办国成立一个选题委员会从各国提供的大量问题中遴选而得. 由于 IMO 的预选题有一年的保密期,因此目前我们只能看到 2019 年及之前的预选题. 2019 年的预选题共有 32 道, 四个板块一般数字越大难度越大, IMO 的预选题是专家们通过讨论选择出来的,绝大多数质量很高, 风格与 IMO 考题类似, 非常适合准备冬令营及以上考试的同学们参考并作为训练资料.

陈晨老师个人比较欣赏 A $6, \mathrm{C} 4, \mathrm{C} 9, \mathrm{G} 8, \mathrm{~N} 4, \mathrm{~N} 7$ 这几道题目, 想法独特或者思路众多, 做起来很有意思.

今年的预选题解答由陈晨老师和上述四位同学提供. 解答经由清华和北大的孙孟越, 仇傲同学帮助汇总整理润色, 其中孙孟越主要负责代数与数论部分的整理, 仇傲主要负责几何与组合部分的整理. 此外, 对于官方解答中特别精彩的部分, 我们也选取了一些与大家分享. 我们已尽力将解答写得清晰易懂, 但仍不免有瑕疪, 欢迎批评指正.

## I. 代数

A 1. 令 $\mathbb{Z}$ 表示整数集, 试确定所有函数 $f: \mathbb{Z} \rightarrow \mathbb{Z}$ 满足

$$
f(2 a)+2 f(b)=f(f(a+b))
$$

对任意整数 $a, b$ 成立., 解 1. 将原函数中的 $a$ 与 $b$ 互换, 得到 $f(2 a)+2 f(b)=$ $f(f((a+b))=2 f(a)+f(2 b)$. 即有 $f(2 a)-2 f(a)=f(2 b)-2 f(b)$ 对任意整数 $a$和 $b$ 成立. 因此对任意整数 $x$ 有 $f(2 x)-2 f(x)=c$.

取 $x=0$, 有 $f(0)=-c$. 代回 (1) 有

$$
c+2 f(a)+2 f(b)=f(f(a+b)) \text {. }
$$

在上式中取 $a=0$, 有

$$
2 f(b)-c=f(f(b)) \text {. }
$$

由 $(2),(3)$ 知 $c+2 f(a)+2 f(b)=f(f(a+b))=2 f(a+b)-c$.

令 $g(x)=f(x)+c$, 有 $g(a)+g(b)=g(a+b)$.

由柯西方法知道 $g(x)=k x, f(x)=k x-c$, 其中 $k$ 为常值

带回 (1) 解得 $f(x) \equiv 0$ 或 $f(x)=2 x-c$ ( $c$ 为任意固定的整数).

解 2. 把 (1) 中 $a$ 换为 $a+x, b$ 换为 $b-x$. 得到

$$
f(2 a+2 x)+2 f(b-x)=f(f(a+b))=f(2 a)+2 f(b) .
$$

取 $a=0, x=1$ 得到, 对任意 $b \in \mathbb{Z}$,

$$
2(f(b)-f(b-1))=f(2)-f(0) .
$$

是常数, 于是 $f$ 是线性函数. 之后同解答 1 .

注. 我们试图对条件做一些变形, 我们想要消去等式两边的若干项. 我们有许多选择, 比如让 $f(a+b)=2 a$, 会得到 $2 f(b)=0$. 但我们没法确保 $f$ 取到一个偶数值. 我们或者想让 $f(a+b)=b$. 但是看上去并没有太大作用. 不过如果我们固定下 $a+b$ 之后, $f(f(a+b))$ 就不变了, 做差以后就可以得到一些很好的性质(直接得到线性性), 这样这个题就迎刃而解了.

A 2. 令实数 $u_{1}, u_{2}, \ldots, u_{2019}$ 满足

$$
u_{1}+u_{2}+\cdots+u_{2019}=0 \text { 与 } u_{1}^{2}+u_{2}^{2}+\cdots+u_{2019}^{2}=1 \text {, }
$$

并记 $a=\min \left(u_{1}, u_{2}, \ldots, u_{2019}\right), b=\max \left(u_{1}, u_{2}, \ldots, u_{2019}\right)$. 证明

$$
a b \leq-\frac{1}{2019}
$$

解 1.

$0 \geq \sum_{i=1}^{2019}\left(a-u_{i}\right)\left(b-u_{i}\right)=2019 a b-\sum_{i=1}^{2019}(a+b) u_{i}+\sum_{i=1}^{2019} u_{i}^{2}=1+2019 a b$.

因此 $a b \leq-\frac{1}{2019}$, 证毕.

解 2. 记

$$
A=\left\{i \mid u_{i} \geq 0\right\}, B=\left\{i \mid u_{i}<0\right\} .
$$

则有 $\sum_{i \in A} u_{i}=\sum_{i \in B}\left(-u_{i}\right)$, 把这个和记为 $S$.
注意到

$$
S=\sum_{i \in A} u_{i} \leq|A||b|, S=\sum_{i \in B}\left(-u_{i}\right) \leq|B||a|,
$$

有

$$
\begin{aligned}
1=\sum_{i=1}^{2019} u_{i}^{2} & =\sum_{i \in A} u_{i}^{2}+\sum_{i \in B} u_{i}^{2} \\
& \leq|b| \sum_{i \in A}\left|u_{i}\right|+|a| \sum_{i \in B}\left|u_{i}\right| \\
& =|a| S+|b| S \\
& \leq|a|(|b||A|)+|b|(|a||B|)=-2019 a b .
\end{aligned}
$$

故 $a b \leq-\frac{1}{2019}$, 证毕.

注. 该不等式可在 $u_{1}=u_{2}=\cdots=u_{k}=-\sqrt{\frac{2019-k}{2019 k}}, u_{k+1}=\cdots=u_{2019}=$ $\sqrt{\frac{k}{2019(2019-k)}}, 1 \leq k \leq 2019$ 时取到等号, 这种用最大值最小值去限制其他数写局部不等式是常用手段.

A 3. 给定正整数 $n \geq 3$ 以及严格递增的 $n$ 项正实数数列 $\left(a_{1}, a_{2}, \ldots, a_{n}\right)$, 满足其各项之和为 $2 . X$ 是使得

$$
\left|1-\sum_{i \in X} a_{i}\right|
$$

最小的 $\{1,2, \ldots, n\}$ 的子集. 证明存在一个严格递增的 $n$ 项正数列 $\left(b_{1}, b_{2}, \ldots, b_{n}\right)$,满足其各项之和亦为 2 ,且

$$
\sum_{i \in X} b_{i}=1
$$

解 1 . 注意到

$$
\left|1-\sum_{i \in X} a_{i}\right|=\left|1-\sum_{i \in X^{c}} a_{i}\right|
$$

我们不妨设 $\sum_{i \in X} a_{i} \leq 1$. 否则用 $X^{c}$ 代替 $X$. ( $X^{c}$ 是 $X$ 关于 $[1, n]$ 的补集. 显然 $X, X^{c}$ 都不是空集, 这个事实我们会在下面的解答中多次使用.)

若 $\sum_{i \in X} a_{i}=1$, 则取 $b_{i}=a_{i}$ 已成立. 下设 $\sum_{i \in X} a_{i}=1-\epsilon, \epsilon>0$. 我们取

$$
b_{i}= \begin{cases}a_{i}+\frac{1}{|X|} \epsilon, & \text { 若 } i \in X, \\ a_{i}-\frac{1}{\left|X^{c}\right|} \epsilon, & \text { 若 } i \in X^{c} .\end{cases}
$$

那么 $\sum_{i \in X} b_{i}=\sum_{i \in X^{c}} b_{i}=1$. 我们只需要验证 $b_{i}$ 递增即可.

若有 $b_{j} \geq b_{j+1}$, 由于 $a_{j}<a_{j+1}$. 所以唯一可能的情况为 $b_{j}=a_{j}+\frac{1}{|X|} \epsilon, b_{j+1}=$
$a_{j+1}-\frac{1}{\left|X^{c}\right|} \epsilon . j \in X, j+1 \in X^{c}$. 由此得到

$$
0<a_{j+1}-a_{j} \leq \frac{\epsilon}{|X|}+\frac{\epsilon}{|X|^{c}}<2 \epsilon
$$

这里的严格不等号用到了 $|X|+|X|^{c}=n \geq 3$. 我们考虑 $X^{\prime}=(X \backslash\{j\}) \cup\{j+1\}$.

则有

$$
1-\epsilon<\sum_{i \in X^{\prime}} a_{i}=1-\epsilon+\left(a_{j+1}-a_{j}\right)<1+\epsilon
$$

这与 $\left|\sum_{i \in X} a_{i}-1\right|$ 的最小性相矛盾.

解 2. 我们对解答 1 略作修改. 仍然设 $\sum_{i \in X} a_{i}=1-\epsilon<1$.

(a) 若存在 $j$ 使得 $j \in X, j+1 \in X^{c}$, 那么我们考虑 $X^{\prime}=(X \backslash\{j\}) \cup\{j+1\}$.

则有

$$
\sum_{i \in X^{\prime}} a_{i}=1-\epsilon+\left(a_{j+1}-a_{j}\right)>1-\epsilon \Longrightarrow \sum_{i \in X^{\prime}} a_{i}=1-\epsilon+\left(a_{j+1}-a_{j}\right) \geq 1+\epsilon
$$

所以 $a_{j+1}-a_{j} \geq 2 \epsilon$.

(a.i)如果 $a_{j+1}-a_{j}>2 \epsilon$, 我们就取

$$
b_{i}= \begin{cases}a_{i}, & \text { 若 } i \neq j \text { 且 } i \neq j+1, \\ a_{j}+\epsilon, & \text { 若 } i=j, \\ a_{j+1}-\epsilon, & \text { 若 } i=j+1 .\end{cases}
$$

即可.

(a.ii) 如果 $a_{j+1}-a_{j}=2 \epsilon$, 分两类情况.

(a.ii.i) 如果 $|X| \geq 2$, 我们就取 $k \in X, k \neq j$ 使得

$$
b_{i}= \begin{cases}a_{i}, & \text { 若 } i \neq j \text { 或 } j+1 \text { 或 } k, \\ a_{j}+\epsilon-\delta, & \text { 若 } i=j, \\ a_{j+1}-\epsilon, & \text { 若 } i=j+1, \\ a_{k}+\delta, & \text { 若 } i=k .\end{cases}
$$

这里的 $0<\delta<\min \left\{a_{k+1}-a_{k}, \epsilon\right\}$. (补充定义 $a_{n+1}=100$.)

(a.ii.i) 如果 $\left|X^{c}\right| \geq 2$, 我们就取 $k \in X^{c}, k \neq j+1$ 使得

$$
b_{i}= \begin{cases}a_{i}, & \text { 若 } i \neq j \text { 或 } j+1 \text { 或 } k, \\ a_{j}+\epsilon, & \text { 若 } i=j, \\ a_{j+1}-\epsilon+\delta, & \text { 若 } i=j+1, \\ a_{k}-\delta, & \text { 若 } i=k .\end{cases}
$$

这里的 $0<\delta<\min \left\{a_{k}-a_{k-1}, \epsilon\right\}$. (补充定义 $a_{0}=0$.)

(b) 若不存在 $j$ 使得 $j \in X, j+1 \in X^{c}$. 那么就有 $X=\{k, k+1, \ldots, n\}$, 对某个 $k>1$ 成立. 那么我们考虑 $X^{\prime}=X \cup\{1\}$. 则有

$$
\sum_{i \in X^{\prime}} a_{i}=1-\epsilon+a_{1}>1-\epsilon \Longrightarrow \sum_{i \in X^{\prime}} a_{i}=1-\epsilon+a_{1} \geq 1+\epsilon
$$

所以 $a_{1} \geq 2 \epsilon$. 我们就取 $k \in X^{c}, k \neq j+1$ 使得

$$
b_{i}= \begin{cases}a_{1}-\epsilon, & \text { 若 } i=1, \\ a_{n}+\epsilon, & \text { 若 } i=n, \\ a_{i}, & \text { 若 } 1<i<n .\end{cases}
$$

即可.

注. 这些做法的想法都是利用 $b_{i}$ 在 $a_{i}$ 的基础上进行微调, 最后利用 $\mid \sum_{i \in X} a_{i}-$ $1 \mid$ 的最小性保持 $b_{i}$ 的递增性. 具体调整的方案可以有非常多种. 我们再呈现一个做法, 他们选取了不同的路径.

解 3. 仍设 $\sum_{i \in X} a_{i}=1-\epsilon<1$.

如果能找到一个 $k$ 使得 $|X \cap[k, n]|>\left|X^{c} \cap[k, n]\right|$. 那么我们选最大的 $k$ 使得 $|X \cap[k, n]|>\left|X^{c} \cap[k, n]\right|$, 就有 $|X \cap[k, n]|-\left|X^{c} \cap[k, n]\right|=1$. 这样, 我们取

$$
b_{i}= \begin{cases}a_{i}, & i<k \\ a_{i}+\epsilon, & i \geq k\end{cases}
$$

就成立了.

我们证明一定存在这样的 $k$, 我们用反证法, 若对每个 $k$ 都有 $|X \cap[k, n]| \leq$ $\left|X^{c} \cap[k, n]\right|$. 那么对每个 $i \in X$, 存在 $j_{i} \in X^{c}$ 使得 $i<j_{i} \leq n$, 并且不同的 $i$ 对应不同的 $j_{i}$. (可以对 $X$ 中元素从大到小来取相应的 $j_{i}$, 由反证法假设保证了一定是能取出来的.) 我们记 $Y$ 是 $X^{c}$ 中去掉所有 $j_{i}$ 构成的集合. 那么

$$
2 \epsilon=\sum_{i \in X^{c}} a_{i}-\sum_{i \in X} a_{i}=\sum_{i \in X}\left(a_{j_{i}}-a_{i}\right)+\sum_{i \in Y} a_{i}
$$

上面每一项都是正的, 并且一共有 $n-|X| \geq n / 2$ 项 ( $X$ 一定非空, $Y$ 可能为空集). 由于 $n \geq 3$, 上面和式中至少有两项, 于是每一项都小于 $2 \epsilon$. 那么考虑 $X^{\prime}=(X \backslash\{i\}) \cup\left\{j_{i}\right\}$, 有

$$
1-\epsilon=\sum_{i \in X} a_{i}<\sum_{i \in X^{\prime}} a_{i}<1+\epsilon
$$

就得到了矛盾.
注. 这个问题本身难度并不高, 主要是如何用数学语言描述清楚这个把一小部分数增加的过程, 笨办法就是把所有的量设出来.

A 4. 给定正整数 $n \geq 2$, 以及实数 $a_{1}, a_{2}, \ldots, a_{n}$, 满足 $a_{1}+a_{2}+\cdots+a_{n}=0$.定义集合 $A$ 满足

$$
A=\left\{(i, j)|1 \leq i<j \leq n,| a_{i}-a_{j} \mid \geq 1\right\}
$$

证明: 若 $A$ 非空,则

$$
\sum_{(i, j) \in A} a_{i} a_{j}<0
$$

解 1 . 原命题等价于

$$
2 \sum_{(i, j) \in A} a_{i} a_{j}<\left(\sum_{i=1}^{n} a_{i}\right)^{2}
$$

也等价于

$$
\sum_{i=1}^{n} a_{i}^{2}+2 \sum_{\substack{1 \leq i<j \leq n \\(i, j) \notin A}} a_{i} a_{j}>0
$$

注意到

$$
\sum_{\substack{1 \leq i<j \leq n \\(i, j) \notin A}} a_{i} a_{j}=\sum_{\substack{1 \leq i<j \leq n \\\left|a_{i}-a_{j}\right|<1 \\ a_{i} a_{j}<0}} a_{i} a_{j}+\sum_{\substack{1 \leq i<j \leq n \\\left|a_{i}-a_{j}\right|<1 \\ a_{i} a_{j}>0}} a_{i} a_{j} \geq \sum_{\substack{1 \leq i<j \leq n \\-1<\min \left\{a_{i}, a_{j}\right\}<0 \\ 0<\max \left\{a_{i}, a_{j}\right\}<1}} a_{i} a_{j}+\sum_{\substack{1 \leq i<j \leq n \\ 0<\left|a_{i}\right|,\left|a_{j}\right|<1 \\ a_{i} a_{j}>0}} a_{i} a_{j} .
$$

这是因为

$$
\sum_{\substack{1 \leq i<j \leq n \\\left|a_{i}-a_{j}\right|<1 \\ a_{i} a_{j}<0}} a_{i} a_{j} \geq \sum_{\substack{1 \leq i<j \leq n \\-1<\min \left\{a_{i}, a_{j}\right\}<0 \\ 0<\max \left\{a_{i}, a_{j}\right\}<1}} a_{i} a_{j}, \quad \sum_{\substack{1 \leq i<j \leq n \\\left|a_{i}-a_{j}\right|<1 \\ a_{i} a_{j}>0}} a_{i} a_{j} \geq \sum_{\substack{1 \leq i<j \leq n \\ 0<\left|a_{i}\right|,\left|a_{j}\right|<1 \\ a_{i} a_{j}>0}} a_{i} a_{j}
$$

故

$$
\sum_{i=1}^{n} a_{i}^{2}+2 \sum_{\substack{1 \leq i<j \leq n \\(i, j) \notin A}} a_{i} a_{j} \geq \sum_{\left|a_{i}\right| \geq 1} a_{i}^{2}+\left(\sum_{\left|a_{i}\right|<1} a_{i}\right)^{2} \geq 0
$$

下说明其不可能取等.

若不然,

$$
\sum_{\left|a_{i}\right| \geq 1} a_{i}^{2}+\left(\sum_{\left|a_{i}\right|<1} a_{i}\right)^{2}=0
$$

表明对任意 $a_{i},\left|a_{i}\right|<1$. 那么对 $(i, j) \in A$, 都有 $a_{i} a_{j}<0$. 于是只要 $A$ 非空, 就有 $\sum_{(i, j) \in A} a_{i} a_{j}<0$. 矛盾, 结论成立.
解 2. 记 $S_{1}=\left\{a_{i}: a_{i} \leq-1\right\}, S_{2}=\left\{a_{i}:-1<a_{i}<0\right\}, S_{3}=\left\{a_{i}: 0<a_{i} \leq\right.$ $1\}, S_{4}=\left\{a_{i}: a_{i} \geq 1\right\}$. 分别记 $d_{i}$ 为 $S_{i}$ 元素和 $i=1,2,3,4$. 这里空集的元素和为 0 . 那么

$$
\sum_{\substack{(i, j) \in A \\ a_{i} a_{j}>0}} a_{i} a_{j} \leq \frac{1}{2} d_{1}^{2}+\frac{1}{2} d_{4}^{2}+d_{1} d_{2}+d_{3} d_{4}
$$

也有

$$
\sum_{\substack{(i, j) \in A \\ a_{i} a_{j}<0}} a_{i} a_{j} \leq d_{1} d_{4}+d_{2} d_{4}+d_{1} d_{3}
$$

所以, 结合 $d_{1}+d_{2}+d_{3}+d_{4}=0$,

$$
\begin{aligned}
\sum_{(i, j) \in A} a_{i} a_{j} & \leq \frac{1}{2} d_{1}^{2}+\frac{1}{2} d_{4}^{2}+d_{1} d_{2}+d_{3} d_{4}+d_{1} d_{4}+d_{2} d_{4}+d_{1} d_{3} \\
& =\frac{\left(d_{1}+d_{4}\right)^{2}}{2}+\left(d_{1}+d_{4}\right)\left(d_{2}+d_{3}\right) \\
& =\frac{-\left(d_{1}+d_{4}\right)^{2}}{2}
\end{aligned}
$$

等号成立需要 $S_{1}, S_{4}$ 中没有元素, 那么对 $(i, j) \in A$, 都有 $a_{i} a_{j}<0$. 于是只要 $A$非空, 就有 $\sum_{(i, j) \in A} a_{i} a_{j}<0$. 矛盾, 结论成立.

注. 从两个解答中都可以看出, 把 $a_{i}$ 分成四类是重要的.

A 5. 令 $x_{1}, x_{2}, \ldots, x_{n}$ 为互异的实数. 证明

$$
\sum_{i=1}^{n} \prod_{j \neq i} \frac{1-x_{i} x_{j}}{x_{i}-x_{j}}= \begin{cases}1, & n \text { 为奇数; } \\ 0, & n \text { 为偶数. }\end{cases}
$$

解 1. 由于两边都是有理函数, 我们只需要对所有 $x_{i}$ 都不为 $\pm 1$ 的情况证明结论即可(这表明通分后化简后会得到一个零多项式). 我们对多项式

$$
f(x)=\prod_{i=1}^{n}\left(1-x_{i} \cdot x\right)
$$

在点 $1,-1, x_{1}, x_{2}, \ldots, x_{n}$ 处, 由于 $\operatorname{deg} f<n+2$, 用Lagrange插值公式就得到

$$
\begin{aligned}
f(x)= & \sum_{i=1}^{n} f\left(x_{i}\right) \frac{(x+1)(x-1)}{\left(x_{i}+1\right)\left(x_{i}-1\right)} \prod_{j \neq i} \frac{x-x_{j}}{x_{i}-x_{j}}+f(1) \frac{x+1}{1+1} \prod_{i=1}^{n} \frac{x-x_{j}}{1-x_{j}} \\
& +f(-1) \frac{x-1}{-1-1} \prod_{i=1}^{n} \frac{x-x_{j}}{-1-x_{j}} .
\end{aligned}
$$

我们比较两边 $x^{n+1}$ 次项系数. 就得到

$$
0=\sum_{i=1}^{n} f\left(x_{i}\right) \frac{1}{\left(x_{i}+1\right)\left(x_{i}-1\right)} \prod_{j \neq i} \frac{1}{x_{i}-x_{j}}+\frac{1}{2} f(1) \prod_{i=1}^{n} \frac{1}{1-x_{j}}-\frac{1}{2} f(-1) \prod_{i=1}^{n} \frac{1}{-1-x_{j}} .
$$

我们注意

$$
\begin{gathered}
f\left(x_{i}\right)=\left(1-x_{i}^{2}\right) \prod_{j \neq i}\left(1-x_{i} x_{j}\right) . \\
f(1)=\prod_{i=1}^{n}\left(1-x_{i}\right) . \\
f(-1)=\prod_{i=1}^{n}\left(1+x_{i}\right)=(-1)^{n} \prod_{i=1}^{n}\left(-1-x_{i}\right) .
\end{gathered}
$$

所以

$$
0=-\sum_{i=1}^{n} \prod_{j \neq i} \frac{1-x_{i} x_{j}}{x_{i}-x_{j}}+\frac{1}{2}+\frac{1}{2}(-1)^{n+1}
$$

即得结论.

注. 本做法的难点在于构造出这样的 $f$ 并选取合适的节点, 构造出这样的 $f$ 之后, 还得添加上 $+1,-1$ 两个节点. 于是这里需要 $x_{i}$ 都不为 $\pm 1$, 才能满足Lagrange插值公式的使用条件.

也有做法只利用 $x_{1}, x_{2}, \ldots, x_{n}$ 来构造插值, 但是这样的代价是要分奇偶讨论. 有兴趣的同学可以参考预选题官方英文解答.

解 2. 记

$$
G\left(x_{1}, \ldots, x_{n}\right)=\sum_{i=1}^{n} \prod_{j \neq i} \frac{1-x_{i} x_{j}}{x_{i}-x_{j}}
$$

我们把 $G\left(x_{1}, \ldots, x_{n}\right)$ 看成关于 $x_{n}$ 有理函数, 把其他变量都看成系数. 通分后可以写为

$$
G\left(x_{1}, \ldots, x_{n}\right)=\frac{P\left(x_{n}\right)}{\prod_{j \neq n}\left(x_{n}-x_{j}\right)}
$$

这里 $P\left(x_{n}\right)$ 是一个关于 $x_{n}$ 的多项式, 其系数中可能出现 $x_{1}, \ldots, x_{n-1}$. 我们实际上有

$$
P\left(x_{n}\right)=\prod_{j \neq n}\left(1-x_{n} x_{j}\right)+\sum_{i=1}^{n-1}\left(x_{i} x_{n}-1\right) \prod_{j \neq i, n} \frac{\left(x_{n}-x_{j}\right)\left(1-x_{i} x_{j}\right)}{x_{i}-x_{j}} .
$$

我们发现 $P(x)$ 是一个至多 $n-1$ 次的多项式. 我们取一个 $k \neq n$. 那么对 $i \neq k, n$就有 $\prod_{j \neq i, n}\left(x_{k}-x_{j}\right)=0$. 由此, 我们得到

$$
\begin{aligned}
P\left(x_{k}\right) & =\prod_{j \neq n}\left(1-x_{k} x_{j}\right)+\sum_{i=1}^{n-1}\left(x_{i} x_{k}-1\right) \prod_{j \neq i, n} \frac{\left(x_{k}-x_{j}\right)\left(1-x_{i} x_{j}\right)}{x_{i}-x_{j}} \\
& =\prod_{j \neq n}\left(1-x_{k} x_{j}\right)+\left(x_{k}^{2}-1\right) \prod_{j \neq k, n} \frac{\left(x_{k}-x_{j}\right)\left(1-x_{k} x_{j}\right)}{x_{k}-x_{j}}
\end{aligned}
$$

$$
\begin{aligned}
& =\prod_{j \neq n}\left(1-x_{k} x_{j}\right)+\left(x_{k}^{2}-1\right) \prod_{j \neq k, n}\left(1-x_{k} x_{j}\right) \\
& =0 .
\end{aligned}
$$

故 $x-x_{k} \mid P(x)$. 所以有

$$
\prod_{j=1}^{n-1}\left(x-x_{j}\right) \mid P(x)
$$

但是 $P(x)$ 是一个至多 $n-1$ 次的多项式, 所以只能有 $P(x)=c \prod_{j=1}^{n-1}\left(x-x_{j}\right), c$是一个只依赖于 $x_{1}, x_{2}, \ldots, x_{n-1}$ 的常数. 所以有理函数 $G=c$ 不依赖于 $x_{n}$.

完全类似地, 可以得到有理函数 $G$ 是不依赖于 $x_{1}, x_{2}, \ldots, x_{n}$, 所以 $G$ 就是一个常数.

最后, 我们只需要定下 $G$ 的值即可. 这里的方法有很多.

对偶数 $n$, 我们可以取 $x_{2 j-1}=j+1, x_{2 j}=1 / x_{2 j-1}, j=1,2, \ldots,[n / 2]$. 那么就有

$$
\prod_{j \neq k}\left(1-x_{k} x_{j}\right)=0, \forall k \quad \Longrightarrow G=0
$$

对奇数 $n$, 在此之上定义一个 $x_{n}=1$. 就得到

$$
G=\prod_{j \neq n} \frac{1-x_{j}}{1-x_{j}}=1
$$

注. 这个做法还有一个变种, 就是根据 $n$ 的奇偶直接把 $G$ 或 $G-1$ 通分, 分母是 $\prod_{i<j}\left(x_{i}-x_{j}\right)$, 而分子可以被 $\prod_{i=1}^{n}\left(x_{i}-1\right) \prod_{i<j}\left(x_{i}-x_{j}\right)$ 整除, 但分子次数没这么高, 只能是零多项式, 结论成立. 细节留给感兴趣的读者.

解 3. 我们考虑关于 $a$ 的多项式

$$
T(a)=\sum_{i=1}^{n} \prod_{j \neq i} \frac{a-x_{i} x_{j}}{x_{i}-x_{j}}
$$

对每个 $0 \leq m-1 \leq n-1$, 我们考虑 $T(a)$ 中 $a^{m}$ 次系数. 记 $\sigma(i, m)$ 是 $x_{1}, x_{2}, \ldots, x_{i-1}, x_{i+1}, \ldots, x_{n}$ 的 $m$ 次初等对称多项式.

$$
\begin{aligned}
T(a) \text { 中 } a^{m} \text { 项系数 } & =\sum_{i=1}^{n} \frac{x_{i}^{n-1-m} \cdot(-1)^{n-1-m} \sigma(i, n-1-m)}{\prod_{j \neq i}\left(x_{i}-x_{j}\right)} \\
& =\sum_{i=1}^{n} \frac{\prod_{j \neq i}\left(y-x_{j}\right)}{\prod_{j \neq i}\left(x_{i}-x_{j}\right)} \cdot x_{i}^{n-1-m} \text { 中 } y^{m} \text { 的系数. }
\end{aligned}
$$

由 Lagrange 插值公式,

$$
\sum_{i=1}^{n} \frac{\prod_{j \neq i}\left(y-x_{j}\right)}{\prod_{j \neq i}\left(x_{i}-x_{j}\right)} \cdot x_{i}^{n-1-m}=y^{n-1-m}
$$

于是

$$
\begin{aligned}
T(a) \text { 中 } a^{m} \text { 项系数 } & =y^{n-1-m} \text { 中 } y^{m} \text { 的系数 } \\
& = \begin{cases}1, & \text { 若 } 2 m=n-1, \\
0, & \text { 其余情形. }\end{cases}
\end{aligned}
$$

所求即为 $T(1)$, 易得结论.

注. 这个解答通过引入一个新的主元，得到一个关于 $a$ 的多项式. 通过分析 $T(a)$ 的各项系数, 我们得到了答案.

我们最后再呈现一个做法, 这个做法利用了 $\frac{1-x y}{x-y}$ 正好和双曲余切差角公式的结构一致。

解 4. 我们引入双曲余切函数 $\operatorname{coth} x=\frac{\mathrm{e}^{x}+\mathrm{e}^{-x}}{\mathrm{e}^{x}-\mathrm{e}^{-x}}=\frac{\mathrm{e}^{2 x}+1}{\mathrm{e}^{2 x}-1}$. 可以证明其满足双曲余切差角公式

$$
\operatorname{coth}(\alpha-\beta)=\frac{1-\operatorname{coth} \alpha \operatorname{coth} \beta}{\operatorname{coth} \alpha-\operatorname{coth} \beta} .
$$

我们记 $f(n)=\sum_{i=1}^{n} \prod_{j \neq i} \frac{1-x_{i} x_{j}}{x_{i}-x_{j}}$. 我们用归纳法证明 $f(n)=f(n-2)$. 奠基 $n=$ 2,3 是容易验证的, 此处略去.

下设 $f(n-1), f(n-2)$ 已经知道为常数, 来证明 $f(n)=f(n-2)$. 与解答 1 相同, 我们只需要证明 $x_{j}$ 都不等于 $\pm 1$ 的情形即可. 我们取 $\theta_{j}=\operatorname{arccoth} x_{j}$, $j=1,2, \ldots, n$. 这里 $\theta_{j}$ 在 $\left|x_{j}\right|<1$ 时是一个虚数, $\left|x_{j}\right|>1$ 时是一个实数. 那利用双曲正切差角公式

$$
\begin{aligned}
f(n)= & \operatorname{coth}\left(\theta_{1}-\theta_{2}\right)\left(\operatorname{coth}\left(\theta_{1}-\theta_{3}\right) \cdots \operatorname{coth}\left(\theta_{1}-\theta_{n}\right)-\operatorname{coth}\left(\theta_{2}-\theta_{3}\right) \cdots \operatorname{coth}\left(\theta_{2}-\theta_{n}\right)\right) \\
& +\sum_{i=3}^{n} \operatorname{coth}\left(\theta_{i}-\theta_{1}\right) \operatorname{coth}\left(\theta_{i}-\theta_{2}\right) \prod_{\substack{j \neq i \\
j>2}} \operatorname{coth}\left(\theta_{i}-\theta_{j}\right) .
\end{aligned}
$$

利用差角公式的变形得到(取 $\alpha=\theta_{i}-\theta_{2}, \beta=\theta_{i}-\theta_{1}$ 之后通分.)

$$
\operatorname{coth}\left(\theta_{i}-\theta_{1}\right) \operatorname{coth}\left(\theta_{i}-\theta_{2}\right)=1+\left(\operatorname{coth}\left(\theta_{i}-\theta_{1}\right)-\operatorname{coth}\left(\theta_{i}-\theta_{2}\right)\right) \operatorname{coth}\left(\theta_{1}-\theta_{2}\right)
$$

于是 $f(n)$ 在上式中第二个和式可以改写为

$$
\begin{aligned}
& \sum_{i=3}^{n} \operatorname{coth}\left(\theta_{i}-\theta_{1}\right) \operatorname{coth}\left(\theta_{i}-\theta_{2}\right) \prod_{\substack{j \neq i \\
j>2}} \operatorname{coth}\left(\theta_{i}-\theta_{j}\right) \\
= & \sum_{i=3}^{n} \prod_{\substack{j \neq i \\
j>2}} \operatorname{coth}\left(\theta_{i}-\theta_{j}\right)+\operatorname{coth}\left(\theta_{1}-\theta_{2}\right) \prod_{\substack{j \neq i \\
j>2}} \operatorname{coth}\left(\theta_{i}-\theta_{j}\right)
\end{aligned}
$$

$$
\begin{aligned}
& \cdot \sum_{i=3}^{n}\left(\operatorname{coth}\left(\theta_{i}-\theta_{1}\right)-\operatorname{coth}\left(\theta_{i}-\theta_{2}\right)\right) \\
= & f(n-2)+\operatorname{coth}\left(\theta_{1}-\theta_{2}\right) \sum_{i=3}^{n}\left(\operatorname{coth}\left(\theta_{i}-\theta_{1}\right)-\operatorname{coth}\left(\theta_{i}-\theta_{2}\right)\right) \prod_{\substack{j \neq i \\
j>2}} \operatorname{coth}\left(\theta_{i}-\theta_{j}\right) .
\end{aligned}
$$

于是, 为了证明 $f(n)=f(n-2)$, 只需证明下式成立.

$$
\begin{aligned}
0= & \operatorname{coth}\left(\theta_{1}-\theta_{2}\right)\left(\prod_{j>2} \operatorname{coth}\left(\theta_{1}-\theta_{j}\right)-\prod_{j>2} \operatorname{coth}\left(\theta_{2}-\theta_{j}\right)\right) \\
& +\operatorname{coth}\left(\theta_{1}-\theta_{2}\right) \sum_{i=3}^{n}\left(\operatorname{coth}\left(\theta_{i}-\theta_{1}\right)-\operatorname{coth}\left(\theta_{i}-\theta_{2}\right)\right) \prod_{\substack{j \neq i \\
j>2}} \operatorname{coth}\left(\theta_{i}-\theta_{j}\right)
\end{aligned}
$$

整理一下, 只要证明

$$
\begin{aligned}
& \prod_{j>2} \operatorname{coth}\left(\theta_{1}-\theta_{j}\right)+\sum_{i=3}^{n} \operatorname{coth}\left(\theta_{i}-\theta_{1}\right) \prod_{\substack{j \neq i \\
j>2}} \operatorname{coth}\left(\theta_{i}-\theta_{j}\right) \\
= & \prod_{j>2} \operatorname{coth}\left(\theta_{2}-\theta_{j}\right)+\sum_{i=3}^{n} \operatorname{coth}\left(\theta_{i}-\theta_{2}\right) \prod_{\substack{j \neq i \\
j>2}} \operatorname{coth}\left(\theta_{i}-\theta_{j}\right) .
\end{aligned}
$$

这就是 $n-1$ 的归纳假设, 等式左边对 $x_{1}, x_{3}, \ldots, x_{n}$ 使用, 等式右边对 $x_{2}, x_{3}, \ldots, x_{n}$使用. 所以等式两边都是 $f(n-1)$. 于是我们证得了 $f(n)=f(n-2)$. 由归纳原理知结论成立.

注. 本题作为一个代数恒等式，可以有非常多种方法. 解答 4 实际上充分利用了双曲余切的代数结构, 因为双曲余切在考场上的出现频率远小于正切和余切, 所以给大家介绍一下这个方案. 其实如果同学熟悉正切差角公式的话, 可以看出做代换 $x=\mathfrak{i} \cot \theta$ 时, $\mathfrak{i}$ 是虚数单位. 也有

$$
\mathfrak{i} \cot (\alpha-\beta)=\frac{1-(\mathfrak{i} \cot \alpha)(\mathfrak{i} \cot \beta)}{(\mathfrak{i} \cot \alpha)-(\mathfrak{i} \cot \beta)} .
$$

成立. 但实际上有 $\operatorname{coth}(\theta)=\mathfrak{i} \cot (\mathfrak{i} \theta)$, 所以也可以得到解答 4 的这个换元.

如果不想出现复数的话, 我们可以在解答 4 中限制所有 $\left|x_{j}\right|$ 都大于 1 , 这样得到的 $\theta_{j}$ 都是实数, 然后利用有理函数的性质得到结论.

这四类方案是非常漂亮的, 各有各的特色, 当然还有很多大同小异的方案.

A 6. 已知三变量实系数多项式 $P(x, y, z)$ 满足恒等式

$$
P(x, y, z)=P(x, y, x y-z)=P(x, x z-y, z)=P(y z-x, y, z) .
$$

证明: 存在单变量多项式 $F(t)$ 使得

$$
P(x, y, z)=F\left(x^{2}+y^{2}+z^{2}-x y z\right) .
$$

解 1. 记 $R(x, y, z)=P\left(x, y, z+\frac{x y}{2}\right)$. 则 $R(x, y, z)=P\left(x, y, z+\frac{x y}{2}\right)=$ $P\left(x, y,-z+\frac{x y}{2}\right)=R(x, y,-z)$. 所以 $R$ 中含有 $z$ 的项的幕次都是偶数. 即 $R(x, y, z)$可以写为关于 $x, y, z^{2}$ 的多项式. 所以

$$
P(x, y, z)=R\left(x, y, z-\frac{x y}{2}\right)=R_{1}\left(x, y,\left(z-\frac{x y}{2}\right)^{2}\right) .
$$

而 $\left(z-\frac{x y}{2}\right)^{2}=\frac{x^{2} y^{2}}{4}+z(z-x y)$, 所以 $P$ 可以写成关于 $x, y, z(z-x y)$ 的多项式.我们设

$$
P(x, y, z)=\sum_{i, j, k \in \mathbb{N}} \mu_{i, j, k} x^{i} y^{j}(z(z-x y))^{k} .
$$

我们考察 $P(x, y, z)$ 的最高次项. 设 $\operatorname{deg} P(x, y, z)=m$, 那么 $P(x, y, z)$ 的最高次项一定是满足 $i+j+3 k=m$ 的 $x^{i} y^{j}(z(z-x y))^{k}$ 提供的. 其最高次项为 $x^{k+i} y^{k+j} z^{k}$, 其余项的次数都小于 $m$. 而且不同的 $(i, j, k)$ 会提供不同的最高次项 $x^{k+i} y^{k+j} z^{k}$, 所以不会被被消掉. 所以我们得到 $P(x, y, z)$ 中最高次项 $x^{\alpha} y^{\beta} z^{\gamma}$, 一定是由 $x^{\alpha-\gamma} y^{\beta-\gamma}(z(z-x y))^{\gamma}$ 提供的, 且满足 $\alpha \geq \gamma, \beta \geq \gamma$.

注意我们还只用到了 $P(x, y, z)=P(x, y, x y-z)$. 对剩下两个等式也做类似的操作, 我们可以得到 $P(x, y, z)$ 中最高次项必然满足 $\alpha \geq \beta, \gamma \geq \beta$ 以及 $\beta \geq \alpha, \gamma \geq \alpha$. 这表明 $\alpha=\beta=\gamma, m=3 \alpha$, 并且 $P(x, y, z)$ 的最高次项都是形如 $(x y z)^{\alpha}$ 的形式的. 设 $P(x, y, z)$ 中 $(x y z)^{m / 3}$ 的系数为 $\mu$, 那么我们考察

$$
P_{1}(x, y, z)=P(x, y, z)-\mu\left(x^{2}+y^{2}+z^{2}-x y z\right)^{m / 3} .
$$

这个多项式 $P_{1}$ 仍然满足题设条件, 并且 $\operatorname{deg} P_{1}<\operatorname{deg} P$. 继续这样做, 有限步就可以把 $P$ 写成关于 $x^{2}+y^{2}+z^{2}-x y z$ 的多项式.

注. 这个做法通过分析最高次项的性质得到了结论.

解 2. 我们要用到如下著名的恒等式. 对满足 $u+v+w=0$ 的实数 $u, v, w$,有

$$
\cos ^{2} u+\cos ^{2} v+\cos ^{2} w-2 \cos u \cos v \cos w-1=0 .
$$

断言 1 . 多项式 $P(x, y, z)$ 在集合

$$
\mathfrak{S}=\{(2 \cos u, 2 \cos v, 2 \cos w): u+v+w=0\} .
$$

上是常数.

断言 1 的证明. 记 $G(u, v, w)=P(2 \cos u, 2 \cos v, 2 \cos w)$, 那么注意

$$
(2 \cos u)(2 \cos v)-2 \cos w=4 \cos u \cos v-2 \cos (u+v)=2 \cos (u-v) \text {. }
$$

所以条件就可以写为 $G(u, v, w)=G(-u, v, u-v)$. 也有 $G(u, v, w)=G(w-$
$v, v,-w$ ). 我们分别使用这两个条件得到(下式第一个等号用了第一个条件, 第二个等号用了第二个条件.)

$$
G(u, v, w)=G(-u, v, u-v)=G(u-2 v, v, v-u)=G(u-2 v, v, w+2 v) .
$$

归纳法得到, 对整数 $k$,

$$
G(u, v, w)=G(u-2 k v, v, w+2 k v) .
$$

类似地, 对整数 $l$,

$$
G(u, v, w)=G(u, v+2 l u, w-2 l u) .
$$

再注意, 对整数 $p, q$, 有

$$
G(u, v, w)=G(u+2 p \pi, v+2 q \pi, w-2(p+q) \pi) .
$$

我们取非零的 $u, v$ 使得 $u, v, \pi$ 在 $\mathbb{Q}$ 上线性无关. 那么我们结合以上三个式子, 可以知道 $G$ 在平面 $u+v+w=0$ 的一个稠密子集上都取到同一个值. 进而结合 $G$的连续性知 $G$ 是常数. 即 $P$ 在 $\mathfrak{S}$ 上是常数, 这个常数是 $P(2,2,2)$. 断言1成立.

断言 2. $P(x, y, z)-P(2,2,2)$ 作为实系数多项式能被 $T(x, y, z)=x^{2}+y^{2}+$ $z^{2}-x y z-4$ 整除.

断言 2 的证明. 作带余除法

$$
P(x, y, z)-P(2,2,2)=T(x, y, z) R(x, y, z)+A(y, z) x+B(y, z) .
$$

我们注意 $P(x, y, z)-P(2,2,2)$ 在 $\mathfrak{S}$ 上取到 $0, T$ 在 $\mathfrak{S}$ 上也取到 0 . 所以 $A(y, z) x+$ $B(y, z)$ 也得在 $\mathfrak{S}$ 上取到 0 .

但是对 $\frac{\pi}{3}<v, w<\frac{2 \pi}{3}, y=2 \cos v, z=2 \cos w$ 时, $x$ 有两个不同的值可以取, 分别是 $2 \cos (v+w)$ 和 $2 \cos (v-w)$. 这两个值一个大于 0 , 一个小于 0 , 是不同的. 但都满足 $A(y, z) x+B(y, z)=0$. 只能有 $A(y, z)=B(y, z)=0$. 于是 $A(y, z), B(y, z)$ 都在一个开集上为 0 , 只能是零多项式. (可以进一步展开成关于 $y$ 的多项式 $A(x, y)=\sum d_{k}(z) y^{k}$, 对固定的 $z$ 有无穷多个解 $y$, 说明其 $d_{k}(z)$都为零. 而 $d_{k}(z)=0$ 对无穷个 $z$ 都成立, 进而 $d_{k}(z)$ 也是零多项式.)

断言 2 成立.

最后, 我们只要对 $\frac{P(x, y, z)-P(2,2,2)}{T(x, y, z)}=P_{1}(x, y, z)$ 继续讨论即可. 由于 $\operatorname{deg} P_{1}<$ $\operatorname{deg} P$, 进行充分多次后, 我们得到 $P_{k}(x, y, z)$ 会是一个常数. 那么我们最开始的 $P(x, y, z)$ 其实可以写为关于 $T(x, y, z)$ 的多项式, 此即结论.

注. 这个做法把条件充分使用, 得到了 $P(x, y, z)-P(2,2,2)$ 在曲面 $\mathfrak{S}$ 的一个稠密集上为零, 由此推出在曲面 $\mathfrak{S}$ 上为零. 进一步, $P(x, y, z)-P(2,2,2)$
被 $x^{2}+y^{2}+z^{2}-x y z-4$ 整除. 这是非常精彩的做法, 思路自然, 层层递进, 太美妙了! 三角恒等式在构造过程中为我们提供了极大的便利.

用代数几何的语言来解释, 这个题实际上要证明Markov三元组在Markov曲面上是Zariski稠密的. 有兴趣的同学可以参考预选题官方英文解答, 并在大学修读代数几何课程。

A 7. 令 $\mathbb{Z}$ 表示整数集. 考虑函数 $f: \mathbb{Z} \rightarrow \mathbb{Z}$ 其满足

$$
f(f(x+y)+y)=f(f(x)+y)
$$

对任意整数 $x, y$ 成立. 对于这样的函数 $f$, 若整数 $v$ 满足集合

$$
X_{v}=\{x \in \mathbb{Z}: f(x)=v\}
$$

有限且非空, 则我们称整数 $v$ 为 $f$-罕见的.

(a) 证明存在一个函数 $f$ 使其有一个对应的 $f$-帘见的整数.

(b) 证明不存在这样的函数 $f$ 使其有大于 1 个对应的 $f$-罕见的整数.

解 1. (a) 我们给出这个函数. 定义 $f(0)=0$. 对 $x \neq 0$, 定义 $f(x)=2^{\nu_{2}(x)+1}$.这里 $\nu_{2}(x)$ 是最大的自然数 $\alpha$, 满足 $2^{\alpha} \mid x$. 定义 $\nu_{2}(0)=+\infty$.

我们来验证这个等式成立. 若 $f(x)=f(x+y)$, 显然成立.

若 $f(x+y) \neq f(x)$, 则说明 $\nu_{2}(y)<\nu_{2}(x) . y \neq 0, \nu_{2}(y)<\infty$. 于是 $\nu_{2}(f(x+$ $y))=\nu_{2}(y)+1>\nu_{2}(y), \nu_{2}(f(x))=\nu_{2}(x)+1>\nu_{2}(y)$. 于是 $\nu_{2}(f(x+y)+y)=$ $\nu_{2}(f(x)+y)=\nu_{2}(y)$, 所以等式成立.

而这里 0 就是 $f$-罕见的整数.

(b) 我们假设存在一个 $f$-罕见的整数 $u$, 由题目条件可知, 对正整数 $k$,

$$
f(f(x)+y)=f(f(x+y)+y)=f(f(x+2 y)+y)=\cdots=f(f(x+k y)+y) .
$$

上式对整数 $k$ 也成立. 我们取 $a$ 是 $X_{u}$ 中最小的元素, 在上式中取 $y=a-f(x)$得到

$$
u=f(a)=f(f(x+k(a-f(x)))+a-f(x)) .
$$

于是 $f(x+k(a-f(x)))+a-f(x) \in X_{u}$, 由于 $a$ 是 $X_{u}$ 中最小的元素, 我们得到

$$
f(x+k(a-f(x)))+a-f(x) \geq a, \forall k, x \in \mathbb{Z} .
$$

即

$$
f(x+k(a-f(x))) \geq f(x), \forall k, x \in \mathbb{Z}
$$

我们再取 $b$ 是 $X_{u}$ 中最大的元素, 在上式中取 $y=b-f(x)$ 得到

$$
u=f(b)=f(f(x+k(b-f(x)))+b-f(x)) .
$$

于是 $f(x+k(b-f(x)))+b-f(x) \in X_{u}$, 由于 $b$ 是 $X_{u}$ 中最大的元素, 我们得到

$$
f(x+k(b-f(x))) \leq f(x), \forall k, x \in \mathbb{Z}
$$

特别地, 结合这两个式子可以得到

$f(x+k(a-f(x))(b-f(x))) \leq f(x) \leq f(x+k(b-f(x))(a-f(x))), \forall k, x \in \mathbb{Z}$.

就这表明

$$
f(x)=f(x+k(a-f(x))(b-f(x))) .
$$

所以对 $f(x) \neq a, b, X_{f(x)}$ 中都含有一个无穷等差数列, 不可能有限. 罕见的整数只能为 $a, b$ 之一. 所以 $u=a$ 或者 $u=b, f(u)=f(a)=f(b)=u$. 所以罕见的整数必然满足 $f(u)=u$.

如果 $a \neq b$ 都是罕见的整数, 就得到 $f(a)=a, f(b)=b$, 但是 $f(a)=f(b)$,这就推出 $a=b$, 矛盾. 所以不存在两个罕见的整数.

解 2. 我们对第二部分给出一个不同的处理方案.

(b) 用反证法, 设 $u \neq v$ 都是 $f$-罕见的整数. $u$ 的原像是 $a_{1}<a_{2}<\cdots<$ $a_{m}$. 那么在

$$
f(f(x)+y)=f(f(x+y)+y) .
$$

中, 取 $x=u, y=a_{i}-u$ 得到

$$
f\left(f(u)+a_{i}-u\right)=f\left(a_{i}\right)=u .
$$

于是 $f(u)-u+a_{i} \in X_{u}$. 那么

$$
a_{1}+f(u)-u<a_{2}+f(u)-u<\ldots<a_{m}+f(u)-u \text {. }
$$

正好也是 $X_{u}$ 中的 $m$ 个元素, 进而 $f(u)-u=0, f(u)=u$. 同样地, $f(v)=v$.

我们记 $x_{0}=u, y_{0}=v-u$. 则有 $f\left(x_{0}\right)=x_{0}, f\left(x_{0}+y_{0}\right)=x_{0}+y_{0}$. 且有 $y_{0} \neq 0$. 那么

$$
x_{0}+y_{0}=f\left(f\left(x_{0}\right)+y_{0}\right)=f\left(f\left(x_{0}+y_{0}\right)+y_{0}\right)=f\left(x_{0}+2 y_{0}\right) .
$$

所以 $f\left(x_{0}+2 y_{0}\right)=x_{0}+y_{0}$. 现在设正整数 $k$ 满足 $f\left(x_{0}+k y_{0}\right)=x_{0}+y_{0}$, 在条件中令 $x=x_{0}, y=k y_{0}$ 得到

$$
f\left(x_{0}+(k+1) y_{0}\right)=f\left(f\left(x_{0}+k y_{0}\right)+k y_{0}\right)=f\left(f\left(x_{0}\right)+k y_{0}\right)=x_{0}+y_{0} .
$$

于是对所有正整数 $k$ 都有 $f\left(x_{0}+k y_{0}\right)=x_{0}+y_{0}=v$. 而这与 $X_{v}$ 有限相矛盾.

注. 这个题第二问可能相对好入手一点点, 做完第二问对第一问的构造有极大的启发, 出题人可能有其他的背景知识进行了这种排序吧.

## II. 几何

G1. 给定三角形 $A B C$, 圆 $\Gamma$ 过点 $A$, 分别再次交线段 $A B, A C$ 于点 $D, E$,与线段 $B C$ 交于点 $F, G$, 其中 $F$ 在 $B, G$ 之间. 过点 $F$ 的圆 $B D F$ 的切线和过点 $G$ 的圆 $C E G$ 的切线交于 $T$. 若 $A$ 和 $T$ 不重合, 证明: $A T \| B C$.



解. 连结 $A F, A G$, 由相切与共圆的性质有 $\angle T F G=\angle B D F=\angle B G A$. 同理 $\angle T G F=\angle A F G$. 因此 $\triangle T G F \cong \triangle A F G, A$ 与 $T$ 到 $F G$ 距离相同. 故 $A T$与 $B C$ 平行.



注. 这道题很简单, 只需要通过导角找到等腰梯形结构即可.

G 2. 锐角三角形 $A B C$ 过 $A, B, C$ 分别向 $B C, C A, A B$ 所引的三条高线垂足是 $D, E, F$. 令 $\omega_{B}, \omega_{C}$ 分别是 $\triangle B D F, \triangle C D E$ 的内切圆, 并设它们分别和线
段 $D F, D E$ 切于点 $M, N$. 直线 $M N$ 和圆 $\omega_{B}, \omega_{C}$ 分别再次交于点 $P \neq M, Q \neq$ $N$. 证明: $M P=N Q$.



解. 设 $I_{1}, I_{2}$ 分别为 $\omega_{B}, \omega_{C}$ 的圆心, $R$ 为 $\omega_{C}$ 与 $B C$ 的切点. 连结 $I_{1} M, I_{2} N$.由垂足性质, $\triangle B D F \sim \triangle B A C \sim \triangle E D C$. 由于相似图形中对应线段长度比等于相似比, 故有

$$
\frac{I_{2} N}{I_{1} M}=\frac{E D}{B D}=\frac{R D}{M D}
$$

因此

$$
\frac{P M}{N Q}=\frac{2 I_{1} M \sin \angle P M D}{2 I_{2} N \sin \angle Q N E}=\frac{B D \sin \angle N M D}{E D \sin \angle M N D}=\frac{B D}{E D} \cdot \frac{N D}{M D}=\frac{B D}{M D} \cdot \frac{R D}{E D}=1 .
$$

即 $P M=N Q$.



注. 本题做法相对唯一, 不难发现可从边的比例计算入手.

G 3. 在三角形 $A B C$ 中, 点 $A_{1}, B_{1}$ 分别在边 $B C, A C$ 上, 点 $P, Q$ 分别在 $A A_{1}, B B_{1}$ 上, 且 $P Q \| A B$. 点 $P_{1}$ 在 $P B_{1}$ 的延长线上, 满足 $\angle P P_{1} C=\angle B A C$.点 $Q_{1}$ 在 $Q A_{1}$ 的延长线上, 满足 $\angle C Q_{1} Q=\angle C B A$. 证明: $P, Q, P_{1}, Q_{1}$ 四点共圆.



解 1. 作 $\triangle A B C$ 的外接圆 $\omega$. 延长 $B B_{1}, A A_{1}$, 分别与 $\omega$ 交于 $X, Y$; 延长 $B_{1} P, A_{1} Q$ 分别与 $A B$ 交于 $S, T$. 由于 $\angle C P_{1} S=\angle C A S$, 故 $C, P_{1}, A, S$ 共圆.因此由相交弦定理,

$$
B_{1} S \cdot B_{1} P_{1}=B_{1} C \cdot B_{1} A=B_{1} X \cdot B_{1} B
$$


由于 $P Q \| S B$, 故有

$$
\frac{B_{1} P}{B_{1} S}=\frac{B_{1} Q}{B_{1} B}
$$

两式相乘得

$$
B_{1} P_{1} \cdot B_{1} P=B_{1} X \cdot B_{1} Q .
$$

故 $P_{1}, X, P, Q$ 共圆. 同理 $Q_{1}, Y, Q, P$ 共圆. 因为 $\angle Y X Q=\angle Y A B=\angle Y P Q$,故 $X, P, Q, Y$ 共圆. 结合三个共圆知 $P_{1}, X, P, Q, Y, Q_{1}$ 六点共圆.

解 2. 设直线 $P Q$ 交 $C A, C B$ 于点 $U, V, Q A$ 交 $P B$ 于 $N . \angle C P_{1} P=$ $\angle C A B=\angle C U P$, 故 $C, P_{1}, U, P$ 共圆, 记为 $\Gamma_{1}$. 同理 $C, Q, V, Q_{1}$ 共圆, 记为 $\Gamma_{2}$.设直线 $C N$ 与 $P Q, A B$ 分别交于点 $W, Z$. 由于 $U V \| A B$, 有

$$
\frac{W Q}{W P}=\frac{Z A}{Z B}=\frac{W U}{W V}
$$

即 $W P \cdot W U=W Q \cdot W V, W$ 到 $\Gamma_{1}, \Gamma_{2}$ 等幕. 故 $C N$ 为 $\Gamma_{1}, \Gamma_{2}$ 的根轴.

若 $P P_{1}$ 与 $Q Q_{1}$ 不平行, 则设它们所在直线交于点 $L$. 对两直线 $A P A_{1}, B Q B_{1}$由Pappus定理, 有 $C, N, L$ 共线, 即 $L$ 在 $\Gamma_{1}, \Gamma_{2}$ 的根轴上. 故 $L Q \cdot L Q_{1}=L P \cdot L P_{1}$,即 $P, Q, Q_{1}, P_{1}$ 共圆.

若 $P P_{1} \| Q Q_{1}$, 由Pappus定理, $P P_{1}\|C N\| Q Q_{1}$. 设 $\Gamma_{1}, \Gamma_{2}$ 交于 $C, K . K$在根轴 $C N$ 上. 故 $P P_{1}\|C K\| Q Q_{1}$. 结合共圆知四边形 $P P_{1} C K, K Q Q_{1} C$ 为等腰梯形. 故 $P_{1} P Q Q_{1}$ 均为等腰梯形. 因此 $P, Q, Q_{1}, P_{1}$ 共圆.



(a)



(b)

解 3. 本解答中, 复平面上的点与其所对应复数用同一字母表示, 单位圆指圆 $|Z|=1$. 我们先证明复数法的几个基本结论.
引理 1. 复平面上三点 $X, Y, Z$ 共线. 则 $(\bar{X}-\bar{Y}) Z+(Y-X) \bar{Z}+X \bar{Y}-$ $\bar{X} Y=0$.

引理 1 的证明. $\frac{Z-X}{Y-Z} \in \mathbb{R}$. 故

$$
\frac{Z-X}{Y-Z}=\overline{\left(\frac{Z-X}{Y-Z}\right)}=\frac{\bar{Z}-\bar{X}}{\bar{Y}-\bar{Z}}
$$

通分即得上式. 引理 1 证毕.

引理 2. 复平面上不共线的四点 $W, X, Y, Z$ 共圆当且仅当 $\frac{(W-Y)(X-Z)}{(W-X)(Y-Z)} \in \mathbb{R}$.

## 引理 2 的证明.

$W, X, Y, Z$ 共圆 $\Longleftrightarrow \measuredangle Z W Y=\measuredangle Z X Y \Longleftrightarrow \arg \frac{W-Z}{W-Y}=\arg \frac{X-Z}{X-Y}$

$$
\Longleftrightarrow \frac{(W-Y)(X-Z)}{(W-X)(Y-Z)} \in \mathbb{R} .
$$

引理 2 证毕.

原命题的证明. 以 $A A_{1}, B B_{1}$ 的交点 $O$ 为原点建立复平面. 由 $A_{1}, P$ 在直线 $O A$ 上, $B_{1}, Q$ 在直线 $O B$ 上, 且 $P Q \| A B$, 可设 $A_{1}=\mu A, B_{1}=\varphi B$, $P=\lambda A, Q=\lambda B$, 其中 $\mu, \varphi, \lambda \in \mathbb{R}$. 由于 $B, A_{1}, C$ 共线, 由引理 1 ,

$$
\left(\overline{A_{1}}-\bar{B}\right) C+\left(B-A_{1}\right) \bar{C}+A_{1} \bar{B}-\overline{A_{1}} B=0,
$$

即

$$
(\mu \bar{A}-\bar{B}) C+(B-\mu A) \bar{C}+\mu(A \bar{B}-\bar{A} B)=0 .
$$

同理,

$$
(\varphi \bar{B}-\bar{A}) C+(A-\varphi B) \bar{C}-\varphi(A \bar{B}-\bar{A} B)=0 .
$$

联立上两式, 消去 $\bar{C}$, 解得

$$
C=\frac{\mu(1-\varphi) A+\varphi(1-\mu) B}{1-\mu \varphi} .
$$

由于 $Q, A_{1}, Q_{1}$ 共线, 由引理 1 ,

$$
\left(\overline{A_{1}}-\bar{Q}\right) Q_{1}+\left(Q-A_{1}\right) \overline{Q_{1}}+A_{1} \bar{Q}-\overline{A_{1}} Q=0
$$

即

$$
(\lambda B-\mu A) \overline{Q_{1}}=(\lambda \bar{B}-\mu \bar{A}) Q_{1}-\lambda \mu(A \bar{B}-\bar{A} B)=0 .
$$

由 $\angle Q Q_{1} C=\angle A B C, \arg \frac{Q-A_{1}}{C-Q_{1}}=\arg \frac{A-B}{C-B}$, 即 $\frac{A-B}{C-B} \cdot \frac{C-Q_{1}}{Q-A_{1}} \in \mathbb{R}$. 而

$$
\begin{aligned}
\frac{A-B}{C-B} \cdot \frac{C-Q_{1}}{Q-A_{1}} & =\frac{(A-B)\left(\frac{\mu(1-\varphi) A+\varphi(1-\mu) B}{1-\mu \varphi}-Q_{1}\right)}{\left(\frac{\mu(1-\varphi) A+\varphi(1-\mu) B}{1-\mu \varphi}-B\right)(\lambda B-\mu A)} \\
& =\frac{(A-B)\left(\mu(1-\varphi) A+\varphi(1-\mu) B-(1-\mu \varphi) Q_{1}\right)}{(1-\varphi)(\mu A-B)(\lambda B-\mu A)}
\end{aligned}
$$

故

$$
\begin{aligned}
& \frac{(A-B)\left(\mu(1-\varphi) A+\varphi(1-\mu) B-(1-\mu \varphi) Q_{1}\right)}{(\mu A-B)(\lambda B-\mu A)} \\
& \quad=\frac{(\bar{A}-\bar{B})\left(\mu(1-\varphi) \bar{A}+\varphi(1-\mu) \bar{B}-(1-\mu \varphi) \overline{Q_{1}}\right)}{(\mu \bar{A}-\bar{B})(\lambda \bar{B}-\mu \bar{A})}
\end{aligned}
$$

交叉相乘, 按 $Q_{1}$ 移项整理得

$$
\begin{aligned}
& (A-B)(\mu(1-\varphi) A+\varphi(1-\mu) B)(\mu \bar{A}-\bar{B})(\lambda \bar{B}-\mu \bar{A}) \\
& -(\bar{A}-\bar{B})(\mu(1-\varphi) \bar{A}+\varphi(1-\mu) \bar{B})(\mu A-B)(\lambda B-\mu A) \\
= & (1-\mu \varphi)\left((A-B)(\mu \bar{A}-\bar{B})(\lambda \bar{B}-\mu \bar{A}) Q_{1}\right. \\
& \left.-(\bar{A}-\bar{B})(\mu A-B)(\lambda B-\mu A) \overline{Q_{1}}\right) .
\end{aligned}
$$

将 $(\star)$ 式代入, 得

$$
\begin{aligned}
& (A-B)(\mu(1-\varphi) A+\varphi(1-\mu) B)(\mu \bar{A}-\bar{B})(\lambda \bar{B}-\mu \bar{A}) \\
& \quad-(\bar{A}-\bar{B})(\mu(1-\varphi) \bar{A}+\varphi(1-\mu) \bar{B})(\mu A-B)(\lambda B-\mu A) \\
& =(1-\mu \varphi)(\lambda \bar{B}-\mu \bar{A})(\lambda \bar{B}-\mu \bar{A})(A \bar{B}-\bar{A} B) Q_{1} \\
& \quad+(1-\mu \varphi)(\bar{A}-\bar{B})(\mu A-B) \lambda \mu(A \bar{B}-\bar{A} B) .
\end{aligned}
$$

解得

$$
\begin{aligned}
(1-\mu \varphi)(\lambda \bar{B}-\mu \bar{A}) Q_{1}= & -\mu^{2}(1-\lambda \varphi) A \bar{A}+\mu(-\lambda+\lambda \varphi-\lambda \mu \varphi-\mu \varphi) A \bar{B} \\
& +\mu \varphi(\lambda-\mu) \bar{A} B+\varphi(\mu-\lambda) B \bar{B}
\end{aligned}
$$

因此

$$
Q_{1}-P=\frac{(\lambda-\mu)(\mu A \bar{A}-(\lambda+\mu \varphi-\lambda \mu \varphi) A \bar{B}-\mu \varphi \bar{A} B+\varphi B \bar{B})}{(1-\mu \varphi)(\lambda \bar{B}-\mu \bar{A})}
$$

同理,

$$
P_{1}-Q=\frac{(\lambda-\varphi)(\mu A \bar{A}-(\lambda+\mu \varphi-\lambda \mu \varphi) \bar{A} B-\mu \varphi A \bar{B}+\varphi B \bar{B})}{(1-\mu \varphi)(\lambda \bar{A}-\varphi \bar{B})}
$$

故

$$
\begin{aligned}
& \frac{\left(Q_{1}-P\right)\left(P_{1}-Q\right)}{\left(A_{1}-Q\right)\left(B_{1}-P\right)} \\
= & \frac{(\lambda-\mu)(\lambda-\varphi)}{(1-\mu \varphi)^{2}} \cdot \frac{|\mu A \bar{A}-(\lambda+\mu \varphi-\lambda \mu \varphi) A \bar{B}-\mu \varphi \bar{A} B+\varphi B \bar{B}|^{2}}{|\lambda \bar{B}-\mu \bar{A}|^{2}|\lambda \bar{A}-\varphi \bar{B}|^{2}} \in \mathbb{R} .
\end{aligned}
$$

而由 $Q, A_{1}, Q_{1}$ 共线, 及 $P, B_{1}, P_{1}$ 共线, 有 $\frac{A_{1}-Q}{Q_{1}-Q}, \frac{B_{1}-P}{P_{1}-P} \in \mathbb{R}$. 故

$$
\frac{\left(Q_{1}-P\right)\left(P_{1}-Q\right)}{\left(Q_{1}-Q\right)\left(P_{1}-P\right)}=\frac{A_{1}-Q}{Q_{1}-Q} \cdot \frac{B_{1}-P}{P_{1}-P} \cdot \frac{\left(Q_{1}-P\right)\left(P_{1}-Q\right)}{\left(A_{1}-Q\right)\left(B_{1}-P\right)} \in \mathbb{R}
$$

而显然, $P, Q, P_{1}, Q_{1}$ 不共线. 因此由引理 $2, P, Q, P_{1}, Q_{1}$ 共圆.
注. 受篇幅限制，部分计算过程略去.

G 4. $P$ 是 $\triangle A B C$ 内一点. 设直线 $A P$ 和 $B C$ 交于点 $A_{1}$, 直线 $B P$ 和 $C A$交于点 $B_{1}$, 直线 $C P$ 和 $A B$ 交于点 $C_{1}$. 点 $A_{2}$ 满足 $A_{1}$ 是 $P A_{2}$ 的中点, 点 $B_{2}$ 满足 $B_{1}$ 是 $P B_{2}$ 的中点, 点 $C_{2}$ 满足 $C_{1}$ 是 $P C_{2}$ 的中点. 证明: $A_{2}, B_{2}, C_{2}$ 不可能同时严格地在 $\triangle A B C$ 外接圆的内部.



解. 反设三个点都在圆内. 设直线 $A P, C P$ 分别与三角形外接圆交于 $A_{3}, C_{3}$.有

$$
A_{1} C \cdot A_{1} B=A_{1} A \cdot A_{1} A_{3}>A_{1} A \cdot A_{1} A_{2}=A_{1} A \cdot A_{1} P
$$

即

$$
\frac{A_{1} C}{A_{1} P}>\frac{A_{1} A}{A_{1} B}
$$

由正弦定理，

$$
\frac{\sin \angle A P C}{\sin \angle P C A_{1}}>\frac{\sin \angle A_{1} B A}{\sin \angle B A A_{1}}
$$

即

$$
\frac{\sin \angle A P C}{\sin \angle A B C}>\frac{\sin \angle P C B}{\sin \angle P A B}
$$

同理, 对称地有

$$
\frac{\sin \angle A P C}{\sin \angle A B C}>\frac{\sin \angle P A B}{\sin \angle P C B}
$$

两式相乘, 得 $\sin \angle A P C>\sin \angle A B C$. 又由 $\angle A P C>\angle A B C$, 有 $\angle A P C+$ $\angle A B C>180^{\circ}$. 同理, $\angle B P C+\angle B A C>180^{\circ}, \angle A P B+\angle A C P>180^{\circ}$. 故 $540^{\circ}=(\angle A P C+\angle A B C)+(\angle B P C+\angle B A C)+(\angle A P B+\angle A C P)>540^{\circ}$,
矛盾! 因此结论成立.



注. 当且仅当 $P=H$ 为 $\triangle A B C$ 垂心时, $A_{2}, B_{2}, C_{2}$ 可同时在外接圆内（包含圆上).

G 5. 凸五边形 $A B C D E$ 满足 $C D=D E, \angle E D C \neq 2 \angle A D B$. 点 $P$ 在五边形内部, 满足 $A P=A E, B P=B C$. 证明: 点 $P$ 在对角线 $C E$ 上当且仅当 $S_{\triangle B C D}+S_{\triangle A D E}=S_{\triangle A B D}+S_{\triangle A B P}$.



解 1. 以 $S(X Y Z)$ 记 $\triangle X Y Z$ 的有向面积, 即定义

$$
S(X Y Z)= \begin{cases}S_{\triangle X Y Z}, & X, Y, Z \text { 顺时针排列; } \\ -S_{\triangle X Y Z}, & X, Y, Z \text { 逆时针排列. }\end{cases}
$$

四边形的有向面积类似定义. 对 $C E$ 垂直平分线 $l$ 上的点, 定义函数

$$
f(D)=S(B C D)+S(A D E)-S(B D A)-S(B P A) \text {. }
$$

在 $D$ 在 $l$ 上沿线匀速运动时, $D$ 到 $B C$ 有向距离匀速变化, 故 $S(B C D)$ 的值匀速变化. 同理, $S(A D E), S(B D A)$ 的值匀速变化. 因此已知 $f$ 的值匀速变化,即其与 $D$ 在 $l$ 上的位置坐标值有线性关系.

设 $P$ 关于 $A B$ 对称点为 $Q$. 由五边形凸性, $Q$ 不在直线 $C E$ 上, 因此可以作出 $Q E C$ 的圆心 $O . O$ 在 $l$ 上. 由于 $B C=B P=B Q$, 有 $\triangle O B C \cong \triangle O B Q$.
同理 $\triangle O A E \cong \triangle O A Q$. 因此

$$
\begin{aligned}
f(O) & =S(B C O)+S(A O E)-S(B O A)-S(B A Q) \\
& =S(B O Q)+S(Q O A)-S(B O A)-S(B A Q)=0 .
\end{aligned}
$$



必要性. $f(D)=0$. 反设 $P$ 不在 $C E$ 上. 取 $\triangle P C E$ 的外心 $R . R$ 在 $l$ 上,且 $\triangle P B R \cong \triangle C B R, \triangle P A R \cong \triangle E A R$. 故

$$
\begin{aligned}
f(R) & =S(B C R)+S(A R E)-S(B R A)-S(B P A) \\
& =S(B C R)+S(A R E)-(S(P B R)+S(A P R)+S(B P A))-S(B P A) \\
& =-2 S(B P A) \neq 0 .
\end{aligned}
$$

因此 $f \neq \equiv 0$. 又由 $f$ 线性及 $f(D)=f(O)=0$, 有 $D=O$. 故

$$
\angle C D E=\angle C D Q+\angle Q D E=2(\angle B D Q+\angle Q D A)=2 \angle B D A=\angle B D A .
$$

与条件矛盾! 因此 $P$ 在 $C E$ 上.


充分性. $P$ 在 $C E$ 上. 取 $C E, C P, P E$ 中点 $M, X, Y$, 有 $X M=P Y$, $X P=M Y, X Y=C M=M E, X B\|l\| Y A$. 下用两种方法证明 $f(D)=0$.

方法 1. 设 $l$ 与 $A B$ 交于点 $S$. 由平行线分线段成比例定理,

$$
\frac{B S}{S A}=\frac{X M}{M Y}=\frac{P Y}{X P}=\frac{P E}{C P}
$$

记 $C, P, E$ 到 $A B$ 的距离为 $h_{C}, h_{P}, h_{E}$. 由定比分点公式,

$$
h_{P}=\frac{P E}{C E} h_{C}+\frac{C P}{C E} h_{E}=\frac{B S}{B A} h_{C}+\frac{S A}{B A} h_{E}=\frac{B S \cdot h_{C}+A S \cdot h_{E}}{B A} .
$$

因此

$$
\begin{aligned}
f(S) & =S(B C S)+S(A S E)-S(B S A)-S(B P A) \\
& =\frac{1}{2}\left(B S \cdot h_{C}+A S \cdot h_{E}-0-B A \cdot h_{P}\right)=0 .
\end{aligned}
$$

而 $S Q=S P<S E$, 故 $S \neq O$. 因此由于 $f$ 线性及 $f(O)=0, f \equiv 0$. 因此 $f(D)=0$.



法 2.

$$
\begin{aligned}
f(D) & =S(B C D)+S(A D E)-S(B D A)-S(B P A) \\
& =S(B C D)+S(A D E)-(S(P B D)+S(A P D)+S(B P A))-S(B P A) \\
& =(S(B C D)-S(P B D))+(S(A D E)-S(A P D))-2 S(B P A) \\
& =2(S(B X D)+S(A D Y)-S(B P A)) \\
& =2(S(B X M)+S(A M Y)-(S(B X Y A)-S(B X P)-S(A P Y))) \\
& =2(S(B C M)+S(A M E)-S(B X Y A)) \\
& =2(S(B X Y)+S(A X Y)-S(B X Y A))=0 .
\end{aligned}
$$



注. 这道题是一道非常规的几何问题, 动态的想法, 特值的选取, 有向面积的引入都是这道题的关键.

解 2. 以 $C E$ 中点 $O$ 为原点, 射线 $D O$ 方向为 $x$ 轴正方向, $O E$ 长为单位长建立平面直角坐标系. 设 $X, Y$ 分别为 $P C, P E$ 中点. 设 $O D=a, P$ 点坐标 $(x, y), \frac{A Y}{P E}=\lambda, \frac{B X}{P C}=\mu$. 有 $E(0,1), C(0,-1), D(-a, 0), \quad X\left(\frac{x}{2}, \frac{y-1}{2}\right)$, $Y\left(\frac{x}{2}, \frac{y+1}{2}\right), A\left(\frac{x}{2}+\lambda(1-y), \frac{y-1}{2}+\lambda x\right), B\left(\frac{x}{2}+\mu(1+y), \frac{y-1}{2}-\mu x\right)$. 因此 $2 S_{\triangle B C D}=x_{B} y_{D}+x_{C} y_{B}+x_{D} y_{C}-x_{B} y_{C}-x_{C} y_{D}-x_{D} y_{B}$ $=\left(\frac{1}{2}-\mu a\right) x+\left(\frac{a}{2}+\mu\right) y+\frac{a}{2}+\mu ;$

$2 S_{\triangle A D E}=x_{A} y_{E}+x_{D} y_{A}+x_{E} y_{D}-x_{A} y_{D}-x_{D} y_{E}-x_{E} y_{A}$

$$
=\left(\frac{1}{2}-\lambda a\right) x-\left(\frac{a}{2}+\lambda\right) y+\frac{a}{2}+\lambda ;
$$

$2 S_{\triangle A B D}=x_{A} y_{D}+x_{B} y_{A}+x_{D} y_{B}-x_{A} y_{B}-x_{B} y_{D}-x_{D} y_{A}$ $=\left(\frac{\lambda}{2}+\frac{\mu}{2}\right)\left(x^{2}+y^{2}\right)+\left(\frac{1}{2}+\lambda a+\mu a+2 \lambda \mu\right) x+(\mu-\lambda) y+a+\frac{\lambda}{2}+\frac{\mu}{2} ;$

$2 S_{\triangle A B P}=x_{A} y_{P}+x_{B} y_{A}+x_{P} y_{B}-x_{A} y_{B}-x_{B} y_{D}-x_{D} y_{A}$

$$
=-\left(\frac{\lambda}{2}+\frac{\mu}{2}\right)\left(x^{2}+y^{2}\right)+\left(2 \lambda \mu-\frac{1}{2}\right) x+\frac{\lambda}{2}+\frac{\mu}{2} .
$$

因此

$$
S_{\triangle B C D}+S_{\triangle A D E}-S_{\triangle A B D}-S_{\triangle A B P}=\frac{1}{2}(1-2 a \lambda-2 a \mu-4 \lambda \mu) x .
$$

若 $1-2 a \lambda-2 a \mu-4 \mu \lambda=0$, 则

$\cot \angle E D O=a=\frac{1-4 \lambda \mu}{2 \lambda+2 \mu}=\frac{1-\tan \angle A E Y \tan \angle B C X}{\tan \angle A E Y+\tan \angle B C X}=\cot (\angle A E Y+\angle B C X)$.

因此 $\angle E D O=\angle A E Y+\angle B C X=180^{\circ}-\angle E A Y-\angle C B X$. 作 $E$ 关于 $A D$ 的对称点 $Q$, 有 $D$ 为 $\triangle E Q C$ 外心, $A$ 为 $\triangle E P Q$ 外心. 因此

$$
\angle P Q C=\angle E Q C-\angle P Q E=\left(180^{\circ}-\angle E D O\right)-\angle E A Y=\angle C B X \text {. }
$$

因此 $B$ 为 $\triangle C P Q$ 外心, 故 $B Q=B C$. 结合 $D Q=D C$, 有 $Q$ 也是 $C$ 关于 $B D$ 的对称点. 因此 $\angle E D C=2 \angle A D B$, 与题目条件矛盾! 所以 $1-2 a \lambda-2 a \mu-4 \mu \lambda \neq 0$.故由 $(\star)$ 式, 有 $S_{\triangle B C D}+S_{\triangle A D E}=S_{\triangle A B D}+S_{\triangle A B P} \Longleftrightarrow x=0 \Longleftrightarrow P$ 在 $C E$上.



注. 在 $(\star)$ 式后也可以继续用坐标系计算.

G 6. 锐角三角形 $A B C$ 的内心为 $I$, 其内切圆分别与 $B C, C A, A B$ 切于点 $D, E, F$. 直线 $E F$ 交三角形的外接圆于点 $P, Q$, 使得 $F$ 在 $E$ 和 $P$ 之间. 证明: $\angle D P A+\angle A Q D=\angle Q I P$.



解 1. 设 $E F, F D, D E$ 中点分别为 $L, M, N, D T \perp E F$ 于 $T$, 线段 $I P, I Q$ 分别交 $\triangle D E F$ 的九点圆于 $P^{\prime}, Q^{\prime}$. 考虑关于圆 $I$ 的反演, $A \longleftrightarrow L, B \longleftrightarrow M$, $C \longleftrightarrow N$. 故圆 $A B C \longleftrightarrow$ 圆 $L M N$. 于是 $P \longleftrightarrow P^{\prime}, Q \longleftrightarrow Q^{\prime}$. 由 $P, Q, E, F$
共线, 有 $P^{\prime}, Q^{\prime}, E, F, I$ 共圆. 由反演的性质,

$$
\begin{aligned}
\angle D P A+\angle A Q D & =\angle A P I+\angle A Q I+\angle D P I+\angle D Q I \\
& =\angle P^{\prime} L I+\angle Q^{\prime} L I+\angle P^{\prime} D I+\angle Q^{\prime} D I=\angle P^{\prime} L Q^{\prime}+\angle P^{\prime} D Q^{\prime}
\end{aligned}
$$



再考虑以 $D$ 为反演中心, $D M \cdot D E$ 为反演幂的反演, 与 $\angle E D F$ 平分线为轴的轴反射变换的复合. 熟知 $M \longleftrightarrow E, N \longleftrightarrow F$. 由 $\triangle D I M \sim \triangle D E T$, $I \longleftrightarrow T$. 因此圆 $M N T \longleftrightarrow$ 圆 $E I F$. 因此 $P^{\prime} \longleftrightarrow Q^{\prime}$. 故 $\triangle D T Q^{\prime} \sim \triangle D P^{\prime} I$, $\triangle D T P^{\prime} \sim \triangle D Q^{\prime} I$. 因此

$$
\begin{aligned}
\angle A P D+\angle A Q D & =\angle P^{\prime} L Q^{\prime}+\angle P^{\prime} D Q^{\prime}=\angle P^{\prime} T Q^{\prime}+\angle P^{\prime} D Q^{\prime} \\
& =\angle P^{\prime} T D+\angle Q^{\prime} T D+\angle P^{\prime} D Q^{\prime} \\
& =\angle I Q^{\prime} D+\angle I P^{\prime} D+\angle P^{\prime} D Q^{\prime}=\angle P^{\prime} I Q^{\prime}=\angle P I Q .
\end{aligned}
$$

解 2. 设 $N, M, T$ 分别为 $\widehat{B A C}, \widehat{B C}, B C$ 中点. 设直线 $P Q, B C$ 交于 $L$. 延长 $N P, N Q$, 分别交直线 $B C$ 于 $P^{\prime}, Q^{\prime}$.

因为 $\angle F A E=\angle B M C, A B=A C, M B=M C$, 故 $\triangle B M C \sim \triangle F A E$.又 $\angle P A F=\angle P^{\prime} M B, \angle Q A E=\angle Q^{\prime} M C, \angle A F I=90^{\circ}=\angle M B N, \angle A E I=$ $90^{\circ}=\angle M C N$. 因此 $A, F, E, P, Q, I$ 与 $M, B, C, P^{\prime}, Q^{\prime}, N$ 相似. 特别地, $\angle P I Q=$ $\angle P^{\prime} M Q^{\prime}$.

由 $B, D, C, L$ 调和,

$$
L D \cdot L T=L C \cdot L B=L P \cdot L Q
$$

因此 $P, Q, D, T$ 共圆. 由 $\angle N Q Q^{\prime}=90^{\circ}=\angle N T Q^{\prime}$, 有 $N, T, Q, Q^{\prime}$ 共圆. 同理, $N, T, P, P^{\prime}$ 共圆. 于是

$$
\begin{aligned}
\angle D P A+\angle D Q A & =360^{\circ}-\angle P D Q-\angle P A Q=360^{\circ}-\angle P M Q-\angle P T Q \\
& =\angle T P M+\angle T Q M=\angle P^{\prime} N M+\angle Q^{\prime} N M=\angle P^{\prime} N Q^{\prime}=\angle P I Q
\end{aligned}
$$



解 3. 设 $N, M, T$ 分别为 $\widehat{B A C}, \widehat{B C}, B C$ 中点. 设直线 $P Q, B C$ 交于 $L$. $A N, P Q$ 交于 $R$. 由 $B, C ; D, L$ 调和,

$$
L D \cdot L T=L C \cdot L B=L P \cdot L Q
$$

因此 $P, Q, D, T$ 共圆. 由 $A M \perp A N, P Q \perp A N$, 有 $A M \| P Q$. 因此 $P M=$ $Q A$. 故

$$
\frac{M P}{A I}=\frac{Q A}{A I}=\frac{A R / \sin \angle A Q R}{A R / \cos ^{2} \angle F A I}=\frac{\cos ^{2} \angle B M N}{\sin \angle A Q R}=\frac{M T / M N}{A P / M N}=\frac{M T}{A P}
$$

又 $\angle P M T=\angle I A P$. 故 $\triangle P M T \sim \triangle I A P$. 因此 $\angle A P I=\angle P T M$. 同理, $\angle A Q I=\angle Q T M$. 于是

$$
\begin{aligned}
\angle D P A+\angle D Q A & =\angle A P I+\angle I P D+\angle A Q I+\angle I Q D \\
& =\angle P T M+\angle I P D+\angle Q T M+\angle I Q D \\
& =\angle P T Q+\angle I P D+\angle I Q D=\angle P D Q+\angle I P D+\angle I Q D=\angle P I Q .
\end{aligned}
$$



注. 我们还可以证明 $T, I$ 是 $\triangle N P Q$ 的等角共轭点.

解答 4. 设 $M, N, T$ 分别为 $\widehat{B A C}, \overparen{B C}, B C$ 中点, $R$ 为 $A$ 关于 $\triangle A B C$外接圆的对径点. 延长 $N D, P D, Q D$, 分别交 $\triangle A B C$ 外接圆于 $S, K, J$. 设直线 $P Q, B C$ 交于 $L$. 我们依次证明以下结论.

结论 1. $\angle A S I=90^{\circ}$.

结论 1 的证明. 因为 $S D$ 平分 $\angle B S C$, 故

$$
\frac{B F}{B S}=\frac{D B}{B S}=\frac{D C}{C S}=\frac{C E}{C S}
$$

又 $\angle F B S=\angle E C S$. 故 $\triangle S F B \sim \triangle S E C$. 因此 $\angle A F S=\angle A E S$, 即 $A, F, E, S$共圆. 又 $A, F, I, E$ 共圆且以 $A I$ 为直径. 故 $\angle A S I=90^{\circ}$. 结论 1 证毕.

结论 2. $Q, D, T, P$ 共圆, $J, T, D, K$ 共圆.

结论 2 的证明. 熟知地, $B, C ; D, L$ 调和. 故 $Q B, Q C ; Q D, Q L$ 调和. 故 $B, C ; J, P$调和. 故 $\angle P T B=\angle P C J=\angle P Q D$. 因此 $Q, D, T, P$ 共圆. 同理 $J, T, D, K$ 共圆. 结论 2 证毕.

结论 3. $L, K, J$ 共线, $L, S, M$ 共线.

结论 3 的证明. 对圆 $P T D Q$, 圆 $T D K J$, 圆 $J K Q P$ 由根心定理, 有直线 $J K, B C, P Q$ 共点 $L$. 对圆 $P T D Q$, 圆 $P Q S M$, 圆 $S M T D$ 由根心定理, 有直线 $M S, B C, P Q$ 共点 $L$. 结论 3 证毕.



结论 4. $\triangle S A P \sim \triangle S Q L, \triangle S A I \sim \triangle S D L$.

结论 4 的证明. 由于 $M A \perp A I, P Q \perp A I$, 故 $A M \| Q P$. 故 $\overparen{A P}=\overparen{M Q}$.因此 $\angle Q S L=\angle M P Q=\angle A S P$. 又 $\angle S Q L=\angle S A P$, 故 $\triangle S A P \sim \triangle S Q L$.由于 $\angle A S I=90^{\circ}=\angle D S L, \angle S D L=\angle S M T=\angle S A I$, 故 $\triangle S A I \sim \triangle S D L$.结论 4 证毕.

结论 5. $\triangle S I P \sim \triangle S Q D$.

结论 5 的证明. 由结论 $1, S, I, R$ 共线. 由于 $R N \perp A I, P Q \perp A I$,故 $R N \| Q P$. 故 $\overparen{N Q}=\overparen{P R}$. 故 $\angle N S Q=\angle P S R$. 又由结论 4,

$$
\frac{S P}{S I}=\frac{S P}{S L} \cdot \frac{S L}{S I}=\frac{S A}{S Q} \cdot \frac{S D}{S A}=\frac{S D}{S Q}
$$

因此 $\triangle S I P \sim \triangle S Q D$. 结论 5 证毕.

原命题的证明. 由结论 5 及旋转相似知 $\triangle S I Q \sim \triangle S P D$. 因此

$$
\begin{aligned}
\angle P I Q & =\angle S I P+\angle S I Q=\angle S Q D+\angle S P D \\
& =360^{\circ}-\angle P S Q-\angle P D Q=360^{\circ}-\angle P A Q-\angle P D Q \\
& =\angle A P D+\angle A Q D .
\end{aligned}
$$

注. 新星问题征解第八期第三题与本题十分相似, 其要证结论为

$$
\angle I P D-\frac{1}{2} B=\angle I Q D-\frac{1}{2} C,
$$

也可使用此方法证明. 此题是一个常见的几何构型.

解 5. 本解答中, 复平面上的点与其所对应复数用同一字母表示, 单位圆指圆 $|Z|=1$. 我们先证明复数法的几个基本结论.

引理 1. $W X, Y Z$ 是复平面单位圆上的两弦, 则他们的交点

$$
T=\frac{W X Y+W X Z-W Y Z-X Y Z}{W X-Y Z} .
$$

引理 $\mathbf{1}$ 的证明. 由 $W, X, T$ 共线, $\frac{W-T}{W-X} \in \mathbb{R}$. 故

$$
\frac{W-T}{W-X}=\overline{\left(\frac{W-T}{W-X}\right)}=\frac{\frac{1}{W}-\bar{T}}{\frac{1}{W}-\frac{1}{X}}=\frac{X W \bar{T}-X}{W-X} .
$$

因此 $W-T=X W \bar{T}-X$. 同理, $Y-T=Y Z \bar{T}-Z$. 联立两式, 解得

$$
T=\frac{W X Y+W X Z-W Y Z-X Y Z}{W X-Y Z} .
$$

引理 1 证毕.

引理 2. $X, Y, Z$ 是复平面单位圆上的三点, 满足

$$
0<\arg X<\arg Y<\arg Z<2 \pi
$$

三复数 $x, y, z$ 满足

$$
x^{2}=X, y^{2}=Y, z^{2}=Z, 0<\arg x<\arg z<\pi<\arg y<2 \pi .
$$

则 $\triangle X Y Z$ 的内心为

$$
I_{X Y Z}=-x y-y z-z x .
$$

引理 2 的证明. 设 $M, N$ 分别为不含 $X$ 的弧 $Y Z$,不含 $Y$ 的弧 $Z X$ 的中点. $M^{2}=Y Z$ 且 $\arg Y<\arg M<\arg Z$. 若 $M=y z$, 则有

$$
\arg M=\arg y+\arg z>\arg Z \text {, 或 } \arg M=\arg y+\arg z-2 \pi<\arg Y \text {, }
$$

矛盾! 故 $M=-y z$. 同理, $N=-z x$. 故由引理 1 ,

$$
\begin{aligned}
I_{X Y Z} & =\frac{X M Y+X M N-Y N X-Y N M}{X M-Y N} \\
& =\frac{x^{2}(-y z) y^{2}+x^{2}(-y z)(-z x)-y^{2}(-z x) x^{2}-y^{2}(-z x)(-y z)}{x^{2}(-y z)-y^{2}(-z x)} \\
& =-x y-y z-z x .
\end{aligned}
$$

引理 2 证毕.
引理 3. $X, Y$ 是复平面单位圆上的点, $Z$ 是复平面上的点. 则 $Z$ 在直线 $X Y$ 上的投影为

$$
H=\frac{1}{2}(X+Y+Z-X Y \bar{Z})
$$

引理 3 的证明. $X, H, Y$ 共线. 故由引理 1 的证明可得, $X-H=X Y \bar{H}-Y$.由于 $X Y \perp H Z$, 故 $\frac{H-Z}{X-Y}$ 是纯虚数. 因此

$$
0=\frac{H-Z}{X-Y}+\overline{\left(\frac{H-Z}{X-Y}\right)}=\frac{H-Z}{X-Y}+\frac{\bar{H}-\bar{Z}}{\frac{1}{X}-\frac{1}{Y}}=\frac{H-Z-X Y \bar{H}+X Y \bar{Z}}{X-Y} .
$$

因此, $H-Z-X Y \bar{H}+X Y \bar{Z}=0$. 联立两式, 解得

$$
H=\frac{1}{2}(X+Y+Z-X Y \bar{Z})
$$

引理 3 证毕.

原命题的证明. 以 $\triangle A B C$ 的外接圆圆心为原点, 半径为单位长, $\angle A O C$ 内一方向为实轴正方向建立复平面. 有 $0<\arg A<\arg B<\arg C<2 \pi$. 设复数 $a, b, c$ 满足

$$
a^{2}=A, b^{2}=B, c^{2}=C, 0<\arg a<\arg c<\pi<\arg b<2 \pi .
$$

有 $|a|=|b|=|c|=|P|=|Q|=1$. 故

$$
\bar{a}=\frac{1}{a}, \bar{b}=\frac{1}{b}, \bar{c}=\frac{1}{c}, \bar{P}=\frac{1}{P}, \bar{Q}=\frac{1}{Q} .
$$

由引理 $1, I=-a b-b c-c a$. 故由引理 2 ,

$$
\begin{aligned}
D & =\frac{1}{2}(B+C+I-B C \bar{I}) \\
& =\frac{1}{2}\left(b^{2}+c^{2}-a b-b c-c a+b^{2} c^{2}\left(\frac{1}{a}+\frac{1}{b}+\frac{1}{c}\right)\right) \\
& =\frac{1}{2}\left(b^{2}+c^{2}-a b-a c+\frac{b^{2} c}{a}+\frac{b c^{2}}{a}\right) .
\end{aligned}
$$

同理,

$E=\frac{1}{2}\left(a^{2}+c^{2}-a b-b c+\frac{a^{2} c}{b}+\frac{a c^{2}}{b}\right), F=\frac{1}{2}\left(a^{2}+b^{2}-a b-a c+\frac{a^{2} b}{c}+\frac{a b^{2}}{c}\right)$.

因此,

$$
\begin{aligned}
E-F & =\frac{1}{2}\left(c^{2}-b^{2}-a b+a c+\frac{a^{2} c}{b}-\frac{a^{2} b}{c}+\frac{a c^{2}}{b}-\frac{a b^{2}}{c}\right) \\
& =\frac{(c-b)(c+b)(a+b)(a+c)}{2 b c} .
\end{aligned}
$$

由于 $P, F, E$ 共线, 有 $\frac{P-E}{E-F} \in \mathbb{R}$. 因此 $\frac{P-E}{E-F}=\overline{\left(\frac{P-E}{E-F}\right)}$, 代入 $P, E, E-F$, 并注意
到 $(\star)$ 式,

$$
\frac{P-\frac{1}{2}\left(a^{2}+c^{2}-a b-b c+\frac{a^{2} c}{b}+\frac{a c^{2}}{b}\right)}{\frac{(c-b)(c+b)(a+b)(a+c)}{2 b c}}=\frac{\frac{1}{P}-\frac{1}{2}\left(\frac{1}{a^{2}}+\frac{1}{c^{2}}-\frac{1}{a b}-\frac{1}{b c}+\frac{b}{a^{2} c}+\frac{b}{a c^{2}}\right)}{-\frac{(c-b)(c+b)(a+b)(a+c)}{2 a^{2} b^{2} c^{2}}}
$$

所以

$P-\frac{1}{2}\left(a^{2}+c^{2}-a b-b c+\frac{a^{2} c}{b}+\frac{a c^{2}}{b}\right)+\frac{a^{2} b c}{P}=\frac{1}{2}\left(\frac{b}{c}+\frac{a^{2} b}{c}-a c-a^{2}+b^{2}+\frac{a b^{2}}{c}\right)$.

因此

$$
P^{2}-\frac{1}{2 b c}\left(a^{2}\left(b^{2}+c^{2}\right)+a\left(b^{3}-b^{2} c-b c^{2}+c^{3}\right)+b c\left(b^{2}+c^{2}\right)\right) P+a^{2} b c=0
$$

因此,

$$
\begin{aligned}
& (P-D)(P-I) \\
& =\left(P-\frac{1}{2}\left(b^{2}+c^{2}-a b-a c+\frac{b^{2} c}{a}+\frac{b c^{2}}{a}\right)\right)(P+a b+b c+c a) \\
& =P^{2}-\frac{1}{2}\left(b^{2}+c^{2}-3 a b-3 a c-2 b c+\frac{b^{2} c}{a}+\frac{b c^{2}}{a}\right) P \\
& -\frac{1}{2}(a b+b c+c a)\left(b^{2}+c^{2}-a b-a c+\frac{b^{2} c}{a}+\frac{b c^{2}}{a}\right) \\
& =\frac{1}{2 b c}\left(a^{2}\left(b^{2}+c^{2}\right)+a\left(b^{3}-b^{2} c-b c^{2}+c^{3}\right)+b c\left(b^{2}+c^{2}\right)\right) P-a^{2} b c \\
& -\frac{1}{2}\left(b^{2}+c^{2}-3 a b-3 a c-2 b c+\frac{b^{2} c}{a}+\frac{b c^{2}}{a}\right) P \\
& -\frac{1}{2}(a b+b c+c a)\left(b^{2}+c^{2}-a b-a c+\frac{b^{2} c}{a}+\frac{b c^{2}}{a}\right) \\
& =\frac{a b^{2}+a c^{2}+b^{2} c+b c^{2}}{2 a b c}\left(\left(a^{2}+a b+a c-b c\right) P+\left(a^{2}-a b-a c-b c\right) b c\right) .
\end{aligned}
$$

同理,

$$
\begin{aligned}
& (Q-D)(Q-I) \\
= & \frac{a b^{2}+a c^{2}+b^{2} c+b c^{2}}{2 a b c}\left(\left(a^{2}+a b+a c-b c\right) Q+\left(a^{2}-a b-a c-b c\right) b c\right) .
\end{aligned}
$$

故

$$
\begin{aligned}
& \frac{(P-D)(P-I)(Q-A)}{(Q-D)(Q-I)(P-A)} \\
= & \frac{\left(\left(a^{2}+a b+a c-b c\right) P+\left(a^{2}-a b-a c-b c\right) b c\right)\left(Q-a^{2}\right)}{\left(\left(a^{2}+a b+a c-b c\right) Q+\left(a^{2}-a b-a c-b c\right) b c\right)\left(P-a^{2}\right)},
\end{aligned}
$$

注意到 $(\star)$ 式, 以及 $-a^{2} b c \overline{\left(a^{2}+a b+a c-b c\right)}=a^{2}-a b-a c-b c$, 从而容易验证上式与其共轭相等. 因此 $\frac{(P-D)(P-I)(Q-A)}{(Q-D)(Q-I)(P-A)} \in \mathbb{R}$. 故

$$
\arg \frac{A-P}{D-P}+\arg \frac{D-Q}{A-Q}=\arg \frac{P-I}{Q-I}
$$

即有 $\angle D P A+\angle A Q D=\angle Q I P$. 证毕.

G 7. 锐角不等边三角形 $A B C$ 的内切圆为 $\omega$, 其圆心为 $I . \omega$ 分别与三边 $B C, C A, A B$ 切于点 $D, E, F$. 过 $D$ 垂直 $E F$ 的直线与 $\omega$ 再次交于 $R$. 直线 $A R$ 再次交 $\omega$ 于 $P . \triangle P C E$ 和 $\triangle P B F$ 的外接圆再次交于 $Q$. 证明: 直线 $D I$和 $P Q$ 的交点在角 $B A C$ 的外角平分线上.



解 1. 本解答中, 复平面上的点与其所对应复数用同一字母表示, 单位圆指圆 $|Z|=1$. 我们先证明复数法的几个基本结论.

引理 1. $X$ 是复平面单位圆上的点, $T$ 是复平面上不在X处切线上的一点.则直线 $X T$ 与单位圆的非 $X$ 的交点为

$$
Y=\frac{T-X}{1-X \bar{T}}
$$

引理 1 的证明. 由 $\mathrm{G} 6$ 引理 1 的证明, $X-T=X Y \bar{T}-X$, 即解得上式.引理 2 证毕.

引理 2. $X, Y$ 是复平面单位圆上的两点. 则单位圆的过它们的切线的交点为

$$
T=\frac{2 X Y}{X+Y}
$$

引理 $\mathbf{2}$ 的证明. 由 $X O \perp X T$, 有 $\frac{T-X}{X}$ 为纯虚数. 故

$$
0=\frac{T-X}{X}+\overline{\left(\frac{T-X}{X}\right)}=\frac{T-X}{X}+\frac{T-\frac{1}{X}}{\frac{1}{X}}=\frac{T-X}{X}+X T-1 .
$$

因此 $X^{2} \bar{T}+T=2 X$. 同理, $Y^{2} \bar{T}+T=2 Y$. 两式联立, 解得

$$
T=\frac{2 X Y}{X+Y}
$$

引理 3 证毕.

注. 事实上, 这是 G6 引理 1 中 $W=X, Y=Z$ 的特殊情况.

引理 3. $W X, Y Z$ 是复平面单位圆上的两条互相垂直的弦. 则 $W X+Y Z=$ 0.

引理 3 的证明. $\frac{W-X}{Y-Z}$ 为纯虚数. 故 $0=\frac{W-X}{Y-Z}+\overline{\left(\frac{W-X}{Y-Z}\right)}=\frac{W-X}{Y-Z}+\frac{Y Z(X-W)}{W X(Z-Y)}=\frac{(X-W)}{W X(Z-Y)}(W X+Y Z)$.即有 $W X+Y Z=0$. 引理 4 证毕.

引理 4. $a \in \mathbb{C}^{*}, b \in \mathbb{R}$. 则满足 $\bar{a} Z+a \bar{Z}+b=0$ 的点在一条直线上.

引理 4 的证明. 取 $Z_{0}=-\frac{b}{2 \bar{a}}$, 有 $\bar{a} Z_{0}+a \overline{Z_{0}}+b=0$. 与原方程相减, 同时除以 $i a \bar{a}$,得

$$
\frac{Z-Z_{0}}{i a}=\overline{\left(\frac{Z-Z_{0}}{i a}\right)} \text {, 即 } \frac{Z-Z_{0}}{i a} \in R \text {. }
$$

故对于原方程上任意一点 $Z, Z Z_{0} \| O X$, 在同一条直线上, 其中 $X=i a$. 引理 5 证毕.

原命题的证明. 以 $\omega$ 的圆心为原点, 半径为单位长建立复平面. 有 $|D|=$ $|E|=|F|=|P|=1$. 故

$$
\bar{D}=\frac{1}{D}, \bar{E}=\frac{1}{E}, \bar{F}=\frac{1}{F}, \bar{P}=\frac{1}{P}
$$

由引理 3 和引理 4 , 有

$$
R=-\frac{E F}{D}, A=\frac{2 E F}{E+F}, B=\frac{2 D F}{D+F}, C=\frac{2 D E}{D+E} .
$$

故由引理 2,

$$
P=\frac{A-R}{1-A R}=\frac{E F(2 D+E+F)}{D E+D F+2 E F} .
$$

由于 $P, E, C, Q$ 共圆, 故由 $\mathrm{G} 2$ 的引理 $2, \frac{(Q-P)(C-E)}{(Q-C)(P-E)} \in \mathbb{R}$. 由于 $I E \perp C E$, $\frac{E}{C-E}$ 是纯虚数. 因此 $\frac{(Q-P) E}{(Q-C)(P-E)}$ 是纯虚数. 代入 $C$, 并注意到 $(\star)$ 式,

$$
0=\frac{(Q-P) E}{(Q-C)(P-E)}+\overline{\left(\frac{(Q-P) E}{(Q-C)(P-E)}\right)}
$$

$$
=\frac{(Q-P) E}{\left(Q-\frac{2 D E}{D+E}\right)(P-E)}+\frac{\left(\bar{Q}-\frac{1}{P}\right) \frac{1}{E}}{\left(\bar{Q}-\frac{2}{D+E}\right) \frac{E-P}{E P}} .
$$

消去 $E-P$, 并代入 $P$, 整理得

$$
\begin{aligned}
& E\left(Q-\frac{E F(2 D+E+F)}{D E+D F+2 E F}\right)\left(\bar{Q}-\frac{2}{D+E}\right) \\
& \quad=\left(Q-\frac{2 D E}{D+E}\right)\left(\frac{E F(2 D+E+F)}{D E+D F+2 E F} \bar{Q}-1\right)
\end{aligned}
$$

通分移项, 按 $Q$ 整理, 得到

$$
\begin{aligned}
E(D+F) & (D+E)(F-E) Q \bar{Q}+(E-D)(D E+D F+2 E F) Q \\
+ & E^{2} F(E-D)(E+F+2 D) \bar{Q}+2 E(E+F)\left(D^{2}-E F\right)=0
\end{aligned}
$$

记上式左边为 $f(Q)$. 从 $(\star \star)$ 式容易看出 $f(P)=0$. 同理, 若记

$$
\begin{aligned}
g(Q)= & F(D+F)(D+E)(E-F) Q \bar{Q}+(F-D)(D E+D F+2 E F) Q \\
& +E F^{2}(F-D)(E+F+2 D) \bar{Q}+2 F(E+F)\left(D^{2}-E F\right)
\end{aligned}
$$

则有 $g(P)=g(Q)=0$. 记

$$
\begin{aligned}
h(Z)= & E f(Z)+F g(Z) \\
= & (D E+D F-2 E F)(D E+D F+2 E F) Z \\
& -E^{2} F^{2}(E+F-2 D)(E+F+2 D) \bar{Z}+4 E F(E+F)\left(E F-D^{2}\right) .
\end{aligned}
$$

注意到

$$
\begin{aligned}
& \frac{(D E+D F-2 E F)(D E+D F+2 E F)}{4 E F(E+F)\left(E F-D^{2}\right)} \\
& =\overline{\left(\frac{-E^{2} F^{2}(E+F-2 D)(E+F+2 D)}{4 E F(E+F)\left(E F-D^{2}\right)}\right)},
\end{aligned}
$$

故由引理 5 , 满足 $h(Z)=0$ 的点在一条直线上. 而 $h(P)=h(Q)=0$. 故这条直线即直线 $P Q$.

记过 $A$ 且垂直于 $A I$ 的直线与直线 $D I$ 的交点为 $X$, 由 $D, I, X$ 共线, 有 $\frac{X}{D} \in$ $\mathbb{R}$. 故

$$
\frac{X}{D}=\overline{\left(\frac{X}{D}\right)}=D \bar{X}
$$

由 $A X \perp A I$, 有 $\frac{X-A}{A}$ 为纯虚数. 故

$$
\begin{aligned}
0 & =\frac{X-A}{A}+\overline{\left(\frac{X-A}{A}\right)}=\frac{X}{A}+\frac{\bar{X}}{\bar{A}}-2=\frac{E+F}{2 E F} X+\frac{E+F}{2} \bar{X}-2 \\
& =\frac{E+F}{2 E F} X+\frac{E+F}{2} \frac{X}{D^{2}}-2=\frac{(E+F)\left(E F+D^{2}\right)}{2 E F D^{2}} X-2 .
\end{aligned}
$$

故

$$
X=\frac{4 E F D^{2}}{(E+F)\left(E F+D^{2}\right)}
$$

所以

$$
\begin{aligned}
h(X)= & (D E+D F-2 E F)(D E+D F+2 E F) \frac{4 E F D^{2}}{(E+F)\left(E F+D^{2}\right)} \\
& -E^{2} F^{2}(E+F-2 D)(E+F+2 D) \frac{4 E F}{(E+F)\left(E F+D^{2}\right)} \\
& +4 E F(E+F)\left(E F-D^{2}\right) \\
= & \frac{4 E F}{(E+F)\left(E F+D^{2}\right)}\left(D^{2}\left(D^{2}(E+F)^{2}-4 E^{2} F^{2}\right)\right. \\
& \left.-E^{2} F^{2}\left((E+F)^{2}-4 D^{2}\right)\right)+4 E F(E+F)\left(E F-D^{2}\right) \\
= & \frac{4 E F}{(E+F)\left(E F+D^{2}\right)}\left(D^{4}(E+F)^{2}-E^{2} F^{2}(E+F)^{2}\right) \\
& +4 E F(E+F)\left(E F-D^{2}\right) \\
= & 0 .
\end{aligned}
$$

故 $X$ 在直线 $P Q$ 上.

解 2. 设直线 $D I$ 与过 $A$ 且垂直于 $A I$ 的直线交点为 $X$, 与 $\omega$ 再次交于 $K$; $X P, A D$ 分别与 $\omega$ 再次交于 $U, V$, 直线 $U E$ 与圆 $P C E$ 再次交于 $L$. 我们先证明两个结论.

结论 1. $U V \| E F$.

结论 1 的证明. 由 $K R \perp A D, A D \perp E F, E F \perp A I, A I \perp A X$,有 $K R \| A X$. 因此 $\angle A X D=\angle R K D=180^{\circ}-\angle A P D$, 从而 $A, X, P, D$ 共圆.因此 $\angle A X P=\angle A D P=\angle V U P$. 故 $U V\|A X\| E F$. 结论 1 证毕.

结论 2. $\triangle L U P \sim \triangle C E P$.

结论 2 的证明. $\angle U L P=\angle E C P, \angle L U P=\angle C E P$. 结论 2 证毕.

原命题的证明. 我们只需证明 $U$ 在圆 $P C E$ 和圆 $P B F$ 的根轴上. 由结论 $2, U$ 关于圆 $P C E$ 的幂为

$$
U E \cdot U L=U E \cdot \frac{C E \cdot P U}{P E}=\frac{U E \cdot C E \cdot P U}{P E} .
$$

同理, $U$ 关于圆 $P B F$ 的幂为 $\frac{U F \cdot B F \cdot P U}{P F}$. 因此我们只需证明

$$
\frac{U E \cdot C E}{P E}=\frac{U F \cdot B F}{P F} .
$$

而

$$
\frac{C E}{B F}=\frac{r / \tan \frac{C}{2}}{r / \tan \frac{B}{2}}=\frac{\tan \frac{B}{2}}{\tan \frac{C}{2}}
$$

其中 $r$ 为 $\omega$ 半径; 由 $E D F V$ 调和及结论 1 ,

$$
\frac{U E}{U F}=\frac{V F}{V E}=\frac{D F}{D E}=\frac{\sin \angle D E F}{\sin \angle D F E}=\frac{\cos \frac{B}{2}}{\cos \frac{C}{2}}
$$

由 $R E P F$ 调和,

$$
\frac{P F}{P E}=\frac{R F}{R E}=\frac{\sin \angle F D R}{\sin \angle E D R}=\frac{\cos \angle D E F}{\cos \angle D F E}=\frac{\sin \frac{B}{2}}{\sin \frac{C}{2}} .
$$

故 $(\star)$ 式成立.



解 3. 设直线 $D I$ 与过 $A$ 且垂直于 $A I$ 的直线交点为 $X$, 与 $\omega$ 再次交于 $K$; $A I$ 交 $E F$ 于 $J, D J$ 的延长线交圆 $I$ 于 $U$. 我们依次证明以下几个结论.

结论 1. $P, J, K$ 共线.

结论 1 的证明. 由 $A J \cdot A I=A F^{2}=A R \cdot A P$, 有 $R, J, I, P$ 共圆. $I R=I P$ , 故 $\overparen{I P}=\overparen{I R}$. 因此 $\angle I J P=\angle A J R$. 由 $K R \perp R D, R D \perp E F$, 有 $E F \perp A I$.故 $K R \perp A I$. 因此 $\angle A J K=\angle A J R=\angle I J P$. 因此 $P, J, K$ 共线.

结论 2. $P, U, X$ 共线.

结论 2 的证明. 由 $A X \perp A I$, 有 $A X$ 是 $J$ 关于圆 $I$ 的极线. 而 $D U, P K$ 为过 $J$ 的圆 $I$ 的两割线, 故直线 $D K, P U$ 交点在 $A X$ 上, 即为 $X$. 结论 2 证毕.

结论 3. $B, I, Q, C$ 共圆. 记这个圆为 $\Gamma$.
结论 3 的证明.

$$
\begin{aligned}
\angle B Q C & =\angle B Q P+\angle C Q P=\angle B F P+\angle C E P=\angle F E P+\angle E F P \\
& =180^{\circ}-\angle F P E=180^{\circ}-\angle F D E=90^{\circ}+\frac{A}{2}=\angle B I C .
\end{aligned}
$$

结论 3 证毕.

结论 4. 设直线 $P Q$ 交 $\Gamma$ 于 $S, I S \| K P$.

结论 4 的证明. $\angle B I S=\angle B Q S=\angle B F P=\angle F K P$. 又由 $B I \perp F D$, $F K \perp F D$, 有 $B I \| F K$. 因此 $I S \| K P$. 结论 4 证毕.

结论 5. $U, I, D, S$ 共圆.

结论 5 的证明. 设 $U D$ 交 $I S$ 于 $M, B I$ 交 $F D$ 于 $Y, C I$ 交 $D E$ 于 $Z$ (未标出). 由结论 4, 结合 $I$ 为 $D K$ 中点, 有 $I M$ 为 $\triangle D K J$ 的中位线. 故 $M$ 为 $D J$中点. 因此 $M$ 在 $\triangle D E F$ 中位线 $Y Z$ 上. 而 $Y$ 为 $\omega, \Gamma$, 圆 BFID 的根心, $Z$为 $\omega, \Gamma$, 圆 $C E I D$ 的根心. 故 $Y Z$ 是 $\omega$ 和 $\Gamma$ 的根轴. 因此 $M U \cdot M D=M I \cdot M S$.故 $U, I, D, S$ 共圆. 结论 5 证毕.

原命题的证明. 由结论 4 和结论 $5, \angle D U S=\angle D I S=\angle D K P=\angle D U P$.故 $P, U, S$ 共线. 因此 $X, U, Q, P, S$ 共线.


解 4. 作 $\triangle A B C$ 的外接圆圆 $O$. 设 $M, N$ 分别为 $\widehat{B A C}, \widehat{B C}$ 中点. 延长 $N I$ , 交圆 $O$ 于 $T$, 交 $\triangle B I C$ 的外接圆圆 $M$ 于 $S$. 由 $M T \perp I S$, 有 $T$ 是 $I S$ 中点.我们依次证明以下几个结论.

结论 1. $Q$ 在圆 $M$ 上. 即解答 2 结论 3 .

结论 2. $A, F, E, I, R, P$ 与 $N, B, C, M, I, S$ 相似.

结论 2 的证明. 由 $\angle F A E=\angle B N C, A F=A E, N B=N C, \triangle A F E \sim$ $\triangle N B C$. 由 $A F \perp F I, A E \perp E I, N B \perp B M, N C \perp C M$, 故 $N, M$在相似的对应位置. $\angle F E R=\angle F D R=90^{\circ}-\angle D F E=\frac{C}{2}=\angle B C I$, 同理, $\angle E F R=\angle C B I$. 因此 $\triangle F R E \sim \triangle B I C$, 即 $R, I$ 在相似的对应位置. 而 $P$是 $A R$ 延长线与圆 $I$ 的交点, $S$ 是 $N I$ 延长线与圆 $M$ 的交点. 故 $P, S$ 在相似的对应位置. 结论 2 证毕.

结论 3. $T$ 在直线 $A R P$ 上.

结论 3 的证明. 由结论 $2, \angle F A R=\angle B N I=\angle B N T=\angle B A T$, 即 $A, R, T$共线. 结论 3 证毕.

结论 4. $S, P, Q$ 共线.

结论 4 的证明. 由结论 $2, \angle S Q B=180^{\circ}-\angle N I B=180^{\circ}-\angle A R F=$ $\angle F R P=\angle B F P=\angle B Q P$, 即 $S, P, Q$ 共线. 结论 4 证毕.

结论 5. IT 平分 $\angle P I D$.

结论 5 的证明. 由结论 $2, \angle P I D=\angle F I P-\angle F I D=2 \angle F R P-$ $\left(180^{\circ}-B\right)=2 \angle B I T-2 \angle B I D=2 \angle D I T$. 结论 5 证毕.

原命题的证明. 延长 $P Q$ 交 $A N$ 于 $X$. 由 $I D \| M N$, 我们只需证明 $X I \|$ $M N$. 而

$$
\begin{aligned}
\frac{A X}{X N} & =\frac{A P \sin \angle A P X / \sin \angle A X P}{N S \sin \angle N S X / \sin \angle N X S}=\frac{A P \sin \angle A P X}{N S \sin \angle N S X}=\frac{A P \sin \angle T P S}{N S \sin \angle T S P} \\
& =\frac{A P}{N S} \cdot \frac{T S}{T P}=\frac{P R}{S I} \cdot \frac{\frac{1}{2} S I}{T P}=\frac{P R}{2 T P}=\frac{1}{2} \cdot \frac{I P \sin \angle P I R / \sin \angle P R I}{I P \sin \angle P I T / \sin \angle P T I} \\
& =\frac{1}{2} \cdot \frac{\sin \angle P I R \sin \angle P T I}{\sin \angle P I T \sin \angle P R I}=\frac{1}{2} \cdot \frac{\sin \angle S M I \sin \angle A T I}{\sin \angle D I T \sin \angle M I S} \\
& =\frac{1}{2} \cdot \frac{\sin \left(180^{\circ}-2 \angle M I S\right) \sin \angle A T I}{\sin \angle T N M \sin \angle M I S}=\cos \angle M I S \cdot \frac{\sin \angle A T I}{\sin \angle T A I} \\
& =\cos \angle M I T \cdot \frac{A I}{T I}=\frac{A I}{I M},
\end{aligned}
$$

即得 $X I \| M N$.



注. 这个题如果结论掌握的多, 可以纯几何做出, 但笔者比较倾向于复数计算.

G 8. 令 $\mathcal{L}$ 为平面上所有直线的集合. 设 $f$ 是一个映射, 它将每条直线 $\ell \in \mathcal{L}$映到 $\ell$ 上的一个点 $f(\ell)$ ，且对任意点 $X$ 和过点 $X$ 的三条直线 $\ell_{1}, \ell_{2}, \ell_{3}$ ，四点 $f\left(\ell_{1}\right), f\left(\ell_{2}\right), f\left(\ell_{3}\right), X$ 共圆. 证明: 存在唯一的点 $P$, 使得对于任意过 $P$ 的直线 $\ell, f(\ell)=P$.

解答. 若平面上的 $P, P^{\prime}$ 满足条件, 则 $P=f\left(P P^{\prime}\right)=P^{\prime}$. 因此至多一个满足条件的 $P$. 下面证明满足条件的 $P$ 的存在性. 先证明以下两个结论.

结论 1. 对每个点 $Z$, 存在一个过该点的圆, 使得对于任意过该点的直线在 $f$ 下的像在圆上. 称这个圆为该点的伴随圆, 记为 $c_{Z}$.

结论 1 的证明. 对于任意一个点 $Z$, 考虑过 $Z$ 的所有直线在 $f$ 下的像构成的集合 $\mathcal{H}$, 若 $\mathcal{H}$ 除了 $Z$ 外有至多一个点, 则显然 $Z$ 的伴随圆存在. 否则取 $\mathcal{H}$
中非 $Z$ 的两点 $X, Y$. 由条件, $\mathcal{H}$ 中任一点与 $X, Y, Z$ 共圆. 于是过 $X, Y, Z$ 的圆是 $Z$ 的伴随圆. 结论 1 证毕.

结论 2. 对于任意两个不同的点, 它们的伴随圆有一个交点在它们的所连直线上.

结论 2 的证明. 考虑两个点连线在 $f$ 下的像, 它在两个点连线上, 也在两个伴随圆上. 结论 2 证毕.

原命题存在性的证明. 我们用两种方法证明.

方法 1. 对平面上的点 $X, Y$, 记 $s(X, Y)$ 为 $c_{X}, c_{Y}$ 非 $f(X Y)$ 的交点 (若两圆相切则令 $s(X, Y)=f(X Y))$. 由 Miquel定理容易得到下面的结论 3 .

结论 3. 对不共线的三点 $X, Y, Z$, 若 $f(X, Y) \neq X, Y, f(Y, Z) \neq Y, Z$, $f(Z, X) \neq Z, X$, 则 $s(X, Y)=s(Y, Z)=s(Z, X)$.



对直线 $\ell \in \mathcal{L}$, 取其上不同的六点 $Y_{1}, \cdots, Y_{6}$. 取不在 $\ell$ 和任一 $c_{Y_{i}}$ 上的点 $X$. 不妨设 $Y_{1}, \cdots, Y_{4}$ 不在 $c_{X}$ 上. 由结论 3 , 对任意 $1 \leqslant i<j \leqslant 4$, $s\left(Y_{i}, Y_{j}\right), s\left(X, Y_{i}\right)$ 相同, 记为点 $O$.

对过 $O$ 的点 $\ell^{\prime}$, 若 $\ell^{\prime}=\ell$, 由 $f\left(\ell^{\prime}\right)$ 在 $\ell, c_{Y_{1}}, c_{Y_{2}}$ 上, 有 $f\left(\ell^{\prime}\right)=O$. 若 $\ell^{\prime} \neq \ell$ , 对 $\ell^{\prime}$ 上的非 $O$ 且不在任一 $c_{Y_{i}}$ 和 $\ell$ 上的任意一点 $X^{\prime}$ (这样的点有无穷多个),不妨 $Y_{1}, Y_{2}$ 不在 $c_{X^{\prime}}$ 上. 对 $X^{\prime}, Y_{1}, Y_{2}$ 由结论 3, $s\left(X^{\prime}, Y_{1}\right)=O$. 故 $O$ 在 $c_{X^{\prime}}$ 上.而 $f\left(\ell^{\prime}\right)$ 在 $c_{X^{\prime}}$ 和 $\ell^{\prime}$ 上, 故 $f\left(\ell^{\prime}\right)=O$ 或 $X^{\prime}$. 由 $X^{\prime}$ 的任意性, $f\left(\ell^{\prime}\right)=O$. 故 $O$满足条件.

方法 2. 反设过任一点 $U$ 都存在一条直线, 使其在 $f$ 下的像不是 $U$. 任取一点 $A$, 设过 $A$ 的直线 $\ell_{T}$ 使 $f\left(\ell_{T}\right)=T \neq A$. 在 $l_{T}$ 上取一点 $B \neq T$. 由结论 2 , $c_{A}, c_{B}$ 均过 $T$. 设两圆另一交点为 $P$ (若两圆相切则令 $P=T$ ).

假设存在过 $P$ 且不过 $A, B$ 的直线 $\ell$, 使 $f(\ell)=Q \neq P$. 记 $\mathcal{K}$ 为 $\ell$ 上满足 $X \neq P, Q, A, B$, 且 $X A$ 不与 $c_{A}$ 相切, $X B$ 不与 $c_{B}$ 相切的点 $X$ 的集合. $\mathcal{K}$ 为
无限集. 对 $X \in \mathcal{K}$, 设 $X A$ 与 $c_{A}$ 再次交于 $A_{1}, X B$ 与再次 $c_{B}$ 交于 $B_{1}$. 对 $A, X$由结论 $2, c_{X}$ 过 $A_{1}$ 或 $A$; 对 $B, X$ 由结论 $2, c_{X}$ 过 $B_{1}$ 或 $B$. 又由伴随圆的定义, $c_{X}$ 过 $Q, X$. 下分四种情况讨论, 以 $\measuredangle$ 表示有向角.

情况一: $c_{X}$ 过 $Q, X, A, B$. 则 $X$ 在圆 $Q A B$ 的圆上, 只有至多一个 $X \in \mathcal{K}$满足.

情况二: $c_{X}$ 过 $Q, X, A_{1}, B_{1}$ 共圆. 则 $\measuredangle X A_{1} P=\measuredangle A A_{1} P=\measuredangle A T P=$ $\measuredangle B T P=\measuredangle B B_{1} P=\measuredangle X B_{1} P$. 因此 $P, X, A_{1}, B_{1}$ 共圆. 矛盾! 故没有满足条件的 $X$.

情况三: $c_{X}$ 过 $Q, X, A_{1}, B$ 共圆. 则 $\measuredangle A A_{1} B=\measuredangle X A_{1} B=\measuredangle X Q B$ 是定角.故 $A_{1}$ 在过 $A, B$ 的一定圆上. 故 $A_{1}$ 为定点. 因此只有至多一个 $X \in \mathcal{K}$ 满足.

情况四: $c_{X}$ 过 $Q, X, B_{1}, A$ 共圆. 与情况三同理, 只有至多一个 $X \in \mathcal{K}$ 满足.

综上, 只有有限个 $X \in \mathcal{K}$. 矛盾! 故对于任意的过 $P$ 且不过 $A, B$ 的直线 $\ell$, $f(\ell)=P$.

取 $\ell_{T}$ 上一点 $C \neq A, B, T$, 由结论 2, 有 $c_{C}$ 过 $T$. 由上, $f(C P)=P$. 故 $c_{C}$过 $P$. 对点 $A, C$ 作上面的讨论，同理知 $f(B P)=P$; 对点 $B, C$ 同作上面的讨论, 同理知 $f(A P)=P$. 因此对任意过 $P$ 的直线 $\ell, f(\ell)=P$. 矛盾! 故存在满足条件的点 $P$.



注. 非常非常有新意的题目.

## III. 数论

N 1. 求所有正整数对 $(m, n)$ 满足

$$
\left(2^{n}-2^{0}\right)\left(2^{n}-2^{1}\right)\left(2^{n}-2^{2}\right) \ldots\left(2^{n}-2^{n-1}\right)=m !
$$

解. 对 $n \leq 5$ 逐一验证, 得到解 $(m, n)=(1,1),(3,2)$. 若 $n \geq 6$, 那么就有 $v_{2}(m !)=\frac{n(n-1)}{2}$.

而我们有

$$
v_{2}(m !)=\sum_{k=1}^{\infty}\left\lfloor\frac{m}{2^{k}}\right\rfloor \leq \sum_{k=1}^{\infty} \frac{m}{2^{k}}=m
$$

于是 $m \geq \frac{n(n-1)}{2}$. 进而

$$
m ! \geq\left(\frac{n(n-1)}{2}\right) ! \geq 7 ! \cdot 8^{\frac{n(n-1)}{2}-7} \geq 2^{\frac{3}{2}\left(n^{2}-n-6\right)} .
$$

这里我们用到了 $7 !>2^{12}$. 但由等式, $m !<2^{n^{2}}$. 所以

$$
\frac{3}{2}\left(n^{2}-n-6\right)<n^{2} \Longrightarrow(n-6)(n+3)<0 \Longrightarrow n<6 \text {. }
$$

矛盾. 故全体解为 $(m, n)=(1,1),(3,2)$.

注. 考察 2 的幂次是直接的. 也可以考察 3 的幂次. 考察别的素数幂次或许也可以做, 方法应该不少.

N 2. 求所有的正整数组 $(a, b, c)$ 使得 $a^{3}+b^{3}+c^{3}=(a b c)^{2}$.

解 1 . 不妨设 $a \geq b \geq c$. 把等式写成

$$
a^{2}\left(b^{2} c^{2}-a\right)=b^{3}+c^{3} .
$$

如果 $b^{2} c^{2}-a \geq 2 b$, 就有

$$
a^{2}\left(b^{2} c^{2}-a\right) \geq 2 b^{3} \geq b^{3}+c^{3} .
$$

由此推出 $a=b=c$, 因此 $b^{3}=3$, 不可能. 所以 $b^{2} c^{2}-a<2 b$. 由此得到

$$
2 b^{3} \geq b^{3}+c^{3} \geq a^{2}>\left(b^{2} c^{2}-2 b\right)^{2} \Longrightarrow 2 b \geq\left(b c^{2}-2\right)^{2}
$$

这里我们用到了 $b^{2} c^{2}-2 b \geq 0$, 否则 $b=c=1, a^{3}+2=a^{2}$ 无整数解.

于是 $b c^{2}-2 \leq 2 b$, 如果 $c \geq 2$, 就有 $2 b \leq 2, b \leq 1$, 矛盾. 所以 $c=1$. 那么有

$$
2 b \geq(b-2)^{2} \Longrightarrow b \leq 3
$$

分别可以得到 $b=1$ 时, $a^{3}+2=a^{2}$ 无整数解. 当 $b=2$ 时, $a^{3}+9=4 a^{2}$, 得到 $a=3$. 而 $b=3$ 时, $a^{3}+28=9 a^{2}$, 得到 $a=2$, 与 $a \geq b$ 相矛盾.
综上, 全体解为 $(1,2,3)$ 的任意排列.

解 2 . 仍设 $a \geq b \geq c$. 有

$$
a^{2} b^{2} c^{2}=a^{3}+b^{3}+c^{3} \leq 3 a^{3} \Longrightarrow 3 a \geq b^{2} c^{2}
$$

那么由于 $a^{2} \mid a^{2} b^{2} c^{2}=a^{3}+b^{3}+c^{3}$, 得到 $b^{3}+c^{3} \geq a^{2}$. 于是有 $18 b^{3} \geq 9 b^{3}+9 c^{3} \geq$ $b^{4} c^{4}$. 即 $c^{4} b \leq 18 \Longrightarrow c^{5} \leq 18$. 所以 $c=1,9 b^{3}+9 \geq b^{4}$. 推出 $b \leq 9$. 此外, $b^{3}+1$ 还要被大于 $b$ 的一个整数的平方整除. 经过验算, 在 $3 \leq b \leq 9$ 的范围内没有这样的数. 于是只有解 $(1,2,3)$ 及其排列.

注. $b^{3}+1=(b+1)\left(b^{2}-b+1\right)$ 可以帮助分解质因数. 运算量已经在可以接受的范围. 也可以进一步缩小 $b$ 的范围.

N 3. 对一个整数集合 $S$, 如果对任意正整数 $n$ 和 $a_{0}, a_{1}, \ldots, a_{n} \in S$, 多项式 $a_{0}+a_{1} x+\cdots+a_{n} x^{n}$ 的整数根也都在 $S$ 中, 那我们称 $S$ 为根深蒂固的. 求所有的根深蒂固的整数集 $S$, 满足 $S$ 包含全体形如 $2^{a}-2^{b}$ 的数 ( $a, b$ 是正整数).

解. 显然 $S=\mathbb{Z}$ 是成立的. 下面证明是 $S$ 唯一的.

首先, 因为 $2,-2 \in S$, 所以 $2 x-2=0$ 的根 $1 \in S$. 也有 $0 \in S$. 若 $n \in S$,那么 $x+n=0$ 的根 $-n \in S$. 所以只要证明自然数都在 $S$ 中即可.

现在假设 $0,1, \ldots, n-1 \in S . n \geq 3$. 设 $n=2^{k} t, k$ 是一个自然数, $t$ 是一个奇数. 那么由欧拉定理, 就有

$$
t\left|2^{\varphi(t)}-1 \Longrightarrow 2^{k} t\right| 2^{k+1+\varphi(t)}-2^{k+1} \in S .
$$

所以存在正整数 $N \in S$ 使得 $n \mid N$. 我们把 $N$ 写成 $n$ 进制表示. 即

$$
N=a_{r} n^{r}+a_{r-1} n^{r-1}+\cdots+a_{1} n+a_{0}\left(a_{r} \neq 0\right) .
$$

那么 $n \mid N$ 表明 $a_{0}=0$. 而 $-N \in S$, 所以下面关于 $x$ 的方程的系数都在 $S$ 中

$$
a_{r} x^{r}+a_{r-1} x^{r-1}+\cdots+a_{1} x-N=0 .
$$

它有解 $x=n$, 所以 $n \in S$. 命题对 $n$ 成立. 由归纳原理知, $S=\mathbb{Z}$.

注. 这里构造被 $n$ 整除的数时用到了 $2^{k+1+\varphi(t)}-2^{k+1}$, 一个常见的小错误是利用了 $2^{k+\varphi(t)}-2^{k}$, 但 $k=0$ 时就不满足题目条件中所要求的正整数了.

N 4. 令 $\mathbb{Z}_{>0}$ 表示全体正整数的集合. 给定一个正整数常数 $C$, 求所有函数 $f: \mathbb{Z}_{>0} \rightarrow \mathbb{Z}_{>0}$ 满足

$$
a+f(b) \mid a^{2}+b f(a)
$$

对任意满足 $a+b>C$ 的正整数 $a, b$ 成立.

解 1. 对任意素数 $p$, 取 $a \equiv-f(p)(\bmod p), a+p>C$. 则 $p \mid a+f(p)$, 由条件, $p \mid a^{2}+p f(a)$. 故 $p|a, p| f(p)$.

对素数 $p>0,1+f(p) \mid 1+p f(1)$, 因此 $f(p) \leq p f(1)$, 存在 $1 \leq k_{p} \leq f(1)$,满足 $f(p)=k_{p} p$, 由素数有无穷多, 存在 $1 \leq k \leq f(1)$, 对无穷多个素数 $p$,有 $f(p)=k p$.

对任意正整数 $a$, 存在素数 $p$, 满足 $f(p)=k p, p>\max \{C-a, a,|f(a)-a k|\}$.由 $a+k p \mid a^{2}+p f(a)$ 知 $a+k p \mid p f(a)-a k p$, 进而 $a+k p \mid f(a)-a k$, 故 $f(a)=a k$.检验满足条件, 所求函数为 $f(x)=k x$, 这里的 $k$ 是一个正整数, 不依赖于 $x$.

解 2. 在条件中取 $a=1$. 由Dirichlet定理知, 存在无穷个正整数 $b>c-1$满足 $1+f(1) b$ 是素数. 那么由 $1+f(b) \mid 1+b f(1)$ 知 $1+f(b)=1+b f(1)$,即 $f(b)=b f(1)$.

在条件中固定 $a$, 存在无穷个 $b>c-a$, 满足 $f(b)=b f(1)$, 代入条件知

$$
\begin{gathered}
a+b f(1) \mid a^{2}+b f(a), \\
\Longrightarrow a+b f(1) \mid\left(a^{2}+b f(a)\right) f(1)-f(a)(a+b f(1))=a(a f(1)-f(a)) .
\end{gathered}
$$

由于 $b f(1)$ 可以任意大, 所以只能有 $a f(1)-f(a)=0$. 所以 $f(a)=a f(1)$.

注. 常见手法: 让整除式左端或者右端为质数.

N 5. 给定正整数 $a$. 如果对正整数 $b$, 对任意满足 $a n \geq b$ 的正整数 $n,\left(\begin{array}{c}a n \\ b\end{array}\right)-1$恒被 $a n+1$ 整除,那我们称 $b$ 为 $a$-好的. 若正整数 $b$ 是 $a$-好的,且 $b+2$ 不是 $a$一好的, 证明: $b+1$ 是质数.

解 1. 第一步, 我们证明 $b$ 是偶数.

取奇素数 $q>b, q \nmid a$, 取 $n$ 满足 $q \mid a n+1, a n>b$. 则

$$
0 \equiv\left(\begin{array}{c}
a n \\
b
\end{array}\right)-1=\frac{(a n)(a n-1) \ldots(a n-b+1)}{b !}-1 \equiv(-1)^{b}-1 \quad(\bmod q)
$$

因此 $b$ 是偶数.

第二步, 证明对任意素数 $p \leq b$ 有 $p \mid a$.

如果存在 $p \leq b, p \nmid a$, 设 $b<p^{\alpha}$, 存在 $n$ 满足 $a n+1 \equiv p\left(\bmod p^{\alpha}\right)$, $a n>b$.因此 $a n$ 在 $p$ 进制下的倒数第二位到倒数第 $\alpha$ 位是 0 , 由 $p \leq b<p^{\alpha}$, 知 $b$ 的 $p$进制表示下倒数第二位到倒数第 $\alpha$ 位有至少一位非 0 , 由Lucas定理, $\left(\begin{array}{c}a n \\ b\end{array}\right) \equiv 0$ $(\bmod p)$, 与 $p|a n+1, a n+1|\left(\begin{array}{c}a n \\ b\end{array}\right)-1$ 相矛盾.
第三步, 证明存在素数 $p \leq b+2$ 有 $p \nmid a$.

用反证法, 如果任意素数 $p \leq b+2$ 有 $p \mid a$. 取 $a n \geq b+2$,满足 $\left(\begin{array}{c}a n \\ b+2\end{array}\right)-1$ 不被 $a n+1$ 整除, 取 $a n+1$ 的任意素因子 $q$, 有 $q>b+2$, 设 $q^{\beta} \| a n+1$,由 $\left(\begin{array}{c}a n \\ b\end{array}\right)-1$被 $a n+1$ 整除,故

$$
\begin{array}{rlr}
\left(\begin{array}{c}
a n \\
b+2
\end{array}\right)-1 & =\left(\begin{array}{c}
a n \\
b
\end{array}\right) \frac{((a n+1)-(b+1))((a n+1)-(b+2))}{(b+2)(b+1)}-1 & \left(\bmod q^{\beta}\right) \\
& \equiv 1 \times 1-1 \equiv 0 . & \left(\bmod q^{\beta}\right)
\end{array}
$$

因此, $\left(\begin{array}{c}a n \\ b+2\end{array}\right)-1$ 被 $a n+1$ 整除,矛盾.

结合以上三步, $b$ 是偶数且存在素数 $b<p \leq b+2$, 故 $p=b+1$ 是素数. 证毕.

注. 第一步是比较好想, 也比较好证明的, 第三步比较 $b, b+2$ 的差异经过尝试是可以发现的, 笔者做这道题时最后才发现第二步, 虽然第二步很短, 但很有思维难度。

解 2. 我们保留上一个解答中第一步和第三步. 对于第二步我们提出一个略有不同的处理方案.

第二步, 证明对任意素数 $p \leq b$ 有 $p \mid a$.

如果存在 $p \leq b, p \nmid a$. 设 $p^{\alpha} \| b$ !, 存在 $n$ 满足 $a n+1 \equiv p\left(\bmod p^{\alpha+1}\right)$, $a n>b$. 那么

$$
\left(\begin{array}{c}
a n \\
b
\end{array}\right)=\frac{a n(a n-1)(a n-2) \ldots(a n-p+1) \ldots(a n-b+1)}{b !} .
$$

上式分子被 $p^{\alpha+1}$ 整除, 分母恰好被 $p^{\alpha}$ 整除, 所以商被 $p$ 整除. 与 $p \left\lvert\,\left(\begin{array}{c}a n \\ b\end{array}\right)-1\right.$ 相矛盾.

注. 由之前证明, 可以看出要控制 $p$ 的幂次, 从而发现此做法.

N 6. 给定 $H=\left\{[i \sqrt{2}]: i \in \mathbb{Z}_{>0}\right\}=\{1,2,4,5,7, \ldots\}$ 和正整数 $n$, 证明存在一个常数 $C$ 使得若 $A \subset\{1,2, \ldots, n\}$ 且 $|A| \geq C \sqrt{n}$, 那么一定存在 $a, b \in A$ 满足 $a-b \in H$ (这里 $\mathbb{Z}_{>0}$ 表示全体正整数的集合, $[z]$ 表示不大于 $z$ 的最大正整数).

解 1. 取 $C=3$, 用反证法, 假设存在 $A \subset\{1,2, \ldots, n\},|A|=k \geq 3 \sqrt{n}$, 对任意 $a>b \in A$, 有 $a-b \notin H$. 由 Beatty 定理, $a-b \in\left\{\lfloor(2+\sqrt{2}) i\rfloor: i \in \mathbb{Z}_{>0}\right\}$.

设 $A=\left\{a_{1}<a_{2}<\cdots<a_{k}\right\}$, 设

$$
a_{i+1}-a_{i}=l_{i}=\left\lfloor(2+\sqrt{2}) m_{i}\right\rfloor(1 \leq i \leq k-1)
$$

,并

$$
\varepsilon_{i}=\left\{(2+\sqrt{2}) m_{i}\right\}=(2+\sqrt{2}) m_{i}-l_{i}
$$

这里的 $\{\cdot\}$ 表示取小数部分.

我们断言 $\varepsilon_{1}+\varepsilon_{2}+\cdots+\varepsilon_{k-1}<1$, 否则取最小的 $1 \leq t \leq k-1$, 满足 $\varepsilon_{1}+$ $\varepsilon_{2}+\cdots+\varepsilon_{t} \geq 1$, 则

$$
\varepsilon_{1}+\varepsilon_{2}+\cdots+\varepsilon_{t} \leq 1+\varepsilon_{t}<2
$$

记 $M=m_{1}+m_{2}+\cdots+m_{t}$,那么

$a_{k+1}-a_{1}=(2+\sqrt{2}) M-\left(\varepsilon_{1}+\varepsilon_{2}+\cdots+\varepsilon_{t}\right) \in((2+\sqrt{2}) M-2,(2+\sqrt{2}) M-1)$

于是

$$
a_{t+1}-a_{1} \in(\lfloor(2+\sqrt{2})(M-1)\rfloor,\lfloor(2+\sqrt{2}) M\rfloor) \text {. }
$$

与假设矛盾.

又有

$\varepsilon_{i}=\sqrt{2} m_{i}-\left(l_{i}-2 m_{i}\right)=\frac{2 m_{i}{ }^{2}-\left(l_{i}-2 m_{i}\right)^{2}}{\sqrt{2} m_{i}+\left(l_{i}-2 m_{i}\right)} \geq \frac{1}{\sqrt{2} m_{i}+\left(l_{i}-2 m_{i}\right)} \geq \frac{1}{2 \sqrt{2} m_{i}}$.

故

$$
\frac{1}{m_{1}}+\frac{1}{m_{2}}+\cdots+\frac{1}{m_{k-1}} \leq 2 \sqrt{2}
$$

此外,

$$
(2+\sqrt{2})\left(m_{1}+\cdots+m_{k-1}\right)=a_{k}-a_{1}+\varepsilon_{1}+\varepsilon_{2}+\cdots+\varepsilon_{k-1} \leq n
$$

进而, 利用柯西不等式得到

$$
\begin{gathered}
(k-1)^{2} \leq\left(m_{1}+m_{2}+\cdots+m_{k-1}\right)\left(\frac{1}{m_{1}}+\frac{1}{m_{2}}+\cdots+\frac{1}{m_{k-1}}\right) \leq(2 \sqrt{2}-2) n . \\
k \leq \sqrt{n}+1<3 \sqrt{n} .
\end{gathered}
$$

矛盾. 结论得证.

解 2. 在这个解答中, 我们将巧妙地绕过Beatty定理的使用, 但实际上得到的不等式是和解答 1 相同的.

首先, 对正整数 $m, m \in H$ 等价于存在 $i \in \mathbb{Z}$ 使得 $i \sqrt{2}-1<m<i \sqrt{2}$, 进一步等价于

$$
\left\{\frac{m}{\sqrt{2}}\right\}>1-\frac{1}{\sqrt{2}} .
$$

仍设 $A=\left\{a_{1}<a_{2}<\cdots<a_{k}\right\}$, 由于 $A$ 具有平移不变性, 不妨设 $a_{1}=0$, 则有 $\left\{\frac{a_{i}}{\sqrt{2}}\right\} \leq 1-\frac{1}{\sqrt{2}}$.
那么对 $i<j$, 如果 $\left\{\frac{a_{i}}{\sqrt{2}}\right\}>\left\{\frac{a_{i}}{\sqrt{2}}\right\}$, 就有

$$
\left\{\frac{a_{j}-a_{i}}{\sqrt{2}}\right\}=1-\left\{\frac{a_{j}}{\sqrt{2}}\right\}+\left\{\frac{a_{i}}{\sqrt{2}}\right\} \geq 1-\left(1-\frac{1}{\sqrt{2}}\right)>1-\frac{1}{\sqrt{2}} .
$$

这就推出 $a_{j}-a_{i} \in H$, 导致矛盾. 所以对 $i<j$, 都有 $\left\{\frac{a_{i}}{\sqrt{2}}\right\}<\left\{\frac{a_{j}}{\sqrt{2}}\right\}$. 那么就有

$$
0=\left\{\frac{a_{1}}{\sqrt{2}}\right\}<\left\{\frac{a_{2}}{\sqrt{2}}\right\}<\cdots<\left\{\frac{a_{k}}{\sqrt{2}}\right\} \leq 1-\frac{1}{\sqrt{2}} .
$$

我们再利用对正整数 $d$, 设 $h=\left\lfloor\frac{d}{\sqrt{2}}\right\rfloor$,

$$
\left\{\frac{d}{\sqrt{2}}\right\}=\frac{d}{\sqrt{2}}-h=\frac{d^{2}-2 h^{2}}{\sqrt{2} d+2 h} \geq \frac{1}{2 \sqrt{2} d} .
$$

所以就有

$$
1-\frac{1}{\sqrt{2}} \geq \sum_{i=1}^{k-1}\left(\left\{\frac{a_{i+1}}{\sqrt{2}}\right\}-\left\{\frac{a_{i}}{\sqrt{2}}\right\}\right)=\sum_{i=1}^{k-1}\left\{\frac{a_{i+1}-a_{i}}{\sqrt{2}}\right\} \geq \sum_{i=1}^{k-1} \frac{1}{2 \sqrt{2}\left(a_{i+1}-a_{i}\right)}
$$

即

$$
\sum_{i=1}^{k-1} \frac{1}{a_{i+1}-a_{i}} \leq 2 \sqrt{2}-2
$$

同样我们有

$$
\sum_{i=1}^{k-1}\left(a_{i+1}-a_{i}\right)=a_{k}-a_{1} \leq n
$$

所以利用柯西不等式,

$$
(k-1)^{2} \leq(2 \sqrt{2}-2) n .
$$

下同解答1.

解 3. 我们再介绍一个非常精妙的解答.

我们的目标是这样的: 我们试图构造一个集合 $B \subset\{1,2, \ldots, n\}$, 使得 $B$ 中元素两两之差在 $H$ 中. 这样的话, 下面的 $|A| \cdot|B|$ 个元素

$$
a+b, a \in A, b \in B
$$

将两两不同! 否则的话, 设对 $b_{1}, b_{2} \in B, b_{1}<b_{2}$ 以及 $a_{1}, a_{2} \in A$, 有

$$
a_{1}+b_{1}=a_{2}+b_{2} \Longrightarrow a_{1}-a_{2}=b_{2}-b_{1} \in H
$$

这与 $A$ 中任两元素之差不在 $H$ 中相矛盾. 于是

$$
\{a+b \mid a \in A, b \in B\} \subseteq\{1,2, \ldots, 2 n\}
$$

所以 $|A| \leq \frac{2 n}{|B|}$. 下面我们来构造一个这样的 $B$ 使得 $|B| \geq\left\lfloor\frac{1}{3} \sqrt{n}\right\rfloor$, 就证得了结果. 我们取 $B=\{X, 2 X, 3 X, \ldots, k X\}$, 这里的 $k=\left\lfloor\frac{1}{3} \sqrt{n}\right\rfloor$, 而 $X \leq \sqrt{n}$ 待定. 那么只需要 $i X \in H, i=1,2, \ldots, k-1$ 即可.
我们利用解答 2 中的观察, $m \in H \Longleftrightarrow\left\{\frac{-m}{\sqrt{2}}\right\}<\frac{1}{\sqrt{2}}$. 只需要

$$
\left\{\frac{-i X}{\sqrt{2}}\right\}<\frac{1}{\sqrt{2}}, i=1,2, \ldots, k-1
$$

即可. 为此, 只需要 $\left\{\frac{-X}{\sqrt{2}}\right\}<\frac{1}{\sqrt{2} k} \Longleftrightarrow\left\{\frac{X}{\sqrt{2}}\right\}>1-\frac{1}{\sqrt{2} k}$.

事实上, 考虑Pell方程 $x^{2}-2 y^{2}=-1$, 其有一列解 $\left(x_{n}, y_{n}\right)$, 满足递推式 $x_{1}=$ $1, x_{2}=7, x_{n+2}=6 x_{n}-x_{n-1}$. 所以可以取一组正整数 $(X, Y)$ 是 $x^{2}-2 y^{2}=-1$的解, 使得 $\sqrt{n} / 6 \leq X \leq \sqrt{n}$. 所以

$$
0>\frac{X}{\sqrt{2}}-Y=-\frac{1}{\sqrt{2} X+2 Y}>-\frac{1}{2 \sqrt{2} X} \geq-\frac{3}{\sqrt{2 n}} \geq-\frac{1}{\sqrt{2} k} .
$$

这就表明 $\left\{\frac{X}{\sqrt{2}}\right\}>1-\frac{1}{\sqrt{2} k}$. 进而结论成立.

注. 可以看出, 对 $\sqrt{2}$ 的有理逼近不会太好, 是这个题能成立的关键. 三个证明都或多或少地使用到了这一个性质。

在解答 3 中, 我们稍稍改进一下结果, 比如可以让 $k=\lfloor\sqrt{n / 3}\rfloor$, 再取 $\sqrt{3 n} / 6 \leq$ $X \leq \sqrt{3 n}, B=\{0, X, 2 X, \ldots, k X\}$, 可得 $|A| \leq 2 \sqrt{3 n}$. 但仍不如前两个解答效果好。

N 7. 证明存在一个常数 $c>0$ 和无穷多个正整数 $n$ 满足下列性质: 存在无穷多个正整数不能表为少于 $c n \log (n)$ 个两两互素的正整数的 $n$ 次方和.

解. 我们把题目中的 $\log$ 看成以 2 为底的对数 $\log _{2}$. 我们待定一个 $c$.

对素数 $p$, 且 $\varphi\left(p^{\alpha}\right) \mid n$, 那么由欧拉定理, $p \nmid x \Longrightarrow x^{n} \equiv 1\left(\bmod p^{\alpha}\right)$. 再注意到 $n \geq \alpha$, 有 $p \mid x \Longrightarrow x^{n} \equiv 0\left(\bmod p^{\alpha}\right)$.

那么, $m$ 个互质整数的 $n$ 次方和模 $p^{\alpha}$ 余 $m$ 或 $m-1$. 我们的计划是找到 $N=p^{\alpha} q^{\beta}$, 这里的 $p, q$ 是不同素数, 且使得 $n=\operatorname{lcm}\left(\varphi\left(p^{\alpha}\right), \varphi\left(q^{\beta}\right)\right)$ 为其最小公倍数.

那么由中国剩余定理, $m$ 个两两互素的正整数 $n$ 次方和, 模 $N$ 恰好有 4 种可能. 再注意 $m \leq c n \log n$, 于是不超过 $c n \log n$ 个两两互素的正整数 $n$ 次方和,模 $N$ 至多有 $4 c n \log n$ 种可能.

如果我们能找到一个正数 $c$, 使得存在无穷对素数幂 $p^{\alpha}, q^{\beta}$ 使得

$$
\operatorname{lcm}\left(\varphi\left(p^{\alpha}\right), \varphi\left(q^{\beta}\right)\right) \mid n \text {, 且 } N=p^{\alpha} q^{\beta}>4 c n \log n \text {. }
$$

能成立, 那么结论就成立了. 之后的构造方案有很多, 我们在这里给出两个.

## 构造1.

我们知道形如 $2^{2^{t}}+1$ 的数的素因子 $p$ 都满足 $2^{t+1} \mid p-1$. 所以我们就取素
数 $p \mid 2^{2^{t}}+1$, 我们取 $N=2^{t} p$. 那么 $n=p-1$. 有 $\log _{2} n \leq 2^{t}$. 所以 $N \geq n \log _{2} n$.容易看出取 $c=0.001$ 即可对任意的 $t$ 成立. 于是成立.

## 构造2.

我们取 $2^{2^{t}}+1$ 的素因子 $p$, 再取 $2^{2^{t+1}}+1$ 的素因子 $q$. 容易证明 $p \neq q$,并且 $2^{t}\left|p-1,2^{t}\right| q-1$. 我们取 $N=p q$. 再取 $n=\frac{(p-1)(q-1)}{2^{t}}$. 我们注意 $\sqrt{n} \leq q-1 \leq 2^{2^{t+1}}$, 所以

$$
N>n \cdot 2^{t} \geq n\left(\log _{2} \sqrt{n}-1\right) \geq \frac{1}{2} n\left(\log _{2} n-2\right)
$$

这对 $c=0.001$ 以及 $t>4$ 都是成立的. (这是因为 $t>4$ 时, $n \geq q-1 \geq 2^{t}$. 所以 $\log _{2} n \geq 4, \log _{2} n-2 \geq \frac{1}{2} \log _{2} n$.)

注. 核心是找若干个数的欧拉函数公倍数尽可能小, 结论可以加强, 有兴趣的同学可以参考预选题官方英文解答.

N 8. 对正整数 $a, b$, 证明整数 $a^{2}+\left\lceil\frac{4 a^{2}}{b}\right\rceil$ 不是完全平方数. (这里 $\lceil z\rceil$ 表示不小于 $z$ 的最小正整数.

解 1 . 我们假设存在正整数 $a, b, c$ 满足

$$
a^{2}+\left\lceil\frac{4 a^{2}}{b}\right\rceil=(a+c)^{2} \Longleftrightarrow\left\lceil\frac{4 a^{2}}{b}\right\rceil=(2 a+c) c .
$$

但我们下面证明关于 $(t, k)$ 的方程

$$
\left\lceil\frac{t^{2}}{b}\right\rceil=(t+k) k
$$

是无正整数解的, 这就得到了矛盾 (因为 $t=2 a, k=c$ 就是一组解).

若不然, 我们取一组 $\left(t_{0}, k_{0}\right)$ 是 (1) 的正整数解, 且 $t_{0}$ 最小. 那么

$$
\begin{gathered}
\frac{t_{0}^{2}}{b}>t_{0} k_{0}+k_{0}^{2}-1 \Longrightarrow t_{0}\left(t_{0}-b k_{0}\right)>b\left(k_{0}^{2}-1\right) \geq 0 \Longrightarrow t_{0}>b k_{0} \\
\frac{t_{0}^{2}}{b} \leq t_{0} k_{0}+k_{0}^{2} \Longrightarrow t_{0}\left(t_{0}-b k_{0}\right) \leq b k_{0}^{2}<\left(b k_{0}+k_{0}\right) k_{0} \Longrightarrow t_{0}<b k_{0}+k_{0}
\end{gathered}
$$

设 $t_{0}=b k_{0}+r_{0}, r_{0}<k_{0}$ 是一个正整数. 那么代入

$$
t_{0} k_{0}+k_{0}^{2}-1<\frac{t_{0}^{2}}{b} \leq t_{0} k_{0}+k_{0}^{2}
$$

化简得到

$$
k_{0}\left(k_{0}-r_{0}\right)-1<\frac{r_{0}^{2}}{b} \leq k_{0}\left(k_{0}-r_{0}\right)
$$

这表明

$$
\left\lceil\frac{r_{0}^{2}}{b}\right\rceil=k_{0}\left(k_{0}-r_{0}\right) .
$$

说明 $(t, k)=\left(r_{0}, k_{0}-r_{0}\right)$ 是一组 (1) 的解, 且使得 $t$ 更小, 与 $t_{0}$ 最小的假设相矛盾.

注. 除了直接对原方程进行无穷递降，我们也可以转化成二次方程进行无穷递降. 我们来展示一个这样的解答.

解 2 . 引理: $n \geq 3, p, q$ 是正整数, 若 $n p q-p^{2}-q^{2} \geq 0$, 则 $n p q-p^{2}-q^{2} \geq n-2$.

引理证明: 设 $n p q-p^{2}-q^{2}=k$, 则 $p^{2}+q^{2}-n p q+k=0$, 来证 $k \geq n-2$.

设 $(p, q)$ 是上方程的一组解满足 $p+q$ 最小, 不妨设 $p \leq q$, 考虑二次方程

$$
q^{2}-n p q+p^{2}+k=0 .
$$

它有一个解 $q_{1}=q$, 设另一个解为 $q_{2}$. 由韦达定理,

$$
q_{1}+q_{2}=n p, q_{1} q_{2}=p^{2}+k
$$

因此 $q_{2}$ 是正整数, $\left(p, q_{2}\right)$ 也是一组解, 由最小性 $q_{2} \geq q_{1} \geq p$, 因此 $\left(q_{1}-p\right)\left(q_{2}-\right.$ $p) \geq 0$, 进而 $p^{2}+k-n p^{2}+p^{2} \geq 0$, 结合 $p^{2} \geq 1$, 知 $k \geq n-2$.

对原结论, 用反证法. 假设存在正整数 $a, b, c$ 满足

$$
a^{2}+\left\lceil\frac{4 a^{2}}{b}\right\rceil=(a+c)^{2} \Longleftrightarrow\left\lceil\frac{4 a^{2}}{b}\right\rceil=(2 a+c) c .
$$

记 $p=2 a+c, q=c, n=b+2 \geq 3$, 那么

$$
\begin{aligned}
& (2 a+c) c-1<\frac{4 a^{2}}{b} \leq(2 a+c) c \\
\Longrightarrow & \frac{4 a^{2}}{(2 a+c) c} \leq b<\frac{4 a^{2}}{(2 a+c) c-1} \Longleftrightarrow \frac{p^{2}+q^{2}}{p q} \leq n<\frac{p^{2}+q^{2}-2}{p q-1}
\end{aligned}
$$

由左侧不等式, $n p q-p^{2}-q^{2} \geq 0$, 由引理知 $n p q-p^{2}-q^{2} \geq n-2$, 也即 $(p-q)^{2} \leq$ $(n-2)(p q-1)$. 因此

$$
n-\frac{p^{2}+q^{2}}{p q}=\frac{n p q-p^{2}-q^{2}}{p q} \geq \frac{n-2}{p q} \geq \frac{(p-q)^{2}}{p q(p q-1)}=\frac{p^{2}+q^{2}-2}{p q-1}-\frac{p^{2}+q^{2}}{p q} .
$$

与右侧不等式矛盾. 结论成立.

注. 我们使用反证法, 随后去掉取整, 分离出自由变量 $b$, 进行变形可以得到一个二次不等式, 把它转化成二次不定方程, 就可以用标准无穷递降解决本问题.

这里的引理是重要的. 也就是对 $0 \leq r \leq b-1,(b+2) p q-p^{2}-q^{2}=r$ 是没有正整数解的. 对于二次型 $(b+2) p q-p^{2}-q^{2}$, 做变量代换 $p=a+c, q=c-a$就得到 $b c^{2}-(b+4) a^{2}=r$ 是无解的. 这进一步等价于

$$
c^{2}=a^{2}+\frac{4 a^{2}+r}{b} .
$$

对 $0 \leq r \leq b-1$ 是无解的, 这就推出了原题是无解的.
其实我们也可以直接证明 $b c^{2}-(b+4) a^{2}=r$ 是无解的, 方法也是无穷递降. 该如何进行无穷递降呢? 我们这时候有两个思路。一个思路是, 我们既然可以对 $p, q$ 进行无穷递降， $a=\frac{p-q}{2}, c=\frac{p+q}{2}$ 自然也可以无穷递降. 但是这样递降得到的 $a, c$ 可能是半整数, 需要对一些奇偶性的细节进行处理. 另一个思路就是把它看成 Pell方程, 利用 Pell方程的根的递降办法来处理, 实际上得到的递降结果是同一个表达式, 同样要处理奇偶性的细节.

## IV. 组合

C 1. 无穷整数序列 $a_{0}, a_{1}, \cdots$ (各项不必互异) 具有以下性质：对于任意整数 $i \geq 0,0 \leq a_{i} \leq i$, 且对于任意整数 $k \geq 0$,

$$
\left(\begin{array}{c}
k \\
a_{0}
\end{array}\right)+\left(\begin{array}{c}
k \\
a_{1}
\end{array}\right)+\cdots+\left(\begin{array}{c}
k \\
a_{k}
\end{array}\right)=2^{k}
$$

证明: 每个整数 $N \geq 0$ 都在该数列中出现 (即对于任意 $N \geq 0$, 存在 $i \geq 0$ 使得 $\left.a_{i}=N\right)$.

解. 我们先证明一个结论.

结论. 对于任意整数 $m \geq 0$, 存在整数 $0 \leq k \leq m$, 使得 $a_{0}, \cdots, a_{m}$ 是 $0, \cdots, k ; 0, \cdots, m-$ $k-1$ (当 $k=m$ 时认为是 $1, \cdots, n)$ 的一个排列.

结论的证明. 对 $m$ 归纳. $m=0$ 时, 有 $a_{0}=0$. 取 $k=0$, 结论成立. 对整数 $n \geq 0$, 假设 $m=n$ 时结论成立, $a_{0}, \cdots, a_{n}$ 是 $0, \cdots, k ; 0, \cdots, n-k-1$ 的排列. 则 $m=n+1$ 时, 有

$$
\begin{aligned}
\sum_{i=0}^{n+1}\left(\begin{array}{c}
n+1 \\
a_{i}
\end{array}\right) & =\sum_{i=0}^{k}\left(\begin{array}{c}
n+1 \\
i
\end{array}\right)+\sum_{i=0}^{n-k-1}\left(\begin{array}{c}
n+1 \\
i
\end{array}\right)+\left(\begin{array}{c}
n+1 \\
a_{n+1}
\end{array}\right) \\
& =\sum_{i=0}^{k}\left(\begin{array}{c}
n+1 \\
i
\end{array}\right)+\sum_{i=k+2}^{n}\left(\begin{array}{c}
n+1 \\
i
\end{array}\right)+\left(\begin{array}{c}
n+1 \\
a_{n+1}
\end{array}\right) \\
& =2^{n+1}-\left(\begin{array}{c}
n+1 \\
k+1
\end{array}\right)+\left(\begin{array}{c}
n+1 \\
a_{n+1}
\end{array}\right) .
\end{aligned}
$$

故 $\left(\begin{array}{c}n+1 \\ a_{n+1}\end{array}\right)=\left(\begin{array}{c}n+1 \\ k+1\end{array}\right)$. 因此 $a_{n+1}=k+1$ 或 $n-k$. 故 $a_{0}, \cdots, a_{n+1}$ 是 $0, \cdots, k+$ $1 ; 0, \cdots, n-k-1$ 或 $0, \cdots, k ; 0, \cdots, n-k$ 的排列, 结论成立. 因此由数学归纳法, 结论证毕.

原命题的证明. 由结论, 对于任意整数 $N \geq 0$, 存在整数 $0 \leq k \leq 2 N$, 使得 $a_{0}, \cdots, a_{2 N}$ 是 $0,1, \cdots, k ; 0,1, \cdots, 2 N-k-1$ 的排列. 而 $\max \{k, 2 N-k-1\} \geq$ $N$. 故 $N$ 在 $a_{0}, \cdots, a_{2 N}$ 中出现.
注. 最自然的想法是想归纳证明 $a_{k}=k$. 我们找第一个 $a_{k} \neq k$, 就会发现 $a_{k}=0$. 继续往后探索会发现 $a_{k+1}=1$ 或 $a_{k+1}=k$. 经过这样的探索很容易发现要证的结论.

C 2. 现有 $n$ 个方块，其重量均不小于 1 , 且和为 $2 n$. 证明：对于任意满足 $0 \leq r \leq 2 n-2$ 的实数 $r$, 都可以选取一些方块, 使其重量之和不小于 $r$ 且不大于 $r+2$.

解. 设方块的重量为 $a_{1} \leq a_{2} \leq \cdots \leq a_{n}$. 我们先证明一个结论.

结论 1. 对 $1 \leq k \leq n, a_{1}+\cdots+a_{k-1}+2 \geq a_{k}$ ( $k=1$ 时左边定义为 2 ).

结论 1 的证明. 反设结论不成立, $a_{k}>a_{1}+\cdots+a_{k-1}+2 \geq k+1$. 则有 $\sum_{i=0}^{n} a_{i} \geq \sum_{i=1}^{k-1} 1+\sum_{i=k}^{n} a_{k}>(k-1)+(n-k+1)(k+1)=2 n+(k-1)(n-k) \geq 2 n$.矛盾! 结论 1 证毕.

原命题的证明. 我们只需证明下面的结论 2. 其 $m=n$ 的情况即蕴含原命题.

结论 2. 对 $0 \leq m \leq n$ 和 $r \in\left[-2, \sum_{i=1}^{m} a_{i}\right]$, 存在集合 $M \subseteq\{1, \cdots, m\}$, 使得

$$
\sum_{i \in M} a_{i} \in[r, r+2]
$$

其中 $m=0$ 时定义上述区间为 $[-2,0], M \subseteq \varnothing$.

结论 2 的证明. 对 $m$ 归纳. $m=0$ 时, 取 $M=\varnothing$, 结论成立. 对正整数 $k$,假设 $m=k-1$ 时结论成立. 下考虑 $m=k$ 时的情况. 当 $r \in\left[-2, \sum_{i=1}^{k-1} a_{i}\right]$时，由归纳假设，存在 $M \subseteq\{1, \cdots, k-1\} \subseteq\{1, \cdots, k\}$ 满足条件. 当 $r \in$ $\left(\sum_{i=1}^{k-1} a_{i}, \sum_{i=1}^{k-1} a_{i}\right]$ 时, 由结论 $1, r-a_{k} \in\left(-2, \sum_{i=1}^{k-1} a_{i}\right]$. 因此由归纳假设, 存在集合 $M^{\prime} \subseteq\{1,2, \cdots, k-1\}$, 满足

$$
\sum_{i \in M^{\prime}} a_{i} \in\left[r-a_{k}, r-a_{k}+2\right]
$$

故取 $M=M^{\prime} \cup\{k\} \subseteq\{1, \cdots, k\}$ 满足条件. 综上, $m=k$ 时结论成立. 因此由归纳法, 结论 2 证毕.

注. 有著名结论: 对于无穷正整数数列 $a_{1}<a_{2}<\cdots<a_{n}<\cdots$, 每个正整数都可以表示为数列中若干个数之和, 当且仅当对于任意正整数 $k$,

$$
\sum_{i=1}^{k-1} a_{i}+1 \geq a_{k}
$$

仿照这个结论便得到上面的证法.

C 3. 设 $n$ 为正整数. 哈里有 $n$ 枚硬币在桌上排成一排, 每枚硬币正面或反面朝上. 他反复地进行如下操作: 若恰有 $k$ 枚硬币正面朝上且 $k>0$, 则他将第 $k$ 枚硬币翻面; 否则停止操作. (例如若分别以 $H, T$ 记正面,反面向上, 初始状态为 $T H T$, 则操作过程为 $T H T \rightarrow H H T \rightarrow H T T \rightarrow T T T$, 共进行了三次操作.)

对每个初始状态 $C$ (即 $n$ 个 $H$ 或 $T$ 组成的序列), 记 $\ell(C)$ 为使其变为全部变为 $T$ 所需的操作步数. 证明: $\ell(C)$ 有限. 并求 $C$ 取遍所有 $2^{n}$ 个可能的初始状态时得到的 $\ell(C)$ 的平均值.

解 1. 以一种状态下 $H$ 的硬币位置序号的集合代表这种状态. $\ell(\varnothing)=0$. 对状态 $C=\left\{a_{1}<\cdots<a_{k}\right\}$, 有 $k \leq a_{k}$. 设 $a_{i-1}<k \leq a_{i}$, 其中 $1 \leq i \leq k$, 规定 $a_{0}=0$.

在第一阶段, 令哈里按题意进行所有将 $T$ 翻转为 $H$ 的操作 (若 $k=a_{i}$ 则第一阶段不用操作). 每次翻转后, $H$ 的数量增加 1 , 故下一次操作翻转后一枚硬币. 因此在这个阶段中, 第 $k$ 至第 $a_{i}-1$ 枚硬币依次被从 $T$ 翻转为 $H$, 然后第一阶段结束, 共进行了 $\left(a_{i}-k\right)$ 次操作, 场上共 $a_{i}$ 枚硬币为 $H$.

在第二阶段, 令哈里按题意进行将 $H$ 翻转为 $T$ 的操作. 每次翻转后, $H$ 的数量减少 1 , 故下一次操作翻转前一枚硬币. 因此在这个阶段中, 第 $a_{i}$ 至第 $k$ 枚硬币依次被从 $H$ 翻转为 $T$. 这时, 共进行了 $\left(a_{i}-k+1\right)$ 次操作, 我们令哈里停止操作.



两阶段共进行了 $\left(2\left(a_{i}-k\right)+1\right)$ 次操作, 硬币的状态变为了 $C \backslash\left\{a_{i}\right\}$. 故

$$
\ell(C)=\ell\left(C \backslash\left\{a_{i}\right\}\right)+2\left(a_{i}-k\right)+1
$$

因此, 记 $i_{1}=i$, 归纳地, 我们有

$$
\begin{aligned}
\ell(C) & =\ell\left(C \backslash\left\{a_{i_{1}}\right\}\right)+2\left(a_{i_{1}}-k\right)+1 \\
& =\ell\left(C \backslash\left\{a_{i_{1}}, a_{i_{2}}\right\}\right)+2\left(a_{i_{1}}-k\right)+1+2\left(a_{i_{2}}-(k-1)\right)+1 \\
& =\cdots \\
& =\ell(\varnothing)+2\left(a_{i_{1}}-k\right)+1+2\left(a_{i_{2}}-(k-1)\right)+1+\cdots+2\left(a_{i_{k}}-1\right)+1 \\
& =2\left(a_{1}+\cdots+a_{k}\right)-k^{2},
\end{aligned}
$$

其中， $a_{i_{t}} \in C \backslash\left\{a_{i_{1}}, \cdots, a_{i_{t-1}}\right\}$, 即 $i_{1}, \cdots, i_{k}$ 为 $1, \cdots, k$ 的一个排列. 因此 $\ell(C)$
有限, 其均值为

$$
\overline{\ell(C)}=\frac{1}{2^{n}} \sum_{C \subseteq\{1, \cdots, n\}}\left(S(C)-|C|^{2}\right)=\frac{n(n+1)}{2}-\frac{1}{2^{n}} \sum_{k=0}^{n} k^{2}\left(\begin{array}{l}
n \\
k
\end{array}\right)=\frac{n(n+1)}{4},
$$

其中 $S(C)$ 表示 $C$ 的元素之和.

解 2. 以 $\rho_{n}$ 记所求均值. 考虑 $\rho_{n+1}$ 与 $\rho_{n}$ 之间的关系. 将 $(n+1)$ 枚硬币时的初始状态分为数量相等两类.

第一类, 第 $(n+1)$ 枚硬币为 $T$. 这时第 $(n+1)$ 枚硬币不影响前 $n$ 枚硬币的翻转, 因此该类状态所需步数与去掉最后一枚硬币得到的状态所需步数相同.故 $\ell(C)$ 的均值为 $\rho_{n}$.

第二类, 第 $(n+1)$ 枚硬币为 $H$. 这时如果不经过所有硬币均为 $H$ 的状态 (我们称之为状态 $H$ ) 便无法将第 $(n+1)$ 枚硬币翻转为 $T$. 我们称一个该类的状态 $X_{1} \cdots X_{n} H$ 与状态 $Y_{1} \cdots Y_{n}$ 互为共轭, 如果 $X_{i} \neq Y_{j}$, 对于任意的 $i+j=n+1$,其中 $X_{k}, Y_{k} \in\{H, T\}$. 显然共轭关系是该类的所有状态与 $n$ 枚硬币的所有状态之间的一一对应. 对于共轭的两种状态, 其 $H$ 数之和为 $n+1$. 因此对它们进行操作时翻转的硬币的位置序号之和为 $n+1$, 从而得到的状态仍然共轭. 故共轭的状态在进行相同步数后仍然共轭. 因此该类的初始状态达到状态 $H$ 所需的步数与其共轭状态达到操作结束所需的步数相同. 又从状态 $H$ 达到操作结束恰用 $(n+1)$ 步, 因此该类状态的 $\ell(C)$ 的均值为 $\rho_{n}+(n+1)$.

因此

$$
\rho_{n+1}=\frac{1}{2}\left(\rho_{n}+\left(\rho_{n}+n+1\right)\right)=\rho_{n}+\frac{n+1}{2} .
$$

又 $\rho_{1}=\frac{1}{2}$, 有 $\rho_{n}=\frac{n(n+1)}{4}$. 这也表明了 $\ell(C)$ 均有限.

解 3. 设共 $n$ 枚硬币的状态以等可能出现. 以随机变量 $\ell_{n}$ 记 $n$ 枚硬币时 $\ell(C)$的值. 所求均值即期望 $E \ell_{n}$. 以 $A B$ 记以下事件: 首枚硬币为 $A$ (若 $A \neq *$ ) 且末枚硬币为 $B$ (若 $B \neq *)$, 其中 $A, B$ 代表 $H, T$ 或 $*$ (这相当于 $*$ 代表了 $H$ 或 $T$ ).我们用 $E(X \mid C)$ 表示在事件 $C$ 条件下随机变量 $X$ 的数学期望.

对 $C \in H *$, 哈里将对后 $(n-1)$ 枚硬币, 如同它们是全部硬币, 按所给规则翻转, 直到它们都变为 $T$. 然后将翻转第 1 枚硬币结束操作. 因此 $E\left(\ell_{n} \mid H *\right)=$ $E \ell_{n-1}+1 ; E\left(\ell_{n} \mid H T\right)=E\left(\ell_{n-1} \mid * T\right)+1$.

对 $C \in * T$, 哈里将对前 $(n-1)$ 枚硬币, 如同它们是全部硬币, 按所给规则翻转, 直到它们都变为 $T$. 这时操作结束. 因此 $E\left(\ell_{n} \mid * T\right)=E \ell_{n-1} ; E\left(\ell_{n} \mid H T\right)=$ $E\left(\ell_{n-1} \mid * T\right)+1=E \ell_{n-2}+1$.
对 $C \in T H$, 第 2 至 $(n-1)$ 枚硬币将, 如同它们是全部硬币, 按所给规则翻转, 直到它们都变为 $T$. 然后将依次翻转第 $1, \cdots, n, \cdots, 1$ 枚硬币, 结束操作. 因此 $E\left(\ell_{n} \mid T H\right)=E \ell_{n-1}+(2 n-1)$.

由于事件 $H H, H T, T H, T T$ 等可能, 我们有 $E\left(\ell_{n} \mid H *\right)=\frac{1}{2}\left(E\left(\ell_{n} \mid H H\right)+\right.$ $E\left(\ell_{n} \mid H T\right)$ ). 解得 $E\left(\ell_{n} \mid H H\right)=2 E \ell_{n-1}-E \ell_{n-2}+1$. 类似地, $E\left(\ell_{n} \mid T T\right)=$ $2 E \ell_{n-1}-E \ell_{n-2}-1$. 因此我们有

$$
E \ell_{n}=\frac{1}{4}\left(E\left(\ell_{n} \mid H H\right)+E\left(\ell_{n} \mid H T\right)+E\left(\ell_{n} \mid T H\right)+E\left(\ell_{n} \mid T T\right)\right)=E \ell_{n-1}+\frac{n}{2}
$$

又 $E \ell_{1}=\frac{1}{2}$. 故 $E \ell_{n}=\frac{n(n+1)}{4}$. 这也表明了 $\ell(C)$ 均有限.

注. 本题是19年IMO的考题, 简单找找规律即可.

C 4. 在卡美洛城堡的一张平面上, 亚瑟王建造了一个 $n$ 堵墙组成的迷宫 $\mathfrak{L}$,其中每堵墙都是无限延伸的直线，任意两堵墙不平行，任意三堵墙不共点。梅林将每堵墙的一侧完全染红, 另一侧完全染蓝.

每两堵墙相交处会产生四个墙角，其中两个相对的墙角内侧为一红色墙面与一蓝色墙面, 一个墙角内侧为两红色墙面, 一个墙角内侧为两蓝色墙面. 在每个相交处, 内侧为两不同颜色的相对的两墙角之间连通着一扇的可双向通行的门。

在梅林染色后, 莫甘娜会在迷宫内放置若干骑士. 骑士可以通过门, 但不能穿过墙体。

令 $k(\mathfrak{L})$ 为最大的正整数 $k$, 使得无论梅林如何对 $\mathfrak{L}$ 染色, 莫甘娜总能放置至少 $k$ 名骑士, 使得他们之间两两永远无法相遇. 对每个 $n$, 求 $k(\mathfrak{L})$ 的所有可能值, 其中 $\mathfrak{L}$ 为任一有 $n$ 堵墙的迷宫.

解. 下面我们证明, $k(\mathfrak{L})$ 只能取到 $n+1$. 为此, 我们分别证明对于任意的 $\mathfrak{L}$, $k(\mathfrak{L})$ 以 $n+1$ 为上界和下界.

下界部分. 以平面上区域为顶点, 两顶点连边当且仅当两个区域间有门, 作简单图 $G(V, E) . G$ 的连通分支个数至少为

$$
|V|-|E|=\left(\frac{1}{2} n(n+1)+1\right)-\frac{1}{2} n(n-1)=n+1
$$

因此无论梅林如何染色, 莫甘娜至少可以放置 $(n+1)$ 名骑士. $k(\mathfrak{L}) \geq n+1$

上界部分. 旋转迷宫使任意一堵墙不沿南北向, 显然每堵墙的两面可定义为南面和北面. 令梅林将每堵墙的北面染为红色, 南面染为蓝色. 下面我们用两种方法证明如此染色莫甘娜至多放入 $(n+1)$ 名骑士, 从而得出 $k(\mathfrak{L}) \leq n+1$.
方法 1. 对迷宫中的每个区域, 将其编号为红色面面向该区域的墙的面数,有 $0, \cdots, n$ 共 $(n+1)$ 种编号. 下面我们只需证明编号相同两区域相通. 为此, 我们先证明一个结论.

结论 1. 同一经线上 (连线为正南北向) 的两点, 所在的区域不同时, 其编号不同.

结论 1 的证明. 两点所连线段必经过墙, 这些墙蓝色面面向两点中南侧的那个点, 红色面向另一点. 而其余的墙面向两点的墙面颜色相同. 回忆编号的定义, 结论 1 证毕.

结论 2. 编号相同两区域相通.

结论 2 的证明. 由结论 1, 两编号相同的区域 (不计边界), 必有一个完全位于另一个的西侧. 因此我们可以将所有编号相同的区域排成一列 $D_{1}, \cdots, D_{s}$,使得 $i<j$ 时, $D_{i}$ 位于 $D_{j}$ 的西侧. 对区域 $D_{i}, 2 \leq i \leq s$, 由于其完全处于 $D_{1}$ 的东侧, 故其必含有最西侧的点. 显然该点为两堵墙的交点, 且 $D_{i}$ 位于其中一堵 $l$ 的北侧和另一堵 $m$ 的南侧. 记 $l, m$ 相交产生的四个角中, 与 $D_{i}$ 中的那个角相对的角所在的区域 $D$. 由染色方法与门的设置, 上述两个角之间有门相通, 即 $D_{i}, D$ 相通. 而 $l$ 分别以红色,蓝色面向 $D_{i}, D, m$ 分别以蓝色,红色面向 $D_{i}, D$, 而其余的每一堵墙面向 $D_{i}, D$ 的颜色相同. 因此 $D_{i}, D$ 的编号相同.又 $D_{i}$ 与 $D$ 有公共的顶点, 故由序列的定义, $D=D_{i-1}$. 因此 $D_{i}$ 与 $D_{i-1}$ 相通.故 $D_{1}, \cdots, D_{s}$ 两两相通. 结论 2 证毕.



方法 2. 不妨设亚瑟王建造门的方法如下: 对每个交点, 将两侧均为红色的墙角和两侧均为蓝色的墙角各建成一段足够小的连接两面墙的圆弧, 然后清理掉两圆弧外两堵墙相交的部分, 使另两个墙角得以连通. 这样建成的迷宫由若干
堵新的两两不交的墙 (由小圆弧连接成的折线) 构成, 它们仍然一面完全为红色一面完全为蓝色, 且均没有端点. 若新的墙自身首尾相连形成闭合的环, 则环的内侧的所有墙面同色. 而考虑环最西端的顶点, 它连接的两条边分别以红色和蓝色为内侧, 矛盾! 因此每堵墙的两端均为无限延申的射线. 考虑迷宫中这样的射线数, 知新的墙的数量为 $n$. 因此它们恰将平面分成了 $(n+1)$ 个部分. 故莫甘娜至多可以放入 $(n+1)$ 名骑士.



注. 解答的前半部分比较好想, 后半部分构造比较自然, 可以通过试验小的情况猜出构造方法, 但是证明构造成立很难表述。也可以采用归纳的方法证明,可以作一个足够大的包含所有交点的圆以方便说明. 方法 2 由周鼎昌同学给出,甚是精彩.

C 5. 一个社交网络上共 2019 名用户，他们之间若千对用户是好友关系，其中好友关系是相互的. 开始时, 有 1010 名用户每人有 1009 个好友, 另外的 1009 名用户每人有 1010 个好友. 但这里的好友关系并不稳固的, 因此下述事件在他们之中反复发生, 且每次只发生一个: 设用户 $A, B, C$ 满足 $A$ 是 $B$ 与 $C$ 的共同好友, 且 $B, C$ 不是好友; 事件发生后 $B, C$ 成为好友, 但 $A$ 与 $B, C$ 均不再是好友. 证明: 无论最开始的好友关系是怎样的, 总存在一个事件序列使其发生之后每个用户只有至多一个好友。

解. 以用户为顶点, 两点相连当且仅当他们为好友, 作简单图 $G . G$ 的每个连通分支均有至少 1010 个点, 因此 $G$ 连通. 记通过 $G$ 发生一系列事件可以得到的边数最小的连通图为 $G^{\prime}$.

若 $G^{\prime}$ 中有三角形, 则考虑 $G^{\prime}$ 中阶数最高的完全子图, 设其顶点为 $A_{1}, \cdots, A_{n}$.由于 $G^{\prime}$ 连通且 $n \neq 2019$, 存在 $B \neq A_{1}, \cdots, A_{n}$ 使之与某个 $A_{i}$ 相连. 而 $B$ 必不与 $A_{1}, \cdots, A_{n}$ 均相连, 因此可设 $B$ 与 $A_{j}$ 不相邻. 这时, 可令 $A_{i}, B, A_{j}$ 发生事件, 得到的新图依然连通, 而边数减少, 矛盾!
若 $G^{\prime}$ 中无三角形, 但存在非Hamilton圈的圈 $A_{1} \cdots A_{n}$. 由于 $G^{\prime}$ 连通, 存在 $B \neq A_{1}, \cdots, A_{n}$ 使之与某个 $A_{i}$ 相连. 由于 $G^{\prime}$ 中无三角形, $B$ 与 $A_{i+1}$ 不相连, 其中定义 $A_{n+1}=A_{1}$. 这时, 可令 $A_{i}, B, A_{i+1}$ 发生事件, 得到的新图依然连通, 而边数减少, 矛盾!

若 $G^{\prime}$ 中无三角形, 且仅存在Hamilton圈, 则 $G^{\prime}$ 没有其他的边. 注意到每次事件的发生不改变每个顶点的度数的奇偶性, 而 $G^{\prime}$ 的每个点度数均为 $2, G$ 中却存在奇数度数的点, 矛盾!

因此 $G^{\prime}$ 中没有圈. 记通过 $G^{\prime}$ 发生一系列事件可以得到的边数最小的图为 $G^{\prime \prime}$. 由于事件的发生不会使没有圈的图产生圈, 故 $G^{\prime \prime}$ 没有圈. 若 $G^{\prime \prime}$ 中有度数大于 1 的点 $A$, 则设其与 $B, C$ 均相连, 并令 $A, B, C$ 发生事件, 得到的图边数减少, 矛盾! 因此 $G^{\prime \prime}$ 中的点的度数均不超过 1 .

注. 容易发现当图中存在孤立的 $K_{n}$ 时, 无法再对 $K_{n}$ 中的点进行操作. 保持图的连通性即可避免这种情况的发生.

C 6. 设整数 $n>1$. 给定平面上 $2 n$ 个点, 其中任意三点不共线. 将这些点按某种顺序记为 $A_{1}, \cdots, A_{2 n}$. 考虑这些点构成的 $2 n$ 个角

$$
\angle A_{1} A_{2} A_{3}, \cdots, \angle A_{2 n-2} A_{2 n-1} A_{2 n}, \angle A_{2 n-1} A_{2 n} A_{1}, \angle A_{2 n} A_{1} A_{2} .
$$

我们记这些角的角度值为其最小正值 (即在 $0^{\circ}$ 至 $180^{\circ}$ 之间). 证明: 存在一种对点的编号方式, 使得对应的 $2 n$ 个角可以被分为角度之和相等的两组.



解. 本解答中各脚标 $\bmod 2 n$ 定义. 在平面上选取 $x$ 轴使得 $y>0$ 与 $y<0$两个半平面中各恰有 $n$ 个点. 将 $y>0$ 中的点编号为偶数, $y<0$ 中的点编号为奇数. 对 $1 \leq k \leq 2 n$, 记 $\theta_{k}$ 为直线 $A_{k-1} A_{k}$ 在坐标系中的倾斜角, $X_{k}$ 为线
段 $A_{k-1} A_{k}$ 与 $x$ 轴的交点.

$$
0=\sum_{k=1}^{2 n}\left(\theta_{k}-\theta_{k+1}\right)=\sum_{k=1}^{2 n} \pm \angle X_{k} A_{k} X_{k+1}=\sum_{k=1}^{2 n} \pm \angle A_{k-1} A_{k} A_{k+1}
$$

按等式右边角度前的符号对角度分组, 移项即得两组角度之和相等.

注. 想到用向量方向的旋转便是角度的连续加减后比较容易推出, 这需要所有边的向量 (如果起点与起点相接, 终点与终点相接) 方向在同一个半平面中,否则可能转一圈出现 $360^{\circ}$, 这样比较容易得出这种构造. 证明可以用向量叙述,这里选取了更为简捷的一种叙述方式.

C 7. 在桌子上放置着一排空盒子 $B_{1}, B_{2}, \cdots, B_{60}$ 以及无限供应的鹅卵石.对正整数 $n$, 甲乙二人进行如下的游戏.

在第一轮, 甲取出 $n$ 块鹅卵石并将它们任意分配到 60 个盒子中. 接下来的每个回合都由以下两步组成:

(a) 乙选择一个正整数 $k$, 满足 $1 \leq k \leq 59$, 并将盒子分成两组: $B_{1}, \cdots, B_{k}$和 $B_{k+1}, \cdots, B_{60}$;

（b）甲选择其中一组，向其中的每个盒子中都放入一块鹅卵石，并从另外一组的每个盒子中取出一块鹅卵石。

若在某个回合结束时, 某个盒子中没有鹅卵石, 则乙获胜. 求最小的 $n$, 使得甲能够使乙永远不获胜.

解答. 记初始时 $B_{k}$ 中石子数为 $x_{k}$. 以 $G$ 记操作 (b)中选取含 $B_{60}$ 的一组放入鹅卵石, 以 $L$ 记选取另一组放入. 我们证明一个结论.

结论. 甲可以不败的充分必要条件是, 对于任意的 $1 \leq k_{1} \leq 59$, 以下两条件至少有一个成立:

(i) 对于任意的 $1 \leq k \leq k_{1}$, 有 $x_{k} \geq\left(k_{1}+1\right)-k+1$;

(ii) 对于任意的 $k_{1}+1 \leq k \leq 60$, 有 $x_{k} \geq k-k_{1}+1$.

结论充分性的证明. 由对称性, 不妨设条件(ii)成立. 取一空序列 $\mathcal{M}$, 每轮结束后记录两人的操作于 $\mathcal{M}$ 的最后. 当 $\mathcal{M}$ 为空时, 令甲进行操作 $L$. 当 $\mathcal{M}$ 非空时, 设 $\mathcal{M}$ 中的最后一轮操作为乙选择 $i$. 在本轮操作中, 如果乙选择 $j \leq i$, 则
令甲进行操作 $G$, 然后去掉 $\mathcal{M}$ 中最后两轮 (包括本轮) 的记录; 否则令甲进行操作 $L$. 这样每次去掉的两轮操作的总效果为 $B_{j+1}, \cdots, B_{i}$ 内石子数增加 $1(j=i$时无效果). 因此若按 $\mathcal{M}$ 中的操作进行游戏时乙不会获胜, 则按原操作进行游戏时乙依然不会获胜. 而任意时刻下, 均有

$$
\mathcal{M}=\left(k_{1}, L\right), \cdots,\left(k_{s}, L\right), \quad 1 \leq k_{1}<\cdots<k_{s} \leq 59
$$

其中 $(k, L)$ 记录一轮中乙选择 $k$, 甲进行操作 $L . \mathcal{M}$ 中全体操作的效果为,对 $k>k_{1}, \quad B_{k}$ 减少 $i \leq k_{i}-k_{1}+1 \leq k-k_{1} \leq x_{k}-1$ 块我卵石, 其中设 $k \in\left(k_{i}, k_{i+1}\right], i=1, \cdots, s, k_{s+1}=60$. 因此每个盒子中均有鹅卵石剩余,乙无法取胜. 结论的充分性证毕.

结论必要性的证明. 令甲用一种策略使游戏一直进行下去. 反设存在 $k_{1}$ 两个条件均不满足. 设 $k_{1}+1 \leq k \leq 60$ 满足 $x_{k} \leq k_{1}-k$. 取一空序列 $\mathcal{M}$, 每轮结束后记录两人的操作于 $\mathcal{M}$ 的最后. 当 $\mathcal{M}$ 为空时, 令乙选择 $k_{1}$, 并不妨假设甲进行操作 $L$ (否则在下一次 $\mathcal{M}$ 为空出现前令乙进行与下述对称的操作即可).当 $\mathcal{M}$ 非空时, 设 $\mathcal{M}$ 中的最后一轮操作乙选择了 $i$. 本轮操作中, 令乙选择 $i+1$ (下面我们将证明 $i<59$ ); 然后若甲进行操作 $G$, 则去掉 $\mathcal{M}$ 中最后两轮 (包括本轮) 的记录. 这样每次去掉的两轮操作的总效果为 $B_{i+1}$ 内石子数减少 1 , 因此若按 $\mathcal{M}$ 中的操作进行, 游戏依然可以进行下去. 而任意时刻下, 均有

$$
\mathcal{M}=\left(k_{1}, L\right),\left(k_{1}+1, L\right), \cdots,(i, L) .
$$

若在某个时刻, $i \geq k-1$, 则 $\mathcal{M}$ 中的全体操作对 $B_{k}$ 的总效果为减少 $k-k_{1} \geq x_{k}$块我鸟卵石, 矛盾! 因此 $i<k-1 \leq 59$. 因此留在 $\mathcal{M}$ 中的操作对所有盒子中的我鸟卵石总数变化的贡献是有界的. 而在足够多次操作后, 共去掉了足够多对操作, 每对去掉的操作的总效果使所有盒子中的我岛卵石总数减少 1 , 从而所有去掉的操作的总效果可以使所有盒子中的鹅卵石总数减少足够多. 但开始时鹅卵石总数有限, 矛盾! 结论的必要性证毕.

原命题的证明. 我们约定结论中 $k_{1}=0$ 时(i)成立, $k_{1}=60$ 时(ii)成立. 若甲可以不败, 设 $m$ 是 $1, \cdots, 59$ 中, 使得结论中 $k_{1}=m$ 时成立 (i)的最大数, 则有 $k_{1}=m+1$ 时成立(ii). 因此

$$
\begin{aligned}
\sum_{i=1}^{60} x_{i} & =\sum_{i=1}^{m} x_{i}+x_{m+1}+\sum_{i=m+2}^{60} x_{i} \geq \sum_{i=1}^{m}(m-i+2)+x_{m+1}+\sum_{i=m+2}^{60}(i-m) \\
& =m^{2}-59 m+1830 \geq 960 .
\end{aligned}
$$

而若令甲取 $x_{1}=30, x_{2}=29, \cdots, x_{30}=1, x_{31}=2, \cdots, x_{60}=31$, 则由结论，甲
可以保持不败. 因此最小的可使甲可以保持不败的 $n$ 为 960 .

注. 容易发现, 如果乙后一次选择的划分点不在上一次甲选择的减一的那一侧, 那么甲可以适当选择使得这两次操作合并后, 每个盒子石子数不减, 乙就会 “吃亏”; 类似地, 如果乙后一次选择的划分点在上一次甲选择的减一的那一侧, 而甲没有继续在同一侧减一, 那么两次操作合并后, 每个盒子石子数不增, 甲就会 “吃亏”, 所以两人的最佳策略已经基本确定, 这就可以得到引理, 引理的证明只是在尽量把“吃亏” 说清楚. 美国有一道“考试作弊”的题目的部分想法与它一模一样。

C 8. 爱丽丝有一张仙境的地图, 仙境由 $n \geq 2$ 个城镇组成. 对每两座城镇,它们之间都有一条狭窄的小路相连. 某天, 所有的小路都被下令只能单向通行.爱丽丝无法得知这些小路允许通行的方向, 但红心国王愿意帮助她。爱丽丝被允许询问他一些问题, 在每个问题中, 爱丽丝选取两座城镇, 国王告诉她它们之间的小路的通行方向.

爱丽丝想知道仙境中是否有至少一座城镇只有至多有一条向外通行的小路. 证明：爱丽丝总可以通过询问至多 $4 n$ 个问题得到答案.

解答. 在每个时刻, 以城镇为顶点, 爱丽丝所有得知方向的道路为有向边作有向图, 称图中的一点为 “优秀” 的, 若其出度为 0 ; 称之为 “良好” 的, 若其出度为 1 ; 否则称之为 “失败” 的. 开始时, 所有的点均为优秀的. 若一个点为失败的, 则可以确定它不满足至多有一条向外通行的小路. 我们令爱丽丝分三阶段询问.

第一阶段. 首先令爱丽丝选择两个点询问. 然后归纳地, 在每一次询问得到 $A_{k}$ 指向 $A_{k+1}$ 后, 选择一个没有被连边的点, 询问其与 $A_{k+1}$ 之间的路. 如此询问直到所有点均有连边. 这样共询问了 $(n-1)$ 次, 得到了一棵树. 由于每次询问恰使一个优秀的点变为良好的点, 故询问后图中恰有 $(n-1)$ 个良好的点和 1 个优秀的点. 设优秀的点为 $X$, 且 $Y_{1}, \cdots, Y_{k}$ 为所有不与 $X$ 相连的点.

第二阶段. 令爱丽丝依次确定 $X Y_{1}, X Y_{2}, \cdots$ 的方向, 直到询问出某条从 $X$出发的边 $X Y_{t}$, 或询问至 $X Y_{k}$ 为止. 若所有边 $X Y_{i}$ 均由 $Y_{i}$ 指向 $X$, 则已经确定 $X$ 没有向外通行的路, 即共进行 $n+k-1 \leq 2 n-2$ 次询问后得到了答案. 下考虑爱丽丝在进行了 $t$ 次询问后得知 $X Y_{1}, \cdots, X Y_{t-1}$ 指向 $X, X Y_{t}$ 指向 $Y_{t}$ 的情况. 这时 $Y_{1}, \cdots, Y_{t-1}$ 是失败的, 其余 $(n-t+1)$ 个点均为良好的. 在这 $(n-t+1)$
个良好的点间, 第二阶段只连出了 $X Y_{t}$ 一条边, 而第一阶段中所连的边没有形成环 (不考虑方向), 因此这些良好的点中至多只有一个点与 $X, Y_{t}$ 同时相连. 此外, 在此之后的每个时刻, 两良好的点之间的连边, 只能是 $X Y_{t}$ 或第一阶段产生的, 因为在此之后对两良好的点连边后它们中的一个即变为失败的.

第三阶段. 令爱丽丝每次选择一个不与 $X, Y_{t}$ 均相连的良好的点 $C$, 确定其与 $X, Y_{t}$ 中不相连的一个所连边的方向, 直到某次询问出的连边从 $X$ 或 $Y_{t}$ 发出,或没有这样的点 $C$ 为止. 分三种情况讨论.

情况一. 某次询问出的连边从 $X$ 或 $Y_{t}$ 发出. 则 $X, Y_{t}$ 之一变为了失败的. 因此在之后的每一时刻, 良好的点之间的连边只能是第一阶段产生的，从而它们不会构成多于二阶的完全图. 因此可以每次询问未连边的两个良好间路的方向,直到只有两个良好的点剩余为止. 由于每次询问均恰将一个良好的点变为失败的, 因此共询问了 $(n-t-1)$ 次. 此后对两个良好的点的每一个, 令爱丽丝依次询问所有未与之相连的点与之连边的方向. 由于第一阶段产生的以这两个点之一为一端点的边至少有两条, 因此至多需要再询问 $(2 n-5)$ 次即可连出以这两个点之一为一端点的所有边, 从而确定这两个点是否有至多一条向外通行的小路. 这时爱丽丝共进行了至多 $(n-1)+t+(n-t-1)+(2 n-5)=4 n-7$ 次询问, 得到了答案.

情况二. 第二阶段结束时, 不存在与 $X, Y_{t}$ 同时相连的点, 且第三阶段已经连出的每条边均指向 $X$ 或 $Y_{t}$. 这时前面的询问过后仅 $X, Y_{t}$ 两点是良好的, 与情况一同理, 共进行至多 $(4 n-7)$ 次询问, 便可得到答案.

情况三. 第二阶段结束时, 存在与 $X, Y_{t}$ 同时相连的点 $Z$, 且第三阶段已经连出的每条边均指向 $X$ 或 $Y_{t}$. 这时前面的询问过后仅 $X, Y_{t}, Z$ 三点是良好的. 此后对 $X, Y_{t}, Z$ 的每一个, 令爱丽丝依次询问所有未与之相连的点与之连边的方向. 由于第二阶段连接的前 $(t-1)$ 条边和第三阶段已经连接的 $(n-t-2)$ 条边均恰与这三点中的一个相连, 且这三个点两两相连, 因此至多需要再询问 $(3 n-$ $6)-(t-1)-(n-t-2)-3=2 n-6$ 次即可连出以这三个点之一为一端点的所有边，从而确定这三个点是否有至多一条向外通行的小路. 这时爱丽丝共进行了至多 $(n-1)+t+(n-t-2)+(2 n-6)=4 n-9$ 次询问, 得到了答案.

注 1. 我们证明了询问次数不超过 $4 n-7$.

注 2. 证明 $5 n$ 次询问可以得到答案是容易的. 大致思路是, 每两次询问排除掉一个点, 大约 $2 n$ 次后, 剩下至多 3 个点不是失败的。再依次询问出所有与它们相关的边, 还需要约 $3 n$ 次. 下面需要进行加强. 我们发现, 必须保证前面的
询问后出现 3 个点均为良好的, 且构成有向的圈. 故在第一阶段我们尽可能多地让点有出度, 而不形成圈. 由此我们基本确定了三角形出现的位置. 之后只需保证后面的询问每次都问到可能出现三角形的点即可.

注 3. 我们的解答至少有两个位置可以加强:

（1）第一阶段问出的树过于随意;

(2) 最后检查剩下的点时估计得过宽.

我们可以据此改进到询问不超过 $\left(4 n-2 \log _{2} n-2\right)$ 次. 具体做法如下. 在第一阶段中. 每轮询问如下进行: 将所有优秀点两两配对, 询问每对点之间的方向;如果有奇数 $(>1)$ 个优秀点, 则在询问完已配对的优秀点后, 再询问余下的那个优秀点与当前的任一优秀点之间的方向. 依此不断询问, 直到只有一个优秀点这止. 这样最后剩下的优秀的点 $X$ 已经连出至少 $m=\left\lfloor\log _{2} n\right\rfloor$ 条边. 注意进行完第 $k$ 轮优秀的点的度数至少为 $k$, 故最后一轮与 $X$ 连边的点的度数不小于 $m$.将所有良好的点按到 $X$ 的距离的奇偶性分为 $A, B$ 两组 ( $A$ 为奇数的). 两各组内的点之间均无连边, 且 $A$ 中包含度不小于 $m$ 的那个点. 类似地, $B$ 中包含度不小于 $m-1$ 的点. 第二阶段以本阶段开始时度数递增的顺序询问未与 $X$ 连边的点与 $X$ 的道路. 不妨设询问不超过 $n-1-m$ 次后得到了两条从 $X$ 发出的边.在第三阶段分别在 $A, B$ 中以入度递增的顺序选取两良好的点询问. $A, B$ 最终剩余的良好的点至少分别已有至少 $m, m-1$ 的度, 因此再进行 $(2 n-2 m-2)$ 次询问便可得到答案.

注 4. 我们还可以证明, 爱丽丝至少需要询问 $\left(4 n-3 \log _{2} n-11\right)$ 次才能保证得到答案. 我们不妨令红心国王在爱丽丝每询问一条路径后再确定其方向, 并证明爱丽丝询问不足上述次数时，狡诈的红心国王有策略使爱丽丝无法得到答案. 我们令红心国王分两个阶段回答.

第一阶段。当爱丽丝询问两个点的方向时, 若这两个点所在的连通分支不同，且都是树 (不考虑方向), 则令红心国王回答度数较大的那个连通分支的点指向另一个点; 否则任意回答. 如此进行, 直到恰有 8 个连通分支为树为止. 注意到每次询问后, 为树的连通分支的个数不变或减少 1 个, 因此该阶段会在至少 $(n-8)$ 个问题后停止. 可以证明, 如此回答保证了, 在每个连通分支中, 如果它是一个有 $k$ 个顶点的树, 则其每个顶点的入度不超过 $\log _{2} k$. 每棵树中, 至少有一个优秀的点. 我们记这 8 棵数中, 顶点数最小的 3 棵数中的那个优秀的点分别为 $V_{1}, V_{2}, V_{3}$.
第二阶段. 设图去掉 $V_{1}, V_{2}, V_{3}$ 后得到连通分支 $A_{1}, \cdots, A_{k}(k \geq 5)$. 当被问及时, 我们令红心国王回答 $A_{j}$ 中的点指向 $A_{j+1}, A_{j+2}$ 中的点, $V_{i}$ 指向 $V_{i+1}$,角标取模定义. 若爱丽丝询问某个 $V_{i}$ 与其他点之间的路，当 $V_{i}$ 还有别的未连的边时, 令红心国王回答指向 $V_{i}$; 而当询问的是 $V_{i}$ 未连接的最后一条边时, 回答从 $V_{i}$ 发出. 其余问题任意回答. 如此回答保证了, 在任意时刻均存在着每个点均有至少两条向外的路的可能; 而在没有连出所有以 $V_{i}$ 为顶点的边之前，也存在着某个 $V_{i}$ 只有一条向外的路的可能. 而在阶段开始时，每个 $V_{i}$ 连接了至多 $\log _{2}\left(\frac{3}{8} n-2\right)<\log 2 n-1$ 条边. 因此爱丽丝为了得到答案, 至少需要再询问 $3\left(n-3-\left(\log _{2} n-1\right)\right)+3=3 n+3 \log _{2} n-3$ 次.

C 9. 对于任意两个不同的实数 $x, y$, 我们定义 $D(x, y)$ 为满足 $2^{d} \leq|x-y|<$ $2^{d+1}$ 的唯一整数 $d$. 给定一个实数的集合 $\mathcal{F}$, 对 $x \in \mathcal{F}$, 我们称 $x$ 在 $\mathcal{F}$ 中的标度是所有 $D(x, y)$ 的值, 其中 $y \in \mathcal{F}$ 且 $y \neq x$.

给定正整数 $k$, 设 $\mathcal{F}$ 中的任一元素 $x$ 都只有至多 $k$ 个不同的标度 (注意这些标度可能依赖于 $x$ 的选取). 求 $\mathcal{F}$ 元素个数的最大值.

解. 下面我们证明 $\mathcal{F}$ 元素个数的最大值为 $2^{k}$. 显然 $\mathcal{F}=\left\{1, \cdots, 2^{k}\right\}$ 满足条件. 因此我们只需证明 $|\mathcal{F}| \leq 2^{k}$. 对 $X \subseteq \mathbb{R}$ 与 $x \in X$, 我们记 $f_{X}(x)$ 为 $x$ 在 $X$中的不同标度个数. 有对于任意 $x \in \mathcal{F}, f_{\mathcal{F}}(x) \leq k$. 因此, 我们只需证明下面的结论.

结论.

$$
\sum_{x \in \mathcal{F}} 2^{-f_{\mathcal{F}}(x)} \leq 1 .
$$

结论的证明. 记 $g(\mathcal{F})=|\{D(x, y): x, y \in \mathcal{F}, x \neq y\}|$, 对 $g(\mathcal{F})$ 归纳. $g(\mathcal{F})=0$ 时, $k=0,|\mathcal{F}|=1$, 结论成立. 对正整数 $m$, 设 $g(\mathcal{F})<m$ 时结论成立. $g(\mathcal{F})=m$ 时, 记 $D(x, y)$ 的最大值为 $t$,

$\mathcal{A}=\{x: x<y, x, y \in \mathcal{F}, D(x, y)=t\}, \quad \mathcal{B}=\{y: x<y, x, y \in \mathcal{F}, D(x, y)=t\}$.若存在 $x \in \mathcal{A} \cap \mathcal{B}$, 则设 $x^{\prime}<x<x^{\prime \prime}$ 使 $D\left(x^{\prime}, x\right)=D\left(x, x^{\prime \prime}\right)=t$. 这时, $D\left(x^{\prime}, x^{\prime \prime}\right)=t+1$, 矛盾. 因此 $\mathcal{A} \cap \mathcal{B}=\varnothing$. 记 $\mathcal{C}=\mathcal{F} \backslash(\mathcal{A} \cup \mathcal{B})$. 有 $g(\mathcal{A} \cup \mathcal{C}) \leq m-1$.因此由归纳假设,

$$
\sum_{x \in \mathcal{A} \cup \mathcal{C}} 2^{-f_{\mathcal{A} \cup \mathcal{C}}(x)} \leq 1
$$

而对 $x \in \mathcal{A} \cup \mathcal{C}$, 其在 $\mathcal{A} \cup \mathcal{C}$ 中相较于其在 $\mathcal{F}$ 中, 没有增加新的标度, 且当 $x \in \mathcal{A}$
时, 缺少了标度 $t$. 因此

$1 \geq \sum_{x \in \mathcal{A} \cup \mathcal{C}} 2^{-f_{\mathcal{A} \cup \mathcal{C}}(x)}=\sum_{x \in \mathcal{A}} 2^{-f_{\mathcal{A} \cup \mathcal{C}}(x)}+\sum_{x \in \mathcal{C}} 2^{-f_{\mathcal{A} \cup \mathcal{C}}(x)} \geq \sum_{x \in \mathcal{A}} 2^{-\left(f_{\mathcal{F}}(x)-1\right)}+\sum_{x \in \mathcal{C}} 2^{-f_{\mathcal{F}}(x)}$.

同理,

$$
\sum_{x \in \mathcal{B}} 2^{-\left(f_{\mathcal{F}}(x)-1\right)}+\sum_{x \in \mathcal{C}} 2^{-f_{\mathcal{F}}(x)} \leq 1
$$

结合两式即有

$$
\sum_{x \in \mathcal{F}} 2^{-f_{\mathcal{F}}(x)}=\sum_{x \in \mathcal{A}} 2^{-f_{\mathcal{F}}(x)}+\sum_{x \in \mathcal{B}} 2^{-f_{\mathcal{F}}(x)}+\sum_{x \in \mathcal{C}} 2^{-f_{\mathcal{F}}(x)} \leq 1
$$

因此由数学归纳法, 结论成立.

注. 此题极为困难, 可认为一切元素均为整数, 然后去分析它们两两最大最小距离, 在消去最大距离的过程中会慢慢认识到小结论从而解决.

