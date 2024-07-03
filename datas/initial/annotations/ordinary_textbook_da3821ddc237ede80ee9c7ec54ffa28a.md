# 调整法在不等式中的非常规应用 

解尧平 ${ }^{1}$ 杜航 ${ }^{2}$

(1. 天津市实验中学, 300074；2. 成都七中, 610041)

调整法是数学竞赛中的一个重要方法, 其思想为将一般的问题化归为某些结构明确的特殊情形. 在不等式中, 调整法更是解决问题的利器. 我们熟悉的调整法包括冻结变量, 求导等方法, 而本文将给出一些应用其他非常规方法进行调整, 从而解决问题的例子. 在例子的分析中, 我们侧重于调整的思考过程以及书写方法, 而一些无实质难度的计算过程则从略处理.

例 1 设正奇数 $n \geq 3, a_{1}, a_{2}, \cdots, a_{n}$ 是 $n$ 个非负实数, 满足 $a_{1}+a_{2}+\cdots+$ $a_{n}=\frac{n}{2}$. 若记 $a_{n+1}=a_{1}$, 求证:

$$
\prod_{i=1}^{n}\left|a_{i}-a_{i+1}\right| \leq \frac{3 \sqrt{3}}{16}
$$

分析 对于一般的 $a_{1}, a_{2}, \cdots, a_{n}$, 上述表达式并不好处理, 同时条件中 $n$ 是奇数也显得比较奇怪. 因此我们先尝试将 $a_{1}, a_{2}, \cdots, a_{n}$ 之间的结构关系描述得清楚一些.

证明 首先我们可以不妨设不存在 $a_{i}=a_{i+1}$ 的情况. 下面我们依次做如下几步调整:

引理 1 定义满足 $a_{i}<a_{i-1}$ 且 $a_{i}<a_{i+1}$ 的数 $a_{i}$ 为小数 (其中角标模 $n$ 理解), 则可不妨设 $a_{1}, \cdots, a_{n}$ 中的小数均为 0 .

证明 若有非零小数 $a_{i}$, 我们将 $a_{i}$ 调整为 0 , 其余 $n-1$ 个数等比例放大一些, 使全体和仍为 $\frac{n}{2}$, 则原表达式值不减. 注意到此调整过程中, 非零小数个数严格减少, 因此最终可设所有小数均为 0 . 引理证毕!

引理 2 可以不妨设 $a_{1}, \cdots, a_{n}$ 中不存在长为 4 的单调子列, 即不存在 $i$ 使得 $a_{i}>a_{i+1}>a_{i+2}>a_{i+3}$ 或者 $a_{i}<a_{i+1}<a_{i+2}<a_{i+3}$, 其中角标模 $n$ 理解.

收稿日期: 2019-06-27.
证明 若不然, 不妨设 $a_{1}>a_{2}>a_{3}>a_{4}$, 将 $a_{2}, a_{3}$ 调换位置, 其余变量不变,原表达式不减. 注意每调整一次, 长为 4 单调子列个数严格递减, 因此最终可设不存在长为 4 单调子列. 引理证毕!

有了上面两个引理, 我们已经能较为清楚地刻画 $a_{1}, \cdots, a_{n}$ 的结构了. 引理 2 告诉我们, 每连续 4 个数之中就一定会有一个小数, 那么如果我们把两个相邻小数之间的数 (包括这两个小数) 视为一组的话, 每组就只可能有 3 个, 4 个或者 5 个数, 且两端的数都是 0 (引理 1 ).

稍加分析可以得到, 每组数必然形如 $(0, a, 0),(0, a, b, 0),(0, a, b, c, 0)$ 之一 (其中最后一种情况满足 $b \geq a, b \geq c$ ). 带入原表达式可以发现, 组与组之间是互不影响的, 因此我们关注每个组本身就可以了. 这相当于只要做 $n=2,3,4$ 的情况, 无疑是极大的化简了问题.

现在我们来研究每组自身对原表达式的贡献. 考虑任意一组, 记此组中所有数之和为 $s$.

对于第一种情况, $s=a$, 此组对原表达式贡献为

$$
a^{2}=s^{2} \text {. }
$$

对于第二种情况, $s=a+b$, 此组对原表达式贡献为 $a b|a-b|$. 若记 $t=|a-b|$, 则由于

$$
a b|a-b|=\frac{s^{2}-t^{2}}{4} \cdot t=\frac{\sqrt{2 t^{2}\left(s^{2}-t^{2}\right)\left(s^{2}-t^{2}\right)}}{4 \sqrt{2}} \leq \frac{\sqrt{\left(\frac{2 s^{2}}{3}\right)^{3}}}{4 \sqrt{2}}=\frac{s^{3}}{6 \sqrt{3}},
$$

当且仅当 $3(a-b)^{2}=(a+b)^{2}$ 时等号成立, 可知当 $s$ 固定时, 此组对原表达式贡献最大值为 $\frac{s^{3}}{6 \sqrt{3}}$.

对于第三种情况, 其贡献为 $a(b-a) c(b-c)$, 我们也可以求其精确最大值,但事实上,

$$
a(b-a) c(b-c) \leq \frac{(a+b-a)^{2}}{4} \cdot \frac{(c+b-c)^{2}}{4}=\frac{b^{4}}{16} \leq \frac{s^{4}}{16}
$$

由 (1) 及 (3) 我们有

引理 3 可以不妨设不存在大小为 5 的组.

证明 若存在大小为 5 的组 $(0, a, b, c, 0)$, 我们将其调整为 $\left(0, \frac{s}{2}, 0, \frac{s}{2}, 0\right)$, 其中 $s=a+b+c$, 则原表达式不减. 注意此调整过程中, 大小为 5 的组数目严格减少, 因此最终可设不存在大小为 5 的组. 引理证毕!

现在我们终于可以解决原问题了. 由上述引理知, 可设 $\left(a_{1}, \cdots, a_{n}\right)$ 被分为 $k$ 个大小为 3 的组以及 $l$ 个大小为 4 的组, 则 $2 k+3 l=n$ (每个 0 算了两次). 由
$n$ 是奇数, 立得 $l \geq 1$. 再记各组内数字总和为 $s_{1}, \cdots, s_{k}, t_{1}, \cdots, t_{l}$, 则

