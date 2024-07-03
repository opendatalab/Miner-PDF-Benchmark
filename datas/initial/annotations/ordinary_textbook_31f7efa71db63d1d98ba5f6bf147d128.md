# 好题与妙解（十） 

胡珏伟 冷岗松

(上海大学, 200444)

2014 年, 本文的第二作者在当年的国内外数学竞赛试题和一些外文期刊中精心挑选了 18 个问题作为参加 CMO 学生的讨论题, 当时国内的几位高手高继扬 (上海中学), 吴东晓 (深圳第三中学), 黄一山、陈泽坤 (武钢三中) 等都提交了这些问题的解法. 前些时候周天佑老师受邀从中选择了他认为有意思的六个问题. 对这六个问题, 本文的第一作者从同学们的解答中选出优秀的解法并进行了整理和点评. 本文还收录了今年国家集训队队员颜川皓同学 (上海中学) 关于第三题的新解法, 现在这六个问题我们认为或许可以作为一套 CMO 的模拟试题. 不当之处, 敬请读者批评指正.

## I. 问 题

题 1. 设 $n$ 是正整数, $x_{1}, x_{2}, \cdots, x_{n}$ 是正实数. 令 $S=x_{1}^{n}+x_{2}^{n}+\cdots+x_{n}^{n}, P=$ $x_{1} x_{2} \cdots x_{n}$, 证明:

$$
\sum_{k=1}^{n} \frac{1}{S-x_{k}^{n}+P} \leq \frac{1}{P}
$$

题 2. 设 $n$ 和 $b$ 都是正整数. 我们称 $n$ 是 $b-$ 可识别的, 如果存在由 $n$ 个都小于 $b$ 的不同正整数组成的集合, 其没有两个不同的子集 $U$ 和 $V$, 使得 $U$ 中所有元之和等于 $V$ 中所有元之和.

(i) 证明: 8 是 $100-$ 可识别的;

(ii) 证明: 9 不是 100 - 可识别的.

题 3. 设 $n$ 为正整数. 试求

$$
|p(1)|^{2}+|p(2)|^{2}+\cdots+|p(n+3)|^{2}
$$

的最小值, 其中 $p$ 为首项系数为 1 的 $n$ 次多项式.

修订日期: 2020-09-28.
题 4. 试求所有的正整数 $n \geq 2$, 使得存在整数 $x_{1}, x_{2}, \cdots, x_{n-1}$ 满足: 如果 $0<i, j<n, i \neq j$, 且 $n \mid(2 i+j)$, 那么 $x_{i}<x_{j}$.

题 5. 设 $D=\{0,1,2, \cdots, 9\}$ 为十进制数字集合, $R \subset D \times D$ 为有序数对的集合. 称无限数字序列 $\left(a_{1}, a_{2}, a_{3}, \cdots\right)$ 与 $R$ 是一致的, 若对每个正整数 $j$ 有 $\left(a_{j}, a_{j+1}\right) \in R$. 试求最小的正整数 $k$ 满足: 如果任意的 $R \subset D \times D$ 与至少 $k$ 个不同的数字序列是一致的, 那么 $R$ 与无限多个数字序列是一致的.

题 6. 设 $n$ 为正整数. 我们有 $n$ 个箱子, 并且每个箱子有非负整数个鹅卵石.定义一次操作为: 从一个箱子中取两个我岛石, 然后丢掉其中一个我卯石, 并把另一个我鸟卯石放到其他的任意一个箱子里. 我们称鹅卵石的初始状态是可解的,如果可以经过有限次(可以为 0 次)操作, 使得所有的箱子非空. 试求我勿石的所有不可解初始状态, 但是如果给其中任意一个箱子额外添加一个我岛石可以变成可解的初始状态.

## II . 解答与评注

题 1. 设 $n$ 是正整数, $x_{1}, x_{2}, \cdots, x_{n}$ 是正实数. 令 $S=x_{1}^{n}+x_{2}^{n}+\cdots+x_{n}^{n}, P=$ $x_{1} x_{2} \cdots x_{n}$, 证明:

$$
\sum_{k=1}^{n} \frac{1}{S-x_{k}^{n}+P} \leq \frac{1}{P}
$$

证明 (吴东晓) 先证局部不等式

$$
\frac{P}{S-x_{k}^{n}+P} \leq \frac{x_{k}}{x_{1}+x_{2}+\cdots+x_{n}} . \quad(k=1,2, \cdots, n)
$$

考虑到

