# Figalli 不等式的初等证明 

罗横溢胡子轩

(湖南师范大学附属中学, 410008)

指导教师: 张湘君

Figalli (2018 菲尔茨奖得主) 在文 [1] 中, 利用分析方法建立了下述不等式 (这个不等式是这篇文章中一个重要的引理):

定理 设实数 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$ 满足 $0<\lambda_{1} \leq \lambda_{2} \leq \cdots \leq \lambda_{n}$. 记

$$
\lambda_{A}=\frac{1}{n} \sum_{k=1}^{n} \lambda_{k}, \lambda_{G}=\left(\prod_{k=1}^{n} \lambda_{k}\right)^{\frac{1}{n}}
$$

则

$$
7 n^{2}\left(\lambda_{A}-\lambda_{G}\right) \geq \frac{1}{\lambda_{n}} \sum_{k=1}^{n}\left(\lambda_{k}-\lambda_{G}\right)^{2}
$$

冷岗松教授将这个问题给了我们, 并希望得到一个初等证明. 下面, 我们给出该不等式的初等证明.

证明 注意到不等式除 $\lambda_{1}=\lambda_{2}=\cdots=\lambda_{n}$ 外无明显的取等. 我们用 $f(n)$ 替换 $7 n^{2}$, 探索不等式对怎样的 $f(n)$, 下述不等式成立:

$$
f(n)\left(\lambda_{A}-\lambda_{G}\right) \geq \frac{1}{\lambda_{n}} \sum_{k=1}^{n}\left(\lambda_{k}-\lambda_{G}\right)^{2} .
$$

若 $\lambda_{A}=\lambda_{G}$, 则 $\lambda_{1}=\lambda_{2}=\cdots=\lambda_{n}$, 从而 (1) 式恒成立.

若 $\lambda_{A}>\lambda_{G}$. 注意到

$$
\begin{aligned}
\sum_{k=1}^{n}\left(\lambda_{k}-\lambda_{G}\right)^{2} & =\sum_{k=1}^{n} \lambda_{k}^{2}-2\left(\sum_{k=1}^{n} \lambda_{k}\right) \lambda_{G}+n \lambda_{G}^{2} \\
& =\sum_{k=1}^{n} \lambda_{k}^{2}-2 n \lambda_{A} \lambda_{G}+n \lambda_{G}^{2} \\
& =\frac{\sum_{1 \leq i<j \leq n}\left(\lambda_{i}-\lambda_{j}\right)^{2}}{n}+\frac{\left(\sum_{k=1}^{n} \lambda_{k}\right)^{2}}{n}-2 n \lambda_{A} \lambda_{G}+n \lambda_{G}^{2}
\end{aligned}
$$

收稿日期: 2018-09-05; 修订日期: 2018-11-15.

$$
=n\left(\lambda_{A}-\lambda_{G}\right)^{2}+\frac{\sum_{1 \leq i<j \leq n}\left(\lambda_{i}-\lambda_{j}\right)^{2}}{n},
$$

故若要 $(1)$ 成立, 只需

$$
f(n) \geq \frac{1}{\lambda_{n}}\left(n\left(\lambda_{A}-\lambda_{G}\right)+\frac{\sum_{1 \leq i<j \leq n}\left(\lambda_{i}-\lambda_{j}\right)^{2}}{n\left(\lambda_{A}-\lambda_{G}\right)}\right)
$$

由 $\lambda_{A}-\lambda_{G}<\lambda_{A} \leq \lambda_{n}$ 知

$$
\frac{n\left(\lambda_{A}-\lambda_{G}\right)}{\lambda_{n}}<n
$$

注意到

$$
\begin{aligned}
\left(\lambda_{i}-\lambda_{j}\right)^{2} & =\left(\sqrt{\lambda_{i}}+\sqrt{\lambda_{j}}\right)^{2}\left(\sqrt{\lambda_{i}}-\sqrt{\lambda_{j}}\right)^{2} \\
& \leq\left(2 \sqrt{\lambda_{n}}\right)^{2}\left(\sqrt{\lambda_{i}}-\sqrt{\lambda_{j}}\right)^{2} \\
& =4 \lambda_{n}\left(\lambda_{i}+\lambda_{j}-2 \sqrt{\lambda_{i} \lambda_{j}}\right) .
\end{aligned}
$$

由 $(2),(3),(4)$ 知, 要使 $(1)$ 成立, 只需

$$
\begin{gathered}
f(n) \geq n+\frac{4 \sum_{1 \leq i<j \leq n}\left(\lambda_{i}+\lambda_{j}-2 \sqrt{\lambda_{i} \lambda_{j}}\right)}{n\left(\lambda_{A}-\lambda_{G}\right)} \\
\Leftrightarrow(f(n)-n) n\left(\lambda_{A}-\lambda_{G}\right) \geq 4 \sum_{1 \leq i<j \leq n}\left(\lambda_{i}+\lambda_{j}-2 \sqrt{\lambda_{i} \lambda_{j}}\right) \\
=4 n(n-1) \lambda_{A}-8 \sum_{1 \leq i<j \leq n} \sqrt{\lambda_{i} \lambda_{j}} \\
\Leftrightarrow(f(n)-5 n+4) n \lambda_{A}+8 \sum_{1 \leq i<j \leq n} \sqrt{\lambda_{i} \lambda_{j}} \geq(f(n)-n) n \lambda_{G} .
\end{gathered}
$$

由均值不等式知

$$
8 \sum_{1 \leq i<j \leq n} \sqrt{\lambda_{i} \lambda_{j}} \geq 8 \cdot \frac{n(n-1)}{2} \lambda_{G}=(4 n-4) n \lambda_{G}
$$

结合上式和 $\lambda_{A} \geq \lambda_{G}$ 知, 若 $f(n) \geq 5 n-4$, 则 (5) 式成立, 从而 (1) 也成立.

特别地, 当 $f(n)=7 n^{2}$ 时, $7 n^{2}+4>5 n$, 故原不等式成立.

评注 此不等式的证明具有一定难题, 关键在于对 $\sum_{k=1}^{n}\left(\lambda_{k}-\lambda_{G}\right)^{2}$ 展开后 $\sum_{k=1}^{n} \lambda_{k}^{2}$ 的处理. 笔者开始将其放为 $n \lambda_{A} \lambda_{n}$ (即将 $\lambda_{i}^{2}$ 放为 $\lambda_{i} \lambda_{n}$ ), 并且自认为放得很好, 因为保证了仍可取等, 并且降低了幂次. 但尝试后发现这样无法处理最大的 拦路虎”: 要证不等式左边的 $\lambda_{A}-\lambda_{G}$.

在上面的证明中, 我们将变量都移到不等式右侧. 利用拉格朗日恒等式和均值不等式证明了结论. 并且常数 $7 n^{2}$ 可优化为 $5 n-4$.

## 参考文献

[1] Figalli, A.; Maggi, F.; Pratelli, A. A mass transportation approach to quantitative isoperimetric inequalities. Invent. Math. 182 (2010), no. 1, 167 - 211.

