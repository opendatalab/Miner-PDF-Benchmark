# 第二十一期问题征解解答与点评 

牟晓生

第一题. 设 $a_{1}, \ldots, a_{n} \in[0,1]$. 证明:

$$
\sum_{i=1}^{n}\left[\left(\prod_{j \neq i} a_{j}\right)^{\frac{n}{2}} \cdot \sqrt{1-a_{i}}\right] \leq 1
$$

(浙江省杭州二中 赵斌 供题)

## 证法一 (根据西北师大附中张江昊同学的解答整理):

首先注意到下面的引理:

引理 对任意 $x_{1}, x_{2}, \ldots, x_{n} \in[0,1]$,

$$
1+(n-1) x_{1} x_{2} \ldots x_{n} \geq \sum_{i=1}^{n} \prod_{j \neq i} x_{j}
$$

引理的证明很简单, 只要考虑每个 $x_{i}$ 取 0 或 1 时的情况即可.

回到原题, 用柯西不等式及引理得

$$
\begin{aligned}
& {\left[\sum_{i=1}^{n}\left(\prod_{j \neq i} a_{j}\right)^{\frac{n}{2}} \cdot \sqrt{1-a_{i}}\right]^{2} } \\
= & {\left[\sum_{i=1}^{n}\left(\prod_{j \neq i} a_{j}\right)^{\frac{n-1}{2}} \cdot \sqrt{\left(1-a_{i}\right) \prod_{j \neq i} a_{j}}\right]^{2} } \\
\leq & {\left[\sum_{i=1}^{n}\left(\prod_{j \neq i} a_{j}\right)^{n-1}\right] \cdot\left[\sum_{i=1}^{n}\left(1-a_{i}\right) \prod_{j \neq i} a_{j}\right] } \\
\leq & {\left[1+(n-1)\left(a_{1} \cdots a_{n}\right)^{n-1}\right] \cdot\left[1-a_{1} \cdots a_{n}\right] . }
\end{aligned}
$$

令 $t=a_{1} \cdots a_{n}$, 则只要证明

$$
\left(1+(n-1) t^{n-1}\right)(1-t) \leq 1 \text {. }
$$

这是很显然的, 因为 $\frac{1}{1-t}>1+t+\cdots+t^{n-1}>1+(n-1) t^{n-1}$. 由此也可以看出原命题中 $\frac{n}{2}$ 这个幂次至少可以改进为 $\frac{n+2}{4}$.

证法二 (根据湖南师大附中杨学文同学的解答整理):
(i) 若存在 $a_{i}=0$, 则结论显然成立.

(ii) 不妨设所有 $a_{i}$ 均属于 $(0,1]$.

令 $a_{i}=\frac{1}{t_{i}}, i=1,2, \cdots, n$, 则 $t_{i} \geq 1$. 所证不等式等价于

$$
\sum_{i=1}^{n} \sqrt{t_{i}^{n}-t_{i}^{n-1}} \leq\left(\prod_{i=1}^{n} t_{i}\right)^{\frac{n}{2}}
$$

由 Cauchy不等式知

$$
\sum_{i=1}^{n} \sqrt{t_{i}^{n}-t_{i}^{n-1}}=\sum_{i=1}^{n} t_{i}^{\frac{n-1}{2}} \sqrt{t_{i}-1} \leq \sqrt{\left(\sum_{i=1}^{n} t_{i}^{n-1}\right)\left(\sum_{i=1}^{n}\left(t_{i}-1\right)\right)} .
$$

要证 (1) 式, 只须证

$$
\left(\sum_{i=1}^{n} t_{i}^{n-1}\right)\left(\sum_{i=1}^{n}\left(t_{i}-1\right)\right) \leq \prod_{i=1}^{n} t_{i}^{n} .
$$

其中 $t_{i} \geq 1, i=1,2, \cdots, n$.

令 $b_{i}=t_{i}-1$, 则 $b_{i} \geq 0, i=1,2, \cdots, n$. 这时 (2) 式等价于

$$
\sum_{i=1}^{n}\left(b_{i}+1\right)^{n-1} \cdot \sum_{i=1}^{n} b_{i} \leq \prod_{i=1}^{n}\left(b_{i}+1\right)^{n}
$$

