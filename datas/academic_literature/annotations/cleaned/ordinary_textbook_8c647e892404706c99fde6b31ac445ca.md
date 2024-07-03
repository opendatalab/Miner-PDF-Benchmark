# 第 33 届 CMO 试题解答与评析 

韩新沝叶奇

(浙江省乐清市乐成寄宿中学, 325600)

指导教师: 羊明亮

第 33 届 CMO (中国数学奥林匹克) 于 2017 年 11 月 13 日至 17 日在浙江省杭州市学军中学举行. 作为参赛者, 我们在考试中发挥正常, 取得了较好的成绩. 下面介绍第 33 届 CMO 试题的解, 并对解法进行评析. 不当之处, 恳请读者批评指正.

题 1. 已知素数 $p$ 满足存在 $a, b \in \mathbb{Z}$, 使得 $\frac{a+b}{p}, \frac{a^{n}+b^{n}}{p^{2}}$ 均为整数, 且均与 $p$ 互质. 设 $A_{n}$ 为所有满足以上条件的素数 $p$ 组成的集合, 若 $A_{n}$ 为有限集合, 定义 $f(n)=\left|A_{n}\right|$. 证明:

(1) $A_{n}$ 为有限集合的充分必要条件是 $n \neq 2$;

(2) 若 $k, m$ 为正奇数, $d$ 为 $k, m$ 的最大公约数, 则

$$
f(d) \leq f(k)+f(m)-f(k m) \leq 2 f(d)
$$

证明 (1) 若对素数 $p$ 及正整数 $n$, 有

$$
p^{\alpha} \mid n \text { 且 } p^{\alpha+1} \nmid n,(\alpha \in \mathbb{N}) \text {, }
$$

则记 $p^{\alpha} \| n$ 及 $\nu_{p}(n)=\alpha$.

记 $B_{n}=A_{n} \backslash\{2\}$, 则

$$
A_{n} \text { 为有限集 } \Leftrightarrow B_{n} \text { 为有限集. }
$$

下证: $B_{n}$ 为有限集 $\Leftrightarrow n \neq 2$.

任取 $p \in B_{n}$, 则由 $A_{n}$ 定义及 $B_{n}=A_{n} \backslash\{2\}$ 知 $p$ 为奇素数, 且存在 $a, b \in \mathbb{N}^{*}$,使得 $p \| a+b$ 且 $p^{2} \| a^{n}+b^{n}$.

(a) 当 $n=1$ 时, 有 $p \| a+b$ 且 $p^{2} \| a+b$, 这是矛盾的.

故 $B_{1}=\emptyset$ 为有限集.

收稿日期: 2017-11-29； 修订日期: 2017-12-03.
(b) 当 $n=2$ 时, 有 $p \| a+b$ 且 $p^{2} \| a^{2}+b^{2}$.

对任意奇素数 $p$, 取 $a=b=p$, 则有

$$
p \| 2 p \text { 且 } p^{2} \| 2 p^{2} \text {. }
$$

即 $p \mid a+b$ 且 $p^{2}|| a^{2}+b^{2}$.

故 $p \in B_{2}$ 对任意奇素数 $p$ 成立. 又奇素数无穷多, 故 $B_{2}$ 为无限集.

(c) 当 $n \geq 3$ 时, 有 $p \| a+b$ 且 $p^{2} \| a^{n}+b^{n}$.

若 $p \mid a$, 则也有 $p \mid b$, 从而 $p^{n} \mid a^{n}+b^{n}$. 又注意到 $n \geq 3$, 故 $p^{3} \mid a^{n}+b^{n}$, 这与 $p \| a^{n}+b^{n}$ 矛盾. 故 $p \nmid a$, 同理 $p \nmid b$.

i) 当 $n$ 为奇数时, 由升幂定理 (设 $p$ 为奇素数, $n$ 为正奇数, $p \nmid a, p \nmid b$, $p \mid a+b, a, b \in \mathbb{N}^{*}$, 则 $\left.\nu_{p}\left(a^{n}+b^{n}\right)=\nu_{p}(a+b)+\nu_{p}(n)\right)$ 知

$$
\nu_{p}\left(a^{n}+b^{n}\right)=\nu_{p}(a+b)+\nu_{p}(n),
$$

结合 $\nu_{p}\left(a^{n}+b^{n}\right)=2, \nu_{p}(a+b)=1$ 知 $\nu_{p}(n)=1$, 即 $p \| n$.

又满足 $p \| n$ 的奇素数 $p$ 只有有限多个. 故 $B_{n}$ 为有限集.

ii) 当 $n$ 为偶数时, 设 $n=2 k\left(k \in \mathbb{N}^{*}, k \geq 2\right)$, 则有

$$
p \| a+b \text { 且 } p^{2} \| a^{2 k}+b^{2 k} \text {. }
$$

又 $a+b \mid a^{2 k}-b^{2 k}$, 故 $p \mid a^{2 k}-b^{2 k}$, 则有 $p\left|2 a^{2 k}, p\right| 2 b^{2 k}$.

注意到 $p$ 为奇素数, 故 $p|a, p| b$, 这与 $p \nmid a, p \nmid b$ 矛盾.

故 $B_{n}=\emptyset$ 为有限集.

综上, $B_{n}$ 为有限集 $\Leftrightarrow n \neq 2$, 从而, $A_{n}$ 为有限集 $\Leftrightarrow n \neq 2$.

(2) 由 (1) 中讨论知, 对正奇数 $n, B_{n}$ 即为满足 $\nu_{p}(n)=1$ 的奇素数 $p$ 构成的集合. (因为这对 $n=1$ 时亦成立)

对正奇数 $n$, 若 $2 \in A_{n}$, 则存在 $a, n \in \mathbb{N}^{*}$, 使

$$
2 \| a+b \text { 且 } 2^{2} \| a^{n}+b^{n} .
$$

