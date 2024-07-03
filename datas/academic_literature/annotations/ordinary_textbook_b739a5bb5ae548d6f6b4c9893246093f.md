$$
\text { 数学新星网 米解答展示 }
$$

www.nsmath.cn/jdzs

# 第三十一期问题征解解答与点评 

牟晓生

第一题 在不等边三角形 $A B C$ 中, $I$ 为内心, $M$ 为 $B C$ 中点. 直线 $M I$与 $A C$ 交于点 $Q_{B}, P_{B}$ 为 $\triangle A B C$ 外接圆弧 $A C$ 的中点, $D_{B}$ 为 $\triangle P_{B} Q_{B} I$ 与 $\triangle A I C$ 两个外接圆的第二个交点. 类似定义 $Q_{C}, P_{C}, D_{C}$. 证明: $D_{B} D_{C}$ 的中点在 $\triangle A B C$ 的外接圆上.

(浙江镇海中学学生 骆晗 供题)

## 证明 (根据浙江镇海中学严君啸同学的解答整理):

设 $I_{B}$ 为 $\triangle A B C$ 对应顶点 $B$ 的旁心, $N$ 为外接圆上弧 $\widehat{B A C}$ 的中点, 则熟知 $N, A, I_{B}$ 共线, 而 $A, I, C, I_{B}$ 都在以 $P_{B}$ 为圆心的一个圆上. 由 Menelaus 定理,

$$
\frac{B M}{M C} \cdot \frac{C Q_{B}}{Q_{B} T} \cdot \frac{T I}{I B}=1
$$

所以 $\frac{C Q_{B}}{Q_{B} T}=\frac{B I}{I T}=\frac{P_{B} I}{P_{B} T}$, 故 $P_{B} Q_{B} / / C I$. 这样得到

$$
\angle Q_{B} P_{B} I=\angle T I C=\frac{\pi-\angle A}{2}=\angle N P_{B} I
$$

故 $N$ 在直线 $P_{B} Q_{B}$ 上.

注意到 $\angle N A Q_{B}=\frac{\pi+\angle A}{2}=\angle Q_{B} P_{B} I_{B}$, 所以 $A, Q_{B}, P_{B}, I_{B}$ 四点共圆, 而直线 $A I_{B}$ 与直线 $Q_{B} P_{B}$ 分别是这个圆与 $\triangle A I C$ 及 $\triangle P_{B} Q_{B} I$ 的外接圆的根轴. 故 $N$ 是这三个圆的根心, 由此导出 $N$ 在直线 $I D_{B}$ 上. 由于 $I I_{B}$ 是 $A I C$ 外接圆的直径, 进一步有 $N D_{B} \perp I_{B} D_{B}$.

同理, 如果我们设 $I_{C}$ 为 $\triangle A B C$ 对应顶点 $C$ 的旁心, 则 $N D_{C} \perp I_{C} D_{C}$. 熟知 $N$ 是 $I_{B} I_{C}$ 的中点, 故两个三角形 $\triangle N D_{B} I_{B}$ 与 $\triangle N D_{C} I_{C}$ 全等, 即知 $N$ 是 $D_{B} D_{C}$ 的中点.

评注 海亮高级中学团队, 山东省实验初中孙永喆, 安庆市第一中学叶龙翔,宁波中学卢宁, 宁波蛟川书院袁吴喆, 江苏海门中学朱嘉奕, 杭州二中刘浩宇,
重庆巴蜀中学但流金, 成都七中嘉祥唐龙天, 镇海中学刘哲源, 大连育明高中陶汉桥, 华南师范大学附属中学冯宣瑞, 重庆南开中学伍垟圳, 山大附中杨安, 王宇彬, 王子或, 人大附中郑云兮, 贾维宸等同学也给出了本题的正确解答.

第二题 设 $n>k$ 是正整数, $p>3$ 是素数. 证明:

$$
\left(\begin{array}{c}
p n \\
p k
\end{array}\right) \equiv\left(\begin{array}{l}
n \\
k
\end{array}\right) \quad\left(\bmod p^{v_{p}(n)+3}\right)
$$

(北京大学学生 陈泽坤 供题)

## 证明 (根据海亮高级中学叶涵和史皓嘉同学的解答整理):

令 $f(x)=(x-1)(x-2) \cdots(x-p+1)$, 则有

