# 正整数的斐波那契型数列表示 

尹顺<br>(湖南师范大学附属中学, 410006)<br>指导教师: 汤礼达

2017 年美国国家队选拔考试 (USA-TST) 有下面的正整数的斐波那契型数列的表示问题:

问题 若正整数序列 $\left\{a_{n}\right\}_{n \geq 1}$ 满足 $a_{n+2}=a_{n+1}+a_{n}, n \geq 1$, 则称它是一个斐波那契型数列. 证明: 正整数集可划分成无穷多个斐波那契型数列的并.

这是一个令人惊诧的有趣的结果, 但它并不是新问题. 早在 2000 年匈牙利的 Kömal 杂志上, 它作为 A244 号问题而提出 (供题人: B.Enekes). Kömal 杂志上公布了该问题的三个解法. 美国 TST 官方网站提供的三个解法与前者本质相同. 这两个文献中的三个解均写得较为简略, 不易理解. 本人最近研究了这个问题, 重写了三个解法, 介绍如下.

## 证法一 先证明如下的 Zerkendorf 定理.

定理 对于斐波那契型数列 $F_{0}=F_{1}=1, F_{n+2}=F_{n+1}+F_{n}, n \in \mathbb{N}$ 以及任意正整数 $n$, 存在 $k$ 及 $1 \leq i_{1}<\cdots<i_{k}$, 满足 $k \geq 1, i_{j+1}-i_{j} \geq 2, j=1,2, \cdots, k-1$,使 $n=F_{i_{1}}+\cdots+F_{i_{k}}$ 且该数列 $\left(i_{1}, \cdots, i_{k}\right)$ 唯一.

定理证明 对 $n$ 归纳证明 $i_{1}, \cdots, i_{k}$ 的存在性.

$n=1$ 时, 只能取 $i_{1}=1 ; n=2$ 时, 只能取 $i_{2}=2$.

假设对小于 $n$ 的正整数结论成立, $n$ 时, 若 $n$ 为斐波那契型数列中的一项 $F_{j}(j \geq 2)$, 取 $i_{1}=j$ 即可.

若 $n$ 不为斐波那契型数列中的一项, 则存在 $j \in \mathbb{N}_{+}$, 使 $F_{j}<n<F_{j+1}$, 则 $1 \leq n-F_{j}<n$.

对 $n-F_{j}$ 使用归纳假设知存在 $1 \leq i_{1}<\cdots<i_{k}$, 使得

$$
i_{j+1}-i_{j} \geq 2, j=1, \cdots, k-1,
$$

且

$$
n-F_{j}=F_{i_{1}}+\cdots+F_{i_{k}}
$$

由于 $F_{j-1}+F_{j}=F_{j+1}$, 所以 $F_{i_{k}}<F_{j-1}$, 因此 $i_{k}<j-1$, 即 $i_{k} \leq j-2$, 从而令 $i_{k+1}=j$ 即可, 满足条件.

综上, 存在性得证.

再证唯一性. 若存在 $1 \leq i_{1}<\cdots<i_{k}$ 及 $1 \leq j_{1}<\cdots<j_{l}$ 满足

$$
\begin{gathered}
i_{j+1}-i_{j} \geq 2, j=1, \cdots k-1 \\
j_{r+1}-j_{r} \geq 2, r=1, \cdots l-1
\end{gathered}
$$

且 $\left(i_{1}, \cdots, i_{k}\right) \neq\left(j_{1}, \cdots, j_{l}\right), n=F_{i_{1}}+\cdots+F_{i_{k}}$. 容易看到

$$
F_{i_{1}}+F_{i_{2}}<F_{i_{2}-1}+F_{i_{2}}=F_{i_{2}+1}
$$

依此类推得

$$
F_{i_{k}} \leq n<F_{i_{k}+1}
$$

同理 $F_{j_{l}} \leq n<F_{j_{l}+1}$. 所以

$$
F_{i_{k}}=F_{j_{l}} .
$$

对 $n-F_{i_{k}}=n-F_{j_{l}}$, 同样讨论知 $\left(i_{1}, \cdots, i_{k}\right)=\left(j_{1}, \cdots, j_{l}\right)$ 产生矛盾!

