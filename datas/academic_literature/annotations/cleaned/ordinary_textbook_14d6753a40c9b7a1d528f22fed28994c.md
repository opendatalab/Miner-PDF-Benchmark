# 第 60 届 IMO 第六题的一个推广 

林扬渊 $^{1}$ 刘哲源 ${ }^{2}$

(1. 山西大学初民学院, 030006; 2. 浙江省镇海中学, 315200)

本文给出今年第 60 届 IMO 第六题的一个推广.

问题 在锐角三角形 $\triangle A B C$ 中, $I$ 是内心, $\triangle A B C$ 的内切圆 $\omega$ 与边 $B C$ 和 $C A, A B$ 分别相切于点 $D, E$ 和 $F$. 过点 $D$ 且垂直于 $E F$ 的直线与 $\omega$ 的另一点交点为 $R$. 直线 $A R$ 与 $\omega$ 的另一交点为 $P . \triangle P C E$ 和 $\triangle P B F$ 的外接圆交于另一点 $Q$. 证明: 直线 $D I$ 和 $P Q$ 的交点在过点 $A$ 且垂直于 $A I$ 的直线上.


我们的推广可表述为:

推广如下图, 已知 $E, F$ 分别为 $A C, A B$ 上的两定点, 给出平面上任一定点 $I$, 设 $\{I, D\} \equiv \odot(I F B) \cap \odot(I E C), Q$ 为 $\odot(D E F)$ 上一动点, $\{P, Q\} \equiv$ $\odot(Q F B) \cap \odot(Q E C), S \equiv P Q \cap I D$, 则

$(1) \odot(S D Q)$ 过一定点 $M i$;

(2) 设 $\{T, M i\} \equiv A M i \cap \odot(S D Q), S T / / E F$.

修订日期: 2019-09-26.



从如下角度考虑, 原问题与推广的关系几乎是显见的: 考虑原题, 设 $D^{\prime}$ 为 $D$关于 $\omega$ 的对径点, 则 $D^{\prime} R / / E F$, 结论即证 $A L / / E F$.

结合 Reim 定理我们只需证明 $A, L, D, P$ 共圆, 而考虑推广结论, $A S / / E F \Leftrightarrow$ $A, S, Q, D$ 共圆仅为特例 (即 $A \equiv T$ 时), 显然可保证原结论.

在证明推广前, 我们先给出如下构型的一些性质及其证明:

性质给定 $\triangle A B C, E \in A C, F \in A B$, 点 $P, Q$ 满足 $\{P, Q\} \equiv \odot(Q F B) \cap$ $\odot(Q E C)$, 点 $E^{\prime}, F^{\prime}$ 满足 $\left\{E, E^{\prime}\right\} \equiv A C \cap \odot(E F Q),\left\{F, F^{\prime}\right\} \equiv A B \cap \odot(E F Q), M i$为完全四边形 $<A B, B E^{\prime}, C F^{\prime}, A C>$ 的 Miquel 点.


证明 设 $\{T, F\} \equiv E F \cap \odot(B P Q),\{S, E\} \equiv E F \cap \odot(C P Q),\left\{B^{\prime}, P\right\} \equiv S P \cap$ $\odot(B P C),\left\{C^{\prime}, P\right\} \equiv T P \cap \odot(B P C), L \equiv B B^{\prime} \cap C C^{\prime}, K \equiv E F \cap C L,\{M i, N\} \equiv$
$M i Q \cap \odot(A B C)$.

(i) $A L / / E F$. 注意到

$$
\measuredangle F K L=\measuredangle E T C^{\prime}+\measuredangle T C^{\prime} L=\measuredangle F B P+\measuredangle P B C=\measuredangle A B C,
$$

得 $B, C, K, F$ 共圆, 故

$$
\measuredangle A F E=\measuredangle B C L,
$$

同理

$$
\measuredangle L B C=\measuredangle F E A,
$$

所以

$$
\angle L B C \sim \angle A E F \sim \triangle A F^{\prime} E^{\prime} \sim \triangle L C^{\prime} B^{\prime}
$$

同时 $A, B, C, L$ 共圆, 对 $\odot(B C L A)$ 与 $\odot(B C K F)$ 应用 Reim 定理即得 $A L / / E F$.

(ii) $P Q / / L N$. 注意到

$$
\measuredangle C^{\prime} B^{\prime} M=\measuredangle\left(C^{\prime} T, P M\right)=\measuredangle(E T, F Q),
$$

同理 $\measuredangle M C^{\prime} B^{\prime}=\measuredangle Q E F$, 可得 $\triangle Q E F \sim \triangle M C^{\prime} B^{\prime}$. 于是结合 $(\psi)$ 可得

$$
A E F E^{\prime} F^{\prime} Q \sim L C^{\prime} B^{\prime} C B M
$$

而由 Miquel 点的性质知 $M i$ 为 $B F^{\prime}, C E^{\prime}$ 的旋转位似中心, 故 $M i$ 也为 $(*)$ 的旋转位似中心.

于是

$$
\measuredangle L N M i=\measuredangle L A M i \measuredangle(M Q, Q M i),
$$

故

$$
P Q / / L N \text {. }
$$

回到上述推广. 类似上述构型的定义得到 $M i, L$, 设 $\{M i, N\} \equiv M i Q \cap$ $\odot(A B C),\{M i, K\} \equiv M i D \cap \odot(A B C)$, 由 (i),(ii) 得

$$
P Q / / L N, I D / / L K
$$

所以

$$
\measuredangle N L K=\measuredangle Q S D=\measuredangle N M i K,
$$

故定点 $M i \in \odot(S D Q)$.

若设 $\{M i, X\} \equiv \odot(S D Q) \cap \odot(A B C),\left\{X, L^{\prime}\right\} \equiv X S \cap \odot(A B C)$, 对 $\odot(M i Q S X)$与 $\odot(M i N L K)$ 应用 Reim 定理得 $S Q / / L^{\prime} N$. 故 $L \equiv L^{\prime}$, 即 $L, S, X$ 共线, 于是
对 $\odot(M i X L A)$ 与 $\odot(M i X S T)$ 应用 Reim 定理即得 $S T / / A L / / E F$.



评注 我们避开原问题中对 $Q$ 点的生硬处理, 从运动的角度考虑更一般性的构型, 利用 Miquel 点引申出的两个平行结论对 $P Q$ 的方向重新刻画, 剩下的就是一些细节处理. 原问题解法甚多, 引入 Miquel 点的想法在 Aops 上亦有提及,但进一步的推广及后面纯粹的导角证明却别具一格.

