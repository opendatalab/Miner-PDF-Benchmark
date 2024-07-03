# 莱斯特定理的复数证法 

## 李泽宇

(北京师范大学第二附属中学, 100088)

1997 年 Lester 在文 [1] 中证明了平面几何中非常优美的结果:

定理 (Lester) $\triangle A B C$ 的外心 $O$, 九点圆心 $N$, 和第一, 第二费马点 $F_{1}, F_{2}$四点共圆.

近几年, 莱斯特定理及对应的莱斯特圆的研究, 得到越来越广泛的关注, 如文献 [2-4] 中得到了很多有用的推广和证明. 而对莱斯特定理本身的证明, 也有文献给出了许多简便的办法, 如解析法, 纯几何法, 投影法, 复数法等, 具体可参见 [5-8]. 在本文中, 我们用复数的方法证明这一定理.

证明 以圆心 $O$ 为原点建立复平面, 记 $A=a, B=b, C=c$, 满足 $|a|=|b|=$ $|c|$. 由九点圆即为 $\triangle A B C$ 三边中点之外接圆, 易知 $N=\frac{(a+b+c)}{2}$.

设 $\triangle A B C$ 向外的三个等边三角形依次为 $\triangle A B C_{1}, \triangle B C A_{1}, \triangle C A B_{1}$, 它们的中心依次为 $O_{3}, O_{1}, O_{2}$, 则由定义知 $F_{1}=A A_{1} \cap B B_{1} \cap C C_{1}$; 设 $\triangle A B C$向内的三个等边三角形依次为 $\triangle A B C_{2}, \triangle B C A_{2}, \triangle C A B_{2}$, 它们的中心依次为 $O_{3}^{\prime}, O_{1}^{\prime}, O_{2}^{\prime}$, 则由定义知 $F_{2}=A A_{2} \cap B B_{2} \cap C C_{2}$. 从而

$$
C_{1}=A+(A-B) w=-b w-a w^{2}, \quad C_{2}=B+(B-A) w=-a w-b w^{2}
$$

其中 $w$ 为三次单位虚根, $w^{3}-1=(w-1)\left(w^{2}+w+1\right)=0$.

同理知

$$
\begin{array}{ll}
A_{1}=-c w-b w^{2}, & B_{1}=-a w-c w^{2} ; \\
A_{2}=-b w-c w^{2}, & B_{2}=-c w-a w^{2} .
\end{array}
$$

故

$$
O_{1}=\frac{b+c+A_{1}}{3}=\frac{(1-w)\left(c-b w^{2}\right)}{3}, O_{1}^{\prime}=\frac{b+c+A_{2}}{3}=\frac{(1-w)\left(b-c w^{2}\right)}{3},
$$

收稿日期: 2016-06-11； 修订日期:2016-09-18。

$$
\begin{aligned}
& O_{2}=\frac{c+a+B_{1}}{3}=\frac{(1-w)\left(a-c w^{2}\right)}{3}, O_{2}^{\prime}=\frac{c+a+B_{2}}{3}=\frac{(1-w)\left(c-a w^{2}\right)}{3}, \\
& O_{3}=\frac{a+b+C_{1}}{3}=\frac{(1-w)\left(b-a w^{2}\right)}{3}, O_{3}^{\prime}=\frac{a+b+C_{2}}{3}=\frac{(1-w)\left(a-b w^{2}\right)}{3} .
\end{aligned}
$$

【注】由 $(1-w)\left(1-w^{2}\right)=3$ 可知下式成立:

$$
O_{1}+O_{2}+O_{3}=O_{1}^{\prime}+O_{2}^{\prime}+O_{3}^{\prime}=a+b+c=A_{1}+B_{1}+C_{1}=A_{2}+B_{2}+C_{2}
$$

进而五个对应三角形的重心重合.

由 $F_{1}$ 为 $\odot\left(A B C_{1}\right)$ 与 $\odot\left(A C B_{1}\right)$ 交点可知 $F_{1}$ 是 $A$ 关于 $O_{2} O_{3}$ 的对称点, 从而

$$
\frac{F_{1}-O_{2}}{O_{2}-O_{3}}=\frac{\overline{A-O_{2}}}{\overline{O_{2}-O_{3}}}
$$

又

$$
O_{2}-O_{3}=\frac{(1-w)\left(a w+b+c w^{2}\right)}{3}
$$

因此

$$
\begin{aligned}
\frac{F_{1}-\frac{(1-w)\left(a-c w^{2}\right)}{3}}{(1-w)\left(a w+b+c w^{2}\right)} & =\frac{\overline{a-\frac{(1-w)\left(a-c w^{2}\right)}{3}}}{\overline{(1-w)\left(a w+b+c w^{2}\right)}} \\
& =\frac{3 \bar{a}-\left(1-w^{2}\right)(\bar{a}-\bar{c} w)}{3\left(1-w^{2}\right)\left(\bar{a} w^{2}+\bar{b}+\bar{c} w\right)}
\end{aligned}
$$

于是,

