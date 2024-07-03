# MATHEMATICS COMPETITIONS 



JOURNAL OF THE

WORLD FEDERATION OF NATIONAL

MATHEMATICS COMPETITIONS

# The Art of Proposing Problems in Mathematics Competitions II 

Bin Xiong and Gangsong Leng



matics Competitions.

Bin Xiong is a professor of mathematics education in the school of mathematics sciences at East China Normal University. His research interest is in problem solving and gifted education, with an emphasis on methodology of mathematics, theory of mathematics problem solving, mathematics education, and the identification and nurturing of talented students. He has published more than 100 papers and published or edited more than 150 books, both within China and abroad. He served as the leader of the Chinese National Team for the International Mathematical Olympiad for 10 times. He is also involved in the National Junior High School Competition, the National High School Mathematics Competition, the Western China Mathematical Olympiad and the Girls Mathematical Olympiad. In 2018, Prof. Xiong was awarded the Paul Erdős Award by the World Federation of National Mathe-



Gangsong Leng is a professor in Department of Mathematics, Founder and Leader of the Convex Geometry group at Shanghai University. His major research interests are convex geometry and integral geometry. In his more than thirty years career, more than 100 academic papers have been published in J. Differential Geom., Adv. Math., Trans. Amer. Math. Soc., Math. Z. and other academic journals. In addition, he has published more than 50 papers on mathematics competition and mathematics education as well. He has been the coach of the National Training Team, and as well a member of the Main Examination Committee of China Mathematics Olympics (CMO). Since 2013, he has been the Chair of Main Examination Committee of the China Western Mathematical Olympiad. He served as the Leader of the China National Team for the International Mathematical Olympiad (IMO) in 2007, and also served as the Deputy Leader in 2006 and 2009. His research won ICCM Best Paper Award (2017), and his achievements on Mathematical Education won him the Paul Erdős Award of the World Federation of National Mathematics Competitions in 2020.

## Introduction

This is the second part of "The Art of Proposing Problems in Mathematics Competitions". In the first part, we give some examples including: a problem originated from Tao's result, the expansion property of pedal triangles, the cardinal number of maximal independent set, finding isosceles trapezoids and Problems on convex sequences.

In this part, we give some more examples.

## The intersections of three nonempty sets

The following problem is from Romania TST in 2004 (see [1]).

Problem 0.1.1. Suppose $n>1$ is a positive integer, and $X$ is an n-term set. $A_{1}, A_{2}, \cdots, A_{101}$ are the subsets of $X$ such that the cardinal number of the union of any 50 sets among them is more than $\frac{50}{51} n$. Prove that there exist 3 sets in these 101 subsets such that any two of them have nonempty intersection.

Proof. We consider the graph $G$ with vertices $A_{1}, A_{2}, \cdots, A_{101}$. If the intersection of any two sets is nonempty, then we draw an edge between them. This problem requires us to prove the existence of a triangle in this graph $G$.

If there does not exist a triangle in the graph $G$, then there are at least 51 vertices in this graph with degree at most 50. In fact, if the number of vertices with degree at most 50 is at most 50, there exist 51 vertices and the degree for each vertex is at least 51. Therefore, there must be two vertices with edge connecting them, say $A$ and $B$. Note that, there exist edges connecting $A$ and 50 vertices among the remaining 99 vertices, and so is $B$. Therefore, there exists a vertex $C$ with connections to $A$ and $B$. Thus, we get a triangle $A B C$. A contradiction!

Now we assume that $A_{1}, A_{2}, \cdots, A_{51}$ are points whose degrees are at most 50. Then each $A_{i}(i \leq$ 51) has intersections with at most 50 subsets and has no intersections with the remaining 50 subsets. This means that there exist 50 subsets such that $A_{i}$ is contained in the complement of the union of these 50 sets. Since the cardinal number of the union of any 50 subsets is more than $\frac{50}{51} n$, then the cardinal number of $A_{i}$ is less than $\frac{1}{51} n$. Hence,

$$
\left|A_{1} \cup A_{2} \cup \cdots \cup A_{50}\right|<\left|A_{1}\right|+\left|A_{2}\right|+\cdots+\left|A_{50}\right|<\frac{50}{51} n
$$

a contradiction. This means that there must exist 3 sets whose intersection is nonempty in these 101 sets.

The above approach is very interesting, and it only uses the fact that each $A_{i}$ is contained in the complement of the union of some 50 subsets. However, if we reconsider this question by counting method, we can find a stronger conclusion.

Problem 0.1.2. Let $n>1$ be a positive integer and let $X$ be a set with $n$ elements. Suppose $A_{1}, A_{2}, \cdots, A_{101}$ are subsets of $X$ and any union of 50 subsets is more than $\frac{50}{51} n$. Prove that there exist 3 subsets whose intersection is nonempty in these 101 subsets.

Proof. We prove it by contradiction. If any 3 subsets of $A_{1}, A_{2}, \cdots, A_{101}$ is nonempty, then

$$
\sum_{1 \leq i<j<k \leq 101}\left|A_{i} \cap A_{j} \cap A_{k}\right|=0
$$

By the inclusion-exclusion principle,

$$
n \geq\left|\bigcup_{i=1}^{101} A_{i}\right|=\sum_{i=1}^{101}\left|A_{i}\right|-\sum_{1 \leq i<j \leq 101}\left|A_{i} \cap A_{j}\right|
$$

Without loss of generality, assume that $\left|A_{101}\right|$ is the maximal. Observing

$$
\begin{aligned}
& \sum_{i=1}^{50}\left|A_{i}\right| \geq\left|\bigcup_{i=1}^{50} A_{i}\right|>\frac{50}{51} n \\
& \sum_{i=51}^{100}\left|A_{i}\right| \geq\left|\bigcup_{i=51}^{100} A_{i}\right|>\frac{50}{51} n
\end{aligned}
$$

one can obtain

$$
\sum_{i=1}^{101}\left|A_{i}\right| \geq \frac{101}{100} \sum_{i=1}^{100}\left|A_{i}\right|>\frac{101}{100} \times \frac{100}{51} n=\frac{101}{51} n
$$

It follows from (0.1.1) and (0.1.2) that

$$
\sum_{1 \leq i<j \leq 101}\left|A_{i} \cap A_{j}\right| \geq \sum_{i=1}^{101}\left|A_{i}\right|-n>\left(\frac{101}{51}-1\right) n=\frac{50}{51} n
$$

On the other hand, for any $\left\{k_{1}, k_{2}, \cdots, k_{50}\right\} \subset\{1,2, \cdots, 101\}$, by inclusion-exclusion principle,

$$
\frac{50}{51} n<\left|\bigcup_{i=1}^{50} A_{k_{i}}\right|=\sum_{i=1}^{50}\left|A_{k_{i}}\right|-\sum_{1 \leq i<j \leq 50}\left|A_{k_{i}} \cap A_{k_{j}}\right|
$$

For any subset in $\{1,2, \cdots, 101\}$ with 50 elements, there exist a similar inequality and the total number of this kind of inequalities is $\left(\begin{array}{c}101 \\ 50\end{array}\right)$. Summing over all these inequalities, we obtain

$$
\frac{50}{51} n \cdot\left(\begin{array}{c}
101 \\
50
\end{array}\right)<\left(\begin{array}{c}
100 \\
49
\end{array}\right) \cdot \sum_{i=1}^{101}\left|A_{i}\right|-\left(\begin{array}{c}
99 \\
48
\end{array}\right) \sum_{1 \leq i<j \leq 100}\left|A_{i} \cap A_{j}\right|
$$