于是唯一性得证, 故定理得证.

回到原题. 由 Zerkendorf 定理, 定义正整数的 “ $F$ 进制”, 即存在

$$
n=a_{k} F_{k}+\cdots+a_{1} F_{1}=\left(a_{k} \cdots a_{1}\right)_{(F)}, k \in \mathbb{N}_{+}
$$

其中 $a_{i} \in\{0,1\}$, 对 $\forall i, a_{i} a_{i+1}=0, i=1, \cdots, k-1, a_{k} \neq 0$.

利用这种表示, 分别依 $a_{1}=1 ; a_{1}=0, a_{2}=1 ; a_{1}=a_{2}=0, a_{3}=1 ; \cdots$ 按行从小到大列出所有正整数:

$$
\begin{array}{cccccc}
F_{1} & F_{1}+F_{3} & F_{1}+F_{4} & F_{1}+F_{5} & F_{1}+F_{3}+F_{5} & \cdots \\
F_{2} & F_{2}+F_{4} & F_{2}+F_{5} & F_{2}+F_{6} & F_{2}+F_{4}+F_{6} & \cdots \\
F_{3} & F_{3}+F_{4} & F_{3}+F_{6} & F_{3}+F_{7} & F_{3}+F_{5}+F_{7} & \cdots \\
F_{4} & F_{4}+F_{6} & \cdots & \ldots & \ldots & \ldots
\end{array}
$$

上面每一列都是一个斐波那契型数列, 故按列把正整数集分划成了无穷多个斐波那契型数列.

从而命题得证.
证法二 对于 $x \in \mathbb{R}^{*}$, 考虑 $f(x)=\left[\varphi x+\frac{1}{2}\right], \varphi=\frac{1+\sqrt{5}}{2}, \varphi^{2}=\varphi+1$.

引理 1 若 $a, b \in \mathbb{N}^{*}$, 且 $f(a)=f(b)$, 则 $a=b$.

引理 1 证明 我们可以用反证法, 不妨设 $b>a$, 则 $b \geq a+1$. 所以

$$
\varphi b+\frac{1}{2} \geq \varphi(a+1)+\frac{1}{2}+\varphi>\left[\varphi a+\frac{1}{2}\right]+1
$$

因此

$$
f(b)=\left[\varphi b+\frac{1}{2}\right] \geq\left[\varphi a+\frac{1}{2}\right]+1=f(a)+1
$$

与 $f(a)=f(b)$ 矛盾!

故引理 1 得证.

引理 2 对 $n \in \mathbb{N}^{*}$, 有 $f(f(n))=f(n)+n$.

引理 2 证明 注意到

$$
\begin{aligned}
f(f(n)) & =\left[\varphi\left[\varphi n+\frac{1}{2}\right]+\frac{1}{2}\right] \\
& >\varphi\left[\varphi n+\frac{1}{2}\right]+\frac{1}{2}-1 \\
& =(\varphi-1)\left[\varphi n+\frac{1}{2}\right]+\frac{1}{2}-1+\left[\varphi n+\frac{1}{2}\right] \\
& =\frac{\left[\varphi n+\frac{1}{2}\right]}{\varphi}+f(n)+\frac{1}{2}-1 \\
& >\frac{\varphi n-\frac{1}{2}}{\varphi}+f(n)+\frac{1}{2}-1 \\
& =n+f(n)+\frac{1}{2}-\frac{1}{2 \varphi}-1 \\
& >n+f(n)-1,
\end{aligned}
$$

且

$$
\begin{aligned}
f(f(n)) & =\left[\varphi\left[\varphi n+\frac{1}{2}\right]+\frac{1}{2}\right] \\
& \leq \varphi\left[\varphi n+\frac{1}{2}\right]+\frac{1}{2} \\
& =(\varphi-1)\left[\varphi n+\frac{1}{2}\right]+\frac{1}{2}+\left[\varphi n+\frac{1}{2}\right] \\
& =\frac{\left[\varphi n+\frac{1}{2}\right]}{\varphi}+\frac{1}{2}+f(n) \\
& \leq \frac{\varphi n+\frac{1}{2}}{\varphi}+\frac{1}{2}+f(n) \\
& =n+f(n)+\frac{1}{2}+\frac{1}{2 \varphi} \\
& <n+f(n)+1,
\end{aligned}
$$

