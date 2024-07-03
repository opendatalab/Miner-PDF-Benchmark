# 第十四期问题征解解答与点评 

牟晓生

第一题. 如图, 在锐角三角形 $A B C$ 中, $\angle B A C=$ $60^{\circ}$, 且 $A B>A C$. 过 $A$ 作 $B C$ 的垂线，垂足为 $K$. $U$ 是 $\triangle A B C$ 的九点圆心, $A U$ 的延长线交 $B C$ 于 $D$, $\triangle U D K$ 的外接圆与 $\triangle A B C$ 的九点圆交于 $K$ 以外的另一点 $J, A J$ 与 $\triangle U D K$ 的外接圆交于另一点 $T$.证明: $B C^{2}=4 J T \cdot J A$.



(广西钦州 卢圣, 陕西西安铁一中 杨运新 供题)

## 证法一 (根据浙江省象山县第三中学黄子宸同学的解答整理):

设 $O, H$ 分别是 $\triangle A B C$ 的外心与垂心, $A D$ 交 $\odot O$ 于 $M, N, V$ 分别是 $B C, D H$ 中点.

由欧拉线定理知: $U O=U H$. 而 $A H=2 R \cdot \cos A=R=O A$, 所以 $A U$ 平分 $\angle O A H$, 且垂直平分 $O H$. 因此 $A H=A O=O M=M H$, 即四边形 $A O M H$为菱形, 故 $O M / / A H$. 而 $A H \perp B C$, 所以 $O M \perp B C$. 结合 $O N \perp B C$, 即得 $O, N, M$ 共线.

由 $\angle H U D=90^{\circ}=\angle H K D$, 知 $H, U, D, K$ 共圆, 显然 $V$ 是圆心, 且 $J K$ 是 $\odot U, \odot V$ 的公共弦, 所以 $U V \perp J K$, 从而 $O D \perp J K$. 结合 $O N \perp D K$, 即得 $\angle D O N=\angle D K J$. 所以

$$
\angle D H J=\angle D K J=\angle D O N=\angle D O M=\angle D H M \text {, }
$$

故 $H, J, M$ 共线.

注意到 $H$ 是 $\odot U, \odot O$ 的位似中心, 位似比为 $1: 2$, 故 $J$ 是 $H M$ 中点.因为 $\angle A O U=\angle U H J=\angle U T J$, 所以 $A, O, U, T$ 共圆, 设圆心为 $Q$. 由于 $\angle A U O=90^{\circ}$, 所以 $Q$ 是 $O A$ 中点. 因此

$$
J T \cdot J A=J \text { 到 } \odot O \text { 的幂 }
$$

$$
\begin{aligned}
& =J Q^{2}-Q U^{2}=M O^{2}-N O^{2} \\
& =-(N \text { 到 } \odot O \text { 的幂 }) \\
& =N B \cdot N C=\left(\frac{1}{2} B C\right)^{2}=\frac{1}{4} B C^{2} .
\end{aligned}
$$

即 $B C^{2}=4 J T \cdot J A$.



## 证法二 (根据北师大二附中李泽宇同学的解答整理):

先证明 $A B \cdot A C=2 A U \cdot A D$.

以 $\triangle A B C$ 九点圆 $\odot U$ 为单位圆建立复平面. 设三边中点坐标如图所示, 其中 $|a|=1, \omega$ 是三次单位虚根, 即 $w=e^{\frac{2 \pi i}{3}}=\cos \frac{2 \pi}{3}+i \sin \frac{2 \pi}{3}$.

易知 $A=1+\omega-a=-\omega^{2}-a$. 设 $D=\lambda A=\lambda\left(-\omega^{2}-a\right)$, 其中实数 $\lambda<0$.由 $D M / /(1-\omega)$ 得

$$
\frac{\lambda(1+\omega-a)-a}{1-\omega}=\frac{\lambda\left(1+\omega^{2}-\bar{a}\right)-\bar{a}}{1-\omega^{2}}
$$

从而

$$
\lambda\left[1+2 \omega+\omega^{2}-a(1+\omega)\right]-a(1+\omega)=\lambda\left(1+\omega^{2}-\bar{a}\right)-\bar{a}
$$

