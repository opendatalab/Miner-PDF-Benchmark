数学新星网 $\%$ 冷岗松专栏

www.nsmath.cn/lgszl

# 2021 年上海新星春季数学奥林匹克试题解析 

吴尉迟胡珏伟 冷岗松

2021 年上海新星春季数学奥林匹克于 2021 年 4 月 15 日 8 点到 12 点在上海举行. 下面介绍此次考试的试题和解答. 不当之处, 敬请读者批评指正.

题 1 给定整数 $n \geq 2$. 对 $1,2, \cdots, n$ 的一个排列 $a_{1}, a_{2}, \cdots, a_{n}$ 及 $1 \leq i \leq n$, 用 $x_{i}$ 表示以 $a_{i}$ 为首项的递增子列的长度的最大值, 用 $y_{i}$ 表示以 $a_{i}$ 为首项的递减子列的长度的最大值. 求 $\sum_{i=1}^{n}\left|x_{i}-y_{i}\right|$ 的最小可能值.

(中国人民大学附属中学 张端阳 供题)

解 先证明对 $1 \leq i \leq n-1, x_{i}=y_{i}$ 与 $x_{i+1}=y_{i+1}$ 不能同时成立.

事实上, 当 $a_{i}<a_{i+1}$ 时, $x_{i}>x_{i+1}, y_{i} \leq y_{i+1}$, 所以 $x_{i}-y_{i}>x_{i+1}-y_{i+1}$;当 $a_{i}>a_{i+1}$ 时, $x_{i} \leq x_{i+1}, y_{i}>y_{i+1}$, 所以 $x_{i}-y_{i}<x_{i+1}-y_{i+1}$. 这样,

$$
\left|x_{i}-y_{i}\right|+\left|x_{i+1}-y_{i+1}\right| \geq 1 \text {. }
$$

故

$$
\sum_{i=1}^{n}\left|x_{i}-y_{i}\right| \geq\left\lfloor\frac{n}{2}\right\rfloor
$$

另一方面, 当 $n=2 k$ 时, 考虑 $1,2, \cdots, 2 k$ 的排列

$$
k+1, k, k+2, k-1, k+3, k-2, \cdots, 2 k, 1 \text {. }
$$

此时 $x_{1}=k, y_{1}=k+1, x_{2}=y_{2}=k, \cdots, x_{2 k-1}=1, y_{2 k-1}=2, x_{2 k}=y_{2 k}=1$,

因此 $\sum_{i=1}^{2 k}\left|x_{i}-y_{i}\right|=k$.

当 $n=2 k+1$ 时, 考虑 $1,2, \cdots, 2 k+1$ 的排列

$$
k+1, k, k+2, k-1, k+3, k-2, \cdots, 2 k, 1,2 k+1
$$

此时 $x_{1}=y_{1}=k+1, x_{2}=k+1, y_{2}=k, \cdots, x_{2 k}=2, y_{2 k}=1, x_{2 k+1}=y_{2 k+1}=1$,因此 $\sum_{i=1}^{2 k+1}\left|x_{i}-y_{i}\right|=k$.

修订日期: 2020-05-13.
综上, 所求最小值为 $\left\lfloor\frac{n}{2}\right\rfloor$.

评注 本题源于对下述 Erdös-Szekeres 定理的思考:

任意由 $n^{2}+1$ 个不同实数构成的序列, 均存在长度至少为 $n+1$ 的单调子序列.

此题作为第一题不算容易, 考试中约 $45 \%$ 的同学做对. 此题可以对较小的 $n$进行尝试, 容易猜出答案和构造. 在论证部分, 将相邻两项 $\left|x_{i}-y_{i}\right|,\left|x_{i+1}-y_{i+1}\right|$作为一组讨论, 证明其不能同时为 0 .

题 2 设 $T$ 是 $n$ 个顶点的树. 证明: 可以用 $1,2, \cdots, n$ 将 $T$ 的顶点编号, 使得任意一边的两个顶点编号之差的绝对值不超过 $\frac{n}{2}$.

(华东师范大学 吴尉迟 供题)

证明 对 $n$ 归纳证明原命题.

$n=1$ 时显然.

$n \geq 2$ 时, 假设 $(n-1)$ 时结论成立.

任取 $T$ 中度为 1 的点 $u$, 从 $T$ 中去掉 $u$ 得到树 $T^{\prime}$. 设 $u v \in E(T)$, 由归纳假设, 可将 $T^{\prime}$ 的点标 $1,2, \cdots, n-1$, 任一边两端差 $\leq \frac{n-1}{2} \leq \frac{n}{2}$.

若 $v$ 标数 $\geq \frac{n}{2}$, 将 $u$ 标 $n$ 即可.

若 $v$ 标数 $<\frac{n}{2}$, 将 $u$ 标 0 , 再将所有点标数均 +1 即可.

由归纳法知原题得证!