$$
\left(\begin{array}{l}
p n \\
p k
\end{array}\right)-\left(\begin{array}{l}
n \\
k
\end{array}\right)=\frac{\prod_{i=n-k+1}^{n} p i \cdot f(p i)}{\prod_{j=1}^{k} p j \cdot f(p j)}-\frac{\prod_{i=n-k+1}^{n} i}{\prod_{j=1}^{k} j}=\left(\begin{array}{l}
n \\
k
\end{array}\right) \cdot\left(\frac{\prod_{i=n-k+1}^{n} f(p i)}{\prod_{j=1}^{k} f(p j)}-1\right) .
$$

所以只要证明

$$
p^{v_{p}(n)+3} \left\lvert\,\left(\begin{array}{l}
n \\
k
\end{array}\right) \cdot\left(\prod_{i=n-k+1}^{n} f(p i)-\prod_{j=1}^{k} f(p j)\right)\right.
$$

我们将 $\left(\begin{array}{l}n \\ k\end{array}\right)$ 写为 $\frac{n}{n-k} \cdot\left(\begin{array}{c}n-1 \\ k\end{array}\right)$, 则只需证明

$$
(n-k) p^{3} \mid \prod_{i=n-k+1}^{n} f(p i)-\prod_{j=1}^{k} f(p j) .
$$

事实上, 我们有 $(x-y) p^{3} \mid f(p x)-f(p y)$ 对任意整数 $x, y$ 成立. 为此我们将 $f(x)$ 展开为 $x^{p-1}+S_{p-2} x^{p-2}+\cdots+S_{2} x^{2}+S_{1} x+S_{0}$, 则

$$
f(p x)-f(p y) \equiv S_{2} \cdot p^{2}\left(x^{2}-y^{2}\right)+S_{1} \cdot p(x-y) \quad\left(\bmod (x-y) p^{3}\right) .
$$

熟知在 $p>3$ 时有 $p \mid S_{2}$ 以及 $p^{2} \mid S_{1}$, 于是命题得证.

评注 重庆一中赵维捷, 哈尔滨第三中学刘香男, 北京四中林明锴, 杭州二中来栩杰, 江西师大附中陈冠伊, 华南师范大学附属中学冯宣瑞, 重庆南开中学伍垟圳, 山大附中王子或, 大连育明高中陶汉桥等同学也给出了本题的正确解答.

第三题 设 $k$ 是正整数, $x \geq k$ 是实数. 给定由至多 $\left(\begin{array}{l}x \\ k\end{array}\right)$ 个 $k$ 元集合构成的集族 $\mathcal{F}$, 证明: 至多存在 $\left(\begin{array}{c}x \\ k+1\end{array}\right)$ 个 $k+1$ 元集合, 满足它们的所有 $k$ 元子集均属于 $\mathcal{F}$.

(天津实验中学学生 解尧平 供题)

## 证明 (根据人大附中陈锐韬的解答整理):

我们对 $k$ 归纳证明, $k=1$ 时命题显然成立. 假设 $k-1$ 时成立, 考虑 $k$ 的情形. 将这个 $\left(\begin{array}{l}x \\ k\end{array}\right)$ 个 $k$ 元集合包含的所有元素无重复地记为 $1, \ldots, n$. 设包含 $i$ 的集合有 $\left(\begin{array}{c}d_{i} \\ k-1\end{array}\right)$ 个, 其中 $d_{i} \geq k-1$ 是一个实数. 则我们首先有

$$
\sum_{i=1}^{n} \frac{d_{i}}{k-1}=k \cdot\left(\begin{array}{l}
x \\
k
\end{array}\right)
$$

下面我们来求包含 $i$ 且满足条件的 $k+1$ 元集合的个数 $e_{i}$. 一方面, 由于每个这样的 $k+1$ 元集合除去 $i$ 后互不相同, 我们有 $e_{i} \leq\left(\begin{array}{l}x \\ k\end{array}\right)-\left(\begin{array}{c}d_{i} \\ k-1\end{array}\right)$. 另一方面, 将所有含 $i$ 的 $k$ 元集合与 $k+1$ 元集合同时除去 $i$, 则转化为 $k-1$ 时的问题. 故由归纳假设又有 $e_{i} \leq\left(\begin{array}{c}d_{i} \\ k\end{array}\right)$. 于是

