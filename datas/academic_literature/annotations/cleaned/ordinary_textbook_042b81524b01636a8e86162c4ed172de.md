数学新星网 $\%$ 冷岗松专栏

www.nsmath.cn/lgszl

# 2021 年上海数学新星五一营测试题解析 

胡珏伟 刘畅吴尉迟罗振华冷岗松

2021 年 5 月 3 日, 上海数学新星举行了一次测试, 测试共六道题, 时间从 17:30-21:30 共 4 个小时. 下面给出这些试题相应的解答. 不当之处, 敬请读者批评指正.

## I. 试 题

1. 求最大的实数 $c$, 使得对平面上任意两个单位向量 $\overrightarrow{v_{1}}, \overrightarrow{v_{2}}$, 均存在单位向量 $\vec{v}$, 满足

$$
\left|\vec{v} \cdot \vec{v}_{1}\right| \cdot\left|\vec{v} \cdot \vec{v}_{2}\right| \geq c
$$

2. 在不等边三角形 $A B C$ 中, 其内心为 $I$, 外心为 $O$. 角 $A, B, C$ 所对的边的长度分别记为 $a, b, c$, 且 $c<a<b$. 点 $B_{1}, C_{1}$ 分别是射线 $A C, A B$ 上的点且满足 $A B_{1}=A C_{1}=b+c-a$. 直线 $B B_{1}$ 与 $C C_{1}$ 交于 $P$, 直线 $A P$ 与 $B C$ 交于 $Q . D$ 是点 $A$ 关于 $O I$ 的轴对称点. 证明: $Q D$ 是 $\angle B D C$ 的外角平分线.证明:
3. 令 $\delta \in(0,1), x_{j} \in \mathbb{R}, j \in\{1,2, \cdots, m\}$, 满足 $0<x_{j} \leq 1+\delta$, 且 $\prod_{j=1}^{m} x_{j}=1$.

$$
\prod_{j=1}^{m}\left|x_{j}-1\right|<(\delta e)^{m}
$$

4. 已知图 $G$ 存在 $k(k \geq 2)$ 个不同的 $r$ 阶完全子图 $G_{1}, G_{2}, \cdots, G_{k}, A_{i}=$ $V\left(G_{i}\right), i=1,2, \cdots, k$, 满足

$$
\left|A_{1} \cup A_{2} \cup \cdots \cup A_{k}\right|+\left|A_{1} \cap A_{2} \cap \cdots \cap A_{k}\right| \leq 2 r-1 .
$$

证明: $G$ 有 $r+1$ 阶完全子图.

5. 将素数从小到大排列为 $p_{1}<p_{2}<\cdots$. 记 $a_{n}=\prod_{i=1}^{n} p_{i}, A_{n}$ 为 $a_{n}$ 的所有因子构成的集合. 证明: 若正整数 $m \leq a_{n}$, 则存在不同的 $b_{1}, b_{2}, \cdots, b_{k} \in A_{n}$,
$k \leq 2 n$ 使得

$$
m=b_{1}+b_{2}+\cdots+b_{k}
$$

6. 已知 $\triangle A B C$ 内接于 $\odot O, A D$ 是 $\odot O$ 的直径, $E$ 是 $B C$ 上一点, $D$ 关于 $E$ 的对称点为 $K$. 过 $C, D, E$ 的圆再次交 $O C$ 于 $F, D F$ 交 $A C$ 于 $P, P K$ 分别交 $A B, B C$ 于 $Q, T$, 过 $A, P, Q$ 的圆再次交 $\odot O$ 于 $S$.

证明: $S, K, E, T$ 四点共圆.

## II. 解答与评注

题 1 求最大的实数 $c$, 使得对平面上任意两个单位向量 $\overrightarrow{v_{1}}, \vec{v}_{2}$, 均存在单位向量 $\vec{v}$, 满足

$$
\left|\vec{v} \cdot \vec{v}_{1}\right| \cdot\left|\vec{v} \cdot \vec{v}_{2}\right| \geq c
$$

(上海大学 胡珏伟 供题)

解 $1 c$ 的最大值为 $\frac{1}{2}$.

由旋转不变性, 不妨假设 $\overrightarrow{v_{1}}=(1,0)$, 设 $\overrightarrow{v_{2}}=(\cos \theta, \sin \theta)$, 记任意单位向量 $\vec{v}=(\cos \varphi, \sin \varphi)$. 有

$$
\left|\vec{v} \cdot \overrightarrow{v_{1}}\right| \cdot\left|\vec{v} \cdot \overrightarrow{v_{2}}\right|=|\cos \varphi||\cos (\theta-\varphi)|=\frac{1}{2}|\cos \theta+\cos (\theta-2 \varphi)| .
$$

对给定的 $\theta$, 总可以适当选取 $\varphi_{0}$, 使 $\cos \left(\theta-2 \varphi_{0}\right)$ 等于 1 或 -1 (符号与 $\cos \theta$ 相同), 此时

$$
\frac{1}{2}\left|\cos \theta+\cos \left(\theta-2 \varphi_{0}\right)\right| \geq \frac{1}{2}
$$

即 $c \geq \frac{1}{2}$.

另一方面, 当 $\cos \theta=0$ (即 $\overrightarrow{v_{1}} \perp \overrightarrow{v_{2}}$ ) 时, 对任意单位向量 $\vec{v}$, 有

$$
\left|\vec{v} \cdot \vec{v}_{1}\right| \cdot\left|\vec{v} \cdot \overrightarrow{v_{2}}\right|=\frac{1}{2}|\cos (\theta-2 \varphi)| \leq \frac{1}{2}
$$

综上可得, $c$ 的最大值为 $\frac{1}{2}$.

## 解 2 (深圳中学冯晨旭)

记 $\langle\vec{a}, \vec{b}\rangle$ 为 $\vec{a}$ 和 $\vec{b}$ 所夹角大小.