(a) 当 $n=1$ 时, 有 $2 \| a+b$ 且 $2^{2} \| a+b$, 这是矛盾的.

(b) 当 $n \geq 3$ 时, 由 $2 \| a+b$ 可知 $a, b$ 同奇偶.

i) 若 $a, b$ 均为奇数, 注意到 $n$ 为奇数及 $a^{2} \equiv b^{2} \equiv 1(\bmod 4)$, 故

$$
a^{n}+b^{n} \equiv a+b \quad(\bmod 4)
$$

这与 $2 \| a+b$ 且 $2^{2} \| a^{n}+b^{n}$ 矛盾.

ii) 若 $a, b$ 均为偶数, 则 $8 \mid a^{n}+b^{n}$,与 $2^{2} \| a^{n}+b^{n}$ 矛盾.

故 $2 \notin A_{n}$. 从而, 对正奇数 $n$, 有

$$
A_{n}=B_{n}=\left\{p \mid p \text { 为奇素数, } \nu_{p}(n)=1\right\} .
$$

对正奇数 $k, m$, 按右图定义 $c_{1}, \cdots, c_{8}$ (例如, $c_{5}=\left\{p \mid p\right.$ 为奇素数, $\nu_{p}(m) \geq 2$, $\left.\left.\nu_{p}(k)=1\right\}\right)$, 则 $c_{1}, \cdots, c_{8}$ 构成 $m k$ 素因子的一个分划.

依定义，易有

$$
\begin{aligned}
f(m) & =\left|c_{1}\right|+\left|c_{4}\right|+\left|c_{7}\right|, \\
f(k) & =\left|c_{3}\right|+\left|c_{4}\right|+\left|c_{5}\right|, \\
f(m k) & =\left|c_{1}\right|+\left|c_{3}\right|, \\
f(d) & =\left|c_{4}\right|+\left|c_{5}\right|+\left|c_{7}\right|,
\end{aligned}
$$

| $v_{p}(k)$ | 0 | 1 | $\geq 2$ |
| :---: | :---: | :---: | :---: |
| 0 |  | $c_{1}$ | $c_{2}$ |
| 1 | $c_{3}$ | $c_{4}$ | $c_{5}$ |
| $\geq 2$ | $c_{6}$ | $c_{7}$ | $c_{8}$ |

故

$$
\begin{aligned}
& f(d) \leq f(m)+f(k)-f(m k) \leq 2 f(d) \\
\Leftrightarrow & \left|c_{4}\right|+\left|c_{5}\right|+\left|c_{7}\right| \leq 2\left|c_{4}\right|+\left|c_{5}\right|+\left|c_{7}\right| \leq 2\left(\left|c_{4}\right|+\left|c_{5}\right|+\left|c_{7}\right|\right)
\end{aligned}
$$

上式成立, 故原不等式成立.

评注 此题需刻画出 $A_{n}$. 由于 $n$ 在幂次中出现, 故可采用升幂定理确定 $p$与 $n$ 的关系. (2) 中需对 $k, m$ 的素因子按幂次分类, 要分为 0 次, 1 次, 和大于等于 2 次, Venn 图的表示手法使表达较为清晰, 值得借鉴.

题 2. 设 $T=\{(x, y, z) \mid 1 \leq x, y, z \leq n, x, y, z \in \mathbb{N}\}$. 将 $T$ 中 $3 n^{2}-3 n+k+1$, $k \in \mathbb{N}^{*}$ 个点染红, 且对于任意染红的两点 $P, Q$ 满足: 若线段 $P Q$ 平行于坐标轴,则线段 $P Q$ 上的点皆染为红色. 求证: 存在至少 $k$ 个单位立方体, 其 8 个顶点均为红色

证明 我们依次从一维, 二维, 三维的角度进行考虑:

(1) 对于给定的 $y, z$, 考虑点集 $\{(x, y, z) \mid 1 \leq x \leq n, x \in \mathbb{N}\}$, 设该点集中共有 $a$ 个红点 $(a \in \mathbb{N})$, 因为这个点集中的所有点均在一条与 $x$ 轴平行的直线上,又由条件, 对该点集中任意两个红点, 以它们为端点的线段上的所有整点均为红色的, 于是, 可知这 $a$ 个红点的横坐标为连续整数, 则有至少 $a-1$ 条以红点为端点的单位线段 (当 $a=0$ 时不取等).

(2) 对于给定的 $z$, 考虑点集 $\{(x, y, z) \mid 1 \leq x, y \leq n, x, y \in \mathbb{N}\}$, 设该点集中共有 $b$ 个红点, 其中纵坐标为 $i$ 的红点共有 $a_{i}$ 个 $(1 \leq i \leq n)\left(b \in \mathbb{N}, a_{i} \in \mathbb{N}\right)$. 则有 $b=\sum_{i=1}^{n} a_{i}$.

考虑点集中纵坐标为 $i$ 的点, 由 (1) 知, 它们可产生至少 $a_{i}-1$ 条以红点为
端点, 纵坐标为 $i$ 的, 与 $x$ 轴平行的单位线段, 故共可产生至少 $\sum_{i=1}^{n}\left(a_{i}-1\right)=b-n$条以红点为端点, 与 $x$ 轴平行的单位线段.

将这些单位线段按照两端点的横坐标中较小的那个值分类, 共有 $n-1$ 类,设第 $i$ 类有 $t_{i}$ 条这样的线段 $(1 \leq i \leq n-1)\left(t_{i} \in \mathbb{N}\right)$, 则有 $\sum_{i=1}^{n-1} t_{i} \geq b-n$.

对于同一类, 任取其中两条线段, 设为 $A_{1} B_{1}$ 与 $A_{2} B_{2}$, 且不妨设 $A_{1}, A_{2}$ 横坐标相同, $B_{1}, B_{2}$ 横坐标相同.