下证 (3) 式. 由贝努利不等式,

$$
\begin{aligned}
\prod_{i=1}^{n}\left(b_{i}+1\right)^{n} & =\prod_{i=1}^{n}\left(b_{i}+1\right)^{n-1} \cdot \prod_{i=1}^{n}\left(b_{i}+1\right) \\
& \geq \prod_{i=1}^{n}\left(b_{i}+1\right)^{n-1}\left(1+\sum_{i=1}^{n} b_{i}\right) \\
& =\prod_{i=1}^{n}\left(b_{i}+1\right)^{n-1}+\prod_{i=1}^{n}\left(b_{i}+1\right)^{n-1} \cdot \sum_{i=1}^{n} b_{i}
\end{aligned}
$$

又由广义贝努利不等式,

$$
\prod_{i=1}^{n}\left(b_{i}+1\right)^{n-1} \geq \sum_{i=1}^{n}\left(b_{i}+1\right)^{n-1}-n+1 .
$$

另一方面，

$$
\prod_{i=1}^{n}\left(b_{i}+1\right)^{n-1} \geq \prod_{i=1}^{n}\left(1+(n-1) b_{i}\right) \geq 1+(n-1) \sum_{i=1}^{n} b_{i}
$$

由 $(4),(5),(6)$ 可知

$$
\begin{aligned}
\prod_{i=1}^{n}\left(b_{i}+1\right)^{n} & \geq 1+(n-1) \sum_{i=1}^{n} b_{i}+\left(\sum_{i=1}^{n}\left(b_{i}+1\right)^{n-1}-n+1\right) \sum_{i=1}^{n} b_{i} \\
& =\sum_{i=1}^{n} b_{i} \cdot \sum_{i=1}^{n}\left(b_{i}+1\right)^{n-1}+1 \\
& >\sum_{i=1}^{n} b_{i} \cdot \sum_{i=1}^{n}\left(b_{i}+1\right)^{n-1},
\end{aligned}
$$

即 (3) 式成立, 证毕.

评注 (1). 湖南师大附中周义云同学也给出了本题的正确解答.

(2). 对 $n$ 进行归纳与反向归纳 (类似于AM-GM) 也可以证明本题.

第二题. 如图, 三角形 $A B C$ 的高分别为 $A D, B E$, $C F . K$ 为 $\triangle D E F$ 的垂心, $L$ 为直线 $K F$ 与 $D E$ 的交点. $G, H, I$ 分别为 $F, D, E$ 在 $B C, C A, A B$ 上的垂足. $M, N$ 为 $\triangle G H I$ 的外接圆与 $\triangle A B C$ 的外接圆的交点. 证明: $K M=K N=\sqrt{K F \cdot K L}$.