评注 此题是较为容易的图论题, 考试中约 $52 \%$ 的同学做对. 上述解法中, 归纳的关键点是选取度为 1 的点 $v$, 先对其补图编号, 再对 $v$ 的邻点标号分类讨论,利用平移不变性得到结论.

题 3 给定整数 $n \geq 4$. 求最大的实数 $\lambda$, 使得对任意满足 $\sum_{i=1}^{n} a_{i}=1$ 的非负实数 $a_{1}, a_{2}, \cdots, a_{n}$, 均有

$$
\sum_{i=1}^{n} a_{i} a_{i+1} \leq \frac{1}{4}-\lambda m M
$$

其中 $a_{n+1}=a_{1}, m=\min \left\{a_{1}, a_{2}, \cdots, a_{n}\right\}, M=\max \left\{a_{1}, a_{2}, \cdots, a_{n}\right\}$.

(中国人民大学附属中学张端阳供题)

解 1 将原题齐次化可知, 原题等价于求最大的实数 $\lambda$, 使得对任意的非负
实数 $a_{1}, a_{2}, \cdots, a_{n}$, 均有

$$
\sum_{i=1}^{n} a_{i} a_{i+1} \leq \frac{1}{4}\left(\sum_{i=1}^{n} a_{i}\right)^{2}-\lambda m M
$$

对大于 1 的实数 $t$, 取 $a_{1}=a_{2}=t, a_{3}=\cdots=a_{n}=1$. 此时 $m=1, M=t$, 所以

$$
t^{2}+2 t+(n-3)+\lambda t \leq \frac{1}{4}(2 t+(n-2))^{2}
$$

即

$$
(2+\lambda) t+(n-3) \leq(n-2) t+\frac{1}{4}(n-2)^{2} .
$$

令 $t \rightarrow+\infty$ 得, $2+\lambda \leq n-2$, 故 $\lambda \leq n-4$.

下面证明, 对任意非负实数 $a_{1}, a_{2}, \cdots, a_{n}$, 均有

$$
\sum_{i=1}^{n} a_{i} a_{i+1}+(n-4) m M \leq \frac{1}{4}\left(\sum_{i=1}^{n} a_{i}\right)^{2}
$$

由轮换对称性, 不妨设 $M=a_{n}$. 再对 $1 \leq i \leq n$, 记 $b_{i}=a_{i}-m \geq 0$. 则只需证明

$$
\sum_{i=1}^{n}\left(b_{i}+m\right)\left(b_{i+1}+m\right)+(n-4) m M \leq \frac{1}{4}\left(\sum_{i=1}^{n}\left(b_{i}+m\right)\right)^{2}
$$

即

$$
\begin{aligned}
& \sum_{i=1}^{n} b_{i} b_{i+1}+2 m \sum_{i=1}^{n} b_{i}+n m^{2}+(n-4) m\left(m+b_{n}\right) \\
\leq & \frac{1}{4}\left(\sum_{i=1}^{n} b_{i}\right)^{2}+\frac{1}{2} n m \sum_{i=1}^{n} b_{i}+\frac{1}{4} n^{2} m^{2},
\end{aligned}
$$

即

$$
\frac{1}{4}(n-4)^{2} m^{2}+\frac{1}{2}(n-4)\left(\sum_{i=1}^{n-1} b_{i}-b_{n}\right) m+\frac{1}{4}\left(\sum_{i=1}^{n} b_{i}\right)^{2}-\sum_{i=1}^{n} b_{i} b_{i+1} \geq 0
$$

当 $\sum_{i=1}^{n-1} b_{i} \geq b_{n}$ 时, 熟知

$$
\frac{1}{4}\left(\sum_{i=1}^{n} b_{i}\right)^{2} \geq \sum_{i=1}^{n} b_{i} b_{i+1}
$$

所以上式成立.

当 $\sum_{i=1}^{n-1} b_{i}<b_{n}$ 时, 我们证明 $\triangle \leq 0$, 即证

$$
\left(\sum_{i=1}^{n-1} b_{i}-b_{n}\right)^{2} \leq\left(\sum_{i=1}^{n-1} b_{i}+b_{n}\right)^{2}-4 \sum_{i=1}^{n} b_{i} b_{i+1}
$$

即

$$
\sum_{i=1}^{n} b_{i} b_{i+1} \leq b_{n} \sum_{i=1}^{n-1} b_{i}
$$

这等价于

$$
\sum_{i=1}^{n-2} b_{i} b_{i+1} \leq b_{n} \sum_{i=2}^{n-2} b_{i}
$$

即

$$
\left(b_{1}+b_{3}\right) b_{2}+\sum_{i=3}^{n-2} b_{i} b_{i+1} \leq b_{n} b_{2}+b_{n} \sum_{i=3}^{n-2} b_{i}
$$

由 $\sum_{i=1}^{n-1} b_{i}<b_{n}$ 即证. 综上, 所求最大值为 $n-4$.