$$
\begin{aligned}
(1) & \Leftrightarrow\left(\sum_{i=1}^{n} x_{i}\right) \prod_{i=1}^{n} x_{i} \leq x_{k}\left(\sum_{\substack{i=1 \\
i \neq k}}^{n} x_{i}^{n}+\prod_{i=1}^{n} x_{i}\right) \\
& \Leftrightarrow\left(\sum_{\substack{i=1 \\
i \neq k}}^{n} x_{i}\right) \prod_{i=1}^{n} x_{i} \leq x_{k}\left(\sum_{\substack{i=1 \\
i \neq k}}^{n} x_{i}^{n}\right) \\
& \Leftrightarrow\left(\sum_{\substack{i=1 \\
i \neq k}}^{n} x_{i}\right) \prod_{\substack{i=1 \\
i \neq k}}^{n} x_{i} \leq \sum_{\substack{i=1 \\
i \neq k}}^{n} x_{i}^{n} .
\end{aligned}
$$

由幕平均不等式和均值不等式可得

$$
\sum_{\substack{i=1 \\ i \neq k}}^{n} x_{i}^{n} \geq(n-1)\left(\frac{1}{n-1} \cdot \sum_{\substack{i=1 \\ i \neq k}}^{n} x_{i}\right)^{n}
$$

$$
\begin{aligned}
& =\left(\sum_{\substack{i=1 \\
i \neq k}}^{n} x_{i}\right)\left(\frac{1}{n-1} \cdot \sum_{\substack{i=1 \\
i \neq k}}^{n} x_{i}\right)^{n-1} \\
& \geq\left(\sum_{\substack{i=1 \\
i \neq k}}^{n} x_{i}\right) \prod_{\substack{i=1 \\
i \neq k}}^{n} x_{i} .
\end{aligned}
$$

即 (1) 式得证.

故

$$
\sum_{k=1}^{n} \frac{1}{S-x_{k}^{n}+P}=\frac{1}{P} \sum_{k=1}^{n} \frac{P}{S-x_{k}^{n}+P} \leq \frac{1}{P} \sum_{k=1}^{n} \frac{x_{k}}{x_{1}+x_{2}+\cdots+x_{n}}=\frac{1}{P}
$$

由幕平均不等式和均值不等式的等号成立条件知, 当 $x_{1}=x_{2}=\cdots=x_{n}$ 时等号成立.

评注 本题的关键在于将证明题目所给不等式转化为证明局部不等式 (1),将 (1) 转化为没有 $x_{k}$ 的形式后, 利用幕平均不等式进行降幂即可得到证明.

题 2. 设 $n$ 和 $b$ 都是正整数. 我们称 $n$ 是 $b-$ 可识别的, 如果存在由 $n$ 个都小于 $b$ 的不同正整数组成的集合, 其没有两个不同的子集 $U$ 和 $V$, 使得 $U$ 中所有元之和等于 $V$ 中所有元之和.

(i) 证明: 8 是 100 - 可识别的;

(ii) 证明: 9 不是 100 - 可识别的.

## 证明 1 (高继扬)

(i) 考虑集合 $\{99,98,97,95,92,87,79,66\}(98=99-1,97=99-1-$ $1,95=99-1-1-2, \cdots, 66=99-1-1-2-3-5-8-13)$, 直接验证知任两个子集元素不和相等, 故 8 是 $100-$ 可识别的.

(ii) 若 9 是 $100-$ 可识别的. 设 $A=\left\{x_{1}, x_{2}, \cdots, x_{9}\right\}, 0<x_{1}<x_{2}<\cdots<$ $x_{9} \leq 100$. 考虑 $A$ 的 $2^{9}$ 个子集元素和从小到大排列

$$
0=s_{1}<s_{2}<\cdots<s_{2^{9}} .
$$

有

$$
\sum_{1 \leq i<j \leq 2^{9}}\left(s_{i}-s_{j}\right)^{2} \geq \sum_{1 \leq i<j \leq 2^{9}}(i-j)^{2}=2^{9} \cdot \sum_{i=1}^{2^{9}} i^{2}-\left(\sum_{i=1}^{2^{9}} i\right)^{2}=5726601216
$$

而

$$
\sum_{1 \leq i<j \leq 2^{9}}\left(s_{i}-s_{j}\right)^{2}=\frac{1}{2} \sum_{U_{1}, U_{2} \subset A}\left(\sum_{x \in U_{1}} x-\sum_{x \in U_{2}} x\right)^{2}
$$

