# 一个不等式猜测的证明 

## 牟晓生

(哈佛大学, xiaoshengmu@fas.harvard.edu)

本文给出了赵斌在数学新星网第九期问题征解上提出的一个不等式猜想的肯定回答, 得到如下定理:

定理. 设 $n$ 是正整数, 实数 $x_{1}, x_{2}, \cdots, x_{n}$ 满足 $0<x_{1} \leq x_{2} \leq \cdots \leq x_{n}$ 且 $x_{1} x_{2} \cdots x_{n}=1$, 则不等式

$$
x_{1}+x_{2}^{2}+\cdots+x_{n}^{n} \geq x_{1}^{-1}+x_{2}^{-2}+\cdots+x_{n}^{-n} .
$$

对所有正整数 $n$ 都成立.

证明 令 $x_{k}=e^{\alpha_{k}}$, 则条件变为 $\alpha_{1} \leq \alpha_{2} \leq \cdots \leq \alpha_{n}$ 且 $\sum_{k} \alpha_{k}=0$. 这个代换将原不等式 (1) 转化为

$$
\sum_{k=1}^{n}\left(e^{k \alpha_{k}}-e^{-k \alpha_{k}}\right) \geq 0
$$

根据熟知的积分公式, (2) 等价于

$$
\sum_{k=1}^{n} \int_{-k \alpha_{k}}^{k \alpha_{k}} e^{y} d y \geq 0
$$

也就是

$$
\sum_{k=1}^{n} \int_{0}^{k \alpha_{k}}\left(e^{y}+e^{-y}\right) d y \geq 0
$$

注意在 (3) 和 (4) 中, 积分的上限有时会小于其下限, 但这并不影响正确性.

让我们假设 $\alpha_{1} \leq \cdots \leq \alpha_{K}<0 \leq \alpha_{K+1} \leq \cdots \leq \alpha_{n}, 1 \leq K<n .{ }^{1}$ 那么我们又可以把(4)写为

$$
\sum_{k>K} \int_{0}^{k \alpha_{k}}\left(e^{y}+e^{-y}\right) d y \geq \sum_{k \leq K} \int_{0}^{-k \alpha_{k}}\left(e^{y}+e^{-y}\right) d y \geq 0 .
$$

此时所有积分区间都包含于 $\mathbb{R}^{+}$, 且上限不小于下限.

接下来我们关键性地交换求和与积分符号, 将 (5) 等价地变为

$$
\int_{0}^{\infty}\left(e^{y}+e^{-y}\right) \cdot\left(\sum_{k>K} \mathbb{I}_{\left\{y \leq k \alpha_{k}\right\}}-\sum_{k \leq K} \mathbb{I}_{\left\{y \leq-k \alpha_{k}\right\}}\right) d y \geq 0
$$[^0]其中 $\mathbb{I}_{\left\{y \leq k \alpha_{k}\right\}}$ 是 $y \leq k \alpha_{k}$ 的特征函数.

对 $y \geq 0$, 令 $f(y)=e^{y}+e^{-y}, g(y)=\sum_{k>K} \mathbb{I}_{\left\{y \leq k \alpha_{k}\right\}}-\sum_{k \leq K} \mathbb{I}_{\left\{y \leq-k \alpha_{k}\right\}}$. 注意到 $f(y)$ 是正的, 且单调递增, 因此为证 $\int_{y \geq 0} f(y) g(y) d y \geq 0$, 利用分部积分公式只需证明 ${ }^{2}$

$$
\int_{y \geq t} g(y) \geq 0, \forall t \geq 0
$$

根据上面对 $g$ 的定义, 要证的不等式 (7) 可以重写为

$$
\sum_{k>K}\left(k \alpha_{k}-t\right)^{+} \geq \sum_{k \leq K}\left(-k \alpha_{k}-t\right)^{+}
$$

其中 $z^{+}$表示 $\max \{z, 0\}$.

下面我们证明不等式 (8) 对每个 $t \geq 0$ 成立. 我们将不等式左边的和记为 $A$, 右边的记为 $B$. 不妨设 $B>0$, 则一定存在 $l \leq K$ 使得 $-l \alpha_{l}-t \geq \frac{B}{K}$. 由于 $\alpha_{1} \leq \alpha_{2} \leq \cdots \leq \alpha_{l}$, 我们得到 $-\sum_{k=1}^{l} \alpha_{k}-t \geq \frac{B}{K}$. 再考虑到 $\alpha_{l+1}, \ldots, \alpha_{K}<0$, 一定有

$$
\sum_{k>K} \alpha_{k}=-\sum_{k \leq K} \alpha_{k} \geq-\sum_{k \leq l} \alpha_{k} \geq \frac{B}{K}+t .
$$

根据 (9), 以及 $\alpha_{K+1} \leq \alpha_{K+2} \leq \cdots \leq \alpha_{n}$, 不难得到

$$
\begin{aligned}
A \geq \sum_{k>K}\left(k \alpha_{k}-t\right) & =\left(\sum_{k>K} k \alpha_{k}\right)-(n-K) t \\
& \geq\left(\frac{n+K+1}{2} \cdot \sum_{k>K} \alpha_{k}\right)-(n-K) t \\
& \geq\left(\frac{n+K+1}{2} \cdot\left(\frac{B}{K}+t\right)\right)-(n-K) t \\
& =\frac{n+K+1}{2 K} \cdot B+\frac{3 K+1-n}{2} \cdot t .
\end{aligned}
$$

如果 $n \leq 3 K+1$, 那么由 (10) 即可推出 $A \geq B$.

如果 $n>3 K+1$, 此时我们需要将 (10) 更精细化. 事实上对每个 $n \geq M \geq$ $K$ 都有

$$
\begin{aligned}
A & \geq \sum_{k>M}\left(k \alpha_{k}-t\right)=\left(\sum_{k>M} k \alpha_{k}\right)-(n-M) t \\
& \geq\left(\frac{(n+M+1)(n-M)}{2(n-K)} \cdot \sum_{k>K} \alpha_{k}\right)-(n-M) t \\
& \geq\left(\frac{(n+M+1)(n-M)}{2(n-K)} \cdot\left(\frac{B}{K}+t\right)\right)-(n-M) t \\
& =\frac{(n+M+1)(n-M)}{2 K(n-K)} \cdot B+\frac{(M+2 K+1-n)(n-M)}{2(n-K)} \cdot t .
\end{aligned}
$$[^1]取 $M=n-2 K-1>K$, 则由 (11) 得到 $A \geq \frac{2 K+1}{K} B \geq B$.

因此无论如何不等式 (8) 都成立. 证毕.

## 编者注:

牟晓生, 2008 年 IMO 满分金牌获得者, 现于美国哈佛大学攻读博士学位. 从 2016 年 3 月起, 牟晓生将主持建设数学新星问题征解专栏, 并在问题解答区增设 “晓生点评”专栏, 敬请期待.


[^0]:    ${ }^{1}$ 除非 $\alpha_{k}$ 恒等于零, 否则这样的 $K$ 是存在的.

[^1]:    2在不等式领域这又被称为 "majorization trick".

