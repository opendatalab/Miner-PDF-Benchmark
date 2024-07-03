# 第十七期问题征解解答与点评 

牟晓生

第一题. 如图, $A D, B E$ 分别是锐角 $\triangle A B C$ 的边 $B C, A C$ 上的高. $A B$ 中点为 $M$ ，直线 $D E$ 交 $\triangle A B C$ 的外接圆于点 $F, K$, 线段 $M K$ 和 $M F$ 分别与 $\triangle M D E$ 的外接圆交于除 $M$ 以外的点 $P, Q$. 证明: $A, P, Q, B$ 四点共圆.



(福建厦门一中 徐小平 供题)

## 证明 (根据如东高级中学张陈成同学的解答整理):

由于 $B E \perp A C, A D \perp B C$, 我们有 $A, B, D, E$ 四点共圆, 而 $M$ 为圆心. 于是 $\angle M D K=\angle M D E=\angle M E D=\angle M P D$, 其中最后一步由 $E, D, M, P$ 共圆.

于是可知 $M D^{2}=M P \cdot M K$, 同理 $M D^{2}=M Q \cdot M F$. 从而 $F, Q, P, K$共圆. 另外由 $M A^{2}=M D^{2}=M P \cdot M K$ 可知 $\angle A P M=\angle M A K$. 而由 $M B^{2}=M D^{2}=M Q \cdot M F$ 可知 $\angle M B Q=\angle M F B$. 所以

$$
\begin{aligned}
\angle A P Q+\angle A B Q & =\angle A P M+\angle M P Q+\angle M F B \\
& =\angle M A K+\angle M F K+\angle M F B \\
& =\angle B A K+\angle B F K=180^{\circ} .
\end{aligned}
$$

命题得证!
评注 浙江省桐乡市高级中学顾文影, 象山县第三中学黄子宸, 黄冈中学陈耀斌, 镇海中学严君啸, 湖南师大附中刘其灵, 东北育才何雨桐, 杭州二中刘浩宇等同学以及雅礼中学团队也给出了本题的正确解答.

第二题. 证明对任意正整数 $n$ 以及任意实数 $x_{1}, x_{2}, \ldots, x_{n}$, 都有

$$
\sum_{k=1}^{n}\left(\frac{1}{k} \sum_{j=1}^{k} x_{j}\right)^{2} \leq \sum_{k=1}^{n}(k+1) x_{k}^{2}
$$

(湖南师大附中 羊明亮 供题)

## 证明 (根据湖南雅礼中学邱添同学的解答整理):

对 $1 \leq k \leq n$, 由柯西不等式得:

$$
\left(\sum_{j=1}^{k} x_{j}\right)^{2} \leq\left(\sum_{j=1}^{k} j(j+1) x_{j}^{2}\right)\left(\sum_{j=1}^{k} \frac{1}{j(j+1)}\right)=\frac{k}{k+1} \sum_{j=1}^{k} j(j+1) x_{j}^{2}
$$

因此求和可得:

$$
\sum_{k=1}^{n}\left(\frac{1}{k} \sum_{j=1}^{k} x_{j}\right)^{2} \leq \sum_{k=1}^{n} \frac{1}{k(k+1)} \sum_{j=1}^{k} j(j+1) x_{j}^{2}=\sum_{j=1}^{n} j(j+1) x_{j}^{2} \sum_{k=j}^{n} \frac{1}{k(k+1)}
$$

等式最右边确实小于 $\sum_{j=1}^{n}(j+1) x_{j}^{2}$.

评注 (1). 浙江省桐乡市高级中学顾文影, 湖南师大附中刘其灵, 如东高级中学张陈成, 东北育才何雨桐以及雅礼中学团队也给出了本题的正确解答.

(2). 这个问题形似 Hardy 不等式, 却又不太一样. 应对这类问题一般有两种方法, 其一是适当地配选 Cauchy 或 Hölder 不等式的系数, 如上面解答所展示的那样. 另一种方法则是用归纳法证明加强命题. 在这里可以证明右边比左边至少大 $\frac{1}{n}\left(\sum_{k=1}^{n} x_{k}\right)^{2}$, 有些同学就是这么做的.

第三题. 如图, $G e$ 是 $\triangle A B C$ 的 Gergonne 点, $c_{1}$ 是过 $G e$ 且与 $A B, A C$ 相切的圆中较小的那个, 类似定义 $c_{2}, c_{3}$. 设 $c_{1}, c_{2}, c_{3}$ 两两间的另一条外公切线彼此交于 $P, Q, R$. 证明: $\triangle A B C$ 的内心 $I, \triangle P Q R$ 的内心 $I^{\prime}$ 以及 $G e$ 三点共线.