$$
\sum_{i=1}^{k} s_{i}+\sum_{j=1}^{l} t_{j}=\sum_{i=1}^{n} a_{i}=\frac{n}{2}
$$

且原表达式不超过

$$
\begin{aligned}
s_{1}^{2} \cdots s_{k}^{2} \frac{t_{1}^{3}}{6 \sqrt{3}} \cdots \frac{t_{l}^{3}}{6 \sqrt{3}} & \leq\left(\frac{s_{1}+\cdots s_{k}}{k}\right)^{2 k} \cdot\left(\frac{t_{1}+\cdots t_{l}}{l}\right)^{3 l} \cdot\left(\frac{1}{6 \sqrt{3}}\right)^{l} \\
& =\left(\frac{s_{1}+\cdots s_{k}}{2 k}\right)^{2 k} \cdot\left(\frac{t_{1}+\cdots t_{l}}{3 l}\right)^{3 l} \cdot\left(\frac{1}{6 \sqrt{3}}\right)^{l} \cdot 2^{2 k} 3^{3 l} \\
& \leq\left(\frac{s_{1}+\cdots s_{k}+t_{1}+\cdots t_{l}}{2 k+3 l}\right)^{2 k+3 l} \cdot\left(\frac{1}{6 \sqrt{3}}\right)^{l} \cdot 2^{2 k} 3^{3 l} \\
& =\left(\frac{3 \sqrt{3}}{16}\right)^{l} \leq \frac{3 \sqrt{3}}{16} .
\end{aligned}
$$

故原不等式得证.

评注 本题的关键即为通过调整将 $a_{1}, a_{2}, \cdots, a_{n}$ 分为若干个较小的局部, 从而使问题变得明朗. 另外由证明过程不难得到此常数 $\frac{3 \sqrt{3}}{16}$ 为最佳的, 例如一个取等条件为 $\left(a_{1}, a_{2}, \cdots, a_{n}\right)=\left(0, \frac{3-\sqrt{3}}{4}, \frac{3+\sqrt{3}}{4}, 0,1, \cdots, 0,1\right)$.

例 2 给定整数 $n \geq 2$, 以及正实数 $a<b$. 设实数 $x_{1}, x_{2}, \cdots, x_{n} \in[a, b]$, 求

的最大值.

$$
\frac{\frac{x_{1}^{2}}{x_{2}}+\frac{x_{2}^{2}}{x_{3}}+\cdots+\frac{x_{n-1}^{2}}{x_{n}}+\frac{x_{n}^{2}}{x_{1}}}{x_{1}+x_{2}+\cdots+x_{n-1}+x_{n}}
$$

(2016 年中国数学奥林匹克)

分析 首先我们可以尝试猜答案: 不难猜到, 以上表达式取最大值时,每个 $x_{i} \in\{a, b\}$, 且 $a, b$ 应尽量交替出现. 因此基本可以断定, 当 $n$ 为偶数时， $\left(x_{1}, \cdots, x_{n}\right)=(a, b, \cdots, a, b)$ 时取最大值; 而 $n$ 为奇数时, $\left(x_{1}, \cdots, x_{n}\right)=$ $(a, b, \cdots, a, b, a)$ 与 $(b, a, \cdots, b, a, b)$ 之一时取最大值, 再稍加计算便可以猜出答案. 而证明思路自然便是想办法通过调整使 $\left(x_{1}, \cdots, x_{n}\right)$ 往上述结构靠拢.

证明 记

$$
\lambda(n)= \begin{cases}\frac{a^{2}-a b+b^{2}}{a b}, & \text { 若 } n \text { 为偶数; } \\ \frac{\frac{n-1}{2}\left(\frac{b^{2}}{a}+\frac{a^{2}}{b}\right)+a}{\frac{n+1}{2} a+\frac{n-1}{2} b}, & \text { 若 } n \text { 为奇数. }\end{cases}
$$

我们取

$$
\left(x_{1}, \cdots, x_{n}\right)= \begin{cases}(a, b, \cdots, a, b), & \text { 若 } n \text { 为偶数; } \\ (b, a, \cdots, b, a, b), & \text { 若 } n \text { 为奇数. }\end{cases}
$$

即可得到所求最大值不小于 $\lambda(n)$.

下证

$$
\frac{x_{1}^{2}}{x_{2}}+\frac{x_{2}^{2}}{x_{3}}+\cdots+\frac{x_{n-1}^{2}}{x_{n}}+\frac{x_{n}^{2}}{x_{1}}-\lambda(n)\left(x_{1}+x_{2}+\cdots+x_{n-1}+x_{n}\right) \leq 0 .
$$

引理 1 可以不妨设 $x_{i} \in\{a, b\}, \forall 1 \leq i \leq n$.

证明 将 $x_{2}, \cdots, x_{n}$ 视为常数, 则 (4) 式左边为关于 $x_{1}$ 的函数

$$
f\left(x_{1}\right)=\frac{x_{1}^{2}}{x_{2}}+\frac{x_{n}^{2}}{x_{1}}-\lambda(n) x_{1}+C
$$

其中 $C$ 为常数. 对其求二阶导可得 $f^{\prime \prime}\left(x_{1}\right)=\frac{2}{x_{2}}+\frac{x_{n}^{2}}{2 x_{1}^{3}}>0$, 从而 $f^{\prime}\left(x_{1}\right)$ 在区间 $[a, b]$ 上单调增, 因此在 $[a, b]$ 上至多只有一个零点. 从而 $f(x)$ 在区间 $[a, b]$ 上单调增或单调减或先减后增, 不论怎样, 其最大值都在端点取到. 因此可将 $x_{1}$ 调到端点. 同理可依次将 $x_{2}, \cdots, x_{n}$ 均调到端点. 引理证毕!

由引理 1 , 我们只需要考虑有限种情况, 因此可取一组 $x_{1}, \cdots, x_{n} \in\{a, b\}$,使得 (4) 式左边最大. 设 $x_{1}, \cdots, x_{n}$ 中有 $m$ 个 $a, n-m$ 个 $b$, 并设 $\left(x_{i}, x_{i+1}\right)(1 \leq$ $\left.i \leq n, x_{n+1}=x_{1}\right)$ 中有 $x$ 对 $(a, b), y$ 对 $(b, a), z$ 对 $(a, a), w$ 对 $(b, b)$. 那么 (4) 式左边可以写成