$$
\begin{aligned}
& =\frac{1}{2} \cdot 2^{8} \cdot 2^{8} \cdot 2 \sum_{i=1}^{9} x_{i}^{2} \\
& =2^{16} \sum_{i=1}^{9} x_{i}^{2}
\end{aligned}
$$

故

$$
\sum_{i=1}^{9} x_{i}^{2} \geq 87381
$$

而

$$
\sum_{i=1}^{9} x_{i}^{2} \leq 100^{2}+99^{2}+\cdots+92^{2}=83004
$$

矛盾！因此 9 不是 100 - 可识别的.

## 证明 2

若 9 是 100 - 可识别的. 设 $A=\left\{x_{1}, x_{2}, \cdots, x_{9}\right\}, 0<x_{1}<x_{2}<\cdots<x_{9} \leq$ 100. 令 $X$ 是所有 $A$ 中元素个数为 $3,4,5,6$ 的子集的集合, 令 $Y$ 是所有 $A$ 中恰好有 2 或 3 或 4 个元素大于 $x_{3}$ 的子集的集合. $X$ 中含有的 $A$ 子集的个数为

$$
\left(\begin{array}{l}
9 \\
3
\end{array}\right)+\left(\begin{array}{l}
9 \\
4
\end{array}\right)+\left(\begin{array}{l}
9 \\
5
\end{array}\right)+\left(\begin{array}{l}
9 \\
6
\end{array}\right)=84+126+126+84=420
$$

个. 其中 $X$ 中集合元素和最大的 $A$ 的子集为 $\left\{x_{4}, x_{5}, \cdots, x_{9}\right\}$, 集合元素和最小的子集为 $\left\{x_{1}, x_{2}, x_{3}\right\}$. 即所有 $X$ 中 420 个 $A$ 的子集元素之和至少为 $x_{1}+x_{2}+x_{3}$,至多为 $x_{4}+x_{5}+\cdots+x_{9}$. 考虑到每个子集的元素和均不相同, 有

$$
\left(x_{4}+x_{5}+\cdots+x_{9}\right)-\left(x_{1}+x_{2}+x_{3}\right)+1 \geq 420 .
$$

下面计算 $Y$ 中元素的个数. 考虑到集合 $\left\{x_{4}, x_{5}, \cdots, x_{9}\right\}$ 中两元子集的个数为 $\left(\begin{array}{l}6 \\ 2\end{array}\right)$, 三元子集的个数为 $\left(\begin{array}{l}6 \\ 3\end{array}\right)$, 四元子集的个数为 $\left(\begin{array}{l}6 \\ 4\end{array}\right)$, 且 $\left\{x_{1}, x_{2}, x_{3}\right\}$ 的不同子集个数为 8 个. 因此 $Y$ 中 $A$ 的子集的个数为

$$
8\left(\left(\begin{array}{l}
6 \\
2
\end{array}\right)+\left(\begin{array}{l}
6 \\
3
\end{array}\right)+\left(\begin{array}{l}
6 \\
4
\end{array}\right)\right)=8(15+20+15)=400
$$

个. 同理考虑 $Y$ 中子集元素和最大数与最小数有

$$
\left(x_{1}+x_{2}+x_{3}+x_{6}+x_{7}+x_{8}+x_{9}\right)-\left(x_{4}+x_{5}\right)+1 \geq 400 .
$$

结合式 $(1),(2)$ 有 $2\left(x_{6}+x_{7}+x_{8}+x_{9}\right) \geq 818$, 而

$$
x_{9}+98+97+96 \geq x_{9}+x_{8}+x_{7}+x_{6} \geq 409 \text {, }
$$

即 $x_{9} \geq 118$, 与 $x_{9}<100$ 矛盾. 因此 9 不是 $100-$ 可识别的.
评注 证明不是 100 - 可识别的关键在于用反证法推出矛盾. 本题的解法 1 通过对子集元素和之差算两次导出矛盾, 解法 2 是官方给出的解答, 考虑两个 $A$ 中不同性质的子集个数结合子集的元素和不相同导出矛盾.

题 3. 设 $n$ 为正整数. 试求

$$
|p(1)|^{2}+|p(2)|^{2}+\cdots+|p(n+3)|^{2}
$$

的最小值, 其中 $p$ 为首项系数为 1 的 $n$ 次多项式.

## 解 1 (颜川皓)

设 $P(x)=\left(x-z_{1}\right) \cdots\left(x-z_{n}\right)\left(z_{1}, \cdots, z_{n} \in \mathbb{Z}\right)$, 则

