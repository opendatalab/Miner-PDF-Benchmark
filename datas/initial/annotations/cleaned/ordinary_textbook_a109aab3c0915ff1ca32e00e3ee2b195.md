# 对两道数论赛题相似性的探究 

## 张晚治

(石家庄二中, 050004)

本文给出两道赛题的构造过程, 并指出它们的相似性.

笔者在做文 [1] 中的题目时, 看到如下题目:

题 1 (第 45 届 IMO 预选题) 设 $k$ 为大于 1 的固定整数, $t=4 k^{2}-5$, 求证: 存在 $a, b \in \mathbb{N}^{*}$, 使得如下定义的数列 $x_{0}=a, x_{1}=b, x_{n+2}=x_{n+1}+x_{n}(n=$ $0,1, \cdots)$, 其所有项均与 $t$ 互素.

分析 此题原答案是直接给一个神奇的构造 “ $a=1, b=2 k^{2}+k-2$ ”, 然后论证同余性质, 至于为什么要取 $a=1, b=2 k^{2}+k-2$, 原解答里并未提及.

笔者做如下分析:

因为此数列为线性递推数列, 所以必为模周期数列, 希望构造出一个 $\left\{x_{n}\right\}$,使每项均与一个数的幂同余. 所以取 $a=1$, 令 $b=m k^{2}+n k+l$ ( $b$ 为关于 $k$ 的二次式) 次同余, 再使此数与 $m$ 互质, 即可得证.

写出 $\left\{x_{n}\right\}$ 前几项 $1, b, 1+b, 1+2 b, 3 b+2$, 即找到 $b$, 满足