Since any element in $X$ belongs to at most two sets in $A_{1}, A_{2}, \cdots, A_{101}$, one has

$$
\sum_{i=1}^{101}\left|A_{i}\right| \leq 2 n
$$

By (0.1.4) and (0.1.5), one has

$$
\begin{aligned}
\sum_{1 \leq i<j \leq 100}\left|A_{i} \cap A_{j}\right| & <\frac{\left(\begin{array}{c}
100 \\
49
\end{array}\right)}{\left(\begin{array}{c}
99 \\
48
\end{array}\right)} \cdot 2 n-\frac{\left(\begin{array}{c}
101 \\
50
\end{array}\right)}{\left(\begin{array}{c}
99 \\
48
\end{array}\right)} \cdot \frac{50}{51} n \\
& =\left(\frac{200}{49}-\frac{100 \times 101}{49 \times 51}\right) n \\
& =\quad \frac{100}{49} \cdot \frac{1}{51} n .
\end{aligned}
$$

It follows from (0.1.3) and (0.1.6) that

$$
\frac{100}{49} \cdot \frac{1}{51} n>\frac{50}{51} n
$$

i.e., $100>49 \times 50$, which is a contradiction.

The above method is based on the inclusion-exclusion principle. For any subset in $\{1,2, \cdots, 101\}$, using the inclusion and exclusion principle and then adding the inequalities together is actually taking the "mean value". It is a common method.

The previous problem is a new conclusion based on a new method but still closely related to the original question. In order to design a new problem based on it, it is necessary to make more changes. We first concentrate on the assumption because $\frac{50}{51} n$ may not be optimal. After several attempts, we found that for general $n$ it seems impossible to determine the sharp bound. In retrospect, could we find the maximum for some special smaller $n$ ? This can assess students' ability on combinational construction. After pondering, we proposed the following problem.

Problem 0.1.3. Let $|X|=16$. For any 8 subsets of $X$, if the cardinal number of the union of any 4 subsets is not less than $n$, then there must exist 3 subsets among them, whose intersection is nonempty. Find the smallest possible $n$.

Answer: $n_{\min }=13$.

Proof. Firstly, we prove that the conclusion for $n=13$ is true. To prove it, we assume the contrary. Suppose that there exist 8 subsets of $X$ satisfying that the number of elements of the union of any 4 subsets of these sets is not less than 13 while any intersection of 3 subsets is empty. Then any 4-subset group of the 8 subsets corresponds least 13 elements in $X$. The number of such elements is at least $13\left(\begin{array}{l}8 \\ 4\end{array}\right)$. On the other hand, each element belongs to at most 2 subsets which means that each element is counted at most $\left(\begin{array}{l}8 \\ 4\end{array}\right)-\left(\begin{array}{l}6 \\ 4\end{array}\right)$ times. Therefore, $13\left(\begin{array}{l}8 \\ 4\end{array}\right) \leq 16\left(\left(\begin{array}{l}8 \\ 4\end{array}\right)-\left(\begin{array}{l}6 \\ 4\end{array}\right)\right)$, i.e., $16\left(\begin{array}{l}6 \\ 4\end{array}\right) \leq 3\left(\begin{array}{l}8 \\ 4\end{array}\right)$, which is a contradiction.

Secondly, we will prove $n \geq 13$. If not, assume $n \leq 12$ and $X=\{1,2, \cdots, 16\}$. Let

$$
\begin{aligned}
A_{i} & =\{4 i-3,4 i-2,4 i-1,4 i\} \quad(i=1,2,3,4), \\
B_{i} & =\{j, j+4, j+8, j+12\} \quad(j=1,2,3,4) .
\end{aligned}
$$

Obviously, the intersection for any 3 subsets is empty. Moreover,

$$
\begin{aligned}
& \left|A_{i} \cap A_{j}\right|=0(1 \leq i<j \leq 4), \\
& \left|B_{i} \cap B_{j}\right|=0(1 \leq i<j \leq 4), \\
& \left|A_{i} \cap B_{j}\right|=\quad 1(1 \leq i, j \leq 4),
\end{aligned}
$$

Therefore, for any subsets $P, Q, R, S$, if there exist 3 subsets equal to $A_{i}$ (or equal to $B_{j}$ at the same time), then the number of elements of the union of these subsets is $12 \geq n$. If 2 sets are $A_{i}$ and the other 2 sets are $B_{i}$, by inclusion and exclusion principle, we have

$$
|P \cup Q \cup R \cup S|=|P|+|Q|+|R|+|S|-2 \times 2=16-4=12 \geq n
$$

But the intersection of any 3 subsets is empty, which is a contraction.

In conclusion, the smallest possible $n$ is 13 .

The solution of Problem 0.1.3 needs a construction process, while Problems 0.1.1 and 0.1.2 do not. It is extremely important to assess students' ability of construction.

The following problem is more difficult than Problem 0.1.3.

Problem 0.1.4. Let $|X|=30$. For any 11 subsets of $X$, if the cardinal number of the union of any 5 subsets is not less than n, there exist 3 subsets whose intersection is nonempty. Find the smallest possible $n$.

The answer is 22 . We do not provide a solution here.

Problems 0.1.3 and 0.1.4 are both nice. However, their proofs are still based on taking mean value directly. We hope to transform the proof into two steps: using optimization first and then taking mean value. (Actually, the way that "delete the lowest score and the highest score, then take the mean value" is used a lot, which seems to be a better way of taking the mean value.) As a result, we proposed the sixth problem of the 21th CMO in 2006 (see [4]).

Problem 0.1.5. Let $|X|=56$. For any 15 subsets of $X$, if the number of elements of the union of any 7 subsets is not less than $n$, there exist 3 subsets among the 15 subsets, whose intersection is nonempty. Find the smallest possible $n$.

The answer is 41 . If we deal with the mean value for 15 subsets, we can only show that the minimum is no more than 42 . Therefore, we must use the optimization process: firstly we find the largest subset (the number of elements is at least 8) and delete it; then we take the mean value, which gives the desired result.

Proof. The smallest possible $n$ is 41 .

We first show that $n$ can be 41 . By contradiction, we assume: There exist 15 subsets of $X$ such that the union of any 7 subsets has no less than 41 elements, but the intersection of any 3 subsets is empty. Since each element belongs to at most 2 subsets, so we can assume without loss of generality that each element belongs exactly to 2 subsets (otherwise we can add some elements in subsets such that the condition above still holds). By the pigeonhole principle, there must be a subset, say $A$, has at least $\left\lceil\frac{2 \times 56}{15}\right\rceil+1=8$ elements. Denote the other 14 subsets by
$A_{1}, A_{2}, \ldots, A_{14}$. Consider any 7 subsets except $A$. They will correspond to 41 elements in $X$. All of them correspond to at least $41 C_{41}^{7}$ elements. On the other hand, for an element $a$, if $a \notin A$, then there are 2 subsets among $A_{1}, A_{2}, \ldots, A_{14}$ containing $a$. So $a$ is counted not more than $\left(\begin{array}{c}14 \\ 7\end{array}\right)-\left(\begin{array}{c}12 \\ 7\end{array}\right)$ times. If $a \in A$, then there is one subset among $A_{1}, A_{2}, \ldots, A_{14}$ containing $a$. So $a$ is counted $\left(\begin{array}{c}14 \\ 7\end{array}\right)-\left(\begin{array}{c}13 \\ 7\end{array}\right)$ times. Hence,

