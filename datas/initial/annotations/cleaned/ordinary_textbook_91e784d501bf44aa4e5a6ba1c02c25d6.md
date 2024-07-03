数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 2022 年匈牙利 Kürschák 竞赛试题解析 

汤礼达

(湖南师范大学附属中学, 410006)

匈牙利是数学竞赛的发源地, 而 Kürschák 竞赛是全球范围内历史最悠久的数学竞赛. 2022 年 Kürschák 竞赛试题考察的思想方法比较典型, 是联赛训练较好的素材. 感谢微信公众号 “恩次方根” 提供的试题. 直于水平, 不当之处, 敬请读者批评指正.

题 1 将一个正方形划分为 2022 个矩形, 其中任意两个矩形在正方形内部没有公共顶点, 由这些矩形的边组成的线段长度至多有多少个不同的值?

解 我们证明所有分界线方向均相同, 即划分必形如



假设存在一个矩形在正方形内部有顶点, 设这个矩形为 $A B C D, D$ 在正方形内部。

用 $A D, C D$ 所在直线把正方形划为 4 个区域, 易知此划分中每个矩形都不能与至少 3 个区域有公共内点, 故 $D$ 点除 $B D, A D$ 外还引出一条分界线.



不妨设它与 $A D$ 共线, 则以这条分界线和 $C D$ 为边有一个以 $D$ 为顶点的矩形, 它与 $A B C D$ 在正方形内有公共顶点 $D$, 矛盾!

修订日期: 2022-12-09.
因此, 所有矩形的顶点均在边界上, 故每一个矩形要么与上边界和下边界都有公共边, 要么与左边界和右边界都有公共边. 故此划分必为



故不同长度最多有 $\left(\begin{array}{c}2023 \\ 2\end{array}\right)$ 个.

评注 本题是常规的组合问题, 只需注意到所有的分界线方向均相同即可.

题 2 设 $p$ 和 $q$ 均为 $4 k+3$ 型的素数. 假设存在非零整数 $x$ 和 $y$ 满足 $x^{2}-p q y^{2}=1$. 求证: 存在正整数 $a$ 和 $b$ 满足 $\left|p a^{2}-q b^{2}\right|=1$.

证明 由于 $p q y^{2}=x^{2}-1=(x-1)(x+1)$, 且

$$
1 \equiv x^{2}-p q y^{2} \equiv x^{2}-y^{2}(\bmod 4) \Rightarrow 2 \nmid x, 2 \mid y,
$$

取所有满足要求的正整数解中使 $x$ 是最小的.

由 $2 \mid x-1$, 知 $(x-1, x+1)=(x-1,2)=2$, 由 $y \neq 0$ 知 $x>1$.

下面进行分类讨论:

(1) 若 $p|x-1, q| x+1$, 存在 $s, v \in \mathbb{Z}_{+}$,

$$
x-1=2 p s^{2}, x+1=2 q v^{2}, 1=q v^{2}-p s^{2} .
$$

(2) 若 $q|x-1, p| x+1$, 存在 $s, v \in \mathbb{Z}_{+}$,

$$
x-1=2 q s^{2}, x+1=2 p v^{2}, 1=p v^{2}-q s^{2} .
$$

(3) 若 $p q \mid x-1$, 存在 $s, v \in \mathbb{Z}_{+}$,

$$
x-1=2 p q s^{2}, x+1=2 v^{2}, v^{2}-p q s^{2}=1
$$

但 $x+1=2 v^{2} \geq 2 x^{2} \Rightarrow \frac{1}{x}+\frac{1}{x^{2}} \geq 1 \Rightarrow x \leq 1$, 矛盾.

(4) 若 $p q \mid x+1$, 存在 $s, v \in \mathbb{Z}_{+}$,

$$
x-1=2 s^{2}, x+1=2 q p v^{2}, p q v^{2}=s^{2}+1 \Rightarrow p \mid s^{2}+1
$$

而 $p \equiv 3(\bmod 4) \Rightarrow\left(\frac{-1}{p}\right)=-1$, 矛盾!

综上所述, 命题成立!

评注 本题为中档偏易的 Pell 型问题但具有较强的迷惑性, 容易联系 Pell 方程的证明而想偏，利用不定方程的因式分解视角可较快找到解决问题的办
法.

题 $3 n^{2}$ 个实数 $a_{i, j}(1 \leq i \leq n, 1 \leq j \leq n)$ 满足对任意 $i$ 和 $j, a_{i, j}+a_{j, i}=0$ (特别地, 对任意 $i, a_{i, i}=0$ ). 求证:

$$
\frac{1}{n} \sum_{i=1}^{n}\left(\sum_{j=1}^{n} a_{i, j}\right)^{2} \leq \frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} a_{i, j}^{2}
$$

证明 注意到

$$
\begin{aligned}
& \frac{n}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} a_{i, j}^{2}-\sum_{i=1}^{n}\left(\sum_{j=1}^{n} a_{i, j}\right)^{2} \\
= & n \sum_{1 \leq i<j \leq n} a_{i, j}^{2}-\sum_{i=1}^{n}\left(\sum_{j=i+1}^{n} a_{i, j}-\sum_{j=1}^{i-1} a_{j, i}\right)^{2} \\
= & n \sum_{1 \leq i<j \leq n} a_{i, j}^{2}-\sum_{i=1}^{n}\left(\sum_{j=i+1}^{n} a_{i, j}^{2}+\sum_{j=1}^{i-1} a_{j, i}^{2}+2 \sum_{1 \leq i<j<k \leq n} a_{i, j} a_{i, k}\right. \\
& \left.+2 \sum_{1 \leq j<k<i \leq n} a_{j, i} a_{k, i}-2 \sum_{1 \leq j<i<k \leq n} a_{j, i} a_{i, k}\right) \\
= & n \sum_{1 \leq i<j \leq n} a_{i, j}^{2}-2 \sum_{1 \leq i<j \leq n} a_{i, j}^{2}-2 \sum_{1 \leq i<j<k \leq n}\left(a_{i, j} a_{i, k}+a_{i, k} a_{j, k}-a_{i, j} a_{j, k}\right) \\
= & \sum_{1 \leq i<j<k \leq n}\left(a_{i, j}+a_{j, k}-a_{i, k}\right)^{2} \geq 0 .
\end{aligned}
$$

故证毕.

评注 处理这种二次型不等式自然想到配方, 再从小情形出发容易观察出配方的结构, 便能得以解决.