取 $\overrightarrow{v_{1}} \perp \overrightarrow{v_{2}}$, 若 $\left\langle\vec{v}, \overrightarrow{v_{1}}\right\rangle=\alpha$, 则 $\left|\vec{v} \cdot \overrightarrow{v_{1}}\right|=|\cos \alpha|,\left|\vec{v} \cdot \overrightarrow{v_{2}}\right|=|\sin \alpha|$. 故

$$
\left|\vec{v} \cdot \vec{v}_{1}\right| \cdot\left|\vec{v} \cdot \vec{v}_{2}\right|=|\cos \alpha \cdot \sin \alpha|=\left|\frac{\sin 2 \alpha}{2}\right| \leq \frac{1}{2}
$$

对任意 $\overrightarrow{v_{1}}, \overrightarrow{v_{2}}$, 分如下两种情况讨论:
若 $\left\langle\overrightarrow{v_{1}}, \overrightarrow{v_{2}}\right\rangle<90^{\circ}$, 则取 $\vec{v}$ 在 $\overrightarrow{v_{1}}, \overrightarrow{v_{2}}$ 所夹角平分线上, 有 $\left\langle\vec{v}, \overrightarrow{v_{1}}\right\rangle=\left\langle\vec{v}, \overrightarrow{v_{2}}\right\rangle<$ $45^{\circ}$. 所以

$$
\left|\vec{v} \cdot \overrightarrow{v_{1}}\right|=\left|\vec{v} \cdot \overrightarrow{v_{2}}\right|>\frac{\sqrt{2}}{2}
$$

若 $\left\langle\overrightarrow{v_{1}}, \overrightarrow{v_{2}}\right\rangle \geq 90^{\circ}$, 则取 $\vec{v}$ 在 $\vec{v}_{1},-\overrightarrow{v_{2}}$ 所夹角平分线上, 有 $\left\langle\vec{v}, \vec{v}_{1}\right\rangle \leq 45^{\circ}$, $\left\langle\vec{v}, \overrightarrow{v_{2}}\right\rangle \geq 135^{\circ}$. 所以

$$
\left|\vec{v} \cdot \overrightarrow{v_{1}}\right|=\left|\vec{v} \cdot \overrightarrow{v_{2}}\right| \geq \frac{\sqrt{2}}{2}
$$

综上, $c$ 最大为 $\frac{1}{2}$.

评注 本题是简单的代数题, 考试中约 $86 \%$ 做对此题. 此题的强化版本如下:

令 $V$ 是二维复内积空间, 令 $\vec{z}_{1}, \overrightarrow{z_{2}}$ 是 $V$ 中的单位向量, 则:

$$
\sup \left\{\left|\vec{z} \cdot \overrightarrow{z_{1}}\right| \cdot\left|\vec{z} \cdot \overrightarrow{z_{2}}\right|:|\vec{z}|=1\right\} \geq \frac{1}{2}
$$

等号成立当且仅当 $\overrightarrow{z_{1}} \perp \overrightarrow{z_{2}}$.

题 2 在不等边三角形 $A B C$ 中, 其内心为 $I$, 外心为 $O$. 角 $A, B, C$ 所对的边的长度分别记为 $a, b, c$, 且 $c<a<b$. 点 $B_{1}, C_{1}$ 分别是射线 $A C, A B$ 上的点且满足 $A B_{1}=A C_{1}=b+c-a$. 直线 $B B_{1}$ 与 $C C_{1}$ 交于 $P$, 直线 $A P$ 与 $B C$ 交于 $Q . D$ 是点 $A$ 关于 $O I$ 的轴对称点. 证明: $Q D$ 是 $\angle B D C$ 的外角平分线.

(华东师范大学 罗振华 供题)



证明 由于 $A, D$ 关于 $O I$ 轴对称, 则 $O A=O D, I A=I D$. 注意到 $O$ 是 $\triangle A B C$ 的外心, 则 $A, B, D, C$ 四点共圆. 设 $I$ 关于 $A C, A B$ 的投影分别为 $B_{2}, C_{2}$. 由熟知的结论,

$$
A B_{2}=A C_{2}=\frac{b+c-a}{2}
$$

那么 $B_{2}, C_{2}$ 分别是 $A B_{1}, A C_{1}$ 的中点. 从而 $I A=I B_{1}=I C_{1}$. 结合 $I A=I D$ 知
$A, B_{1}, D, C_{1}$ 四点共圆且 $I$ 是圆心.

那么

$$
\angle B C_{1} D=\angle C B_{1} D, \angle C_{1} B D=\angle B_{1} C D \text {, }
$$

则 $\triangle B C_{1} D \backsim \triangle C B_{1} D$, 故

$$
\frac{D B}{D C}=\frac{B C_{1}}{C B_{1}}
$$

对 $\triangle A C C_{1}$ 及截线 $B_{1} B P$, 由 Menelaus 定理

$$
\frac{C P}{P C_{1}} \cdot \frac{C_{1} B}{B A} \cdot \frac{A B_{1}}{B_{1} C}=1 .
$$

对 $\triangle B C C_{1}$ 及截线 $A Q P$, 由 Menelaus 定理

$$
\frac{C_{1} A}{A B} \cdot \frac{B Q}{Q C} \cdot \frac{C P}{P C_{1}}=1
$$

将上两式相除, 并注意到 $A B_{1}=A C_{1}$, 可得 $\frac{Q B}{Q C}=\frac{B C_{1}}{C B_{1}}$. 所以 $\frac{Q B}{Q C}=\frac{D B}{D C}$. 由外角平分线定理知 $Q D$ 是 $\angle B D C$ 的外角平分线.

评注 本题是中等难度的几何题, 考试中约 $55 \%$ 做对此题. 由外角平分线定理知只需证 $\frac{B D}{C D}=\frac{B Q}{C Q}$. 使用两次 Menelaus 定理(或一次 Cave 定理)可得 $\frac{B Q}{C Q}=$ $\frac{B C_{1}}{C B_{1}}$. 再由 $A, B, D, C$ 四点共圆, $A, B_{1}, D, C_{1}$ 四点共圆知 $\triangle B C_{1} D \backsim \triangle C B_{1} D$,从而 $\frac{B D}{C D}=\frac{B C_{1}}{C B_{1}}$, 这样就证明了结论.