$$
\begin{aligned}
41 C_{41}^{7} & \leq(56-|A|)\left(C_{14}^{7}-C_{12}^{7}\right)+|A|\left(C_{14}^{7}-C_{13}^{7}\right) \\
& =56\left(C_{14}^{7}-C_{12}^{7}\right)-|A|\left(C_{13}^{7}-C_{12}^{7}\right) \\
& \leq 56\left(C_{14}^{7}-C_{12}^{7}\right)-8\left(C_{13}^{7}-C_{12}^{7}\right)
\end{aligned}
$$

which implies $196 \leq 195$, a contradiction.

Next we prove that $n \geq 41$.

We present a counterexample to show that $n$ can not be $\leq 40$. Let $X=\{1,2, \ldots, 56\}$, and let

$$
\begin{gathered}
A_{i}=\{i, i+7, i+14, i+21, i+28, i+35, i+42, i+49\}, \quad i=1,2, \ldots, 7, \\
B_{j}=\{j, j+8, j+16, j+24, j+32, j+40, j+48\}, \quad j=1,2, \ldots, 8 .
\end{gathered}
$$

Clearly,

$$
\begin{aligned}
& \left|A_{i}\right|=8(i=1,2, \ldots, 7), \\
& \left|A_{i} \cap A_{j}\right|=0(1 \leq i<j \leq 7), \\
& \left|B_{j}\right|=7(j=1,2, \ldots, 8), \\
& \left|B_{i} \cap B_{j}\right|=0(1 \leq i<j \leq 8), \\
& \left|A_{i} \cap B_{j}\right|=1(1 \leq i \leq 7,1 \leq j \leq 8) .
\end{aligned}
$$

For any 3 subsets, there must be 2 subsets belonging to $\left\{A_{1}, \ldots, A_{7}\right\}$ or belonging to $\left\{B_{1}, \ldots, B_{8}\right\}$, and thus their intersection is empty.

For any 7 subsets

$$
A_{i_{1}}, A_{i_{2}}, \ldots, A_{i_{s}}, B_{j_{1}}, B_{j_{2}}, \ldots, B_{j_{t}}, \quad(s+t=7),
$$

we have

$$
\begin{aligned}
& \left|A_{i_{1}} \cup A_{i_{2}} \cup \ldots \cup A_{i_{s}} \cup B_{j_{1}} \cup B_{j_{2}} \cup \ldots \cup B_{j_{t}}\right| \\
& =\left|A_{i_{1}}\right|+\left|A_{i_{2}}\right|+\ldots+\left|A_{i_{s}}\right|+\left|B_{j_{1}}\right|+\left|B_{j_{2}}\right|+\ldots+\left|B_{j_{t}}\right|-s t \\
& =8 s+7 t-s t=8 s+7(7-s)-s(7-s)
\end{aligned}
$$

$$
=(s-3)^{2}+40 \geq 40 \text {. }
$$

while the intersection of any 3 subsets is empty. Thus, the minimum $n$ is not less than 41 .

In conclusion, the smallest possible $n$ is exactly 41 .

Among the total 150 participants, only 10 of them completely solved this problem. It is a difficult problem, which was voted to be the best problem in the selection activities (voted by participants) sponsored by the Jiuzhang book store in Taiwan in that year.

## A counting problem for sequences

Problem 0.1.6. (1998, Bulgaria; 2010, Hongkong) Let $n$ be a given positive integer. How many sequences of $a_{1}, a_{2}, \ldots, a_{2 n}$ with $a_{i}=1$ or -1 such that for any $1 \leq k \leq m \leq n, k, m \in \mathbb{N}^{*}$,

$$
\left|\sum_{i=2 k-1}^{2 m} a_{i}\right| \leq 2 ?
$$

Question: Could we propose a similar counting problem for sequences of $\pm 1$ with length $2 n+1$ ? Finally, we modify the assumptions of Problem 0.1.6, and consider a more difficult "dual counting problem":

Problem 0.1.7. Find the number of the different sequences with terms $\pm 1$ and sequence length $2 n+1$ such that the absolute value of the sum of any odd successive terms is no greater than 1.

Sketch of Proof. Denote $S_{j}$ by the sum of preceding $j$ terms. Let $S_{0}=0$. We only consider the case $S_{1}=1$, and the case $S_{1}=-1$ is similar. It suffices to find the number of sequences $\left(S_{0}, S_{1}, \ldots, S_{2 n+1}\right)$ with $S_{0}=0, S_{1}=1, S_{j+1}=S_{j} \pm 1, j \geq 1$ such that, for any $0 \leq k, m \leq n$,

$$
\left|S_{2 k}-S_{2 m+1}\right| \leq 1
$$

Taking $m=0$ in (0.1.7) yields $S_{2 k}=0$ or 2 , and taking $k=0$ in (0.1.7) yields $S_{2 m+1}=-1$ or 1 .

There are two cases:

(1) The number of sequences with $S_{2 t+1}=1$ for each $1 \leq t \leq n$ is $2^{n}$.

(2) The number of sequences with $S_{2 t+1}=-1$ for some $t(1 \leq t \leq n)$ is $2^{n}-1$.

Then the number of sequences with $S_{1}=1$ satisfying given assumptions is $2^{n}+2^{n}-1=2^{n+1}-1$.

Thus, the number of sequences satisfying given conditions is $2\left(2^{n+1}-1\right)=2^{n+2}-2$.

## Inequalities for complex numbers from unit modulus

In this section, we will show an example of transforming a math Olympic problem to a research problem. It gives us some enlightenments that how to think, pose and find new problems by mathematical thinking.

Problem 0.1.8. (IMO, 2003) Let $n$ be a positive integer and let $x_{1} \leq x_{2} \leq \cdots \leq x_{n}$ be real numbers. Then

$$
\left(\sum_{i=1}^{n} \sum_{j=1}^{n}\left|x_{i}-x_{j}\right|\right)^{2} \leq \frac{2\left(n^{2}-1\right)}{3} \sum_{i=1}^{n} \sum_{j=1}^{n}\left(x_{i}-x_{j}\right)^{2} .
$$

Later, the reverse version of this inequality appeared in NSMath http://www.nsmath.cn/.

Problem 0.1.9. Let $x_{1}, x_{2}, \cdots, x_{n}$ be real numbers. Then

$$
\left(\sum_{1 \leq i<j \leq n}\left|x_{i}-x_{j}\right|\right)^{2} \geq(n-1) \sum_{1 \leq i<j \leq n}\left(x_{i}-x_{j}\right)^{2}
$$

Note that the above problem is translation invariant (i.e., invariant under the transformation $x_{i} \rightarrow$ $\left.x_{i}+t\right)$. Based on translation invariance, it is equivalent to the following:

Problem 0.1.10. Let $x_{1} \leq x_{2} \leq \cdots \leq x_{n}$ be real numbers with $\sum_{k=1}^{n} x_{k}=0$. Then

$$
\left(\sum_{k=1}^{n} k x_{k}\right)^{2} \geq \frac{n(n-1)}{4} \sum_{k=3}^{n} x_{k}^{2}
$$

Does it hold for complex numbers? We conjectured that the complex version of Problem 0.1.9 is still true.

Problem 0.1.11. Assume that $z_{1}, z_{2}, \cdots, z_{n} \in \mathbb{C}$. Then