$$
\begin{aligned}
F_{1}= & \frac{\left[3 \bar{a}-\left(1-w^{2}\right)(\bar{a}-\bar{c} w)\right]\left(a w+b+c w^{2}\right)}{3(1+w)\left(\bar{a} w^{2}+\bar{b}+\bar{c} w\right)} \\
& +\frac{(1-w)\left(a-c w^{2}\right)(1+w)\left(\bar{a} w^{2}+\bar{b}+\bar{c} w\right)}{3(1+w)\left(\bar{a} w^{2}+\bar{b}+\bar{c} w\right)} \\
= & \frac{S}{3(1+w)\left(\bar{a} w^{2}+\bar{b}+\bar{c} w\right)},
\end{aligned}
$$

其中

$$
\begin{aligned}
S= & 3 \bar{a}\left(a w+b+c w^{2}\right)-\left(1-w^{2}\right)(\bar{a}-\bar{c} w)\left(a w+b+c w^{2}\right) \\
& +\left(1-w^{2}\right)\left(a-c w^{2}\right)\left(\bar{a} w^{2}+\bar{b}+\bar{c} w\right) \\
= & 3\left(\bar{a} a w+\bar{a} b+\bar{a} c w^{2}\right)+\left(1-w^{2}\right)\left[\left(a \bar{a} w^{2}+a \bar{b}+a \bar{c} w-c \bar{a} w-c \bar{b} w^{2}-c \bar{c}\right)\right. \\
& \left.-\left(a \bar{a} w+\bar{a} b+c \bar{a} w^{2}-a \bar{c} w^{2}-b \bar{c} w-c \bar{c}\right)\right] \\
= & 3 \bar{a} a w+3 \bar{a} b+3 \bar{a} c w^{2}+a \bar{a} w^{2}+a \bar{b}+a \bar{c} w \\
& -c \bar{a} w-c \bar{b} w^{2}-a \bar{a} w-\bar{a} b-c \bar{a} w^{2}+a \bar{c} w^{2} \\
& +b \bar{c} w-a \bar{a} w-a \bar{b} w^{2}-a \bar{c}+c \bar{a}+c \bar{b} w+a \bar{a}+\bar{a} b w^{2}+c \bar{a} w-a \bar{c} w-b \bar{c}
\end{aligned}
$$

$$
\begin{aligned}
= & a \bar{b}\left(1-w^{2}\right)+a \bar{c}\left(w^{2}-1\right)+c \bar{a}\left(1+2 w^{2}\right) \\
& +c \bar{b}\left(w-w^{2}\right)+\bar{a} b\left(w^{2}+2\right)+b \bar{c}(w-1) \\
= & \left(1-w^{2}\right) a(\bar{b}-\bar{c})+\left(w^{2}-w\right) c(\bar{a}-\bar{b})+(w-1) b(\bar{c}-\bar{a})
\end{aligned}
$$

从而

$$
F_{1}=\frac{(w-1)\left[w^{2} a(\bar{b}-\bar{c})+b(\bar{c}-\bar{a})+w c(\bar{a}-\bar{b})\right]}{3(1+w)\left(w^{2} \bar{a}+\bar{b}+w \bar{c}\right)} .
$$

令 $b \rightarrow c, c \rightarrow b$, 则

$$
F_{2}=\frac{(w-1)\left[w^{2} a(\bar{c}-\bar{b})+w b(\bar{a}-\bar{c})+c(\bar{b}-\bar{a})\right]}{3(1+w)\left(w^{2} \bar{a}+w \bar{b}+\bar{c}\right)} .
$$

欲证 $F_{1}, F_{2}, O, N$ 四点共圆, 只需证交比 $\left(F_{1}, F_{2} ; O, N\right)=\frac{F_{1}}{F_{2}} \cdot \frac{F_{2}-N}{F_{1}-N}$ 为实数.

注意到

$$
\frac{F_{1}}{F_{2}}=\frac{w^{2} a(\bar{b}-\bar{c})+b(\bar{c}-\bar{a})+w c(\bar{a}-\bar{b})}{w^{2} a(\bar{c}-\bar{b})+w b(\bar{a}-\bar{c})+c(\bar{b}-\bar{c})+c(\bar{b}-\bar{a})} \cdot \frac{w^{2} \bar{a}+w \bar{b}+\bar{c}}{w^{2} a(\bar{c}-\bar{b})+\bar{b}+w \bar{c}},
$$

且由 $(1-w)\left(1-w^{2}\right)=3,\left(1-w^{2}\right)(1+w)=(1-w) w$, 可得

