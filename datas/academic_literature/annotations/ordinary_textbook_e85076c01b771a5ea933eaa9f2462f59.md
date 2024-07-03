# 一个几何问题的复数刻画 

曾卫国

(湖南省雅礼中学，410007)

最近, 法国路易大帝中学曾靖国同学在文 [1] 中研究了一个与四点共圆有关的几何问题, 证明了如下定理:

定理 已知非直角 $\triangle A B C$ 的三边互不相等, $\Gamma_{1}$ 为 $\triangle A B C$ 的外接圆, 圆心为 $O . H$ 为 $\triangle A B C$ 的垂心, $G$ 为 $\Gamma_{1}$ 上异于 $A, B, C$ 的一点, $G$ 不在直线 $A H$ 上,过 $G$ 作 $A G$ 的垂线与直线 $B C$ 交于 $F$. 过 $A, G$ 作一圆 $\Gamma_{2}$, 圆心为 $M . \Gamma_{2}$ 交直线 $A B$ 于 $A, D$ 两点, 交直线 $A C$ 于 $A, E$ 两点. 则 $M, D, E, F$ 四点共圆当且仅当 $M$ 在直线 $B C$ 上或 $H$ 在圆 $\Gamma_{2}$ 上.

本文我们给出上述定理的一个复数刻画版本, 使证明过程较之纯几何法更为简捷.

如图, 设 $\triangle A B C$ 的外心 $O$ 为复平面原点, 并且不妨设圆 $O$ 就是单位圆. 为了简化计算, 对于平面上任意一点 $X$, 直接用 $X$ 记为它所对应的复数. 显然 $H=A+B+C$. 不妨设 $B C=1$, 即 $B=\bar{C}$.

