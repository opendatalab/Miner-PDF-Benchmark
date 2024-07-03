数学新星网 $\%$ 教师专栏

www.nsmath.cn/jszl

# 2016 年秋季上海新星数学奥林匹克试题解析 

吴尉迟 1 施柯杰 ${ }^{2}$

(1. 上海大学数学系, 200444；2. 复旦大学附属中学, 200433)

题 1. 设 $x_{1}, x_{2}, \cdots, x_{n}$ 是 $n$ 个不同的实数, 记 $D=\max _{1 \leq i<j \leq n}\left|x_{i}-x_{j}\right|$. 证明:存在 $x_{1}, x_{2}, \cdots, x_{n}$ 的一个排列 $y_{1}, y_{2}, \cdots, y_{n}$ 使得

$$
\left|\sum_{i=1}^{n} i y_{i}\right| \geq \frac{n-1}{2} D
$$

(上海大学 冷岗松 供题)

证法一 不妨设 $\max _{1 \leq i<j \leq n}\left|x_{i}-x_{j}\right|=\left|x_{1}-x_{n}\right|$. 令

$$
\begin{aligned}
& X=x_{1}+2 x_{2}+\cdots+(n-1) x_{n-1}+n x_{n}, \\
& Y=n x_{1}+2 x_{2}+\cdots+(n-1) x_{n-1}+x_{n} .
\end{aligned}
$$

则对任意 $\sigma \in S_{n}$, 有

$$
\begin{aligned}
\max _{\sigma \in S_{n}}\left|\sum_{i=1}^{n} i x_{\sigma(i)}\right| & \geq \max \{|X|,|Y|\} \geq \frac{|X-Y|}{2} \\
& =\frac{1}{2}(n-1)\left|x_{n}-x_{1}\right| \\
& =\frac{n-1}{2} D .
\end{aligned}
$$

证法二 设 $y_{1} \leq y_{2} \leq \cdots \leq y_{n}$ 为 $x_{1}, x_{2}, \cdots, x_{n}$ 的递增排列, 则

$$
\max _{1 \leq i<j \leq n}\left|x_{i}-x_{j}\right|=y_{n}-y_{1} .
$$

记 $X=\sum_{i=1}^{n} i y_{i}, Y=\sum_{i=1}^{n} i y_{n+1-i}$, 则由排列不等式知

$$
\sum_{i=2}^{n-1} i y_{i} \geq \sum_{i=2}^{n-1} i y_{n+1-i}
$$

收稿日期: 2016-12-05; 修订日期: 2017-01-07.
从而

$$
\begin{aligned}
X-Y & =\left(n y_{n}+y_{1}\right)-\left(n y_{1}+y_{n}\right)+\sum_{i=2}^{n-1} i\left(y_{i}-y_{n+1-i}\right) \\
& \geq(n-1)\left(y_{n}-y_{1}\right) \\
& =(n-1) \max _{1 \leq i<j \leq n}\left|x_{i}-x_{j}\right| .
\end{aligned}
$$

因此

$$
\begin{aligned}
\max (|X|,|Y|) & \geq \frac{1}{2}(|X|+|Y|) \geq \frac{1}{2}|X-Y| \\
& \geq \frac{1}{2}(n-1) \max _{1 \leq i<j \leq n}\left|x_{i}-x_{j}\right| .
\end{aligned}
$$

故 $x_{1}, \cdots, x_{n}$ 的排列 $y_{1} \leq \cdots \leq y_{n}$ 或 $y_{n} \leq \cdots \leq y_{1}$ 满足要求, 结论成立.

评注 此题难度并不大. 此类存在性问题可以采用优化的思想. 选取两个 $x_{1}, \cdots, x_{n}$ 的排列, 并用绝对值的三角不等式得出结论. 事实上, 此题是下面命题的一个特例:

设 $x_{1}, x_{2}, \cdots, x_{n}$ 是 $n$ 个向量, $\alpha_{1}, \alpha_{2}, \cdots, \alpha_{n}$ 是 $n$ 个实数, 则存在 $x_{1}, x_{2}, \cdots, x_{n}$的一个排列 $y_{1}, y_{2}, \cdots, y_{n}$ 使得