$$
\left(\sum_{1 \leq k<j \leq n}\left|z_{k}-z_{j}\right|\right)^{2} \geq(n-1) \sum_{1 \leq k<j \leq n}\left(z_{k}-z_{j}\right)^{2}
$$

Shiquan Li, a student in Yali Middle School, proved our conjecture (see [2]).

If we restrict the complex number in Problem 0.1.11 on the unit circle, then we obtain a weaker inequality. However, we can improve it to the following version.

Problem 0.1.12. Let $z_{1}, z_{2}, \cdots, z_{n}$ be $n$ complex numbers on the unit circle with $\sum_{k=1}^{n} z_{k}=0$. Then

$$
\sum_{1 \leq k<j \leq n}\left|z_{k}-z_{j}\right| \geq \frac{n^{2}}{2}
$$

Proof.

$$
\begin{aligned}
\sum_{1 \leq k<j \leq n}\left|z_{k}-z_{j}\right| & =\frac{1}{2} \sum_{k=1}^{n} \sum_{j=1}^{n}\left|z_{k}-z_{j}\right| \geq \frac{1}{2} \sum_{k=1}^{n}\left|\sum_{j=1}^{n}\left(z_{k}-z_{j}\right)\right| \\
& =\frac{1}{2} \sum_{k=1}^{n} n\left|z_{k}\right|=\frac{n^{2}}{2} .
\end{aligned}
$$

Is the bound in Problem 0.1.12 optimal?

Problem 0.1.13. Let $z_{1}, z_{2}, \cdots, z_{n}$ be $n$ complex numbers on the unit circle with $\sum_{k=1}^{n} z_{k}=0$.

Denote

$$
S:=\sum_{1 \leq k<j \leq n}\left|z_{k}-z_{j}\right|
$$

(1) If $n$ is even, the minimum of $S$ is $\frac{n^{2}}{2}$.

$(2)^{*}$ If $n$ is odd, find the minimum of $S$.

Note that $(2)^{*}$ is not completely solved. Yunhao Fu tested the distribution of the minimum point and found a weaker lower bound. Xiaosheng Mu solved the case for $n=5$ completely.

The following is the reverse version of Problem 0.1.13.

Problem 0.1.14. Let $z_{1}, z_{2}, \cdots, z_{n}$ be $n$ complex numbers on the unit circle. Find the maximum of

$$
\sum_{1 \leq k<j \leq n}\left|z_{k}-z_{j}\right|
$$

The maximum is $n \cot \frac{\pi}{2 n}$. When $n$ points form a regular polygon, the sum attains its maximum.

Problem 0.1.14 is the 2-dimensional version of the following well-known Thompson problem.

Thompson's problem Let $x_{1}, x_{2}, \cdots, x_{n}$ be $n$ points in the unit sphere in $\mathbb{R}^{m}$. Find the maximum of

$$
\sum_{1 \leq k<j \leq n}\left|x_{k}-x_{j}\right|
$$

When $m=3$, the problem is the seventh problem in "Mathematical Problems in 21st Century" proposed by Smale, Fields awards owner, in 1998.

Based on our problems, we proposed the following reverse Thompson's problem. Actually Problems 0.1.12 and 0.1.13 are the special cases of this problem in dimension 2 .

Problem 0.1.15. Let $x_{1}, x_{2}, \cdots, x_{n}$ be $n$ points on the unit ball in $\mathbb{R}^{m}$ with $\sum_{k=1}^{n} x_{k}=0$ (the centroid is the origin). Find the minimum of

$$
\sum_{1 \leq k<j \leq n}\left|x_{k}-x_{j}\right| .
$$

It seems to be a difficult and new question!

Now it is clear for us that the background of Problem 0.1.8 (problem of IMO) is actually a 1dimensional (real number) Thompson's problem.

## Problems of short vectors

Problem 0.1.16. (ShahAli, AMM 2010) If a vector $v$ in $\mathbb{R}^{n}$ satisfies $\|v\| \leq 1$, then we call it a short vector. Let $v_{1}, v_{2}, \ldots, v_{6}$ be 6 short vectors in the plane such that their sum is zero. Prove that there exists three of them satisfying their sum is still a short vector.

In 2014, Xiaosheng Mu proposed the following generalization of Problem 0.1.16.

Problem 0.1.17. Suppose that the sum of $2 n$ vectors in the plane is zero. Prove that there are $n$ vectors among them such that their sum is a short vector.

It seems that the above two problems are not appropriate for Mathematical contest. Thus, we consider their special cases.

(1) The case of 1-dimensional real numbers

Problem 0.1.18. Let $x_{1}, x_{2}, \ldots, x_{6}$ be six real numbers in $[-1,1]$ such that their sum is zero. How many triples $(i, j, k), 1 \leq i<j<k \leq 6$, at least are there, such that $x_{i}+x_{j}+x_{k} \in[-1,1]$ ?

The answer is 12. It is a problem of medium difficulty.

(2) Problems of short vectors of cubes

Notice that when $v$ is a short vector, it means that $v$ belongs to an unit disk. If we replace the unit disk by unit cube (the unit ball of the normed space $l_{\infty}^{2}$ ), then we have

Problem 0.1.19. (2017, Summer Olympic Test of NSMath) Let

$$
A=\{z=x+y i|| x|\leq 1,| y \mid \leq 1, x, y \in \mathbb{R}\},
$$

and let $z_{1}, z_{2}, \cdots, z_{6} \in A$ with $\sum_{i=1}^{6} z_{i}=0$. Prove that there exist $1 \leq i<j<k \leq 6$ such that $z_{i}+z_{j}+z_{k} \in A$.

The common solution is viewing Problem 0.1.18 as a lemma, and then utilizing the counting method. Another elegant proof is to assume the contrary and to analyze the position of the sum of triples.

Next, we introduce these two solutions respectively.

Proof 1. The following lemma is needed.

Lemma Let $x_{1}, \ldots, x_{6} \in[-1,1]$ be real numbers such that their sum is 0 , then there exist 12 triples $\left(x_{i}, x_{j}, x_{k}\right)$ of $x_{1}, \ldots, x_{6}$ satisfying that the sum of each triple belongs to $[-1,1]$.

Proof of Lemma. We can assume that the number of nonnegative numbers among $x_{1}, \ldots, x_{6}$ is no less than the number of negative ones. Otherwise, we can replace $x_{1}, \ldots, x_{6}$ by $-x_{1}, \ldots,-x_{6}$. There are following 4 cases:

Case 1. $\left\{x_{1}, \ldots, x_{6}\right\}$ has 6 nonnegative numbers. In this case, $x_{1}=\cdots=x_{6}=0$. Thus, the sum of any triples of $x_{1}, \ldots, x_{6}$ belongs to $[-1,1]$. There are $\left(\begin{array}{l}6 \\ 3\end{array}\right)=20>12$ triples meeting the requirements of the lemma.

Case 2. $\left\{x_{1}, \ldots, x_{6}\right\}$ has exactly 5 nonnegative numbers. We can assume that the six numbers satisfy $x_{1}<0 \leq x_{2} \leq \cdots \leq x_{6} . \forall x_{i}, x_{j}, x_{k} \in\left\{x_{1}, \cdots, x_{6}\right\}$, if $x_{1} \notin\left\{x_{i}, x_{j}, x_{k}\right\}$, then

$$
0 \leq x_{i}+x_{j}+x_{k} \leq x_{2}+\cdots+x_{6}=-x_{1} \leq 1 ;
$$

If $x_{1} \in\left\{x_{i}, x_{j}, x_{k}\right\}$, then

