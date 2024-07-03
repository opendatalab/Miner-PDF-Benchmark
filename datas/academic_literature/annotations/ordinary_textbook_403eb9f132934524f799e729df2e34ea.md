# 一道 Minklös-Schweitzer 试题的另解 

冷岗松

2000 年匈牙利的 Minklös-Schweitzer 大学生数学竞赛中有一个十分优雅的初等数学问题:

问题: 设 $a_{1}<a_{2}<a_{3}$ 是正整数. 证明: 存在不全为 0 的整数 $x_{1}, x_{2}, x_{3}$ 使得

$$
a_{1} x_{1}+a_{2} x_{2}+a_{3} x_{3}=0,
$$

且 $\max \left\{\left|x_{1}\right|,\left|x_{2}\right|,\left|x_{3}\right|\right\} \leq \frac{2}{\sqrt{3}} \sqrt{a_{3}}$.

我们在文 [1] 中介绍了韦东奕的解法. 韦的解法尽管十分精妙, 但开始的二元点集的构造却有 “旱地拔葱” 之感. 关于这个问题, 同年 (2009 年) 的另一位国家队队员、IMO 金牌得主郑志伟有一个漂亮而自然的解法, 现介绍如下.

## 解 (根据郑志伟的解答整理):

记 $t=\left[\frac{2}{\sqrt{3}} \sqrt{a_{3}}\right]$. 考虑 $(t+1)^{2}$ 个数: $a_{1} u_{1}+a_{2} u_{2}$, 其中整数 $u_{1}, u_{2}$ 满足 $0 \leq u_{1}, u_{2} \leq t$.

记这些数构成的可重集为 $S$, 则

$$
|S|=(t+1)^{2}>\left(\frac{2}{\sqrt{3}} \sqrt{a_{3}}\right)^{2}=\frac{4}{3} a_{3},
$$

且 $S$ 中任意一个数均属于区间 $\left[0, t\left(a_{1}+a_{2}\right)\right]$. 由此立得 $S$ 中的任意 3 个数中必有两数之差 $\leq \frac{t\left(a_{1}+a_{2}\right)}{2}<a_{3} t$.

下分两种情况讨论.

(1) 如果 $S$ 中存在 3 个数模 $a_{3}$ 同余.

此时, 这 3 个数中必存在两个模 $a_{3}$ 同余, 且它们的差 $<a_{3} t$. 不妨设这两个数为 $a_{1} u_{1}+a_{2} u_{2}, a_{1} v_{1}+a_{2} v_{2}$, 则

$$
\left|\left(a_{1} u_{1}+a_{2} u_{2}\right)-\left(a_{1} v_{1}+a_{2} v_{2}\right)\right|=s a_{3},
$$

其中整数 $s$ 满足 $0 \leq s<t$.

从而我们有

$$
a_{1}\left(u_{1}-v_{1}\right)+a_{2}\left(u_{2}-v_{2}\right)+s a_{3}=0,
$$

或

$$
a_{1}\left(u_{1}-v_{1}\right)+a_{2}\left(u_{2}-v_{2}\right)-s a_{3}=0 .
$$

注意到 $\left|u_{1}-v_{1}\right|,\left|u_{2}-v_{2}\right|,|s|$ 均不超过 $t \leq \frac{2}{\sqrt{3}} \sqrt{a_{3}}$, 这时结论成立.

(2) 如果 $S$ 中任意 3 个数不模 $a_{3}$ 同余.

此时注意到 $|S|>\frac{4}{3} a_{3}$, 由抽屉原理知 $S$ 中有大于 $\frac{a_{3}}{3}$ 对数模 $a_{3}$ 同余, 且不妨设任一对这样的数之差 $\geq t a_{3}$ (否则就回到情形 (1)).

设 $a_{1} u_{1}+a_{2} u_{2}, a_{1} v_{1}+a_{2} v_{2} \in S$ 且

$$
\left(a_{1} u_{1}+a_{2} u_{2}\right)-\left(a_{1} v_{1}+a_{2} v_{2}\right)=s a_{3},
$$

其中整数 $s$ 满足 $s>t$.

上式可重写为

$$
\left(u_{1}-v_{1}\right) a_{1}+\left(u_{2}-v_{2}\right) a_{2}=s a_{3} .
$$