(北京人大附中学生 杨泓梀 供题)

## 证明 (根据吉大附中李濛初和初炜康同学的解答整理):

记 $I$ 在 $B C, C A, A B$ 上的射影为 $I_{1}, I_{2}, I_{3} . c_{1}$ 与 $A B, A C$ 相切于 $A_{3}, A_{2}, c_{2}$与 $A B, B C$ 相切于 $B_{3}, B_{1}, c_{3}$ 与 $A C, B C$ 相切于 $C_{2}, C_{1}$. 设 $c_{3}, c_{1}$ 与 $P R$ 分别切于 $K, L$, 而 $c_{2}, c_{1}$ 与 $P Q$ 分别切于 $S, T$.



由定义, $G_{e}$ 在 $A I_{1}, B I_{2}, C I_{3}$ 上. 由于 $B$ 为 $c_{2}$ 与内切圆的外位似中心, $G_{e}, I_{2}$是这个位似中的对应点, 所以 $\frac{B_{1} I_{1}}{B I_{1}}=\frac{G e I_{2}}{B I_{2}}$. 同理 $\frac{C_{1} I_{1}}{C I_{1}}=\frac{G e I_{3}}{C I_{3}}$. 对 $\triangle B G_{e} C$ 以及点 $A$ 用 Ceva 定理, 我们有:

$$
\frac{B I_{1}}{I_{1} C} \cdot \frac{C I_{3}}{I_{3} G_{e}} \cdot \frac{G_{e} I_{2}}{I_{2} B}=1
$$

利用之前得到的结论, 也就是:

$$
\frac{B I_{1}}{I_{1} C} \cdot \frac{C I_{1}}{C_{1} I_{1}} \cdot \frac{B_{1} I_{1}}{I_{1} B}=1
$$

化简得到 $B_{1} I_{1}=C_{1} I_{1}$. 由于 $B I_{1}=B I_{3}, B B_{1}=B B_{3}$, 我们又有 $B_{1} I_{1}=B_{3} I_{3}$.于是可得:

$$
B_{1} I_{2}=I_{1} C_{1}=C_{2} I_{2}=I_{2} A_{2}=A_{3} I_{3}=I_{3} B_{3} .
$$

所以 $I_{1}$ 在 $c_{2}, c_{3}$ 的根轴上, 而这个根轴就是 $A G_{e} I_{1}$. 注意到 $L K, A_{2} C_{2}$ 均为 $c_{1}, c_{3}$的外公切线, 所以 $L K=A_{2} C_{2}$. 同理 $S T=A_{3} C_{3}$, 于是 $L K=S T$. 而 $P L=P T$,故 $P K=P S$. 这说明 $P$ 到 $c_{2}, c_{3}$ 等幂, 于是 $P$ 在根轴 $A G_{e} I_{1}$ 上. 由对称性, $A P, B Q, C R$ 共点于 $G_{e}$.

设圆 $I$ 与圆 $I^{\prime}$ 的外位似中心为 $O$. 由于 $c_{1}$ 与这两个圆的外位似中心分别为 $A, P$, 我们知道 $A, P, O$ 共线. 同理 $O$ 也在 $B Q, C R$ 上. 所以 $O=G_{e}$. 于是 $I, I^{\prime}, G_{e}$ 三点共线.

评注 如东高级中学张陈成, 象山县第三中学黄子宸, 湖南师大附中刘其灵,东北育才何雨桐, 雅礼中学尹龙晖, 丘添, 李师铨, 谢添乐, 李正浩, 肖澍旸等同学也给出了本题的正确解答.
第四题. 设 $f(x)$ 是一个复系数多项式, 满足

$$
x^{2} \left\lvert\, f(x)-e^{\frac{2 \pi i}{m}} \cdot x\right.
$$

其中 $m>1$ 是给定的正整数. 令 $f^{(m)}(x)$ 为 $f$ 的 $m$ 次迭代, 证明:

$$
x^{m+1} \mid f^{(m)}(x)-x .
$$

(清华大学 刘畅 供题)

## 证明 (根据供题者的解答整理):

我们首先证明如下引理:

引理 设 $\lambda$ 是复数, $k>1$ 是正整数, 满足 $\lambda^{k} \neq \lambda$. 如果多项式 $f, P$ 满足 $x^{k} \mid f \circ P-P(\lambda x)$, 且 $P(0)=0, P^{\prime}(0) \neq 0$. 则存在多项式 $R$ 满足 $x^{k+1} \mid f \circ R-$ $R(\lambda x)$, 且 $R(0)=0, R^{\prime}(0) \neq 0$.

