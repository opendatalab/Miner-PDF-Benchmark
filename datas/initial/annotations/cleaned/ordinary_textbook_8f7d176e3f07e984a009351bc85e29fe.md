数学新星网 $\%$ 学生专栏

www.nsmath.cn/xszl

# 2022 年韩国数学奥林匹克决赛试题解析 

王凯信1 高嘉成 ${ }^{2}$

(1. 加拿大, 温哥华市, Magee Secondary School; 2. 江苏省天一中学, 214101)

本文介绍 2022 年韩国数学奥林匹克总决赛试题及其解析. 其中第 $1 、 4$ 题由高嘉成解答, 其余均由王凯信 (2022 IMO 加拿大国家队队员) 发布在 AoPS 网站上的解答整理.

本卷质量很高, 难度安排合理: $1 、 4$ 约为高联第 $1 、 2$ 题难度, $2 、 3 、 5 、 6$大致与 CMO 对应难度相当. 我们已将解答写得尽量清晰易懂, 但不当之处在所难免, 欢迎读者批评!

## I. 试 题

1. 给定外心为 $O$ 的锐角 $\triangle A B C$, 令 $D 、 E 、 F$ 分别为 $A 、 B 、 C$ 到对边的垂足. $P$ 为 $\triangle A B C$ 的外接圆在 $B$ 和 $C$ 处的切线的交点. 一条经过 $P$ 且垂直于 $E F$ 的直线交直线 $A D$ 于 $Q . R$ 为 $A$ 在 $E F$ 上的投影. 证明: $D R / / O Q$. (本题的图见解答与评注部分)
2. 有 $n \geq 4$ 个盒子 $A_{1}, \cdots, A_{n}$, 里面有非负数个鹅卵石(所以它可以是空的). 令 $a_{n}$ 为盒子 $A_{n}$ 中的我鸟卵石数量. 所有盒子总计有 $3 n$ 块我勿卵石. 从现在开始, Alice 执行以下操作: 在每一次操作中, Alice 选择其中一个非空的盒子.然后她将该盒中鹅卵石分成 $n$ 组, 使得任意两组鹅卵石的数量之差最多为 1 ,并将这 $n$ 组鹅卵石依次放入 $n$ 个盒子中. 这种情况一直持续到只有一个盒子里有所有的我勿石, 其余的都是空的. 结束后, 将该操作的“长度”定义为 Alice 完成的操作总数.

令 $f\left(a_{1}, \cdots, a_{n}\right)$ 为对 $\left(a_{1}, \cdots, a_{n}\right)$ 所有可能的操作中 “长度” 的最小值.求 $f\left(a_{1}, \cdots, a_{n}\right)$ 的最大可能值, 并求出所有有序对 $\left(a_{1}, \cdots, a_{n}\right)$ 使得它取得该最大值.

修订日期: 2022-06-07.

3. 给定函数 $g: \mathbb{R} \rightarrow \mathbb{R}$, 其值域是一有限集. 求所有 $f: \mathbb{R} \rightarrow \mathbb{R}$, 使得对任意 $x, y \in \mathbb{R}$, 均满足 $2 f(x+g(y))=f(2 g(x)+y)+f(x+3 g(y))$.
4. 给定不等边三角形 $A B C$, 其内心为 $I$. 令 $A I$ 与 $\triangle A B C$ 的外接圆再次交于 $M$. 三角形 $A B C$ 的内切圆 $\omega$ 分别切 $A B 、 A C$ 于 $D 、 E . O$ 为 $\triangle B D E$ 的外心, $L$ 为 $\omega$ 与 $A$ 到 $B C$ 的高的交点, 且 $A$ 和 $L$ 位于直线 $D E$ 同侧. 用 $\Omega$ 表示以 $O$ 为圆心、经过 $L$ 的圆, $A L$ 与 $\Omega$ 再次交于 $N$. 证明: 直线 $L D$ 和 $M B$ 的交点在 $\triangle L N E$ 的外接圆上. (本题的图见解答与评注部分)
5. 求所有正整数 $m$, 使得存在整数 $x 、 y$ 满足 $m \mid x^{2}+11 y^{2}+2022$.
6. 我们称集合 $X$ 为“花式集合”,如果它满足如下三个条件:

(a) $|X|=2022$;

(b) $X$ 的每个元素都是包含于 $[0,1]$ 中的闭区间;

(c) 对于任意实数 $r \in[0,1], X$ 中包含 $r$ 的元素个数不超过 1011 .

对于“花式集合” $A 、 B$ 和区间 $I \in A 、 J \in B$, 用 $n(A, B)$ 表示使得 $I \cap J \neq \varnothing$ 的对 $(I, J)$ 的数量. 求 $n(A, B)$ 的最大值.