题 3 令 $\delta \in(0,1), x_{j} \in \mathbb{R}, j \in\{1,2, \cdots, m\}$, 满足 $0<x_{j} \leq 1+\delta$, 且 $\prod_{j=1}^{m} x_{j}=1$. 证明:

$$
\prod_{j=1}^{m}\left|x_{j}-1\right|<(\delta e)^{m}
$$

(山西大学附属中学 王永喜供题)

证明 1 (雅礼中学周韬顺) 先证如下引理.

引理 设 $n$ 是整数, $a_{1}, a_{2}, \cdots, a_{n}, b_{1}, b_{2}, \cdots, b_{n}$ 是非负数, 且 $a_{i} \geq b_{i}, i=$ $1, \cdots, n$, 则

$$
\prod_{i=1}^{n}\left(a_{i}-b_{i}\right) \leq\left(\sqrt[n]{\prod_{i=1}^{n} a_{i}}-\sqrt[n]{\prod_{i=1}^{n} b_{i}}\right)^{n}
$$

证明 由广义的柯西不等式(又称乘积形式的 Minkowski 不等式),

$$
\prod_{i=1}^{n} a_{i} \geq\left(\sqrt[n]{\prod_{i=1}^{n}\left(a_{i}-b_{i}\right)}+\sqrt[n]{\prod_{i=1}^{n} b_{i}}\right)^{n}
$$

变形即得要证结论.
回到原题.

不妨设 $x_{1}, x_{2}, \cdots, x_{m}$ 不全为 1 (否则左边为 0 ). 设 $x_{1}, x_{2}, \cdots, x_{n} \geq 1$, $x_{n+1}, \cdots, x_{m}<1(m-n=k)$. 由引理, 有

$$
\text { 左边 }=\prod_{i=1}^{n}\left(x_{i}-1\right) \prod_{j=1}^{k}\left(1-x_{n+j}\right) \leq\left(\prod_{i=1}^{n} x_{i}^{\frac{1}{n}}-1\right)^{n}\left(1-\prod_{j=1}^{k} x_{n+j}^{\frac{1}{k}}\right)^{k} \text {, }
$$

设

$$
\prod_{i=1}^{n} x_{i}^{\frac{1}{n}}=x \leq 1+\delta
$$

则

$$
\prod_{j=1}^{k} x_{n+j}^{\frac{1}{k}}=\sqrt[k]{\frac{1}{x^{n}}}
$$

此时

$$
\text { 左边 } \leq(x-1)^{n}\left(1-\frac{1}{x^{\frac{n}{k}}}\right)^{k} \leq \delta^{n}\left(1-(1+\delta)^{-\frac{n}{k}}\right)^{k} \text {. }
$$

由 Bernoulli 不等式得 $(1+\delta)^{-\frac{n}{k}}>1-\frac{n}{k} \delta$, 所以

$$
\delta^{n}\left(1-(1+\delta)^{-\frac{n}{k}}\right)^{k}<\delta^{n}\left(\frac{n}{k} \cdot \delta\right)^{k}=\delta^{m}\left(\frac{n}{k}\right)^{k}
$$

故只需证 $\left(\frac{n}{k}\right)^{\frac{k}{m}} \leq e$, 而 $e^{\frac{m}{k}} \geq \frac{m}{k}+1>\frac{n}{k}$, 故得证.

证明 2 不妨设 $x_{j} \neq 1$, 否则结论显然成立.

由对称性, 不妨设 $x_{1} \leq x_{2} \leq \cdots \leq x_{k}<1<x_{k+1} \leq \cdots \leq x_{m}$, 其中 $1 \leq k<m$. 令

$$
T=\prod_{j=k+1}^{m} x_{j}
$$

则 $T>1, \prod_{j=1}^{k} x_{j}=\frac{1}{T}$, 由于 $0<x_{j} \leq 1+\delta$, 故 $T \leq(1+\delta)^{m-k}$, 即 $\delta \geq T^{\frac{1}{m-k}}-1$.

由证明 1 中引理, 有

$$
\begin{aligned}
\prod_{j=1}^{m}\left|x_{j}-1\right| & =\prod_{j=1}^{k}\left(1-x_{j}\right) \prod_{j=k+1}^{m}\left(x_{j}-1\right) \\
& \leq\left(1-\sqrt[k]{x_{1} \cdots x_{k}}\right)^{k}\left(\sqrt[m-k]{x_{k+1} \cdots x_{m}}-1\right)^{m-k} \\
& =\left(1-T^{-\frac{1}{k}}\right)^{k}\left(T^{\frac{1}{m-k}}-1\right)^{m-k}
\end{aligned}
$$

注意到 $\delta \geq T^{\frac{1}{m-k}}-1$, 故要证原命题, 只需证

$$
\begin{aligned}
& \left(1-T^{-\frac{1}{k}}\right)^{k}\left(T^{\frac{1}{m-k}}-1\right)^{m-k}<e^{m}\left(T^{\frac{1}{m-k}}-1\right)^{m} \\
\Leftrightarrow & e^{\frac{m}{k}} T^{\frac{1}{m-k}}+T^{-\frac{1}{k}}-e^{\frac{m}{k}}-1>0 .
\end{aligned}
$$

令

$$
f(x)=e^{\frac{m}{k}} x^{\frac{1}{m-k}}+x^{-\frac{1}{k}}-e^{\frac{m}{k}}-1,
$$

则当 $x \geq 1$ 时, 由 $e^{x}>x, \forall x>0$ 知,