这时由 (1) 知

$$
\left(u_{1}-v_{1}\right) a_{1}+t a_{3}>\left(u_{1}-v_{1}\right) a_{1}+\left(u_{2}-v_{2}\right) a_{2}=s a_{3}>t a_{3},
$$

因此

$$
u_{1}-v_{1}>0
$$

同理

$$
u_{2}-v_{2}>0
$$

又

$$
s a_{3}=\left(u_{1}-v_{1}\right) a_{1}+\left(u_{2}-v_{2}\right) a_{3}<t\left(a_{1}+a_{2}\right)<2 t a_{3},
$$

所以

$$
s<2 t \text {. }
$$

再设

$$
a_{1} u_{1}^{\prime}+a_{2} u_{2}^{\prime}, a_{1} v_{1}^{\prime}+a_{2} v_{2}^{\prime} \in S
$$

且

$$
\left(u_{1}^{\prime}-v_{1}^{\prime}\right) a_{1}+\left(u_{2}^{\prime}-v_{2}^{\prime}\right) a_{2}=s^{\prime} a_{3},
$$

其中 $u_{1}^{\prime}-v_{1}^{\prime}>0, u_{2}^{\prime}-v_{2}^{\prime}>0, s^{\prime}>t$, 且诸变元都表示是整数.

(i) 当 $\left(u_{1}-v_{1}, u_{2}-v_{2}\right) \neq\left(u_{1}^{\prime}-v_{1}^{\prime}, u_{2}^{\prime}-v_{2}^{\prime}\right)$ 时,
将 (1), (2) 相减可得

$$
\left(\left(u_{1}-v_{1}\right)-\left(u_{1}^{\prime}-v_{1}^{\prime}\right)\right) a_{1}+\left(\left(u_{2}-v_{2}\right)-\left(u_{2}^{\prime}-v_{2}^{\prime}\right)\right) a_{2}=\left(s-s^{\prime}\right) a_{3} .
$$

注意到 $0<u_{1}-v_{1}, u_{2}-v_{2}, u_{1}^{\prime}-v_{1}^{\prime}, u_{2}^{\prime}-v_{2}^{\prime} \leq t$, 且 $t<s, s^{\prime}<2 t$, 便易知 (3) 中 $a_{1}, a_{2}, a_{3}$ 的系数的绝对值 $\leq t$ 且不全为 0 , 故题中结论成立.

(ii) 当总有 $u_{1}-v_{1}=u_{1}^{\prime}-v_{1}^{\prime}$ 且 $u_{2}-v_{2}=u_{2}^{\prime}-v_{2}^{\prime}$ 时.

设 $u_{1}-v_{1}=a, u_{2}-v_{2}=b$, 其中 $a, b$ 是两个固定的非负整数.

由 (1) 知

$$
s a_{3}=a_{1} a+a_{2} b<a_{3}(a+b),
$$

即

$$
a+b>s>t \text {. }
$$

所以

$$
a+b \geq t+2 \text {. }
$$

又因为满足 $\left(a_{1} u_{1}+a_{2} u_{2}\right)-\left(a_{1} v_{1}+a_{2} v_{2}\right)=s a_{3}, s>t$ 的四元数组 $\left(u_{1}, u_{2}, v_{1}, v_{2}\right)$有 $>\frac{a_{3}}{3}$ 组. 而对这样的数组, 注意到

$$
0 \leq v_{1}=u_{1}-a \leq t-a, \quad 0 \leq v_{2}=u_{2}-b \leq t-b
$$

故满足要求的四元数组个数

$$
\begin{aligned}
T & \leq(t-a+1)(t-b+1) \\
& \leq \frac{(2 t-(a+b)+2)^{2}}{4} \\
& \leq \frac{t^{2}}{4} \leq \frac{1}{4}\left(\frac{2}{\sqrt{3}} \sqrt{a_{3}}\right)^{2}=\frac{1}{3} a_{3} .
\end{aligned}
$$

矛盾! 这说明 (ii) 不可能出现.

综上, 便知本题的结论成立.

## 参考文献

[1] 冷岗松, 韦东奕的妙解, 数学新星网 (冷岗松专栏), 网址: www.nsmath.cn.