由条件知线段 $A_{1} A_{2}, B_{1} B_{2}$ 上的格点均为红点. 于是可知同一类线段的纵坐标连续, 从而第 $i$ 类可产生至少 $t_{i}-1$ 个以红点为顶点, 与平面 $x o y$ 平行的单位正方形, $i=1, \cdots, n-1$.

而对不同类的线段, 产生的单位正方形的顶点横坐标中最小的那个值不同, 从而这些正方形互不相同, 故共可产生至少 $\sum_{i=1}^{n-1}\left(t_{i}-1\right) \geq b-n-(n-1)=$ $b-(2 n-1)$ 个以红点为顶点, 与平面 $x o y$ 平行的单位正方形.

(3) 考虑点集 $\{(x, y, z) \mid 1 \leq x, y, z \leq n, x, y, z \in \mathbb{N}\}$, 设 $T$ 中 $z$ 轴方向上坐标为 $i$ 的红点有 $b_{i}$ 个 $(1 \leq i \leq n)\left(b_{i} \in \mathbb{N}\right)$, 则有 $\sum_{i=1}^{n} b_{i}=3 n^{2}-3 n+k+1$.

考虑 $T$ 中 $z$ 轴方向上坐标为 $i$ 的点, 由 $(2)$ 知, 它们可产生至少 $b_{i}-(2 n-1)$个以红点为顶点, $z$ 轴方向上坐标为 $i$ 的, 与 $x o y$ 平行的单位正方形, 故共可产生至少 $\sum_{i=1}^{n}\left(b_{i}-(2 n-1)\right)=3 n^{2}-3 n+1+k-n(2 n-1)=n^{2}-2 n+1+k$ 个以红点为顶点, 与平面 $x o y$ 平行的单位正方形.

我们将这些正方形按照其顶点的横坐标的最小值及纵坐标的最小值分为 $(n-1)^{2}$ 类, 设第 $i$ 类有 $s_{i}$ 个这样的单位正方形 $\left(1 \leq i \leq(n-1)^{2}\right)\left(s_{i} \in \mathbb{N}\right)$. 则有 $\sum_{i=1}^{(n-1)^{2}} s_{i} \geq(n-1)^{2}+k$.

类似于 (2) 中讨论, 可知第 $i$ 类的正方形可产生至少 $s_{i}-1$ 个以红点为顶点的单位立方体, 且这些立方体互不相同.

故共可产生至少 $\sum_{i=1}^{(n-1)^{2}}\left(s_{i}-1\right) \geq(n-1)^{2}+k-(n-1)^{2}=k$ 个以红点为顶点的单位立方体. 证毕.

评注 上述解法思路自然清晰, 从低维向高维扩展, 每次扩展的本质也一样,故难度不大. 但由简单情况入手的想法值得借鉴, 某种程度上, 简单情况往往反映了一般情况的本质.

题 3. 已知正整数 $q$ 不是完全立方数, 证明：存在 $c \in \mathbb{R}_{+}$使得

$$
\{n \sqrt[3]{q}\}+\left\{n \sqrt[3]{q^{2}}\right\} \geq c \cdot \frac{1}{\sqrt{n}}
$$

对所有的正整数 $n$ 成立, 其中 $\{\lambda\}, \lambda \in \mathbb{R}$ 表示 $\lambda$ 的小数部分.

证法一 设 $[n \sqrt[3]{q}]=k_{1},\left[n \sqrt[3]{q^{2}}\right]=k_{2},\{n \sqrt[3]{q}\}=\varepsilon_{1},\left\{n \sqrt[3]{q^{2}}\right\}=\varepsilon_{2}\left(k_{1}, k_{2} \in\right.$ $\mathbb{N}^{*}, 0<\varepsilon_{1}<1,0<\varepsilon_{2}<1$. 对某一给定的 $n$ ) (用到 $q$ 不为完全立方数).

我们证明:

$$
\varepsilon_{1}+\varepsilon_{2} \geq \frac{1}{\sqrt{3} \sqrt{q^{\frac{2}{3}}+q^{\frac{4}{3}}}} \cdot \frac{1}{\sqrt{n}}
$$

记 $x=k_{1} n \sqrt[3]{q^{2}}, y=k_{2} n \sqrt[3]{q}, z=q n^{2}$, 注意到有恒等式

$$
(x+y+z)\left(x^{2}+y^{2}+z^{2}-x y-y z-z x\right)=x^{3}+y^{3}+z^{3}-3 x y z .
$$

且.

$$
\begin{aligned}
x+y+z & =k_{1} n \sqrt[3]{q^{2}}+k_{2} n \sqrt[3]{q}+q n^{2} \\
& <q^{\frac{1}{2}} n \cdot n q^{\frac{2}{3}}+q^{\frac{2}{3}} n \cdot n q^{\frac{1}{3}}+q n^{2}=3 q n^{2}
\end{aligned}
$$

又

$$
\begin{aligned}
& x^{2}+y^{2}+z^{2}-x y-y z-z x=\frac{1}{2}\left((x-y)^{2}+(y-z)^{2}+(z-x)^{2}\right) \\
= & \frac{1}{2}\left(\left(k_{1} n \sqrt[3]{q^{2}}-k_{2} n \sqrt[3]{q}\right)^{2}+\left(k_{2} n \sqrt[3]{q}-q n^{2}\right)^{2}+\left(k_{1} n \sqrt[3]{q^{2}}-q n^{2}\right)^{2}\right) \\
= & \frac{1}{2}\left(\left(k_{1}\left(k_{2}+\varepsilon_{2}\right)-k_{2}\left(k_{1}+\varepsilon_{1}\right)\right)^{2}+\left(n q^{\frac{1}{3}}\left(k_{2}-q^{\frac{2}{3}} n\right)\right)^{2}+\left(n q^{\frac{2}{3}}\left(k_{1}-q^{\frac{1}{3}} n\right)\right)^{2}\right) \\
= & \frac{1}{2}\left(\left(k_{1} \varepsilon_{2}-k_{2} \varepsilon_{1}\right)^{2}+n^{2} q^{\frac{2}{3}} \varepsilon_{2}^{2}+n^{2} q^{\frac{4}{3}} \varepsilon_{1}^{2}\right) \\
< & \frac{1}{2}\left(k_{1}^{2}+\left(q^{\frac{1}{3}} n\right)^{2}\right) \varepsilon_{2}^{2}+\left(k_{2}^{2}+\left(q^{\frac{2}{3}} n\right)^{2} \varepsilon_{1}^{2}\right) \quad\left(k_{1} k_{2} \varepsilon_{1} \varepsilon_{2}>0\right) \\
< & \left(q^{\frac{1}{3}} n\right)^{2} \varepsilon_{2}^{2}+\left(q^{\frac{2}{3}} n\right)^{2} \varepsilon_{1}^{2} \quad\left(k_{1}<q^{\frac{1}{3}} n, k_{2}<q^{\frac{2}{3}} n\right) \\
< & \left(q^{\frac{2}{3}}+q^{\frac{4}{3}}\right) n^{2}\left(\varepsilon_{1}+\varepsilon_{2}\right)^{2},
\end{aligned}
$$