解 2 (根据杭州二中叶临风解答整理) $\lambda \leq n-4$ 的证明同解 1 .

下面证明 $\lambda=n-4$ 时结论成立, 有

$$
\sum_{i=1}^{n} a_{i} a_{i+1} \leq \frac{1}{4}-(n-4) m M
$$

(1) $n=4$ 时, 由于 $n-4=0$, 而

$$
a_{1} a_{2}+a_{2} a_{3}+a_{3} a_{4}+a_{4} a_{1}=\left(a_{1}+a_{3}\right)\left(a_{2}+a_{4}\right) \leq\left(\frac{a_{1}+a_{2}+a_{3}+a_{4}}{2}\right)^{2} \leq \frac{1}{4}
$$

故不等式成立.

(2) $n \geq 5$ 时. 先看下面引理.

引理 记 $f(a, b, c, d, e)=a b+b c+c d+d e$, 则当 $a \leq e$ 时, 有

$$
f(a, b, c, d, e) \leq f(a, m, c, b+d-m, e),
$$

其中 $m \leq \min \{a, b, c, d, e\}$.

事实上, 这仅需 $(e-a)(b-m) \geq 0$, 显然成立.

回到原题. 由轮换对称性, 不妨设 $a_{1}=m$, 记一次调整 $f$ 为一次操作, 则操作把连续五个数中较小一端的旁边一个数变成 $m$. 第一次对 $a_{1}, a_{2}, a_{3}, a_{4}, a_{5}$ 操作, 由于 $a_{1}$ 是最小的, 故 $a_{2}$ 变为 $m$; 第二次对 $a_{2}, a_{3}, a_{4}, a_{5}, a_{6}$ 操作, 由于 $a_{2}$ 已被调为 $m$, 是最小的, 故 $a_{3}$ 变为 $m$, 如此进行下去, 直至对 $a_{n-3}, a_{n-2}, a_{n-1}, a_{n}, a_{1}$操作 (此时 $a_{n-3}=a_{1}=m$ ), 把 $a_{n-2}$ 调为 $m$. 操作结束 (也可能只操作一次).

考察操作的性质.

(i) 此时除了 $a_{n-1}, a_{n}$, 其余数均为 $m$, 且所有数的和仍为 1 .

(ii) 记此时最大数为 $M^{\prime}$, 则 $M^{\prime} \geq M$.

这时由于 $b+d-m \geq \max \{b, d\}$, 故操作后五个数的最大值不减. 回原题,由操作的性质知 LHS 不减, RHS 不增. 记 $a_{n-1}=x, a_{n}=y$, 不妨设 $x \geq y$, 则只需证

$$
x y+m(x+y)+(n-3) m^{2} \leq \frac{1}{4}-(n-4) m x,
$$

其中 $x+y+(n-2) m=1$, 代入 $y=1-(n-2) m-x$, 整理, 知原不等式等价于

$$
x^{2}+2\left(m-\frac{1}{2}\right) x+\left(m-\frac{1}{2}\right)^{2}=\left[x+\left(m-\frac{1}{2}\right)\right]^{2} \geq 0
$$

显然成立.

解 $3 \lambda \leq n-4$ 的证明同解 1 .

下面证明 $\lambda=n-4$ 时结论成立.

不妨设 $a_{1}=M$, 再设 $a_{k}=\max \left\{a_{3}, \cdots, a_{n-1}\right\}$. 注意到

$$
\begin{aligned}
& a_{2} a_{3}+a_{3} a_{4}+\cdots+a_{n-1} a_{n} \\
= & \left(a_{2} a_{3}+a_{3} a_{4}+\cdots+a_{k-1} a_{k}\right)+\left(a_{k} a_{k+1}+\cdots+a_{n-1} a_{n}\right) \\
\leq & a_{k}\left(a_{2}+a_{3}+\cdots+a_{k-1}+a_{k+1}+\cdots+a_{n}\right), \\
& a_{1}\left(a_{2}+a_{n}\right) \\
= & a_{1}\left(a_{2}+a_{3}+\cdots+a_{k-1}+a_{k+1}+\cdots+a_{n}\right) \\
& -a_{1}\left(a_{3}+\cdots+a_{k-1}+a_{k+1}+\cdots+a_{n-1}\right) \\
\leq & a_{1}\left(a_{2}+a_{3}+\cdots+a_{k-1}+a_{k+1}+\cdots+a_{n}\right)-(n-4) m M .
\end{aligned}
$$

所以由均值不等式,