$$
x \cdot \frac{a^{2}}{b}+y \cdot \frac{b^{2}}{a}+z a+w b-\lambda(n)(m a+(n-m) b) .
$$

我们希望进一步挖掘这些变量之间的关系. 为了可控性, 我们先固定 $m$ 的值, 即固定组成 $x_{1}, x_{2}, \cdots, x_{n}$ 的“零件”, 而去考虑这些零件怎样构成我们的序列才能满足取最值条件. 一个基本出发点为: 取最大值时 $a, b$ 交错应尽量多. 利用这个观点, 我们建立如下引理 2：

引理 2 称满足 $x_{i}=x_{i+1}$ 的对 $\left(x_{i}, x_{i+1}\right)$ 为好对. 则至多出现一种好对, 即 $(a, a),(b, b)$ 不能都出现.

证明 将所有好对标记出来, 分别染上红色 (代表 $(a, a)$ 对)与蓝色 (代表 $(b, b)$ 对). 若两种好对均存在, 则必然有相邻的两个好对一红一蓝. 不妨设其中红对为 $\left(x_{1}, x_{2}\right)$, 蓝对为 $\left(x_{t}, x_{t+1}\right)$, 则 $x_{1}, x_{2}, \cdots, x_{t}, x_{t+1}$ 的分布情况为

$$
x_{1}=a, a, b, a, b, a, \cdots, b, a, b, b=x_{t+1} \text {, }
$$

由此可知 $2 \nmid t$. 此时我们做一个调整使得 “ $a, b$ 交错” 的对变多, 调整如下:

$$
x_{i}^{\prime}= \begin{cases}x_{t+2-i}, & \text { 若 } 2 \leq i \leq t \\ x_{i}, & \text { 否则 }\end{cases}
$$

相当于将 $x_{2}$ 至 $x_{t}$ 首尾翻转一下, 其余不变. 则稍加计算可知, 此调整后 $m$ 不变,
$x, y$ 分别增加 1 , 而 $z, w$ 分别减少 1 , 从而 (4) 式左边的改变量

$$
\Delta=\frac{b^{2}}{a}+\frac{a^{2}}{b}-a-b>0
$$

这与我们的取法矛盾. 引理证毕!

引理 2 说明, 如果我们将这组 $x_{1}, \cdots, x_{n}$ 放在一个圆周上, 并把连续一段相同字母的段称为一个同类段, 那么至多有一种同类段. 称一个同类段是一个极长同类段, 是指它的两端的字母都与此段字母不同.

引理 3 可以假设至多只有一个极长同类段.

证明 证明的想法是, 如果有多于一个极长同类段, 则可通过调整使得 (4) 式左边不减, 而极长同类段个数减少. 若有多于一个极长同类段, 由于它们由同一个字母组成 (引理 2), 我们不妨设由 $a$ 组成 (由 $b$ 组成完全类似), 再不妨设 $x_{n}, x_{1}$ 是某个极长同类段的末端, 则存在 $3 \leq i<j \leq n-2$ 使得 $x_{n}, x_{1}, \cdots, x_{j+1}$的分布如下:

$$
\left(x_{n}=\right) a,\left(x_{1}=\right) a, b, a, b, a, \cdots, b, a, b,\left(x_{i}=\right) a, a, \cdots, a,\left(x_{j}=\right) a,\left(x_{j+1}=\right) b .
$$

由上可知 $2 \nmid i$. 现在做一个和刚才类似的调整:

$$
x_{i}^{\prime}= \begin{cases}x_{j+1-i}, & \text { 若 } 1 \leq i \leq j \\ x_{i}, & \text { 否则 }\end{cases}
$$

即将 $x_{1}$ 至 $x_{j}$ 首尾翻转而其他变量不变. 稍加计算可知 (4) 式左边并无改变, 但此操作将 $x_{i}, x_{j}$ 之间的极长同类段合并到了 $x_{1}$ 所在的极长同类段之中, 从而使极长同类段个数减少. 因此引理 3 成立. 引理证毕!

由引理 3 , 我们可以得到 $x_{1}, \cdots, x_{n}$ 的清晰结构: 某一段均等于某个字母,而其它项 $a, b$ 交替. 至此本题已无实质难度, 略加计算便可证明 (4) 式, 此处从略. 因此 $\lambda(n)$ 即为所求最大值.

评注 在 (4) 式证明过程中, 第一步将 $x_{i}$ 调成端点是常规的. 而后面的调整过程则用到了二色链的思想, 颇具组合味道. 本题也有更为简洁的的做法, 但是笔者认为上述做法较为自然。

例 3 设正整数 $n \geq 3, n+1$ 项数列 $\left\{a_{k}\right\}$ 满足: $a_{0}=0, a_{i} \geq 0,1 \leq i \leq n$,且 $\frac{a_{i-1}+a_{i+1}}{2} \leq a_{i}, 1 \leq i \leq n-1$. 证明: 存在常数 $c$, 使得对任何 $n$ 以及满足条件的数列 $\left\{a_{k}\right\}$, 均有

$$
\left(\sum_{i=1}^{n} a_{i}\right)^{2} \geq \frac{3 n-c}{4} \sum_{i=1}^{n} a_{i}^{2}
$$

分析 所给条件是一个凹数列, 条件可化为 $a_{1} \geq a_{2}-a_{1} \geq \cdots \geq a_{n}-a_{n-1}$.因此, 若记 $a_{k}=\max \left\{a_{1}, \cdots, a_{n}\right\}$ (若有多个 $a_{k}$ 满足此性质, 则取 $k$ 尽量小), 则 $a_{1} \leq \cdots \leq a_{k}, a_{k} \geq \cdots \geq a_{n}$. 现在我们固定

$$
S_{1}=\sum_{i=1}^{k} a_{i}, S_{2}=\sum_{i=k}^{n} a_{i}
$$