$$
\begin{aligned}
f^{\prime}(x) & =\frac{1}{m-k} e^{\frac{m}{k}} x^{\frac{1}{m-k}-1}-\frac{1}{k} x^{-\frac{1}{k}-1} \\
& =x^{-1}\left(\frac{1}{m-k} e^{\frac{m}{k}} x^{\frac{1}{m-k}}-\frac{1}{k} x^{-\frac{1}{k}}\right) \\
& \geq x^{-1}\left(\frac{1}{m-k} \cdot \frac{m}{k}-\frac{1}{k}\right)>0
\end{aligned}
$$

故 $f(T)>f(1)=0$, 故原命题成立.

证明 3 若存在某个 $x_{i}=1$, 则结论显然成立. 由对称性, 不妨假设 $x_{1} \leq x_{2} \leq$ $\cdots \leq x_{s}<1<x_{s+1} \leq \cdots \leq x_{m},(1 \leq s<m)$. 若固定 $x y$, 且 $0<x<1, y>1$,则

$$
|x-1||y-1|=(1-x)(y-1)=x+y-x y-1 .
$$

故 $x+y$ 增大时, $|x-1||y-1|$ 也增大. 因此, 对 $\left(x_{1}, x_{m}\right),\left(x_{1}, x_{m-1}\right) \cdots,\left(x_{1}, x_{s+1}\right)$用调整, 至 $x_{s+1}=\cdots=x_{m}=1+\delta$, 有 LHS 增大.

此时对调整后的 $x_{1} \leq x_{2} \leq \cdots \leq x_{s}$, 将其中的最小数与最大数 $x_{1}, x_{s}$ 调为 $\sqrt[s]{x_{1} \cdots x_{s}}$ 和 $x_{1} \cdot x_{s} / \sqrt[s]{x_{1} \cdots x_{s}}$. 类似前述调整知 LHS 增大. 不断对新得到的 $x_{1} \leq x_{2} \leq \cdots \leq x_{s}$ 进行这样的调整, 至多 $s-1$ 次调整后, 有

$$
x_{1}=\cdots=x_{s}=a, x_{s+1}=\cdots=x_{n}=1+\delta(s \geq 1) \text {, 且 } a^{s}(1+\delta)^{m-s}=1 \text {. }
$$

下面只需证明

$$
\prod_{j=1}^{m}\left|x_{j}-1\right|=(1-a)^{s} \delta^{m-s}<(\delta e)^{m} \Leftrightarrow 1-a<\delta e^{\frac{m}{s}}
$$

若 $\delta e^{\frac{m}{s}} \geq 1$, 则显然(1)成立, 下设 $\delta e^{\frac{m}{s}}<1$. 结合 $a^{s}(1+\delta)^{m-s}=1$, 有

$$
\begin{aligned}
(1) & \Leftrightarrow\left(1-\delta e^{\frac{m}{s}}\right)^{s}(1+\delta)^{m-s}<1 \\
& \Leftrightarrow s \ln \left(1-\delta e^{\frac{m}{s}}\right)+(m-s) \ln (1+\delta)<0 .
\end{aligned}
$$

令

$$
f(\delta)=s \ln \left(1-\delta e^{\frac{m}{s}}\right)+(m-s) \ln (1+\delta)
$$

求导有

$$
\begin{aligned}
f^{\prime}(\delta) & =-\frac{s e^{\frac{m}{s}}}{1-\delta e^{\frac{m}{s}}}+\frac{m-s}{1+\delta} \\
& =\frac{m-s-m \delta e^{\frac{m}{s}}-s e^{\frac{m}{s}}}{\left(1-\delta e^{\frac{m}{s}}\right)(1+\delta)}
\end{aligned}
$$

考虑到 $s e^{\frac{m}{s}}>s \cdot \frac{m}{s}=m$, 有 (3) $<0$. 故

$$
f(\delta) \leq f(0)=0
$$

即(2)成立.

综上, 命题得证!

评注 本题是中等难度的代数题, 考试中约 $35 \%$ 做对此题. 法 1 是利用广义柯西不等式, 将原不等式放缩为两个几何平均与 1 之差乘积的形式, 进而只需证明一个单变量不等式, 最后利用 Bernoulli 不等式得到证明. 法 2 直接用求导的方法证明了同一单变量不等式. 法 3 利用调整法, 先调落在 1 两侧的数, 再调小于 1 的数. 特别注意在这步调整时, 需直接调为全体小于 1 之数的几何平均数,若仅仅调为两个的平均, 则此调整不会在有限步结束.

题 4 已知图 $G$ 存在 $k(k \geq 2)$ 个不同的 $r$ 阶完全子图 $G_{1}, G_{2}, \cdots, G_{k}, A_{i}=$ $V\left(G_{i}\right), i=1,2, \cdots, k$, 满足

$$
\left|A_{1} \cup A_{2} \cup \cdots \cup A_{k}\right|+\left|A_{1} \cap A_{2} \cap \cdots \cap A_{k}\right| \leq 2 r-1 .
$$

证明: $G$ 有 $r+1$ 阶完全子图.

(华东师范大学 吴尉迟 供题)

证明 1 我们对 $k+r$ 归纳证明 $G_{1} \cup G_{2} \cup \cdots \cup G_{k}$ 有 $r+1$ 阶完全子图.

当 $k=2$ 时, 由容斥原理, $\left|A_{1} \cup A_{2}\right|+\left|A_{1} \cap A_{2}\right|=\left|A_{1}\right|+\left|A_{2}\right|=2 r$, 故条件不成立.

当 $k=3, r=2$ 时, 条件不等式即为

$$
\left|A_{1} \cup A_{2} \cup A_{3}\right|+\left|A_{1} \cap A_{2} \cap A_{3}\right| \leq 3,
$$

易知 $G_{1} \cup G_{2} \cup G_{3}$ 为 3 阶完全图.

假设结论对小于 $k+r(k \geq 3)$ 时成立, 考虑 $k+r$ 的情形.

若 $A_{1} \cap A_{2} \cap \cdots \cap A_{k} \neq \emptyset$, 取 $v \in A_{1} \cap A_{2} \cap \cdots \cap A_{k}$, 则 $v$ 与所有点相邻. 将所有 $A_{i}$ 去掉 $v$, 用归纳假设可知存在 $r$ 阶完全子图, 再并上 $v$ 及其所连的边, 即得 $r+1$ 阶子图.

