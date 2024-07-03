数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 2022 年联赛加试试题解法拾贝 

肖一君 杜燕

(杭州学军中学教育集团文泮中学, 311200)

本文介绍我们收集到的 2022 全国联赛加试前三题的不同于官方解答的一些妙解. 不当之处, 敬请诸位指正.

题 1 如图, 在凸四边形 $A B C D$ 中, $\angle A B C=\angle A D C=90^{\circ}$, 对角线 $B D$上一点 $P$ 满足 $\angle A P B=2 \angle C P D$, 线段 $A P$ 上两点 $X, Y$ 满足 $\angle A X B=$ $2 \angle A D B, \angle A Y D=2 \angle A B D$. 证明: $B D=2 X Y$.

![](https://cdn.mathpix.com/cropped/2024_02_26_75be897bbd3a23326344g-01.jpg?height=443&width=514&top_left_y=1315&top_left_x=768)

证明 1 (相似证法) 注意 $\angle A B C=\angle A D C=90^{\circ}$, 取 $A C$ 的中点 $O$, 则 $O$ 为凸四边形 $A B C D$ 的外心. 显然 $P, B$ 在 $A C$ 的同侧 (否则 $\angle A P B \leq \angle C P D<$ $2 \angle C P D$, 不合题意) . 根据条件, 可知

$$
\angle A X B=2 \angle A D B=\angle A O B, \angle A Y D=2 \angle A B D=\angle A O D
$$

分别得到 $A, O, X, B$ 四点共圆, $A, Y, O, D$ 四点共圆.

因此

$$
\begin{aligned}
& \angle O X A=\angle O B A=\angle C A B=\angle C D B, \\
& \angle O Y P=\angle O D A=\angle C A D=\angle C B D,
\end{aligned}
$$

所以 $\triangle O X Y \sim \triangle C D B$.

修订日期: 2022-09-14.
方法 1 同参考答案, 做两三角形的高, 证明对应相似比.

方法 2 延长 $C P$ 至任一点 $L$. 取 $A P$ 中点 $Q$, 由 $O$ 为 $A C$ 中点, 故 $O Q$ 为 $\triangle A C P$ 的中位线.

所以 $O Q / / A C$ 且 $O Q=\frac{1}{2} C P$. 又因为

$$
\angle O Q X=\angle L P Q=\frac{1}{2} \angle A P B=\angle C P D
$$

则 $P, Q$ 为 $\triangle C B D, \triangle O Y X$ 的相似对应点. 故

$$
\frac{B D}{X Y}=\frac{C P}{O Q}=2
$$

即 $B D=2 X Y$.
![](https://cdn.mathpix.com/cropped/2024_02_26_75be897bbd3a23326344g-02.jpg?height=554&width=1374&top_left_y=885&top_left_x=364)

方法 3 倍长 $A X$ 至 $Q$, 连结 $C Q$. 则 $O X$ 为 $\triangle A Q C$ 的中位线, 故 $O X / / C Q$.所以

$$
\angle P Q C=\angle A X O=\angle A B O=\angle B A O=\angle B D C .
$$

又因为 $\angle A P B=2 \angle C P D$, 故

$$
\angle Q P C=\angle A P B-\angle C P D=\angle C P D \text {, }
$$

所以 $\triangle P C D \cong \triangle P C Q$.

故

$$
O X=\frac{1}{2} C Q=\frac{1}{2} C D \Rightarrow \frac{X Y}{B D}=\frac{O X}{C D}=\frac{1}{2^{2}},
$$

即 $B D=2 X Y$.

特别地, 也可以倍长 $A Y$ 用类似方式证明.

证明 2 延长 $A P$ 交 $\odot O$ 于点 $S$.

类似上述证法可知 $A, Y, O, D$ 共圆, 通过导角可得 $\triangle D O Y \sim \triangle D C S$, 故 $\frac{O Y}{D O}=\frac{S C}{C D}$, 即 $O Y=\frac{D O}{C D} \cdot S C$.
同理 $O X=\frac{B O}{C B} \cdot S C$. 故

$$
\begin{aligned}
X Y & =O Y \cdot \cos \angle O Y X+O X \cdot \cos \angle O X Y \\
& =O Y \cdot \cos \angle O A D+O X \cdot \cos \angle O A B \\
& =O Y \cdot \frac{A D}{A C}+O X \cdot \frac{A B}{A C} \\
& =\frac{D O}{C D} \cdot S C \cdot \frac{A D}{A C}+\frac{B O}{C B} \cdot S C \cdot \frac{A B}{A C} \\
& =\frac{1}{2} S C \cdot\left(\frac{A D}{C D}+\frac{A B}{C B}\right) \\
& =\frac{1}{2} S C \cdot \frac{A B \cdot C D+A D \cdot B C}{B C \cdot C D} \\
& =\frac{1}{2} S C \cdot \frac{A C \cdot B D}{C D \cdot B C},
\end{aligned}
$$

故只需证明 $C D \cdot B C=A C \cdot S C$.

又因为

$$
\angle D P C=\frac{1}{2} \angle A P B=\frac{1}{2} \angle D P S=\angle S P C \text {, }
$$

由正弦定理得:

$$
\frac{S C}{\sin \angle S P C}=\frac{P C}{\sin \angle P S C}, \frac{C D}{\sin \angle C P D}=\frac{P C}{\sin \angle P D C} .
$$

两式联立可得

$$
\frac{S C}{C D}=\frac{\sin \angle P D C}{\sin \angle P S C}=\frac{B C}{A C},
$$

即 $C D \cdot B C=A C \cdot S C$, 可知命题成立.

![](https://cdn.mathpix.com/cropped/2024_02_26_75be897bbd3a23326344g-03.jpg?height=508&width=554&top_left_y=1679&top_left_x=751)

证明 3 延长 $A P$ 交 $\odot O$ 于点 $H$. 则

$$
\angle B H X=\angle B D A, \angle B X A=2 \angle A D B=2 \angle A H B \Rightarrow B X=X H \text {. }
$$

同理 $D Y=Y H$. 设 $\angle A B D=\alpha, \angle A D B=\beta$. 则对于内接四边形 $B H C D$ 运用三弦定理得

$$
B H \sin \angle D H C+H C \sin \angle B H D=H D \sin \angle B H C,
$$

$$
\begin{aligned}
& \Rightarrow B H \cos \alpha+H C \sin (\alpha+\beta)=H D \cos \beta \\
& \Rightarrow \frac{B H}{\cos \beta}+\frac{H C \sin (\alpha+\beta)}{\cos \alpha \cos \beta}=\frac{H D}{\cos \alpha}
\end{aligned}
$$

由于 $\triangle B X H, \triangle D H Y$ 为等腰三角形, 故

$$
X H=\frac{B H}{2 \cos \angle A H B}=\frac{B H}{2 \cos \beta}, Y H=\frac{H D}{2 \cos \angle A H D}=\frac{H D}{2 \cos \alpha} .
$$

所以

$$
2 X Y=2(Y H-X H)=\frac{H D}{\cos \alpha}-\frac{B H}{\cos \beta}=\frac{H C \sin (\alpha+\beta)}{\cos \alpha \cos \beta} .
$$

又因为

$$
P C=\frac{H C}{\sin \angle H P C}, \frac{C D}{\sin \angle H P C}=\frac{P C}{\sin \angle P D C}=\frac{P C}{\cos \beta},
$$

故 $\frac{H C}{C D}=\cos \beta$, 又由于 $\frac{C D}{\cos \alpha}=\frac{B D}{\sin (\alpha+\beta)}$, 故

$$
2 X Y=\frac{H C \sin (\alpha+\beta)}{\cos \alpha \cos \beta}=\frac{C D \sin (\alpha+\beta)}{\cos \alpha}=B D,
$$

则原命题成立.

![](https://cdn.mathpix.com/cropped/2024_02_26_75be897bbd3a23326344g-04.jpg?height=491&width=531&top_left_y=1262&top_left_x=748)

证明 4 延长 $C P$ 至任一点 $E$.

首先可得 $\triangle X Y O \sim \triangle D B C$, 下证 $\frac{B D}{X Y}=\frac{C D}{X O}=2$.

由 $A, B, X, O$ 共圆, 故

$$
\begin{aligned}
& O X \cdot A B=A X \cdot B O-A O \cdot B X \\
& \Rightarrow O X \cdot \sin \angle A O B=B O \cdot \sin \angle A B X-A O \cdot \sin \angle B A X \\
&=B O \cdot 2 \cdot \cos \angle A B O \sin \angle C A P \\
&=B O \cdot 2 \cdot \sin \angle A C B \sin \angle C A P \\
&=B O \cdot 2 \cdot \sin \angle A C B \cdot \frac{C P \cdot \sin \angle A P C}{A C} \\
&=B O \cdot 2 \cdot \sin \angle A C B \cdot \frac{C P \cdot \sin \angle A P E}{A C}
\end{aligned}
$$

$$
\begin{aligned}
& =B O \cdot 2 \cdot \sin \angle A C B \cdot \frac{C P \cdot \sin \angle C P D}{A C} \\
& =B O \cdot 2 \cdot \sin \angle A C B \cdot \frac{C P \cdot \sin \angle C D P}{A C} \\
& =B O \cdot \frac{\sin \angle A O B}{\cos \angle A C B} \cdot \frac{C D \cdot \sin \angle C A B}{A C} .
\end{aligned}
$$

而 $\cos \angle A C B=\sin \angle C A B, 2 B O=A C$. 故上式等于

$$
\frac{C D}{2} \cdot \sin \angle A O B
$$

即 $\frac{C D}{2}=X Y$, 命题得证.

![](https://cdn.mathpix.com/cropped/2024_02_26_75be897bbd3a23326344g-05.jpg?height=509&width=554&top_left_y=805&top_left_x=745)

题 2 设整数 $n(n>1)$ 恰有 $k$ 个互不相同的素因子, 记 $n$ 的所有正约数之和为 $\sigma(n)$. 证明: $\sigma(n) \mid(2 n-k)$ !.

证明 (1) 当 $k=1$ 时, 设 $n=p_{1}^{\alpha_{1}}$ (其中 $p_{1}$ 是素数, $\alpha_{1} \in \mathbb{N}^{*}$ ), 则

$$
\sigma(n)=1+p_{1}+\cdots+p_{1}^{\alpha_{1}}=\frac{p_{1}^{\alpha_{1}+1}-1}{p_{1}-1}
$$

断言

$$
\frac{p_{1}^{\alpha_{1}+1}-1}{p_{1}-1} \leq 2 p_{1}^{\alpha_{1}}-1
$$

上式等价于

$$
\begin{aligned}
& p_{1}^{\alpha_{1}+1}-1 \leq\left(p_{1}-1\right)\left(2 p_{1}^{\alpha_{1}}-1\right) \\
& \Leftrightarrow p_{1}^{\alpha_{1}+1}-1 \leq 2 p_{1}^{\alpha_{1}+1}-2 p_{1}^{\alpha_{1}}-p_{1}+1 \\
& \Leftrightarrow p_{1}^{\alpha_{1}+1}-2 p_{1}^{\alpha_{1}}-p_{1}+2 \geq 0 \\
& \Leftrightarrow\left(p_{1}-2\right)\left(p_{1}^{\alpha_{1}}-1\right) \geq 0 .
\end{aligned}
$$

由 $p_{1} \geq 2$ 可知上式显然成立.

(2) 当 $k \geq 2$ 时, 设 $n=p_{1}^{\alpha_{1}} p_{2}^{\alpha_{2}} \cdots p_{k}^{\alpha_{k}}$, 其中 $p_{1}, p_{2}, \cdots, p_{k}$ 为互不相同素数, 且 $\alpha_{1}, \alpha_{2}, \cdots, \alpha_{k} \in \mathbb{N}^{*}$. 此时,

$$
\sigma(n)=\frac{p_{1}^{\alpha_{1}+1}-1}{p_{1}-1} \cdot \frac{p_{2}^{\alpha_{2}+1}-1}{p_{2}-1} \cdots \frac{p_{k}^{\alpha_{k}+1}-1}{p_{k}-1} .
$$

不妨设 $p_{1}<p_{2}<\cdots<p_{k}$, 注意到 $p_{k} \geq 2 k-1$ (这是由于 $p_{k} \geq 3$ 时, 只能为奇数), 断言 $p_{1}^{\alpha_{1}+1}-1, p_{2}^{\alpha_{2}+1}-1, \cdots, p_{k-1}^{\alpha_{k-1}+1}-1$, 互不相同, 且

$$
p_{i}^{\alpha_{i}+1}-1<\frac{2 n-k}{2}, i=1,2, \cdots, k-1 .
$$

注意到,

$$
\text { (1) } \Leftrightarrow p_{i}^{\alpha_{i}+1}-1<p_{1}^{\alpha_{1}} \cdots p_{k}^{\alpha_{k}}-\frac{k}{2},
$$

而

$$
p_{1}^{\alpha_{1}} \cdots p_{k}^{\alpha_{k}}-p_{i}^{\alpha_{i}+1} \geq p_{i}^{\alpha_{i}}\left(p_{k}-p_{i}\right) \geq p_{i}\left(p_{k}-p_{i}\right) \geq p_{k}-1>\frac{k}{2}-1
$$

故断言成立! (*) 成立.

再断言,

$$
\frac{p_{k}^{\alpha_{k}+1}-1}{p_{k}-1}<2 n-k
$$

事实上，

$$
\frac{p_{k}^{\alpha_{k}+1}-1}{p_{k}-1}<p_{k} \cdot \frac{p_{k}^{\alpha_{k}}}{p_{k}-1} \leq \frac{3}{2} p_{k}^{\alpha_{k}}\left(p_{k} \geq 3\right) .
$$

而 $2 n-k=2 p_{1}^{\alpha_{1}} \cdots p_{k}^{\alpha_{k}}-k$, 所以

$$
2 n-k-\frac{3}{2} p_{k}^{\alpha_{k}} \geq 4 p_{k}^{\alpha_{k}}-\frac{3}{2} p_{k}^{\alpha_{k}}-k>p_{k}^{\alpha_{k}}-k>0 .
$$

从而断言成立! (**) 成立.

回到原题. (1) 当 $\frac{p_{k}^{\alpha_{k}+1}-1}{p_{k}-1}$ 与 $p_{1}^{\alpha_{1}+1}-1, \cdots, p_{k-1}^{\alpha_{k-1}+1}-1$ 都不同时, 此时 $p_{1}^{\alpha_{1}+1}-1, \cdots, p_{k-1}^{\alpha_{k-1}+1}-1, \frac{p_{k}^{\alpha_{k}+1}-1}{p_{k}-1}$ 为小于 $2 n-k$ 的互不相同的 $k$ 个数, 由 (1)(2)知

$$
\sigma(n)\left|\left(p_{1}^{\alpha_{1}+1}-1\right) \cdots\left(p_{k-1}^{\alpha_{k-1}+1}-1\right) \cdot \frac{p_{k}^{\alpha_{k}+1}-1}{p_{k}-1}\right|(2 n-k) !
$$

(2) 当 $\frac{p_{k}^{\alpha_{k}+1}-1}{p_{k}-1}$ 与某个 $p_{i}^{\alpha_{i}+1}-1$ 相同时 $(1 \leq i \leq k-1)$, 此时由 (1) 知

$$
\frac{p_{k}^{\alpha_{k}+1}-1}{p_{k}-1}=p_{i}^{\alpha_{i}+1}-1<n-\frac{k}{2}
$$

于是存在 $t \in \mathbb{N}^{*}$ 使得

$$
t \frac{p_{k}^{\alpha_{k}+1}-1}{p_{k}-1} \in\left[\frac{2 n-k}{2}, 2 n-k\right),
$$

则 $p_{1}^{\alpha_{1}+1}-1, \cdots, p_{k-1}^{\alpha_{k-1}+1}-1, t \frac{p_{k}^{\alpha_{k}+1}-1}{p_{k}-1}$ 为互不相同的小于 $2 n-k$ 的数.

从而

$$
\sigma(n)\left|\left(p_{1}^{\alpha_{1}+1}-1\right) \cdots\left(p_{k-1}^{\alpha_{k-1}+1}-1\right) \cdot t \frac{p_{k}^{\alpha_{k}+1}-1}{p_{k}-1}\right|(2 n-k) ! .
$$

综上, 命题获证.
题 3 设 $a_{1}, a_{2}, \cdots, a_{100}$ 是非负整数, 同时满足以下条件:

(1) 存在正整数 $k \leq 100$, 使得 $a_{1} \leq a_{2} \leq \cdots \leq a_{k}$, 而当 $i>k$ 时 $a_{i}=0$;

(2) $a_{1}+a_{2}+a_{3}+\cdots+a_{100}=100$;

(3) $a_{1}+2 a_{2}+3 a_{3}+\cdots+100 a_{100}=2022$.

求 $a_{1}+2^{2} a_{2}+3^{2} a_{3}+\cdots+100^{2} a_{100}$ 的最小可能值.

解法 1 我们记 $a_{1} \leq a_{2} \leq \cdots a_{k}$, 且 $i>k$ 时 $a_{i}=0$.

若 $k \leq 20$, 则

$$
2022=\sum_{i=1}^{100} i a_{i} \leq 20 \sum_{i=1}^{100} a_{i}=2000
$$

矛盾. 故 $k \geq 21$.

又因为

$$
\sum_{i=1}^{100}(i-19)\left(i-\frac{62}{3}\right) a_{i} \geq \frac{2}{3} a_{21}-\frac{2}{3} a_{20} \geq 0
$$

故

$$
\begin{aligned}
\sum_{i=1}^{100} i^{2} a_{i} & \geq \frac{119}{3} \sum_{i=1}^{100} i a_{i}-\frac{62}{3} \cdot 19 \sum_{i=1}^{100} a_{i}=\frac{119}{3} \cdot 2022-\frac{62 \cdot 19 \cdot 100}{3} \\
& =80206-39266 \frac{2}{3}=40939 \frac{1}{3}
\end{aligned}
$$

故可得

$$
\sum_{i=1}^{100} i^{2} a_{i} \geq 40940
$$

继而给出构造: 当 $a_{19}=19, a_{20}=40, a_{21}=41, a_{i}=0(i \neq 19,20,21)$ 时,

$$
\sum_{i=1}^{100} i^{2} a_{i}=19^{2} \cdot 19+20^{2} \cdot 40+21^{2} \cdot 41=40940 .
$$

故 $a_{1}+2^{2} a_{2}+\cdots+100^{2} a_{100}$ 的最小值为 40940 .

评注 局部不等式放缩非常巧妙, 叹为观止! 本解答局部不等式的数据, 因为最小值需要集中到尽可能少的 $a_{i}$, 先猜出取等条件 $a_{19}=19, a_{20}=40, a_{21}=$ $41, a_{i}=0(i \neq 19,20,21)$, 然后待定系数 $19 \leq A<20<B \leq 21$, 得到局部不等式

$$
\sum_{i=1}^{100}(i-A)(i-B) a_{i} \geq \sum_{i=19}^{21}(i-A)(i-B) a_{i}
$$

这里 $a_{19}, a_{21}$ 系数非负, 而 $a_{20}$ 系数为负, 因为 $a_{19} \leq a_{20} \leq a_{21}$, 故 $a_{19}$ 在下一步放缩不能起到作用, 于是取 $A=19$, 为使得 $a_{21}$ 与 $a_{20}$ 系数成相反数, 必须取 $B=\frac{62}{3}$.
事实上, 本解法还得到了 $a_{i}$ 是实数情况的最小值 $40939 \frac{1}{3}$, 当 $a_{19}+a_{20}+a_{21}=$ $100,19 a_{19}+20 a_{20}+21 a_{21}=2022, a_{20}=a_{21}$, 即算得 $a_{19}=\frac{56}{3}, a_{20}=a_{21}=\frac{122}{3}$时取到.

解法 2 记 $S=\sum_{i=1}^{100} i^{2} a_{i}$, 令 $k=21, a_{1}=a_{2}=\cdots=a_{18}=0, a_{19}=19, a_{20}=$ $40, a_{21}=41, a_{22}=\cdots=a_{100}=0$. 则 $S$ 值为 40940. 下证 $S \geq 40940$.

设 $a_{1}=b_{1}, a_{2}-a_{1}=b_{2}, \cdots, a_{k}-a_{k-1}=b_{k}$, 则 $b_{1}, b_{2}, \cdots, b_{k} \in \mathbb{N}$. 则条件等价于

$$
\left\{\begin{array}{l}
k b_{1}+(k-1) b_{2}+\cdots+b_{k}=100 \\
\sum_{i=1}^{k} \frac{(k+i)(k-i+1)}{2} b_{i}=2022
\end{array}\right.
$$

设 $c_{i}=(k+1-i) b_{i}, 1 \leq i \leq k$, 则条件等价于

$$
\left\{\begin{array} { l } 
{ c _ { 1 } + c _ { 2 } + \cdots + c _ { k } = 1 0 0 , } \\
{ \sum _ { i = 1 } ^ { k } ( k + i ) c _ { i } = 4 0 4 4 }
\end{array} \Rightarrow \left\{\begin{array}{l}
c_{1}+c_{2}+\cdots+c_{k}=100, \\
\sum_{i=1}^{k} i c_{i}=4044-100 k
\end{array}\right.\right.
$$

则

$$
\begin{aligned}
S=\sum_{i=1}^{k}\left(i^{2}+\cdots+k^{2}\right) b_{i} & =\frac{1}{6} \sum_{i=1}^{k}(k(k+1)(2 k+1)-(i-1) i(2 i-1)) b_{i} \\
& =\frac{1}{6} \sum_{i=1}^{k}(k-i+1)\left(2 i^{2}+(2 k-i) i+2 k^{2}+k\right) b_{i} \\
& =\frac{1}{6} \sum_{i=1}^{k}\left(2 i^{2}+(2 k-1) i+2 k^{2}+k\right) c_{i} \\
& =\frac{1}{6}\left(\left(2 k^{2}+k\right) \cdot 100+(2 k-1)(4044-100 k)+2 \sum_{i=1}^{k} i^{2} c_{i}\right) \\
& =\frac{1}{3}\left(4144 k-2022+\sum_{i=1}^{k} i^{2} c_{i}\right) .
\end{aligned}
$$

由 Cauthy 不等式可得

$$
\sum_{i=1}^{k} i^{2} c_{i} \cdot \sum_{i=1}^{k} c_{i} \geq\left(\sum_{i=1}^{k} i c_{i}\right)^{2}
$$

故

$$
\sum_{i=1}^{k} i^{2} c_{i} \geq \frac{(4044-100 k)^{2}}{100} \Rightarrow S \geq \frac{1}{3}\left(4144 k-2022+\frac{(4044-100 k)^{2}}{100}\right)
$$

即

$$
S \geq \frac{1}{3}\left(100 k^{2}-3944 k+\frac{4044^{2}}{100}-2022\right)
$$

另一方面, 由于

$$
100 k=k\left(c_{1}+c_{2}+\cdots+c_{k}\right) \geq \sum_{i=1}^{k} i c_{i}=4044-100 k \Rightarrow k \geq 21 .
$$

若 $k \geq 22$, 则

命题成立.

$$
\begin{aligned}
S & \geq \frac{1}{3}\left(100 \cdot 22^{2}-3944 \cdot 22+\frac{4044^{2}}{100}-2022\right) \\
& =\frac{1}{3}(123149.36)>40940
\end{aligned}
$$

若 $k=21$, 则条件等价于

$$
\left\{\begin{array}{l}
c_{1}+c_{2}+\cdots+c_{21}=100 \\
\sum_{i=1}^{21} i c_{i}=1944
\end{array}\right.
$$

由 (1) 可知 $S=\frac{1}{3}\left(85002+\sum_{i=1}^{k} i^{2} c_{i}\right)$, 故

$$
S \geq 40940 \Leftrightarrow S>40939 \Leftrightarrow \sum_{i=1}^{k} i^{2} c_{i}>37815
$$

又因为

$$
\begin{aligned}
\sum_{1 \leq i<j \leq 21}(i-j)^{2} c_{i} c_{j} & =\sum_{i=1}^{21} i^{2} c_{i} \cdot \sum_{i=1}^{21} c_{i}-\left(\sum_{i=1}^{21} i c_{i}\right)^{2} \\
& =100 \sum_{i=1}^{21} i^{2} c_{i}-1944^{2}
\end{aligned}
$$

故仅需证明: 当满足条件 $(*)$ 以及 $c_{i} \in N(1 \leq i \leq 21)$, 有

$$
\sum_{1 \leq i<j \leq 21}(i-j)^{2} c_{i} c_{j}>2364
$$

若 $c_{1}, \cdots, c_{21}$ 中有至少 3 个不为 0 , 则可取 $i<j, c_{i}, c_{j} \geq 1,2 \mid i+j$. 注意 $c_{i}$ 已经没有单调性约束, 故可用 $\left(c_{i}-1, c_{\frac{i+j}{2}}+2, c_{j}-1\right)$ 代替 $\left(c_{i}, c_{\frac{i+h}{2}}, c_{j}\right)$,则 $\sum_{i=1}^{21} i^{2} c_{i}$ 值减小. 故可设 $c_{1}, c_{2}, \cdot, c_{21}$ 中至多 2 个不为 0 .

将其记为 $c_{i}, c_{j}(i<j)$, 则

$$
\left\{\begin{array}{l}
c_{i}+c_{j}=100 \\
i c_{i}+j c_{j}=1944
\end{array}\right.
$$

若 $j \leq 19$, 则 $i c_{i}+j c_{j} \leq 19\left(c_{i}+c_{j}\right)=1900$, 矛盾;

若 $i \leq 20$, 则 $i c_{i}+j c_{j} \geq 20\left(c_{i}+c_{j}\right)=2000$, 矛盾.

故 $i \leq 19<j \Rightarrow c_{i}=\frac{100 j-1944}{j-i}, c_{j}=\frac{1944-100 i}{j-i}$, 则

$$
\text { (2) LHS }=(i-j)^{2} c_{i} c_{j}=(100 j-1944)(1944-100 i) \geq 56 \cdot 44=2464 \text {, }
$$

可知 (2) 成立.
综上, 所求 $S$ 的最小值为 40940 .

评注 通过对 $a_{i}$ 做差分得到 $b_{i}$, 再换元成 $c_{i}$, 还是两个条件, 一个目标函数,但是可避免单调性的问题, 此方法对计算能力要求很高!

解法 3 取 $1 \leq t \leq 100$.

对 $i>t,(i-(t+1))^{2} \geq 0$. 即 $i^{2} \geq 2 i(t+1)-(t+1)^{2}$. 故

$$
\begin{aligned}
& (t+1)^{2} a_{t+1}+\cdots+100^{2} a_{100} \\
& \geq 2(t+1)\left((t+1) a_{t+1}+\cdots+100 a_{100}-(t+1)^{2}\left(a_{t+1}+\cdots+a_{100}\right)\right. \\
& =2(t+1)\left(2022-a_{1}-2 a_{2}-\cdots-t a_{t}\right)-(t+1)^{2}\left(100-a_{1}-a_{2}-\cdots-a_{t}\right)
\end{aligned}
$$

于是

$$
\begin{aligned}
& a_{1}+2^{2} a_{2}+\cdots+100^{2} a_{100} \\
& \geq a_{t}+2^{2} a_{t-1}+\cdots+t^{2} a_{1}+4044(t+1)-100(t+1)^{2}
\end{aligned}
$$

同理, 对 $i<t,(i-(t-1))^{2} \geq 0$. 类似可得

$$
\begin{aligned}
& a_{1}+2^{2} a_{2}+\cdots+100^{2} a_{100} \\
& \geq a_{t}+2^{2} a_{t+1}+\cdots+(100-t+1)^{2} a_{100}+4044(t-1)-100(t-1)^{2}
\end{aligned}
$$

两式联立可得

$$
\begin{aligned}
a_{1}+2^{2} a_{2}+\cdots+100^{2} a_{100} & \geq 4044 t-100 t^{2}-100+\frac{1}{2}\left(a_{t}+2^{2} a_{t-1}+\cdots+t^{2} a_{1}\right) \\
& +\frac{1}{2}\left(a_{t}+2^{2} a_{t+1}+\cdots+(100-t+1)^{2} a_{100}\right) \\
& \geq 4044 t-100 t^{2}-100+\frac{1}{2}\left(4\left(100-a_{t}\right)+2 a_{t}\right)
\end{aligned}
$$

令 $t=20$ 可得

$$
a_{1}+2^{2} a_{2}+\cdots+100^{2} a_{100} \geq 40980-a_{20}
$$

故当 $a_{20} \leq 40$ 时,

$$
a_{1}+2^{2} a_{2}+\cdots+100^{2} a_{100} \geq 40940 .
$$

另一方面, 当 $a_{20}>40$ 时, 参考标准解答;

当 $a_{20} \geq 41$ 时, 由 $k \geq 21$ 及条件可知 $a_{21} \geq 41$, 故

$$
\begin{aligned}
\sum_{i=1}^{100} i^{2} a_{i} & =\sum_{i=1}^{100}(i-19)(i-20) a_{i}+39 \sum_{i=1}^{100} i a_{i}-380 \sum_{i=1}^{100} a_{i} \\
& =\sum_{i=1}^{100}(i-19)(i-20) a_{i}+40858 \\
& \geq(21-19)(21-20) a_{21}+40858 \geq 40940 .
\end{aligned}
$$

综上, 所求最小值为 40940 .

评注 对 $a_{20} \leq 40$ 利用待定 $t$ 的局部不等式可证得, 另一种情况与标答相同.

解法 4 设 $S_{i}=a_{1}+a_{2}+\cdots+a_{i}(i=1,2, \cdots, 100)$, 则由 $\left\{a_{n}\right\}$ 为非负整数列, 可知 $S_{i}$ 不减. 且由条件可知 $a_{1} \leq a_{2} \cdots \leq a_{k}$, 故

$$
S_{i}-S_{i-1} \leq S_{i+1}-S_{i}(i=1,2, \cdots, k-1)
$$

同时, $S_{100}=a_{1}+a_{2}+\cdots+a_{100}=100$, 且

$$
\begin{aligned}
a_{1}+2 a_{2}+\cdots+100 a_{100} & =S_{1}+2\left(S_{2}-S_{1}\right)+\cdots+100\left(S_{100}-S_{99}\right) \\
& =100 S_{100}-S_{1}-S_{2}-\cdots-S_{99} \\
& =2022
\end{aligned}
$$

故

$$
\sum_{i=1}^{99} S_{i}=100 S_{100}-2022=7978
$$

记 $T=\sum_{i=1}^{100} i^{2} a_{i}$, 则

$$
\begin{aligned}
T & =S_{1}+2^{2}\left(S_{2}-S_{1}\right)+\cdots+100^{2}\left(S_{100}-S_{99}\right) \\
& =100^{2} S_{100}-\sum_{i=1}^{99}(2 i+1) S_{i} \\
& =100^{3}-100^{2}+2022-\sum_{i=1}^{99} 2 i S_{i} .
\end{aligned}
$$

从而只需求 $S_{i}$ 的加权求和 $M=\sum_{i=1}^{99} i S_{i}$ 的最大值. 首先

$$
M \leq M_{0}=\sum_{i=21}^{99} i \cdot 100+20 \cdot 78=475560 .
$$

事实上, $S_{i}$ 的系数随 $i$ 递增, 故应使得 $S_{i}$ 求和值不变意义时, 下标较大的 $S_{i}$ 项值尽可能大.

先证明: $S_{20}<100$. 否则, 设 $a_{20}=100$, 则可知 $S_{i}=100(i \geq 21)$, 从而

$$
\sum_{i=1}^{99} S_{i} \geq \sum_{i=20}^{99} S_{i}=100 \cdot 80>7978
$$

矛盾, 从而 $S_{20}<100$.

不妨令

$$
S_{21}=S_{22}=\cdots=S_{100}=100
$$

此时 $S_{20} \leq 59$. 否则若 $S_{20} \geq 60$, 则由 (1) 可得

$$
S_{19} \geq 2 S_{20}-S_{21} \geq 60 \times 2-100=20
$$

此时

$$
\sum_{i=1}^{99} S_{i} \geq \sum_{i=20}^{99} S_{i}=100 \cdot 79+60+20>7978
$$

矛盾. 且由 $\sum_{i=1}^{99} S_{i}=7978$ 可知 $\sum_{i=1}^{19} S_{i}=19$, 从而 $S_{19} \leq 19$, 且

$$
\begin{aligned}
M=\sum_{i=1}^{99} i S_{i} & \leq 19 \times 19+59 \times 20+\sum_{i=21}^{99} i \cdot 100 \\
& =361+1180+474000=475541
\end{aligned}
$$

取 $S_{i}=0(i \leq 18) ; S_{19}=19, S_{20}=59 ; S_{j}=100(j \geq 21)$ 可取等.

我们再来解释 $(2)$ : 若 $S_{21}$ 不为 100 ,

当 $\sum_{i=1}^{19} S_{i} \geq 19$, 则 $M_{0}-M \geq 19$; (相当于将 $S_{1}, S_{2}, \cdots, S_{19}$ 都挪到 $S_{20}, \cdots, S_{99}$, 权重至少相差 1 )

当 $\sum_{i=1}^{19} S_{i} \geq 18$, 于是 $S_{20} \leq \frac{S_{19}+S_{21}}{2} \leq \frac{18+100}{2}=59$, 则

$$
\sum_{i=1}^{19} S_{i} \geq 7978-100 \cdot 79-S_{20} \geq 19
$$

矛盾!

总有 $M \leq 475541$. 故

$$
\begin{aligned}
T & \geq 100^{3}-100^{2}+2022-2 M_{\max } \\
& =100^{3}-100^{2}+2022-951082 \\
& =40940 .
\end{aligned}
$$

取等即 $a_{1}=a_{2}=\cdots=a_{18}=0, a_{19}=19, a_{20}=40, a_{21}=41, a_{22}=\cdots=$ $a_{100}=0$.

综上, 所求式的最小值为 40940 .

评注 考虑前 $n$ 项和 $S_{n}$, 则条件有两个等式转化成一个等式 $\sum_{i=1}^{99} S_{i}=7978$,目标函数为 $\sum_{i=1}^{99} i S_{i}$, 这就能直接反映出本题的方向, 应尽可能下标大的 $S_{i}$ 都是 100 , 当然直接调整还是会破坏单调性, 不好直接处理, 跳过中间过程直接考虑最优情况, 很容易说明最优情况必须有 $S_{21}=S_{22}=\cdots=S_{100}=100$, 本题就迎刃而解了.
解法 5 (阿贝尔变换) 利用解法 4 的叙述, 设 $S_{i}=a_{1}+a_{2}+\cdots+a_{i}(i=$ $1,2, \cdots, 100)$, 则非负数列 $S_{i}$ 不减, $S_{k}=S_{k+1}=\cdots=S_{100}=100$, 满足下凸性质 $S_{i} \leq \frac{S_{i+1}+S_{i-1}}{2}(i=2, \cdots, k-1)$,

$$
\sum_{i=1}^{99} S_{i}=100 S_{100}-2022=7978
$$

然后要证明

$$
M=\sum_{i=1}^{99} i S_{i} \leq 475541
$$

注意

$$
M=\sum_{i=1}^{99}\left(S_{i}+S_{i+1}+\cdots+S_{99}\right)
$$

对 $21 \leq i \leq 99$,

$$
S_{i}+S_{i+1}+\cdots+S_{99} \leq 100(100-i),
$$

对 $1 \leq i \leq 19$,

$$
S_{i}+S_{i+1}+\cdots+S_{99} \leq \sum_{i=1}^{99} S_{i}=7978 .
$$

当 $S_{19} \geq 19$, 则

$$
S_{20}+S_{21}+\cdots+S_{99} \leq \sum_{i=1}^{99} S_{i}-S_{19} \leq 7959
$$

当 $S_{19} \leq 18$, 利用数列凸性,

$$
S_{20} \leq \frac{S_{19}+S_{21}}{2} \leq \frac{18+100}{2}=59
$$

故仍有

$$
S_{20}+S_{21}+\cdots+S_{99} \leq 59+100 \times 79=7959
$$

将上述不等式代入 (1) 可得 $M \leq 475541$.

评注 本解法关键是做两次阿贝尔变换, 再利用条件的界和凸性进行放缩,非常精彩! 本文第一作者在浙江省联赛阅卷过程中, 与沈虎跃, 赵斌, 郡达, 陈军杰, 胡克元, 高程宇等教练讨论学习得到这个方法, 有些学生也在试卷上完成了类似的解答!