以及 $a_{k}$ 的值, 并保持 $a_{k}=\max \left\{a_{1}, \cdots, a_{n}\right\}$ 这一性质不变, 考虑 $a_{1}, \cdots, a_{k-1}$ 以及 $a_{k+1}, \cdots, a_{n}$ 应当如何排布, 才能使 $\sum_{i=1}^{n} a_{i}^{2}$ 尽量大. 由优超不等式的思想, 在和一定的条件下, 为使平方和尽量大, 应使大的数尽量大, 小的数尽量小. 但同时又要符合非负凹数列的条件, 因此我们可以尝试将一般情形化归成如下的排法:前若干项构成递增等差数列, 中间若干项均等于 $a_{k}$, 而后面若干项又构成递减等差数列.

证明 我们先不加证明地给出两个凹数列性质, 这些性质均可类比凹函数性质得到.

引理 1 对任何 $1 \leq i \leq j \leq n-1$, 有

$$
a_{i}+a_{j} \geq a_{i-1}+a_{j+1}
$$

引理 2 对任何 $0 \leq i \leq m \leq j \leq n$, 有

$$
a_{m} \geq \frac{(j-m) a_{i}+(m-i) a_{j}}{j-i}
$$

设 $a_{k}, S_{1}, S_{2}$ 的定义同分析. 结合引理 1 , 通过配对不难证明

$$
k a_{k} \geq S_{1} \geq \frac{k+1}{2} a_{k}, \quad(n-k+1) a_{k} \geq S_{2} \geq \frac{n-k+1}{2} a_{k}
$$

故可取到最小正整数 $i(1 \leq i \leq k)$, 以及最大正整数 $j(k \leq j \leq n)$, 分别满足

$$
k a_{k}-\frac{i-1}{2} a_{k} \leq S_{1}, \frac{n+j+1}{2} a_{k}-k a_{k} \leq S_{2} .
$$

对于 $j \leq n-2$ 的情形. 我们令

$$
b_{m}= \begin{cases}K_{1} m, & 0 \leq m \leq i-1 \\ a_{k}, & i \leq m \leq j \\ K_{2}(n-m), & j+1 \leq m \leq n\end{cases}
$$

其中 $K_{1}=\frac{S_{1}-(k-i+1) a_{k}}{\frac{i(i-1)}{2}}, K_{2}=\frac{S_{2}-(j-k+1) a_{k}}{\frac{(n-j)(n-j-1)}{2}}$ (对 $i=1$ 的情形, 令 $K_{i}=0$ ). 由 $i, j$ 的选取可以验证 $\left\{b_{m}\right\}$ 的确符合题设条件, 且有

$$
\sum_{i=1}^{k} b_{i}=\sum_{i=1}^{k} a_{i}, \sum_{i=k}^{n} b_{i}=\sum_{i=k}^{n} a_{i}, a_{k}=\max _{1 \leq i \leq n}\left\{a_{i}\right\}=b_{k}=\max _{1 \leq i \leq n}\left\{b_{i}\right\}
$$

并且 $0=b_{0}<\cdots<b_{i-1}$ 构成等差数列, $b_{i}, \cdots, b_{j}$ 构成常数列, 而 $b_{j+1}>\cdots>$ $b_{n}=0$ 构成递减等差数列.

下面我们尝试证明 $\sum_{i=1}^{n} b_{i}^{2} \geq \sum_{i=1}^{n} a_{i}^{2}$. 注意到 $a_{k}=b_{k}$, 因此只要分别证明

$$
\sum_{i=1}^{k} b_{i}^{2} \geq \sum_{i=1}^{k} a_{i}^{2} \text { 以及 } \sum_{i=k}^{n} b_{i}^{2} \geq \sum_{i=k}^{n} a_{i}^{2}
$$

即可.

取最大的正整数 $l(1 \leq l \leq i-1)$ 使得 $b_{l}<a_{l}$ (若这样的 $l$ 不存在, 则必有 $\left.a_{m}=b_{m}, 1 \leq m \leq k\right)$, 下面我们证明： $b_{m}<a_{m}, \forall 1 \leq m \leq l$.

任取 $1 \leq m \leq l$, 由引理 2 知

$$
a_{m} \geq \frac{m a_{l}+(l-m) a_{0}}{l}=\frac{m a_{l}}{l}
$$

又由 $b_{0}, b_{1}, \cdots, b_{l}$ 成等差数列, 可知

$$
b_{m}=\frac{m b_{l}+(l-m) b_{0}}{l}=\frac{m b_{l}}{l} .
$$

因此由 $a_{l}>b_{l}$ 可知 $a_{m}>b_{m}, \forall 1 \leq m \leq l$.

再由 $l$ 最大性得, $b_{m} \geq a_{m}, \forall l+1 \leq m \leq k$. 这样我们便推出: 序列 $\left\{b_{k}, b_{k-1}, \cdots, b_{1}\right\}$ 优超序列 $\left\{a_{k}, a_{k-1}, \cdots, a_{1}\right\}$. 从而由 Karamata 不等式立得 $\sum_{i=1}^{k} b_{i}^{2} \geq \sum_{i=1}^{k} a_{i}^{2}$. 同理得另一个不等式. 因此在 $j \leq n-2$ 时, 我们成功将 $\left\{a_{1}, \cdots, a_{n}\right\}$ 调整成了所期望的结构.

对于 $j=n-1, n$ 的情形, 类似上面的方法, 可以将数列 $\left\{a_{m}\right\}$ 调整为 $0=b_{0}<\cdots<b_{i-1}$ 成等差数列, 而 $b_{i}=\cdots=b_{n-1} \geq b_{n}$ 的情形. 因此我们只需对这两种特殊情形证明结论即可. 我们可以证明, 这两种情形下均有

$$
\left(\sum_{i=1}^{n} a_{i}\right)^{2}-\frac{3 n-\frac{3 n}{2 n-1}}{4} \sum_{i=1}^{n} a_{i}^{2} \geq 0
$$

该不等式的证明几乎是纯计算问题了, 但我们还可以做一些简化, 例如我们可以将第一种情况再化归到 $a_{0}, \cdots, a_{i-1}, a_{i}$ 成等差数列, $a_{i}=\cdots=a_{j}$, $a_{j}, a_{j+1}, \cdots, a_{n}$ 也成等差数列的情形.