$$
-1 \leq x_{i}+x_{j}+x_{k} \leq x_{1}+\cdots+x_{6}=0 .
$$

Thus, there are $\left(\begin{array}{l}6 \\ 3\end{array}\right)=20>12$ triples meeting the requirements of the lemma.

Case 3. $\left\{x_{1}, \ldots, x_{6}\right\}$ has exactly 4 nonnegative numbers. We can assume that the six numbers satisfy $x_{1} \leq x_{2}<0 \leq x_{3} \leq \cdots \leq x_{6} . \forall x_{i}, x_{j} \in\left\{x_{3}, \ldots, x_{6}\right\}$, we have

$$
-1 \leq x_{1}+x_{i}+x_{j} \leq \frac{x_{1}+x_{2}}{2}+x_{i}+x_{j}=-\sum_{t=3}^{6} \frac{x_{t}}{2}+x_{i}+x_{j} \leq \frac{x_{i}+x_{j}}{2} \leq 1
$$

Thus $x_{1}+x_{i}+x_{j} \in[-1,1]$ and

$$
x_{2}+x_{i}+x_{j}=-\left(x_{1}+\sum_{\substack{3 \leq t \leq 6, t \neq i, j}} x_{t}\right) \in[-1,1]
$$

So there are $\left(\begin{array}{l}4 \\ 2\end{array}\right) \times 2=12$ triples meeting the requirements of the lemma.

Case 4. $\left\{x_{1}, \ldots, x_{6}\right\}$ has exactly 3 nonnegative numbers. We can assume that the six numbers satisfy $x_{1} \leq x_{2} \leq x_{3}<0 \leq x_{4} \leq x_{5} \leq x_{6}$.

Assume that $\left|x_{3}\right| \leq\left|x_{4}\right|$. Otherwise, replace $x_{1}, \cdots, x_{6}$ by $-x_{1}, \cdots,-x_{6}$. Note that

$$
-1 \leq x_{2}+x_{5}+x_{6}=-x_{1}-x_{3}-x_{4} \leq 1-x_{3}+x_{3}=1
$$

i.e. $x_{2}+x_{5}+x_{6} \in[-1,1]$. Thus, for any $x_{i}, x_{j}$ from $x_{4}, x_{5}, x_{6}$ and any $x_{k}$ from $x_{1}, x_{2}$, we have

$$
-1 \leq x_{i}+x_{j}+x_{k} \leq x_{5}+x_{6}+x_{2} \leq 1,
$$

i.e. $x_{i}+x_{j}+x_{k} \in[-1,1]$. For any $x_{i}$ in $\left\{x_{4}, x_{5}, x_{6}\right\}$ and $x_{j}$ in $\left\{x_{1}, x_{2}\right\}$, we have

$$
x_{i}+x_{j}+x_{3}=-\left(\left(x_{4}+x_{5}+x_{6}-x_{i}\right)+\left(x_{1}+x_{2}-x_{j}\right)\right) \in[-1,1] .
$$

Therefore, there are $\left(\begin{array}{l}3 \\ 2\end{array}\right) \times\left(\begin{array}{l}2 \\ 1\end{array}\right)+\left(\begin{array}{l}3 \\ 1\end{array}\right) \times\left(\begin{array}{l}2 \\ 1\end{array}\right)=12$ triples meeting the requirements of the lemma.

In conclusion, there are always 12 triples meeting the requirements of the lemma. When $x_{1}=$ $x_{2}=-1, x_{3}=x_{4}=x_{5}=x_{6}=\frac{1}{2}$, there are exactly 12 triples meeting the requirements of the lemma. So 12 is optimal.

Back to the original problem. Let $z_{k}=a_{k}+i b_{k}(i=1, \cdots, 6)$. By the assumptions of the problem, we have $a_{k} \in[-1,1], \sum_{k=1}^{6} a_{k}=0$.

Let $A_{1}=\left\{(j, k, l) \mid 1 \leq j<k<l \leq 6, a_{j}+a_{k}+a_{l} \in[-1,1]\right\}$. By the lemma, $\left|A_{1}\right| \geq 12$.

Similarly, letting

$$
B_{1}=\left\{(j, k, l) \mid 1 \leq j<k \leq l \leq 6, b_{j}+b_{k}+b_{l} \in[-1,1]\right\},
$$

we also have $\left|B_{1}\right| \geq 12$.

$A_{1}, B_{1}$ are the subsets of $S=\{(j, k, l) \mid 1 \leq j<k<l \leq 6\}$. Since $|S|=C_{6}^{3}=20<\left|A_{1}\right|+$ $\left|B_{1}\right|, A_{1}$ and $B_{1}$ have a nonempty intersection. That is, $\exists 1 \leq j<k<l \leq 6$ such that both $a_{j}+a_{k}+a_{l}$ and $b_{j}+b_{k}+b_{l}$ belong to $[-1,1]$. Therefore $z_{j}+z_{k}+z_{l} \in A$.

Proof 2. Suppose the conclusion is not true. That is, $\forall 1 \leq i<j<k \leq 6$, the point $z_{i}+z_{j}+$ $z_{k}$ does not belong to the cube $A$.

Let

$$
\begin{aligned}
& H_{1}=\{x+i y \mid y<-1, x, y \in \mathbb{R}\}, \\
& H_{2}=\{x+i y \mid y>1, x, y \in \mathbb{R}\}, \\
& H_{3}=\{x+i y \mid x<-1, x, y \in \mathbb{R}\}, \\
& H_{4}=\{x+i y \mid x>1, x, y \in \mathbb{R}\} .
\end{aligned}
$$

We first prove the following lemma.

Lemma: Let $1 \leq i<j \leq 6$. For any $k_{1}, k_{2}$ satisfying $1 \leq k_{1}<k_{2} \leq 6, k_{1} \neq i, j$ and $k_{2} \neq$ $i, j$, the following cases will not appear.
(i) $z_{i}+z_{j}+z_{k_{1}}$ belongs to one of $H_{1}, H_{2}$ and $z_{i}+z_{j}+z_{k_{2}}$ belongs to the other;

(ii) $z_{i}+z_{j}+z_{k_{1}}$ belongs to one of $H_{3}, H_{4}$ and $z_{i}+z_{j}+z_{k_{2}}$ belongs to the other.

Proof of Lemma. If this lemma is not true, we have $\left|\operatorname{Re}\left(z_{k_{1}}-z_{k_{2}}\right)\right|>2$ or $\left|\operatorname{Im}\left(z_{k_{1}}-z_{k_{2}}\right)\right|>$ 2, which contradicts the definition of $A$.

By the lemma, there are two of $z_{1}+z_{2}+z_{3}, z_{1}+z_{2}+z_{4}, z_{1}+z_{2}+z_{5}$ belonging to the same $H_{l}$. Without loss of generality, we assume that $z_{1}+z_{2}+z_{3}, z_{1}+z_{2}+z_{4} \in H_{1}$. Combining with $\sum_{i=1}^{6} z_{i}=0$, we conclude that $z_{4}+z_{5}+z_{6} \in H_{2}$.