$$
S=\sum_{i=1}^{n+3}|P(i)|^{2}=\sum_{i=1}^{n+3} \prod_{j=1}^{n}\left|i-z_{j}\right|^{2} \geq \sum_{i=1}^{n+3} \prod_{j=1}^{n}\left|i-R e z_{j}\right|^{2}
$$

故不妨设 $P$ 为实系数多项式, 即 $z_{1}, \cdots, z_{n} \in \mathbb{R}$.

令 $x_{i}=P(i)(1 \leq i \leq n+3)$, 则 $x_{i} \in \mathbb{R}$, 由差分公式有

$$
\begin{gathered}
x_{n+1}-\mathrm{C}_{n}^{1} x_{n}+\cdots+(-1)^{n} \mathrm{C}_{n}^{n} x_{1}=n !, \\
x_{n+2}-\mathrm{C}_{n}^{1} x_{n+1}+\cdots+(-1)^{n} \mathrm{C}_{n}^{n} x_{2}=n !, \\
x_{n+3}-\mathrm{C}_{n}^{1} x_{n+2}+\cdots+(-1)^{n} \mathrm{C}_{n}^{n} x_{3}=n ! .
\end{gathered}
$$

对 $S-\lambda \cdot(1)-\mu \cdot(2)-\varphi \cdot$ (3) 用 Lagrange 乘数法, 得

$$
2 x_{j}=\lambda(-1)^{n+1-j} \mathrm{C}_{n}^{n+1-j}+\mu(-1)^{n+2-j} \mathrm{C}_{n}^{n+2-j}+\varphi(-1)^{n+3-j} \mathrm{C}_{n}^{n+3-j},
$$

其中, $j=1,2, \cdots, n+3$. 再返代回 (1), (2), (3) 有