$$
e_{i} \leq \min \left\{\left(\begin{array}{l}
x \\
k
\end{array}\right)-\left(\begin{array}{c}
d_{i} \\
k-1
\end{array}\right),\left(\begin{array}{c}
d_{i} \\
k
\end{array}\right)\right\} \leq \frac{x-k}{k} \cdot\left(\begin{array}{c}
d_{i} \\
k-1
\end{array}\right)
$$

后一不等式是因为当 $d_{i} \leq x-1$ 时 $\left(\begin{array}{c}d_{i} \\ k\end{array}\right) \leq \frac{x-k}{k} \cdot\left(\begin{array}{c}d_{i} \\ k-1\end{array}\right)$, 而当 $d_{i} \geq x-1$ 时 $\left(\begin{array}{l}x \\ k\end{array}\right)-\left(\begin{array}{c}d_{i} \\ k-1\end{array}\right) \leq \frac{x-k}{k} \cdot\left(\begin{array}{c}d_{i} \\ k-1\end{array}\right)$.

有了这个对 $e_{i}$ 的估计, 我们即知满足条件的 $k+1$ 元集合个数为

$$
\frac{\sum_{i=1}^{n} e_{i}}{k+1} \leq \frac{\frac{x-k}{k} \cdot \sum_{i=1}^{n}\left(\begin{array}{c}
d_{i} \\
k-1
\end{array}\right)}{k+1}=\frac{\frac{x-k}{k} \cdot k\left(\begin{array}{l}
x \\
k
\end{array}\right)}{k+1}=\left(\begin{array}{c}
x \\
k+1
\end{array}\right)
$$

命题得证.

评注 山大附中王子或以及重庆南开中学伍垟圳同学也给出了本题的正确解答.

第四题 给定平面上 $n$ 个模长不超过一的向量, 它们的和为零向量. 证明:对每个 $k \leq n$, 存在其中某 $k$ 个向量, 它们和的模长不超过一.

(耶鲁大学 牟晓生 供题)

## 证明 (根据供题者的解答整理):

我们将这个问题表示成代数形式: 给定向量 $\left\{v_{i}\right\}_{i=1}^{n}$, 满足 $\left|v_{i}\right| \leq 1$ 以及 $\sum_{i} v_{i}=\mathbf{0}$, 要找 $\epsilon_{i} \in\{0,1\}$ 使得 $\sum_{i} \epsilon_{i}=k$ 且 $\left|\sum_{i} \epsilon_{i} v_{i}\right| \leq 1$. 证明的关键是把这个离散的问题转化为连续的问题, 也就是先允许 $\epsilon_{i}$ 取 $[0,1]$ 中的实数值, 以保证 $\sum_{i} \epsilon_{i} v_{i}$ 的模长较小. 最后我们再进行调整, 把 $\epsilon_{i}$ 变成整数.

具体来说, 将 $v_{i}$ 写成 $\left(x_{i}, y_{i}\right)$ 的形式, 考虑如下关于 $\epsilon_{1}, \ldots, \epsilon_{n}$ 的线性方程组:

$$
\sum_{i=1}^{n} \epsilon_{i}=k ; \quad \sum_{i=1}^{n} \epsilon_{i} x_{i}=\sum_{i=1}^{n} \epsilon_{i} y_{i}=0 .
$$

注意到这个方程组在 $\epsilon_{i} \in[0,1]$ 里有解, 比如每个 $\epsilon_{i}=\frac{k}{n}$ 就是一组解. 所以一定存在一组 $\epsilon_{i} \in[0,1]$ 的解, 使得至多有三个 $\epsilon_{i}$ 不等于零或一. 否则,
假设 $\epsilon_{1}, \epsilon_{2}, \epsilon_{3}, \epsilon_{4} \in(0,1)$, 我们知道四个三维向量必定线性相关, 所以存在 $\delta_{1}, \delta_{2}, \delta_{3}, \delta_{4}$ 不全为零, 使得

$$
\delta_{1}\left(1, x_{1}, y_{1}\right)+\delta_{2}\left(1, x_{2}, y_{2}\right)+\delta_{3}\left(1, x_{3}, y_{3}\right)+\delta_{4}\left(1, x_{4}, y_{4}\right)=(0,0,0)
$$