$$
\left|\sum_{i=1}^{n} \alpha_{i} y_{i}\right| \geq \frac{n-1}{2} D
$$

其中 $D=\max _{1 \leq i<j \leq n}\left|x_{i}-x_{j}\right|$.

题 2. 设 $A$ 是任意大于 1 的整数, $p_{1}, \cdots, p_{k}$ 是 $k$ 个互不相同的素数 $(k \geq 1)$.证明: 存在整数 $x \geq 0$ 使得满足 $x<m \leq x+A$, 且与所有 $p_{i}(i=1, \cdots, k)$ 均互素的正整数 $m$ 的个数不超过 $A \prod_{i=1}^{k}\left(1-\frac{1}{p_{i}}\right)$.

(苏州大学 余红兵 供题)

证明 记 $B_{k}=p_{1} \cdots p_{k}$, 因为模 $B_{k}$ 的一个缩系中恰有 $\varphi\left(B_{k}\right)$ 个数与 $B_{k}$互素，而区间 $\left[1, A B_{k}\right]$ 可表示为 $A$ 个模 $B_{k}$ 的缩系之并, 故该区间中恰有 $A \varphi\left(B_{k}\right)=A p_{1} \cdots p_{k}\left(1-\frac{1}{p_{1}}\right) \cdots\left(1-\frac{1}{p_{k}}\right)$ 个数与 $p_{1} \cdots p_{k}$ 互素, 这里 $\varphi$ 是欧拉函数.

另一方面，区间 $\left[1, A B_{k}\right]$ 可表示为下面 $B_{k}$ 个区间的并:

$$
(0, A], \quad(A, 2 A], \cdots, \quad\left(\left(B_{k}-1\right) A, B_{k} A\right] .
$$

记第 $i$ 个区间中与 $B_{k}$ 互素的个数为 $x_{i}, i=1, \cdots, B_{k}$, 则由上面结果知

$$
\sum_{1 \leq i \leq B_{k}} x_{i}=A B_{k}\left(1-\frac{1}{p_{1}}\right) \cdots\left(1-\frac{1}{p_{k}}\right)
$$

故有一个 $i \in\left\{1,2, \cdots, B_{k}\right\}$, 使得 $x_{i} \leq A\left(1-\frac{1}{p_{1}}\right) \cdots\left(1-\frac{1}{p_{k}}\right)$, 即区间 $((i-1) A, i A]$符合要求, 即可取 $x=(i-1) A$.

评注 此题可以利用欧拉函数性质, 采用整体估计的方法, 然后利用平均值原理便可证明.

题 3. 如图, $\triangle A B C$ 中, $A B>A C$, 点 $H$ 为垂心, 点 $S, M$ 在边 $B C$ 上且满足 $B M=C M, \angle B H M=\angle C H S$, 点 $P$ 为点 $A$ 在直线 $H S$ 上的射影. 证明: $\triangle M P S$ 的外接圆与 $\triangle A B C$ 的外接圆相切.

(上海理工大学 张思汇 供题)



第 3 题配图



证法一配图

证法一 连接 $A H$ 并延长交 $\triangle A B C$ 的外接圆于点 $D$, 作 $D E / / B C$ 与 $\triangle A B C$的外接圆交于点 $E$.

易知 $D, H$ 关于 $B C$ 对称, 故 $\angle H C B=\angle B C D=\angle C B E$, 因此 $C H / / B E$.由此推出 $E B \perp A B$. 故 $A E$ 为 $\triangle A B C$ 外接圆的直径.

又由 $C H=C D=E B$, 结合 $C H / / B E$ 知四边形 $C H B E$ 为平行四边形,所以 $E H$ 过点 $M$.

设 $B^{\prime}, C^{\prime}$ 为 $B, C$ 在 $A C, B C$ 上的射影, 延长 $E H$ 交 $\triangle A B C$ 的外接圆于点 $Q$. 由 $\angle A Q H=\angle A Q E=90^{\circ}=\angle A P H$, 得 $A, Q, B^{\prime}, H, C^{\prime}, P$ 共圆, 且以 $A H$为直径.

由 $\angle B H M=\angle C H S$ 可得 $\angle B^{\prime} H Q=\angle C^{\prime} H P$. 所以 $Q B^{\prime}=P C^{\prime}$ (相等的圆周角所对弦长相等), 故有 $P Q / / B^{\prime} C^{\prime}$.