## II. 解答与评注

题 1 给定外心为 $O$ 的锐角 $\triangle A B C$, 令 $D 、 E 、 F$ 分别为 $A 、 B 、 C$ 到对边的垂足. $P$ 为 $\triangle A B C$ 的外接圆在 $B$ 和 $C$ 处的切线的交点. 一条经过 $P$ 且垂直于 $E F$ 的直线交直线 $A D$ 于 $Q . R$ 为 $A$ 在 $E F$ 上的投影. 证明: $D R / / O Q$.


证明 显然 $B 、 C 、 E 、 F$ 四点共圆, 故 $\angle A B C=\angle A E R$. 因此

$$
\angle R A E=90^{\circ}-\angle A E R=90^{\circ}-\angle A B C .
$$

另一方面, 由 $\angle O A E=90^{\circ}-\angle A B C$, 可得 $A 、 R 、 O$ 三点共线. 从而, 四边形 $A O P Q$ 为平行四边形. 又

$$
\angle P O C=\frac{1}{2} \angle B O C=\angle B A C=\angle B A E, \angle A E B=\angle O C P=90^{\circ},
$$

所以 $\triangle \mathrm{ABE} \sim \triangle O P C$. 因此,

$$
\frac{A R}{A D}=\frac{A E}{A B}=\frac{O C}{O P}=\frac{A O}{A Q}
$$

所以 $D R / / O Q$.

评注 本题很简单, 考察的结构已经为人熟知. 注意到四边形 $A O P Q$ 为平行四边形即可.

题 2 有 $n \geq 4$ 个盒子 $A_{1}, \cdots, A_{n}$, 里面有非负数个鹅卵石(所以它可以是空的). 令 $a_{n}$ 为盒子 $A_{n}$ 中的鹅卵石数量. 所有盒子总计有 $3 n$ 块鹅卵石. 从现在开始, Alice 执行以下操作: 在每一次操作中, Alice 选择其中一个非空的盒子.然后她将该盒中鹅卵石分成 $n$ 组, 使得任意两组鹅卵石的数量之差最多为 1 ,并将这 $n$ 组鹅卵石依次放入 $n$ 个盒子中. 这种情况一直持续到只有一个盒子里有所有的鹅卵石，其余的都是空的．结束后，将该操作的“长度” 定义为 Alice 完成的操作总数.

令 $f\left(a_{1}, \cdots, a_{n}\right)$ 为对 $\left(a_{1}, \cdots, a_{n}\right)$ 所有可能的操作 中 “长度” 的最小值.求 $f\left(a_{1}, \cdots, a_{n}\right)$ 的最大可能值, 并求出所有有序对 $\left(a_{1}, \cdots, a_{n}\right)$ 使得它取得该最大值.

解 答案是 $3 n-4$, 当且仅当 $a_{i}=3(1 \leq i \leq n)$ 时取等. 在解答过程中, $A_{n}$ 为所有石头最终的归属, 即任意时刻均有 $a_{n}=\max \left\{a_{1}, a_{2}, \cdots, a_{n}\right\}$.因此, $A_{n}$ 每次均获得 1 或 2 块石头(如果某次它获得 3 块石头, 则对于某个 $j \neq n, a_{j} \geq 2 n+1$, 那么 $a_{j}+a_{n} \geq 4 n>3 n$, 矛盾).

下面, 我们分成三步解决此问题:

第一步，最值点构造.

- 对 $A_{i}(1 \leq i \leq n-3)$ 操作, 将石头运到 $A_{n-2}, A_{n-1}, A_{n}$, 得到 $a_{1}=$ $\cdots=a_{n-3}=0, a_{n-2}=a_{n-1}=a_{n}=n$. 这需要 $n-3$ 步;
- 对 $A_{n-2}$ 操作, 给每盒 1 块石头, 得到 $a_{1}=\cdots=a_{n-2}=1, a_{n-1}=a_{n}=$ $n+1$. 这需要 1 步;
- 对 $A_{n-1}$ 操作, 给 $A_{n-2}$ 块石头, 其余各一块石头, 得到 $a_{1}=\cdots=$ $a_{n-2}=2, a_{n-1}=1, a_{n}=n+3$. 这需要 1 步;
- 对 $A_{i}(1 \leq i \leq n-1)$ 操作, 均将一块石头运到 $A_{n}$, 这需要 $3 n-(n+3)=$ $2 n-3$ 步.

综合上述, 我们总共用了 $3 n-4$ 步.

第二步, 论证 $f\left(a_{1}, \cdots, a_{n}\right) \leq 3 n-5, \forall\left(a_{1}, \cdots, a_{n}\right) \neq(3, \cdots, 3)$.

