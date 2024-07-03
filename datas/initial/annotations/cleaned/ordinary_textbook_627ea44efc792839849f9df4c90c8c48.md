# 第 35 届 CMO 试题解答 

$$
\text { 严彬玮 }
$$

(南京师范大学附属中学, 210000)

指导教师: 葛军 陈兴江

2019 年第 35 届 CMO 于 11 月 24 日至 11 月 30 日在武汉华中师大一附中举行, 我取得了满分的好成绩. 下面介绍我的解法, 请读者批评指正!

题 1 设实数 $a_{1}, a_{2}, \cdots, a_{40}$ 满足 $a_{1}+a_{2}+\cdots+a_{40}=0$, 且对 $1 \leq i \leq 40$,均有 $\left|a_{i}-a_{i+1}\right| \leq 1$, 这里 $a_{41}=a_{1}$. 记 $a=a_{10}, b=a_{20}, c=a_{30}, d=a_{40}$.

(1) 求 $a+b+c+d$ 的最大值;

(2) 求 $a b+c d$ 的最大值.

解 (1) 由于 $a_{i+1} \leq a_{i}+1, a_{i+1} \geq a_{i}-1$, 为了方便, 令 $a_{i+40}=a_{i}$, 有

$$
\begin{aligned}
a_{1}+\cdots+a_{40}= & \left(a_{5}+a_{6}+\cdots+a_{14}\right)+\left(a_{15}+a_{16}+\cdots+a_{24}\right)+ \\
& \left(a_{25}+a_{26}+\cdots+a_{34}\right)+\left(a_{35}+a_{36}+\cdots+a_{4}\right) \\
\geq & (10 a-5-4-3-2-1)+(10 b-25)+10 c-25+10 d-25 \\
= & 10(a+b+c+d)-100 .
\end{aligned}
$$

因此 $a+b+c+d \leq 10$. 当

$$
\begin{aligned}
& a_{1}=1.5, a_{2}=0.5, a_{3}=-0.5, a_{4}=-1.5, a_{5}=-2.5, a_{6}=-1.5, \\
& a_{7}=-0.5, a_{8}=0.5, a_{9}=1.5, a_{10}=2.5, a_{i+10}=a_{i}
\end{aligned}
$$

时取等.

(2) 由于

$$
\begin{gathered}
a_{1}+\cdots+a_{40} \geq a-15+a-14+\cdots a+a-1+\cdots+a-4+ \\
\quad b-5+b-4+\cdots+b+b-1+\cdots+b-14 \\
=(a+b) \times 20-250 .
\end{gathered}
$$

修订日期: 2019-12-22.
因此 $a+b \leq \frac{25}{2}$.

取所有 $a_{1} \sim a_{40}$ 为相反数可知 $a+b \geq-\frac{25}{2}$.

同理 $|c+d| \leq \frac{25}{2}$.

若 $a, b$ 不同号, 有

$$
a b+c d \leq \frac{(c+d)^{2}}{4} \leq \frac{625}{16}<\frac{425}{8} .
$$

$c, d$ 不同号的情况同理;

若 $a, b, c, d$ 均非负, 有

$$
a b+c d \leq \frac{(a+b)^{2}+(c+d)^{2}}{4} \leq \frac{(a+b+c+d)^{2}}{4} \leq 25<\frac{425}{8}
$$

若 $a, b \geq 0, c, d \leq 0$, 设

$$
|a+b|=m,|c+d|=n,
$$

其中 $m, n \leq \frac{25}{2}$. 由

$$
(a-d)+(b-c) \leq 10+10=20
$$

知 $m+n \leq 20$. 记 $m+n=k$, 不妨设 $m \geq \frac{k}{2}, m \leq k$,

$$
a b+c d \leq \frac{m^{2}+n^{2}}{4}=\frac{m^{2}+(k-m)^{2}}{4}
$$

以 $m$ 主元二次函数在 $m \geq \frac{k}{2}$ 时单调增.

当 $k \leq \frac{25}{2}$ 时,

$$
a b+c d \leq \frac{k^{2}}{4}=\frac{625}{16}<\frac{425}{8} .
$$