$$
\begin{aligned}
\sum_{i=1}^{n} a_{i} a_{i+1} & =a_{1}\left(a_{2}+a_{n}\right)+\left(a_{2} a_{3}+a_{3} a_{4}+\cdots+a_{n-1} a_{n}\right) \\
& =\left(a_{1}+a_{k}\right)\left(a_{2}+a_{3}+\cdots+a_{k-1}+a_{k+1}+\cdots+a_{n}\right)-(n-4) m M \\
& \leq \frac{1}{4}\left(a_{1}+a_{2}+\cdots+a_{n}\right)^{2}-(n-4) m M \\
& =\frac{1}{4}-(n-4) m M .
\end{aligned}
$$

综上, 命题得证.

解 $4 \lambda \leq n-4$ 的证明同解 1.

下面证明 $\lambda=n-4$ 时结论成立.

对 $1 \leq i \leq n$, 记 $b_{i}=a_{i}-m \geq 0$, 则 $\sum_{i=1}^{n} b_{i}=1-n m$, 进而

$$
\sum_{i=1}^{n} a_{i} a_{i+1}=\sum_{i=1}^{n}\left(b_{i}+m\right)\left(b_{i+1}+m\right)=\sum_{i=1}^{n} b_{i} b_{i+1}+2 m(1-n m)+n m^{2}
$$

熟知存在 $\{1,2, \cdots, n\}$ 的非空子集 $I$, 使得

$$
\sum_{i=1}^{n} b_{i} b_{i+1} \leq\left(\sum_{i \in I} b_{i}\right)\left(\sum_{i \notin I} b_{i}\right)
$$

不妨设 $M=a_{n}$ 且 $n \in I$, 并记 $S=\sum_{i \in I} b_{i}$, 则 $M \leq S+m$.
这样,

$$
\begin{aligned}
& \sum_{i=1}^{n} a_{i} a_{i+1}+(n-4) m M \\
= & \sum_{i=1}^{m} b_{i} b_{i+1}+2 m(1-n m)+n m^{2}+(n-4) m M \\
\leq & S(1-n m-S)+2 m(1-n m)+n m^{2}+(n-4) m(S+m) \\
= & S(1-4 m-S)+2 m-4 m^{2} \\
\leq & \left(\frac{1}{2}-2 m\right)^{2}+2 m-4 m^{2}=\frac{1}{4} .
\end{aligned}
$$

综上, 命题得证.

解 5 (根据陈舜老师的解答整理) $\lambda \leq n-4$ 的证明同解 1 .

下面证明 $\lambda=n-4$ 时结论成立. 注意到这等价于证明

$$
\sum_{i=1}^{n}\left(M-a_{i}\right)\left(a_{i+1}-m\right)-(M+m)+4 m M+\frac{1}{4} \geq 0
$$

不妨设 $m=a_{1}, M=a_{k}$, 则

$$
\begin{aligned}
& \sum_{i=1}^{n}\left(M-a_{i}\right)\left(a_{i+1}-m\right) \geq \sum_{i=1}^{k-1}\left(M-a_{i}\right)\left(a_{i+1}-m\right) \\
= & (M-m)\left(a_{2}-m\right)+\left(M-a_{k-1}\right)(M-m)+\sum_{i=2}^{k-2}\left(M-a_{i}\right)\left(a_{i+1}-m\right) .
\end{aligned}
$$

因为

$$
\begin{aligned}
\left(M-a_{i}\right)\left(a_{i+1}-m\right) & =\left(M-a_{i+1}\right)\left(a_{i}-m\right)+\left(a_{i+1}-a_{i}\right)(M-m) \\
& \geq\left(a_{i+1}-a_{i}\right)(M-m),
\end{aligned}
$$

所以

$$
\begin{aligned}
& \sum_{i=1}^{n}\left(M-a_{i}\right)\left(a_{i+1}-m\right) \\
\geq & (M-m)\left(a_{2}-m\right)+\left(M-a_{k-1}\right)(M-m)+\sum_{i=2}^{k-2}\left(a_{i+1}-a_{i}\right)(M-m) \\
= & (M-m)^{2} .
\end{aligned}
$$

故只需证明

$$
(M-m)^{2}-(M+m)+4 m M+\frac{1}{4} \geq 0
$$

这等价于 $\left(M+m-\frac{1}{2}\right)^{2} \geq 0$, 成立!

评注 此题是经典不等式

$$
\frac{1}{4}\left(\sum_{i=1}^{n} a_{i}\right)^{2} \geq \sum_{i=1}^{n} a_{i} a_{i+1}
$$

的强化版本, 是中等偏难的代数题, 考试中约 $15 \%$ 的同学做对此题.

本题的难点之一是猜测 $\lambda$ 的最大值, 可通过对常见的最优情形的分布进行尝试, 得到在两点分布时是最优的.

论证部分也有一定难度. 在论证部分, 解法 1 , 将 $m$ 看成主元, 将问题转化为一元二次函数恒大于 0 的问题; 解法 2 通过巧妙的调整, 将其中 $n-2$ 个变量调整至 $m$ ，这样便可转化为单变元的情形; 解法 3 体现了最值 $n-4$ 的个数意义;解法 4 借用了经典不等式的证明过程; 解法 5 将 $a_{i}$ 都转化为 $M, m$, 放缩的过程十分巧妙.