此时, 在任一初始情况中, 存在 $j(1 \leq j \leq n)$ 使得 $a_{j} \geq 4$.

如果此 $a_{j} \geq 5$, 确保每次操作都给 $A_{j}$ 一块石头, 那么 $f\left(a_{1}, \cdots, a_{n}\right) \leq$ $3 n-5$, 结论成立; 否则对所有 $j \in\{1,2, \cdots, n\}$, 我们有 $a_{j} \leq 4$. 不妨设 $a_{n}=4$.若我们确保每次操作后, $A_{n}$ 至少增加一块石头, 且有一次增加 2 块石头, 那么结论成立.

我们有 $\max \left\{a_{1}, \cdots, a_{n-1}\right\} \in\{3,4\}$.

以下分两类讨论:

$1^{\circ}$ 如果 $\max \left\{a_{1}, a_{2}, \cdots, a_{n-1}\right\}=3$, 我们希望某一刻 $A_{n-1}$ 有 $n+1$ 块石头,并让其余 $A_{j}(1 \leq j \leq n-2)$ 每次各运给 $A_{n-1}$ 和 $A_{n}$ 一块石头. 因为 $a_{j} \leq 3(1 \leq$ $j \leq n-1)$ 且 $\sum_{j=1}^{n-1} a_{j}=3(n-1)-1$, 故 $\left\{a_{1}, a_{2}, \cdots, a_{n}\right\}=\{2,3,3, \cdots, 3,3,4\}$.对于 $1 \leq j \leq n-2$, Alice 每次操作将 $A_{j}$ 清空并给 $A_{n-1}$ 和 $A_{n}$ 各运一块石头,这就保证了在某一刻会出现 $a_{n-1}=n+1$.

$2^{\circ}$ 如果 $\max \left\{a_{1}, a_{2}, \cdots, a_{n-1}\right\}=4$, 不妨设 $a_{n-1}=4$, 希望 $A_{n-1}$ 和 $A_{n}$同时增加 $n-3$ 次. 此时 $a_{1}, a_{2}, \cdots, a_{n-2} \in[0,4]$, 其和为 $3 n-8$. 我们需要确保除了 $A_{1}, \cdots, A_{n-2}$ 中的一个之外, 其它所有的 $A_{j}$ 都给 $A_{n-1}$ 运一块石头, 这意味着当它们给出石头的时候, 它们至少拥有 2 块石头. 如果 $A_{j}$ 的石头数多于 2 ,让它把石头运给那些拥有 0 或 1 块石头的盒子.

我们对 $n$ 归纳证明: 若 $a_{1}+\cdots+a_{n-2} \geq 2(n-2)$, 那么可使 $A_{n-1}$ 获得至少 $n-3$ 块石头.

奠基为 $n=4$, 不难直接验证其正确.

假设命题对 $n-1$ 成立, 来看 $n$ 时的情形: 当 $A_{j}(1 \leq j \leq n-2)$ 给 $A_{n-1}$ 和 $A_{n}$ 各一块石头后, 我们让 $A_{j}$ 把它剩余的石头运给 $A_{1}, \cdots, A_{n-2}$ (除去 $A_{j}$ ) 的其中之一, 并对 $\left\{a_{1}, \cdots a_{n-2}\right\} \backslash\left\{a_{j}\right\}$ 运用归纳假设即可.

综合以上所有情况, 可知: 我们可以使 $A_{n-1}$ 拥有 $n+1$ 块石头, 它将在某次操作中运给 $A_{n-2}$ 块石头, 这就保证了在不多于 $3 n-4-1=3 n-5$ 次操作后必能实现 $a_{n}=3 n$, 因为每次操作后 $A_{n}$ 至少获得了 1 块石头.
第三步, 论证 $f(3,3, \cdots, 3) \geq 3 n-4$.

反证法, 假设 $f(3,3, \cdots, 3) \leq 3 n-5$. 这意味着 $a_{n}$ 增加 2 至少两次. 考虑除 $A_{n}$ 以外的某一盒首次拥有 $n+1$ 块石头的时刻. 在这盒将 2 块石头运给 $A_{n}$ 之前, $a_{n} \geq n+1$. 在这盒将 2 块石头运给 $A_{n}$ 之后, 前 $n-1$ 盒中最多剩下 $3 n-(n+3)=2 n-3$ 块石头, 且每个 $A_{j}(1 \leq j \leq n-1)$ 中至少有一块石头.

假设每一盒尝试在 $A_{1}, \cdots, A_{n}$ 中再创造一个拥有 $n+1$ 块石头的盒(不妨设为 $\left.A_{n-1}\right)$. 分两种情况讨论:

$1^{\circ}$ 如果 $A_{n}$ 每次均获得 1 块石头, 由于 $A_{i}(1 \leq i \leq n-2)$ 始终需要给 $A_{n}$ 运一块石头, 因此它最多能给除 $A_{n}$ 以外的其它盒 $a_{i}-1$ 块石头. 因此, 在 $A_{1}, \cdots, A_{n-2}$ 都向 $A_{n}$ 运送了一块石头后,

$$
a_{n-1}^{\prime} \leq \sum_{j=1}^{n-2}\left(a_{j}-1\right)+a_{n-1} \leq \sum_{j=1}^{n-1} a_{j}-(n-2) \leq(2 n-3)-(n-2)=n-1
$$

故 $\max \left\{a_{1}, \cdots, a_{n-1}\right\}$ 的最大值为 $n-1$, 也即无法给另一盒 $n+1$ 块石头.

$2^{\circ}$ 如果 $A_{n}$ 不满足每次增加 1 块石头, 那么, 为了实现目标, 我们必须至少 2 次不给 $A_{n}$ 运送石头. 这是因为, 每块未运给 $A_{n}$ 的石头至多为某个拥有 $n+1$ 块石头的候选盒贡献 1 块石头, 且每次给 $A_{n}$ 运 1 块石头将会使得它至多拥有 $n-1$ 块石头. 因此, 结合 $a_{n}$ 每次至多增加 2 , 可知这样将会使 “长度”严格增加. 这显然是一个矛盾.

根据 $1^{\circ}$ 和 $2^{\circ}$ 知, 反证法假设不成立!

综合上述三个步骤即得原题结论.

评注 这道题的想法简单、直观: 把主要注意力集中在一个盒子上, 分析它的鹅卵石数量的变化, 但是想要严谨地将过程表达清楚却并不容易。

题 3 给定函数 $g: \mathbb{R} \rightarrow \mathbb{R}$, 其值域是一有限集. 求所有 $f: \mathbb{R} \rightarrow \mathbb{R}$, 使得对任意 $x, y \in \mathbb{R}$, 均满足 $2 f(x+g(y))=f(2 g(x)+y)+f(x+3 g(y))$.

解 答案是一切常函数, 不难验证其成立. 下证只有常函数符合要求.

定义 $P(x, y)$ 为题中所给等式, $\operatorname{Im}(f), \operatorname{Im}(g)$ 分别表示函数 $f 、 g$ 的值域. 因为 $g$ 的值域是有限集, 故我们不妨设 $\operatorname{Im}(g)=\left\{a_{1}, a_{2}, \cdots, a_{n}\right\}, T_{j}=$ $\left\{y \mid g(y)=a_{j}\right\}$. 我们先证明:

$$
|\operatorname{Im}(f)| \leq|\operatorname{Im}(g)| .
$$

这是因为, 由 $P\left(x, t_{j}\right)$ (此处的 $t_{j}(1 \leq j \leq n)$ 遍历 $T_{j}$ 的所有元素)可得,

$$
f\left(2 g(x)+t_{j}\right)=2 f\left(x+a_{j}\right)-f\left(x+3 a_{j}\right) .
$$

我们可以看出, 固定 $x$, 当 $t_{j}$ 变化时, 右式是一个常量.

又因为 $T_{1} \cup T_{2} \cup \cdots \cup T_{n}=\mathbb{R}$, 所以 $\operatorname{Im}(f) \subseteq\left\{f\left(2 g(x)+t_{j}\right) \mid 1 \leq j \leq n\right\}$.因此 $|\operatorname{Im}(f)| \leq|\operatorname{Im}(g)|$.

设 $\operatorname{Im}(f)=\left\{x_{1}, x_{2}, \cdots, x_{m}\right\}$, 不妨设

$$
x_{1}=\max \left\{x_{1}, x_{2}, \cdots, x_{m}\right\}, x_{m}=\min \left\{x_{1}, x_{2}, \cdots, x_{m}\right\} .
$$

设 $X_{j}=\left\{x \mid f(x)=x_{j}\right\}, 1 \leq j \leq m$. 既然 $\operatorname{Im}(f)$ 为有限集, 如果 $f(x+g(y))$取得最大值, 那么 $f(x+3 g(y))$ 和 $f(2 g(x)+y)$ 也取得最大值.

设 $x$ 为 $X_{1}$ 中某个元素减去 $a_{j}$ 后的值. 由于 $x+a_{j} \in X_{1}$, 故 $f\left(x+a_{j}\right)=x_{1}$.由 $x_{1}$ 的最大性, 可得: 对于任意的 $t_{j} \in T_{j}$, 均有 $f\left(2 g(x)+t_{j}\right)=x_{1}$.

