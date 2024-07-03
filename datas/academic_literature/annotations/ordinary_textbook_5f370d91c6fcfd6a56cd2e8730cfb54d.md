# 一道俄罗斯不等式试题简析 

尹龙晖<br>(湖南省雅礼中学, 410007)<br>指导教师: 申东

2015 年俄罗斯数学奥林匹克 11 年级试题中有一道不等式问题:

问题 1 设实数 $a, b, c, d$ 满足 $|a|>1,|b|>1,|c|>1,|d|>1$, 且

$$
a b(c+d)+d c(a+b)+a+b+c+d=0
$$

证明:

$$
\frac{1}{a-1}+\frac{1}{b-1}+\frac{1}{c-1}+\frac{1}{d-1}>0 .
$$

冷岗松老师在新星夏令营上向我们介绍了如下解法:

证明 条件中的等式等价于 $\prod(a+1)=\prod(a-1)$, 即 $\prod \frac{a+1}{a-1}=1$. 又注意到

$$
\frac{a+1}{a-1}>0, \frac{b+1}{b-1}>0, \frac{c+1}{c-1}>0, \frac{d+1}{d-1}>0,
$$

故由均值不等式便得

$$
\sum \frac{1}{a-1}=\frac{1}{2} \sum \frac{a+1}{a-1}-2 \geq 2 \sqrt[4]{\prod \frac{a+1}{a-1}}-2=0
$$

且上式等号成立须 $a=b=c=d$, 这时由条件易推知 $|a|=1$, 矛盾! 故上式不取等号, 也即要证不等式成立.

由这个做法, 立得问题 1 的如下自然推广:

问题 2 设 $a_{1}, a_{2}, \cdots, a_{n} \in \mathbf{R}$ 满足 $\left|a_{i}\right|>1, i=1,2, \cdots, n$. 且

$$
\prod_{i=1}^{n}\left(a_{i}+1\right)=\prod_{i=1}^{n}\left(a_{i}-1\right)
$$

则

$$
\sum_{i=1}^{n} \frac{1}{a_{i}-1}>0
$$

在学习过程中, 我发现了一个新证法. 这个证法尽管用了一些微积分的知识,
但使我们更能看清问题的本质, 并得到一个新的推广.

下面是我给出的问题 2 的新证明:

证明 令 $f(x)=\prod_{i=1}^{n}\left(x-a_{i}\right)$, 则 $f(x)$ 是一个实多项式, 且

$$
\frac{f^{\prime}(x)}{f(x)}=\sum_{i=1}^{n} \frac{1}{x-a_{i}}
$$

记 $g(x)=\frac{f^{\prime}(x)}{f(x)}$, 则

$$
g^{\prime}(x)=-\sum_{i=1}^{n} \frac{1}{\left(x-a_{i}\right)^{2}} \leq 0 .
$$

这说明 $g(x)$ 在 $\mathbf{R}$ 上单调递减.

又由条件知 $f(1)=f(-1)$, 应用罗尔定理知, 存在 $r \in(-1,1)$ 使得 $f^{\prime}(r)=0$.又注意到 $f(r) \neq 0$, 所以 $g(r)=\frac{f^{\prime}(r)}{f(r)}=0$. 故由 $g(x)$ 的单调性立得

$$
g(-1)>g(r)=0>g(1) .
$$

由 $g(1)<0$ 立得所证不等式

$$
\sum_{i=1}^{n} \frac{1}{1-a_{i}}<0
$$

上面的证法使我们能清楚地看出问题中的条件的作用和地位. 这样, 我们得到了如下的推广形式:

问题 3 设 $f(x)=\prod_{i=1}^{n}\left(x-a_{i}\right), a_{i} \in \mathbf{R}, i=1,2, \cdots, n$. 实数 $\alpha, \beta$ 满足

(i) $f(\alpha)=f(\beta)$;

(ii) $[\alpha, \beta] \cap\left\{a_{1}, a_{2}, \cdots, a_{n}\right\}=\emptyset$.

则

$$
\sum_{i=1}^{n} \frac{1}{\alpha-a_{i}}>0, \text { 且 } \sum_{i=1}^{n} \frac{1}{\beta-a_{i}}<0 .
$$

证明完全类似于上面的解法. 关键的一步是证明存在 $r \in(\alpha, \beta)$ 使得

$$
\sum_{i=1}^{n} \frac{1}{r-a_{i}}=0
$$

具体过程这里从略.

当然, 问题 3 可写得更隐蔽, 难度似乎更大.

问题 4 设 $f(x)=\prod_{i=1}^{n}\left(x-a_{i}\right), a_{i} \in \mathbf{R}, i=1,2, \cdots, n$. 实数 $\alpha, \beta$ 满足 (i) $f(\alpha)=f(\beta)$;
(ii) $[\alpha, \beta] \cap\left\{a_{1}, a_{2}, \cdots, a_{n}\right\}=\emptyset$.

则

$$
\sum_{i=1}^{n}\left(\frac{1}{\alpha-a_{i}}-\frac{1}{\beta-a_{i}}\right)>0
$$

上述问题的结论还可进一步拓广到非多项式的实函数上, 这里不再介绍.