当 $k>\frac{25}{2}$ 时,

$$
a b+c d \leq \frac{\left(\frac{25}{2}\right)^{2}+\left(k-\frac{25}{2}\right)^{2}}{4} \leq \frac{\left(\frac{25}{2}\right)^{2}+\left(\frac{15}{2}\right)^{2}}{4}=\frac{425}{8} .
$$

当

$$
\begin{aligned}
& a=b=\frac{25}{4}, c=d=\frac{-15}{4}, a b+c d=\frac{425}{8}, \\
& a_{1}=a-9, a_{2}=a-8, \cdots, a_{9}=a-1, \\
& a_{11}=a-1, a_{12}=a-2, \cdots, a_{15}=a-5, \\
& a_{16}=b-4, a_{17}=b-3, \cdots, a_{19}=b-1, \\
& a_{21}=b-1, a_{22}=b-2, \cdots, a_{35}=b-15, \\
& a_{36}=a-14, a_{37}=a-13, \cdots, a_{40}=a-10
\end{aligned}
$$

时取等.
题 2 如图所示, 在 $\triangle A B C$ 中, $A B>A C, \angle B A C$ 的平分线与 $B C$ 交于点 $D$. 点 $P$ 是线段 $D A$ 延长线上一点, $P Q$ 与 $\triangle A B D$ 的外接圆相切于点 $Q(Q, B$在直线 $A D$ 同侧), $P R$ 与 $\triangle A C D$ 的外接圆相切于点 $R$ ( $R, C$ 在直线 $A D$ 同侧).线段 $B R, C Q$ 交于点 $K$. 过点 $K$ 作 $B C$ 的平行线, 分别与 $Q D, A D, R D$ 相交于点 $E, L, F$. 证明: $E L=F K$.



证明 作 $\triangle A B C$ 外接圆 $\odot O$, 设 $\mathrm{AD}$ 交 $\odot O$ 于 $M$, 设 $\odot A D B$ 为 $\odot O_{1}$, 半径为 $r_{1}, \odot A D C$ 为 $\odot O_{2}$, 半径为 $r_{2}$. 延长 $M B, P Q$ 交于 $X, P R, M C$ 交于 $Y$ (若 $P Q / / M B$, 则 $X$ 不存在, 令 $\angle P X M=0^{\circ}, \angle X Q B=90^{\circ}=\angle X B Q$; 若 $P R / / M C$, 则 $Y$ 不存在, 令 $\left.\angle P Y M=0^{\circ}, \angle Y R C=90^{\circ}=\angle Y C R\right)$.

(1) 我们先证明 $B C R Q$ 共圆. 由

$$
\begin{aligned}
\angle B Q R+\angle B C R & =360^{\circ}-\angle P Q R-\angle X Q B-\angle B C M-\angle Y C R \\
& =360^{\circ}-\left(360^{\circ}-\frac{\angle Q P R}{2}-\frac{\angle B M C}{2}-\frac{\angle P Y M}{2}-\frac{\angle P X M}{2}\right) \\
& =180^{\circ} .
\end{aligned}
$$

故 $B C R Q$ 共圆. 有 $\frac{R K}{K Q}=\frac{R C}{Q B}$.

(2) 我们再证明 $\frac{E L}{L F}=\frac{F K}{K E}$. 由正弦定理:

$$
E L=\frac{D L \sin \angle E D L}{\sin \angle L E D}, L F=\frac{D L \sin \angle F D L}{\sin \angle L F D}
$$

而由 $E F / / B C$,

而

$$
\sin \angle L E D=\sin \angle Q D B=\frac{Q B}{2 r_{1}}, \sin \angle L F D=\frac{R C}{2 r_{2}} .
$$

$$
\frac{\sin \angle Q D A}{\sin \angle R D A}=\frac{P Q \sin \angle P Q D}{P D} \times \frac{P D}{P R \sin \angle P R D}=\frac{\sin \angle Q B D}{\sin \angle R C D}
$$

故