下设 $A_{1} \cap A_{2} \cap \cdots \cap A_{k}=\emptyset$.

若 $\left|A_{1} \cup \cdots \cup A_{k-1}\right|+\left|A_{1} \cap \cdots \cap A_{k-1}\right| \leq 2 r-1$, 则对 $G_{1}, G_{2}, \cdots, G_{k-1}$ 用归纳假设知, 结论成立.

若 $\left|A_{1} \cup \cdots \cup A_{k-1}\right|+\left|A_{1} \cap \cdots \cap A_{k-1}\right| \geq 2 r$.

记 $X=\left(A_{1} \cup \cdots \cup A_{k-1}\right) \backslash\left(A_{1} \cap \cdots \cap A_{k-1}\right)$. 注意到 $A_{k} \cap X$ 及其边构成的图为完全图, 且所有点均与 $A_{1} \cap \cdots \cap A_{k-1}$ 相连, 又 $A_{1} \cap \cdots \cap A_{k-1}$ 及其边构成完全图, 故 $\left(A_{k} \cap X\right) \cup\left(A_{1} \cap \cdots \cap A_{k-1}\right)$ 及其边构成完全图.
故可不妨设 $\left|\left(A_{k} \cap X\right) \cup\left(A_{1} \cap \cdots \cap A_{k-1}\right)\right| \leq r$, 否则结论成立. 由 $A_{k} \cap X$ 与 $A_{1} \cap \cdots \cap A_{k-1}$ 不交, 且 $A_{1} \cap A_{2} \cap \cdots \cap A_{k}=\emptyset$, 故

$$
\begin{aligned}
r \geq & \left|\left(A_{k} \cap X\right) \cup\left(A_{1} \cap \cdots \cap A_{k-1}\right)\right| \\
= & \left|A_{k} \cap X\right|+\left|A_{1} \cap \cdots \cap A_{k-1}\right| \\
= & \left|A_{k}\right|+|X|-\left|A_{k} \cup X\right|+\left|A_{1} \cap \cdots \cap A_{k-1}\right| \\
= & r+\left|A_{1} \cup \cdots \cup A_{k-1}\right|-\left|A_{1} \cap \cdots \cap A_{k-1}\right| \\
& \quad-\left(\left|A_{1} \cup \cdots \cup A_{k}\right|-\left|A_{1} \cap \cdots \cap A_{k-1}\right|\right)+\left|A_{1} \cap \cdots \cap A_{k-1}\right| \\
& =r+\left|A_{1} \cup \cdots \cup A_{k-1}\right|+\left|A_{1} \cap \cdots \cap A_{k-1}\right|-\left|A_{1} \cup \cdots \cup A_{k}\right| .
\end{aligned}
$$

于是,

$$
\left|A_{1} \cup \cdots \cup A_{k}\right| \geq\left|A_{1} \cup \cdots \cup A_{k-1}\right|+\left|A_{1} \cap \cdots \cap A_{k-1}\right| \geq 2 r
$$

这与条件矛盾, 故结论成立!

证明 2 令 $A_{1} \cup A_{2} \cup \cdots \cup A_{i}=B_{i}, A_{1} \cap A_{2} \cap \cdots \cap A_{i}=C_{i}(i=1,2, \cdots, k)$,则

$$
\left|B_{1}\right|+\left|C_{1}\right|=\left|A_{1}\right|+\left|A_{1}\right|=2 r \text {. }
$$

又由条件知 $\left|B_{k}\right|+\left|C_{k}\right| \leq 2 r-1$, 故存在 $i \in\{1,2, \cdots, k-1\}$, 使得

$$
\left|B_{i}\right|+\left|C_{i}\right|-\left|B_{i+1}\right|-\left|C_{i+1}\right| \geq 1
$$

下面考察集合 $\left(B_{i} \cap A_{i+1}\right) \cup C_{i}$.

首先, 我们证明 $\left(B_{i} \cap A_{i+1}\right) \cup C_{i}$ 是一个完全子图, 将该集合划分为两个部分: $B_{i} \cap A_{i+1}$ 与 $C_{i} \backslash\left(B_{i} \cap A_{i+1}\right)$.

对 $x, y \in B_{i} \cap A_{i+1}$, 有 $x, y \in A_{i+1}$ 故 $x, y$ 相邻.

对 $x, y \in C_{i} \backslash\left(B_{i} \cap A_{i+1}\right)$, 有 $x, y \in C_{i}$, 即 $x, y \in A_{1}$, 故 $x, y$ 相邻.

对 $x \in B_{i} \cap A_{i+1}, y \in C_{i} \backslash\left(B_{i} \cap A_{i+1}\right)$. 由 $x \in B_{i}$, 设 $x \in A_{j}(j \in\{1,2, \cdots, i\})$,又由 $y \in C_{i}$ 知 $y \in A_{j}$, 故 $x, y$ 相邻.

综上, 任意 $x, y \in\left(B_{i} \cap A_{i+1}\right) \cup C_{i}$, 有 $x, y$ 相邻. 即 $\left(B_{i} \cap A_{i+1}\right) \cup C_{i}$ 是一个完全子图.

下面证明 $\left(B_{i} \cap A_{i+1}\right) \cup C_{i}$ 至少是 $r+1$ 阶的完全子图, 这是由于

$$
\begin{aligned}
\left|\left(B_{i} \cap A_{i+1}\right) \cup C_{i}\right| & =\left|B_{i} \cap A_{i+1}\right|+\left|C_{i}\right|-\left|B_{i} \cap A_{i+1} \cap C_{i}\right| \\
& =\left|B_{i}\right|+\left|A_{i+1}\right|-\left|B_{i} \cup A_{i+1}\right|+\left|C_{i}\right|-\left|C_{i+1}\right| \\
& =\left|B_{i}\right|+\left|A_{i+1}\right|-\left|B_{i+1}\right|+\left|C_{i}\right|-\left|C_{i+1}\right|
\end{aligned}
$$