题 4 在某个合成水果小游戏中, 水果有一系列品种 $S_{1}, S_{2}, \cdots$. 游戏的操作规则是: 对任意正整数 $i$, 可以将两个水果 $S_{i}$ 合成一个水果 $S_{i+1}$, 也可以将三个水果 $S_{i}$ 合成一个水果 $S_{i+2}$. 对正整数 $n$, 已知篮子 $B_{n}$ 装有 $\frac{n(n+1)}{2}$ 个水果: $n$ 个 $S_{1}, n-1$ 个 $S_{2}, \cdots, 1$ 个 $S_{n}$. 证明: 可以通过适当操作, 将 $B_{n}$ 中的所有水果最终合成一个水果.

(浙江大学 张洪申 华东师范大学 何忆捷 供题)

证明 1 定义水果 $S_{k}$ 的价值为 $2^{k-1}, k=1,2, \cdots$. 对任意正整数 $i$, 记 $f_{i}$ 是将两个 $S_{i}$ 合成一个 $S_{i+1}$ 的操作, $g_{i}$ 是将三个 $S_{i}$ 合成个 $S_{i+2}$ 的操作.

易知, 一次操作 $f_{i}$ 使水果的总价值增加 $2^{i}-2 \cdot 2^{i-1}=0$, 一次操作 $g_{i}$ 使水果的总价值增加 $2^{i+1}-3 \cdot 2^{i-1}=2^{i-1}$. 设一开始篮子 $B_{n}$ 中的水果的总价值为 $W_{n}$,则

$$
\begin{aligned}
W_{n} & =2^{0} \cdot n+2^{1} \cdot(n-1)+\cdots+2^{n-1} \cdot 1, \\
2 W_{n} & =2^{1} \cdot n+2^{2} \cdot(n-1)+\cdots+2^{n} \cdot 1
\end{aligned}
$$

所以

$$
W_{n}=2 W_{n}-W_{n}=-n+2^{1}+2^{2}+\cdots+2^{n}=2^{n+1}-n-2 .
$$

为将 $B_{n}$ 中的所有水果合成一个水果, 可通过以下两个步骤来实现目标:

(i) 对 $B_{n}$ 中的水果适当操作, 使水果的总价值变为 2 的方幂;

(ii) 将总价值为 $2^{m}$ ( $m$ 为非负整数 ) 的水果合成一个价值为 $2^{m^{\prime}}$ 的水果.

对于步骤 (i), 由于 $W_{1}=1, W_{2}=4$, 故当 $n=1,2$ 时, 步骤 (i) 已完成.

当 $n=3$ 时, 水果 $S_{1}, S_{2}, S_{3}$ 各有 $3,2,1$ 个, 可依次进行操作 $g_{1}, f_{2}, g_{3}$, 此时水果的总价值变为 $2^{4}$ (只有一个水果 $S_{5}$ ).

当 $n=4$ 时, 水果 $S_{1}, S_{2}, S_{3}, S_{4}$ 各有 $4,3,2,1$ 个, 可依次进行操作 $f_{1}, f_{1}, g_{2}$,
$f_{2}, g_{3}, f_{4}, f_{5}$, 此时水果的总价值变为 $2^{5}$.

当 $n \geq 5$ 时, 注意到 $n+2 \leq 2^{n-2}-1=2^{0}+2^{1}+\cdots+2^{n-3}$, 可将 $n+2$ 表示为 $n+2=a_{1} \cdot 2^{0}+a_{2} \cdot 2^{1}+\cdots+a_{n-2} \cdot 2^{n-3}, a_{1}, a_{2}, \cdots, a_{n-2} \in\{0,1\}$. 由于一开始 $B_{n}$ 中的水果 $S_{1}, S_{2}, \cdots, S_{n-2}$ 各有至少 3 个, 故对 $i=1,2, \cdots, n-2$, 可分别进行 $a_{i}$ 次操作 $g_{i}$, 在这些操作下, 水果的总价值变为

$$
W_{n}+a_{1} \cdot 2^{0}+a_{2} \cdot 2^{1}+\cdots+a_{n-2} \cdot 2^{n-3}=W_{n}+(n+2)=2^{n+1} .
$$

以上给出了步骤 (i) 的完成方式.

再考虑步骤 (ii).

对总价值为 $2^{m}$ 的水果, 尽可能地进行操作 $f_{i}(i=1,2, \cdots)$, 显然这样的操作只能做有限次, 且保持水果的总价值不变, 故存在某个时刻无法再进行任何操作 $f_{i}(i=1,2, \cdots)$, 这意味着此时各水果的品种两两不同.

设这些水果分别为 $S_{i}, S_{i_{2}}, \cdots, S_{i_{r}}\left(i_{1}<i_{2}<\cdots<i_{r}\right)$, 则有