解得

$$
\lambda=\frac{a(1+\omega)-\bar{a}}{2 \omega-a(1+\omega)+\bar{a}}=\frac{-a^{2} \omega^{2}-1}{(a \omega+1)^{2}}
$$

又利用

$$
|1+\omega-a|=\left|-\omega^{2}-a\right||\omega|=|a \omega+1|
$$

$$
|1-a||\omega-a|=\left|a^{2}-a(1+\omega)+\omega\right|=\left|a^{2}+a \omega^{2}+\omega\right|\left|\omega^{2}\right|=\left|a^{2} \omega^{2}+a \omega+1\right| \text {, }
$$

可证明

$$
4|1-a||\omega-a|=2\left|\frac{2 a^{2} \omega^{2}+2 a \omega+2}{(a \omega+1)^{2}}\right| \cdot|1+\omega-a|^{2}=2(1-\lambda)|A U|^{2} .
$$

这就证明了 (1) 式.

有 $\angle J D K=\angle J U K=2 \angle J M K$, 可知 $D M=D J$. 又 $U M=U J$, 故 $A D$为 $M J$ 中垂线. 由中线长公式, 得

$$
2\left(A B^{2}+A C^{2}\right)-B C^{2}=4 A M^{2}=4 J A^{2} .
$$

又由余弦定理及 $(1)$, 得

$$
B C^{2}=A B^{2}+A C^{2}-2 A B \cdot A C \cos 60^{\circ}=A B^{2}+A C^{2}-2 A U \cdot A D .
$$

从而

$$
B C^{2}=4\left(J A^{2}-A U \cdot A D\right)=4\left(J A^{2}-A T \cdot A J\right)=4 J T \cdot J A
$$

结论得证.



评注 巴蜀中学叶安宁同学, 东北育才中学何雨桐同学, 长沙市长郡中学曾科荣同学, 北京市第五中学高天伟同学, 长沙市一中张天佑, 何沛予同学, 温州育英国际实验学校高敬翔同学, 浙江省鐎州二中何旭峥同学以及雅礼中学团队也给出了本题的正确解答.
第二题. 定义函数 $f(x)$ : 当 $0 \leq x \leq 1$ 时 $f(x)=1$, 否则 $f(x)=0$. 设 $x_{1}, x_{2}, \ldots x_{n} ; a_{1}, a_{2}, \ldots a_{n}$ 为任意正实数, 证明:

$$
\sum_{i, j=1}^{n} a_{i} a_{j} f\left(\frac{\left|x_{i}-x_{j}\right|}{2}\right) \leq 3 \sum_{i, j=1}^{n} a_{i} a_{j} f\left(\left|x_{i}-x_{j}\right|\right) .
$$

(浙江杭州二中 赵斌 供题)

## 证明 (根据供题者的解答整理):

我们首先证明不等式对 $a_{1}=a_{2}=\cdots=a_{n}=1$ 成立. 此时令

$$
\begin{aligned}
& T_{1}=\left\{\left(x_{i}, x_{j}\right): 1 \leq i, j \leq n,\left|x_{i}-x_{j}\right| \leq 1\right\} \\
& T_{2}=\left\{\left(x_{i}, x_{j}\right): 1 \leq i, j \leq n,\left|x_{i}-x_{j}\right| \leq 2\right\} .
\end{aligned}
$$

我们需要证明: $\left|T_{2}\right|<3\left|T_{1}\right|$.