$$
\begin{aligned}
& \frac{F_{2}-N}{F_{1}-N} \cdot \frac{w^{2} \bar{a}+w \bar{b}+\bar{c}}{w^{2} \bar{a}+\bar{b}+w \bar{c}} \\
& =\frac{2(w-1)\left[w^{2} a(\bar{c}-\bar{b})+w b(\bar{a}-\bar{c})+c(\bar{b}-\bar{a})\right]+}{2(w-1)\left[w^{2} a(\bar{b}-\bar{c})+b(\bar{c}-\bar{a})+w c(\bar{a}-\bar{b})\right]+} \\
& \frac{-3(a+b+c)(1+w)\left(w^{2} \bar{a}+w \bar{b}+\bar{c}\right)}{-3(a+b+c)(1+w)\left(w^{2} \bar{a}+\bar{b}+w \bar{c}\right)} \\
& =\frac{2\left[w^{2} a(\bar{c}-\bar{b})+w b(\bar{a}-\bar{c})+c(\bar{b}-\bar{a})\right]+}{2\left[w^{2} a(\bar{b}-\bar{c})+b(\bar{c}-\bar{a})+w c(\bar{a}-\bar{b})\right]+} \\
& \frac{+(1-w)(a+b+c)\left(\bar{a}+w^{2} \bar{b}+w \bar{c}\right)}{+(1-w)(a+b+c)\left(\bar{a}+w \bar{b}+w^{2} \bar{c}\right)} \\
& =\frac{\bar{a}(2 w b-2 c)+\bar{b}\left(2 c-2 w^{2} a\right)+\bar{c}\left(2 w^{2} a-2 w b\right)+}{\bar{a}(2 w c-2 b)+\bar{b}\left(2 w^{2} a-2 w c\right)+\bar{c}\left(2 b-2 w^{2} a\right)+} \\
& \frac{+(1-w)\left[a \bar{a}+w^{2} b \bar{b}+w c \bar{c}+\bar{a}(b+c)+w^{2} \bar{b}(c+a)+w \bar{c}(a+b)\right]}{+(1-w)\left[a \bar{a}+w b \bar{b}+w^{2} c \bar{c}+\bar{a}(b+c)+w \bar{b}(c+a)+w^{2} \bar{c}(a+b)\right]} \\
& =\frac{\bar{a}(2 w b-2 c+b+c-w b-w c)+\bar{b}\left(2 c-2 w^{2} a+w^{2} c+w^{2} a-c-a\right)+}{\bar{a}(2 w c-2 b+b+c-w b-w c)+\bar{b}\left(2 w^{2} a-2 w c+w c+w a-w^{2} c-w^{2} a\right)+} \\
& \frac{+\bar{c}\left(2 w^{2} a-2 w b+w a+w b-w^{2} a-w^{2} b\right)}{+\bar{c}\left(2 b-2 w^{2} a+w^{2} a+w^{2} b-a-b\right)} \\
& =\frac{(w+1) \bar{a}(b-c)+\left(w^{2}+1\right) \bar{b}(c-a)+\left(w^{2}+w\right) \bar{c}(a-b)}{(w+1) \bar{a}(c-b)+\left(w^{2}+w\right) \bar{b}(a-c)+\left(w^{2}+1\right) \bar{c}(b-a)} \\
& =\frac{w^{2} \bar{a}(b-c)+w \bar{b}(c-a)+\bar{c}(a-b)}{w^{2} \bar{a}(c-b)+\bar{b}(a-c)+w \bar{c}(b-a)} .
\end{aligned}
$$

故而

$$
\begin{aligned}
\left(F_{1}, F_{2} ; O, N\right)= & \frac{w^{2} a(\bar{b}-\bar{c})+b(\bar{c}-\bar{a})+w c(\bar{a}-\bar{b})}{w^{2} a(\bar{c}-\bar{b})+w b(\bar{a}-\bar{c})+c(\bar{b}-\bar{a})} \\
& \cdot \frac{w^{2} \bar{a}(b-c)+w \bar{b}(c-a)+\bar{c}(a-b)}{w^{2} \bar{a}(c-b)+\bar{b}(a-c)+w \bar{c}(b-a)} \\
= & \left|\frac{w^{2} a(\bar{b}-\bar{c})+b(\bar{c}-\bar{a})+w c(\bar{a}-\bar{b})}{w^{2} a(\bar{c}-\bar{b})+w b(\bar{a}-\bar{c})+c(\bar{b}-\bar{a})}\right|^{2} \in \mathbb{R} .
\end{aligned}
$$

从而结论得证.

## 参考文献

[1] J. Lester, Triangles III: Complex triangle functions [J]. Aequationes Math., 53 (1997), 4-35.

[2] M. Trott, Applying GroebnerBasis to Three Problems in Geometry [J]. Math. Edu. Res., 6 (1997), 15-28.

[3] P. Yiu, The circles of Lester, Evans, Parry, and their generalizations [J]. Forum Geom., 10 (2010), 175-209.

[4] D. Oai, A Simple Proof of Gilbert's Generalization of the Lester Circle Theorem [J]. Forum Geom., 14 (2014), 201-202.

[5] R. Shail, A proof of Lester's Theorem [J]. Math. Gaz., 85 (2001), 225-232.

[6] J. Rigby, A simple proof of Lester's theorem [J]. Math. Gaz., 87 (2003), 444-452.

[7] M. Duff, A short projective proof of Lester's theorem [J].Math. Gaz., 89 (2005), 505-506.

[8] 张金金圭, 卢圣, 三角形莱斯特定理的证明 $[\mathrm{J}]$. 数学新星网 - 学生专栏, 2016-04-12 期.