另一方面, 如果 $x+g(y) \in X_{1}$, 那么 $x+3 g(y)$ 和 $2 g(x)+y$ 皆属于 $X_{1}$. 此时, 若 $z \in X_{1}$, 代入 $P(z-g(y), y)$ 即得 $f(z+2 g(y))=x_{1}$.

这意味着, $\left\{x+2 a_{j} \mid x \in X_{1}\right\} \subseteq X_{1}$.

同理, 若 $z \in X_{m}$, 则 $\left\{x+2 a_{j} \mid x \in X_{m}\right\} \subseteq X_{m}$.

我们选取 $x \in X_{1}, z \in X_{m}$, 由 $P(x-g(y), y)$ 和 $P(z-g(y), y)$ 分别得到:

$$
2 g(x-g(y))+y \in X_{1} ; 2 g(z-g(y))+y \in X_{m} .
$$

再由 $(*)$ 得:

$$
2 g(x-g(y))+2 g(z-g(y))+y \in X_{1} ; 2 g(x-g(y))+2 g(z-g(y))+y \in X_{m} \text {. }
$$

因此, $x_{1}=x_{m}$, 故 $f$ 为常函数.

评注 $(1)$. 本题的关键在于得到 $f(\mathbb{R})$ 为有限集.

(2). 尽管此题被放在了第一天的第三题位置, 其难度却不算太高, 但是一个极不常规的函数方程, 类似于 2018 年国家集训队第一次测试的第四题. 最后得到 $f(x)$ 为常函数的步骤也可以通过反证法实现, 读者不妨尝试.

题 4 给定不等边三角形 $A B C$, 其内心为 $I$. 令 $A I$ 与 $\triangle A B C$ 的外接圆再次交于 $M$. 三角形 $A B C$ 的内切圆 $\omega$ 分别切 $A B 、 A C$ 于 $D 、 E . O$ 为 $\triangle B D E$的外心, $L$ 为 $\omega$ 与 $A$ 到 $B C$ 的高的交点, 且 $A$ 和 $L$ 位于直线 $D E$ 同侧. 用 $\Omega$ 表示以 $O$ 为圆心、经过 $L$ 的圆, $A L$ 与 $\Omega$ 再次交于 $N$. 证明: 直线 $L D$ 和 $M B$ 的交点在 $\triangle L N E$ 的外接圆上.

证明 同一法. 设 $L D$ 与 $M B$ 的延长线交于 $X, \triangle E L X$ 的外接圆(圆心为 $Q)$ 与直线 $A L$ 再次交于点 $\mathrm{N}^{\prime}$.

下面, 我们证明 $N \equiv N^{\prime}$.



这等价于 $Q O$ 垂直平分 $L N^{\prime}$, 进而等价于 $B C / / O Q$.

由于

$$
\begin{aligned}
\angle E L X & =\pi-(\angle L D E+\angle L E D)=\pi-(\angle L D E+\angle L D A) \\
& =\angle E D B=\frac{(\pi+\angle A)}{2}
\end{aligned}
$$

从而 $\angle E Q X=\angle E O B=\pi-\angle A$.

又因为 $Q E=Q X, O E=O B$, 故 $\triangle E Q X \sim \triangle E O B$. 亦可得到 $\triangle E O Q \sim$ $\triangle E B X$. 此时, 直线 $B M$ 与直线 $O Q$ 的夹角即为 $\angle Q E X=\frac{1}{2} \angle B A C=\angle M B C$,故 $B C / / O Q$.

评注 本题没有本质的难度, 对于点 $L$ 稍作考察, 便得到上述仅用倒角的方法. 有兴趣的读者不妨试证: 直线 $B X$ 与 $\triangle B D E$ 的外接圆的第二个交点在 $\Omega$上.

题 5 求所有正整数 $m$, 使得存在整数 $x 、 y$ 满足 $m \mid x^{2}+11 y^{2}+2022$.

解 答案是 $\left\{m \in \mathbb{N} \mid \nu_{2}(m) \leq 1, \nu_{337}(m) \leq 1,11 \nmid m\right\}$. 我们分成两步证明之. 解答中的 $\left(\frac{a}{p}\right)$ 为勒让德符号.

第一步, 符合条件的 $m$ 只能是上述集合中的数.

$1^{\circ}$ 如果 $2 \mid x^{2}+11 y^{2}+2022$, 则 $x 、 y$ 同奇偶. 因此, $x^{2}+11 y^{2}+2022 \equiv 2$ $(\bmod 4)$, 故 $4 \nmid x^{2}+11 y^{2}+2022$.