为此对 $n$ 归纳, $n=1,2$ 时显然成立. 对 $n \geq 3$, 不妨设 $x_{1} \leq x_{2} \leq \cdots \leq x_{n}$.对 $1 \leq k \leq n$, 令 $N_{k}$ 为区间 $\left[x_{k}-1, x_{k}+1\right]$ 中包含 $x_{j}$ 的个数 (至少一个). 设 $N_{k}$ 的最大值为 $s+1$, 并取最大的 $k$ 使得 $N_{k}=s+1$. 对这个 $k$, 我们证明区间 $\left[x_{k}-2, x_{k}+2\right]$ 中包含 $x_{j}$ 的个数至多是 $3 s+2$. 实际上, 如果区间 $\left[x_{k}-2, x_{k}-1\right)$包含某个 $x_{i}$, 则 $\left[x_{k}-2, x_{k}-1\right) \subset\left[x_{i}-1, x_{i}+1\right]$. 由 $N_{i} \leq s+1$ 我们知道 $\left[x_{k}-2, x_{k}-1\right)$ 中至多包含 $s+1$ 个 $x_{j}$. 类似地可以证明 $\left(x_{k}+1, x_{k}+2\right]$ 中至多包含 $s$ 个 $x_{j}$ (这里少了一个是因为 $k$ 的最大性). 最后 $\left[x_{k}-1, x_{k}+1\right]$ 中有 $s+1$ 个 $x_{j}$, 因此综合三个子区间得到 $\left[x_{k}-2, x_{k}+2\right]$ 中至多有 $(s+1)+s+(s+1)=3 s+2$个 $x_{j}$.

由 $N_{k}$ 的定义, $x_{k}$ 对于 $T_{1}$ 的贡献恰好是 $2(s+1)-1=2 s+1$ 次, 其中减一是因为 $i=j=k$ 被重复计算了. 同样地, 由上一段最后的结论知 $x_{k}$ 对于 $T_{2}$ 的贡献至多是 $2(3 s+2)-1=6 s+3=3(2 s+1)$ 次. 于是可以将 $x_{k}$ 去掉用归纳假设, 得到 $\left|T_{2}\right|<3\left|T_{1}\right|$.

接下来我们证明结论对正整数 $a_{1}, \ldots, a_{n}$ 成立. 为此考虑一个新的实数列 $y_{1}, y_{2}, \ldots, y_{m}$, 其中每个 $x_{i}$ 都被重复了 $a_{i}$ 次. 不难验证

$$
\begin{aligned}
\sum_{i, j=1}^{n} a_{i} a_{j} f\left(\frac{\left|x_{i}-x_{j}\right|}{2}\right) & =\sum_{i, j=1}^{m} f\left(\frac{\left|y_{i}-y_{j}\right|}{2}\right) ; \\
\sum_{i, j=1}^{n} a_{i} a_{j} f\left(\left|x_{i}-x_{j}\right|\right) & =\sum_{i, j=1}^{m} f\left(\left|y_{i}-y_{j}\right|\right) .
\end{aligned}
$$

因此原不等式对于 $\left(x_{1}, \ldots, x_{n}\right),\left(a_{1}, \ldots, a_{n}\right)$ 的结论等价于对于 $\left(y_{1}, \ldots, y_{m}\right)$, $(1,1, \ldots, 1)$ 的结论. 命题仍然成立. 再注意到命题关于 $a_{1} \sim a_{n}$ 是齐次的, 因此
结论对一切正有理数 $a_{1}, \ldots, a_{n}$ 成立. 由连续性, 结论对正实数也成立.

评注 (1). 假设 $a_{1}+a_{2}+\cdots+a_{n}=1$, 那么这个问题转化为一个有趣的概率论结果: 对任意独立等分布的随机变量 $X, Y$,

$$
\operatorname{Pr}(|X-Y| \leq 2) \leq 3 \cdot \operatorname{Pr}(|X-Y| \leq 1)
$$

这是 N. Alon 与 R. Yuster 的 “ 123 ” 定理. 更一般的结论是对任意实数 $b>a>0$, 有

$$
\operatorname{Pr}(|X-Y| \leq b) \leq\left(2\left\lceil\frac{b}{a}\right\rceil-1\right) \cdot \operatorname{Pr}(|X-Y| \leq a)
$$

不难验证这里的常数 3 (或一般的 $2\left\lceil\frac{b}{a}\right\rceil-1$ ) 是最优的.

(2). 从上面的证明可以看出, 在 $a_{1}=a_{2}=\cdots=a_{n}$ 时的结论实际上与一般的结论等价. 其中的转化在本质上是把一个任意的随机变量看成等分布的.这种以相对较弱结论为跳板的证明技巧在竞赛中也有出现, 比如 2006 年 IMO 的第六题就是很好的例子.