$$
\frac{E L}{L F}=\frac{\sin \angle L F D}{\sin \angle L E D} \times \frac{\sin \angle E D L}{\sin \angle F D L}=\frac{R C}{Q B} \times \frac{r_{1}}{r_{2}} \times \frac{\sin \angle Q B D}{\sin \angle R C D}
$$

而

$$
\frac{F K}{K E}=\frac{\sin \angle B R D \times R K}{\sin \angle C Q D \times K Q} \times \frac{\sin \angle Q D B}{\sin \angle R D C}=\frac{R C}{Q B} \times \frac{B D}{R B} \times \frac{Q C}{C D},
$$

由 $\angle B A D=\angle C A D$ 有

$$
\frac{B D}{D C}=\frac{A B}{A C}=\frac{r_{1}}{r_{2}}
$$

而由于 $B C R Q$ 共圆, 因此

$$
\frac{Q C}{R B}=\frac{\sin \angle Q B D}{\sin \angle R C D}
$$

故

$$
\frac{F K}{K E}=\frac{R C}{Q B} \times \frac{r_{1}}{r_{2}} \times \frac{\sin \angle Q B D}{\sin \angle R C D}
$$

可得

$$
\frac{E L}{L F}=\frac{F K}{K E}
$$

故

$$
\frac{L F}{E L}=\frac{K E}{F K}, \frac{L F+E L}{E L}=\frac{K E+F K}{F K} .
$$

因此 $E L=F K$. 证毕.

题 3 设 $S$ 是一个 35 元集合, $F$ 是由一些 $S$ 到自身的映射构成的集合. 对于正整数 $k$, 称 $F$ 具有性质 $P(k)$, 如果对于任意 $x, y \in S$, 都存在 $F$ 中的 $k$ 个映射 $f_{1}, f_{2}, \cdots, f_{k}$ (可以相同), 使得 $f_{k}\left(\cdots\left(f_{2}\left(f_{1}(x)\right)\right) \cdots\right)=f_{k}\left(\cdots\left(f_{2}\left(f_{1}(y)\right)\right) \cdots\right)$.

求最小正整数 $m$,使得所有具有性质 $P(2019)$ 的 $F$ 都具有性质 $P(m)$.

解 $m$ 最小值为 595 , 理由如下.

(1) 先证明 $m \leq 595$.

若 $m>595$, 设 $m$ 最小值为 $t$, 则必存在 $x, y, x \neq y$, 使得对所有 $f_{1} \cdots f_{k} \in$ $F$, 满足 $f_{k}\left(f_{k-1}\left(\cdots\left(f_{1}(x)\right)\right) \cdots\right)=f_{k}\left(f_{k-1}\left(\cdots\left(f_{1}(y)\right)\right) \cdots\right)$ 的 $k$ 均有 $k \geq t$ (由于 $F$ 满足 $P(2019)$ 所以存在 $\left.f_{1}, \cdots, f_{k}\right)$.

对于每一个 $f_{i}$, 定义 $g_{i}$ : 对所有

$$
f_{i}(a)=b, g_{i}(a)=b, f_{i}(c)=d, g_{i}(c)=d \text {. }
$$

$b \neq d$ 时, $g_{i}(a, c)=(b, d), b=d$ 时, $g_{i}(a, c)=b$ (此时的数组为不计顺序的二元集, 为了方便写成数组的形式). 因此必定存在 $x, y, x \neq y,(x, y)$ 在 $F$ 中映射
至少 $k$ 次方可变为一个数字而非数组. 由于 $k \geq 596, \mathrm{C}_{35}^{2}=595$, 而 $(x, y)$ 映射 0 次到 $k-1$ 次之后均为数组, 否则与 $k$ 最小值矛盾. 记 $g_{0}(x, y)=(x, y)$, 必存在 $i, j, i \neq j$, 满足

$$
g_{i}\left(\cdots\left(g_{1}(x, y)\right) \cdots\right)=g_{j}\left(\cdots\left(g_{i}\left(\cdots\left(g_{1}(x, y)\right) \cdots\right)\right)\right) \text {. }
$$