所以

$$
f(f(n))=f(n)+n \text {. }
$$

故引理 2 得证.

回到原题. 下面我们构造满足条件的无穷多个斐波那契型数列, 第 $i$ 个斐波那契型数列的第 $j$ 项用 $a_{i, j}$ 表示:

$$
a_{1,1}=1, a_{1, i+1}=f\left(a_{1, i}\right)=\left[\varphi a_{1, i+1}+\frac{1}{2}\right], \forall i \in \mathbb{N}^{*}
$$

由引理 2, 它是斐波那契型数列.

假设第 $1, \cdots, k$ 个斐波那契型数列已经取好 $\left(k \in \mathbb{N}^{*}\right)$.

对第 $k+1$ 个斐波那契型数列, 取 $a_{k+1,1}$ 为不在前 $k$ 个斐波那契型数列中出现的最小正整数,

$$
a_{k+1, i+1}=f\left(a_{k+1}, i\right)=\left[\varphi a_{k+1, i}+\frac{1}{2}\right], \forall i \in \mathbb{N}^{*}
$$

由引理 2 , 那么这样得到的无穷多个斐波那契型数列, 显然每一个正整数均在某个数列中出现, 于是我们只用证明以上表示的数列不交.

若第 $m$ 个斐波那契型数列与第 $n$ 个斐波那契型数列相交, 不妨设 $m<n$,这两个数列的公共项中小标最小的一项为 $x=a_{m, i}=a_{n, j}$, 则 $i>j \geq 1$. 显然 $j \neq 1$, 否则与 $a_{n, 1}$ 的定义矛盾! 所以 $j>1$. 而

$$
a_{m, i}=f\left(a_{m, i-1}\right), a_{n, j}=f\left(a_{n, j-1}\right)
$$

所以

$$
f\left(a_{m, i-1}\right)=f\left(a_{n, j-1}\right) .
$$

由引理 1 , 有 $a_{m, i-1}=a_{n, j-1}$ 与 $a_{m, i}, a_{n, j}$ 的选取矛盾!

于是任意取出的两个斐波那契型数列均不交.

从而命题得证.

证法三 我们来归纳构造无穷多个这样的斐波那契型数列.

对于两个斐波那契型数列 $\left\{a_{i}\right\}_{i \geq 1}$ 和 $\left\{b_{i}\right\}_{i \geq 1}$, 若对某个 $i \in \mathbb{N}^{*}$, 有

$$
a_{i}<b_{1}<a_{i+1}<b_{2}<a_{i+2},
$$

则称 $\left\{a_{i}\right\}_{i \geq 1}$ 与 $\left\{b_{i}\right\}_{i \geq 1}$ “相隔”. 此时归纳易证: $a_{i+n-1}<b_{n}<a_{i+n}$, 从而 $\left\{a_{i}\right\}_{i \geq 1}$与 $\left\{b_{i}\right\}_{i \geq 1}$ 不交.

用 $A_{i}$ 表示我们将构造的第 $i$ 个斐波那契型数列, $a_{i, j}$ 表示 $A_{i}$ 的第 $j$ 项, 则

$$
A_{1}: a_{1,1}=1, a_{1,2}=2, \cdots ;
$$

$$
A_{2}: a_{2,1}=4, a_{2,2}=6, \cdots .
$$

假设 $A_{1}, \cdots, A_{k-1}$ 已取好 $(k \geq 3)$.

对 $A_{k}$, 取 $a_{k, 1}$ 为最小的不在 $A_{1}, \cdots, A_{k-1}$ 中的数,

$$
a_{k, 2}=2 a_{k, 1}-k
$$

并注意到 $k=2$ 时该等式也成立, 从而对 $\forall k \in \mathbb{N}^{*}, k \geq 2$ 均成立.

$$
a_{k, j+2}=a_{k, j+1}+a_{k, j}, j \geq 1
$$

这样取出了无穷多个斐波那契型数列.

我们要证明以上构造的数列中任意两个数列都是相隔的, 那么他们不交, 且含所有正整数, 也就完成了证明. 为此我们使用数学归纳法.