第三题. 考虑一个 $n^{2}+1$ 阶 $n$-正则简单图 $G$, 满足其中任意两个顶点的距离至多是 2. 证明:

1) 当 $n \leq 3$ 时存在这样的图;
2) $n=4$ 时不存在这样的图;
3) $n=5$ 时也不存在这样的图.

(湖北武钢三中学生 王逸轩 供题)

## 证明 (根据雅礼中学李师铨同学的解答整理):

1) $n=1$ 时 $K_{2}$ 满足条件, $n=2$ 时 $C_{5}$ (长度为 5 的圈) 满足条件, $n=3$ 时彼得森图满足条件.
2) 假设这样的图存在, 那么对任意不相邻的顶点 $v, w$, 存在某个顶点 $u$ 与它们都相邻. 一方面, 由 $n$-正则性可知不相邻的有序点对 $(v, w)$ 共有 $\left(n^{2}+\right.$ 1) $\left(n^{2}-n\right)$ 对. 另一方面, 每个顶点 $u$ 恰与 $n(n-1)=n^{2}-n$ 对 $(v, w)$ 相邻. 由于总数恰好相等, 我们得出任意不相邻点对 $(v, w)$ 恰与一个 $u$ 相邻, 而任意相邻点对 $(v, w)$ 不与任何 $u$ 相邻. 也就是说 $G$ 中没有三角形或四边形.

现在设 $n=4, G$ 有 17 个顶点. 我们来计算 $G$ 中 $C_{5}$ 的个数. 固定一个顶点 $u$, 设它与 $v_{1}, v_{2}, v_{3}, v_{4}$ 相邻. 由于图中无三角形, $v_{1}, v_{2}, v_{3}, v_{4}$ 互不相邻. 因此它们各与外面的三个顶点相邻, 并且互不重叠 (否则图中有四边形). 现在
考虑过 $u$ 的长度为 5 的圈, 它一定具有 $u v_{i} w z v_{j}$ 的形式. 假设我们已经选好了 $v_{i}, v_{j}$. 如果 $w \neq u$ 与 $v_{i}$ 相邻, 那么 $w$ 不与 $v_{j}$ 相邻. 因此存在唯一的 $z$ 使得 $z$ 与 $w, v_{j}$ 都相邻, 并且 $z \neq u$ (否则 $u v_{i} w$ 是三角形). 由于 $(i, j)$ 有 6 种选择,而 $w \in N\left(v_{i}\right) \backslash\{u\}$ 有 3 种选择, 共有 18 个过 $u$ 的 $C_{5}$. 这样导致总共的五圈个数等于 $\frac{18 \times 17}{5}$, 不是整数! 因此这样的图不存在.

3) 设 $n=5, G$ 有 26 个顶点. 此时过一个顶点的 $C_{5}$ 个数是 $\left(\begin{array}{l}5 \\ 2\end{array}\right) \times 4=40$ 个,是 5 的倍数, 无法导出矛盾. 为证命题, 我们考虑 $C_{7}$ 的个数. 固定一个顶点 $u$,设它与 $v_{1}, v_{2}, v_{3}, v_{4}, v_{5}$ 相邻, 而每个 $v_{i}$ 又与剩下 20 个顶点 $w_{1}, w_{2}, \ldots, w_{20}$ 中的某四个相邻. 一个过 $u$ 的七圈一定是 $u v_{i} w_{p} w_{q} w_{r} w_{s} v_{j}$. 类似于前一问的分析, 我们假设 $v_{i}, v_{j}$ 已经选定. 然后选取 $w_{q}, w_{r}$ 与 $v_{i}, v_{j}$ 都不相邻(否则由这个七圈可以得到三角形或四边形), 且它们相邻. 这时 $w_{p}$ 由 $v_{i}$ 与 $w_{q}$ 唯一确定, 而 $w_{s}$ 由 $w_{r}$与 $v_{j}$ 唯一确定, 并且 $w_{p}, w_{q}, w_{r}, w_{s}$ 互不相同.