以及

$$
\begin{aligned}
x^{3}+y^{3}+z^{3}-3 x y z & =k_{1}^{3} n^{3} q^{2}+k_{2}^{3} n^{3} q+q^{3} n^{6}-3 k_{1} k_{2} q^{2} n^{4} \\
& =q n^{3}\left(k_{1}^{3} q+k_{2}^{3}+q^{2} n^{3}-3 k_{1} k_{2} q n\right) \\
& \geq q n^{3}
\end{aligned}
$$

(注意到由 $A-G$ 不等式:

$$
k_{1}^{3} q+k_{2}^{3}+q^{2} n^{3} \geq 3 \sqrt[3]{k_{1}^{3} q \cdot k_{2}^{3} \cdot q^{2} n^{3}}=3 k_{1} k_{2} q n,
$$

又 $0<\varepsilon_{2}<1$, 故 $k_{2}<q^{\frac{2}{3}} n$, 故 $k_{2} \neq q^{\frac{2}{3}} n$, 等号取不到, 即 $k_{1}^{3} q+k_{2}^{3}+q^{2} n^{3}>$ $3 k_{1} k_{2} q n$. 又 $3 k_{1} k_{2} q n, k_{1}^{3} q+k_{2}^{3}+q^{2} n^{3} \in \mathbb{N}^{*}$, 故由整数的离散性: $k_{1}^{3} q+k_{2}^{3}+q^{2} n^{3}-$
$3 k_{1} k_{2} q n \geq 1$.)

将 $(1)(2)(3)$ 代入 $(*)$ 得:

$$
3 q n^{2}\left(q^{\frac{2}{3}}+q^{\frac{4}{3}}\right) n^{2}\left(\varepsilon_{1}+\varepsilon_{2}\right)^{2}>q n^{3} .
$$

故

$$
\varepsilon_{1}+\varepsilon_{2}>\frac{1}{\sqrt{3} \sqrt{q^{\frac{2}{3}}+q^{\frac{4}{3}}}} \cdot \frac{1}{\sqrt{n}} .
$$

(菓) 获证!

那么由 $(*)$, 取 $c=\frac{1}{\sqrt{3} \sqrt{q^{\frac{2}{3}}+q^{\frac{4}{3}}}}$, 则对任给的 $n \in \mathbb{N}^{*}$,

$$
\{n \sqrt[3]{q}\}+\left\{n \sqrt[3]{q^{2}}\right\} \geq c \cdot \frac{1}{\sqrt{n}}
$$

故存在满足条件的 $c$. 原命题获证!

证法二 取 $c=\frac{q^{-\frac{11}{6}}}{3}$. 我们证明: 对任意的正整数 $n$,

$$
\left\{q^{\frac{1}{3}} n\right\}+\left\{q^{\frac{2}{3}} n\right\} \geq \frac{q^{-\frac{11}{6}}}{3} \cdot \frac{1}{\sqrt{n}} .
$$

对给定的正整数 $n$, 记 $a=\left[n q^{\frac{1}{3}}\right], b=\left[n q^{\frac{2}{3}}\right]$, 则 $a<n q^{\frac{1}{3}}, b<n q^{\frac{2}{3}}$ (用到 $q$ 非完全立方数). 那么

$$
\left\{n q^{\frac{1}{3}}\right\}=n q^{\frac{1}{3}}-a=\frac{q n^{3}-a^{3}}{\left(n q^{\frac{1}{3}}\right)^{2}+n q^{\frac{1}{3}} a+a^{2}}>\frac{q n^{3}-a^{3}}{3 n^{2} q^{\frac{2}{3}}}>\frac{q n^{3}-a^{3}}{3 n^{2} q^{\frac{4}{3}}},
$$

$\left\{n q^{\frac{2}{3}}\right\}=n q^{\frac{2}{3}}-b=\frac{q^{2} n^{3}-b^{3}}{\left(n q^{\frac{2}{3}}\right)^{2}+n q^{\frac{2}{3}} b+b^{2}}>\frac{q^{2} n^{3}-b^{3}}{3 n^{2} q^{\frac{4}{3}}}, \quad$ (用到 $a<n q^{\frac{1}{3}}, b<n q^{\frac{2}{3}}$ )

故有

$$
\left\{n q^{\frac{1}{3}}\right\}+\left\{n q^{\frac{2}{3}}\right\}>\frac{q n^{3}+q^{2} n^{3}-a^{3}-b^{3}}{3 n^{2} q^{\frac{4}{3}}} .
$$

下面我们记 $x=n^{3} q-a^{3}, y=n^{3} q^{2}-b^{3}$. 我们证明

$$
y+q x \geq\left(q n^{3}\right)^{\frac{1}{2}}
$$

由 $x=n^{3} q-a^{3}, y=n^{3} q^{2}-b^{3}$ 知