$2^{\circ}$ 如果方程 $x^{2} \not \equiv-11 y^{2}(\bmod 337)$ 有 $x 、 y \not \equiv 0(\bmod 337)$ 的整数解,则 $\left(\frac{-11}{337}\right)=1$. 因为 -1 是 $\bmod 337$ 的二次剩余, 故必然有 $\left(\frac{11}{337}\right)=1$. 由二次互反律, 知:

$$
\left(\frac{337}{11}\right)=\left(\frac{11}{337}\right) \cdot\left(\frac{337}{11}\right)=(-1)^{\frac{337-1}{2} \cdot \frac{11-1}{2}}=1
$$

这导致 7 是 $\bmod 11$ 的二次剩余, 矛盾!

所以, 如果 $337 \nmid x^{2}+11 y^{2}+2022$, 则 $337 \mid x, y$, 故 $337^{2} \mid x^{2}+11 y^{2}$, 故 $337^{2} \nmid x^{2}+11 y^{2}+2022$.

$3^{\circ}$ 注意到 $2022 \equiv 9(\bmod 11)$ 且 $11 \mid x^{2}+9$ 无整数解.

综合 $1^{\circ} 、 2^{\circ} 、 3^{\circ}$ 可知 $m$ 必为上述集合中的数.

第二步, 上述 $m$ 符合题设.

(i) 若 $p=2$ 或 337 , 则存在 $x 、 y$ 使得 $p \mid x^{2}+11 y^{2}+2022$. 只需取 $x=y=0$ 即可.

(ii) 若质数 $p \notin\{2,11,337\}$, 我们先证明一个引理.

引理 若 $p$ 是一个奇质数, 则存在 $x 、 y$ 使得 $p \mid x^{2}+11 y^{2}+2022$ 且 $p \nmid x y$.

证明 $1^{\circ}$ 若 $p=3$, 取 $x=y=1$ 即可.

$2^{\circ}$ 若 $p \geq 5$, 考虑方程 $x^{2}-y^{2} \equiv t(\bmod p)$. 当 $p \nmid t$ 时, 它有 $p-1$ 个解;其余情况有 $2 p-1$ 个解. 此易于证明(注意到当 $x+y$ 固定时, $x-y$ 也固定).

如果 $\left(\frac{-11}{p}\right)=1$, 不妨设 $-11 \equiv c^{2}(\bmod p)$. 则由 $-2022 \equiv x^{2}+11 y^{2} \equiv$ $x^{2}-(c y)^{2}(\bmod p)$, 结合刚刚的结论知引理成立;

如果 $\left(\frac{-11}{p}\right)=-1$, 这意味着 $-11 y^{2}$ 可以取到所有 $\bmod p$ 的二次非剩余.如果存在 $x_{0} \in\{1,2, \cdots, p-1\}$, 使得 $x_{0}^{2}+2022$ 是 $\bmod p$ 的二次非剩余,则存在 $y_{0}$ 使得 $x_{0}^{2}+2022 \equiv-11 y_{0}^{2}(\bmod p)$, 结论成立; 否则, 对于 $\bmod p$ 的任意非零二次剩余 $a$, 有 $a+2022$ 也是 $\bmod p$ 的二次剩余. 则不存在某个 $\bmod p$ 的非零二次剩余 $a$, 使得 $a+2022 k\left(0 \leq k \leq \frac{p-1}{2}\right)$ 均为 $\bmod p$ 的非零二次剩余. 所以, 对所有 $\bmod p$ 的非零二次剩余 $a_{1}, a_{2}, \cdots, a_{\frac{p-1}{2}}$, 均存在 $1 \leq k_{i} \leq \frac{p-1}{2}\left(1 \leq i \leq \frac{p-1}{2}\right.$ 且 $k_{i}$ 互不相同 $)$, 使得

而