注意到 $v_{i}, v_{j}$ 有 $\left(\begin{array}{l}5 \\ 2\end{array}\right)=10$ 种选择, 而在 $(i, j)$ 确定后 $w_{q}, w_{r}$ 有 $12 \times 2=24$ 种选择. 后者是因为假设 $i=4, j=5$, 那么 $w_{q}$ 不与 $v_{4}, v_{5}$ 相邻共有 12 种选择; 而假设 $w_{q}$ 与 $v_{3}$ 相邻, 则 $w_{r}$ 与 $w_{q}$ 相邻且与 $v_{1}$ 或 $v_{2}$ 相邻, 恰有 2 种选择. 因此过 $u$的七圈共有 $10 \times 24=240$ 个. 这样导致总共的七圈个数为 $\frac{240 \times 26}{7}$, 不是整数! 因此当 $n=5$ 时这样的图也不存在.

评注 (1). 巴蜀中学叶安宁同学, 雅礼中学刘哲成, 尹龙晖同学也给出了本题正确的解答. 雅礼中学刘凯睿, 王文瑞, 胡东健, 谢添乐, 邱添, 陈钦品, 黄磊,刘麟轩等同学给出了前两问的正确解答. 他们在得出图中没有三角形及四边形后进行有效的讨论, 从而导出 $n \neq 4,5$. 当然, 这样的方法无法推广, 而上面李师铨同学的解答能一般地证明 $n \equiv 0,1,2,3(\bmod 5,7)$. 我记得曾在单墫老师的《研究教程》上读到 $n=4$ 的证明, 就是基于五圈的个数. 李同学能触类旁通地考虑七圈, 非常值得赞赏!

(2). 实际上可以证明 $n$ 只有可能是 $1,2,3,7,57$. 为此考虑 $G$ 的关联矩阵 $A$, 并记 $A$ 的行向量分别为 $\alpha_{1}, \ldots, \alpha_{n^{2}+1} \in \mathbb{R}^{n}$. 那么对于任意 $i \neq j$, 我们有 $\alpha_{i} \cdot \alpha_{j}=1-A_{i j}$. 这个关系简洁地表达了当 $v_{i}, v_{j}$ 相邻时它们没有共同的邻居, 而当它们不相邻时它们恰有一个共同的邻居. 另外 $\alpha_{i} \cdot \alpha_{i}=n$, 于是我们有

$$
A^{2}+A=(n-1) I+E,
$$

其中 $I$ 是 $n^{2}+1$ 阶单位矩阵, 而 $E$ 是所有元素都是 1 的 $\left(n^{2}+1\right) \times\left(n^{2}+1\right)$ 矩阵. 显然 $E$ 的秩是 1 , 所以 $E$ 有一个特征根是 $n^{2}+1$, 而其余 $n^{2}$ 个特征根都
是 0 . 由 (1) 式, $A$ 有一个特征根 $\lambda$ 满足 $\lambda^{2}+\lambda=n^{2}+n$, 其余所有特征根都满足 $\beta^{2}+\beta=n-1$. 所以 $\lambda=n$ 或 $-n-1$, 而 $\beta_{1,2}=\frac{-1 \pm \sqrt{4 n-3}}{2}$.

进一步分析可知 $\lambda$ 必须等于 $n$, 这是因为 $A$ 的每个行和都等于 $n$, 故 $n$ 一定是特征根 (而 $-n-1$ 不可能是). 然后考虑 $A$ 的迹, 一方面由于 $A$ 对角线上都是零, $\operatorname{tr}(A)=0$. 另一方面 $\operatorname{tr}(A)$ 是 $A$ 的所有特征根之和. 令 $k$ 是 $A$ 的特征根中 $\beta_{1}$ 的重数, 那么有

$$
k \cdot \frac{-1+\sqrt{4 n-3}}{2}+\left(n^{2}-k\right) \cdot \frac{-1-\sqrt{4 n-3}}{2}=-n .
$$

如果 $4 n-3$ 不是完全平方数, 那么由 (2) 必有 $k=n^{2}-k$. 于是 $-\frac{n^{2}}{2}=-n$, 导出 $n=2$. 下面假设 $n=m^{2}+m+1$, 于是 (2) 变成 $k \cdot m+\left(n^{2}-k\right)(-m-1)=-n$,也就是