$$
a^{3} b^{3}=\left(n^{3} q-x\right)\left(n^{3} q^{2}-y\right)=n^{6} q^{3}+x y-n^{3} q(y+q x) .
$$

下面分两种情况讨论:

(1) 若 $a b \geq n^{2} q-\frac{y+q x}{3 n q}$. 则

$$
n^{6} q^{3}+x y-n^{3} q(y+q x) \geq\left(n^{2} q-\frac{y+q x}{3 n q}\right)^{3},
$$

故

$$
x y \geq \frac{(y+q x)^{2}}{3 q}-\left(\frac{y+q x}{3 n q}\right)^{3}
$$

又由 $A-G$ 不等式有

$$
x y=\frac{1}{q} \cdot y \cdot q x \leq \frac{1}{q} \cdot \frac{(y+q x)^{2}}{4}
$$

故有

$$
\left(\frac{y+q x}{3 n q}\right)^{3} \geq \frac{(y+q x)^{2}}{12 q},
$$

即

$$
y+q x>\frac{9}{4} n^{3} q^{2}
$$

故有

$$
y+q x \geq \frac{9}{4} n^{3} q^{2}>(q n)^{\frac{3}{2}},
$$

即

$$
y+q x>q^{\frac{1}{2}} n^{\frac{3}{2}} .
$$

(*) 证毕!

(2) 若 $a b<n^{2} q-\frac{y+q x}{3 n q}$, 则

$$
a b \leq n^{2} q-\frac{y+q x+1}{3 n q}, \quad \text { (用到 } a, b \in \mathbb{N}^{*}, q n \in \mathbb{N}^{*} \text { ) }
$$

故

$$
n^{6} q^{3}+x y-n^{3} q(y+q x) \leq\left(n^{2} q-\frac{y+q x+1}{3 n q}\right)^{3}
$$

即

$$
x y+n^{3} q \leq \frac{(y+q x+1)^{2}}{3 q}-\left(\frac{y+q x+1}{3 n q}\right)^{3} .
$$

故

$$
\begin{gathered}
n^{3} q \leq \frac{(y+q x+1)^{2}}{3 q} \leq(y+q x)^{2}, \\
\left(y+q x \geq 1+q\left(x, y \in N^{*}\right), \text { 故 } y+q x \geq 2, \text { 故 } \frac{(y+q x+1)^{2}}{3} \leq(y+q x)^{2}\right)
\end{gathered}
$$

即有

$$
y+q x \geq\left(q n^{3}\right)^{\frac{1}{2}}
$$

(*) 证毕!

综合 (1)(2) 知, $y+q x \geq\left(q n^{3}\right)^{\frac{1}{2}}$.
那么代入 $(*)$ 有:

$$
\left\{n q^{\frac{1}{3}}\right\}+\left\{n q^{\frac{2}{3}}\right\}>\frac{q x+q y}{3 n^{2} \cdot q^{\frac{7}{3}}}>\frac{y+q x}{3 n^{2} \cdot q^{\frac{7}{3}}}>\frac{q^{\frac{1}{2}} \cdot n^{\frac{3}{2}}}{3 n^{2} \cdot q^{\frac{7}{3}}}=\frac{q^{-\frac{11}{6}}}{3} \cdot \frac{1}{\sqrt{n}},
$$

即

$$
\left\{n q^{\frac{1}{3}}\right\}+\left\{n q^{\frac{2}{3}}\right\}>\frac{q^{-\frac{11}{6}}}{3} \cdot \frac{1}{\sqrt{n}}
$$

故 $c$ 满足要求!

综上: 存在满足要求的 $c$, 原命题获证!

评注 此题的难度较大, 但若熟悉 $\{\sqrt{\alpha} n\} \geq \frac{c}{n}$ ( $d$ 为非完全平方数, $c$ 为正常数) 一类问题的证明, 似乎思路较为自然, 关键在于利用整数离散性上, 为此必须想方设法使 $n q^{\frac{1}{3}}$ 与 $n q^{\frac{2}{3}}$ 乘立方, 那么我们有如下两个恒等式:

(1) $a^{3}+b^{3}+c^{3}-3 a b c=(a+b+c)\left(a^{2}+b^{2}+c^{2}-a b-b c-c a\right)$

(2) $a^{3}+b^{3}=(a+b)\left(a^{2}-a b+b^{2}\right)$ 或 $a^{3}-b^{3}=(a-b)\left(a^{2}+a b+b^{2}\right)$

证 1 考虑到 $\left\{q^{\frac{1}{3}} n\right\}+\left\{q^{\frac{2}{3}} n\right\}$ 可能趋向于 0 , 因此我们选择式 (1), 并先提取左侧公因式, 再利用离散性, 提高了次数, 恰到好处的放出了 $-\frac{1}{2}$ 次.

证 2 考虑了单项的式 (2), 因而需证关于整体性质的 (*) 式, 在证明过程中体现了 “削足适履” 的思想.

题 4. 已知圆内接四边形 $A B C D$, 其对角线 $A C$ 与 $B D$ 交于点 $P, \triangle A D P$的外接圆交 $A B$ 于 $E, \triangle B C P$ 的外接圆交 $A B$ 于 $F$, 设 $\triangle A D E$ 与 $\triangle B C F$ 的内心分别为 $I, J$, 连接直线 $I J$ 交 $A C$ 于 $K$. 求证: $A, I, K, E$ 四点共圆.


证明 延长 $E I$ 交 $\triangle A D P$ 外接圆于 $S$, 延长 $F J$ 交 $\triangle B C P$ 外接圆于 $T$.

下证: (1) $S, P, T$ 三点共线; (2) $I J / / S T$; (3) $A, I, K, E$ 四点共圆.

对 (1): 因为 $I$ 是 $\triangle A D E$ 内心, 所以 $S$ 是 $\overparen{A D}$ 中点.

从而 $\angle D P S=\angle A P S=\frac{1}{2} \angle D P A$.