此时去除 $g_{i} \sim g_{j-1}$ 之后, $g_{k}\left(\cdots\left(g_{j}\left(g_{i-1}(\cdots(x, y) \cdots)\right)\right)\right)$ 为一个数, 而少于 $k$ 次映射, 矛盾. 因此 $m \leq 595$.

(2)再证明 $m \geq 595$. 不妨令 $S=\{1,2, \cdots, 35\}$, 取 $F=\left\{f_{A}, f_{B}\right\}$, 其中

$$
f_{A}(x)=x+1(\bmod 35), f_{B}(x) \equiv\left\{\begin{array}{l}
x \quad x \neq 1(\bmod 35) \\
2 x=1(\bmod 35)
\end{array}\left(\text { 即 } f_{A}(35)=1\right) .\right.
$$

此时先证明 $F$ 满足 $P(2019)$ : 对任意 $x, y$, 如(1)时定义 $g_{A}, g_{B}$, 在 $f_{A}$ 中操作至多 34 次可使 $(x, y)$ 中有一个变为 1 , 设为 $(1, n) . n=1$ 时已满足, $n \neq 1$ 时, 则 $g_{B}(1, n)=(2, n)$.

$$
\begin{aligned}
& \text { 令 } g_{C}=g_{B} \circ g_{A}^{(34)} \text {, 则 } \\
& g_{C}^{(n-2)}\left(g_{B}(1, n)\right)=g_{C}^{(n-2)}(2, n)=g_{C}^{(n-3)}(2, n-1)=\cdots=g_{C}(2,3)=2 .
\end{aligned}
$$

共计操作了至多 $34+35 \times(n-2)+1 \leq 35^{2}<2019$ 次. 因此 $F$ 满足 $P(2019)$.

下证 $F$ 不满足 $P(594)$. 取 $(2,19)$, 则对任意 $x \neq y$, 令

$$
h(x, y) \equiv \pm(x-y)(\bmod 35)
$$

$h(x, y)$ 取 $|x-y|, 35-|x-y|$ 中较小的一个, 则 $h(2,19)=17$. 考虑只有 $g_{B}(1,2)=2$ 是唯一一个数组 $\rightarrow$ 数的方法, 而 $h(1,2)=1$,

不考虑自身映射时, $x \neq y, x \neq 1, y \neq 1$ 只能映射到 $(x+1, y+1)$ (模 35 意义下, 下文均在模 35 意义下).

不妨设从 $(2,19)$ 到 2 至少需 $P$ 次映射, 则每一次映射后所得到数组互不相同, 以 $(1,2)$ 倒推:

(I) $x \neq y, x \neq 2, y \neq 2$ 时 $(x, y)$ 只能由 $(x-1, y-1)$ 映射到 $(x, y)$.

(II) $y \neq 1, x=2$ 时可以从 $(1, y) \rightarrow(x, y)(B)$ 或从 $(1, y-1) \rightarrow$ $(2, y)(A) . y=1, x=2$ 时只可以从 $(35,1) \rightarrow(1,2)$ ( $A$ 映射 $)$.

因此有 $(1,2) \leftarrow(35,1) \leftarrow \cdots \leftarrow(3,4) \leftarrow(2,3)$. 此时所有 $x \neq y, h(x, y)=$ 1 的数组均出现过了 $(2,3)$ 为 $(\mathrm{II})$ 情况, 但 $(1,2) \rightarrow(2,3)(A)$ 或 $(1,3) \rightarrow(2,3)(B)$,而 $(1,2)$ 出现过了, 由每次映射后所得数组互不相同有 $(2,3) \leftarrow(1,3) \leftarrow$ $(35,2), B$ 映射 $(1,35) \rightarrow(2,35)$, 而 $h(1,35)=1$ 已出现. 故 $(35,2) \leftarrow(34,1) \leftarrow$ $\cdots \leftarrow(2,4)$, 到此时所有 $x \neq y, h(x, y)=2$ 数组已出现, 对于所有的 $i=$
$2,3, \cdots 16$, 若 $h(x, y)=i$ 的 $(\mathrm{x}, \mathrm{y})$ 均已出现过, 且倒推到了 $(2,(36-i))$ 这个数, 则 $(2,(36-i))$ 若由 $(1,36-i)$ 推出, 则 $h(1,36-i)=i$ 已出现, 矛盾. 因此 $(2,(36-i))$ 由 $(1,35-i)$ 推出.

若已倒推到 $(2,2+i)$, 则若 $(1,1+i) \rightarrow(2,2+i), h(1,1+i)=i$ 已出现,矛盾. 因此 $(2,2+i)$ 由 $(1,2+i)$ 推出, 故

$$
\begin{aligned}
2 & \leftarrow(1,2) \leftarrow(35,1) \leftarrow \cdots \leftarrow(2,3) \leftarrow(1,3) \leftarrow(35,2) \leftarrow(34,1) \leftarrow \cdots \leftarrow(2,4) \\
& \leftarrow(1,4) \leftarrow \cdots \leftarrow(34,2) \leftarrow(33,1) \leftarrow \cdots \leftarrow(1,5) \leftarrow \cdots \leftarrow(2,18) \\
& \leftarrow(1,18) \leftarrow \cdots \leftarrow(2,20) \leftarrow(1,19) \leftarrow \cdots \leftarrow(19,2)
\end{aligned}
$$

共用了 $17 \times 35=595$ 次映射. 因此 $F$ 不满足 $P(594)$.

证毕.

题 4 求最大实数 $c$, 使得下述结论对于所有整数 $n \geq 3$ 成立: 设 $A_{1}, A_{2}, \cdots$, $A_{n}$ 是圆周上的 $n$ 条弧 (每条弧都包含自身的端点), 如果存在至少 $\frac{1}{2} \mathrm{C}_{n}^{3}$ 个三元组 $(i, j, k)$, 满足 $1 \leq i<j \leq n$, 且 $A_{i} \cap A_{j} \cap A_{k} \neq \varnothing$, 则存在 $I \in\{1,2, \cdots, n\}$, 满足 $|I|>c n$, 且 $\bigcap_{i \in I} A_{i} \neq \varnothing$.

解 $c=\frac{\sqrt{6}}{6}$, 理由如下:

(1) 先证 $c=\frac{\sqrt{6}}{6}$ 时命题成立.

对于所有位置上的端点, 若存在两个端点重合, 则可以移动其中一个非常短的距离, 使得其所在弧稍微变长一点点而不影响任何交关系(即交是否为空集不会改变).

设端点为 $a_{1}, a_{2}, \cdots, a_{2 n}$. 设在每一个端点处有 $x_{i}$ 个弧包含了 $a_{i}$. 在每个端点处记录所有三元组, 其中一段弧以该端点为端点, 另外两段弧包含该端点,他们交非空, 则求和得到 $T=\sum_{i=1}^{2 n} \mathrm{C}_{x_{i-1}}^{2}$ 个.

另一方面, 每个三元组, 只要他们交非空, 他们交为一小段弧(已知端点不重). 这一小段弧的 2 个端点均记录了这个三元组各一次. 此时每个三元组被计至少 2 次. 故 $T \geq 2 \times \frac{1}{2} \mathrm{C}_{n}^{3}$, 即

$$
\sum_{i=1}^{2 n} \mathrm{C}_{x_{i-1}}^{2} \geq \frac{n(n-1)(n-2)}{3 \times 2}
$$

不妨设 $x_{1}=\max \left\{x_{1}, \cdots, x_{2 n}\right\}$, 有 $2 n \times \mathrm{C}_{x_{1-1}}^{2} \geq \frac{n(n-1)(n-2)}{3 \times 2}$. 故 $\left(x_{1}-1\right)\left(x_{1}-2\right) \geq \frac{(n-1)(n-2)}{6}>\frac{(n-\sqrt{6})(n-2 \sqrt{6})}{6}=\left(\frac{\sqrt{6}}{6} n-1\right)\left(\frac{\sqrt{6}}{6} n-2\right)$.因此 $x_{1}>\frac{\sqrt{6}}{6} n$. 故 $C=\frac{\sqrt{6}}{6}$ 时取包含 $x_{1}$ 的所有弧即可.
下证 $C \leq \frac{\sqrt{6}}{6}$.

取充分大的 $n$, 将圆周分为 $n$ 段圆弧, $A_{i}$ 为第 $i$ 段圆弧到第 $i+\left[\frac{\sqrt{6}}{6} n+50\right]$ 段圆弧之并 (第 $i$ 段圆弧 $=$ 第 $n+i$ 段圆弧), 则只要 $i<j<k, i-k \leq\left[\frac{\sqrt{6}}{6} n+50\right]$知 $A_{i} \cap A_{j} \cap A_{k} \neq \varnothing$ 这样的 $(i, j, k)$ 共有至少

$k-i=2$ 时, $n$ 组,

$k-i=3$ 时, $2 n$ 组,

$k-i=\left[\frac{\sqrt{6}}{6} n+50\right]$ 时, $\left[\frac{\sqrt{6}}{6} n+49\right] n$ 组.

至少有

$$
n \times \frac{\left[\frac{\sqrt{6}}{6} n+49\right]\left[\frac{\sqrt{6}}{6} n+50\right]}{2}>\frac{n^{3}}{2 \times 6}>\frac{1}{2} \times \mathrm{C}_{n}^{3}
$$

组, 而对于每一个圆周上的点, 包含其的圆弧数至多有

$$
\left[\frac{\sqrt{6}}{6} n+50\right]+1<\frac{\sqrt{6}}{6} n+100
$$

个, 即 $m \leq \frac{\sqrt{6}}{6} n+100$. 故 $\frac{m}{n} \leq \frac{\sqrt{6}}{6}+\frac{100}{n}, n \rightarrow \infty$ 时, 有若 $c>\frac{\sqrt{6}}{6}, c=\frac{\sqrt{6}}{6}+$ $\varepsilon, \frac{\sqrt{6}}{6}+\varepsilon<\frac{m}{n} \leq \frac{\sqrt{6}}{6}+\frac{100}{n}$, 矛盾.

因此 $c$ 最大值为 $\frac{\sqrt{6}}{6}$.

题 5 数列 $\left\{a_{n}\right\}_{n \geq 1}$ 定义如下: $a_{1}$ 是大于 1 的整数, 对 $n \geq 1, a_{n+1}=a_{n}+$ $P\left(a_{n}\right)$, 其中 $P\left(a_{n}\right)$ 表示 $a_{n}$ 的最大素因子. 证明: 数列 $\left\{a_{n}\right\}_{n \geq 1}$ 中有完全平方数.

证明 若否, 令 $b_{n}=\frac{a_{n}}{p\left(a_{n}\right)}$.

(1) 必存在 $n$ 使得 $p\left(a_{n}\right) \mid b_{n}$. 若否, 取

$$
p\left(a_{n}\right) \times b_{n}, p\left(a_{n+1}\right) \times b_{n+1}, \cdots, p\left(a_{l}\right) \times b_{l},
$$

$l$ 为比 $n$ 大的第一个使得 $p\left(a_{l}\right)$ 与 $p\left(a_{n}\right)$ 不同的数.

若 $b_{l} \geq b_{n}$, 设 $b_{l}=p\left(a_{n}\right) \times t$. 有

$$
b_{n} \leq p\left(a_{n}\right) \times t<p\left(a_{l}\right) \times t
$$

因此 $n \sim l-1$ 中有一个 $n^{\prime}$ 满足 $p\left(a_{n}\right) \mid b_{n^{\prime}}$, 而 $p\left(a_{n^{\prime}}\right)=p\left(a_{n}\right)$, 矛盾.

(2) 令 $c_{n}=\frac{b_{n}}{p\left(a_{n}\right)}$, 取所有 $\left\{c_{n}\right\}$ 整值中最小值, 不妨设为 $c_{i}$, 设 $p\left(a_{i}\right)=p, a_{i}=$ $p^{2} c_{i}$, 考虑比 $i$ 大的第一个 $j$ 满足 $p\left(a_{j}\right) \neq p$, 设为 $q$, 即

$$
p^{2} c_{i} \rightarrow \cdots \rightarrow p q\left(\frac{b_{j}}{p}\right)
$$

(I) 若 $\frac{b_{j}}{p}>c_{i}$, 则 $p q c_{i}$ 一项在 $a_{i} a_{j}$ 之间且最大素因子 $\geq q$, 矛盾.

(II) 若 $\frac{b_{j}}{p}<c_{i}$, 若 $p\left(\frac{b_{j}}{p}\right) \sim p c_{i}$ 中无 $>q$ 素因子, 有

$$
p^{2} c_{i} \rightarrow \cdots \rightarrow p q\left(\frac{b_{j}}{p}\right)=q \times b_{j} \rightarrow \cdots \rightarrow q p c_{i} \rightarrow \cdots \rightarrow q^{2}\left(\frac{b_{j}}{p}\right)
$$

$\frac{b_{j}}{p}<c_{i}$, 与 $c_{i}$ 最小性矛盾. 因此 $p\left(\frac{b_{j}}{p}\right) \sim p c_{i}$ 中存在比 $q$ 大素因子. 设第一个出现的含大于 $q$ 素因子项为 $p_{1} t_{1} q$.

(III) $p q\left(\frac{b_{j}}{p}\right) \rightarrow \cdots \rightarrow q p_{1} t_{1}, t_{1}<c_{1}$, 如(I)知 $t_{1} \leq \frac{b_{j}}{p}$. 若 $q t_{1} \sim q \frac{b_{j}}{p}$ 中无比 $p_{1}$ 大素因子, 同 (II)矛盾. 设 $q t_{1} \sim q \frac{b_{j}}{p}$ 中第一个出现的含大于 $p_{1}$ 素因子的项为 $p_{2} t_{2}$, 且有 $t_{1}<\frac{b_{j}}{p}$. 因此有 $q p_{1} t_{1}=p_{1}(q t) \rightarrow \cdots \rightarrow p_{1} p_{2} t_{2}$, 如 (III)知 $t_{2}<t_{1}$, 同样找到 $p_{1} t_{2} \sim p_{1} t_{1}$ 中第一个出现的含大于 $p_{2}$ 素因子数 $p_{3} t_{3}$. 这样一直找下去可找到 $t_{1}, t_{2}, t_{3}, \cdots$, 由正整数构成的递减数列, 矛盾. 故 $\frac{b_{j}}{p}=c_{i}$ 且

$$
p^{2} c_{i} \rightarrow \cdots \rightarrow p q c_{i}=q\left(p c_{i}\right) \rightarrow \cdots \rightarrow q q c_{i} .
$$

对 $q^{2} c_{i}$ 同样操作, 不妨记

$$
\begin{aligned}
& q^{2} c_{i} \rightarrow \cdots \rightarrow q q_{1} c_{i} \rightarrow \cdots \rightarrow q_{1}^{2} c_{i} \\
& q_{1}^{2} c_{i} \rightarrow \cdots \rightarrow q_{1} q_{2} c_{i} \rightarrow \cdots \rightarrow q_{2}^{2} c_{i}
\end{aligned}
$$

找一个素因子 $u$ 使得 $\left(u, c_{i}\right)=1$ 且 $u>q c_{i}$. 设 $u \in\left(q_{k} c_{i}, q_{k+1} c_{i}\right)$, 但是

$$
q_{k}^{2} c_{i} \rightarrow \cdots \rightarrow q_{k} q_{k+1} c_{i}
$$

中有一项为 $q_{k} u$. 而 $u>q_{k}$, 因此 $u=q_{k+1}$. 则

$$
q_{k} q_{k+1}=q_{k} q_{k+1} c_{i}, c_{i}=1
$$

与 $\left\{a_{n}\right\}$ 中无平方数矛盾.

综上, 命题证毕.

题 6. 是否存在正实数 $a_{0}, a_{1}, \cdots, a_{19}$ 同时满足以下两个条件? 请证明你的结论.

(I) 多项式 $P(x)=x^{20}+a_{19} x^{19}+\cdots+a_{1} x+a_{0}$ 无实根.

(II) 对任意整数 $0 \leq i<j \leq 19$, 交换 $P(x)$ 的 $x^{i}$ 和 $x^{j}$ 的系数所得的多项式均有实根。

解 存在, 理由如下: 取 $b_{18}>b_{16}>\cdots>b_{2}>b_{0}>b_{1}>\cdots>b_{17}>b_{19}$. 令

$$
h(x)=\frac{b_{19}}{x}+\frac{b_{18}}{x^{2}}+\cdots+\frac{b_{1}}{x^{19}}+\frac{b_{0}}{x^{20}}
$$

当 $x \leq-1$ 时, 求导可知 $x$ 极小时 $h^{\prime}(x)<0, x \rightarrow-\infty$ 时 $h(x)<0$. 因此 $x \leq-1$
时 $h(x)$ 有最小值, 设在 $x=x_{0}$ 处取到, 有 $h\left(x_{0}\right)<0$. 令

$$
\begin{aligned}
h_{i, j}(x) & =h(x)+\frac{b_{i}}{x^{20}-j}+\frac{b_{j}}{x^{20}-i}-\frac{b_{i}}{x^{20}-i}-\frac{b_{j}}{x^{20}-j} \\
& =h(x)-\frac{\left(b_{i}-b_{j}\right)\left(x^{i}-x^{j}\right)}{\left(x^{20}-i\right)\left(x^{20}-j\right)} .
\end{aligned}
$$

对于 $x \leq-1$ 的情况, 当 $i$ 为偶, $j$ 为奇时 $b_{i}>b_{j}, x^{i}>x^{j}$.

$i, j$ 均为奇且 $i>j$ 时, $b_{i}<b_{j}, x^{i}<x^{j}$.

$i, j$ 均为偶且 $i>j$ 时, $b_{i}>b_{j}, x^{i}>x^{j}$.

因此任取 $x \leq-1$, 对任意 $i, j \in\{0,1,2, \cdots, 19\}, i \neq j$, 有 $h_{i, j}(x)<h(x)$.令 $c=\max \left\{h_{i, j}\left(x_{0}\right)\right\}$, 则 $c<h\left(x_{0}\right)$. 取 $a_{20}=h\left(x_{0}\right)-\varepsilon$ 满足 $h\left(x_{0}\right)-\varepsilon>c, a_{20}<$ $0, \epsilon>0$. 令

$$
a_{t}=-\frac{b_{t}}{a_{20}}, t \in\{0,1, \cdots, 19\}
$$

则 $a_{t}>0$. 此时

$$
p(x)=-\frac{x^{20}}{a_{20}}\left(\frac{a_{19}}{x}+\frac{a_{18}}{x^{2}}+\cdots+\frac{a_{0}}{x^{20}}-a_{20}\right) .
$$

下证 $p(x)$ 满足条件.

$x \leq-1$ 时,

$$
p(x) \geq \frac{x^{20}}{-a_{20}}\left(h\left(x_{0}\right)-h\left(x_{0}\right)+\varepsilon\right)>0 .
$$

$x \in(-1,0)$ 时,

$$
\begin{aligned}
p(x) & \geq\left(a_{18} x^{18}+a_{19} x^{19}\right)+\cdots+\left(a_{0}+a_{1} x\right) \\
& >\left(a_{18} x^{18}+a_{19} x^{19}\right)+\cdots+\left(a_{0}+a_{0} x\right) \\
& >0 .
\end{aligned}
$$

$x>0$ 时, $p(x)>0$.

因此 $p(x)$ 无根. 而交换 $a_{i}, a_{j}$ 之后, 代入 $x=x_{0}$, 有

$$
x^{20}+x^{20} \times\left(\frac{-1}{a_{20}}\right) \times h_{i, j}\left(x_{0}\right) \leq x^{20} \times \frac{(-1)}{a_{20}} \times\left(-a_{20}+c\right)<0 .
$$

而 $x>0$ 时多项式无上界, 所以交换后多项式必有根, 证毕!