$$
\left\{\begin{aligned}
& a_{1}+2022 k_{1} \equiv 0(\bmod p) \\
& a_{2}+2022 k_{2} \equiv 0(\bmod p) \\
& \vdots \\
& a_{\frac{p-1}{2}}+2022 k_{\frac{p-1}{2}} \equiv 0 \quad(\bmod p)
\end{aligned}\right.
$$

$$
\begin{aligned}
& a_{1}+a_{2}+\cdots+a_{\frac{p-1}{2}} \equiv 0 \quad(\bmod p) \\
& k_{1}+k_{2}+\cdots+k_{\frac{p-1}{2}}=1+2+\cdots+\frac{p-1}{2} \not \equiv 0 \quad(\bmod p)
\end{aligned}
$$

矛盾!

综合 $1^{\circ} 、 2^{\circ}$, 引理得证!

回到原题, 我们断言: $m=p^{k}\left(k \in \mathbb{N}_{+}\right.$, 质数 $\left.p \notin\{2,11,337\}\right)$ 均符合题设.
对 $k$ 用归纳法:

$1^{\circ} k=1$ 时即为引理的结论.

$2^{\circ}$ 假设 $p^{k-1} \mid x^{2}+11 y^{2}+2022, p \nmid x y$, 考虑如下 $p$ 个代数式:

$$
x^{2},\left(x+p^{k-1}\right)^{2}, \cdots,\left(x+(p-1) p^{k-1}\right)^{2}
$$

它们对于 $\bmod p^{k}$ 两两不同余, 但是都同余于 $x^{2}\left(\bmod p^{k-1}\right)$. 因此, 至少有一个 $\left(x+j \cdot p^{k-1}\right)^{2}+11 y^{2}+2022(0 \leq j \leq p-1)$ 被 $p^{k}$ 整除. 这就完成了归纳过渡.

最后, 由中国剩余定理, 原命题得证!

评注 (1). 该问题很标准, 不难分析. 从 $x$ 到 $x+p^{k}, x+2 p^{k}, \cdots, x+(p-1) p^{k}$的素数幂递归法(prime lifting) 是 $\bmod p^{k}$ 意义下进行同余分析的宗旨. 有时,这比 Hensel引理用起来更直观、有效.

(2). 事实上, 该问题的背景与 Cauchy-Davenport 定理有关.

(3). 有兴趣的读者也可尝试通过 $\sum_{y=0}^{p-1}\left(\frac{t-y^{2}}{p}\right)$ 来证明解的存在性.

题 6 我们称集合 $X$ 为“花式集合”，如果它满足如下三个条件:

(a) $|X|=2022$;

(b) $X$ 的每个元素都是包含于 $[0,1]$ 中的闭区间;

(c) 对于任意实数 $r \in[0,1], X$ 中包含 $r$ 的元素个数不超过 1011 .

对于“花式集合” $A 、 B$ 和区间 $I \in A 、 J \in B$, 用 $n(A, B)$ 表示使得 $I \cap J \neq \varnothing$ 的对 $(I, J)$ 的数量. 求 $n(A, B)$ 的最大值.

解 答案是 $3 \times 1011^{2}(=3066363)$.

先给出取得最大值的构造: 易于验证, 当 $A$ 由 1011 个 $[0,0.4]$ 以及 1011 个 $[0.45,1]$ 组成、 $B$ 由 1011 个 $[0,0.46]$ 以及 1011 个 $[0.5,1]$ 组成时, 符合题意.

再给出最优性的证明: 分成两步进行.

第一步, 调整集合.

断言一: 对于 $A$ 中区间 $[a, c],[b, d]$, 如果 $a \leq b \leq c \leq d$, 则将 $A$ 中的 $[a, c],[b, d]$ 替换为 $[a, d],[b, c]$ 不改变原结果, 称之为“切换”.

这是因为, $1^{\circ}$ 如果 $B$ 中的一个区间与 $[b, c]$ 相交, 那么它最初和现在都与两个区间相交, 成立;

$2^{\circ}$ 如果 $B$ 中的一个区间与 $[b, c]$ 不相交, 则它要么与 $[a, b]$ 和 $[c, d]$ 都不相交, 要么恰与 $[a, b],[c, d]$ 中一个相交. 因此, 如果它与其中之一相交, 则在替换区间后仍会与其中之一相交, 也成立.
断言二: 总能在有限次 “切换” 后, 使得对于 $A$ 中任意两个区间, 它们要么不交, 要么一个包含另一个, 对于 $B$ 亦然.

为此, 考虑一个以区间为顶点的图 $G$, 两顶点之间连边当且仅当它们对应的两区间交集非空(特别地, $[a, a]$ 仍算作非空). 将每个连通分支的顶点对应的区间划分为一组, 记为 $G_{j}$, 使得如果 $X_{j}=\bigcup_{I \in G_{j}} I$, 则 $X_{i} \cap X_{j}=\varnothing$. 显然此分组方式唯一且不改变图 $G$ 的连通性.

下面, 我们固定 $j$ 并对 $|A|$ 进行归纳. 奠基为 $|A|=2$, 显然成立.

对每个 $j$, 考虑 $G_{j}$ 中左端点位于最左边的区间 $K_{j}=\left[l_{1}, r\right]$ (注意 $r$ 稍后可能会变化). 则对于其它任何区间 $[a, b](b \geq a)$, 我们有 $l_{1} \leq a$. 另外, 若 $b \leq r$,则称 $K_{j}$ 包含 $[a, b]$.

对其它区间 $K_{j}$ 执行操作, 那么 $K_{j}$ 总是包含操作后的区间. 因此, $K_{j}$ 与 $G_{j}$中的每个区间最多相交一次. 只要存在区间 $[a, b]$ 且 $a \leq r<b$, 操作过程就不会结束. 当操作终止时, $G_{j}$ 中必然不存在满足 $a \leq r<b$ 的区间 $[a, b]$, 并且对于 $k \neq j, G_{j}$ 不与 $G_{k}$ 中的任何区间相交. 因此, $K_{j}=X_{j}$, 且 $K_{j}$ 包含 $G_{j}$ 中的所有区间. 此时, 我们去掉 $K_{1}, K_{2}, \cdots$, 对 $A \backslash\left\{K_{1}, \cdots\right\}$ 应用归纳假设即可.

第二步, 加强归纳.

设集合 $X$ 为“ ( $a, b)$-好的”集合, 如果: 1) $|X|=a ; 2) X$ 的每个元素都是包含在 $[0,1]$ 中的闭区间; 3$)$ 对于任意实数 $r \in[0,1], X$ 中包含 $r$ 的元素个数不超过 $b$. 定义 $f(a, b, c, d)$ 为 $n(A, B)$ 可以取得的最大值, 其中 $A$ 是 “ $(a, b)$-好的”集合且 $B$ 是“ $(c, d)$-好的”集合. 下证加强的命题: $f(a, b, c, d) \leq b c+a d-b d$,原题即 $a=c=2 k, b=d=k$ 时的特例.

