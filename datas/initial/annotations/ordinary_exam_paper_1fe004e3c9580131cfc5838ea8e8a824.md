# 线代期中考试试卷解析（2019.11.11） 

一、(本题 10 分）设有下列 $n$ 阶行列式:

$D_{n}=\left|\begin{array}{cccccc}4 & 1 & 0 & \cdots & 0 & 0 \\ 4 & 4 & 1 & 0 & \cdots & 0 \\ 0 & 4 & 4 & 1 & 0 & \cdots \\ & & \cdots & & \\ 0 & \cdots & 0 & 4 & 4 & 1 \\ 0 & 0 & \cdots & 0 & 4 & 4\end{array}\right|$, 试证明: $D_{n}=(1+n) 2^{n}$.

证: 用数学归纳法. 当 $n=1$ 时, $D_{1}=4=2^{2}=(1+n) 2^{n}$, 即命题成立; 当 $n=2$时, $D_{2}=12=3 \times 4=(1+n) 2^{n}$, 即命题也成立. 假设当 $n<k, k \geq 3$ ( $k$ 为正整数) 时, 命题成立, 即 $\forall n=1, \ldots, k-1, D_{n}=(1+n) 2^{n}$, 则当 $n=k$ 时, 按第一列展 开 有 $D_{k}=4 D_{k-1}-4 D_{k-2}=4(1+k-1) 2^{k-1}-4(1+k-2) 2^{k-2}=(1+$ $k) 2^{k}$. 从而有 $\forall n \in Z^{+}, D_{n}=(1+n) 2^{n}$. 证毕.

二、(本题 10 分) 设 $\alpha=(1,0,-1)^{T}$, 矩阵 $A=\alpha \alpha^{T}$. 又设 $n$ 为一正整数, 试求 $\mid 2 E-$ $\left(A^{*}\right)^{n}+A^{n} \mid$.

解: 由于 $A=\alpha \alpha^{T}=\left(\begin{array}{llr}1 & 0 & -1 \\ 0 & 0 & 0 \\ -1 & 0 & 1\end{array}\right)$. 故 $A^{*}=O_{3 \times 3}$, 其中 $O_{3 \times 3}$ 为三阶零矩阵, 于是 $\left(A^{*}\right)^{n}=O_{3 \times 3}$, 又 $A^{n}=\left(\alpha \alpha^{T}\right)^{n}=\alpha\left(\alpha^{T} \alpha\right)\left(\alpha^{T} \ldots \alpha\right)=2^{n-1} \alpha \alpha^{T}=2^{n-1} A$. 于 是 $\left|2 E-\left(A^{*}\right)^{n}+A^{n}\right|=\left|2 E+2^{n-1} A\right|=\left|\begin{array}{ccc}2+2^{n-1} & 0 & -2^{n-1} \\ 0 & 2 & 0 \\ -2^{n-1} & 0 & 2+2^{n-1}\end{array}\right|=8+2^{n+2}$.三、(本题 15 分) 设有实方阵 $A=\left(\begin{array}{ccc}1 & 3 & 9 \\ 2 & 0 & 6 \\ -3 & 1 & -7\end{array}\right), B=\left(\begin{array}{ccc}0 & a & b \\ 1 & 2 & 1 \\ -1 & 1 & 0\end{array}\right)$, 其中 $a, b$ 为实常数. 已知 $r(A)=r(B)$, 且线性方程组 $A X=(b, 1,0)^{T}$ 有解, 试求 $a, b$ 的值.解：对线性方程组 $A X=(b, 1,0)^{T}$ 的增广矩阵作初等行变换得:

$\left(\begin{array}{cccc}1 & 3 & 9 & b \\ 2 & 0 & 6 & 1 \\ -3 & 1 & -7 & 0\end{array}\right) \rightarrow\left(\begin{array}{cccc}1 & 3 & 9 & b \\ 0 & -6 & -12 & 1-2 b \\ 0 & 10 & 20 & 3 b\end{array}\right) \rightarrow\left(\begin{array}{cccc}1 & 3 & 9 & b \\ 0 & 1 & 2 & \frac{2 b-1}{6} \\ & & & \frac{3 b}{10}\end{array}\right)$

$\rightarrow\left(\begin{array}{cccc}1 & 3 & 9 & b \\ 0 & 1 & 2 & \frac{2 b-1}{6} \\ 0 & 0 & 0 & \frac{3 b}{10}-\frac{2 b-1}{6}\end{array}\right)$, 因为线性方程组 $A X=(b, 1,0)^{T}$ 有解, 故其系数矩阵的秩等于其增广矩阵的秩. 因此 $\frac{3 b}{10}-\frac{2 b-1}{6}=0$, 解之得 $b=5$, 又可知 $r(A)=2$,由已知条件知 $r(B)=2$, 故 $|B|=0$, 即 $\left|\begin{array}{ccc}0 & a & 5 \\ 1 & 2 & 1 \\ -1 & 1 & 0\end{array}\right|=0$, 解之得 $a=15$.
四、(本题 20 分) 当实数 $a$ 取何值时线性方程组 $\left\{\begin{array}{c}-x_{1}-4 x_{2}+x_{3}=1 \\ a x_{2}-3 a x_{3}=3 \\ x_{1}+3 x_{2}+(a+1) x_{3}=0\end{array}\right.$ 无解,有唯一解，有无穷多解? 有解时请求出所有解.

解：对其增广矩阵进行初等行变换可得:

$\bar{A}=\left(\begin{array}{cccc}-1 & -4 & 1 & 1 \\ 0 & a & -3 a & 3 \\ 1 & 3 & (a+1) & 0\end{array}\right) \rightarrow\left(\begin{array}{cccc}-1 & -4 & 1 & 1 \\ 0 & a & -3 a & 3 \\ 0 & -1 & (a+2) & 1\end{array}\right)$

$\rightarrow\left(\begin{array}{cccc}-1 & -4 & 1 & 1 \\ 0 & -1 & (a+2) & 1 \\ 0 & a & -3 a & 3\end{array}\right) \rightarrow\left(\begin{array}{cccc}-1 & -4 & 1 & 1 \\ 0 & -1 & (a+2) & 1 \\ 0 & 0 & a^{2}-a & a+3\end{array}\right)$

于是有:

当 $a=0$ 或 1 时, 由于 $r(A)=2 \neq 3=r(\bar{A})$, 故原方程组无解;

当 $a \neq 0$ 且 $a \neq 1$ 时, 由于 $r(A)=r(\bar{A})=3=$ 未知数个数, 故原方程组有唯一解,此时解为 $\left(x_{1}, x_{2}, x_{3}\right)=\left(\frac{-a^{2}-22 a-21}{a^{2}-a}, \frac{6 a+6}{a^{2}-a}, \frac{a+3}{a^{2}-a}\right)$;

由上分析亦知没有实数 $a$ 使得该线性方程组有无穷多解.

五、(本题 15 分) 设 $A=\left(\begin{array}{llll}k & 1 & 1 & 1 \\ 1 & k & 1 & 1 \\ 1 & 1 & k & 1 \\ k & k & k & k\end{array}\right)$, 其中 $k$ 为实常数, 试求 $A$ 的秩 $r(A)$.

解：对 $A$ 作初等行变换得：

$A=\left(\begin{array}{cccc}k & 1 & 1 & 1 \\ 1 & k & 1 & 1 \\ 1 & 1 & k & 1 \\ k & k & k & k\end{array}\right) \rightarrow\left(\begin{array}{cccc}1 & 1 & k & 1 \\ 1 & k & 1 & 1 \\ k & 1 & 1 & 1 \\ k & k & k & k\end{array}\right) \rightarrow\left(\begin{array}{cccc}1 & 1 & k & 1 \\ 0 & k-1 & 1-k & 0 \\ 0 & 1-k & 1-k^{2} & 1-k \\ 0 & 0 & k-k^{2} & 0\end{array}\right)$

$\rightarrow\left(\begin{array}{cccc}1 & 1 & k & 1 \\ 0 & k-1 & 1-k & 0 \\ 0 & 1-k & 1-k^{2} & 1-k \\ 0 & 0 & k-k^{2} & 0\end{array}\right) \rightarrow\left(\begin{array}{cccc}1 & 1 & k & 1 \\ 0 & k-1 & 1-k & 0 \\ 0 & 0 & 2-k-k^{2} & 1-k \\ 0 & 0 & k-k^{2} & 0\end{array}\right)$

于是有:

当 $k=1$ 时,$r(A)=1$;

当 $k=0$ 时, $r(A)=3$;

当 $k \neq 0$ 且 $k \neq 1$ 时, $r(A)=4$.

六、(本题 20 分) 设 $A, B$ 为 $n$ 阶方阵, 试证明:

(1) $\operatorname{tr}(A+B)=\operatorname{tr} A+\operatorname{tr} B$

(2) $\operatorname{tr}(A B)=\operatorname{tr}(B A)$

(3) 设 $P$ 是一个 $n$ 阶可迸矩阵, 则有 $\operatorname{tr}\left(P^{-1} A P\right)=\operatorname{tr} A$;

(4) 若 $A=E_{i j}$, 其中 $E_{i j}$ 是第 $i$ 行第 $j$ 列处的元素为 1 , 其余元素为全部为零的 $n$ 阶方阵, 试求 $\operatorname{tr} A$.
证 (1) : 设 $A=\left(a_{i j}\right), B=\left(b_{i j}\right)$, 则有 $\operatorname{tr} A=\sum_{k=1}^{n} a_{k k} ， \operatorname{tr} B=\sum_{k=1}^{n} b_{k k}$. 而 $A+B=$ $\left(a_{i j}+b_{i j}\right)$, 故 $\operatorname{tr}(A+B)=\sum_{k=1}^{n}\left(a_{k k}+b_{k k}\right)$, 从而有 $\operatorname{tr}(A+B)=\operatorname{tr} A+\operatorname{tr} B$;

证 (2) : 设 $A=\left(a_{i j}\right), B=\left(b_{i j}\right)$, 则有 $A B=\left(\sum_{k=1}^{n} a_{i k} b_{k j}\right), B A=\left(\sum_{k=1}^{n} b_{i k} a_{k j}\right)$, 于是有 $\operatorname{tr}(A B)=\sum_{m=1}^{n} \sum_{k=1}^{n} a_{m k} b_{k m}, \operatorname{tr}(B A)=\sum_{m=1}^{n} \sum_{k=1}^{n} b_{m k} a_{k m}$, 于是可得: $\operatorname{tr}(A B)=\operatorname{tr}(B A)$

证 (3) : 利用 (2) 可直接得, 将 $P^{-1}$ 看成 $A, A P$ 看成 $B$ 再利用矩阵乘法的结合律即可;证 (4) $:$ 直接计算可得: $\operatorname{tr} E_{i j}=\delta_{i j}$.

七、(本题 5 分）设 $A$ 是一个 $n(\geq 2)$ 阶方阵. $A^{*}$ 是 $A$ 的伴随矩阵. 若存在 $n$ 维非零列向量 $\alpha$ 使得 $A \alpha=\theta$, 其中 $\theta$ 为 $n$ 维零列向量. 且非齐次线性方程组 $A^{*} X=\alpha$ 有解, 试证明: $r(A)=n-1$.

证: 因为由题意知齐次线性方程组 $A \alpha=\theta$ 有非零解, 故 $r(A) \leq n-1$, 再证 $r(A) \geq$ $n-1$. 用反证法，假设 $r(A)<n-1$, 则 $A^{*}$ 为 $n$ 阶零矩阵. 从而非齐次线性方程组 $A^{*} X=\alpha$ 无解, 与题设非齐次线性方程组 $A^{*} X=\alpha$ 有解矛盾. 于是有 $r(A) \geq n-1$.于是命题得证.

八、(本题 5 分) 设 $A$ 为 $n$ 阶可逆矩阵. $\alpha, \beta$ 为两个 $n$ 维列向量. 试证明: $\left|A+\alpha \beta^{T}\right|=$ $|A|+\beta^{T} A^{*} \alpha$.

证法一：由

$$
\begin{aligned}
\left|\begin{array}{cc}
A & \alpha \\
-\beta^{T} & 1
\end{array}\right| & =\left|\begin{array}{cc}
A & \alpha \\
0 & 1+\beta^{T} A^{-1} \alpha
\end{array}\right|=|A|\left(1+\beta^{T} A^{-1} \alpha\right)=|A|+\beta^{T}|A| A^{-1} \\
& =|A|+\beta^{T} A^{*} \alpha
\end{aligned}
$$

又

$\left|\begin{array}{cc}A & \alpha \\ -\beta^{T} & 1\end{array}\right|=\left|\begin{array}{cc}A+\alpha \beta^{T} & \alpha \\ 0 & 1\end{array}\right|=\left|A+\alpha \beta^{T}\right|$.

因此命题得证.

证法二: $\left|A+\alpha \beta^{T}\right|=\left|A+A A^{-1} \alpha \beta^{T}\right|=\left|A\left(E+A^{-1} \alpha \beta^{T}\right)\right|=|A|\left|E+A^{-1} \alpha \beta^{T}\right|$.

下面先证结论: 设 $A_{n \times m}, B_{m \times n}, n \geq m$, 则 $\left|\lambda E_{n}-A B\right|=\lambda^{n-m}\left|\lambda E_{m}-B A\right|(\lambda \neq 0)$.证: 因为 $\lambda \neq 0$, 考虑分块矩阵的行列式:

$\left|\begin{array}{cc}\lambda E_{n} & A \\ B & E_{m}\end{array}\right| \xrightarrow{r_{2}-\left(\frac{1}{\lambda} B\right) r_{1}}=\left|\begin{array}{cc}\lambda E_{n} & A \\ 0 & E_{m}-\frac{1}{\lambda} B A\end{array}\right|=\lambda^{n}\left|E_{m}-\frac{1}{\lambda} B A\right|=\lambda^{n-m}\left|\lambda E_{m}-B A\right|$.

另一方面, $\left|\begin{array}{cc}\lambda E_{n} & A \\ B & E_{m}\end{array}\right| \xrightarrow{r_{1}-A r_{2}}=\left|\begin{array}{cc}\lambda E_{n}-A B & 0 \\ B & E_{m}\end{array}\right|=\left|\lambda E_{n}-A B\right|$.

因此, 综上有: $\left|\lambda E_{n}-A B\right|=\lambda^{n-m}\left|\lambda E_{m}-B A\right|$, 证毕.

（这个结论回忆线代第五次习题课补充题目，或参考课本附录四例 4.1 (2) )由公式 $\left|\lambda E_{n}-A B\right|=\lambda^{n-m}\left|\lambda E_{m}-B A\right|(\lambda \neq 0)$ 可知, 当 $\lambda, m$ 均取值为 1 时，有: $\left|E+A^{-1} \alpha \beta^{T}\right|=1^{n-1}\left|1+\beta^{T} A^{-1} \alpha\right|=1+\beta^{T} A^{-1} \alpha=1+\beta^{T} \frac{A^{*}}{|A|} \alpha$, 于是有: $\left|A+\alpha \beta^{T}\right|=|A|\left|E+A^{-1} \alpha \beta^{T}\right|=|A|\left(1+\beta^{T} \frac{A^{*}}{|A|} \alpha\right)=|A|+\beta^{T} A^{*} \alpha$. 证毕.

(注意: 一定要强调利用了公式 $\left|\lambda E_{n}-A B\right|=\lambda^{n-m}\left|\lambda E_{m}-B A\right|(\lambda \neq 0)$, 最好再把这个公式证明一遍, 不可以直接得 $\left|E+A^{-1} \alpha \beta^{T}\right|=1+\beta^{T} A^{-1} \alpha$, 要体现出你不是在强行凑相等. 题目核心就是分块矩阵初等变换, 大家注意体会.)

证法三: 设 $A=\left(\begin{array}{cccc}a_{11} & a_{12} & \cdots & a_{1 n} \\ a_{21} & a_{22} & \cdots & a_{2 n} \\ & \cdots & & 2 \\ a_{n 1} & a_{n 2} & \cdots & a_{n n}\end{array}\right), \alpha=\left(\begin{array}{c}\alpha_{1} \\ \alpha_{2} \\ \vdots \\ \alpha_{n}\end{array}\right), \beta=\left(\begin{array}{c}\beta_{1} \\ \beta_{2} \\ \vdots \\ \beta_{n}\end{array}\right)$, 则:

$\left|A+\alpha \beta^{T}\right|=\left|\begin{array}{cccc}a_{11}+\alpha_{1} \beta_{1} & a_{12}+\alpha_{1} \beta_{2} & \cdots & a_{1 n}+\alpha_{1} \beta_{n} \\ a_{21}+\alpha_{2} \beta_{1} & a_{22}+\alpha_{2} \beta_{2} & \cdots & a_{2 n}+\alpha_{2} \beta_{n} \\ a_{n 1}+\alpha_{n} \beta_{1} & a_{n 2}+\alpha_{n} \beta_{2} & \cdots & a_{n n}+\alpha_{n} \beta_{n}\end{array}\right|$

$=\left|\begin{array}{cccc}a_{11} & a_{12} & \cdots & a_{1 n} \\ a_{21} & a_{22} & \cdots & a_{2 n} \\ & \cdots & & \\ a_{n 1} & a_{n 2} & \cdots & a_{n n}\end{array}\right|+\sum_{i=1}^{n}\left|\begin{array}{ccccc}a_{11} & \cdots & \alpha_{1} \beta_{i} & \cdots & a_{1 n} \\ a_{21} & \cdots & \alpha_{2} \beta_{i} & \cdots & a_{2 n} \\ & & \cdots & & \\ a_{n 1} & \cdots & \alpha_{n} \beta_{i} & \cdots & a_{n n}\end{array}\right|$.

(按列拆分共有 $2^{n}$ 项，但是只有该 $(n+1)$ 项不为 0 ，其余项均为 0$)$由于

![](https://cdn.mathpix.com/cropped/2024_05_06_9a6fca4ddf6a42732e43g-4.jpg?height=214&width=1253&top_left_y=1178&top_left_x=296)
故 $\left|A+\alpha \beta^{T}\right|=|A|+\beta^{T} A^{*} \alpha$, 证毕.

