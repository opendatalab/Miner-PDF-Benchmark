# 第十八期问题征解解答与点评 

## 牟晓生

第一题. 证明：从任意 9 个不同的实数中可以选出四个不同的 $a, b, c, d$, 满足

$$
(a c+b d)^{2} \geq \frac{5}{6}\left(a^{2}+b^{2}\right)\left(c^{2}+d^{2}\right)
$$

(华南师范大学中山附属中学 刘诗雄 供题)

## 证明 (根据长郡中学张騄同学的解答整理):

由于一共有 9 个实数, 我们可以取出其中 8 个 $x_{1}, y_{1}, x_{2}, y_{2}, x_{3}, y_{3}, x_{4}, y_{4}$, 使得 $x_{i}$ 与 $y_{i}$ 同号, 且不妨设 $\left|x_{i}\right| \leq\left|y_{i}\right|$. 考虑对应的四个向量 $u_{i}=\left(\left|x_{i}\right|,\left|y_{i}\right|\right)$, 它们的幅角均在 $\left[0,45^{\circ}\right]$ 之间. 由抽屉原理, 存在 $u_{i}$ 与 $u_{j}$, 它们的夹角 $\theta \leq 15^{\circ}$. 令 $a=x_{i}, b=y_{i}, c=x_{j}, d=y_{j}$, 则

$$
|a c+b d|=\left|x_{i} x_{j}+y_{i} y_{j}\right|=u_{i} \cdot u_{j}=\left|u_{i}\right|\left|u_{j}\right| \cos \theta,
$$

因此

$$
(a c+b d)^{2} \geq\left(a^{2}+b^{2}\right)\left(c^{2}+d^{2}\right) \cos ^{2} 15^{\circ}=\frac{2+\sqrt{3}}{4}\left(a^{2}+b^{2}\right)\left(c^{2}+d^{2}\right) .
$$

这比要证明的结论更强.

评注 (1). 北师大二附中夏晨曦, 东北育才学校何雨桐, 湖南师大附中刘其灵, 雅礼中学尹龙晖, 谭梓阳和王子安等同学以及湖南长沙一中团队也给出了本题的正确解答.

(2). 上面的方法还可以改进. 有兴趣的同学可以研究使得不等式成立的最优常数.

第二题. 设 $p>3$ 是素数. 证明: 组合数 $\left(\begin{array}{c}3 n \\ n\end{array}\right)$ 遍历 $(\bmod p)$ 的完整剩余系. (哈佛大学 牟晓生 供题)

证明 (根据雅礼中学刘哲成同学的解答整理):
应用 Lucas 定理可知对任意正整数 $m, n, t$, 只要 $p^{t}>3 n$ 就有

$$
\left(\begin{array}{c}
3 p^{t} m+3 n \\
p^{t} m+n
\end{array}\right) \equiv\left(\begin{array}{c}
3 m \\
m
\end{array}\right)\left(\begin{array}{c}
3 n \\
n
\end{array}\right) \quad(\bmod p)
$$

于是 $\left\{\left(\begin{array}{c}3 n \\ n\end{array}\right)\right\}$ 模 $p$ 的余数集合 $A$ 在乘法下封闭. 由于 $a^{p-2} \equiv a^{-1}(\bmod p), A$ 中非零元素在除法下也封闭.

为证 $A=\{0,1,2, \ldots, p-1\}$, 我们用归纳法. 显然 $0 \in A, 3 \in A$, 因此

$3 / 3=1 \in A$. 对 $p>3$, 则由 Lucas 定理知 $\left(\frac{3 p+3}{\frac{p+1}{2}}\right) \equiv \frac{p+3}{2}(\bmod p)$. 于是 $\frac{p+3}{2} \in A$,从而 $(p+3) /\left(\frac{p+3}{2}\right)=2 \in A$. 假设我们已有 $0,1, \ldots, k-1 \in A$, 其中 $k \geq 4$. 如果 $k$ 是合数, 那么由乘法封闭性可知 $k \in A$. 所以假设 $k>3$ 是素数, 且 $k=3 n+1$或 $3 n+2$. 此时考虑 $\frac{\left(\begin{array}{c}3 n+3 \\ n+1\end{array}\right)}{\left(\begin{array}{c}n \\ n\end{array}\right)}=\frac{3(3 n+1)(3 n+2)}{2(n+1)(2 n+1)} \in A$. 注意到 $n+1<2 n+1<k$, 因此分母 $2(n+1)(2 n+1) \in A$. 而分子是 $3 k(k \pm 1)=6 k \cdot \frac{k \pm 1}{2}$, 其中 $\frac{k \pm 1}{2}<k$ 属于 $A$. 于是用乘除法封闭性我们就能证明 $k \in A$.

评注 (1). 雅礼中学陈依一, 谢添乐以及湖南师大附中刘其灵同学也给出了本题的正确解答.