由 $\angle E A B+\angle B^{\prime} C^{\prime} A=90^{\circ}-\angle A E B+\angle A C B=90^{\circ}$, 得 $A E \perp B^{\prime} C^{\prime}$. 所以

$$
A E \perp P Q \text {. }
$$

结合 $A Q \perp Q E$ 有

$$
\angle A Q P=\angle A E Q .
$$

由此推出

$$
\begin{aligned}
\angle S D H & =\angle S H D=\angle A H P=\angle A Q P \\
& =\angle A E Q=\angle A D Q=\angle Q D H
\end{aligned}
$$

所以点 $Q, S, D$ 共线. 再由

$$
\angle Q P S=\angle Q P H=\angle Q A H=\angle Q A D=\angle Q E D=\angle Q M S
$$

得, $P, Q, S, M$ 四点共圆 $\omega$.

过点 $Q$ 作 $\triangle A B C$ 外接圆的切线, 由

$$
\angle T Q S=\angle T Q D=\angle Q E D=\angle Q M S
$$

知, $T Q$ 也是圆 $\omega$ 的切线.

故 $\triangle M P S$ 的外接圆与 $\triangle A B C$ 的外接圆相切, 证毕.

证法二 (杭州二中学生竺沈涵等) 设 $\odot(A B C)$的外心为 $O$, 取 $A$ 关于 $\odot O$ 的对径点 $E$, 连接 $A E$.则 $B E \perp A B, C E \perp A C$, 结合 $C H \perp A B, B H \perp A C$可知 $B E / / C H, C E / / B H$. 所以四边形 $B H C E$ 是平行四边形, 结合 $M$ 是中点可得 $H, M, E$ 三点共线.



延长 $E H$ 交 $\odot O$ 于 $Q$ 点, 从而由 $\angle A Q H=\angle A P H=90^{\circ}$ 可知 $A, T, H, P$四点共圆. 连接 $A H$ 并延长交 $\triangle A B C$ 的外接圆于点 $D$, 易知 $D, H$ 关于 $B C$ 对称. 结合四边形 $B H C E$ 是平行四边形, 有 $C D=C H=B E$, 从而 $B C / / D E$.

另一方面，

$$
\angle P Q M=\angle P Q H=\angle P A H=90^{\circ}-\angle A H P=90^{\circ}-\angle S H D=\angle P S M,
$$

所以有 $P T S M$ 四点共圆 $\omega$.

连接 $T S, S D$. 由 $H, D$ 关于 $B C$ 对称可知

$$
\begin{aligned}
\angle C D S & =\angle C H S=\angle B H M=\angle B H E \\
& =\angle C E H=\angle C E T=\angle C D T .
\end{aligned}
$$

故 $Q, S, D$ 三点共线.

过点 $Q$ 作 $\triangle A B C$ 外接圆的切线, 由 $Q, S, D$ 三点共线和 $B C / / D E$ 可得

$$
\angle T Q S=\angle T Q D=\angle Q E D=\angle Q M S
$$

因此, $T Q$ 也是圆 $\omega$ 的切线.
故 $\triangle M P S$ 的外接圆与 $\triangle A B C$ 的外接圆相切, 证毕.

评注 此题巧妙地将切点 “隐藏” 了起来, 所以要点是找出切点, 再利用垂心的一些对称性质来证明.

题 4. 对每个正整数 $n$, 用 $S_{2}(n)$ 表示 $n$ 在二进制表示下的各位数字之和.证明: 存在无穷多个正整数对 $\left(a_{1}, b_{1}\right),\left(a_{2}, b_{2}\right), \cdots$, 使得对任意正整数 $k$, 均有 $\frac{a_{k}}{b_{k}}=\frac{S_{2}\left(a_{k}\right)}{S_{2}\left(b_{k}\right)}$, 且 $\frac{a_{1}}{b_{1}}, \frac{a_{2}}{b_{2}}, \cdots$ 的值两两不同.

(华东师范大学 何忆捷 供题)

证法一 首先证明, 对每个正整数 $k$, 存在正整数 $m_{k}$, 满足