具体方法如下: 当 $i \geq 2$ 时, 对 $t \in\left[\frac{i-1}{i} \frac{a_{i}}{a_{i-1}}, \frac{a_{i}}{a_{i-1}}\right]$, 我们令

$$
a_{m}^{\prime}= \begin{cases}t a_{m}, & 0 \leq m \leq i-1 \\ a_{m}, & i \leq m \leq n\end{cases}
$$

相当于将前面等差数列部分的斜率改变, 而其余项不动. 由 $t$ 范围知 $\left\{a_{m}^{\prime}\right\}$ 也符合题设条件, 且将 $a_{m}^{\prime}(1 \leq m \leq n)$ 代入 (5) 式, 左边为关于 $t$ 的开口向下二次函数. 注意到要证即为 $t=1$ 对应的不等式, 而由开口向下二次函数性质,
我们只需要证明两个端点所对应的不等式, 即 $a_{0}, a_{1}, \cdots, a_{i}$ 成等差数列, 或 $a_{i-1}=a_{i}$ 的情形即可. 而这两种情形本质上是一样的, 并且我们可以对另一边作相同的调整, 因此便完成了化归. 类似地, 我们可以对后一种情形作相应的简化.

完成上述简化后, 本问题已无实质难度, 经计算可知 (5) 的确成立, 因此原题中令 $c=3$ 即可.

评注 本题调整方式基于优超不等式的思想, 虽然证明过程略显复杂, 但总体思路还是较为清晰自然的, 借助图像可能会帮我们更深刻的理解本题所用调整的动机，以及整个调整的过程。另外，本题调整方法并不唯一，读者们可以尝试利用其它调整方法解决本题。

接下来的两个问题并没有直接用到调整法, 而是通过不等式取等条件限定出特定结构, 从而相当于做了“调整”.

例 4 给定正整数 $n>1$ 以及正实数 $x_{1}, \cdots, x_{n}$, 满足 $x_{1}+\cdots+x_{n}=n-1$.证明:

$$
\sum_{1 \leq i<j \leq n} \frac{\left(1-x_{i}\right)\left(1-x_{j}\right)}{x_{i} x_{j}} \geq \frac{n}{2 n-2}
$$

(摘自《Problems from the Book》)

分析 通过恒等变形可知, 原不等式等价于

$$
\left(\sum_{i=1}^{n} \frac{1}{x_{i}}-(n-1)\right)^{2}-\sum_{i=1}^{n} \frac{1}{x_{i}^{2}} \geq \frac{n}{n-1}-(n-1)
$$

现在我们固定

$$
a=\sum_{i=1}^{n} \frac{1}{x_{i}}
$$

的值, 来考虑在此限制条件下, 使 $a$ 取最大值的取等条件有何性质. 我们通过局部不等式取等条件来证明: 其中有 $n-1$ 个变量相等.

证明 设 $a$ 定义同分析, 则由柯西不等式不难得到 $a \geq \frac{n^{2}}{n-1}$. 任取 $i \in$ $\{1,2, \cdots, n\}$, 则我们有

$$
\sum_{j \neq i} x_{j}=n-1-x_{i}, \sum_{j \neq i} \frac{1}{x_{j}}=a-\frac{1}{x_{i}}
$$

从而由柯西不等式, 我们得到

$$
\left(n-1-x_{i}\right)\left(a-\frac{1}{x_{i}}\right)=\sum_{j \neq i} x_{j} \sum_{j \neq i} \frac{1}{x_{j}} \geq(n-1)^{2}, \forall 1 \leq i \leq n .
$$

以上不等式可以解得 $x_{i} \in[\alpha, \beta]$, 其中 $0<\alpha \leq \beta$ 为关于 $x$ 的方程

$$
\frac{n-1}{x}+a x=(n-1) a-n^{2}+2 n
$$

的两正实根. 现在, 我们有局部不等式

$$
\frac{\left(x_{i}-\alpha\right)\left(x_{i}-\frac{n-1-\alpha}{n-1}\right)^{2}}{x_{i}^{2}} \geq 0,
$$

展开得

$$
x_{i}-\lambda_{1}-\frac{\lambda_{2}}{x_{i}}-\frac{\lambda_{3}}{x_{i}^{2}} \geq 0,
$$

其中 $\lambda_{i}(i=1,2,3)$ 均由 $a$ 确定, 且 $\lambda_{3}>0$. 因此对上述不等式从 $i=1$ 到 $n$ 求和即知,

$$
\sum_{i=1}^{n} \frac{1}{x_{i}^{2}} \leq \sum_{i=1}^{n} \frac{x_{i}-\lambda_{1}-\frac{\lambda_{2}}{x_{i}}}{\lambda_{3}}=F(a)
$$

其中 $F$ 是一个仅与 $a$ 有关的函数, 这样我们就消掉了 $x_{1}, \cdots, x_{n}$. 再考虑能否取等: 事实上只要 $x_{1}=\cdots=x_{n-1}=\frac{n-1-\alpha}{n-1}, x_{n}=\alpha$, 则利用 (7) 可得

$$
\sum_{i=1}^{n} \frac{1}{x_{i}}=\frac{(n-1)^{2}}{n-1-\alpha}+\frac{1}{\alpha}=\frac{\left(n^{2}-2 n\right) \alpha+n-1}{(n-1-\alpha) \alpha}=a,
$$

且以上各局部不等式均成立等号.

因此我们说明了若固定 $\sum_{i=1}^{n} \frac{1}{x_{i}}$ 的值, 则 $\sum_{i=1}^{n} \frac{1}{x_{i}^{2}}$ 取最大值时必有 $n-1$ 个变量相等. 故我们只需要对这种特殊情况证明原不等式 (6) 即可.

$$
\text { 令 } x_{1}=\cdots=x_{n-1}=t, x_{n}=(n-1)(1-t)(t<1) \text {. 带入不等式 }(6) \text {, 其左端 }
$$

为

$$
\left(\frac{n-1}{t}+\frac{1}{(n-1)(1-t)}-(n-1)\right)^{2}-\frac{n-1}{t^{2}}-\frac{1}{(n-1)^{2}(1-t)^{2}}
$$