$$
2^{m^{\prime \prime}}=2^{i_{1}-1}+2^{i_{2}-1}+\cdots+2^{i_{r}-1} .
$$

由二进制表示的唯一性, 可知 $r=1, m=i_{1}-1$, 从而这些水果被合成一个价值为 $2^{m^{\prime}}$ 的水果 $S_{m+1}$, 步骤 (ii) 完成. 综上, 结论得证.

## 证明 2 (根据历城二中欧瑜的解答整理)

先用归纳法证下面引理:

引理 设 $m \geq 2$, 可以将 2 个 $S_{1}, 2$ 个 $S_{2}, \cdots, 2$ 个 $S_{m}$ 合成 $S_{m+2}$.

证明 当 $m=2$ 时, 可做如下操作:

$$
\left(S_{2}, S_{2}, S_{1}, S_{1}\right) \rightarrow\left(S_{2}, S_{2}, S_{2}\right) \rightarrow S_{4}
$$

假设 $m(m \geq 2)$ 时成立, 考虑 $m+1$ 时的情形. 由归纳假设, 可将 2 个 $S_{1}, 2$个 $S_{2}, \cdots, 2$ 个 $S_{m}$ 合成 $S_{m+2}$, 此时再将 2 个 $S_{m+1}$ 合成一个 $S_{m+2}$. 此时, 剩余两个 $S_{m+2}$, 将这两个合成 $S_{m+3}$ 即可. 引理得证.

回到原题. 当 $n=1$ 时, 只有一个水果, 结论成立.

当 $n=2$ 时, 可做如下操作: $\left(S_{2}, S_{1}, S_{1}\right) \rightarrow\left(S_{2}, S_{2}\right) \rightarrow S_{3}$.

当 $n=3$ 时, 可做如下操作:

$$
\left(S_{3}, S_{2}, S_{2}, S_{1}, S_{1}, S_{1}\right) \rightarrow\left(S_{3}, S_{2}, S_{2}, S_{3}\right) \rightarrow\left(S_{3}, S_{3}, S_{3}\right) \rightarrow S_{5}
$$

下面证明: 若 $n(n \geq 3)$ 时结论成立, 则 $n+2$ 时结论也成立.

由归纳假设, 首先可将 $B_{n+2}$ 中的 $n$ 个 $S_{1}, n-1$ 个 $S_{1}, \cdots, 1$ 个 $S_{n}$ 合成 $S_{n+2}$.
此时, 篮子中剩 2 个 $S_{n+2}, 2$ 个 $S_{n+1}, \cdots, 2$ 个 $S_{1}$, 由引理知这些水果可以合成一个 $S_{n+4}$.

由归纳原理知命题得证!

评注 此题是中等难度的组合题, 考试中约 $25 \%$ 的同学做对此题.

解法 1 采用赋值方法, 这里用 2 的幕次赋值, 其好处是可以保持 $f_{i}$ 变换下赋值之和不变, 在 $g_{i}$ 变换下赋值之和单增. 利用归纳法证明赋值之和可以最终变为 2 的幂, 这样由 2 进制表示的唯一性便得结果.

解法 2 是一个妙解. 考试中不少同学尝试用步长为 1 的归纳法证明, 但均未做出. 若改用步长为 2 的归纳法, 即跳跃归纳法, 问题便可以迎刃而解.

题 5 设 $\sigma(n)$ 表示正整数 $n$ 的正约数之和, $A_{n}$ 是 $\sigma(n)$ 的不同素因子构成的集合, $B_{n}$ 是 $n$ 的不同素因子构成的集合. 证明: 对任意正整数 $k$, 存在正整数 $m$,使得 $\left|A_{m} \backslash B_{m}\right|=k$.

(温州知临中学 杨浩泽 供题)

证明 1 取 $k$ 个互不相同的奇素数 $p_{1}, p_{2}, \cdots, p_{k}$, 则对任意正整数 $i, 1 \leq i \leq$ $k$, 由 $\left(2, p_{i}\right)=1$, 及 $p_{i}$ 为素数, 结合 Fermat 小定理, 有

$$
2^{p_{i}-1} \equiv 1 \quad\left(\bmod p_{i}\right), \quad i=1,2, \cdots, k
$$

取 $t=\prod_{i=1}^{k}\left(p_{i}-1\right)$, 则由上式知 $2^{t} \equiv 1\left(\bmod p_{i}\right)$, 即 $p_{i} \mid 2^{t}-1(i=1,2, \cdots, k)$.

取 $m_{1}=2^{t-1}$, 有

$$
\sigma\left(m_{1}\right)=1+2+\cdots+2^{t-1}=2^{t}-1 .
$$

所以

$$
p_{i} \in A_{m_{1}}(i=1,2, \cdots, k), B_{m_{1}}=\{2\}
$$