![](https://cdn.mathpix.com/cropped/2024_02_26_e4631df71e9453f07fbag-1.jpg?height=545&width=554&top_left_y=1869&top_left_x=751)

收稿日期: 2016-09-30. 修订日期: 2016-11-09.
设 $\triangle A D E$ 的外心为 $M, A N$ 是圆 $O$ 的直径, 则 $G, N, F$ 共线.

当 $M$ 确定之后, 可以算出 $D, E, F, G$ 的表达式.

(1) $G=\frac{M \bar{A}}{\bar{M}}$.

(2) $D=M+B-A B \bar{M}, E=M+C-A C \bar{M}$.

(3) $F=\frac{\bar{B}+\bar{C}-\bar{G}-\bar{N}}{\overline{B C}-\overline{G N}}=\frac{\bar{B}+\bar{C}+\bar{A}-\bar{G}}{\overline{B C}+\overline{A G}}$

$=\frac{\bar{B}+\bar{C}+\bar{A}-\frac{\bar{M}}{M} A}{1+\frac{\bar{M}}{M}}=\frac{M(\bar{B}+\bar{C}+\bar{A})-\bar{M} A}{M+\bar{M}}$.

(1) 的证明 注意到 $O M$ 是 $A G$ 的中垂线, 所以

$$
\frac{G}{M}=\frac{\bar{A}}{\bar{M}}
$$

故 $G=\frac{M \bar{A}}{\bar{M}}$.

(2) 的证明 注意到 $\angle M A D=\angle M D A$, 所以

$$
\frac{M-D}{A-B}=\frac{\bar{M}-\bar{A}}{\bar{B}-\bar{A}}
$$

从而解得 $D=M+B-A B \bar{M}$.

同理, $E=M+C-A C \bar{M}$.

(3) 的证明 注意到 $F, B, C$ 共线, 所以

$$
\frac{F-B}{C-B}=\frac{\bar{F}-\bar{B}}{\bar{C}-\bar{B}}
$$

整理得 $\overline{B C} F+\bar{F}=\bar{B}+\bar{C}$, 同理, $F, G, N$ 共线, 所以 $\overline{G N} F+\bar{F}=\bar{G}+\bar{N}$. 解得

$$
\begin{aligned}
F & =\frac{\bar{B}+\bar{C}-\bar{G}-\bar{N}}{\overline{B C}-\overline{G N}}=\frac{\bar{B}+\bar{C}+\bar{A}-\bar{G}}{\overline{B C}+\overline{A G}} \\
& =\frac{\bar{B}+\bar{C}+\bar{A}-\frac{\bar{M}}{M} A}{1+\frac{\bar{M}}{M}}=\frac{M(\bar{B}+\bar{C}+\bar{A})-\bar{M} A}{M+\bar{M}} .
\end{aligned}
$$

利用 (1), (2), (3), $M, D, E, F$ 共圆当且仅当 $\frac{E-M}{D-M} \times \frac{D-F}{E-F} \in \mathbb{R}$, 而

$$
\begin{aligned}
& \frac{E-M}{D-M} \times \frac{D-F}{E-F}=\frac{C-A C \bar{M}}{B-A B \bar{M}} \times \frac{D-F}{E-F} \\
= & \frac{C}{B} \frac{(M+\bar{M})(M+B-A B \bar{M})-M(\bar{A}+\bar{B}+\bar{C})+A \bar{M}}{(M+\bar{M})(M+C-A C \bar{M})-M(\bar{A}+\bar{B}+\bar{C})+A \bar{M}}
\end{aligned}
$$

因此 $M, D, E, F$ 共圆当且仅当

$$
\Leftrightarrow \frac{E-M}{D-M} \times \frac{D-F}{E-F}=\frac{\bar{E}-\bar{M}}{\bar{D}-\bar{M}} \times \frac{\bar{D}-\bar{F}}{\bar{E}-\bar{F}}
$$

$$
\begin{aligned}
& \Leftrightarrow \frac{C}{B} \frac{(M+\bar{M})(M+B-A B \bar{M})-M(\bar{A}+\bar{B}+\bar{C})+A \bar{M}}{(M+\bar{M})(M+C-A C \bar{M})-M(\bar{A}+\bar{B}+\bar{C})+A \bar{M}} \\
& =\frac{\bar{C}}{\bar{B}} \frac{(M+\bar{M})(\bar{M}+\bar{B}-A \overline{B M})-\bar{M}(A+B+C)+\bar{A} M}{(M+\bar{M})(\bar{M}+\bar{C}-A \overline{C M})-\bar{M}(A+B+C)+\bar{A} M} .
\end{aligned}
$$

利用 $C=\bar{B}=\frac{1}{B}$ 以及 $\bar{C}=B$, 上式可以整理得

$$
\begin{aligned}
& \Leftrightarrow \bar{B}^{2}[(M+\bar{M})(M+B-A B \bar{M})-M(\bar{A}+\bar{B}+B)+A \bar{M}] \\
& {[(M+\bar{M})(\bar{M}+B-\bar{A} B M)-\bar{M}(A+B+\bar{B})+\bar{A} M]} \\
& -B^{2}[(M+\bar{M})(M+\bar{B}-A \overline{B M})-M(\bar{A}+\bar{B}+B)+A \bar{M}] \\
& {[(M+\bar{M})(\bar{M}+\bar{B}-\overline{A B} M)-\bar{M}(A+B+\bar{B})+\bar{A} M]=0 .}
\end{aligned}
$$

即

$$
(M-A B \bar{M})(M-A \overline{B M})(M+\bar{M}-B-\bar{B})(M+\bar{M}-\bar{A}-A-B-\bar{B})=0
$$

上式是直接分解因式得到.

a) 当 $M-A B \bar{M}=0$ 时, 即 $\frac{M}{A}=\frac{\bar{M}}{\bar{C}}, M$ 在 $A C$ 中垂线上, 此时 $E$ 与 $C$ 重合, 不符合.

b) 当 $M-A \overline{B M}=0$ 时, 即 $\frac{M}{A}=\frac{\bar{M}}{\bar{B}}, M$ 在 $A B$ 中垂线上, 此时 $D$ 与 $B$ 重合, 不符合.

c) 当 $M+\bar{M}-B-\bar{B}=0$, 即 $M$ 在 $B C$ 上, 符合.

d) 当 $M+\bar{M}-\bar{A}-A-B-\bar{B}=0$ 时, 即 $M+\bar{M}-\frac{\bar{A}+\bar{H}+A+H}{2}=0$, 说明 $M$ 在 $A H$ 中垂线上, $M H=M A$, 故 $A, D, H, E$ 共圆.

综上, $M, D, E, F$ 共圆的充要条件是 $M$ 在 $B C$ 上或者 $A, D, H, E$ 共圆.

## 参考文献

[1] 曾靖国,一个几何问题的探究 [J]. 数学新星网 - 学生专栏, 2016-11-07 期.