同理 $\angle C P T=\angle B P T=\frac{1}{2} \angle B P C$.

注意到 $\angle D P A=\angle B P C$, 故 $\angle D P S=\angle B P T$. 即 $S, P, T$ 三点共线.
对 (2): 要证 $I J / / S T$, 只需证点 $I$ 到 $S T$ 的距离等于点 $J$ 到 $S T$ 的距离, 即 $I S \cdot \sin \angle P S E=J T \cdot \sin \angle P T F$. 由

$$
\angle S D A=\angle S A D=\frac{1}{2} \angle D P A=\frac{1}{2} \angle C P B=\angle T C B=\angle T B C,
$$

知 $\triangle A S D \sim \triangle B T C$; 由 $\angle A D P=\angle B C P, \angle D P A=\angle C P B$ 知 $\triangle A D P \backsim$ $\triangle B C P ;$ 由鸡爪定理知 $I S=A S, J T=B T$. 故

$$
\frac{I S}{J T}=\frac{A S}{B T}=\frac{A D}{B C}=\frac{A P}{B P}=\frac{\sin \angle P B A}{\sin \angle P A B}=\frac{\sin \angle P T F}{\sin \angle P S E},
$$

即

$$
I S \cdot \sin \angle P S E=J T \cdot \sin \angle P T F,
$$

从而 $I J / / S T$.

对 (3): 因为 $\angle I K A=\angle S P A=\angle S E A=\angle I E A$, 所以 $A, I, K, E$ 四点共圆.证毕.

评注 本题解法较多, 这里列出了一种思路比较自然的做法. 通过简单导角可知命题等价于 $I J / / S T$, 转而计算点 $I, J$ 到直线 $S T$ 的距离, 再结合内心性质即可.

题 5. 设 $n \geq 3, n$ 为奇数, 对 $n \times n$ 的方格表进行黑白染色, 若两个方格 $a, b$有公共顶点且同色, 则称 $a, b$ 两个方格相邻. 若方格 $a, b$ 能通过一系列的方格 $c_{1} \rightarrow c_{2} \rightarrow \cdots \rightarrow c_{k}$, 其中 $c_{1}=a, c_{k}=b$, 且 $c_{i}$ 与 $c_{i+1}$ 相邻, 则 $a, b$ 称为连通. 求最大的正整数 $M$, 使得存在 $M$ 个方格, 使得两两不连通.

解法一 所求 $M$ 的最大值为 $\frac{(n+1)^{2}}{4}+1$.

一方面, 我们说明 $M=\frac{(n+1)^{2}}{4}+1$ 满足要求.

如右图, 对奇数行且奇数列的方格染黑, 其余方格染白, 取出所有黑格及任意一个白格, 这些方格互不连通,此时, 共有 $\frac{(n+1)^{2}}{4}+1$ 个方格.

另一方面, 我们证明: $M \leq \frac{(n+1)^{2}}{4}+1$.

我们可将所有方格分成一些类, 使得对任意两个方


格, 它们在同一类当且仅当它们连通, 对每一类, 我们称其为一个连通分支, 并设共有 $m$ 个连通分支.

对第 $i$ 列第 $j$ 行的格点, 我们记其坐标为 $(i, j)(1 \leq i, j \leq n+1)$.

对每个连通分支 $A$, 我们取其所含方格的顶点中 $x+y$ 最大, $x+y$ 最小,
$x-y$ 最大, $y-x$ 最大 ( $x, y$ 分别表示点的横, 纵坐标) 的各一点, 且尽量不取处于方格表边界的格点 (即若有两点均为 $x+y$ 有最大, 其中一个在方格表边界,一个不在方格表边界, 则取不在方格表边界的那个点. 另三种情况, $x+y$ 最小, $x-y$ 最大, $y-x$ 最大同理), 则易知取出的四个点互不相同.

则对由 $A$ 选出的格点 $a$. 以 $a$ 为顶点的另三个 (可能小于三个) 在 $A$ 外的方格均与 $A$ 异色, 由上述结论知, 处于方格表内部的格点至多被一个连通分支对应. (否则, 若 $a$ 分别被 $A$ 与 $B$ 对应, 则以 $a$ 为顶点的四个方格一个与 $A$ 同色,三个与 $A$ 异色, 且一个与 $B$ 同色, 三个与 $B$ 异色, 则 $A, B$ 同色, 而它们有公共顶点, 与 $A, B$ 为不同连通分支矛盾.)

下考虑处于方格表边界的格点, 若其被两个不同连通分支对应, 如图, 设点 $a$ 被连通分支 $A, B$ 对应, 不妨设 $1 \in A, 2 \in B$ (用数字代表对应方格).

(1) 若 $3 \in A$ 且 $4 \in B$,则 $b$ 不会被任意连通分支对应, 设这种情况的 $a$ 共有 $t$ 个, 故可对应 $t$ 个 $b$ (可能相同).

注意到 1,3 同色及 2,4 同色, 及 $n \geq 3$, 所以 $a_{1}, a_{2}, a_{3}$均不为这种情况的 $a$, 故 $b$ 不可能由别的 $a$ 对应, 于是不同 $a$ 对应不同 $b$, 故至少有 $t$ 个点没被取出过.



(2) 若 $4 \in A$ 或 $3 \in B$, 不妨设 $4 \in A$, 则 $a, c$ 均为 $A$所含方格的顶点, 又由 $a$ 被取出及之前取法中的 “尽量不取处于方格表边界的格点” 知 $c$ 也在方格表边界, 则 $d$ 为方格表角落的顶点.

又注意到 $c$ 不会被取出两次, 故对每个方格表角落的


顶点, 至多对应一个这种情况的顶点 $a$, 从而至多有四个这样的 $a$.

因此, 取出的格点数 (包括重复) 至多 $(n+1)^{2}+t-t+4=(n+1)^{2}+4$ 个,又注意到共取了 $4 m$ 个格点 (包括重复), 故 $4 m \leq(n+1)^{2}+4$, 即