$$
k \cdot(2 m+1)=n^{2}(m+1)-n=m\left(m^{2}+m+1\right)\left(m^{2}+2 m+2\right) \text {. }
$$

我们有 $(m, 2 m+1)=1,4 m^{2}+4 m+4 \equiv 3(\bmod 2 m+1), 4 m^{2}+8 m+8 \equiv 5$ $(\bmod 2 m+1)$. 于是由 $(3)$ 得到 $2 m+1 \mid 15$. 所以 $m=0,1,2,7$, 而相应地有 $n=1,3,7,57$, 正如之前所说的.

(3). 上面的漂亮结论是由 Hoffman 与 Singleton 在 1960 年得到的. 并且他们还构造了 $n=7$ 时的例子, 称为 Hoffman-Singleton 图. 然而对于 $n=57$ 目前仍没有定论, 是一个公开的问题. 另外可以考虑更一般的 Moore 图问题, 即对什么样的正整数对 $n, k$ 存在 $N=1+n \sum_{i=0}^{k-1}(n-1)^{i}$ 阶 $n$-正则图, 满足任意两点的距离 $\leq k$ (易证这个 $N$ 是理论最大值). Damarell 在 1973 年证明当 $n, k \geq 3$ 时这个上界无法取到. 但是求最大可能的阶数仍然是一个重要的未解决问题.

第四题. 给定正整数 $k$. 证明存在无穷多对互异正整数 $a, b$, 使得 $a^{2}+k$ 与 $b^{2}+k$ 有相同的素因子集合.

(哈佛大学牟晓生 供题)

## 证明 (根据供题者的解答整理):

要控制一个数的所有素因子无疑是很困难的. 幸好, 我们只要比较 $a^{2}+k$与 $b^{2}+k$ 的素因子. 把问题简单化, 我们只需要找到三元组 $(d, a, b)$, 使得 $a^{2}+k=d\left(b^{2}+k\right)$, 并且 $d \mid b^{2}+k$. 这样的两个数一定有相同的素因子, 而余下要做的就是适当选取 $d$ 使得上面的 Pell 方程有无穷多个满足 $d \mid b^{2}+k$ 的解.

我们从 $k=1$ 入手. 此时需要 $b^{2}+1 \mid a^{2}+1$. 由于 $n^{2}+1$ 的前几项是 $1,2,5,10$,
自然地考虑 $d=2$ 或者 $d=5$. 当 $d=2$ 时我们得到 Pell 方程 $a^{2}+1=2\left(b^{2}+1\right)$,显然此时 $b^{2}+1$ 是奇数, 无法符合条件. 如果 $d=5$, 那么我们得到 Pell 方程 $a^{2}-5 b^{2}=4$. 所有正整数解可以写为

$$
\frac{a+b \sqrt{5}}{2}=\left(\frac{3+\sqrt{5}}{2}\right)^{n} .
$$

我们需要 $5 \mid b^{2}+1$, 也即 $b \equiv 2,3(\bmod ) 5$. 而由 (4) 式通过二项式展开得到 $b \equiv n \cdot\left(\frac{3}{2}\right)^{n-1}(\bmod ) 5$. 这里 $\frac{3}{2}$ 理解为 3 乘上 2 的数论倒数, 结果也就是 -1 .于是当 $n \equiv 2,3(\bmod 5)$ 时也有 $b \equiv 2,3(\bmod 5)$, 我们也就证明了 $k=1$ 时的结论.

下面考虑一般的 $k$. 我们需要解 Pell 方程 $a^{2}+k=d\left(b^{2}+k\right)$, 即

$$
a^{2}-d b^{2}=k(d-1) .
$$

假设我们有 (5) 的一组解 $\left(a_{0}, b_{0}\right)$, 而 $x+\sqrt{d} y$ 是 $x^{2}-d y^{2}=1$ 的基本解, 那么 (5) 式有无穷多组解

$$
a+\sqrt{d} b=\left(a_{0}+\sqrt{d} b_{0}\right) \cdot(x+\sqrt{d} y)^{n} .
$$