由 $p_{1} \geq 3$, 知 $t-1>0$. 故 $\left|A_{m_{1}} \backslash B_{m_{1}}\right| \geq k$.

我们定义如下操作构造数列 $\left\{m_{j}\right\}$ : 第 $j$ 次操作, 对 $\left\{m_{j}\right\}$ :

若 $\left|A_{m_{j}} \backslash B_{m_{j}}\right| \geq 1$, 则取 $A_{m_{j}} \backslash B_{m_{j}}$ 的一个元素 $q_{j}$, 取 $m_{j+1}=m_{j} \cdot q_{j}$,

若 $\left|A_{m_{j}} \backslash B_{m_{j}}\right|=0$, 则终止操作.

由 $q_{j} \in A_{m_{j}} \backslash B_{m_{j}}$, 知 $\left(q_{j}, m_{j}\right)=1$, 所以

$$
\begin{gathered}
B_{m_{j+1}}=B_{m_{j}} \cup\left\{q_{j}\right\} \\
\sigma\left(m_{j+1}\right)=\sigma\left(m_{j} \cdot q_{j}\right)=\sigma\left(m_{j}\right) \cdot \sigma\left(q_{j}\right)=\sigma\left(m_{j}\right) \cdot\left(q_{j}+1\right)
\end{gathered}
$$

故 $A_{m_{j}} \subset A_{m_{j+1}}$, 知

$$
\left|A_{m_{j+1}} \backslash B_{m_{j+1}}\right| \geq\left|A_{m_{j}} \backslash B_{m_{j+1}}\right| \geq\left|A_{m_{j}} \backslash B_{m_{j}}\right|-1
$$

又对任意奇素数 $p$, 若 $p \leq 2^{t}-1$, 有 $p+1$ 中的素因子 $\leq 2^{t}-1$ (因为 $2 \mid p+1$,所以 $p+1$ 的素因子 $\leq \frac{p+1}{2}<p \leq 2^{t}-1$ ).

由此, 简单归纳可得对任意正整数 $j, A_{m_{j}}$ 和 $B_{m_{j}}$ 中的元素均 $\leq 2^{t}-1$. 又

$$
\left|B_{j+1}\right|=\left|B_{j} \cup\left\{q_{j}\right\}\right|=\left|B_{j}\right|+1, \quad j \in \mathbb{N}^{+}
$$

且不大于 $2^{t}-1$ 的素数仅有有限个, 知存在正整数 $s$ 使 $\left|A_{m_{s}} \backslash B_{m_{s}}\right|=0$.

结合 $\left|A_{m_{1}} \backslash B_{m_{1}}\right| \geq k$, 及 $(*)$, 可得存在正整数 $l \leq s$, 使 $\left|A_{m_{l}} \backslash B_{m_{l}}\right|=k$.

故命题得证.

## 证明 2 (根据杭州学军中学叶梓的解答整理)

设 $q_{1}, \cdots, q_{k}$ 为互不相同的奇素数. 令 $r=\varphi\left(q_{1} \cdots q_{k}\right)-1$, 则

$$
q_{1} \cdots q_{k} \mid 2^{r+1}-1=\sigma\left(2^{r}\right) .
$$

取 $m_{1}=2^{r}$, 于是

$$
\left\{q_{1}, \cdots, q_{k}\right\} \subset A_{2^{r}},\left|B_{2^{r}}\right|=|\{2\}|=1 .
$$

从而, $\left|A_{m_{1}} \backslash B_{m_{1}}\right| \geq k$.

不妨设 $\left|A_{m_{1}} \backslash B_{m_{1}}\right|>k$, 否则结论成立. 此时, $\sigma\left(m_{1}\right)$ 至少有 $k+1$ 个素因子,故可设 $2^{r+1}-1$ 的所有素因子从小到大的排列为

$$
r_{1}<r_{2}<\cdots<r_{l+1}<\cdots<r_{l+k}
$$

其中 $l$ 为正整数. 设 $p_{1}, p_{2}, \cdots$ 为所有素数从小到大的排列. 设 $r_{l}=p_{t}, t \in \mathbb{N}^{*}$.

令 $m=2^{r} p_{1} p_{2} \cdots p_{t}$, 那么

$$
\sigma(m)=\sigma\left(2^{r}\right) \sigma\left(p_{1}\right) \cdots \sigma\left(p_{t}\right)=\left(2^{r+1}-1\right)\left(p_{1}+1\right) \cdots\left(p_{t}+1\right)
$$

注意到 $p_{i}+1,1 \leq i \leq t$ 的素因子不超过 $\frac{p_{t}+1}{2}<p_{t}$, 又 $r_{l+1}, \cdots, r_{l+k}$ 均是 $2^{r+1}-1$的素因子,因此

$$
A_{m} \subset\left\{p_{1}, \cdots, p_{t}, r_{l+1}, \cdots, r_{l+k}\right\} \text {, 且 } r_{l+1}, \cdots, r_{l+k} \in A_{m} \text {. }
$$