$$
\begin{aligned}
& \left\{\begin{array}{c}
4 b \equiv b^{2} \quad\left(\bmod 4 k^{2}-5\right) \\
2 b+1 \equiv b^{3} \quad\left(\bmod 4 k^{2}-5\right) \\
3 b+2 \equiv b^{4} \quad\left(\bmod 4 k^{2}-5\right)
\end{array}\right. \\
& x_{n} \equiv b^{0}, b^{1}, b^{2}, b^{3}, b^{4} \quad\left(\bmod 4 k^{2}-5\right) .
\end{aligned}
$$

注意到后两式可由第 1 式推出, 只考虑第 1 式, 将 $b$ 代入

$$
1+m k^{2}+n k+l \equiv 4 l k+n^{2} k^{2}+2 l n k+l^{2}+5 k^{2}+5 n k
$$

为消去四次, 三次项, 不妨设 $m=2$ (使之不出现分数), 利用

$$
4 k^{2} \equiv 5 \quad\left(\bmod 4 k^{2}-5\right)
$$[^0]所以

$$
\left(4 l+n^{2}+5-2\right) k^{2}+(2 l n+4 n) k+l^{2}-l-1 \equiv 0 \quad\left(\bmod 4 k^{2}-5\right) .
$$

为使上式成立, 令

$$
\left\{\begin{array}{l}
n^{2}+3=4 \\
2 l n+4 n=0
\end{array}\right.
$$

可以推出

$$
\left\{\begin{array}{l}
n=1,-1 \\
l=-2,-2
\end{array}\right.
$$

经检验 $l^{2}+4 l-1=-5$ 成立! 所以不妨设 $b=2 k^{2}+k-2$.

至此我们得到了原题构造. 因为

$$
\left(2 k^{2}+k-2,4 k^{2}-5\right)=\left(-2 k-1,4 k^{2}-5\right)=(2 k+1,4)=1,
$$

所以回到原题,归纳证明 $x_{n} \equiv b^{n}(\bmod t)$.

$n=1,2$ 显然, 设结论对 $\leq n$ 时成立, 则

$$
\begin{aligned}
x_{n+1} & =x_{n-1}+x_{n} \\
& \equiv b^{n}+b^{n-1}=b^{n-1}(1+b) \\
& \equiv b^{n-1} \cdot b^{2}=b^{n+1} \quad\left(\bmod 4 k^{2}-5\right) .
\end{aligned}
$$

由数学归纳法知, $x_{n} \equiv b^{n}(\bmod t)$ 成立.

又 $(b, t)=1$, 所以 $\left(b^{n}, t\right)=1$, 所以 $\left\{x_{n}\right\}$ 中每一项均与 $t$ 互素.

再看一道类似的题目,这是笔者在做文 [2] 中看到的.

题 2 (2017 年印度国家队选拔考试) 数列 $\left\{a_{n}\right\}, a_{0}=m, a_{1}=n$, 对任意 $k \geq 1$, 均有 $a_{k+1}=4 a_{k}-5 a_{k-1}$, 记 $p$ 为大于 5 且模 4 余 1 的素数, 求证: 存在 $m, n \in \mathbb{N}^{*}$, 满足 $p$ 不整除 $a_{k}$, 对任意 $k \geq 0$ 恒成立.

分析 此题同上题一样, 仍需找到一个使得 $a_{k} \equiv n_{k}(\bmod p)$.

证明 同上题, 令 $m=1$, 因为 $p \equiv 1(\bmod 4)$, 所以 $p$ 整除 $t^{2}+1$ (二次剩余).同上题, 希望找 $n$ 满足

$$
4 n-5 \equiv n^{2} \quad\left(\bmod t^{2}+1\right) .
$$

令

$$
\begin{gathered}
n=a t^{2}+b t+c \\
a^{2} t^{4}+2 a b t^{3}+\left(2 a c+b^{2}\right) t^{2}+2 b c t+c^{2} \equiv 4\left(a t^{2}+b t+c\right)-5 \quad\left(\bmod t^{2}+1\right) .
\end{gathered}
$$

左式 $\equiv a^{2} t^{2}+2 a b t+\left(2 a c+b^{2}\right) t^{2}+2 b c t+c^{2}\left(\bmod t^{2}+1\right)$,

右式 $\equiv 4 a t^{2}+4 b t+4 c-5\left(\bmod t^{2}+1\right)$,

所以

$$
\left(a^{2}+2 a c+b^{2}-4 a\right) t^{2}+(2 a b+2 b c-4 b) t+c^{2}-4 c+5 \equiv 0 .
$$

为方便化简

$$
\left\{\begin{array}{l}
c^{2}-4 c+5=1, \\
2 a b+2 b c-4 b=0, \\
a^{2}+2 a c+b^{2}-4 a=1
\end{array}\right.
$$

由 (1) 式 $c=2$, 由 (2) 式不妨设 $a=0$, 在此式中 $b$ 任意, 由 (3) 式 $b= \pm 1$,所以取 $b=1, n=t+2$.

下同上题, 证明对任意 $k \geq 0$, 有 $a_{k} \equiv n^{k}(\bmod p)$.

$k=0,1$, 显然. 设对任意 $s=0,1 \cdots k, a_{s} \equiv n^{s}(\bmod p)$. 则 $s=k+1$ 时,

$a_{k+1}=4 a_{k}-5 a_{k}-1 \equiv 4 n^{k}-5 n^{k-1} \equiv n^{k-1}(4 n-5) \equiv n^{k+1} \quad(\bmod p)$.

又若

$$
p|n, p| t+2, t^{2}+1 \equiv(-2)^{2}+1 \equiv 5 \quad(\bmod p)
$$

与 $p=5$ 矛盾, 所以 $p$ 不整除 $n$. 故 $p$ 不整除 $a_{k}$.

此题应是印度人做完预选题后在此基础上改编而成的, 换汤不换药.

## 参考文献

[1] 中等数学编辑部编. 国内外数学奥林匹克试题精选 (2002-2012): 数论部分 $[\mathrm{M}]$, 浙江大学出版社, 2015.10.

$[2]$ 中等数学编辑部编. 国内外数学奥林匹克试题及精解 (2016-2017) [M] , 哈尔滨工业大学出版社, 2018.8 .


[^0]:    收稿日期: 2019-04-05.