因此对任意实数 $\lambda, \epsilon_{1}+\lambda \delta_{1}, \epsilon_{2}+\lambda \delta_{2}, \epsilon_{3}+\lambda \delta_{3}, \epsilon_{4}+\lambda \delta_{4}, \epsilon_{5}, \ldots, \epsilon_{n}$ 也是上述方程组的解. 适当地选取 $\lambda$ 可以保证每个新的 $\epsilon_{i}$ 仍在 $[0,1]$ 区间里, 且它们当中不等于零或一的个数比原来少. 这样反复操作最终可以保证至多三个 $\epsilon_{i}$ 不等于零或一.

下面我们分几种情况讨论:

(1) 如果每个 $\epsilon_{i}$ 都是零或一, 那么问题已然解决. 我们找到了某 $k$ 个向量和为零.

(2) 如果恰有一个 $\epsilon_{i}$ 不是零或一, 这是不可能的, 因为 $\sum_{i} \epsilon_{i}=k$ 是一个整数.

(3) 如果恰有两个 $\epsilon_{i}$ 不是零或一, 不妨设为 $\epsilon_{1}, \epsilon_{2}$. 则由 $\sum_{i} \epsilon_{i}=k$ 知 $\epsilon_{1}+\epsilon_{2}=1$. 不妨设 $\epsilon_{1} \leq \frac{1}{2}$. 令 $\epsilon_{1}^{\prime}=0, \epsilon_{2}^{\prime}=1$, 则

$$
\left|\epsilon_{1}^{\prime} v_{1}+\epsilon_{2}^{\prime} v_{2}-\epsilon_{1} v_{1}-\epsilon_{2} v_{2}\right|=\left|\epsilon_{1}\left(v_{2}-v_{1}\right)\right| \leq \frac{1}{2}\left|v_{2}-v_{1}\right| \leq 1
$$

所以将 $\epsilon_{1}, \epsilon_{2}$ 换成 $\epsilon_{1}^{\prime}, \epsilon_{2}^{\prime}$ 对最后的和 $\sum_{i} \epsilon_{i} v_{i}$ 的影响不超过一个模长为一的向量.结论成立.

(4) 如果恰有三个 $\epsilon_{i}$ 不是零或一, 不妨设为 $\epsilon_{1}, \epsilon_{2}, \epsilon_{3}$. 同上我们有 $\epsilon_{1}+\epsilon_{2}+$ $\epsilon_{3}$ 等于一或二.

首先考虑 $\epsilon_{1}+\epsilon_{2}+\epsilon_{3}=1$ 的情况. 此时将 $v_{1}, v_{2}, v_{3}$ 看成单位圆内的点 $A, B, C$, 则向量 $\epsilon_{1} v_{1}+\epsilon v_{2}+\epsilon v_{3}$ 对应 $\triangle A B C$ 内部的某个点 $X$. 不难证明 $X$ 与至少一个顶点的距离不超过 1 , 不妨设为顶点 $C$. 则将 $\epsilon_{1}, \epsilon_{2}, \epsilon_{3}$ 换成 $\epsilon_{1}^{\prime}=0, \epsilon_{2}^{\prime}=0, \epsilon_{3}^{\prime}=1$ 即知命题成立.

如果 $\epsilon_{1}+\epsilon_{2}+\epsilon_{3}=2$, 则向量 $\left(1-\epsilon_{1}\right) v_{1}+\left(1-\epsilon_{2}\right) v_{2}+\left(1-\epsilon_{3}\right) v_{3}$ 对应 $\triangle A B C$ 内部的某个点 $Y$. 假设 $Y$ 与顶点 $C$ 的距离不超过 1 , 则可以将 $\epsilon_{1}, \epsilon_{2}, \epsilon_{3}$ 换成 $\epsilon_{1}^{\prime}=1, \epsilon_{2}^{\prime}=1, \epsilon_{3}^{\prime}=0$, 对最后的和 $\sum_{i} \epsilon_{i} v_{i}$ 的影响也不超过 1.

综合上述情况, 命题得证!

评注 (1). 归纳法是这道题的一个自然思路, 但是操作过程中有些困难. 就我所知只能证明对每个 $k$, 存在某 $k$ 个或 $k+1$ 个向量, 它们和的模长不超过一. 例如美国国家队曾经考过 $n=101, k=50$ 的情况, 可以用归纳法解决(因为 $k=50$ 和 $k=51$ 是等价的).

(2). 有兴趣的同学可以研究本题结论的高维推广.