$$
\left\{\begin{array}{r}
\mathrm{C}_{2 n}^{n} \lambda-\mathrm{C}_{2 n}^{n-1} \mu+\mathrm{C}_{2 n}^{n-2} \varphi=2 n ! \\
-\mathrm{C}_{2 n}^{n-1} \lambda+\mathrm{C}_{2 n}^{n} \mu-\mathrm{C}_{2 n}^{n-1} \varphi=2 n ! \\
\mathrm{C}_{2 n}^{n-2} \lambda-\mathrm{C}_{2 n}^{n-1} \mu+\mathrm{C}_{2 n}^{n} \varphi=2 n !
\end{array}\right.
$$

求解得到

$$
\lambda=\varphi, \mu=\varphi \cdot \frac{2 n+2}{n+2}
$$

其中

$$
\lambda=\frac{2 n ! \mathrm{C}_{n+2}^{2}}{\mathrm{C}_{2 n}^{n}}=\frac{(n+2) !}{\mathrm{C}_{2 n}^{n}}
$$

$$
\begin{aligned}
4 S & =\mathrm{C}_{2 n}^{n}\left(\lambda^{2}+\mu^{2}+\varphi^{2}\right)-2 \mathrm{C}_{2 n}^{n-1}(\lambda \mu+\mu \varphi)+2 \mathrm{C}_{2 n}^{n-2} \lambda \varphi \\
& =\lambda^{2}\left\{\frac{(2 n) !}{n ! \cdot n !}\left[\left(\frac{2 n+2^{2}}{n+2}\right)+2\right]\right\}-4 \mathrm{C}_{2 n}^{n-1} \frac{2 n+2}{n+2} \lambda^{2}+2 \mathrm{C}_{2 n}^{n-2} \lambda^{2} \\
& =\lambda^{2}\left[\frac{(2 n) !}{n !(n+2) !(n+2)} \cdot(8 n+12)\right],
\end{aligned}
$$

故

$$
S_{\min }=\frac{[(n+2) !]^{2}}{4\left(\mathrm{C}_{2 n}^{n}\right)^{2}} \cdot \frac{(2 n) !(n+1)(8 n+12)}{[(n+2) !]^{2}}=\frac{(2 n) !(n+1)(2 n+3)}{\left(\mathrm{C}_{2 n}^{n}\right)^{2}} .
$$

## 解 2 (高继扬)

由 $n$ 次多项式的 $n$ 阶差分为最高次项系数 $\times n$ ! (可用归纳法证明), 有

$$
\begin{aligned}
& \mathrm{C}_{n}^{0} p(1)-\mathrm{C}_{n}^{1} p(2)+\mathrm{C}_{n}^{2} p(3)-\cdots+(-1)^{n} \mathrm{C}_{n}^{n} p(n+1)=n !, \\
& \mathrm{C}_{n}^{0} p(2)-\mathrm{C}_{n}^{1} p(3)+\mathrm{C}_{n}^{2} p(4)-\cdots+(-1)^{n} \mathrm{C}_{n}^{n} p(n+2)=n !, \\
& \mathrm{C}_{n}^{0} p(3)-\mathrm{C}_{n}^{1} p(4)+\mathrm{C}_{n}^{2} p(5)-\cdots+(-1)^{n} \mathrm{C}_{n}^{n} p(n+3)=n !,
\end{aligned}
$$

则 $(1) \cdot(n+2)+(2) \cdot(2 n+2)+(3) \cdot(n+2)$ 便得

$$
\sum_{i=0}^{n+2}\left((n+2) \mathrm{C}_{n}^{i-2}-(2 n+2) \mathrm{C}_{n}^{i-1}+(n+2) \mathrm{C}_{n}^{i}\right) p(i+1)(-1)^{i}=(4 n+6) \cdot(n !)
$$

记

$$
\begin{gathered}
A=\sum_{i=0}^{n+2}\left((n+2) \mathrm{C}_{n}^{i-2}-(2 n+2) \mathrm{C}_{n}^{i-1}+(n+2) \mathrm{C}_{n}^{i}\right)^{2} \\
B=\sum_{i=0}^{n+2}\left((n+2) \mathrm{C}_{n}^{i-2}-(2 n+2) \mathrm{C}_{n}^{i-1}+(n+2) \mathrm{C}_{n}^{i}\right) p(i+1)(-1)^{i}
\end{gathered}
$$

由 Cauchy 不等式可得

$$
A \cdot\left(\sum_{i=0}^{n+2}|p(i+1)|^{2}\right) \geq B^{2}=(4 n+6)^{2} \cdot(n !)^{2} .
$$

而

$$
\begin{aligned}
A= & \sum_{i=0}^{n+2}\left((n+2) \mathrm{C}_{n}^{i-2}-(2 n+2) \mathrm{C}_{n}^{i-1}+(n+2) \mathrm{C}_{n}^{i}\right)^{2} \\
= & \left(2(n+2)^{2}+(2 n+2)^{2}\right) \sum_{i=0}^{n}\left(\mathrm{C}_{n}^{i}\right)^{2}+2(n+2)^{2} \sum_{i=0}^{n} \mathrm{C}_{n}^{i} \mathrm{C}_{n}^{i+2} \\
& -4(n+2)(2 n+2) \sum_{i=0}^{n} \mathrm{C}_{n}^{i} \mathrm{C}_{n}^{i+1}
\end{aligned}
$$

$$
\begin{aligned}
& =\left(2(n+2)^{2}+(2 n+2)^{2}\right) \mathrm{C}_{2 n}^{n}+2(n+2)^{2} \mathrm{C}_{2 n}^{n-2}-4(n+2)(2 n+2) \mathrm{C}_{2 n}^{n-1} \\
& =2 \mathrm{C}_{2 n}^{n} \cdot \frac{4 n+6}{n+1}
\end{aligned}
$$

故

$$
\sum_{i=0}^{n+2}|p(i+1)|^{2} \geq \frac{(4 n+6)^{2} \cdot(n !)^{2}}{A}=\frac{(2 n+3)(n+1)(n !)^{2}}{\mathrm{C}_{2 n}^{n}}
$$

当 $i=1,2, \cdots, n+3$, 时, 取

$$
\begin{aligned}
p(i)= & (-1)^{i+1} \frac{n !}{(n+2) \mathrm{C}_{2 n}^{n}-(2 n+2) \mathrm{C}_{2 n}^{n-1}+(n+2) \mathrm{C}_{2 n}^{n-2}} \\
& \cdot\left((n+2) \mathrm{C}_{n}^{i-3}-(2 n+2) \mathrm{C}_{n}^{i-2}+(n+2) \mathrm{C}_{n}^{i-1}\right) \\
= & (-1)^{i+1} \frac{n !}{2 \mathrm{C}_{2 n}^{n}}\left((n+2) \mathrm{C}_{n}^{i-3}-(2 n+2) \mathrm{C}_{n}^{i-2}+(n+2) \mathrm{C}_{n}^{i-1}\right) .
\end{aligned}
$$

此时的 $p(i)$ 满足 (1)(2)(3), 且满足 (4) 的取等条件. 其中

因此, 所求最小值为 $\frac{(2 n+3)(n+1)(n !)^{2}}{\mathrm{C}_{2 n}^{n}}$.

评注 本题有两个入手点. 第一个是从多项式的根入手, 将待求式理解为 $1,2, \cdots, n+3$ 到各根距离之积的平方和, 这可以得出 $P(x)$ 的每个根均为实数; 第二个是利用多项式的差分得到三个约束式, 在这三个条件下, 求一个式子的最值. 结合以上两点, 就可以脱去多项式的外衣, 将原题化作我们所熟悉的带条件的实数范畴内的不等式, 而且是二次型. 接着, 无论是利用 Lagrange 乘数法, 还是待定系数柯西都可以解决本题. 当然, 本题中计算过程较复杂, 涉及到很多组合数之间的运算, 非常考验一个学生的代数基本功, 是一道偏难的好题.

题 4. 试求所有的正整数 $n \geq 2$, 使得存在整数 $x_{1}, x_{2}, \cdots, x_{n-1}$ 满足: 如果 $0<i, j<n, i \neq j$, 且 $n \mid(2 i+j)$, 那么 $x_{i}<x_{j}$.

## 解 (黄一山)

(1) 首先证明当正整数 $n$ 为 $2^{k}(k \geq 1)$ 或 $3 \cdot 2^{k}(k \geq 1)$ 时满足题意.

令 $x_{i}=\nu_{2}(i)$, 其中 $\nu_{2}(i)$ 表示正整数 $i$ 所含有的 2 的幂次. 因为对任意的 $0<i \neq j<n$, 满足 $n \mid(2 i+j)$, 则 $\nu_{2}(2 i+j) \geq \nu_{2}(n)=k$, 而由题有 $\nu_{2}(2 i) \leq \nu_{2}(2 n)=k+1, \nu_{2}(j) \leq \nu_{2}(n)=k$. 考虑如下两种情形:

i) 若 $\nu_{2}(2 i) \leq \nu_{2}(j)$, 有

