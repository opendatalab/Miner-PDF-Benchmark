$$
\text { 数学新星网 米解答展示 }
$$

www.nsmath.cn/jdzs

# 第二十期问题征解解答与点评 

牟晓生

第一题. 对每个非负整数 $k$, 令 $N(k)$ 为满足 $2017^{k} \| n$ ! 的正整数 $n$ 的个数.求 $N(k)$ 的所有可能值.

(广西南宁二中学生 陈宝麟 供题)

## 解 (根据长郡中学秦珺辉同学的解答整理):

首先注意到 2017 是素数. 若 $k=0$, 显然 $N(k)=2016$. 对于 $k \geq 1$, 若存在正整数 $n$ 使得 $2017^{k} \| n !$, 那么这个最小的 $n=n_{0}$ 一定是 2017 的倍数. 于是 $n_{0}, n_{0}+1, \ldots, n_{0}+2016$ 都符合条件, 而对任意 $n \geq n_{0}+2017$ 都有 $2016^{k+1} \mid n$ !所以要么 $N(k)=0$, 要么 $N(k)=2017$.

故 $N(k)$ 的所有可能值为 $0,2016,2017$.

评注 湖南师大附中石恺宁, 长郡中学彭永坚以及东北育才学校何雨桐同学也给出了本题的正确解答.

第二题. 设 $M$ 是一个 $m \times n$ 的整数数表, 其中 $1 \leq m \leq n$. 允许对 $M$ 进行如下操作: 任取一行或一列, 将其中的数同时加上某个整数 $a$. 假设 $M$ 中恰有 $r$个数为 1 , 其余的数都为 -1 , 而 $1 \leq r<m$. 证明: 无法通过有限次操作使得 $M$中所有数都相等.

(深圳高级中学 冯跃峰 供题)

证明 (根据长郡中学彭永坚同学的解答整理):

以 $M_{i j}$ 表示 $M$ 中第 $i$ 行第 $j$ 列的数. 由条件不妨设 $M_{11}=1$. 对每个 $2 \leq i \leq m$, 考虑 $M_{1 i}, M_{i 1}, M_{i i}$ 这三个数. 由于 $M$ 中至多有 $m-1$ 个 “ 1 ” ,一定存在某个 $i$ 使得这三个数都是 “ -1 ” 。

注意到 $M_{11}+M_{i i}-M_{1 i}-M_{i 1}$ 在每次操作下保持不变, 而一开始它的值为 2, 因此无论如何都无法使这四个数相等.

评注 (1). 重庆南开中学朱棣文, 湖南师大附中石恺宁, 长郡中学秦珺辉以
及东北育才学校何雨桐同学也给出了本题的正确解答.

(2). 另一种证明方法是把问题归结为 $m=n=r+1$ 的情况, 然后注意到表中所有数之和模 $r+1$ 的余数在操作下不变.

第三题. 在三角形 $A B C$ 中, $O$ 是外心, $M$ 是 $B C$ 的中点. $P$ 在三角形内,满足 $A, O, P, M$ 共圆. $J$ 是 $A B$ 上的点, 使得 $\angle J M C=\angle A P C$. 同样地, $K$ 是 $A C$ 上的点, 使得 $\angle K M B=\angle A P B$. 证明: $B, J, K, C$ 共圆.

(浙江省象山县第三中学学生 黄子宸 供题)

## 证明 (根据浙江省淮州二中毛恒毅同学的解答整理):