$$
S_{2}\left(m_{k}\right)=2^{k+1}, \quad S_{2}\left(3 m_{k}\right)=3
$$

为此, 取

$$
m_{k}=1+\left(\sum_{i=1}^{t_{k}} 2^{2 i-1}\right)+2^{2 t_{k}}
$$

其中 $t_{k}=2^{k+1}-2$.

由 (2) 知, $S_{2}\left(m_{k}\right)=t_{k}+2=2^{k+1}$. 又考虑到

$$
\begin{aligned}
3 m_{k} & =3+3 \cdot \frac{2 \cdot\left(2^{2 t_{k}}-1\right)}{2^{2}-1}+3 \cdot 2^{2 t_{k}} \\
& =3+2 \cdot\left(2^{2 t_{k}}-1\right)+3 \cdot 2^{2 t_{k}} \\
& =1+5 \cdot 2^{2 t_{k}}=1+2^{2 t_{k}}+2^{2 t_{k}+2}
\end{aligned}
$$

故 $S_{2}\left(3 m_{k}\right)=3$. 从而由 (2) 所定义的正整数 $m_{k}$ 满足 (1).

以下令

$$
a_{k}=2^{k+1} m_{k}, \quad b_{k}=3 m_{k}, \quad k=1,2, \cdots,
$$

结合 (1) 知

$$
\frac{a_{k}}{b_{k}}=\frac{2^{k+1}}{3}=\frac{S_{2}\left(m_{k}\right)}{S_{2}\left(3 m_{k}\right)}=\frac{S_{2}\left(2^{k+1} m_{k}\right)}{S_{2}\left(3 m_{k}\right)}=\frac{S_{2}\left(a_{k}\right)}{S_{2}\left(b_{k}\right)}
$$

并且当 $k$ 取不同正整数时, 各 $\frac{a_{k}}{b_{k}}=\frac{2^{k+1}}{3}$ 的值两两不同. 证毕.

证法二 (雅礼中学学生陈伊一) 对每一个正整数 $k$, 令

$$
\begin{aligned}
a_{k} & =\sum_{i=1}^{2^{k+1}}\left(2^{k+1}\right)^{i} \\
b_{k} & =\sum_{i=1}^{2^{k+1}}\left(2^{k+1}\right)^{i} \frac{2^{k+1}+1}{2^{k+1}}
\end{aligned}
$$

$$
\begin{aligned}
& =\sum_{i=1}^{2^{k+1}}\left(2^{k+1}\right)^{i}+\sum_{i=0}^{2^{k+1}-1}\left(2^{k+1}\right)^{i} \\
& =1+\left(2^{k+1}\right)^{2^{k+1}}+2 \sum_{i=1}^{2^{k+1}-1}\left(2^{k+1}\right)^{i} \\
& =1+\left(2^{k+1}\right)^{2^{k+1}}+\sum_{i=1}^{2^{k+1}-1} 2^{(k+1) i+1} .
\end{aligned}
$$

因为 $k \geq 1$, 故 $2^{k+1}(k+1)>\left(2^{k+1}-1\right)(k+1)+1$, 于是

$$
\begin{aligned}
& S_{2}\left(a_{k}\right)=2^{k+1}, \\
& S_{2}\left(b_{k}\right)=2^{k+1}+1 .
\end{aligned}
$$

故

$$
\frac{S_{2}\left(a_{k}\right)}{S_{2}\left(b_{k}\right)}=\frac{2^{k+1}}{2^{k+1}+1}=\frac{a_{k}}{b_{k}}
$$

并且当 $k$ 取不同正整数时, 各 $\frac{a_{k}}{b_{k}}=\frac{2^{k+1}}{3}$ 的值两两不同, 证毕.

评注 此题的解法虽然较多, 但需要一定的想法和尝试.

题 5. 设 $n \geq 2$ 为整数, $A_{1}, A_{2}, \cdots, A_{2^{n}}$ 为 $\{1,2, \cdots, n\}$ 的所有子集的任一个排列. 求

$$
\sum_{i=1}^{2^{n}}\left|A_{i} \cap A_{i+1}\right| \cdot\left|A_{i} \cup A_{i+1}\right|
$$

的最大值, 其中 $A_{2^{n}+1}=A_{1}$.