经计算知上式 $\geq \frac{n}{n-1}-(n-1) \Longleftrightarrow(1-t)\left(t-\frac{n-1}{n}\right)^{2} \geq 0$, 显然成立. 因此原不等式得证.

评注 本题通过待定系数与局部不等式取等条件限定出取等条件的特定结构, 无形中对变量进行了调整。值得注意的是, 当我们得到了 $\sum_{i=1}^{n} \frac{1}{x_{i}^{2}} \leq F(a)$ 时,我们并没有将其直接带回原不等式，而是利用设而不求的思想，跳出原来的局面，转而去解决更为一般，也更为自然的情形。这种思想在下面的例子中还会出现, 并且利用类似本题的方法, 我们可以解决如下问题:

思考题 1 已知存在一组正实数 $x_{1}, x_{2}, \cdots, x_{k}$ 满足不等式组

$$
\left\{\begin{array}{l}
x_{1}^{2}+x_{2}^{2}+\cdots+x_{k}^{2}<\frac{1}{2}\left(x_{1}+x_{2}+\cdots+x_{k}\right) \\
x_{1}+x_{2}+\cdots+x_{k}<\frac{1}{2}\left(x_{1}^{3}+x_{2}^{3}+\cdots+x_{k}^{3}\right)
\end{array}\right.
$$

试求满足上述条件的正整数 $k$ 最小值.

(2007 年中国国家队培训题)

思考题 2 设 $a_{1}, a_{2}, \cdots, a_{n}, x_{1}, x_{2}, \cdots, x_{n}$ 为 $2 n$ 个正实数, 且满足

$$
\sum_{1 \leq i<j \leq n} x_{i} x_{j}=\left(\begin{array}{l}
n \\
2
\end{array}\right)
$$

试证明:

$$
\sum_{i=1}^{n}\left(\frac{a_{i}}{\sum_{j \neq i} a_{j}} \sum_{j \neq i} x_{j}\right) \geq n
$$

(摘自《Problems from the Book》)

例 5 求最大常数 $C$, 使得对任何正整数 $n$ 以及非负实数 $x_{1}, x_{2}, \cdots, x_{n}$ 都有

$$
\left(\sum_{i=1}^{n} i x_{i}\right)\left(\sum_{i=1}^{n} x_{i}^{2}\right) \geq C\left(\sum_{i=1}^{n} x_{i}\right)^{3}
$$

(摘自《Problems from the Book》)

分析 首先由排序不等式可知, 我们只需要考虑 $x_{1} \geq x_{2} \geq \cdots \geq x_{n}$ 的情形. 此时, 我们试图将一般情形化归成如下特殊情形: 对某个 $1 \leq l \leq n$, $x_{1}>x_{2}>\cdots>x_{l}>0$ 成递减等差数列, 而 $x_{l+1}=\cdots=x_{n}=0$ (从后面的过程可以看出这种形式是如何猜到的).

一个自然地想法是：固定上述表达式中两个一次式的值, 将为题转化为条件极值问题. 具体地, 我们设

$$
\sum_{i=1}^{n} x_{i}=a, \sum_{i=1}^{n} i x_{i}=b
$$

其中 $a, b$ 为常数, 且由序关系以及切比雪夫不等式知, 我们可以假设 $0<a \leq$ $b \leq \frac{n+1}{2} a$. 下面来求 $c=\sum_{i=1}^{n} x_{i}^{2}$ 的最小值. 对于这类条件极值问题, 我们可以借助拉格朗日乘数法的思想, 选取待定参数 $\lambda_{1}, \lambda_{2}$, 考虑

$$
c+\lambda_{1} a+\lambda_{2} b=\sum_{i=1}^{n}\left(x_{i}^{2}+\left(\lambda_{1}+i \lambda_{2}\right) x_{i}\right)
$$

则只需对上式在 $x_{i} \geq 0$ 条件下求局部最小值, 从而导出相应取等条件的结构.最后只需要说明存在适当的 $\lambda_{1}, \lambda_{2}$ 满足以上取等条件确实可以取到, 便完成了化归.

证明 以下记号同分析. 对任何 $\lambda_{1}, \lambda_{2}>0$, 记 $l$ 为小于 $\lambda_{2}$ 而不大于 $n$ 的最
大整数, 则我们有

$$
\lambda_{1} x_{i}^{2}+\left(i-\lambda_{2}\right) x_{i} \geq \begin{cases}-\frac{\left(i-\lambda_{2}\right)^{2}}{4 \lambda_{1}}, & \text { 若 } i \leq l ; \\ 0, & \text { 若 } i>l .\end{cases}
$$

求和得到

$$
\lambda_{1} c+b-\lambda_{2} a=\sum_{i=1}^{n}\left(\lambda_{1} x_{i}^{2}+\left(i-\lambda_{2}\right) x_{i}\right) \geq \sum_{i=1}^{l}\left(-\frac{\left(i-\lambda_{2}\right)^{2}}{4 \lambda_{1}}\right),
$$

且取等条件为

$$
x_{i}= \begin{cases}\frac{\lambda_{2}-i}{2 \lambda_{1}}, & \text { 若 } 1 \leq i \leq l \\ 0, & \text { 若 } i>l\end{cases}
$$

若想要上述不等式能取等, $\lambda_{1}, \lambda_{2}$ 需要满足

$$
\left\{\begin{array}{l}
\sum_{i=1}^{l} \frac{\lambda_{2}-i}{2 \lambda_{1}}=a \\
\sum_{i=1}^{l} \frac{i \lambda_{2}-i^{2}}{2 \lambda_{1}}=b
\end{array}\right.
$$

解得

$$
\left\{\begin{array}{l}
\lambda_{1}=\frac{l(l-1)(l+1)}{12((l+1) a-2 b)} \\
\lambda_{2}=\frac{(l+1)((2 l+1) a-3 b)}{3((l+1) a-2 b)}
\end{array}\right.
$$

这时还需要满足 $\lambda_{1}>0, \lambda_{2}>0$, 且 $l$ 为小于 $\lambda_{2}$ 且不超过 $n$ 的最大整数这一条件. 稍加计算可知, 只要取

$$
l= \begin{cases}\left\lceil\frac{3 b}{a}\right\rceil-2, & \text { 若 } b \leq \frac{n+1}{3} a ; \\ n, & \text { 若 } \frac{n+1}{3} a<b \leq \frac{n+1}{2} a .\end{cases}
$$

便可保证以上条件均成立. 因此, 对上述 $l$, 令 $\lambda_{1}, \lambda_{2}$ 满足 (8) 式, 则以上每个不等式均可取等. 这样我们说明了: 在两个一次式 $\sum_{i=1}^{n} x_{i}, \sum_{i=1}^{n} i x_{i}$ 的值固定的条件下, $\sum_{i=1}^{n} x_{i}^{2}$ 在 $x_{1}, \cdots, x_{l}$ 成等差数列, 而 $x_{l+1}=\cdots=x_{n}=0$ 的情况下取最小值.因此我们只需对这种特殊情况解决原问题即可.

仅需考虑 $l>1$ 的情形. 设 $x_{i}=r(i-1)+s(l-i), 1 \leq i \leq l$, 其中 $r, s>0$.再令 $t=\frac{r}{r+s} \in(0,1)$, 则以上不等式等价于

$$
\frac{2(l+1)}{9 l(l-1)} \cdot\left((2 l+2) t^{3}-3 t+2 l-1\right) \geq \frac{4}{9}
$$

求导知上式左边关于 $t$ 最小值为

$$
\frac{4(l+1)\left(l-\frac{1}{2}-\frac{1}{\sqrt{2 l+2}}\right)}{9 l(l-1)}>\frac{4}{9}
$$

且令 $l \rightarrow \infty$ 知 $\frac{4}{9}$ 不可改进. 因此所求 $C$ 的最大值为 $\frac{4}{9}$.

评注 本题的基本出发点是固定两个较简单的一次式, 从而将问题化为条件极值问题, 再借助拉格朗日乘数法思想选取待定系数放缩, 以得到取等条件的结构 (解竞赛题时应尽量避开直接使用拉格朗日乘数法)。值得注意的是, 如果只要证明 $C=\frac{4}{9}$ 的正确性, 仅仅利用前一部分的放缩即可, 而上述做法完全刻画了取等条件的结构, 因此甚至可以做出对固定的 $n$ 的最佳值(见证明过程).另外, 本题亦可用积分处理.

最后, 我们举一个应用无限调整法的例子.

例 6 给定正整数 $n \geq 3$, 以及 $n$ 个正实数 $a_{1}, a_{2}, \cdots, a_{n}$. 令

$$
A_{n}=\frac{1}{n} \sum_{i=1}^{n} a_{i}, G_{n}=\sqrt[n]{a_{1} a_{2} \cdots a_{n}}, H_{n}=\frac{n}{\sum_{i=1}^{n} \frac{1}{a_{i}}}, Q_{n}=\sqrt{\frac{1}{n} \sum_{i=1}^{n} a_{i}^{2}} .
$$

证明:

$$
Q_{n} \cdot H_{n} \leq \frac{(n-1)^{\frac{3 n-4}{2 n}}}{\sqrt{n^{2}-3 n+3}} A_{n} \cdot G_{n}
$$

分析 我们仍然试图将原不等式化归成有 $n-1$ 个变量相等的情形. 我们的出发点是如下三元对称不等式中的重要结论:

引理 设正实数 $a, b, c$ 满足 $a+b+c=p, a b c=r$, 其中 $p, r$ 为定值. 则 $q=a b+b c+c a$ 取最小值在 $a, b, c$ 中较小的两个数相等.

这里我们只提一下引理的证明思路. 第一个方法是利用函数图像: $y_{1}=$ $x^{3}-p x^{2}-r$ 与 $y_{2}=-q x$ 应有 3 个横坐标大于 0 的交点, 现在要使 $q$ 尽量小, 那么 $y_{2}$ 应是 $y_{1}$ 的切线, 从而结合图像可知结论成立.

![](https://cdn.mathpix.com/cropped/2024_02_26_32a62e02ff7d7ce3d55eg-12.jpg?height=628&width=731&top_left_y=1962&top_left_x=662)
另一个方法是将 $a^{2}+b^{2}+c^{2}$ 与 $a^{3}+b^{3}+c^{3}$ 用 $p, q, r$ 表示出来, 再同例 4 一样构造局部不等式. 具体过程这里就不赘述了.

证明 我们定义 $L-$ 操作如下：对任何三个正实数 $0<a \leq b \leq c$, 称 $(a, b, c) \rightarrow\left(a^{\prime}, b^{\prime}, c^{\prime}\right)$ 为一次 $L$-操作, 其中 $\left(a^{\prime}, b^{\prime}, c^{\prime}\right)$ 是满足

$$
\left\{\begin{array}{l}
a^{\prime}+b^{\prime}+c^{\prime}=a+b+c \\
a^{\prime} b^{\prime} c^{\prime}=a b c \\
0<a^{\prime} \leq b^{\prime} \leq c^{\prime}
\end{array}\right.
$$

且使 $a^{\prime} b^{\prime}+b^{\prime} c^{\prime}+c^{\prime} a^{\prime}$ 最小的三元数组. 则由上述引理及其证明过程可知, 必有

$$
a \leq a^{\prime}=b^{\prime} \leq c \leq c^{\prime} .
$$

现在, 我们固定 $a_{1}, a_{2}, \cdots, a_{n}$ 中 $n-3$ 个变量, 而对余下三个变量做 $L-$ 操作, 则每操作一次 $A_{n}, G_{n}$ 均不变, 而 $H_{n}, Q_{n}$ 均不增. 可惜的是, 仅凭 $L-$ 操作并不能直接化归为 $a_{1}, a_{2}, \cdots, a_{n}$ 中有 $n-1$ 个变量相等的情形, 但我们可以做到的是, 通过很多次这样的 $L-$ 操作, 使得 $a_{1}, a_{2}, \cdots, a_{n}$ 无限逼近这种情形.

不妨设 $a_{1} \leq a_{2} \leq \cdots \leq a_{n}$, 记 $\left(a_{1}, \cdots, a_{n}\right)=\left(a_{1}^{(0)}, \cdots, a_{n}^{(0)}\right)$. 我们依次进行如下操作 : 对任何 $k \geq 0$, 设我们有 $a_{1}^{(k)} \leq \cdots \leq a_{n}^{(k)}$, 固定 $a_{2}^{(k)}, \cdots, a_{n-2}^{(k)}$, 对 $a_{1}^{(k)}, a_{n-1}^{(k)}, a_{n}^{(k)}$ 做 $L$-操作, 再对所得 $n$ 个数重新排序得到 $a_{1}^{(k+1)} \leq \cdots \leq a_{n}^{(k+1)}$.我们来证明:

$$
\lim _{k \rightarrow \infty}\left|a_{n-1}^{(k)}-a_{1}^{(k)}\right|=0 .
$$

由 $(\star)$ 我们知道, $a_{1}^{(0)} \leq a_{1}^{(1)} \leq \cdots$ 以及 $a_{n}^{(0)} \leq a_{n}^{(1)} \leq \cdots$, 又这两个数列均有界, 因此极限均存在, 分别记为 $x$ 与 $y$. 则对 $\forall \varepsilon>0$, 存在 $N$, 使得对任何 $m \geq N$, 均有

$$
x-\varepsilon<a_{1}^{(m)} \leq x, y-\varepsilon<a_{n}^{(m)} \leq y .
$$

则对任何 $m \geq N$, 考虑 $L-$ 操作 $\left(a_{1}^{(m)}, a_{n-1}^{(m)}, a_{n}^{(m)}\right) \rightarrow\left(t, t, a_{n}^{(m+1)}\right)$, 则

$$
\left\{\begin{array}{l}
a_{1}^{(m)}+a_{n-1}^{(m)}+a_{n}^{(m)}=2 t+a_{n}^{(m+1)} \\
a_{1}^{(m)} a_{n-1}^{(m)} a_{n}^{(m)}=t^{2} a_{n}^{(m+1)}
\end{array} .\right.
$$

注意到 $y-\varepsilon<a_{n}^{(m)} \leq a_{n}^{(m+1)} \leq y$, 因此我们有

$$
\left\{\begin{array}{l}
\left|a_{1}^{(m)}+a_{n-1}^{(m)}-2 t\right|=\left|a_{n}^{(m+1)}-a_{n}^{(m)}\right|<\varepsilon \\
a_{1}^{(m)} a_{n-1}^{(m)}=t^{2} \frac{a_{n}^{(m+1)}}{a_{n}^{(m)}} \geq t^{2}
\end{array} .\right.
$$

从而由 $\left|a_{1}^{(m)}-a_{n-1}^{(m)}\right|^{2}=\left(a_{1}^{(m)}+a_{n-1}^{(m)}\right)^{2}-4 a_{1}^{(m)} a_{n-1}^{(m)} \leq(2 t+\varepsilon)^{2}-4 t^{2}$ 得

$$
\left|a_{1}^{(m)}-a_{n-1}^{(m)}\right|^{2} \leq \varepsilon^{2}+4 t \varepsilon \leq \varepsilon^{2}+4 y \varepsilon, \forall m \geq N
$$

由 $\varepsilon$ 的任意性, 我们就证明了 (9). 并可由此立即得到

$$
\lim _{k \rightarrow \infty}\left(a_{1}^{(k)}, \cdots, a_{n}^{(k)}\right)=(x, x, \cdots, x, y)
$$

现在, 考虑函数

$$
F\left(a_{1}, a_{2}, \cdots, a_{n}\right)=\frac{A_{n} \cdot G_{n}}{H_{n} \cdot Q_{n}},
$$

则我们得到

$$
F\left(a_{1}, \cdots, a_{n}\right)=F\left(a_{1}^{(0)}, \cdots, a_{n}^{(0)}\right) \leq F\left(a_{1}^{(1)}, \cdots, a_{n}^{(1)}\right) \leq \cdots
$$

又显然有 $F$ 连续, 因此

$F\left(a_{1}, \cdots, a_{n}\right) \leq \lim _{k \rightarrow \infty} F\left(a_{1}^{(k)}, \cdots, a_{n}^{(k)}\right)=F\left(\lim _{k \rightarrow \infty}\left(a_{1}^{(k)}, \cdots, a_{n}^{(k)}\right)\right)=F(x, x, \cdots, x, y)$

这样我们就成功将问题化归为 $n-1$ 个变量相等的情形.

最后, 对这种特殊情形, 我们可设 $a_{1}=\cdots=a_{n-1}=1, a_{n}=t \geq 1$, 则

$$
F\left(a_{1}, \cdots, a_{n}\right)=f(t)=\frac{n^{\frac{3}{2}} \sqrt{n-1+t^{2}}}{\left(n-1+\frac{1}{t}\right)(n-1+t) \sqrt[n]{t}} .
$$

求导知

$$
f^{\prime}(t)=\frac{\sqrt{n}(n-1)(t+1)(t-1)^{2}\left((n-1)^{2}-t\right)}{t^{2+\frac{1}{n}}\left(n-1+\frac{1}{t}\right)^{2}(n-1+t)^{2} \sqrt{n-1+t^{2}}}
$$

因此

$$
\max _{t \geq 1}\{f(t)\}=f\left((n-1)^{2}\right)=\frac{(n-1)^{\frac{3 n-4}{2 n}}}{\sqrt{n^{2}-3 n+3}}
$$

原不等式得证.

评注 本题的证明从局部出发, 对任 3 个变量做局部分析, 再应用至整体. 当然, 有限次调整并不能保证得到我们所期望的结构, 因此我们采用极限的思想,通过调整不断逼近最终的理想结构, 再利用一些连续性等极限分析, 便可达到调整的目的.

总评 调整法不应局限于某几种特定形式的调整, 而应视为一种寻找结构性质的思想. 这种刻画局部结构, 整体结构, 甚至是抽象结构的思想, 在数学竞赛的许多方面都有重要应用. 本文所举的几个例子, 正是这样想方设法通过各种技巧获取结构性质, 从而简化问题. 最后, 调整法的奇思妙想, 绝非本文区区几例便可道尽, 还需读者自己多多感悟与探寻.

