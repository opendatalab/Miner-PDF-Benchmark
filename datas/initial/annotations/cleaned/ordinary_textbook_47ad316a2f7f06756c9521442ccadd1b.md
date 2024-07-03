# 一道伊朗组合试题的新解 

冷岗松

2004 年伊朗大学生数学竞赛中有这样一道组合试题:

问题 设 $r, k$ 都是固定的整数 $(r, k \geq 2), X_{r}$ 是集合 $X$ 的所有 $r$ 元子集构成的集合, $F \subseteq X_{r}$ 且满足 $F$ 中的任意 $k$ 个元的交非空. 记

$$
I(F)=\min \{|T|: T \subseteq X, T \cap A \neq \emptyset, \forall A \in F\} .
$$

证明:

$$
I(F) \leq \frac{r-1}{k-1}+1
$$

我们没有能够发现这个问题的最先出处, 仅查到它曾出现在 Lovász 的专著 $[1, \mathrm{p} .80]$中.

这篇短的注记介绍这个组合问题的两个解法, 解法一是标准答案 (也同 [1] 中的解法);解法二是上海中学学生高继扬 (2014年 IMO 满分金牌获得者) 给出的, 吉林大学附属中学的郝天泽同学也独立给出了类似的解法.

解法一 要证 (1), 只须证明下面更一般的结论: 对任意 $j \leq k, j \in N^{*}$, 存在 $A_{1}, A_{2}, \cdots, A_{j} \in F$, 使得

$$
\left|A_{1} \cap \cdots \cap A_{j}\right| \leq r-(j-1)(I(F)-1) .
$$

事实上, 在 (2) 中取 $j=k$ 并注意到 $\left|A_{1} \cap \cdots \cap A_{j}\right| \geq 1$ 便立得要证的不等式 (1).

对 $j$ 用归纳法证明 (2):

当 $j=1$ 时, $F$ 中的任何元 $A_{1}$ 满足 $\left|A_{1}\right|=r,(2)$ 显然成立.

假设 (2) 对 $j(j \leq k-1)$ 成立，下面考察 $j+1$ 的情况.

任取 $F$ 中的 $j$ 个元 $A_{1}, A_{2}, \cdots, A_{j}(j \leq k-1)$, 由条件知 $A_{1} \cap \cdots \cap A_{j}$ 与 $F$ 中的任何一个元都有非空的交, 故由 $I(F)$ 的定义知

$$
\left|A_{1} \cap \cdots \cap A_{j}\right| \geq I(F) .
$$

不妨设 $I(F)>1$, 再取 $S \subseteq A_{1} \cap \cdots \cap A_{j}$ 且 $|S|=I(F)-1$, 则由 $I(F)$ 的定义知存在一个 $A_{j+1} \in F$ 使得

$$
S \cap A_{j+1}=\emptyset .
$$

故

$$
\begin{aligned}
\left|A_{1} \cap \cdots \cap A_{j} \cap A_{j+1}\right| & \leq\left|A_{1} \cap \cdots \cap A_{j} \cap S^{c}\right| \\
& =\left|A_{1} \cap \cdots \cap A_{j} \backslash S\right| \\
& =\left|A_{1} \cap \cdots \cap A_{j}\right|-(I(F)-1) \\
& \leq r-(j-1)(I(F)-1)-(I(F)-1) \\
& =r-j(I(F)-1) .
\end{aligned}
$$

这说明 (2) 对 $j+1$ 成立. 这样我们就完成了证明.

解法二 任取 $A \in F,|A|=r$. 因

$$
(k-1)\left(\left[\frac{r-1}{k-1}\right]+1\right) \geq(k-1) \frac{r}{k-1}=r .
$$

所以可将 $A$ 划分为 $k-1$ 个集合 $A_{1}, A_{2}, \cdots, A_{k-1}$ 满足

$$
\bigcup_{i=1}^{k-1} A_{i}=A, \quad \text { 且 } \quad\left|A_{i}\right| \leq\left[\frac{r-1}{k-1}\right]+1, i=1,2, \cdots, k-1 .
$$

若对任意 $1 \leq i \leq k-1, A_{i}$ 不满足: 对任意 $B \in F, B \cap A_{i} \neq \emptyset$. 那么存在 $B_{i} \in F$, 使得

$$
B_{i} \cap A_{i}=\emptyset, i=1,2, \cdots, k-1 .
$$

由条件, $A, B_{1}, B_{2}, \cdots, B_{k-1}$ 的交非空, 即存在 $x \in X$, 使得 $x \in A, x \in B_{1}, \cdots, x \in$ $B_{k-1}$. 又

$$
\bigcup_{i=1}^{k-1} A_{i}=A
$$

所以存在 $i \in\{1,2, \cdots, k-1\}$ 使得 $x \in A_{i}$. 因此 $x \in A_{i} \cap B_{i}$. 这与 $A_{i} \cap B_{i}=\emptyset$ 矛盾!

这就说明 $A_{1}, A_{2}, \cdots, A_{k-1}$ 中存在 $A_{j} \in\{T \mid T \subseteq X, T \cap A \neq \emptyset, \forall A \in F\}$. 故

$$
I(F) \leq\left|A_{j}\right| \leq\left[\frac{r-1}{k-1}\right]+1 \leq \frac{r-1}{k-1}+1 .
$$

评注 高继扬的解法二从 $F$ 中的一个集合 $A$ 出发, 构造了元素个数 $\left[\frac{r-1}{k-1}\right]+1$ 的 $A_{j} \in\{T \mid T \subseteq X, T \cap A \neq \emptyset, \forall A \in F\}$, 手法直接而简明, 值得品味!

## 参考文献

[1] L. Lovász, Combinatorial Problems and Exercises, North-Holland Publishing Company, Amsterdam. New York. Oxford, 1979.