(北京大学 吴茁 供题)

证明 先证两个引理.

引理 1. 设 $A_{1}, A_{2}, \cdots, A_{2^{n}}$ 是集合 $\{1,2, \cdots, n\}$ 的所有子集, 则存在 $A_{1}, A_{2}$, $\cdots, A_{2^{n}}$ 的一个排列 $B_{1}, B_{2}, \cdots, B_{2^{n}}$, 使得对任意的 $i=1,2, \cdots, 2^{n}$ 均满足 $B_{i}, B_{i+1}$ 中的一个是另一个的子集, 且元素个数差 1 , 其中约定 $B_{2^{n}+1}=B_{1}$.

引理 1 的证明 对 $n$ 用归纳法.

当 $n=2$ 时, 集合 $\{1,2\}$ 的 4 个子集排列为 $\emptyset,\{1\},\{1,2\},\{2\}$ 便满足要求.

假设当 $n=k$ 时存在排列 $B_{1}, B_{2}, \cdots, B_{2^{n}}$ 满足要求, 则当 $n=k+1$ 时, 考虑下面的排列 $B_{1}, B_{2}, \cdots, B_{2^{k}}, B_{2^{k}} \cup\{k+1\}, B_{2^{k}-1} \cup\{k+1\}, \cdots, B_{2} \cup\{k+1\}, B_{1} \cup\{k+1\}$,这显然是集合 $\{1,2, \cdots, k+1\}$ 的所有子集满足要求的一个排列.
引理 1 证毕.

引理 2. 设 $A, B$ 是任意两个不同有限集, 则

$$
2|A \cap B| \cdot|A \cup B| \leq|A|^{2}+|B|^{2}-1
$$

当 $A, B$ 中一个为另一个的子集, 且元素个数差 1 时等号成立.

引理 2 的证明 设 $|A \backslash B|=x,|B \backslash A|=y .|A \cap B|=z$.

因 $A \neq B$, 故 $x, y$ 不能同时为 0 , 于是 $x, y$ 中至少有一个 $\geq 1$.

显然

$$
\text { (1) } \begin{aligned}
& \Leftrightarrow 2(x+y+z) z \leq(x+z)^{2}+(y+z)^{2}-1 \\
& \Leftrightarrow x^{2}+y^{2} \geq 1,
\end{aligned}
$$

这是显然成立的.

又当 $A, B$ 中一个为另一个的子集时且元素个数差 1 时, $x, y$ 中有一个为 0 ,一个为 1. (2) 中取等号, 从而 (1) 也取等号.

引理 2 证毕.

回到原题. 由引理 2 可得

$$
\begin{aligned}
\sum_{i=1}^{2^{n}}\left|A_{i} \cap A_{i+1}\right|\left|A_{i} \cup A_{i+1}\right| & \leq \frac{1}{2} \sum_{i=1}^{2^{n}}\left(\left|A_{i}\right|^{2}+\left|A_{i+1}\right|^{2}-1\right) \\
& =\sum_{i=1}^{n}\left|B_{i}\right|^{2}-2^{n-1} \\
& =\sum_{k=1}^{n} k^{2} C_{n}^{k}-2^{n-1} \\
& =\left(n^{2}+n\right) 2^{n-2}-2^{n-1} \\
& =\left(n^{2}+n-2\right) 2^{n-2} .
\end{aligned}
$$

又如果将 $\{1,2, \cdots, n\}$ 的所有子集按照引理 1 中的排法便知上式等号成立.

故所求的最大值为 $\left(n^{2}+n-2\right) 2^{n-2}$.

评注 这是一道难题, 其难点在于需要观察到

$$
2|A \cap B| \cdot|A \cup B| \leq|A|^{2}+|B|^{2}-1
$$

这一局部不等式.

题 6. 设 $A_{1}, A_{2}, \cdots, A_{13}$ 是太空中的 13 颗新星. 对任意 $i, j(1 \leq i<j \leq 13)$,从新星 $A_{i}$ 通行至 $A_{j}$, 或从新星 $A_{j}$ 通行至 $A_{i}$, 需花费 $f(i, j)$ 个太空币. 问是否可将各 $f(i, j)(1 \leq i<j \leq 13)$ 的值设定为两两不同的正整数, 使得从 $A_{1}$ 出发,
以无论何种次序经过 $A_{2}, A_{3}, \cdots, A_{13}$ 各一次, 再回到 $A_{1}$, 总是花费恰好 2017 个太空币?