![](https://cdn.mathpix.com/cropped/2024_02_26_4e02a8f79eff43ae44ecg-03.jpg?height=409&width=423&top_left_y=475&top_left_x=1316)

(北京大学学生 徐恺, 华中师大一附中学生 姚睿 供题)

## 解法一 (根据雅礼中学谭梓阳同学的解答整理):

先证明一个引理.

引理 设 $\triangle A B C$ 三边 $B C, C A, A B$ 边上高的垂足分别为 $H_{A}, H_{B}, H_{C} . H_{A}$在 $A B, A C$ 上的射影分别为 $H_{A C}, H_{A B}$. 同理定义 $H_{B A}, H_{B C} ; H_{C A}, H_{C B}$. 设 $\triangle H_{A} H_{B} H_{C}$ 的垂心为 $H_{1}$. 则 $H_{A C}, H_{A B}, H_{B A}, H_{B C}, H_{C A}, H_{C B}$ 共圆, 且其圆心为 $O H_{1}$ 中点.

![](https://cdn.mathpix.com/cropped/2024_02_26_4e02a8f79eff43ae44ecg-03.jpg?height=508&width=548&top_left_y=1499&top_left_x=754)

引理证明由于 $\angle C H_{B} H_{A}=\angle C H H_{A}=\angle C H_{C} H_{C A}=\angle C H_{C B} H_{C A}$, 故

$$
H_{B} H_{A} / / H_{C B} H_{C A}, \frac{C H_{B}}{C H_{A}}=\frac{C H_{C B}}{C H_{C A}} .
$$

又 $H_{B}, H_{A B}, H_{B A}, H_{A}$ 共圆, 故 $C H_{B} \cdot C H_{A B}=C H_{A} \cdot C H_{B A}$. 则

$$
C H_{A B} \cdot C H_{C B}=C H_{B A} \cdot C H_{C A} .
$$

这说明 $H_{A B}, H_{C B}, H_{B A}, H_{C A}$ 共圆.

同理, $H_{A B}, H_{C B}, H_{A C}, H_{B C} ; H_{B A}, H_{C A}, H_{A C}, H_{B C}$ 分别共圆.
由 Davis 定理知 $H_{A C}, H_{A B}, H_{B A}, H_{B C}, H_{C A}, H_{C B}$ 共圆.

设 $\triangle C H_{B} H_{A}, \triangle B H_{C} H_{A}$ 的垂心分别为 $H_{2}, H_{3}$. 由于 $T$ 在 $H_{C A} H_{B A}$ 及 $H_{B C} H_{A C}$ 的中垂线上. 故 $T$ 为 $H_{B} H_{3}$ 中点.

同理, $T$ 为 $H_{C} H_{2}$ 中点.

这说明 $H_{2} H_{3} H_{C} H_{B}$ 为平行四边形. $H_{2} H_{3}$ 与 $H_{B} H_{C}$ 平行且相等. 又 $H_{A} H_{B}$逆平行于 $A B$. 故 $O H_{2} \perp H_{A} H_{B}$, 结合 $H_{1} H_{C} \perp H_{A} H_{B}$ 知 $O H_{2} / / H_{1} H_{C}$.

同理 $O H_{3} / / H_{1} H_{B}$. 故 $\triangle O H_{2} H_{3} \cong \triangle H_{1} H_{C} H_{B}, O H_{3}$ 与 $H_{1} H_{B}$ 平行且相等.

故 $T$ 为 $O H_{1}$ 中点. 引理得证!

![](https://cdn.mathpix.com/cropped/2024_02_26_4e02a8f79eff43ae44ecg-04.jpg?height=520&width=548&top_left_y=831&top_left_x=754)

回到原题. 记 $\triangle A B C$ 的外接圆半径为 $R . \triangle G H I$ 的外接圆半径为 $R_{T}$. 设 $\triangle G H I$ 的外心为 $T$, 作 $E$ 在 $B C$ 上的射影 $J$.

由引理, $J$ 在 $\odot T$ 上, 且 $T$ 为 $O K$ 中点.

由于 $K$ 在 $O T$ 上, 故 $K M=K N$.

在 $\triangle O M K$ 中, 由中线长公式 $M T^{2}=\frac{1}{2} K M^{2}+\frac{1}{2} M O^{2}-O T^{2}$, 即

$$
\begin{aligned}
K M^{2} & =2 M T^{2}+2 O T^{2}-M O^{2} \\
& =2 R_{T}^{2}+2 O T^{2}-R^{2}
\end{aligned}
$$

在 $\triangle O K D$ 中, 由中线长公式 $D T^{2}=\frac{1}{2} K O^{2}+\frac{1}{2} O D^{2}-O T^{2}$, 即

$$
O T^{2}=\frac{1}{2} K D^{2}+\frac{1}{2} O D^{2}-D T^{2} .
$$

在 $\odot T$ 中, 由圆幂定理得 $T D^{2}=R_{T}^{2}-J D \cdot D G$. 故

$$
\begin{aligned}
O T^{2} & =\frac{1}{2} K D^{2}+\frac{1}{2} O D^{2}-R_{T}^{2}+J D \cdot D G, \\
K M^{2} & =K D^{2}+O D^{2}+2 J D \cdot D G-R^{2} \\
& =K D^{2}+2 J D \cdot D G-C D \cdot D B(\text { 圆幂定理 }) .
\end{aligned}
$$

设 $E F$ 交 $K D$ 于 $S$,

$$
\begin{aligned}
& K D^{2}+2 J D \cdot D G-C D \cdot D B-K F \cdot K L \\
& =K D^{2}+2 J D \cdot D G-C D \cdot D B-K S \cdot K D \\
& =D S \cdot D K+2 J D \cdot D G-C D \cdot D B \\
& =D L \cdot D E+2 J D \cdot D G-C D \cdot D B \\
& =D F \cdot D E \cdot \cos \angle F D E+2 D F \cdot D E \cdot \cos \angle F D B \cdot \cos \angle E D C-C D \cdot D B . \\
& \text { 又 } \angle F D B=\angle E D C=\angle B A C \text {. 故 } \\
& K D^{2}+2 J D \cdot D G-C D \cdot D B-K F \cdot K L \\
& =D F \cdot D E \cdot(-\cos 2 \angle B A C)+2 D F \cdot D E \cdot \cos ^{2} \angle B A C-C D \cdot D B \\
& =D F \cdot D E-C D \cdot D B=0(\triangle B D F \backsim \triangle E D C) \text {. }
\end{aligned}
$$

故 $K M^{2}-K F \cdot K L=0$.

故 $K M=K N=\sqrt{K F \cdot K L}$, 得证!

## 解法二 (根据供题者提供的解答整理):

由于这里的计算过程不是特别重要, 我们把计算过程写作一个引理.

引理 在 $\triangle A B C$ 中,

$$
\begin{aligned}
& 1+2 \cos 2 A \cos 2 B \cos 2 C \\
= & \cos ^{2} A+\cos ^{2}(B-C) \cos ^{2} 2 A+\frac{1}{2}(1-\cos 2 A)^{2} \sin ^{2}(B-C) \\
& +2 \sin ^{2} A \cos ^{2} A \cos ^{2}(B-C) .
\end{aligned}
$$

引理证明 注意到

$$
\begin{aligned}
\cos 2 A \cos 2 B \cos 2 C & =\cos 2 A \cdot \frac{1}{2}[\cos (2 B-2 C)+\cos (2 B+2 C)] \\
& =\frac{1}{2} \cos ^{2} 2 A+\cos ^{2}(B-C) \cos 2 A-\frac{1}{2} \cos 2 A
\end{aligned}
$$

设 $\alpha=2 A, \beta=B-C$, 在求证式子中取 (左 - 右) 并代入上式, 得到:

$$
\begin{aligned}
1+ & \frac{1}{2} \cos ^{2} \alpha+\cos ^{2} \beta \cos \alpha-\frac{1}{2} \cos \alpha-\frac{1}{2}(1+\cos \alpha) \\
& -\cos ^{2} \beta \cos ^{2} \alpha-\frac{1}{2}(1-\cos \alpha)^{2} \sin ^{2} \beta-\frac{1}{2} \sin ^{2} \alpha \cos ^{2} \beta \\
= & 1+\frac{1}{2} \cos ^{2} \alpha+\cos ^{2} \beta \cos \alpha-\frac{1}{2}-\cos \alpha-\left(\frac{1}{2} \cos ^{2} \beta \cos ^{2} \alpha+\frac{1}{2} \cos ^{2} \beta \cos ^{2} \alpha\right) \\
& -\left(\frac{1}{2} \sin ^{2} \beta+\frac{1}{2} \cos ^{2} \alpha \sin ^{2} \beta-\cos \alpha \sin ^{2} \beta\right)-\frac{1}{2} \sin ^{2} \alpha \cos ^{2} \beta
\end{aligned}
$$

$$
\begin{aligned}
= & \frac{1}{2}+\left(\cos ^{2} \beta \cos \alpha+\sin ^{2} \beta \cos \alpha-\cos \alpha\right) \\
& -\frac{1}{2}\left(\cos ^{2} \beta \cos ^{2} \alpha+\cos ^{2} \alpha \sin ^{2} \beta-\cos ^{2} \alpha\right) \\
& -\frac{1}{2}\left(\cos ^{2} \beta \cos ^{2} \alpha+\sin ^{2} \alpha \cos ^{2} \beta+\sin ^{2} \beta\right) \\
= & 0 .
\end{aligned}
$$

回到原题. 我们说两个结论.

(1) 如图, 我们把另外三个垂足作出来, 那么 $I, Q, J, G, P, H$ 六个点共圆.

![](https://cdn.mathpix.com/cropped/2024_02_26_4e02a8f79eff43ae44ecg-06.jpg?height=343&width=531&top_left_y=791&top_left_x=768)

证明如下:

由于 $\angle A J H=\angle A D H=\angle A C B=\angle A Q I$, 那么我们就有 $I, J, Q, H$ 共圆.

同理有 $I, J, G, P$ 以及 $E, H, G, P$ 共圆.

如果这六个点不共圆那么这里共的三个圆两两的根轴分别是 $A B, B C, C A$并不是三线共点, 矛盾. 那么这六点共圆.

记这个圆圆心是 $R$, 我们再次证明一个结论:

(2) $R$ 是 $O K$ 中点, 其中 $O$ 是三角形 $A B C$ 外心.

我们先证明, $R$ 在 $B C$ 上投影是 $K, O$ 在 $B C$ 上投影的中点, 如果这个证明完毕, 那么 $R$ 在 $C A$ 上也表现出相同的性质, 继而可以采用斜坐标记法证明 $R$是 $O, K$ 中点.

![](https://cdn.mathpix.com/cropped/2024_02_26_4e02a8f79eff43ae44ecg-06.jpg?height=508&width=548&top_left_y=2005&top_left_x=754)

我们建立平面直角坐标系, 以 $D$ 为原点. 那么我们只需证 $2 X_{R}=X_{O}+X_{K}$,
这里设 $T$ 是 $B C$ 中点也是 $O$ 往 $B C$ 作垂线的垂足, $S$ 是 $K$ 往 $B C$ 的投影, $U$ 是 $I Q$ 中点.

我们知道 $I Q / / B C$, 并且长度比是 $\frac{I Q}{B C}=\frac{A Q}{A C}=\frac{A Q}{A E} \cdot \frac{A E}{A C}=\cos ^{2} A$.

那么由于 $A, U, T$ 共线以及 $I Q$ 中垂线过 $R$ 我们有

$$
X_{R}=X_{U}=\frac{I Q}{B C} X_{T}=\cos ^{2} A X_{T}=\cos ^{2} A X_{O}
$$

由熟知结论, $K D$ 和 $A O$ 平行而且

$$
K D=2 R_{1} \cdot \cos \angle F D E=-R_{0} \cdot \cos 2 A .
$$

这里式子的 $R_{0}$ 是 $\triangle A B C$ 外接圆半径, $R_{1}$ 是 $\triangle D E F$ 的外接圆半径.

那么 $\overrightarrow{K D}=-\cos 2 A \overrightarrow{A O}$, 即 $X_{K}=\cos 2 A X_{O}$, 由于 $\cos 2 A+1=2 \cos ^{2} A$.我们就有 $2 X_{R}=X_{O}+X_{K}$. 故 $R$ 是 $O K$ 中点.

现在我们来证明原题.

注意到第二个结论里面蕴含了两个圆心和 $K$ 共线, 那么 $K M=K N$ 是显然的了.

设 $S, T$ 是 $K, O$ 在 $B C$ 上投影, 由于我们知道一个基本事实: 到两点距离的平方和是一个定值 (这个定值需要一定范围) 的轨迹是一个圆.

那么以 $K$ 为圆心, $\sqrt{K F \cdot K L}$ 为半径做的圆也过 $M, N$ 的充分必要条件是

$$
K F \cdot K L+R_{0}^{2}=K X^{2}+O X^{2} .
$$

其中 $X$ 是圆 $R$ 上面的任何一点.

由第二个结论我们还可以知道, $S G=P T$ (因为 $G P$ 中垂线也过 $R$ ).

分别取 $X$ 为 $P$ 和 $G$ 我们知道

$$
\begin{aligned}
K X^{2}+O X^{2} & =\frac{K G^{2}+O G^{2}+K P^{2}+O P^{2}}{2} \\
& =K S^{2}+O T^{2}+\frac{1}{2}\left(P G^{2}+S T^{2}\right)
\end{aligned}
$$

所以我们只需证

$$
K F \cdot K L+R_{0}^{2}=K S^{2}+O T^{2}+\frac{1}{2}\left(P G^{2}+S T^{2}\right) .
$$

现在我们正式的需要这个图了, 我们一一来看:

$$
\begin{aligned}
K F & =2 R_{1} \cdot \cos 2 C=R_{0} \cdot \cos 2 C, \\
K L & =K E \cos \angle E K L=2 R_{1} \cdot \cos (\pi-2 B) \cdot \cos (\pi-2 A)=R_{0} \cdot \cos 2 B \cos 2 A, \\
K S & =K D \cdot \cos \angle O A D=-\cos 2 A \cdot A O \cdot \cos (B-C) \\
& =-R_{0} \cdot \cos 2 A \cos (B-C) O T=R_{0} \cdot \cos A,
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_02_26_4e02a8f79eff43ae44ecg-08.jpg?height=520&width=548&top_left_y=208&top_left_x=754)

$$
\begin{aligned}
P G & =E F \cdot \cos \angle(E F, B C)=B C \cdot \cos A \cdot \cos (B-C) \\
& =R_{0} \cdot 2 \sin A \cos A \cos (B-C), \\
S T & =(A O+K D) \cdot \sin \angle O A D=A O(1-\cos 2 A) \cdot \sin (B-C) \\
& =R_{0} \cdot(1-\cos 2 A) \sin (B-C) .
\end{aligned}
$$

那么我们由于只需证:

$$
K F \cdot K L+R^{2}=K S^{2}+O T^{2}+\frac{1}{2}\left(P G^{2}+S T^{2}\right)
$$

转而证明

$$
\begin{aligned}
& R \cdot \cos 2 C \cdot R \cdot \cos 2 B \cos 2 A+R^{2} \\
= & (-R \cdot \cos 2 A \cos (B-C))^{2}+(R \cdot \cos A)^{2}+\frac{1}{2}\left((R \cdot 2 \sin A \cos A \cos (B-C))^{2}\right. \\
& \left.+(R \cdot(1-\cos 2 A) \sin (B-C))^{2}\right) .
\end{aligned}
$$

两边约去 $R$ 的平方, 即得引理条件, 证毕.

评注 浙江省郎州二中毛恒毅, 湖南师大附中杨学文, 罗横溢同学也给出了本题的正确解答.

第三题. 在 $2 n \times 2 n$ 的方格表中填入 $\pm 1$, 满足所有数之和为零. 证明可以找到 $n$ 行 $n$ 列, 它们相交的 $n \times n$ 子方格表中所有数之和至少是 $n$.

(哈佛大学 牟晓生 供题)

## 证明 (根据浙江杭州二中刘浩宇同学的解答整理):

先证明 $n$ 为偶数时的情况. 由于表中所有数的和非负, 一定存在一行的和非负. 于是这一行有 $n$ 个 “ 1 ”, 不妨设它们在前 $n$ 列. 令 $A(B)$ 分别为前 (后) $n$ 列构成的子表, 取 $A_{1}$ 为 $A$ 中行和最大的 $n$ 行, 其余的为 $A_{2}$. 如果 $A_{1}$ 中数的
和至少是 $n$, 命题得证. 否则由于 $A_{1}$ 中有一行和为 $n$, 故必有一行和为负数. 由选择, $A_{2}$ 中每一行的和均为负数. 由于 $n$ 为偶数, $A_{2}$ 中每一行的和至多是 -2 .于是 $A$ 的所有数之和小于 $n+n \times(-2)=-n$.

所以 $B$ 中所有数之和大于 $n$. 此时令 $B_{1}$ 为 $B$ 中行和最大的 $n$ 行, 其余的为 $B_{2}$. 如果 $B_{2}$ 中所有数之和非负, 则 $B_{1}$ 中所有数之和大于 $n$, 命题亦成立. 否则 $B_{2}$ 中必有一行的和大于零, 于是 $B_{1}$ 中每一行的和大于零. 这样 $B_{1}$ 中所有数之和也至少是 $n, n$ 为偶数时命题得证!

接下来考虑 $n$ 为奇数. 令 $P$ 为和最大的 $n \times n$ 子表, 不妨设其在前 $n$ 行前 $n$ 列. 我们可以自然地将整张表划分为四个 $n \times n$ 子表 $P, Q, R, S$, 其中 $Q$ 在 $P$的右边而 $R$ 在 $P$ 的下边. 假设 $P$ 的和小于 $n$, 则 $P$ 中必有一列的和至多是零.由 $P$ 的最大性, $Q$ 中每一列的和都至多是零. 然而 $n$ 为奇数, 所以 $Q$ 中每一列的和都至多是 -1 . 故 $Q$ 的和至多是 $-n$, 同样地 $R$ 的和至多是 $-n$. 于是 $P$ 或者 $S$ 的和至少是 $n$, 命题得证!

评注 (1). 雅礼中学陈伊一, 西北师大附中张江昊同学也给出了正确解答.

(2). 我所知道的解答都大同小异, 只能证明存在一个 $n \times n$ 子表的和不小于 $n$. 有兴趣的同学可以研究这个结论是否能够加强. 换而言之, 是否存在满足题目条件的一个方格表, 使得每个 $n \times n$ 子表的和都不大于 $n$ ?

第四题. 给定素数 $p$ 以及正整数 $k$. 求最小的正整数 $d$, 使得存在 $d$ 次整值多项式 $f$, 满足 $p \mid f(n)$ 当且仅当 $p^{k} \mid n$.

(哈佛大学牟晓生 供题)

## 解 (根据东北师大附中徐洋同学的解答整理):

答案是 $2 p^{k-1}-1$.

一方面, 构造 $f(x)=\left(\begin{array}{c}x+2 p^{k-1}-1 \\ 2 p^{k-1}-1\end{array}\right)-1$. 令 $x+2 p^{k-1}-1$ 在 $p$ 进制下的最后 $k$位为 $t_{k-1}, \ldots, t_{1}, t_{0}$, 则由卢卡斯定理,

$$
f(x) \equiv\left(\begin{array}{c}
t_{k-1} \\
1
\end{array}\right) \cdot \prod_{j=0}^{k-2}\left(\begin{array}{c}
t_{j} \\
p-1
\end{array}\right)-1 \quad(\bmod p)
$$

由此易见 $p \mid f(x)$ 当且仅当 $t_{k-1}=1$ 以及 $t_{k-2}=\cdots=t_{0}=p-1$. 也就是 $p \mid f(x)$ 当且仅当 $p^{k} \mid x$.

另一方面, 假设 $f(x)$ 的次数小于 $2 p^{k-1}-1$. 由于 $f(x)$ 是整值多项式, 可将
它写为

$$
f(x)=\sum_{m=0}^{2 p^{k-1}-1} a_{m}\left(\begin{array}{l}
x \\
m
\end{array}\right)
$$

其中 $a_{m}$ 为整数, 而由假设 $a_{2 p^{k-1}-1}=0$. 由于 $p \mid f(0)$, 我们有 $p \mid a_{0}$. 而 $p \nmid f\left(p^{k-1}\right)$, 所以 $p \nmid a_{p^{k-1}}$.

对 $1 \leq u \leq p^{k-1}-1,0 \leq v \leq p-1$, 由卢卡斯定理知

$$
f\left(u+v \cdot p^{k-1}\right) \equiv \sum_{i=1}^{u} a_{i}\left(\begin{array}{c}
u \\
i
\end{array}\right)+v \cdot\left[\sum_{j=0}^{u} a_{p^{k-1}+j}\left(\begin{array}{c}
u \\
j
\end{array}\right)\right]
$$

由条件, 这些都不是 $p$ 的倍数. 固定 $u$, 令 $v$ 变化, 则知

$$
p \left\lvert\, \sum_{j=0}^{u} a_{p^{k-1}+j}\left(\begin{array}{l}
u \\
j
\end{array}\right)\right., \forall 1 \leq u \leq p^{k-1}-1 .
$$

由此以及简单归纳可以证明 $p \mid a_{p^{k-1}+u}+a_{p^{k-1}+u-1}, \forall 1 \leq u \leq p^{k-1}-1$. 结合 $a_{2 p^{k-1}-1}=0$ 可知 $a_{p^{k-1}}, \ldots, a_{2 p^{k-1}-1}$ 都是 $p$ 的倍数. 这样就与之前得到的 $p \nmid a_{p^{k-1}}$ 相矛盾了!

评注 湖南雅礼中学陈伊一同学也给出了本题的正确解答.