定义 $a_{i, i}$ 为 $A_{j}$ 中在 $a_{n, 1}$ 之前出现的最大的元素. 数列个数为 2 时, 由于

$$
a_{1,3}=3<a_{2,1}=4<a_{1,4}=5<a_{2,2}=6<a_{1,5}=8,
$$

故 $A_{1}$ 与 $A_{2}$ “相隔”. 假设数列个数小于 $n$ 时, 结论成立 $(n \geq 3)$.

结论 $1\left\{a_{1, i_{1}}, a_{2, i_{2}}, \cdots, a_{n-1, i_{n-1}}\right\}=\left\{a_{n, 1}-(n-1), a_{n, 1}-(n-2), \cdots, a_{n, 1}-1\right\}$.

证明 我们用反证法. 若断言错误, 则存在两个元素在某个 $A_{j 1}$ 中, 也在 $\left\{a_{n, 1}-(n-1), \cdots, a_{n, 1}-1\right\}$ 中. 从而由抽屉原理, 存在某个 $A_{j_{2}}$, 满足

$$
a_{j_{2}, i_{j_{2}}}<a_{n, 1}-(n-1) \leq a_{j_{1}, i_{j_{1}}-1}<a_{j_{1}, i_{j_{1}}}<a_{j_{2}, i_{j_{2}}+1}
$$

则可推出 $A_{j_{1}}$ 与 $A_{j_{2}}$ 不相隔. 这与归纳假设矛盾!

故结论 1 得证.

结论 2 对任意 $j \in\{1, \cdots, n-1\}, a_{j, i_{j}+2}>a_{n, 2}$.

证明 由结论 1 , 有 $a_{i, i_{j}} \geq a_{n, 1}-n+1, \forall j \in\{1, \cdots, n-1\}$.

由 $i_{j}$ 定义知 $a_{i, i_{j}+1} \geq a_{n, 1}+1$. 从而

$$
\begin{aligned}
a_{j, i_{j}+2}=a_{j, i_{j}+1}+a_{j, i_{j}} & \geq\left(a_{n, 1}+1\right)+a_{n, 1}-n+1 \\
& =2 a_{n, 1}-n+2 \\
& =a_{n, 2}+2>a_{n, 2} .
\end{aligned}
$$

故结论 2 成立.

结论 3 对任意 $j \in\{1, \cdots, n-1\}$, 若 $i_{j} \geq 2$, 则 $a_{j, i_{j}+1}<a_{n, 2}$.

证明 $a_{j, i_{j}} \leq a_{n, 1}-1$, 由结论 1 有 $a_{j, i_{j}-1} \leq a_{n, 1}-n$. 所以

$$
\begin{aligned}
a_{j, i_{j}+1}=a_{j, i_{j}}+a_{j, i_{j}-1} & \leq\left(a_{n, 1}-1\right)+\left(a_{n, 1}-n\right) \\
& =2 a_{n, 1}-n-1=a_{n, 2}-1<a_{n, 2}
\end{aligned}
$$

故结论 3 成立.

结论 4 对任意 $j \in\{1, \cdots, n-1\}$, 若 $i_{j}=1$, 则 $a_{j, i_{j}+1}=a_{j, 2}<a_{n, 2}$.

证明 由构造特点有 $a_{1,1}<a_{2,1}<a_{3,1}<\cdots$, 从而

$$
a_{j_{1}} \leq a_{n, 1}-(n-j)<a_{n, 1}-\frac{n-j}{2}
$$

故可以推出 $2 a_{j, 1}-j<2 a_{n, 1}-n$. 由定义, 应有

$$
a_{n, 1}>a_{2,1}=4>a_{1,2}
$$

从而 $j \neq 1$, 故有 $2 a_{j, 1}-j=a_{j, 2}$. 因此

$$
a_{j, 2}<a_{n, 2} \text {. }
$$

故结论 4 成立.

综上, 由结论 $2,3,4$, 对任意 $j \in\{1, \cdots, n-1\}$, 有

$$
a_{j, i_{j}}<a_{n, 1}<a_{j, i_{j}+1}<a_{n, 2}<a_{j, i_{j}+2} .
$$

故命题得证.