(华东师范大学 何忆捷 供题)

解 结论是肯定的. 我们设

$$
f(i, j)=a_{i}+a_{j}-1(1 \leq i<j \leq 13),
$$

其中 $a_{1}, a_{2}, \cdots, a_{13}$ 为待定正整数, 且满足

$$
a_{1}+a_{2}+\cdots+a_{13}=1015
$$

此时, 设 $\left(t_{2}, t_{3}, \cdots, t_{13}\right)$ 为 $(2,3, \cdots, 13)$ 的任何一个排列, 并约定 $t_{1}=t_{14}=$ 1 , 则从 $A_{1}$ 出发依次经过新星 $A_{t_{2}}, A_{t_{3}}, \cdots, A_{t_{13}}$ 再回到 $A_{1}$ 所需花费的太空币数为

$$
\sum_{k=1}^{13} f\left(t_{k}, t_{k+1}\right)=\sum_{k=1}^{13}\left(a_{t_{k}}+a_{t_{k+1}}-1\right)=2 \cdot\left(\sum_{i=1}^{13} a_{i}\right)-13=2017 .
$$

下面对 $a_{1}, a_{2}, \cdots, a_{13}$ 取适当的正整数值, 使得各 $f(i, j)(1 \leq i<j \leq 13)$ 的值两两不同. 为此令

$$
\left(a_{1}, a_{2}, \cdots, a_{13}\right)=(1,2,3,5,8,13,21,34,55,89,144,233,407)
$$

这样有

$$
a_{1}+a_{2}+\cdots+a_{13}=1015
$$

且

$$
a_{i}+a_{i+1}=a_{i+2}(i=1,2, \cdots, 10), a_{11}+a_{12}<a_{13} .
$$

考虑任意两组不同的 $(i, j),\left(i^{\prime}, j^{\prime}\right)$, 其中 $1 \leq i<j \leq 13,1 \leq i^{\prime}<j^{\prime} \leq 13$.

若 $j \neq j^{\prime}$, 不妨设 $j<j^{\prime}$, 那么结合 (3) 知,

$$
a_{i}+a_{j} \leq a_{j-1}+a_{j} \leq a_{j+1} \leq a_{j^{\prime}}<a_{i^{\prime}}+a_{j^{\prime}}
$$

若 $j=j^{\prime}$, 不妨设 $i<i^{\prime}$, 那么 $a_{i}<a_{i^{\prime}}$, 则 $a_{i}+a_{j}<a_{i^{\prime}}+a_{j^{\prime}}$.

因此总有 $a_{i}+a_{j} \neq a_{i^{\prime}}+a_{j^{\prime}}$, 从而

$$
f(i, j)=a_{i}+a_{j}-1 \neq a_{i^{\prime}}+a_{j^{\prime}}-1=f\left(i^{\prime}, j^{\prime}\right) .
$$

综上可知, 由 (1), (2) 所确定的各 $f(i, j)$ 的取值符合题意.

评注 此题改编自第 64 届俄罗斯圣彼得堡数学奥林匹克选拔赛十年级第3 题 (参见林常《俄罗斯圣彼得堡数学奥林匹克题解》, 浙江大学出版社), 改编后比原题要求更高, 解题者并不能平凡地套用原解法, 而需做较大的变通.
虽然要构造 $f(i, j)=a_{i}+a_{j}-1(1 \leq i<j \leq 13)$ 是有难度的, 但我们也可以从 $f(i, j)+f(m, n)=f(i, m)+f(j, n)$ 和 $f(i, j)=f(j, i)$ 这两个性质窥探一二,正是由于这样一种对称性, 最自然的想法是用加法这一可交换的运算来构造 $f(i, j)=a_{i}+a_{j}$. 为了使其有解, 我们又可能令 $f(i, j)=a_{i}+a_{j}-1$. 又为了使 $f(i, j)$ 两两不同, 就要求 $a_{i}, a_{j}$ 足够分散, 从而想到用斐波那契数列来构造 $a_{i}$.

