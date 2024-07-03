# 一道罗马尼亚 TST 试题的简解 

王淳稷<br>(上海市上海中学, 200231)<br>指导教师: 王广廷

2018 年罗马尼亚 TST 试题中有一个难度很大的问题. 本文给出这个问题的一个简解.

原题 设 $n \geq 2$ 为给定的整数, 求下述式子的整数部分

$$
\sum_{k=1}^{n-1} \frac{1}{\left(1+\frac{1}{n}\right) \cdots\left(1+\frac{k}{n}\right)}-\sum_{k=1}^{n-1}\left(1-\frac{1}{n}\right) \cdots\left(1-\frac{k}{n}\right) .
$$

解 记

$$
S=\sum_{k=1}^{n-1} \frac{1}{\left(1+\frac{1}{n}\right) \cdots\left(1+\frac{k}{n}\right)}-\sum_{k=1}^{n-1}\left(1-\frac{1}{n}\right) \cdots\left(1-\frac{k}{n}\right) .
$$

注意到

$$
\frac{1}{\left(1+\frac{1}{n}\right) \cdots\left(1+\frac{k}{n}\right)}>\left(1-\frac{1}{n}\right) \cdots\left(1-\frac{k}{n}\right)
$$

故 $S>0$. 下证 $S<1$.

事实上,

$$
S<\sum_{k=1}^{n} \frac{1}{\left(1+\frac{1}{n}\right) \cdots\left(1+\frac{k}{n}\right)}-\sum_{k=1}^{n-1}\left(1-\frac{1}{n}\right) \cdots\left(1-\frac{k}{n}\right) .
$$

又由于

$$
\begin{aligned}
& \sum_{k=1}^{n} \frac{1}{\left(1+\frac{1}{n}\right) \cdots\left(1+\frac{k}{n}\right)}-\sum_{k=1}^{n-1}\left(1-\frac{1}{n}\right) \cdots\left(1-\frac{k}{n}\right) \\
& =\sum_{k=1}^{n}\left(\frac{n}{n+1} \cdot \frac{n}{n+2} \cdots \frac{n}{n+k}-\frac{n-1}{n} \cdot \frac{n-2}{n} \cdots \frac{n-k}{n}\right) \\
& =\sum_{k=1}^{n}\left(\sum_{l=1}^{k} \frac{n}{n+1} \cdots \frac{n}{n+l-1} \cdot \frac{n-l-1}{n} \cdots \frac{n-k}{n}\left(\frac{n}{n+l}-\frac{n-l}{n}\right)\right)
\end{aligned}
$$

修订日期: 2022-10-28.

$$
\begin{aligned}
& =\sum_{k=1}^{n} \sum_{l=1}^{k} \frac{n}{n+1} \cdot \frac{n}{n+2} \cdots \frac{n}{n+l-1} \cdot \frac{l^{2}}{n(n+l)} \cdot \frac{n-l-1}{n} \cdots \frac{n-k}{n} \\
& =\sum_{k=1}^{n} \sum_{l=1}^{k} \frac{n^{l-2} \cdot l^{2}}{(n+1)(n+2) \cdots(n+l)} \cdot \frac{n-l-1}{n} \cdot \frac{n-l-2}{n} \cdots \frac{n-k}{n} \\
& =\sum_{l=1}^{n} \sum_{k=l}^{n} \frac{n^{l-2} \cdot l^{2}}{(n+1)(n+2) \cdots(n+l)} \cdot \frac{n-l-1}{n} \cdot \frac{n-l-2}{n} \cdots \frac{n-k}{n} \\
& \leq \sum_{l=1}^{n} \frac{n^{l-2} \cdot l^{2}}{(n+1)(n+2) \cdots(n+l)} \cdot \sum_{k=l}^{n}\left(\frac{n-l}{n}\right)^{k-l} \\
& \leq \sum_{l=1}^{n} \frac{n^{l-2} \cdot l^{2}}{(n+1)(n+2) \cdots(n+l)} \cdot \frac{1}{1-\frac{n-l}{n}} \\
& =\sum_{l=1}^{n} \frac{n^{l-1} \cdot l}{(n+1)(n+2) \cdots(n+l)}=\sum_{l=1}^{n} \frac{n^{l-1} \cdot[(n+l)-n]}{(n+1)(n+2) \cdots(n+l)} \\
& =1-\frac{n}{n+1}+\sum_{l=2}^{n}\left[\frac{n^{l-1}}{(n+1) \cdots(n+l-1)}-\frac{n^{l}}{(n+1) \cdots(n+l)}\right] \\
& =1-\frac{n^{n}}{(n+1)(n+2) \cdots(2 n)}<1 .
\end{aligned}
$$

故 $0<S<1$, 即所求式子的整数部分为 0 .