为证引理, 设 $f \circ P-P(\lambda x)=b x^{k}+O\left(x^{k+1}\right)$, 其中 $O\left(x^{k+1}\right)$ 表示次数至少是 $k+1$ 的高阶多项式. 考虑取 $R(x)=P\left(x+c x^{k}\right)$. 那么

$$
\begin{aligned}
f \circ R & =f \circ P \circ\left(x+c x^{k}\right) \\
& =P\left(\lambda x+c \lambda x^{k}\right)+b\left(x+c x^{k}\right)^{k}+O\left(x+c x^{k}\right)^{k+1} \\
& =P(\lambda x)+c \lambda P^{\prime}(0) x^{k}+b x^{k}+O\left(x^{k+1}\right) .
\end{aligned}
$$

另一方面

$$
\begin{aligned}
R(\lambda x) & =P\left(\lambda x+c(\lambda x)^{k}\right) \\
& =P(\lambda x)+c \lambda^{k} P^{\prime}(0) x^{k}+O\left(x^{k+1}\right)
\end{aligned}
$$

对比 (1) 和 (2), 我们只要令 $c=\frac{b}{\lambda^{k}-\lambda}$ 就能满足 $x^{k+1} \mid f \circ R-R(\lambda x)$. 最后注意到 $R^{\prime}(x)=P^{\prime}\left(x+c x^{k}\right)\left(1+c k x^{k-1}\right)$. 所以 $R^{\prime}(0)=P^{\prime}(0) \neq 0 . R(0)=P(0)=0$是显然的. 引理证毕.

回到原题, 取 $P(x)=x, \lambda=e^{\frac{2 \pi i}{m}}, k=2$, 由题目假设有 $x^{k} \mid f \circ P-P(\lambda x)$.反复运用引理, 我们最终得到多项式 $R(x)$, 使得 $f \circ R=R(\lambda x)+O\left(x^{m+1}\right)$. 于是

$$
\begin{aligned}
f^{(2)} \circ R & =f \circ(f \circ R) \\
& =f\left(R(\lambda x)+O\left(x^{m+1}\right)\right) \\
& =f(R(\lambda x))+O\left(x^{m+1}\right) \\
& =R\left(\lambda^{2} x\right)+O\left(x^{m+1}\right)
\end{aligned}
$$

其中第三行用到 $x \mid f(x)$. 用归纳法不难证明对每个正整数 $k$ 都有

$$
f^{(k)} \circ R=R\left(\lambda^{k} x\right)+O\left(x^{m+1}\right) .
$$

特别地, 我们有

$$
f^{(m)} \circ R=R(x)+O\left(x^{m+1}\right) .
$$

此时设 $f^{(m)}(x)=a_{1} x+a_{2} x^{2}+\cdots+a_{m} x^{m}+O\left(x^{m+1}\right)$, 则 $f^{(m)} \circ R=a_{1} R+$ $a_{2} R^{2}+\cdots+a_{m} R^{m}+O\left(x^{m+1}\right)$, 因为 $R(x)^{m+1}=O\left(x^{m+1}\right)$. 于是 (5) 式导出

$$
a_{1} R+a_{2} R^{2}+\cdots+a_{m} R^{m}=R+O\left(x^{m+1}\right) .
$$

由于 $R(0)=0, R^{\prime}(0) \neq 0$, 对比两边 $x^{1}$ 的系数得到 $a_{1}=1$. 之后依次对比 $x^{2}, x^{3}, \ldots, x^{m}$ 的系数得到 $a_{2}=a_{3}=\cdots=a_{m}=0$. 于是 $f^{(m)}(x)=x+O\left(x^{m+1}\right)$,命题得证!

评注 (1). 湖南师大附中刘其灵同学通过组合方法计算高阶导数也给出了本题的正确解答.

(2). 我们可以把 $f \circ P-P(\lambda x)=O\left(x^{k}\right)$ 改写为 $P^{-1} \circ f \circ P=\lambda x+O\left(x^{k}\right)$.这样上面的引理就是函数方程中的桥函数方法 (或者矩阵理论里的正规化). 虽然在竞赛中考的很少, 但桥函数是处理迭代问题的重要工具. 在这里 $P$ 是多项式, 所以反函数 $P^{-1}$ 并不好定义, 上面的解答避开了这个问题 (当然利用复变函数的知识可以局部地定义 $P^{-1}$, 也能完成证明).