It follows from the facts $z_{1}+z_{2}+z_{4} \in H_{1}, z_{4}+z_{5}+z_{6} \in H_{2}$ and the lemma that $z_{1}+z_{4}+$ $z_{5}, z_{1}+z_{4}+z_{6}, z_{2}+z_{4}+z_{5}, z_{2}+z_{4}+z_{6}$ belong to neither $H_{1}$ nor $H_{2}$. Thus, these four numbers belong to $H_{3}$ or $H_{4}$. By the lemma, they must all belong to one of $H_{3}$ and $H_{4}$. Without loss of generality, we can assume that they all belong to $H_{3}$. By the assumption $\sum_{j=1}^{6} z_{j}=0$, we conclude that $z_{2}+z_{3}+z_{6} \in H_{4}$. By the lemma again, $z_{2}+z_{4}+z_{6} \in H_{4}$. A contradiction.

A stronger version of Problem 0.1.19 is

Problem 0.1.20. Let

$$
A=\{z=x+y i|| x|\leq 1,| y \mid \leq 1, x, y \in \mathbb{R}\},
$$

and let $z_{1}, z_{2}, \cdots, z_{6} \in A$ with $\sum_{i=1}^{6} z_{i}=0$. How many triples $(i, j, k), 1 \leq i<j<k \leq 6$, at least are there, such that $x_{i}+x_{j}+x_{k} \in A$ ?

The answer is 6. It seems a difficult question.

## Permutation Problems

First, we look at a simple example.

Problem 0.1.21. Do there exist 4 permutations $a_{1}, a_{2}, \cdots, a_{50} ; b_{1}, b_{2}, \cdots, b_{50} ; c_{1}, c_{2}, \cdots, c_{50}$; $d_{1}, d_{2}, \cdots, d_{50}$ of $1,2, \cdots, 50$, such that

$$
\sum_{i=1}^{50} a_{i} b_{i}=2 \sum_{i=1}^{50} c_{i} d_{i} ?
$$

Sketch of Proof. The answer is negative. In fact, let $S=\sum_{i=1}^{50} i x_{i}$. Then

$$
S_{\max }=\sum_{i=1}^{50} i^{2}=42925, \quad S_{\min }=\sum_{i=1}^{50} i(51-i)=22100 .
$$

Since $S_{\max }<2 S_{\min }$, it is impossible for equality.

This problem can be extended trivially to general $n$. However, as a strengthening version of Problem 0.1.21, the following problem is not trivial.

Problem 0.1.22. Let $x=\left\{x_{1}, x_{2}, \cdots, x_{n}\right\}$ be a permutation of $1,2, \cdots, n$. Denote $f(x)=$ $x_{1}+2 x_{2}+\cdots+n x_{n}$. Can the value $f(x)$ be any integer in the interval between $\sum_{i=1}^{n} i(n+1-i)$ and $\sum_{i=1}^{n} i^{2}$ ?

In 2009, we studied this question. We first considered the case $n=3$ : Let $\left\{x_{1}, x_{2}, x_{3}\right\}$ be a permutation of $1,2,3$. Then the range of $f(x)=x_{1}+2 x_{2}+3 x_{3}$ is $\{10,11,13,14\}$, without 12 . The number 12 is a "discontinuous point"!

It inspired us to think: For what kind of $n$, the range of $f(x)$ has discontinuous points? For what kind of $n$, the range of $f(x)$ is a set of successive positive integers?

By case studyp, we found that when $n \geq 4$ the range of $f(x)$ does not have discontinuous points.

Therefore, we proposed the following problem, which appeared in the Chinese Southeast Mathematical Olympiad in 2009 (see [5]).

Problem 0.1.23. Let $n \geq 4$ be a positive integer and denote by $A$ all the permutations of $1,2, \cdots, n$. For any $x_{n}=\left(a_{1}, a_{2}, \cdots, a_{n}\right) \in A$, let $f\left(x_{n}\right)=a_{1}+2 a_{2}+\cdots+n a_{n}$. Determine the cardinal number of the set $\left\{f\left(x_{n}\right) \mid x_{n} \in A\right\}$.

Proof. The solution is $\left|M_{n}\right|=\frac{n^{3}-n+6}{6}$.

We will prove

$$
M_{n}=\left\{\frac{n(n+1)(n+2)}{6}, \frac{n(n+1)(n+2)}{6}+1, \cdots, \frac{n(n+1)(2 n+1)}{6}\right\},
$$

by induction.

When $n=4$, by the rearrangement inequality, the minimal element and maximal element of the set $M$ is

$$
f(\{4,3,2,1\})=20 \text { and } f(\{1,2,3,4\})=30
$$

respectively.

Together with

$$
\begin{aligned}
& f(\{3,4,2,1\})=21, f(\{3,4,1,2\})=22, \\
& f(\{4,2,1,3\})=23, f(\{3,2,4,1\})=24, \\
& f(\{2,4,1,3\})=25, f(\{1,4,3,2\})=26,
\end{aligned}
$$

$$
\begin{array}{r}
f(\{1,4,2,3\})=27, f(\{2,1,4,3\})=28, \\
f(\{1,2,4,3\})=29,
\end{array}
$$

we have that $M_{4}=\{20,21, \cdots, 30\}$ has $\frac{4^{3}-4+6}{6}=11$ elements. Thus, the conclusion is true when $n=4$.

Assume that the conclusion holds for $n-1(n \geq 5)$. Next we prove it for $n$. Consider a permutation $X_{n-1}=\left\{x_{1}, x_{2}, \cdots, x_{n-1}\right\}$ of $1,2, \cdots, n-1$.

First, let $x_{n}=n$. We get a permutation $x_{1}, x_{2}, \cdots, x_{n-1}, n$ of $1,2, \cdots, n$. In this case,

$$
\sum_{k=1}^{n} k x_{k}=n^{2}+\sum_{k=1}^{n-1} k x_{k}
$$

By induction hypothesis, $\sum_{k=1}^{n} k x_{k}$ can attain any positive integer in the interval of

$$
\left[\frac{n\left(n^{2}+5\right)}{6}, \frac{n(n+1)(2 n+1)}{6}\right] \text {. }
$$

Anther way is to take $x_{n}=1$. We have

$$
\begin{aligned}
\sum_{k=1}^{n} k x_{k} & =n+\sum_{k=1}^{n-1} k x_{k} \\
& =\frac{n(n+1)}{2}+\sum_{k=1}^{n-1} k\left(x_{k}-1\right) .
\end{aligned}
$$

By induction hypothesis, $\sum_{k=1}^{n} k x_{k}$ can attain any positive integer in the interval of

$$
\left[\frac{n(n+1)(n+2)}{6}, \frac{2 n\left(n^{2}+2\right)}{6}\right] \text {. }
$$

Noticing that

$$
\frac{2 n\left(n^{2}+2\right)}{6} \geq \frac{n\left(n^{2}+5\right)}{6}
$$

we have that $\sum_{k=1}^{n} k x_{k}$ can attain any positive integer in the interval of

$$
\left[\frac{n(n+1)(n+2)}{6}, \frac{n(n+1)(2 n+1)}{6}\right] .
$$

Therefore, the conclusion holds for $n$, and our proof is completed by induction.

Hence, the cardinal number of $M_{n}$ is

$$
\frac{n(n+1)(2 n+1)}{6}-\frac{n(n+1)(n+2)}{6}+1=\frac{n^{3}-n+6}{6} \text {. }
$$

It is a question of medium difficulty.

## A discrete Wirtinger type inequality

The celebrated Wirtinger inequality states that:

If $f, f^{\prime} \in L^{2}[0, \pi]$, and $f$ is a function with a period of $2 \pi$ satisfying

$$
\int_{0}^{2 \pi} f(x) d x=0
$$

then