$$
x_{j}=\nu_{2}(j)>\nu_{2}(i)=x_{i},
$$

符合题意.

ii) 若 $\nu_{2}(2 i)>\nu_{2}(j)$, 记 $i=2^{k_{1}} l_{1}, j=2^{k_{2}} l_{2}$, 其中 $l_{1}, l_{2}, k_{1}, k_{2}$ 均为正整数,
$2 \nmid l_{1}, l_{2}$ 且 $k_{1} \geq k_{2}$. 有

$$
\begin{aligned}
n \mid 2 i+j & \Leftrightarrow \nu_{2}(n) \leq \nu_{2}\left(2^{k_{1}+1} l_{1}+2^{k_{2}} l_{2}\right) \\
& \Leftrightarrow k-k_{2} \leq \nu_{2}\left(2^{k_{1}+1-k_{2}} l_{1}+l_{2}\right)
\end{aligned}
$$

此时 $k_{1}+1-k_{2} \geq 1$, 故 $2^{k_{1}+1-k_{2}} l_{1}$ 为偶数. 而 $l_{2}$ 为奇数, 故 $\nu_{2}\left(2^{k_{1}+1-k_{2}} l_{1}+l_{2}\right)=0$.因此 $k=k_{2}$. 又有 $\nu_{2}(j)<\nu_{2}(2 i) \leq k+1$, 故 $k_{1}=k$. 而由题有 $i \neq j$, 因此只有 $i=j=2^{k}$. 故不存在 $\nu_{2}(2 i)>\nu_{2}(j)$ 的情形.

综上, 当正整数 $n$ 为 $2^{k}(k \geq 1)$ 或 $3 \cdot 2^{k}(k \geq 1)$ 时, 令 $x_{i}=\nu_{2}(i)$ 即满足题意.

(2) 下面用反证法证明 $n$ 为其他正整数时均不满足题意.

假设 $n=2^{k} l$ 满足题意, 其中正整数 $l \geq 5$, 且 $2 \nmid l$. 令 $i_{0}=1, i_{1}=$ $(-2), \cdots, i_{l}=(-2)^{l}$, 则 $i_{l-1} \equiv i_{0}(\bmod l)$.

设 $j_{m}(0 \leq m \leq l-1)$ 为 $i_{m}$ 模 $l$ 的最小正剩余, 则

$$
j_{m+1} \equiv(-2) j_{m} \quad(\bmod l)
$$

即 $l \mid j_{m+1}+2 j_{m}$. 由题意有

$$
x_{2^{k} j_{0}}<x_{2^{k} j_{1}}<\cdots<x_{2^{k} j_{l-1}}=x_{2^{k} j_{0}},
$$