对此, 我们采用归纳法.

奠基为 $b=d=1$. 此时, 再对 $a+c$ 使用归纳法. 如果 $\min \{a, c\}=1$, 显然成立; 否则, 设 $\left[l_{1}, r_{1}\right],\left[l_{2}, r_{2}\right]$ 为 $A$ 中最左边的两个区间(注意到 $r_{1}<l_{2}$, 因此我们能够比较这两个区间的位置)、 $\left[x_{1}, y_{1}\right],\left[x_{2}, y_{2}\right]$ 为 $B$ 中最左边的两个区间. 此时不难得到: $\left[l_{1}, r_{1}\right]$ 或 $\left[x_{1}, y_{1}\right]$ 两者之一，与另一个集合中最多一个区间有非空交集. 这是因为, 若对某个 $k \geq 2,\left[l_{1}, r_{1}\right]$ 与 $\left[x_{k}, y_{k}\right]$ 的交集非空, 则 $y_{1}<x_{2} \leq x_{k} \leq r_{1} \leq l_{2}$. 因此, 对于所有 $j \geq 2,\left[x_{1}, y_{1}\right]$ 与 $\left[l_{j}, r_{j}\right]$ 交集为空. 不妨设 $\left[x_{1}, y_{1}\right]$ 与另一个集合中最多一个区间有非空交集, 这样一来, 我们可以去掉 $\left[x_{1}, y_{1}\right]$, 再利用归纳假设, 结论成立.

不妨设 $b \geq 2$, 否则把 $(a, b)$ 换成 $(c, d)$.

令 $S$ 为 $A$ 中互相不包含的区间的集合(如果多个区间相同且未严格包含于
更大的区间中, 则选择任意一个加入 $S)$. 注意到 $S$ 为“( $|S|, 1)$-好的”集合, $A \backslash S$为“ $(a-|S|, b-1)$-好的”集合. 则:

$$
\begin{aligned}
n(A, B) & =n(S, B)+n(A \backslash S, B) \\
& \leq f(|S|, 1, c, d)+f(a-|S|, b-1, c, d) \\
& =|S| d+c-d+(a-|S|) d+(b-1) c-(b-1) d \\
& =a d+b c-b d
\end{aligned}
$$

其中, 不等号使用了奠基的结论.

至此, 加强的命题得证!

评注 (1). 该解法的动机是本题存在多种取等条件, 其中的关键部分是如下的操作: $a<b<c<d \rightarrow[a, c],[b, d] \rightarrow[a, d],[b, c]$, 以使得两个区间要么不交, 要么一个包含另一个. 然后推而广之, 使用加强归纳法. 有兴趣的读者可以思考，如何使用相同的“切换”，在任意“ $(2 k, k)$-好的”集合中得到 $k$ 对不交的区间.

(2). 事实上, 2022 年伊朗 TST 的第12 题也考察了“区间集”, 读者不妨尝试.

## III. 写在最后

致谢 非常感谢审稿人对本文提出的宝贵意见和冷岗松老师的指导, 让我们意识到严谨表述的重要性.

## 参考 (王凯信同学的解答出处)

第二题: https://artofproblemsolving.com/community/c6h2830263p25205282

第三题: https://artofproblemsolving.com/community/c6h2830169p25053464

第五题: https://artofproblemsolving.com/community/c6h2830171p25043204

第六题: https://artofproblemsolving.com/community/c6h2830172p25072925