$$
\begin{aligned}
& =\left|A_{i+1}\right|+\left(\left|B_{i}\right|+\left|C_{i}\right|-\left|B_{i+1}\right|-\left|C_{i+1}\right|\right) \\
& \geq\left|A_{i+1}\right|+1 \\
& =r+1
\end{aligned}
$$

综上, 原命题得证.

证明 3 (雅礼中学周蹈顺) $k=2$ 时,

$$
2 r-1 \geq\left|A_{1} \cup A_{2}\right|+\left|A_{1} \cap A_{2}\right|=\left|A_{1}\right|+\left|A_{2}\right|=2 r
$$

矛盾.

$k \geq 3$ 时, 记

$$
S_{l}=\bigcup_{i=1}^{l}\left(A_{l+1} \cap A_{i}\right) \cup\left(\bigcap_{i=1}^{l} A_{i}\right) \quad(l=2,3, \cdots, k-1)
$$

任取 $S_{l}$ 中两点, 若这两点均属于 $\bigcup_{i=1}^{l}\left(A_{l+1} \cap A_{i}\right)$, 则这两点均属于 $A_{l+1}$, 故在 $G$ 中相邻. 若这两点均属于 $\bigcap_{i=1}^{l} A_{i}$, 则这两点在 $G$ 中也相邻. 若这两点分别属于 $\bigcup_{i=1}^{l}\left(A_{l+1} \cap A_{i}\right)$ 和 $\bigcap_{i=1}^{l} A_{i}$, 则它们都属于一个公共的集合 (在 $A_{1}, \cdots, A_{l+1}$ ) 中,这两点在 $G$ 中仍然相邻. 故 $S_{l}$ 诱导了一个完全子图, 若结论不成立, 则 $\left|S_{l}\right| \leq r$.

下面证明:

$$
\left|\bigcup_{i=1}^{k} A_{i}\right|+\left|\bigcap_{i=1}^{k} A_{i}\right|+\sum_{l=2}^{k-1}\left|S_{l}\right|=\sum_{i=1}^{k}\left|A_{i}\right|
$$

考虑元素 $x$, 它恰属于集合 $A_{i_{1}}, A_{i_{2}}, \cdots, A_{i_{m}}\left(i_{1}<i_{2}<\cdots<i_{m}, m \geq 1\right)$.

若 $m=k$, 则 $x$ 在左右式各被计算 $k$ 次.

若 $m<k$, 对 $i_{2}$ 分如下两种情况讨论:

(1) $i_{2} \geq 3$, 则 $x \in S_{l}$ 当且仅当存在 $j>1$ 使 $l=i_{j}-1$, 故 $x$ 在左右两边各被计算 $m$ 次.

(2) $i_{2}=2$, 取最小的正整数 $p \notin\left\{i_{1}, i_{2}, \cdots, i_{m}\right\}$, 则 $x \in S_{l}$ 当且仅当存在 $j>2$ 使 $l=i_{j}-1$ 或 $l=p-1$, 故 $x$ 在左右两边仍被计算 $m$ 次.

所以 $(*)$ 式成立, 而由反证假设,

$$
\text { 左边 } \leq 2 r-1+(k-2) r=k r-1<k r=\text { 右边, }
$$

矛盾. 故假设不成立, 证毕.

评注 本题是较难的组合题, 考试中不到 $5 \%$ 做对此题.一个自然的切入点是考虑 $A_{1}, \cdots, A_{i}$ 的交, 再在 $A_{1}, \cdots, A_{i}$ 的并中选取一些点使之构成 $r+1$ 阶
完全子图. 故可以先考虑这些点的落在其它某个 $A_{j}$ 的情形. 上面三种证法, 皆依赖于这个想法. 在具体的个数的估计中, 证法 1 利用了归纳假设, 选取 $i$ 为 $k$; 证法 2 直接选取 $\left|B_{i}\right|+\left|C_{i}\right|$ 减小最快的那个 $i$; 证法 3 则是在整体上考虑, 利用恒等式 $(*)$ 得到矛盾.

题 5 将素数从小到大排列为 $p_{1}<p_{2}<\cdots$. 记 $a_{n}=\prod_{i=1}^{n} p_{i}, A_{n}$ 为 $a_{n}$ 的所有因子构成的集合. 证明: 若正整数 $m \leq a_{n}$, 则存在不同的 $b_{1}, b_{2}, \cdots, b_{k} \in A_{n}$, $k \leq 2 n$ 使得

$$
m=b_{1}+b_{2}+\cdots+b_{k}
$$

(浙江温州知临中学 羊明亮 供题)

证明 1 (东北师大附中付佳睿) 先证下面的引理:

引理 任一个含平方因子的正整数可表示为两个不同的无平方因子的正整数之和.

证明 反证法, 假设正整数 $n$ 不满足引理, 则

$$
\{1, n-1\},\{2, n-2\}, \cdots,\left\{\left\lfloor\frac{n-1}{2}\right\rfloor, n-\left\lfloor\frac{n-1}{2}\right\rfloor\right\}
$$

每对均至少有一个含平方因子的数. 结合 $n$ 含平方因子知, 1 至 $n$ 中至少有 $\left\lfloor\frac{n-1}{2}\right\rfloor+1 \geq \frac{n}{2}$ 个含平方因子的数.

而 1 至 $n$ 中含平方因子的数的个数至多有

$$
\begin{aligned}
\sum_{p \text { 是素数 }}\left\lfloor\frac{n}{p^{2}}\right\rfloor & \leq \sum_{p \text { 是素数 }} \frac{n}{p^{2}} \\
& <n\left(\frac{1}{2^{2}}+\frac{1}{3^{2}}+\frac{1}{5^{2}}+\frac{1}{7^{2}}+\frac{1}{11^{2}}+\frac{1}{13^{2}}+\frac{1}{17^{2}}+\frac{1}{19^{2}}+\frac{1}{23^{2}}+\cdots\right) \\
& <n\left(\frac{1}{2^{2}}+\frac{1}{2 \times 4}+\frac{1}{4 \times 6}+\frac{1}{6 \times 8}+\frac{1}{8 \times 10}+\cdots\right) \\
& <\frac{n}{2},
\end{aligned}
$$