$$
m \leq\left(\frac{n+1}{2}\right)^{2}+1
$$

考虑取出的 $M$ 个方格, 因为它们两两不连通, 所以它们属于互不相同的连通分支, 故

$$
M \leq m \leq\left(\frac{n+1}{2}\right)^{2}+1
$$

综上, $M_{\max }=\left(\frac{n+1}{2}\right)^{2}+1$.

解法二 (黄哲宇) 答案与构造同解 1.

下面, 我们证明: $M \leq \frac{(n+1)^{2}}{4}+1$.
我们可将所有方格分成一些类, 使得对任意两个方格, 它们在同一类中当且仅当它们连通, 对上述每一类方格, 我们称其为一个块, 并设共 $s$ 个块, 其中, 白块为 $k_{1}, \cdots, k_{t}$, 黑块为 $k_{t+1}, \cdots, k_{s}(s \geq t)$.

定义两个块 $A, B$ 相邻当且仅当存在 $A$ 中一个方格与 $B$ 中一个方格有公共顶点.

构造图 $G, s$ 个顶点分别对应 $k_{1}, \cdots, k_{s}$, 两点连边当且仅当对应的两块相邻.

注意到对任意两个方格 $a, b$, 存在一系列方格 $c_{1} \rightarrow c_{2} \rightarrow \cdots \rightarrow c_{k}$, 其中 $c_{1}=a, c_{k}=b$, 且 $c_{i}$ 与 $c_{i+1}$ 有公共顶点, 所以 $G$ 连通, 于是有

边数 $E \geq s-1$.

下面证明: 若一黑块 $A$ 与一白块 $B$ 相邻, 则 $A$ 与 $B$ 至少有 4 个公共顶点,或 $A$ 与 $B$ 恰有 3 个公共顶点, 且有一块恰含一个小方格且占据方格表的一个角落.

由定义知, 存在 $A$ 中一方格与 $B$ 中一方格有公共顶点, 考虑以该公共顶点为顶点的 4 个或 2 个方格, 它们必在 $A$ 或 $B$ 中, 又由于其中有两个方格异色,故必有两个有公共边的方格异色, 如图, 不妨设 $a \in A, b \in B$.

由 $n \geq 3$ 可不妨设 $a, b$ 所在行的下方还有行, 如图, 若 $c \in A, d \in A$, 分下列两种情况:

若 $b$ 上方和右方均无方格, 则即为 $(*)$ 后者的情况.

若 $b$ 上方或右方有方格, 不妨设上方有方格, 如图,

对 $e \in A, f \in A ; e \in A, f \in B ; e \in B, f \in A ; e \in B$, $f \in B$, 均有 $(*)$ 前者成立.

若 $c \in A, d \in B$, 由 $n \geq 3$, 可不妨设 $a, b$ 所在行上方还有行, 如图, 对 $e \in A, f \in A ; e \in A, f \in B ; e \in B, f \in A$; $e \in B, f \in B$, 均有 $(*)$ 前者成立.


若 $c \in B, d \in A$, 则已有 $(*)$ 前者成立.

若 $c \in B, d \in B$, 同 $c \in A, d \in A$ 知 $(*)$ 成立.

故 $(*)$ 获证.

于是, 由 $(*)$ 知, 对相邻的一黑块与一白块, 若为 $(*)$ 前者, 则其可对应黑块与白块的 4 个不同公共顶点; 若为 $(*)$ 后者, 则其可对应黑块与白块的 3 个不同公共顶点及方格表角落的一个顶点.

又因为每个点至多属于一个黑块, 也至多属于一个白块, 且对一个仅含一个
方格且占据方格表一个角落的块, 与其相邻的异色块至多一个, 所以, 上述对应中的顶点集互不相交, 故

$$
4 E \leq(n+1)^{2} .
$$

注意到取出的 $M$ 个方格互不连通, 故它们属于互不相同的块, 于是.

$$
M \leq s
$$

结合 (1), (2), (3) 即知

$$
M \leq \frac{(n+1)^{2}}{4}+1
$$

综上, $M_{\max }=\frac{(n+1)^{2}}{4}+1$.

评注 本题答案不难猜出是 $\frac{(n+1)^{2}}{4}+1$. 从答案中就可以看出本题的方向是找 1 对 4 的映射, 难点主要在于如何产生这个 +1 . 解 1 直接构造连通分支到顶点集的映射, 用一些点被取两次的特例产生 +1 . 解 2 由乐成寄宿中学的黄哲宇同学给出. 这个解法中产生 +1 的想法更加明智, 联系到了连通图中的 $\nu \leq e+1$. 之后转而对 $e$ 分析, 构造映射.

此题中有条件 $n$ 为奇数, 自然会让人去联想 $n$ 为偶数的情况, 不过这比较困难, 留给读者思考.

题 6. 给定 $n, k \in \mathbb{N}^{*}(n>k), a_{1}, a_{2}, \cdots, a_{n} \in(k-1, k)$. 若正实数 $x_{1}, x_{2}, \cdots, x_{n}$ 满足: 对任意的集合 $I \subseteq\{1,2, \cdots, n\},|I|=k$, 有

$$
\sum_{i \in I} x_{i} \leq \sum_{i \in I} a_{i}
$$

试求 $x_{1} x_{2} \cdots x_{n}$ 的最大值.

解 $x_{1} x_{2} \cdots x_{n}$ 的最大值为 $a_{1} a_{2} \cdots a_{n}$.

一方面, 当 $x_{i}=a_{i}, i=1,2, \cdots, n$ 时, 对任意集合 $I \subseteq\{1,2, \cdots, n\},|I|=$ $k$, 有

$$
\sum_{i \in I} x_{i} \leq \sum_{i \in I} a_{i}
$$

此时, $x_{1} x_{2} \cdots x_{n}=a_{1} a_{2} \cdots a_{n}$.