矛盾! 故不存在满足条件的正整数 $x_{1}, x_{2}, \cdots, x_{n-1}$.

评注 考虑到欧拉定理有当 $2 \nmid l$ 时, $(-2)^{l-1}=2^{l-1} \equiv 1(\bmod l)$. 同时构造 $\left\{j_{n}\right\}(n=0,1, \cdots, n)$ 为 $\left\{i_{n}\right\}(n=0,1, \cdots, n)$ 模 $l$ 的最小正剩余恰好可以得到类似题目条件的结构, 进而可以得到矛盾证明 $2^{k} \cdot l$ 的形式对 $2 \nmid l, l \geq 5$ 时均不存在符合题意的解.

题 5. 设 $D=\{0,1,2, \cdots, 9\}$ 为十进制数字集合, $R \subset D \times D$ 为有序数对的集合. 称无限数字序列 $\left(a_{1}, a_{2}, a_{3}, \cdots\right)$ 与 $R$ 是一致的, 若对每个正整数 $j$ 有 $\left(a_{j}, a_{j+1}\right) \in R$. 试求最小的正整数 $k$ 满足: 如果任意的 $R \subset D \times D$ 与至少 $k$ 个不同的数字序列是一致的, 那么 $R$ 与无限多个数字序列是一致的.

## 解 (陈泽坤)

设 $D_{n}=\{1,2, \cdots, n\}, n \in \mathbb{N}^{+}$. 我们用归纳法证明:设 $R \subset D_{n} \times D_{n}$ 为有序数对的集合. 称无限数列 $\left(a_{1}, a_{2}, a_{3}, \cdots\right)$ 与 $R$ 一致, 若对每个正整数 $j$ 有 $\left(a_{j}, a_{j+1}\right) \in R$. 如果 $R$ 与有限个无限数列一致, 则 $R$ 至多与 $2^{n-1}$ 个无限数列是一致的.

$n=1$ 时显然成立.
假设 $n=k$ 时结论成立. 当 $n=k+1$ 时我们用一个带环的有向图 $G=(V, E)$ 来表示 $R$, 即若 $(i, j) \in R$, 则在 $G$ 中从 $i$ 向 $j$ 连一条有向边. 我们称一个无限数列与 $G$ 一致, 若它与 $R$ 一致.

(1) 若 $G$ 中无圈, 则 $G$ 不可能与任何一个无限数列一致.

(2) 若 $G$ 中有圈, 则分如下两种情况进行讨论.

i) 若存在 $v_{0} \in V$, 其入度为零.

考虑去掉 $v_{0}$ 及与之相连的边, 设得到的图为 $G^{\prime}$. 对任意一个与 $G$ 一致的序列 $\pi$. 若 $v_{0} \in \pi$, 则 $v_{0}$ 一定仅在第一位出现一次. 设 $\pi$ 去掉 $v_{0}$ 得到 $\pi^{\prime}$, 则 $\pi^{\prime}$ 与 $G^{\prime}$一致. 因为 $G^{\prime}$ 为一个 $k$ 阶图, 则由归纳假设知, 与 $G^{\prime}$ 一致的序列至多 $2^{k-1}$ 个. 故与 $G$ 一致的序列至多有 $2^{k}$ 个.

ii) 若对任意的 $v_{0} \in V$, 其入度均不为零.

如果 $G$ 中有两个相交的圈, 则 $G$ 与无穷多个无穷数列一致, 矛盾! 若 $G$ 中存在一条从一个圈到另一个圈的路, 则 $G$ 也与无穷多个无穷数列一致, 矛盾!故 $G$ 由一些两两不相交的圈或一个圈构成. 此时, 与 $G$ 一致的无穷数列由它的第一项唯一确定, 故与 $G$ 一致的无穷数列至多有 $k+1$ 个. 而 $k+1 \leq 2^{k}$.

故由 (1) 和 (2) 便知, $n=k+1$ 时结论也成立.

下面说明等号可以取到. 令 $E=\{\overrightarrow{i j} \mid 1 \leq i<j \leq n\} \cup\{\overrightarrow{n n}\}$, 则对 $D_{n}-\{n\}$的任一个子集 $\left\{a_{1}, a_{2}, \cdots, a_{t}\right\}, 1 \leq a_{1}<a_{2}<\cdots<a_{t} \leq n-1$, 存在唯一的无穷数列 $\left(a_{1}, a_{2}, \cdots, a_{t}, n, n, \cdots\right)$ 与之对应. 故此时恰有 $2^{n-1}$ 个无穷数列与之一致, 因此等号可以取到.