又 $B_{m}=\left\{2, p_{1}, \cdots, p_{t}\right\}$, 故

$$
\left|A_{m} \backslash B_{m}\right|=\left|\left\{r_{l+1}, \cdots, r_{l+k}\right\}\right|=k
$$

命题得证.
评注 此题是较难的数论题, 考试中约 $6 \%$ 做对此题.

证明 1 采用了离散介值原理. 由费马小定理构造 2 的方幂 $m_{1}$, 使其对应的 $\left|A_{m_{1}} \backslash B_{m_{1}}\right| \geq k$, 每次操作将 $m_{j}$ 乘以 $A_{m_{j}} \backslash B_{m_{j}}$ 的某个素因子, 再证明这种操作下, $|A \backslash B|$ 至多减少 1 , 这样由介值原理知结论成立.

证明 2 是一个妙解. 通过将较 $m$ 定义为 $2^{r}$ 与 $2^{r+1}-1$ 较小的素因子的乘积,从而保证 $2^{r+1}-1$ 较大的 $k$ 个素因子恰是 $A_{m} \backslash B_{m}$ 的全部元素.

题 6 已知 $\triangle A B C$ 的外接圆为 $\Gamma, D$ 为 $B C$ 中点. $E$ 在 $\triangle A B C$ 内, 满足 $\angle B A D=\angle C A E$, 且 $\angle B E C=90^{\circ} . M$ 在 $B C$ 上, 满足 $\angle E M D=\angle A D M$. 延长 $A M$ 交 $\Gamma$ 于 $L, K$ 为线段 $A L$ 上一点, 满足 $\angle A B K=\angle C D L$. 设 $A N \perp B C$ 交 $B C$ 于 $N$, 证明: $K L=2 D N$.

(温州育英国际实验学校 林逸沿 供题)



## 证明 (浙江省温州育英国际实验学校胡俊浦、凌晨)

设 $A E$ 交 $\Gamma$ 于 $T$, 由题意可知

$$
\triangle A B K \backsim \triangle C D L \Rightarrow \frac{A B}{D C}=\frac{B K}{D L}
$$

而又 $A B T C$ 为调和四边形可知 $\frac{A B}{D C}=\frac{A B}{B D}=\frac{B T}{D T}, \angle A B T=\angle C D T$, 于是有

$$
\angle K B T=\angle L D T, \frac{D L}{D T}=\frac{B K}{B T} \Rightarrow \triangle B T K \backsim \triangle D T L
$$

进而有

$$
\triangle T L K \backsim \triangle T D B \backsim \triangle B D A \Rightarrow K L=\frac{T L \cdot A D}{D B} .
$$

过 $A$ 作 $B C$ 的平行线交 $\Gamma$ 于 $S$, 易知 $A S=2 D N$, 要证明 $K L=2 D N$, 只要证

$$
\frac{T L \cdot A D}{D B}=A S \Leftrightarrow \sin \angle E A M \cdot A D=\sin \angle A T S \cdot D B
$$

设 $A E$ 交 $B C$ 于 $X$, 交以 $B C$ 为直径的圆于另一点 $J$, 则

$$
A X \cdot X T=B X \cdot X C=E X \cdot X J \Rightarrow \frac{A X}{X J}=\frac{E X}{X T}
$$

又 $A B T C$ 为调和四边形, 故

$$
\angle A D M=\angle T D M \Rightarrow E M \| D T \Rightarrow \frac{E X}{X T}=\frac{M X}{X D}
$$

于是

$$
\frac{A X}{X J}=\frac{M X}{X D} \Rightarrow D J / / A M
$$

故可知 $\angle D E T=\angle D J X=\angle E A M$. 于是 $\sin \angle E A M=\sin \angle D E T$, 而由又正弦定理知

$$
\sin \angle D E T=\frac{D T}{D E} \sin \angle A T D=\frac{D T}{D C} \sin \angle A T D
$$

又易知 $\frac{A D}{D C}=\frac{D C}{D T}$, 故

$$
\sin \angle D E T=\frac{D C}{A D} \cdot \sin \angle A T D=\frac{D C \cdot \sin \angle A D C}{\sin \angle A C B \cdot A C} \cdot \sin \angle A T D,
$$

故命题等价于 $A D \cdot \sin \angle A D C=A C \cdot \sin \angle A C B$, 这显然成立, 故命题得证.

评注 此题是难题, 考试中不到 $3 \%$ 的人做对此题. 本题的难点是如何证明 $\angle D E X=\angle E A M$.

上述解法非常漂亮, 其思想在于将 $K L$ 用相似来表示, 从而进行消点, 但这样的方法难以想到, 原因在于 $\triangle A B K \sim \triangle C D L$ 先入为主, 导致解题人多半会往这个方向想。