$$
\int_{0}^{2 \pi} f^{\prime}(x)^{2} d x \geq \int_{0}^{2 \pi} f^{2}(x) d x
$$

In 1950, Schoenberg [3] established the following discrete version of Wirtinger inequality.

If $z_{1}, z_{2}, \ldots, z_{n} n \geq 2$ are complex numbers such that $\sum_{k=1}^{n} z_{k}=0$, then

$$
\sum_{k=1}^{n}\left|z_{k+1}-z_{k}\right|^{2} \geq 4 \sin ^{2} \frac{\pi}{n} \sum_{k=1}^{n}\left|z_{k}\right|^{2}
$$

where $z_{n+1}=z_{1}$.

In 1992, Alzer [7] obtained a variant version of the discrete Wirtinger inequality.

If $z_{1}, z_{2}, \ldots, z_{n} n \geq 2$ are complex numbers such that $\sum_{k=1}^{n} z_{k}=0$, then

$$
\sum_{k=1}^{n}\left|z_{k+1}-z_{k}\right|^{2} \geq \frac{12 n}{n^{2}-1} \max _{1 \leq k \leq n}\left|z_{k}\right|^{2}
$$

where $z_{n+1}=z_{1}$. The constant $\frac{12 n}{n^{2}-1}$ is best possible.

Notice that the condition of $z_{n+1}=z_{1}$ is called the period condition. By this condition, the sum of $n$ differences $z_{2}-z_{1}, z_{3}-z_{2}, \ldots, z_{n}-z_{n-1}, z_{1}-z_{n}$ is zero. Without the period condition, is there an analogous Alzer type inequality? After a deal of contemplation, we proposed the following problem.

Problem 0.1.24. Let $n \geq 2$ be a given positive integer. Find the maximum of $\lambda(n)$ such that, for any complex numbers $z_{1}, z_{2}, \ldots, z_{n}$ satisfying $\sum_{k=1}^{n} z_{k}=0$, one has

$$
\sum_{k=1}^{n-1}\left|z_{k+1}-z_{k}\right|^{2} \geq \lambda(n) \max _{1 \leq k \leq n}\left|z_{k}\right|^{2}
$$

This question for real numbers is actually the first problem of CMO in 2006 (see [4]), while the solution is completely different from the Alzer inequality.

Another natural question is whether there exists a reserve Alzer inequality. So we have the following two problems.

Problem 0.1.25. (The reverse Alzer inequality under the non-period condition) If $z_{1}, z_{2}, \ldots, z_{n}$, $n \geq 2$, are complex numbers such that $\sum_{k=1}^{n} z_{k}=0$, then

$$
\sum_{k=1}^{n}\left|z_{k}\right|^{2} \geq \frac{1}{n}\left[\frac{n^{2}}{4}\right] \min _{1 \leq k \leq n-1}\left\{\left|z_{k+1}-z_{k}\right|^{2}\right\}
$$

where the coefficient $\frac{1}{n}\left[\frac{n^{2}}{4}\right]$ is best possible.

Problem 0.1.26. (The reverse Alzer inequality under the period condition) Let $n$ be a given positive integer. Find the maximum of $\lambda(n)$ such that, for any $n$ complex numbers $z_{1}, z_{2}, \ldots, z_{n}$, one has

$$
\sum_{k=1}^{n}\left|z_{k}\right|^{2} \geq \lambda(n) \min _{1 \leq k \leq n}\left\{\left|z_{k+1}-z_{k}\right|^{2}\right\}
$$

where $z_{n+1}=z_{1}$.

Solution. Let

$$
\lambda_{0}(n)= \begin{cases}\frac{n}{4} & \text { when } n \text { is even, } \\ \frac{n}{4 \cos ^{2} \frac{\pi}{2 n}} & \text { when } n \text { is odd }\end{cases}
$$

we will prove that $\lambda_{0}(n)$ is the maximum of $\lambda(n)$.

If there exists a positive number $k(1 \leq k \leq n)$ such that $\left|z_{k+1}-z_{k}\right|=0$, then the conclusion holds. Thus, we can assume that

$$
\min _{1 \leq k \leq n}\left\{\left|z_{k+1}-z_{k}\right|^{2}\right\}=1
$$

Under this condition, it suffices to prove that the minimal of $\sum_{k=1}^{n}\left|z_{k}\right|^{2}$ is $\lambda_{0}(n)$.

when $n$ is even, since

$$
\begin{aligned}
\sum_{k=1}^{n}\left|z_{k}\right|^{2} & =\frac{1}{2} \sum_{k=1}^{n}\left(\left|z_{k}\right|^{2}+\left|z_{k+1}\right|^{2}\right) \\
& \geq \frac{1}{4} \sum_{k=1}^{n}\left|z_{k+1}-z_{k}\right|^{2} \\
& \geq \frac{n}{4} \min _{1 \leq k \leq n}\left\{\left|z_{k+1}-z_{k}\right|^{2}\right\}=\frac{n}{4},
\end{aligned}
$$

the equality holds if $\left(z_{1}, z_{2}, \cdots, z_{n}\right)=\left(\frac{1}{2},-\frac{1}{2}, \cdots, \frac{1}{2},-\frac{1}{2}\right)$. Thus, the minimal of $\sum_{k=1}^{n}\left|z_{k}\right|^{2}$ is $\frac{n}{4}=\lambda_{0}(n)$.

We now consider the case that $n$ is odd. Let

$$
\theta_{k}=\arg \frac{z_{k+1}}{z_{k}} \in[0,2 \pi), k=1,2, \cdots, n .
$$

For each $k(k=1,2, \cdots, n)$, if $\theta_{k} \leq \frac{\pi}{2}$ or $\theta_{k} \geq \frac{3 \pi}{2}$, by ( 0.1 .8$)$, we have

$$
\begin{aligned}
\left|z_{k}\right|^{2}+\left|z_{k+1}\right|^{2} & =\left|z_{k}-z_{k+1}\right|^{2}+2\left|z_{k}\right|\left|z_{k+1}\right| \cos \theta_{k} \\
& \geq\left|z_{k}-z_{k+1}\right|^{2} \geq 1
\end{aligned}
$$

If $\theta_{k} \in\left(\frac{\pi}{2}, \frac{3 \pi}{2}\right)$, it follows from $\cos \theta_{k}<0$ and (0.1.8) that

$$
\begin{aligned}
1 & \leq\left|z_{k}-z_{k+1}\right|^{2} \\
& =\left|z_{k}\right|^{2}+\left|z_{k+1}\right|^{2}-2\left|z_{k}\right|\left|z_{k+1}\right| \cos \theta_{k} \\
& \leq\left(\left|z_{k}\right|^{2}+\left|z_{k+1}\right|^{2}\right)\left(1-2 \cos \theta_{k}\right) \\
& =\left(\left|z_{k}\right|^{2}+\left|z_{k+1}\right|^{2}\right) \cdot 2 \sin ^{2} \frac{\theta_{k}}{2} .
\end{aligned}
$$

Therefore,

$$
\left|z_{k}\right|^{2}+\left|z_{k+1}\right|^{2} \geq \frac{1}{2 \sin ^{2} \frac{\theta_{k}}{2}}
$$

Now, we consider the following two cases.

(i) If $\theta_{k} \in\left(\frac{\pi}{2}, \frac{3 \pi}{2}\right), \forall 1 \leq k \leq n$, by (0.1.10),