另一方面, 我们证明: $x_{1} x_{2} \cdots x_{n} \leq a_{1} a_{2} \cdots a_{n}$.

当 $n=k+1$ 时, 记

$$
S=\left\{i \mid x_{i}>a_{i}, 1 \leq i \leq n\right\}, \quad T=\left\{i \mid x_{i} \leq a_{i}, 1 \leq i \leq n\right\}
$$

$$
A=\sum_{i \in S}\left(x_{i}-a_{i}\right), \quad B=\sum_{i \in T}\left(a_{i}-x_{i}\right) . \quad\left(\text { 规定 } \sum_{x \in \emptyset} x=0\right)
$$

若 $S=\emptyset$, 则对任意 $1 \leq i \leq n$, 有 $x_{i} \leq a_{i}$. 从而

$$
x_{1} x_{2} \cdots x_{n} \leq a_{1} a_{2} \cdots a_{n}
$$

结论成立!

下设 $S \neq \emptyset$, 则 $|T| \leq k, k \geq 2$.

由 $n=k+1$ 及题设条件知对任意 $1 \leq j \leq n$, 有:

从而

$$
\sum_{i \neq j} x_{i} \leq \sum_{i \neq j} a_{i}
$$

$$
a_{j}-x_{j} \leq a_{j}-x_{j}+\sum_{i \neq j}\left(a_{i}-x_{i}\right)=\sum_{i=1}^{n}\left(a_{i}-x_{i}\right)=B-A .
$$

对 $j \in T$ 求和有:

$$
B \leq|T|(B-A)
$$

从而

$$
\frac{A}{B} \leq \frac{|T|-1}{|T|} \leq \frac{k-1}{k}, \quad(|T| \leq k)
$$

即

$$
\frac{A}{k-1} \leq \frac{B}{k}
$$

故

$$
\begin{aligned}
\sum_{i=1}^{n} \frac{x_{i}-a_{i}}{a_{i}} & =\sum_{i \in S} \frac{x_{i}-a_{i}}{a_{i}}-\sum_{i \in T} \frac{a_{i}-x_{i}}{a_{i}} \\
& \leq \sum_{i \in S} \frac{x_{i}-a_{i}}{k-1}-\sum_{i \in T} \frac{a_{i}-x_{i}}{k} \quad\left(a_{i} \in(k-1, k)\right) \\
& =\frac{A}{k-1}-\frac{B}{k} \leq 0
\end{aligned}
$$

从而

$$
\sum_{i=1}^{n} \frac{x_{i}}{a_{i}} \leq n
$$

由均值不等式知:

$$
\sum_{i=1}^{n} \frac{x_{i}}{a_{i}} \geq n \cdot\left(\prod_{i=1}^{n} \frac{x_{i}}{a_{i}}\right)^{\frac{1}{n}}
$$

故

$$
n \cdot\left(\prod_{i=1}^{n} \frac{x_{i}}{a_{i}}\right)^{\frac{1}{n}} \leq n
$$

即

$$
\prod_{i=1}^{n}\left(\frac{x_{i}}{a_{i}}\right) \leq 1
$$

亦即

$$
x_{1} x_{2} \cdots x_{n} \leq a_{1} a_{2} \cdots a_{n} .
$$

当 $n \geq k+2$ 时, 由 $n=k+1$ 的情形的证明有: 对 $\{1,2, \cdots, n\}$ 的任一 $k+1$ 元子集 $I$, 有

$$
\prod_{i \in I} x_{i} \leq \prod_{i \in I} a_{i} .
$$

对 $I$ 求积即得:

$$
\left(\prod_{i=1}^{n} x_{i}\right)^{\left(\begin{array}{c}
n-1 \\
k
\end{array}\right)} \leq\left(\prod_{i=1}^{n} a_{i}\right)^{\left(\begin{array}{c}
n-1 \\
k
\end{array}\right)}
$$

从而

$$
x_{1} x_{2} \cdots x_{n} \leq a_{1} a_{2} \cdots a_{n} .
$$

综上可知: $x_{1} x_{2} \cdots x_{n}$ 的最大值为 $a_{1} a_{2} \cdots a_{n}$.

评注 上述证明可能不是最简单的, 但是是本质的.

本题的答案不难猜出为 $a_{1} a_{2} \cdots a_{n}$. 假设结论对 $n=k+1$ 成立, 援引 $n=k+1$ 的情形即可证明 $n \geq k+2$ 的情形. 因此只考虑 $n=k+1$.

由于题设条件均为线性, 但结论为积性, 所以考虑将积性转化为线性, 这就用到了均值不等式. 这一步看似大胆, 但也是限于题目条件而不得不为之. 证明中用了不等式证明中常用的增量思想和正负分离技巧.

我们补充一个类似的问题:

问题非负实数 $a_{1}, a_{2}, \cdots, a_{n}, b_{1}, b_{2}, \cdots, b_{n}$ 满足:

(1) $a_{1} \leq a_{2} \leq \cdots \leq a_{n}, a_{1} \leq b_{1} \leq b_{2} \cdots \leq b_{n} \leq a_{n}$;

(2) 对任意的 $1 \leq i<j \leq n$, 有 $a_{j}-a_{i} \geq b_{j}-b_{i}$.

证明: $a_{1} a_{2} \cdots a_{n} \leq b_{1} b_{2} \cdots b_{n}$.

总评 本次 $\mathrm{CMO}$ 的 6 个题难度适中. 1,4 是基本题. 第 2 题只要不一味地想着一步登天, 花上一定时间从简单情况逐步深入, 应该就能做出来. $3,5,6$ 都具有一定难度, 能攻下其中一道并且前面那三题能稳稳拿下就具有了一定的竞争力. 第 3 题需要较强的代数基本功. 第 5 题主要是用到了对应的思想, 难点还是在 +1 上. 第 6 题是一道新颖的中等难度的代数问题, 考查学生对一些代数基本思想和技巧的掌握情况.