特别注意, 一般无法断定上面给出的是 (5) 式的全部解. 例如之前考虑的情况 $k=1, d=5$, 不难验证它的全部解由三组不同的 $a_{0}, b_{0}$ 通过 (6) 式表出.

当然我们只要有无穷多组解就够了, 所以下面只考虑 (6) 式. 二项式展开并 $\bmod d$, 我们得到

$$
a+\sqrt{d} b \equiv\left(a_{0}+\sqrt{d} b_{0}\right) \cdot\left(x^{n}+\sqrt{d} n x^{n-1} y\right) \quad(\bmod d)
$$

于是

$$
b \equiv x^{n-1}\left(b_{0} x+n a_{0} y\right) \quad(\bmod d) .
$$

我们希望存在 $n$ 使得通过 (7) 式有 $d \mid b^{2}+1$. 由于 $x^{n-1}$ 这项难以控制,一个自然的想法是使得 $b_{0} x+n a_{0} y$ 能够遍历 $\bmod d$ 的完系 (尽管这既不必要也不够充分). 沿着这个思路走, 我们希望 $a_{0} y$ 与 $d$ 互素. 由于 $a_{0}^{2}-d b_{0}^{2}=k(d-1), a_{0}$ 与 $d$互素当且仅当 $d$ 与 $k$ 互素. 这样的 $d$ 是很好选取的.

另一方面, 虽然知道 $x^{2}-d y^{2}=1$ 是基本解但我们难以刻画 $y$ 的性质. 因此难点在于选取适当的 $d$ 使得 $(d, y)=1$. 通过模可以导出一些必要条件, 比如若 $d$ 是偶数则必是 8 的倍数. 但这样做很难得到充分条件. 为此, 我们接下来寻找特殊的 $d$ 使得 $x^{2}-d y^{2}=1$ 的基本解可以直接写出来. 可以想到这样的例子有 $d=m^{2}+\epsilon$, 其中 $m$ 是正整数, 而 $\epsilon \in\{ \pm 1, \pm 2, \pm 4\}$. 由于我们还需
要 $a_{0}^{2}+k=\left(m^{2}+\epsilon\right)\left(b_{0}^{2}+k\right)$ 存在解, 所以自然地考虑 $b_{0}, m$ 是 $k$ 的一次多项式,而 $a_{0}$ 是 $k$ 的二次多项式. 假设 $b_{0}$ 已经确定, 那么为保证 $b_{0}^{2}+k \mid a_{0}^{2}+k$ 我们可以令 $a_{0}=c\left(b_{0}^{2}+k\right) \pm b_{0}$. 这样就得到

$$
m^{2}+\epsilon=\frac{a_{0}^{2}+k}{b_{0}^{2}+k}=c^{2}\left(b_{0}^{2}+k\right) \pm 2 b_{0} c+1 .
$$

通过简单尝试可在等式右边取 $b_{0}=k, c=2$ 以及负号, 得到 $m=2 k$, $\epsilon=1$. 也即 $d=4 k^{2}+1, a_{0}=2 k^{2}+k, b_{0}=k$. 此时 $x^{2}-d y^{2}=1$ 的基本解是 $x+\sqrt{d} y=(2 k+\sqrt{d})^{2}$, 也即 $x=8 k^{2}+1, y=4 k$. 代回到 (7) 式中, 我们得到

$$
b \equiv(-1)^{n-1}(-k-n(2 k+1)) \quad\left(\bmod 4 k^{2}+1\right)
$$

由于 $4 k^{2}+1 \mid a_{0}^{2}+k$, 我们只需要 $k+n(2 k+1) \equiv 2 k^{2}+k\left(\bmod 4 k^{2}+1\right)$ 即可保证 $d \mid b^{2}+k$. 由于 $\left(2 k+1,4 k^{2}+1\right)=1$, 这样的 $n$ 有无穷多个, 证毕!

评注 有趣的是, 在上面的解答中也可以令 $a_{0}=2 k^{2}-k+1, b_{0}=k-1$, 同样对应 $d=4 k^{2}+1$. 有兴趣的同学可以试着寻找其他可能的 $d$.