$$
\sum_{k=1}^{n}\left|z_{k}\right|^{2}=\frac{1}{2} \sum_{k=1}^{n}\left(\left|z_{k}\right|^{2}+\left|z_{k+1}\right|^{2}\right) \geq \frac{1}{4} \sum_{k=1}^{n} \frac{1}{\sin ^{2} \frac{\theta_{k}}{2}} .
$$

Since $\prod_{k=1}^{n} \frac{z_{k+1}}{z_{k}}=\frac{z_{n+1}}{z_{1}}=1$,

$$
\sum_{k=1}^{n} \theta_{k}=\arg \left(\prod_{k=1}^{n} \frac{z_{k+1}}{z_{k}}\right)+2 m \pi=2 m \pi
$$

where $m \in \mathbb{N}^{*}$ and $m<n$. Since $n$ is odd, it follows that

$$
0<\sin \frac{m \pi}{n} \leq \sin \frac{(n-1) \pi}{2 n}=\cos \frac{\pi}{2 n} .
$$

Let $f(x)=\frac{1}{\sin ^{2} x}, x \in\left[\frac{\pi}{4}, \frac{3 \pi}{4}\right]$, then $f(x)$ is a convex function. By (0.1.11), the Jensen inequality, (0.1.12) and (0.1.13),

$$
\begin{aligned}
\sum_{k=1}^{n}\left|z_{k}\right|^{2} & \geq \frac{1}{4} \sum_{k=1}^{n} \frac{1}{\sin ^{2} \frac{\theta_{k}}{2}} \geq \frac{n}{4} \cdot \frac{1}{\sin ^{2}\left(\frac{1}{n} \sum_{k=1}^{n} \frac{\theta_{k}}{2}\right)} \\
& =\frac{n}{4} \cdot \frac{1}{\sin ^{2} \frac{m \pi}{n}} \geq \frac{n}{4} \cdot \frac{1}{\cos ^{2} \frac{\pi}{2 n}}=\lambda_{0}(n) .
\end{aligned}
$$

(ii) If there exists a $j(1 \leq j \leq n)$ such that $\theta_{j} \notin\left(\frac{\pi}{2}, \frac{3 \pi}{2}\right)$, denote by

$$
I=\left\{j \left\lvert\, \theta_{j} \notin\left(\frac{\pi}{2}, \frac{3 \pi}{2}\right)\right., j=1,2, \cdots, n\right\} .
$$

By (0.1.9), we have that $\left|z_{j}\right|^{2}+\left|z_{j+1}\right|^{2} \geq 1, \forall j \in I$; By (0.1.10), for any $j \notin I$,

$$
\left|z_{j}\right|^{2}+\left|z_{j+1}\right|^{2} \geq \frac{1}{2 \sin ^{2} \frac{\theta_{j}}{2}} \geq \frac{1}{2}
$$

Therefore,

$$
\begin{aligned}
\sum_{k=1}^{n}\left|z_{k}\right|^{2} & =\frac{1}{2}\left(\sum_{j \in I}\left(\left|z_{j}\right|^{2}+\left|z_{j+1}\right|^{2}\right)+\sum_{j \notin I}\left(\left|z_{j}\right|^{2}+\left|z_{j+1}\right|^{2}\right)\right) \\
& \geq \frac{1}{2}|I|+\frac{1}{4}(n-|I|) \\
& =\frac{1}{4}(n+|I|) \geq \frac{n+1}{4} .
\end{aligned}
$$

Note that

$$
\begin{aligned}
& \frac{n+1}{4} \geq \frac{n}{4} \frac{1}{\cos ^{2} \frac{\pi}{2 n}} \\
\Leftrightarrow & \cos ^{2} \frac{\pi}{2 n} \geq \frac{n}{n+1} \\
\Leftrightarrow & \sin ^{2} \frac{\pi}{2 n}=1-\cos ^{2} \frac{\pi}{2 n} \leq 1-\frac{n}{n+1}=\frac{1}{n+1} .
\end{aligned}
$$

when $n=3,(0.1 .15)$ holds; When $n \geq 5$,

$$
\sin ^{2} \frac{\pi}{2 n}<\left(\frac{\pi}{2 n}\right)^{2}<\frac{\pi^{2}}{2 n} \cdot \frac{1}{n+1}<\frac{1}{n+1} .
$$

(0.1.15) also holds. Thus, for any odd number $n \geq 3$,

$$
\frac{n+1}{4} \geq \frac{n}{4} \cdot \frac{1}{\cos ^{2} \frac{\pi}{2 n}}
$$

Together with (0.1.14), we have

$$
\sum_{k=1}^{n}\left|z_{k}\right|^{2} \geq \frac{n}{4} \cdot \frac{1}{\cos ^{2} \frac{\pi}{2 n}}=\lambda_{0}(n)
$$

Note that if we assume

$$
z_{k}=\frac{1}{2 \cos \frac{\pi}{2 n}} \cdot e^{\frac{i(n-1) k \pi}{n}}, k=1,2, \cdots, n
$$

we have

$$
\left|z_{k}-z_{k+1}\right|=1, k=1,2, \cdots, n
$$

Thus, $\sum_{k=1}^{n}\left|z_{k}\right|^{2}=\lambda_{0}(n)$.

In conclusion, the maximum of $\lambda(n)$ is $\lambda_{0}(n)$.

The Problem 0.1.26 is actually the fifth problem of China TST in 2014 (see [6]). Among 60 students, only 6 students got it right.

## Acknowledgements

We would like to thank Ruixiang Zhang for their careful reading and suggestions to improve the original draft. Research of the second author is supported by a research grant from Shanghai Key Laboratory of PMMP $18 \mathrm{dz} 2271000$.

## References

[1] Radu Gologan and Dan Schwarz, Romanian Mathematical Competitions, Bucharest, 2004.

[2] Shiquan Li, A proof of the complex inequalities, 2016, http://www.nsmath.cn/

[3] I. J. Schoenberg, The finite Fourier series and elementary geometry. Amer. Math. Monthly 57 (1950), 390-404.

[4] Bin Xiong and Peng Yee Lee, Mathematical olympiad in China. Problems and solutions. World Scientific Publishing Co. Pte. Ltd., Hackensack, NJ; East China Normal University Press, Shanghai, 2007. xxii+251 pp. ISBN: 978-981-270-789-5; 981-270-789-1

[5] Bin Xiong and Peng Yee Lee, Mathematical Olympiad in China (2009-2010). Problems and solutions. Translated by Mathematical Olympiad Series, 9. World Scientific Publishing Co. Pte. Ltd., Hackensack, NJ; East China Normal University Press, Shanghai, 2013. xxvi+178 pp. ISBN: 978-981-4390-21-7

[6] Bin Xiong and Peng Yee Lee, Mathematical Olympiad in China (2011-2014). Problems and solutions. Mathematical Olympiad Series, 15. World Scientific Publishing Co. Pte. Ltd., Hackensack, NJ; East China Normal University Press, Shanghai, 2018. xxiv+344 pp. ISBN: 978-981-3142-93-0

[7] Horst Alzer, A continuous and a discrete variant of Wirtinger's inequality. Math. Pannon. 3 (1992), no. 1, 83-89.

## Bin Xiong*

School of Mathematical Sciences, East China Normal University, Shanghai 200241, China

Shanghai Key Laboratory of Pure Mathematics and Mathematical Practice, Shanghai 200241, China bxiong@math.ecnu.edu.cn

Gangsong Leng

Department of Mathematics, Shanghai University, Shanghai 200444, China

gleng@staff.shu.edu.cn

* Corresponding author