(2). 有兴趣的同学可以试着证明此题的结论对模素数幂也成立. 模一般的正整数, 目前最优的结论是 Erdös, Graham, Ruzsa 和 Straus 在 1975 年得到的:对任意不同奇素数 $p, q$, 存在无穷多个正整数 $n$ 使得 $\left(\begin{array}{c}2 n \\ n\end{array}\right)$ 与 $p q$ 互素. 我们甚至不知道是否存在无穷多个正整数 $n$ 使得 $\left(\begin{array}{c}2 n \\ n\end{array}\right)$ 与 105 互素—C Graham 奖励 1000 美金解决这个问题.

第三题. 如图, 在 $\triangle A B C$ 中, $A C>A B$, 过内心 $I$作 $A I$ 的垂线交直线 $B C$ 于 $K . E, F$ 分别在 $B A, C A$的延长线上, 使得 $B E, C F$ 均等于 $\triangle A B C$ 的半周长.证明: $E F / / A K$.

(广西钦州 卢圣 供题)



## 证明 (根据长郡中学张騄同学的解答整理):

要证 $E F / / A K$, 只要证 $\angle A E F=\angle K A B$. 而

$$
\angle A E F+\angle A F E=\angle K A B+K A F,
$$

故只需证:

$$
\frac{\sin \angle K A B}{\sin \angle K A F}=\frac{\sin \angle A E F}{\sin \angle A F E} .
$$

我们有

$$
\begin{aligned}
\frac{\sin \angle K A B}{\sin \angle K A F}=\frac{\sin \angle K A B}{\sin \angle K A C} & =\frac{K B}{K C} \cdot \frac{A C}{A B} \\
& =\frac{I B \cdot \sin \angle K I B}{I C \cdot \sin \angle K I C} \cdot \frac{A C}{A B} \\
& =\frac{I B \cdot \sin \frac{C}{2}}{I C \cdot \sin \frac{B}{2}} \cdot \frac{\sin B}{\sin C} \\
& =\frac{I B \cdot \cos \frac{B}{2}}{I C \cdot \cos \frac{C}{2}} \\
& =\frac{p-b}{p-c} \\
& =\frac{A F}{A E}=\frac{\sin \angle A E F}{\sin \angle A F E} .
\end{aligned}
$$

于是 (1) 式成立, 命题得证!

评注 上海复旦附中青浦分校林扬渊, 上海市建平中学毕其功, 北京四中胡宇征, 浙江省富阳中学黄昊中, 浙江省象山县第三中学黄子宸, 浙江省筧州二中毛恒毅, 浙江省杭州二中刘浩宇, 如东高级中学张陈成, 北师大二附中夏晨曦,东北育才学校何雨桐, 湖南师大附中刘其灵, 长沙市一中何沛予, 吴纪伯, 雅礼中学刘哲成, 谢添乐等同学也给出了本题的正确解答.

第四题. 给定正整数 $n>k \geq 2 . n$ 个小朋友坐成一圈, 他们每人都有 $m$ 顶不同颜色的帽子. 求最小的 $m=f(n, k)$, 使得无论最初分发的帽子颜色如何,都能让每个小朋友戴上一顶他的帽子, 并且任意连续 $k$ 个小朋友的帽子颜色互不相同.

(哈佛大学 牟晓生 供题)

## 证明 (根据供题者的解答整理):

答案是 $m=\left\lceil\frac{n}{\lfloor n / k\rfloor}\right\rceil$. 必要性很容易: 由条件, 每种颜色的帽子最多被 $\lfloor n / k\rfloor$个人戴, 因此至少总共有 $\frac{n}{\lfloor n / k\rfloor}$ 种不同颜色.

为证充分性, 我们首先证明只需考虑 $k \mid n$ 的情况. 假设我们已经证明那时只要每个人有 $k$ 顶帽子就可以使连续 $k$ 个人的帽子颜色互不相同. 对一般的 $n, k$, 如果 $k \nmid n$, 则

$$
m \geq \frac{n}{\lfloor n / k\rfloor}>\frac{n}{n / k}=k .
$$

我们在适当的位置加一些人 (帽子颜色随意), 使得总共有 $m\lfloor n / k\rfloor$ 个人. 由于每个人有 $m$ 顶帽子, 而 $m$ 整除 $m\lfloor n / k\rfloor$, 在此操作后我们可以使连续 $m$ 个人
的帽子颜色互不相同. 为保证原来 $n$ 个人中连续 $k$ 个人的颜色互不相同, 我们只要适当地加人, 使得原来任意连续 $k$ 个人都在操作后的某连续 $m$ 个人中. 为此, 令 $t=m\lfloor n / k\rfloor-n<\lfloor n / k\rfloor$ 表示需要加的人数. 我们可以在原来 $n$ 个人中找到 $t$ 个人, 使得每个人到下一个人的顺时针距离均为 $k$, 而最后一个人到第一个人的距离至少是 $k$. 如果在这 $t$ 个人的顺时针后面各加一个人, 则不难看出原来任意连续 $k$ 个人都在操作后的某连续 $k+1$ 个人中.