取 $n=10$, 便知 $k$ 的最小值为 $2^{9}+1=513$.

评注 本题巧妙的将原问题转化为一个图论问题, 将无穷数列与圈联系在一起, 使得问题变得直观. 首先, 将问题转化为: 若 $G$ 与有限个无穷数列一致, 则 $G$至多与多少个无限数列一致. 其次, 考虑到无穷数列的存在可以推出 $G$ 中必定存在圈, 而当存在两个或更多圈时, 除非任意两个圈不相交也不相连, 否则都有 $G$ 与无穷多个无限数列一致的结论. 该情形下与 $G$ 一致的无穷数列由其第一项完全确定. 而当仅存在一个圈时, 所有无穷数列的有限项后都是圈内的点. 此时,圈经过的点越少在圈外的点组合就越多, 与 $G$ 一致的无穷数列也越多, 由此不难得到结论.

题 6. 设 $n$ 为正整数. 我们有 $n$ 个箱子, 并且每个箱子有非负整数个鹅卵石.定义一次操作为: 从一个箱子中取两个鹅卵石, 然后丢掉其中一个我岛石, 并把
另一个我鸟卯石放到其他的任意一个箱子里. 我们称鹅卵石的初始状态是可解的,如果可以经过有限次(可以为 0 次)操作, 使得所有的箱子非空. 试求鹅卵石的所有不可解初始状态, 但是如果给其中任意一个箱子额外添加一个我岛石可以变成可解的初始状态.

解 (高继扬) 设初始状态时, $n$ 个箱子的我岛石数分别为 $x_{1}, x_{2}, \cdots, x_{n}$. 将第 $i(1 \leq i \leq n)$ 个箱子赋值 $\left[\frac{x_{i}-1}{2}\right]$. 令

$$
N=\sum_{i=1}^{n}\left[\frac{x_{i}-1}{2}\right], S=\sum_{i=1}^{n} x_{i}
$$

并设 $x_{1}, x_{2}, \cdots, x_{n}$ 中有 $J$ 个奇数, 则

$$
N=\frac{S-n}{2}-\frac{n-J}{2}=\frac{S}{2}+\frac{J}{2}-n .
$$

由题意知经过一次操作后, $S$ 变为 $S-1, J$ 变为 $J+1$ 或 $J-1$, 故 $N$ 不变或变为 $N-1$. 假设初始状态为可解的, 则最终每个箱子赋值大于或等于 0 , 故此时 $N \geq 0$, 即可解的初始状态满足 $N \geq 0$.

下面证明: 若 $N \geq 0$, 则初始状态为可解的.

若不然, 假设空箱子的数量最小, 且有空箱子, 其赋值为 -1 . 因为此时有 $N \geq 0$, 则必有一个箱子的赋值 $\geq 1$, 故其至少有 3 个我卵石, 将其中两个取出,放一个到刚才的空箱子中, 另一个丢掉, 则 $S$ 变为 $S-1, J$ 变为 $J+1$. 故 $N$ 不变, 仍有 $N \geq 0$, 但空箱子数量减少了. 矛盾!

综上, 一个初始状态是可解的当且仅当 $N \geq 0$.

由上述可知, 所要求的不可解初始状态要满足: $N<0$, 但任添加一个鹅卵石, $N$ 要变为 $N+1 \geq 0$, 故此时 $N=-1$. 要将 $N$ 变为 $N+1$, 由 (1) 知, $S$ 变为 $S+1$, 同时 $J$ 也变为 $J+1$. 考虑到题目要求是对所求的不可解初始状态的任意一个箱子添加我岛卵石都变为可解的, 因此 $J=0$, 故 $\frac{S}{2}-n=-1$. 即 $S=2 n-2$.

综上, 所要求的不可解初始状态为 $n$ 个箱子的我卵石总数为 $2 n-2$, 且每个箱子中的鹅卵石个数均为偶数.

评注 考虑到要使一个空箱子非空只需存在另一个鹅卵石数目 $\geq 3$ 的箱子,进行一次操作后两个箱子均为非空. 事实上对一个非空箱子赋值 $k$, 表示该箱子可以至多取出 $2 k$ 个鹅卯石仍保持非空, 即至多进行 $k$ 次取出操作. 同时对空箱子赋值 -1 表示需要进行一次操作使得其非空. 两者结合即得到初始状态是可解的当且仅当 $N \geq 0$.