矛盾! 故引理得证.

回到原题.

对 $n$ 归纳证明原命题.

当 $n=1$ 时, $a_{1}=2$, 显然成立.

假设结论对 $n-1(n \geq 2)$ 成立, 考虑 $n$ 的情形.

对任意不大于 $a_{n}$ 的数 $m$, 设 $m=k p_{n}+r$, 其中 $k, r \in \mathbb{N}^{*}$ 且 $r<p_{n}$. 则

$$
k \leq \frac{a_{n}}{p_{n}}=a_{n-1}
$$

故由归纳假设知 $k$ 可表示为 $a_{n-1}$ 不多于 $2 n-2$ 个不同因子之和. 又 $a_{n}=p_{n} a_{n-1}$,故 $p_{n} k$ 可以表示为 $a_{n}$ 不多于 $2 n-2$ 个不同因子之和, 且这些因子均不小于 $p_{n}$.

若 $r=0$, 则结论成立. 下设 $r>0$.

若 $r$ 无平方因子, 则由 $r<p_{n}$ 知, $r$ 为 $a_{n}$ 的因子且与已选取因子不同, 故结论成立.

若 $r$ 含平方因子, 由引理可知, $r$ 可以表示为 2 个不同的无平方因子数之和,且这些数小于 $p_{n}$. 故这两个数为 $a_{n}$ 的因子且与已选取因子不同, 故结论成立!

评注 本题是较难的数论题, 考试中不到 $5 \%$ 做对此题. 用归纳法证明该问题是自然的,在归纳过度中利用带余除法可保证所选取的因子各不相同, 这样只需考虑余数 $r$ 含平方因子的情形, 这便是引理.

题 6 已知 $\triangle A B C$ 内接于 $\odot O, A D$ 是 $\odot O$ 的直径, $E$ 是 $B C$ 上一点, $D$ 关于 $E$ 的对称点为 $K$. 过 $C, D, E$ 的圆再次交 $O C$ 于 $F, D F$ 交 $A C$ 于 $P, P K$ 分别交 $A B, B C$ 于 $Q, T$, 过 $A, P, Q$ 的圆再次交 $\odot O$ 于 $S$

证明: $S, K, E, T$ 四点共圆.

(湖南师范大学附属中学 苏林 供题)


证明 1 设 $M, N$ 分别是 $D Q, D P$ 中点, $O_{1}, O_{2}$ 分别是 $\triangle C E D, \triangle B E D$ 的外心, $O B$ 再次交 $\odot(B D E)$ 于 $L$.

因为 $O M / / A B$, 所以 $O M \perp B D$, 从而 $O_{2}$ 在 $O M$ 上, 同理 $O_{1}$ 在 $O N$ 上. 因为

$$
\angle O O_{1} D=\frac{1}{2}\left(360^{\circ}-\angle D O_{1} C\right)=180^{\circ}-\angle D F C=\angle O F D
$$

所以 $O, F, O_{1}, D$ 四点共圆;同理 $O, L, O_{2}, D$ 四点共圆. 因为

$$
\angle O O_{2} D=180^{\circ}-\angle B E D=\angle D E C=\angle D F C \text {, }
$$

所以 $O, F, O_{2}, D$ 四点共圆, 从而 $O, L, O_{1}, D, O_{2}, F$ 六点共圆. 于是

$$
\angle D L E=\angle D B E=\angle D A C=\angle D O O_{1}=\angle D L O_{1},
$$

从而 $L, E, O_{1}$ 三点共线. 同理 $F, E, O_{2}$ 三点共线.

在圆内接六边形 $L D F O_{2} O O_{1}$ 中由帕斯卡定理知: $L D, O O_{2}$ 的交点在 $N E$上, 于是 $L, M, D$ 三点共线, 从而 $L$ 在 $D Q$ 上. 因为 $B, L, E, D$ 四点共圆, 所以

$$
\angle L D E=\angle L B E=90^{\circ}-\angle B A C \text {, }
$$

同理 $\angle F D E=90^{\circ}-\angle B A C$.

而

$\angle C B M=\angle Q B M-\angle A B C=\angle B Q M-\angle A B C=\angle B A D+\angle Q D A-\angle A B C$,

$\angle B C N=\angle A C B-\angle P C N=\angle A C B-\angle D P C=\angle A C B-(\angle C A D+\angle A D P)$,

所以

$\angle C B M-\angle B C N=(\angle B A D+\angle Q D A+\angle C A D+\angle A D P)-(\angle A B C+\angle A C B)=0$,

于是 $\angle C B M=\angle B C N$, 所以 $B M / / C N$. 所以

$$
\frac{K P}{K Q}=\frac{E N}{E M}=\frac{E C}{E B}
$$

因为 $\angle S Q A=\angle S P A$, 所以 $\angle S Q B=\angle S P C$. 而 $\angle S B Q=\angle S C P$, 所以 $\triangle S B Q$与 $\triangle S C P$ 旋转相似, 从而 $\triangle S Q P$ 与 $\triangle S B C$ 也旋转相似. 由 $\frac{K P}{K Q}=\frac{E C}{E B}$ 知 $K, E$是一对相似对应点, 所以 $A K, A E$ 的夹角与 $P Q, B C$ 的夹角相等, 即

$$
\angle K S E=\angle P T C=\angle K T E .
$$

所以 $S, K, E, T$ 四点共圆.


证明 2 (深圳中学冯晨旭) 设 $D$ 关于 $A B, A C$ 对称点分别为 $H, I, H I$ 交 $A B, A C$ 于 $J, L$. 设 $\triangle B D E$ 外接圆交 $B O$ 于 $G, D G$ 交 $A B$ 于 $Q^{\prime}, P Q^{\prime}$ 交 $H I$于 $K^{\prime}$. 由于