下面我们考虑 $k$ 整除 $n$, 在此情况下证明给每个人 $k$ 种颜色就足够了. 令 $A_{i} \subset \mathbb{N}$ 表示第 $i$ 个人的颜色集合. 考虑以下的多项式:

$$
P\left(x_{1}, \ldots, x_{n}\right)=\prod_{i=1}^{n} \prod_{d=1}^{k-1}\left(x_{i}-x_{i+d}\right)
$$

这样我们把原题转化为以下代数问题: 假设 $k \mid n$, 则对任意的 $k$ 元集合 $A_{1}, A_{2}, \ldots, A_{n}$, 存在 $x_{i} \in A_{i}, 1 \leq i \leq k$, 使得 $P\left(x_{1}, \ldots, x_{n}\right) \neq 0$. 注意到 $P(x)$ 的次数是 $(k-1) n=\sum_{i=1}^{n}\left(\left|A_{i}\right|-1\right)$, 因此由 Noga Alon的组合零点定理, 多项式 $P$在 $A_{1} \times A_{2} \times \cdots \times A_{n}$ 上均为零的必要条件是 $P$ 中 $\left(x_{1} \cdots x_{n}\right)^{k-1}$ 的系数为零.这个结论的证明是通过带余除法, 类似于 07 年 IMO 第六题的一种解答, 我们在这里略去.

下面我们只要证明当 $k \mid n$ 时, 多项式 $P$ 中 $\left(x_{1} \cdots x_{n}\right)^{k-1}$ 的系数非零. 如果 $k=2, n$ 是偶数, 易见这个系数是 2 . 对一般的 $k$, 直接求这个系数并不容易. 接下来的关键想法是把零点定理反过来用. 具体来说, 令 $B=\{0,1, \ldots, k-1\}$, 考虑 $P$ 在 $B \times B \times \cdots \times B$ 上的取值. 那么由差分公式, 我们有

$$
\begin{aligned}
((k-1) !)^{n} \lambda & =\Delta_{1}^{k-1} \cdots \Delta_{n}^{k-1}\left(P\left(x_{1}, x_{2}, \ldots, x_{n}\right)\right) \\
& =\sum_{0 \leq b_{1}, b_{2}, \ldots, b_{n} \leq k-1}(-1)^{n(k-1)-\sum b_{i}} \cdot \prod_{i=1}^{n}\left(\begin{array}{c}
k-1 \\
b_{i}
\end{array}\right) \cdot P\left(b_{1}, b_{2}, \ldots, b_{n}\right),
\end{aligned}
$$

其中 $\lambda$ 是 $P$ 中 $\left(x_{1} \cdots x_{n}\right)^{k-1}$ 的系数, 而 $\Delta_{i}$ 是第 $i$ 维的差分算子.

现在注意到 $P\left(b_{1}, b_{2}, \ldots, b_{n}\right) \neq 0$ 当且仅当 $b_{1}, b_{2}, \ldots, b_{k}$ 是 $0,1, \ldots, k-1$ 的一个排列, 且 $b_{i+k}=b_{i}, \forall i$. 并且此时

$$
P\left(b_{1}, b_{2}, \ldots, b_{n}\right)=\left(\prod_{0 \leq i<j \leq k-1}-(j-i)^{2}\right)^{\frac{n}{k}}
$$

代入 (3) 式, 我们得到

$$
((k-1) !)^{n} \lambda=k ! \cdot(-1)^{\frac{n(k-1)}{2}} \cdot\left(\prod_{i=0}^{k-1}\left(\begin{array}{c}
k-1 \\
i
\end{array}\right) \cdot \prod_{0 \leq i<j \leq k-1}-(j-i)^{2}\right)^{\frac{n}{k}} .
$$

化简得到 $\lambda=k !$, 于是命题得证!

评注 (1). 本题 $n=100, k=2$ 的情况是俄罗斯早年的一道竞赛题. 在那特殊情况下归纳法或许更直接, 但是出题者的最初思路就是用多项式方法.

(2). 本题是图论中的列染色数问题, 而用到的多项式方法出现在 Alon 和 Tarsi 1992 年的论文. 之后 Alon, Nathanson 和 Rusza 用类似方法对 CauchyDavenport 定理以及相关的组合数论问题进行了研究. 近年, 多项式方法被成功应用于有限域上的 Kakeya 猜想, 以及 Erdös 互异距离问题. 在之前的一期专栏上, 张瑞祥对后者进行了深入介绍.