![](https://cdn.mathpix.com/cropped/2024_02_26_795f487895556efff25bg-2.jpg?height=631&width=612&top_left_y=918&top_left_x=722)

延长 $A P$ 交 $\triangle A B C$ 的外接圆于点 $X$. 由条件 $\angle B P X=\angle C M K, \angle B X P=$ $\angle B C A$, 于是 $\triangle B P X \sim \triangle K M C$.

同理 $\triangle C P X \sim \triangle J M B$. 因此

$$
\frac{J M}{B M}=\frac{C P}{X P}, \frac{K M}{C M}=\frac{B P}{X P}
$$

从而 $\frac{J M}{K M}=\frac{C P}{B P}$.

作 $\triangle B P C$ 的外接圆 $\omega$, 延长 $P M$ 交 $\omega$ 于另一点 $N$. 由 $M$ 为 $B C$ 中点知 $\frac{C P}{B P}=\frac{B N}{C N}$, 所以 $\frac{J M}{K M}=\frac{B N}{C N}$. 而

$$
\begin{aligned}
\angle B N C & =\pi-\angle B P C=\pi-\angle B P X-\angle C P X \\
& =\pi-\angle B M J-\angle C M K=\angle J M K
\end{aligned}
$$

所以 $\triangle J M K \sim \triangle B N C$. 我们有

$$
\begin{aligned}
\angle J K C & =\angle C K M+\angle J K M=\angle C K M+\angle B C N \\
& =\angle X B P+\angle B P N=\pi-\angle B X P-\angle B P X+\angle B P N
\end{aligned}
$$

$$
\begin{aligned}
& =\pi-\angle B C A+\angle X P M=\pi-\angle C+\pi-\angle A O M \\
& =\pi-\angle C+(\angle C-\angle B)=\pi-\angle B .
\end{aligned}
$$

故 $B, C, K, J$ 四点共圆, 证毕!

评注 长郡中学秦珺辉, 彭永坚, 东北育才学校何雨桐同学以及湖南省雅礼中学团队也给出了本题的正确解答.

第四题. 给定正整数 $n$ 以及非负实数 $l_{i j}(1 \leq i<j \leq n)$. 是否一定存在非负实数 $a_{1}, a_{2}, \ldots, a_{n}$, 满足 $\left|a_{i}-a_{j}\right| \geq l_{i j}(\forall i<j)$, 并且 $\sum_{k=1}^{n} a_{k} \leq \sum_{i<j} l_{i j}$ ?

(哈佛大学 牟晓生 供题)

## 解 (根据东北育才学校何雨桐同学的解答整理):

为方便起见, 我们对所有 $i<j$ 令 $l_{j i}=l_{i j}$. 取 $i_{1}=1$, 取 $i_{2} \neq i_{1}$ 使得 $l_{i_{1} i_{2}}$ 最小, 再取 $i_{3} \neq i_{1}, i_{2}$ 使得 $l_{i_{1} i_{3}}+l_{i_{2} i_{3}}$ 最小, 依次类推直到定义 $i_{1} \sim i_{n}$. 然后对每个 $1 \leq t \leq n$, 定义

$$
a_{i_{t}}=\sum_{s<t} l_{i_{s} i_{t}}
$$

这样显然有

$$
\sum_{k} a_{k}=\sum_{t} a_{i_{t}}=\sum_{t} \sum_{s<t} l_{i_{s} i_{t}}=\sum_{i<j} l_{i j}
$$

另外, 假设 $t_{2}>t_{1}$, 那么由 $i_{t_{1}}$ 的选择知道

$$
l_{i_{t_{1}} i_{t_{2}}}+a_{i_{t_{1}}}=l_{i_{t_{1}} i_{t_{2}}}+\sum_{s<t_{1}} l_{i_{s} i_{t_{1}}} \leq l_{i_{t_{1}} i_{t_{2}}}+\sum_{s<t_{1}} l_{i_{s} i_{t_{2}}} \leq a_{i_{t_{2}}}
$$

所以 $\left|a_{i}-a_{j}\right| \geq l_{i j}$ 对所有 $i, j$ 都成立. 命题得证!

评注 (1). 湖南省雅礼中学陈伊一, 汤继尧同学也给出了本题的正确解答.

(2). 这个解答看似简单, 但构造性非常强. 一个好的出发点或许是 $\sum_{k=1}^{n} a_{k} \leq$ $\sum_{i<j} l_{i j}$ 这个需要满足的条件. 由此令每个 $a_{k}$ 为若干个 $l_{i j}$ 之和是比较自然的.