$$
\angle O G D=180^{\circ}-\angle B G D=180^{\circ}-\angle B E D=\angle D E C=180^{\circ}-\angle O F D,
$$

故 $O, F, D, G$ 共圆. 因为

$$
\frac{Q^{\prime} K^{\prime}}{K^{\prime} P}=\frac{Q^{\prime} J}{P L} \cdot \frac{\sin \angle Q^{\prime} J K^{\prime}}{\sin \angle P L K^{\prime}}
$$

过 $D$ 作 $M N / / B C$ 交 $A B, A C$ 于 $M, N$, 由 $\angle A B D=\angle A C D=90^{\circ}$, 有

$$
\angle J D B=\angle M D B=90^{\circ}-\angle A B C=\angle O A C .
$$

故

$$
\angle A D J=\angle O C B=\angle A D L=\angle O B C
$$

而

$$
\angle L D J=2 \angle O B C=180^{\circ}-\angle B O C=\angle P D Q^{\prime}
$$

因此

$$
\begin{gathered}
\angle Q^{\prime} D J=\angle P D L \\
\frac{Q^{\prime} J}{P L}=\frac{Q^{\prime} D}{P D} \cdot \frac{\sin \angle P L D}{\sin \angle Q^{\prime} J D}=\frac{Q^{\prime} D}{P D} \cdot \frac{\sin \angle L D A}{\sin \angle J D A} \cdot \frac{A J}{A L}=\frac{Q^{\prime} D}{P D} \cdot \frac{\sin \angle P L K^{\prime}}{\sin \angle Q^{\prime} J K^{\prime}}
\end{gathered}
$$

故

$$
\frac{Q^{\prime} K^{\prime}}{K^{\prime} P}=\frac{Q^{\prime} D}{D P}
$$

即 $D K^{\prime}$ 平分 $\angle Q^{\prime} D P$. 由 $D E$ 平分 $\angle Q^{\prime} D P$ 有 $D E K^{\prime}$ 共线. 由 $D E=E K=E K^{\prime}$有 $K=K^{\prime}, Q=Q^{\prime}$. 因此

$$
\angle Q H J=\angle Q D J=\angle P D L=\angle P I L
$$

故 $Q H / / P I$. 可得

$$
\frac{Q K}{P K}=\frac{Q D}{P D}=\frac{Q H}{P I}=\frac{H K}{I K}=\frac{B E}{C E} .
$$

因为 $A, B, C, S$ 和 $A, P, Q, S$ 共圆, 有

$$
\angle S P T=\angle S A B=\angle S C T
$$

故 $S, P, C, T$ 共圆.

因为

$$
\angle S Q P=\angle S A P=\angle S B C, \angle S P Q=180^{\circ}-\angle S A Q=\angle S C B
$$

有 $\triangle S P Q \backsim \triangle S C B$. 由 $\frac{Q K}{K P}=\frac{B E}{E C}$, 有 $\triangle S K E \backsim \triangle S P C$. 故

$$
\angle K S E=\angle P S C=\angle P T C,
$$

即 $K, S, T, E$ 共圆.



证明 3 (雅礼中学周韬顺) 设

$$
\angle P D E=\alpha=\angle F C E=90^{\circ}-\angle B A C .
$$

在 $A B$ 上取点 $Q^{\prime}$ 使直线 $D P, D Q^{\prime}$ 关于直线 $D K$ 对称, 由张角定理:

$$
\frac{\sin \angle C D B}{D E}=\frac{\sin \angle C D E}{B D}+\frac{\sin \angle B D E}{C D}
$$

因为 $\sin \angle C D B=\sin \angle C A B=\cos \alpha$, 由

$$
\angle C D B-\alpha=\left(180^{\circ}-\angle B A C\right)-\left(90^{\circ}-\angle B A C\right)=90^{\circ}
$$

得

$$
\angle C D E+\angle B D Q^{\prime}=\angle B D E+\angle C D P=90^{\circ},
$$

代入(1)得

$\frac{\cos \alpha}{D E}=\frac{\cos \angle B D Q^{\prime}}{B D}+\frac{\cos \angle C D P}{C D}=\frac{1}{P D}+\frac{1}{Q^{\prime} D}$ (用到 $D C \perp A C, D B \perp A B$ ),所以

$$
\frac{\sin 2 \alpha}{D K}=\frac{\sin \alpha}{P D}+\frac{\sin \alpha}{Q^{\prime} D}
$$

故 $P, K, Q^{\prime}$ 共线, 从而 $Q$ 与 $Q^{\prime}$ 重合. 所以

$$
\frac{P K}{K Q}=\frac{P D}{D Q}=\frac{C D}{B D} \cdot \frac{\cos \angle B D Q}{\cos \angle C D P}=\frac{C D}{B D} \cdot \frac{\sin \angle C D E}{\sin \angle B D E}=\frac{C E}{E B} .
$$

因为

$$
\angle S P Q=\angle S A Q=\angle S C B, \angle S Q P=180^{\circ}-\angle S A P=\angle S B C \text {. }
$$

所以结合(2得 $\triangle S P Q \sim \triangle S C B, \triangle S P K \sim \triangle S C E$ 所以 $\angle S K Q=\angle S E B$, 故 $S, K, E, T$ 四点共圆. 证毕.
评注 本题是较难的几何题, 考试中不到 $5 \%$ 做对此题. 法 1 主要通过找共圆, 共线及平行关系得到 $\frac{K P}{K Q}=\frac{E C}{E B}$. 再结合 $\triangle S P Q \backsim \triangle S C B$ 即可证明结论. 法 2 与法 1 思路大致相同, 不过使用了分角定理使运算简化了一些. 法 3 比较巧妙得使用张角定理证明了 $D K$ 平分 $\angle P D Q$, 从而证明了结论.

