# MATHEMATICS COMPETITIONS 



JOURNAL OF THE

WORLD FEDERATION OF NATIONAL

MATHEMATICS COMPETITIONS

## MATHEMATICS COMPETITIONS



JOURNAL OF THE

WORLD FEDERATION OF NATIONAL MATHEMATICS COMPETITIONS



# The Art of Proposing Problems in Mathematics Competitions I 

Bin Xiong and Gangsong Leng



Bin Xiong is a professor of mathematics education in the school of mathematics sciences at East China Normal University. His research interest is in problem solving and gifted education, with an emphasis on methodology of mathematics, theory of mathematics problem solving, mathematics education, and the identification and nurturing of talented students. He has published more than 100 papers and published or edited more than 150 books, both within China and abroad. He served as the leader of the Chinese National Team for the International Mathematical Olympiad for 10 times. He is also involved in the National Junior High School Competition, the National High School Mathematics Competition, the Western China Mathematical Olympiad and the Girls Mathematical Olympiad. In 2018, Prof. Xiong was awarded the Paul Erdös Award by the World Federation of National Mathematics Competitions.



Gangsong Leng is a professor in Department of Mathematics, Founder and Leader of the Convex Geometry group at Shanghai University. His major research interests are convex geometry and integral geometry. In his more than thirty years career, more than 100 academic papers have been published in J. Differential Geom., Adv. Math., Trans. Amer. Math. Soc., Math. Z. and other academic journals. In addition, he has published more than 50 papers on mathematics competition and mathematics education as well. He has been the coach of the National Training Team, and as well a member of the Main Examination Committee of China Mathematics Olympics (CMO). Since 2013, he has been the Chair of Main Examination Committee of the China Western Mathematical Olympiad. He served as the Leader of the China National Team for the International Mathematical Olympiad (IMO) in 2007, and also served as the Deputy Leader in 2006 and 2009. His research won ICCM Best Paper Award (2017), and his achievements on Mathematical Education won him the Paul Erdös Award of the World Federation of National Mathematics Competitions in 2020.

## Introduction

Problems are at the heart of mathematics.

Proposing good contest problems is crucial to mathematics competitions. What kind of contest problems is good? The criterion in mathematics is that the problems should be
natural, reasonable and also elegant, that is, with unique perspective, original structure and brief description. Since mathematics competitions are a time-limited and spacerestricted problem-solving activities, the educational criterion should be also taken into consideration. The problems should be of moderate difficulty, low threshold and adequate complexity. In short, a good math problem for high school students should be elementary mathematics problems, which are natural and elegant, yet with educational function.

Difficulty assessment is one important task in the problem-designing process. The test paper for mathematics competition is required to have three levels of problems: easy, intermediate and advanced, with a ratio of 2:2:2 in CMO (Chinese Mathematical Olympiad). Therefore, the test designer should assess the difficulty of every potential problem, especially from the perspective of students.

The goal of problem designers is to develop innovative problems with high item discrimination that uncover the beauty of mathematics.

We will provide some examples to share our experience in proposing problems in two parts. This paper is the first part.

## A problem originated from Tao's result

In 2009, the following result due to Terence Tao appeared in Romanian TST [3].

Theorem 1. Let $A, B \subseteq \mathbb{Z}$ be two finite sets. Then there exists $X \subseteq \mathbb{Z}$ satisfying $|X| \leq$ $\frac{|A+B|}{|B|}$ such that

$$
B \subseteq X+A-A,
$$

where $A+B=\{a+b \mid a \in A, b \in B\}, A-B=\{a-b \mid a \in A, b \in B\}$.

During our reading, we found an interesting fact. Consider a special case: Let $A=$ $\{-n,-n+1, \cdots, n-1, n\}$ and $B=\left\{x_{1}, x_{2}, \cdots, x_{m}\right\}$ be two sets of integers with $x_{1}<$ $x_{2}<\cdots<x_{m}$. By Tao's theorem, there exists a set $X \subseteq \mathbb{Z}$ satisfying

$$
|X| \leq 1+\frac{1}{2 n+1}\left(x_{m}-x_{1}\right)
$$

such that $x_{i}=x+s$, where $x \in X, s \in[-2 n, 2 n]$.

However, we found that Tao's result is not strong enough for this special case, and realized that the range of $s$ can be improved to $[-n, n]$. Thus, we used Tao's frame to produce a problem which requires new methods.

Problem 7. Let $m, n>1$ be two given integers and let $a_{1}<a_{2}<\cdots<a_{m}$ be $m$ integers. Prove that there exists a subset $T$ of integers such that

$$
|T| \leq 1+\frac{1}{2 n+1}\left(a_{m}-a_{1}\right)
$$

and for each $i \in\{1,2, \ldots, m\}, t \in T$ and $s \in[-n, n]$, one has $a_{i}=t+s$.

Solution. Let $a_{1}=a, a_{m}=b$ and

$$
b-a=(2 n+1) q+r
$$

where $q, r \in \mathbb{Z}, 0 \leq r \leq 2 n$.

Let

$$
T=\{a+n+(2 n+1) k \mid k=0,1, \cdots, q\} .
$$

Then,

$$
|T|=q+1 \leq 1+\frac{b-a}{2 n+1}
$$

and the set

$$
\begin{aligned}
B & :=\{t+s \mid t \in T, s=-n,-n+1, \cdots, n\} \\
& =\{a, a+1, \cdots, a+(2 n+1) q+2 n\} .
\end{aligned}
$$

Noticing that

$$
a+(2 n+1) q+2 n \geq a+(2 n+1) q+r=b
$$

we have that each $a_{i}$ belongs to $B$. The conclusion follows.

It was actually the fourth problem of the 25th CMO in 2010 (see [7]). During the exam, nearly three quarters of the students got it right.

## The expansion property of pedal triangles

Let $P$ be an interior point of $\triangle A B C$, and $D, E, F$ be the projection of $P$ onto $B C, C A, A B$ respectively. We call the triangle $\triangle D E F$ the pedal triangle about $P$.

There are the following two famous theorems in elementary geometry.

Theorem 2. The area of a parallelogram in any triangle is no more than half of the area of the triangle.

Theorem 3. Let $P$ be an interior point of $\triangle A B C$, then the area of the pedal triangle about $P$ is no more than $\frac{1}{4} S_{\triangle A B C}$.

We found that Theorem 3 can be deduced from Theorem 2. This is because that we established an expansion property of pedal triangle. Its special version for acute triangles became one of the problems in Chinese Western Mathematical Olympiad in 2003 (see [5]).

Problem 8. Let $P$ be an interior point of an acute triangle $\triangle A B C$, and let $\triangle D E F$ be the pedal triangle about $P$. Show that there is a parallelogram contained in $\triangle A B C$, such that its two adjacent edges are exactly two edges of $\triangle D E F$.

Proof. Let $O$ be the circumcenter of $\triangle A B C$. Since $\triangle A B C$ is acute, $O$ lies in the interior of $\triangle A B C$. Without loss of generality, we may assume that $P$ lie in $\triangle A O B$. See Figure 2.

To prove the parallelogram $D F E G$ with adjacent edges $F E, F D$ lies in $\triangle A B C$, we only need to prove

$$
\begin{aligned}
& \angle F E G \leq \angle F E C, \\
& \angle F D G \leq \angle F D C .
\end{aligned}
$$

Since

$$
\angle F E G=\angle A F E+\angle B F D, \angle F E C=\angle A F E+\angle A .
$$



Figure 2:

So to pove (0.0.2), we only need to prove

$$
\angle B F D \leq \angle A .
$$

In fact, since that four points $B, F, P$ and $D$ are on a circle, we have

$$
\angle B F D=\angle B P D \text {. }
$$

Draw a line $O H \perp B C$ with $H$ the foot of perpendicular. By

$$
\angle P B D \geq \angle B O H
$$

we have

$$
\angle B P D \leq \angle B O H .
$$

Moreover, since $O$ is the circumcenter of $\triangle A B C$, it follows that

$$
\angle B O H=\angle B A C=\angle A \text {. }
$$

From (0.0.5), (0.0.6), (0.0.7), (0.0.4), the proof of (0.0.2) is completed. The proof of (0.0.3) is similar.

## The cardinal number of the maximal independent set

S. Fajtlowicz proved the following result in [4].

Theorem 4. Suppose that $G$ is a simple graph with $n$ vertices and maximal degree $p$. Assume that $G$ does not contain the complete subgraph with $q$ vertices. If $p \geq q$, then the cardinal number $\alpha$ of the maximal independent set of $G$ satisfies

$$
\alpha \geq \frac{2 n}{p+q}
$$

Furthermore, S. Fajtlowicz studied the equality conditions for the above inequality in another paper [2] and proved the following.

Theorem 5. If $q \leq p$, then $\alpha=\frac{2 p}{p+q}$ implies $3 q-2 p \leq 5$. Moreover, for positive integers $p_{1}$ and $q_{1}$ with $3 q_{1}-2 p_{1}=5$, there exists an unique connected graph such that $p=p_{1}$, $q=q_{1}$ and $\alpha=\frac{2 n}{p+q}$.

After reading these two papers, we got an idea. Could we unite these results to yield a combinatorial extremal problem about the maximal independent subset of graphs? Testing some special values of $n, p, q$, we decided to set $n=30, p=5, q=5$ and proposed the following problem.

Problem 9. Let $G$ be a simple graph. Suppose that the degree of each vertex is at most 5, and for any 5 points of $G$, there are two points without any edge connecting them. Find the minimal cardinal number of the maximal independent subset.

The answer to this problem is 6 . The proof is not hard, but the construction is a challenge for us, because it would be tedious and non-intuitive if we perform the construction along with the original method. Finally, we found a simple but interesting combinatorial model. That is, we construct a graph $G$ that can be written as the disjoint union of 3 subgraphs, and each subgraph "looks like a pentagonal prism".

When we have the intuitive construction, it would be appropriate for competition test for high school students. To make the problem more interesting, we verified the statement and proposed the fifth problem of the 30th CMO in 2015 (see [8]).

Problem 10. There are 30 persons in a meeting. Each person has at most 5 acquaintances. For any 5 persons, there are at least 2 of them who do not know each other. Determine the maximal positive integer $k$ such that, for 30 persons satisfying the above conditions, there are $k$ persons who do not know each other.

Proof. The desired value of $k$ is 6 .

We can use 30 vertices to denote the persons. If two persons know each other, then we can draw an edge between the corresponding vertices. Thus, we get a simple graph $G$ with the vertex set of 30 points satisfying the following conditions:

(i) The degree of each vertex of $G$ is no more than 5 .

(ii) For any 5 vertices of $G$, there are 2 vertices without connecting edges.

Denote the vertex set of $G$ by $V$. If $A \subseteq G$ and any 2 vertices of $A$ have no connecting edge, then we call $A$ an "independent set" of $G$. An independent set is called the maximal independent set if its number of elements is maximal.

(1) We first show that the cardinal number of the maximal independent set of $G$ that satisfies the conditions is no less than 6 .

In fact, let $X$ be a maximal independent set of $G$. By the maximality of $|X|$, any vertex of $V \backslash X$ has an adjacent vertex in $X$. Otherwise, if $a \in V \backslash X$ does not have any adjacent vertices in $X$, then we can add the point $a$ into $X$ and get a bigger independent set. A contradiction. Thus, there are at least $|V \backslash X|=30-|X|$ edges between $V \backslash X$ and $X$. Notice that the degree of each vertex of $X$ is no more than 5. Hence, we have

$$
30-|X| \leq 5|X|
$$

which gives $|X| \geq 5$.

If $|X|=5$, then by the equality condition of (0.0.8), these $30-|X|=25$ edges are distributed to the 5 vertices of $X$; i.e., the adjacent vertex set of each vertex of $X$ is formed by 5 vertices of $V \backslash X$. Since $|V \backslash X|=25$, the adjacent vertex sets of any two vertices in $X$ do not intersect. Denote $X=\{a, b, c, d, e\}$. Consider the adjacent vertex set of $a$ and denote it by $Y_{a}=\left\{y_{1}, y_{2}, y_{3}, y_{4}, y_{5}\right\}$. By condition (ii), there are two vertices in $Y_{a}$ have no connecting edge, say $y_{1}, y_{2}$. Since the adjacent vertex sets of any two vertices do not intersect, $y_{1}, y_{2}$ are not the adjacent vertices of any point among $b, c, d, e$. Hence $\left\{y_{1}, y_{2}, b, c, d, e\right\}$ is an independent set of $G$, and the number of elements is greater than 5 . A contradiction. Therefore, $|X| \geq 6$.

(2) Next we will prove that there exists a graph $G$ satisfying the conditions such that the cardinal number of each maximal independent set is no more than 6 .

Divide $V$ into 3 sets $V_{1}, V_{2}, V_{3}$ such that $\left|V_{i}\right|=10, i=1,2,3$. Let

$V_{1}=\left\{A_{1}, A_{2}, A_{3}, A_{4}, A_{5}, B_{1}, B_{2}, B_{3}, B_{4}, B_{5}\right\}$. Connect the vertices of $V_{1}$ in the following way (as shown in Figure 3).



Figure 3:

(I) Connect edges $A_{i} A_{i+1}, i=1,2,3,4,5$;

(II) Connect edges $B_{i} B_{i+1}, i=1,2,3,4,5$;

(III) Connect edges $A_{i} B_{i}, A_{i} B_{i+1}, A_{i} B_{i-1}, i=1,2,3,4,5$,

where $A_{6}=A_{1}, B_{6}=B_{1}, B_{0}=B_{5}$.

The connecting ways of the vertex sets $V_{2}, V_{3}$ are completely the same as $V_{1}$, and for any $1 \leq i<j \leq 3$, there are no edges connecting $V_{i}$ and $V_{j}$. Then the degree of each vertex of $G$ is always 5 and there exist 2 vertices among any 5 vertices in $G$ without connecting edges.

For any maximal independent set $X$ of $G$, we will show $\left|V_{i} \cap X\right| \leq 2$.

In fact, since $A_{i}$ and $A_{i+1}$ are adjacent $(i=1,2,3,4,5)$, there are at most two sets among $A_{1}, \ldots, A_{5}$ belonging to $X$. Similarly, there are at most two sets among $B_{1}, \ldots, B_{5}$
belonging to $X$. If there are exactly two sets among $A_{1}, \ldots, A_{5}$ belonging to $X$, say $\left\{A_{1}, A_{3}\right\}$, then the union of the adjacent vertex sets of $A_{1}, A_{3}$ is precisely $\left\{B_{1}, B_{2}, B_{3}, B_{4}, B_{5}\right\}$. Thus, $B_{1}, B_{2}, B_{3}, B_{4}, B_{5}$ do not belong to $X$. Similarly, if there are exactly two sets among $B_{1}, \ldots, B_{5}$ belonging to $X$, then $A_{1}, A_{2}, A_{3}, A_{4}, A_{5}$ do not belong to $X$. This proves that $\left|V_{1} \cap X\right| \leq 2$.

A similar arguement yields $\left|V_{2} \cap X\right| \leq 2,\left|V_{3} \cap X\right| \leq 2$. Thus,

$$
|X|=|V \cap X|=\left|V_{1} \cap X\right|+\left|V_{2} \cap X\right|+\left|V_{3} \cap X\right| \leq 6 \text {. }
$$

Therefore, $G$ has the desired property.

By the results of (1) and (2), it follows that $k=6$.

During the exam, one fifth of the participants got it right, which indicates this problem is a hard problem.

## Finding isosceles trapezoids

In the 47th IMO (2007) in Vietnam, the leader of the Belorussian team presented some material to us, in which there were three problems for three grades in Belarus $(A, B, C)$ :

Problem 11. Color each point on the circle with red or blue. Each point is colored only once.

(1) Does there exist an equilateral triangle with vertices of the same color?

(2) Prove that there must be an isosceles triangle with vertices of the same color.

Solution: (1) The answer is negative. We only need to color one semicircle red and the other blue. Thus, there does not exist an equilateral triangle with vertices of the same color.

(2) Consider a regular pentagon inscribed in the circle. It is easy to see that there are at least 3 vertices of the same color among all 5 vertices. On the other hand, any 3 vertices of the regular pentagon form an isosceles triangle. The conclusion follows.

Problem 12. Color each point on the circle with red or blue. Each point is colored only once.

(1) Is there always an inscribed rectangle with vertices of the same color?

(2) Prove that there must be an inscribed trapezoid with vertices of the same color.

The answer of (1) is negative. It is easy to check by coloring two semicircles with different colors. In this case, there is no inscribed rectangles with vertices of the same color. The offprint from the manager of the Belorussian team did not provide the answer, but it claimed that (2) is a special case of the following problem.

Problem 13. Color each point on the circle with one of the $N$ colors. Each point is colored only once. Prove that there exists an isosceles trapezoid with vertices of the same color.

Proof 1. Let $A_{1}, A_{2}, \ldots, A_{N+1}$ be $n+1$ points on the circle. If the arc distances of any 2 adjacent points are all equal to a constant $a>0$ which is independent of $N$, then we call these $N+1$ points a block. Now we choose $N^{2}+1$ blocks on the semicircle which don't meet each other (It can be true if $a$ is small enough). Notice that each block has two points of the same color, and then we let the color be $C$ with the arc distance $l$ between these two points. Thus, each block is associated with a pair $(C, l)$. Since $(C, l)$ has exactly $N^{2}$ different values, by the pigeonhole principle, these $N^{2}+1$ blocks must have two blocks with the same pair $\left(C_{1}, l_{1}\right)$. So the four points of the same color in the two blocks form an isosceles trapezoid.

The advantage of Proof 1 is if we take such $N^{2}+1$ blocks from the semicircle, then we can find an isosceles trapezoid rather than a rectangle.

Proof 2. Let $K N+1$ be positive odd (where $K$ is an undetermined even number). Consider the vertices of a regular $(K N+1)$-polygon. By the pigeonhole principle, these must be $K+1$ vertices of the same color, whose arc distances have $\left(\begin{array}{c}K+1 \\ 2\end{array}\right)$ values. But the vertices of the $(K N+1)$-polygon yields $\frac{K N}{2}$ different arc distances. Thus, if $K$ satisfies

$$
\left(\begin{array}{c}
K+1 \\
2
\end{array}\right)>2 \cdot \frac{K N}{2}
$$

then we can find 3 arcs with endpoints of the same color, whose distances are identical when $K>2 N-1$. Hence there are two arcs of the same color without common endpoints, whose distances are identical. Because the diagonals of regular polygons with odd edges don't pass through the origin, such four vertices form an isosceles trapezoid with vertices of the same color.

The well-known van der Waerden theorem states that for any given positive integer $N$ and $l$, there exists $W(l, N)$ such that when $n>W(l, N)$, the set $\{1,2, \ldots, n\}$, after $N$-coloring, must have an $l$-term arithmetic progression with same color. (Another weaker but also very common version of van der Waerden's theorem says that the set of integers, after finite coloring, must have an arithmetic progression of the same color with arbitrary length.) The essence of Problem 13 is actually a special case of the van der Waerden theorem. In fact, let us divide the semicircle equally into $W(4, N)$ parts, and then denote the points of division by $1,2, \ldots, W(4, N)$. Then there exists an 4 -term arithmetic sequence with same color, and the corresponding four points form an isosceles trapezoid with same color.

All these problems and their background motivate us to design a new problem. They inspired us to find the isosceles trapezoid with same color in a regular odd $n$-polygon.

Problem 14. Find the smallest possible of $n$ such that, after 2 -coloring for the vertices of a regular odd n-polygon, there exists an isosceles trapezoid with vertices of same color.

Proof. Obviously, when $n \leq 7$, we can color any 4 points among vertices red and the others blue, where these 4 points don't form a trapezoid. Then there does not exist a trapezoid of the same color. So we always assume $n \geq 9$.

When $n=9$, we will show that after 2 -coloring for regular 9 -polygons, there exist trapezoids of the same color.

By pigeonhole principle, there are 5 points with same color. Assume that the color is red. For any vertices $A$ and $B$ of a regular 9-polygon, we connect $A B$ and consider the
minor arc $A B$. If the minor arc $A B$ contains $r-1$ vertices $(r=1,2,3,4)$ of the regular 9 -polygon, then we say that the span of the the minor $\operatorname{arc} A B$ is $r$. The 5 red points have $C_{5}^{2}=10$ spans. There are only 4 different spans, and thus there are $\left\lceil\frac{10}{4}\right\rceil+1=3$ pairs have a same span.

If the points in the 3 pairs don't form any regular triangles, then they must form a red trapezoid. If they form a regular triangle, then the span is 3 . Assume that these 3 red vertices are 1,4,7. There are at least 2 other red points. Each point forms a minor arc with one of $1,4,7$ with span of 1 . This yields a red isosceles trapezoid.

In conclusion, the smallest possible $n$ is 9 .

This problem is rather simple. To make it more difficult, we need to consider similar problems of 3-coloring for regular polygons with odd number of edges.

Problem 15. Find the smallest possible odd number $n$ such that among the vertices of a regular polygon with $n$ edges, after 3-colored, there exists an isosceles trapezoid with vertices of same color.

If we add another color, then the argument and construction become more difficult (Problem 13 didn't require any construction.)

Problem 15 is of great difficulty. Finally, we found that there is a counterexample for regular 15-polygon, and the minimum is 17 .

Now let us go further: in the previous discussion we focused on regular polygons with odd number of edges, because in that case we believe it would be easier to find isosceles trapezoids with same color. But it is possible that regular polygons with even numbers of edges may have rectangles with vertices all having the same color. This will precisely be the starting point of our new problem. We studied regular 16-polygons and 18-polygons, and we found counterexamples for the problem we just proposed for both polygons. The counterexample for regular 18-polygons is accidentally misleading for the problem related to general regular polygons. Indeed, it seems reasonable to guess that $n=19$ is the desired minimum based on the counterexample of $n=18$. Based on our study of the problem with three colors, the fifth problem of the 23th CMO in 2008 (See [6]) is as follows.

Problem 16. Find the smallest positive integer $n$ which has following properties: whenever we color each vertex of regular n-polygons arbitrarily with one of three colors (red, yellow, blue), there always exist four vertices with same color that are the vertices of an isosceles trapezoid.

Solution. The smallest possible $n$ is 17 .

We first show that the conclusion holds when $n=17$.

By contradiction, we assume that there is a way of coloring the vertices of the regular 17-polygon with three colors such that there do not exist four vertices of the same color such that they are the vertices of an isosceles trapezoid.

Since $\left[\frac{17-1}{3}\right]+1=6$, there must exist 6 vertices of same color, say, yellow. Connecting these 6 vertices with each other yields $\left(\begin{array}{c}6 \\ 2\end{array}\right)=15$ segments. Since the lengths of segments have only $\left\lceil\frac{17}{2}\right\rceil=8$ possible values, there must be one of the following two cases.

(1) There are 3 segments with the same length.

Notice that 17 is not a multiple of 3 . It is impossible that any 2 segments among these 3 segments have a common vertex. So there exist two segments with different vertices. Thus, these 4 vertices of 2 segments satisfy the requirement, a contradiction.

(2) There are 7 pairs of segments with the same length.

By assumption each pair of segments must have a common yellow vertex. Otherwise we can find 4 yellow vertices satisfy the requirement. By the pigeonhole principle, there must be two pairs of segments that share the common yellow vertex. The other 4 vertices of these 4 segments must be the vertices of an isosceles trapezoid, a contradiction.

Therefore, when $n=17$ the conclusion follows.

Next, when $n \leq 16$, we will construct a way of coloring, which does not satisfy the requirement. Denote the vertices of the regular $n$-polygon (clockwise) by $A_{1}, A_{2}, \ldots, A_{n}$. Let $M_{1}, M_{2}, M_{3}$ be the vertex sets of three colors, respectively.

If $n=16$, let

$$
\begin{aligned}
& M_{1}=\left\{A_{5}, A_{8}, A_{13}, A_{14}, A_{16}\right\}, \\
& M_{2}=\left\{A_{3}, A_{6}, A_{7}, A_{11}, A_{15}\right\}, \\
& M_{3}=\left\{A_{1}, A_{2}, A_{4}, A_{9}, A_{10}, A_{12}\right\} .
\end{aligned}
$$

For $M_{1}$, the distances from $A_{14}$ to any other verteices are unique, while the other 4 vertices are exactly the vertices of a rectangle. Similarly, one can verify that there do not exist 4 vertices in $M_{2}$, such that they are vertices of an isosceles trapezoid. For $M_{3}$, the 6 vertices are exactly the vertices of 3 diameters, so any 4 of them are either the vertices of a rectangle, or the vertices of a quadrilateral who is not an isosceles trapezoid.

If $n=15$, let

$$
\begin{aligned}
& M_{1}=\left\{A_{1}, A_{2}, A_{3}, A_{5}, A_{8}\right\}, \\
& M_{2}=\left\{A_{6}, A_{9}, A_{13}, A_{14}, A_{15}\right\}, \\
& M_{3}=\left\{A_{4}, A_{7}, A_{10}, A_{11}, A_{12}\right\},
\end{aligned}
$$

where each $M_{i}$ does not have 4 points who are the vertices of an isosceles trapezoid.

If $n=14$, let

$$
\begin{aligned}
& M_{1}=\left\{A_{1}, A_{3}, A_{8}, A_{10}, A_{14}\right\}, \\
& M_{2}=\left\{A_{4}, A_{5}, A_{7}, A_{11}, A_{12}\right\}, \\
& M_{3}=\left\{A_{2}, A_{6}, A_{9}, A_{13}\right\} .
\end{aligned}
$$

Each $M_{i}$ does not have 4 points satisfying that they are the vertices of an isosceles trapezoid.

If $n=13$, let

$$
\begin{aligned}
& M_{1}=\left\{A_{5}, A_{6}, A_{7}, A_{10}\right\}, \\
& M_{2}=\left\{A_{1}, A_{8}, A_{11}, A_{12}\right\}, \\
& M_{3}=\left\{A_{2}, A_{3}, A_{4}, A_{9}, A_{13}\right\} .
\end{aligned}
$$

Each $M_{i}$ does not have 4 points satisfying that they are the vertices of an isosceles trapezoid.

Deleting the vertex $A_{13}$, and then coloring other vertices as same as the case $n=13$, we get the coloring method for $n=12$. Next and similarly, deleting the vertex $A_{12}$ we get the coloring method for $n=11$. At last, deleting the vertex $A_{11}$ we get the coloring method for $n=10$.

When $n \leq 9$, we can let the number of vertices of same color be less than 4 . Thus there are not 4 vertices of same color, such that they are vertices of an isosceles trapezoid.

The above constructions show that the case $n \leq 16$ does not satisfy the requirement.

In conclusion, the smallest possible $n$ is 17 .

During the exam, nearly a quarter of students got it right, which indicates that this problem is of intermediate difficulty with high item discrimination.

## Problems on convex sequences

In the 1990s, the USA TST (see [1]) used the following problem.

Problem 17. Color each positive integer of $1,2, \cdots, \frac{n\left(n^{2}-2 n+3\right)}{2}(n \geq 2)$ by one of two colors (red and blue). Prove that there exists an n-term sequence $a_{1}<a_{2}<\cdots<a_{n}$ of the same color satisfying $a_{2}-a_{1} \leq a_{3}-a_{2} \leq \cdots \leq a_{n}-a_{n-1}$.

The solution depends on a strengthening induction.

Proof. Let $S_{n}=\frac{n\left(n^{2}-2 n+3\right)}{2}$. If a sequence $a_{1}<a_{2}<\cdots<a_{n}$ satisfies

$$
a_{2}-a_{1} \leq a_{3}-a_{2} \leq \cdots \leq a_{n}-a_{n-1} \leq m
$$

then we call it an $n$-term m-sequence.

By induction, we will prove a stronger proposition: after a 2 -coloring for $\left\{1,2, \cdots, S_{n}\right\}$, there must be contain an $n$-term $3\left(\begin{array}{l}n \\ 2\end{array}\right)$-sequence of the same color.

In fact, the case $n=2$ is trivial.

Assume that after a 2 -coloring for $\left\{1,2, \cdots, S_{n}\right\}$, there is a red $n$-term $3\left(\begin{array}{c}n \\ 2\end{array}\right)$-sequence. Notice that

$$
S_{n+1}-S_{n}=3\left(\begin{array}{l}
n \\
2
\end{array}\right)+\left(\begin{array}{c}
n \\
1
\end{array}\right)+1
$$

Consider the following $n+1$ numbers

$$
a_{n}+3\left(\begin{array}{l}
n \\
2
\end{array}\right), a_{n}+3\left(\begin{array}{l}
n \\
2
\end{array}\right)+1, \cdots, a_{n}+3\left(\begin{array}{l}
n \\
2
\end{array}\right)+n
$$

where

$$
a_{n}+3\left(\begin{array}{l}
n \\
2
\end{array}\right)+n<S_{n}+3\left(\begin{array}{l}
n \\
2
\end{array}\right)+\left(\begin{array}{c}
n \\
1
\end{array}\right)+1=S_{n+1} \text {. }
$$

If the terms are all blue, then we get a blue $(n+1)$-term 1 -sequence, and the conclusion follows. Otherwise, there is at least one red term, say, $a_{n}+3\left(\begin{array}{l}n \\ 2\end{array}\right)+k(0 \leq k \leq n)$. Let $a_{n+1}=a_{n}+3\left(\begin{array}{c}n \\ 2\end{array}\right)+k$. Then

$$
a_{n+1}-a_{n}=3\left(\begin{array}{l}
n \\
2
\end{array}\right)+k=3\left(\begin{array}{c}
n+1 \\
2
\end{array}\right)-3\left(\begin{array}{c}
n \\
1
\end{array}\right)+k \leq 3\left(\begin{array}{c}
n+1 \\
2
\end{array}\right) \text {. }
$$

Thus, we get a red $(n+1)$-term $3\left(\begin{array}{c}n+1 \\ 2\end{array}\right)$-sequence. The proof is completed by induction.

The above question shows that after a 2 -coloring for $1,2, \cdots, \frac{n\left(n^{2}-2 n+3\right)}{2}$, there exists an $n$-term convex sequence of the same color. It is a very interesting question, which often appeared in the frontier research in combinatorial mathematics. A natural question is whether the result $\frac{n\left(n^{2}-2 n+3\right)}{2}$ could become smaller.

Now we consider the following problem.

Problem 18. Find the minimum of positive integer $f(n)$ such that there exist a convex $n$-term sequence of the same color after 2-coloring for the sequence $1,2, \cdots, f(n)$.

Firstly, we concentrated on the solution of Problem 17 to improve the upper bound. We did find some ways to make the upper bound smaller. However, the improved upper bound is a polynomial of $n$ with degree 3 , which means that we had not succeed in improving upon the order of $n$. With many unsuccessful attempts, we were stuck.

One day, a simple but natural idea occurred to us: a counterexample shows that the upper bound can not be better than $n^{2}-n$.

In fact, we can do a 2-coloring in the following way: color one point red and another point blue, then color two points red and another two points blue, color three points red and another three points blue,......, and do this alternately. At last, we color $n-1$ points red and $n-1$ blue. For this coloring, there does not exist a convex $n$-term sequence with same color in $\left\{1,2, \cdots, n^{2}-n\right\}$.

With this counterexample, we may conjecture the minimum to be $f(n)=n^{2}-n+1$. Unfortunately, this conjecture remains open. However, this counterexample is sufficient to produce an intermediate contest problem as follows.

Problem 19. We color $n^{2}-n$ numbers: $1,2, \cdots, n^{2}-n(n \geq 2)$ red or blue. Prove that there exists a way of coloring such that there don't exist $n$ numbers $a_{1}<a_{2}<\cdots<a_{n}$ with same color satisfying $a_{k} \leq \frac{a_{k-1}+a_{k+1}}{2}(k=2,3, \cdots, n-1)$.

Compared with the original problem, Problem 19 is totally new, which can be restated in the language of set classifying. This is the third problem of the 23th CMO in 2008.

Problem 20. Given a positive integer $n$ with $n \geq 3$, prove that the set $X=\left\{1,2, \cdots, n^{2}-\right.$ $n\}$ can be divided into two disjoint nonempty subsets of $X$, such that these two subsets don't contain $n$ elements $a_{1}<a_{2}<\cdots<a_{n}$ satisfying $a_{k} \leq \frac{a_{k-1}+a_{k+1}}{2}(k=2,3, \cdots, n-1)$.

Proof. Define

$$
S_{k}=\left\{k^{2}-k+1, k^{2}-k+2, \ldots, k^{2}\right\}, \quad T_{k}=\left\{k^{2}+1, k^{2}+2, \ldots, k^{2}+k\right\}
$$

where $k=1,2, \ldots, n-1$. Let $S=\bigcup_{k=1}^{n-1} S_{k}, T=\bigcup_{k=1}^{n-1} T_{k}$. We will show that the sets $S, T$ satisfy the requirement.

Firstly, $S \cap T=\emptyset$ and $S \cup T=X$.

Secondly, if the set $S$ has $n$ elements $a_{1}, a_{2}, \ldots, a_{n}\left(a_{1}<a_{2}<\cdots<a_{n}\right)$ satisfying

$$
a_{k} \leq \frac{a_{k+1}+a_{k-1}}{2}
$$

where $k=2,3, \ldots, n-1$, then

$$
a_{k}-a_{k-1} \leq a_{k+1}-a_{k} .
$$

Assume without loss of generality that $a_{1} \in S_{i}$. Since $\left|S_{n-1}\right|<n$, it follows that $i<$ $n-1$. Thus, for $n$ elements $a_{1}, a_{2}, \ldots, a_{n}$, there are at least $n-\left|S_{i}\right|=n-i$ elements in $S_{i+1} \cup \cdots \cup S_{n-1}$. By the pigeonhole principle, there must be a $S_{j}(i<j<n)$ containing at least two elements. Let $a_{k} \in S_{j}$ such that $k$ is smallest possible, then $a_{k}, a_{k+1} \in S_{j}$.

But $a_{k-1} \in S_{1} \cup \cdots \cup S_{j-1}$, so $a_{k+1}-a_{k} \leq\left|S_{j}\right|-1=j-1, a_{k}-a_{k-1} \geq\left|T_{j-1}\right|+1=j$. Thus, $a_{k+1}-a_{k}<a_{k}-a_{k-1}$, which contradicts against (0.0.9). It implies that the set $S$ does not have $n$ elements satisfying the requirement.

Similarly, the set $T$ does not have such $n$ elements, either.

This shows that the sets $S, T$ satisfy the requirement.

We recalled that nearly one third of students gave the right answer, which shows this problem is of intermediate difficulty and has high item discrimination.

## Acknowledgements

We would like to thank Ruixiang Zhang for their careful reading and suggestion to improve the original draft. Research of the second author is supported by a research grant from Shanghai Key Laboratory of PMMP 18dz2271000.

## References

[1] Titu Andreescu and Zuming Feng, 102 combinatorial problems. From the training of the USA IMO team. Birkhäuser Boston, Inc., Boston, MA, 2003. xii+115 pp. ISBN:0-8176-4317-6.

[2] Siemion Fajtlowicz, Independence, clique size and maximum degree. Combinatorica 4 (1984), no. $1,35-38$.

[3] Radu Gologan and Dan Schwarz, Romanian Mathematical Competitions, Bucharest, 2009 .

[4] Siemion Fajtlowicz, On the size of independent sets in graphs, in: Frederick Hoffman, D. McCarthy, Ronald C. Mullin and Ralph G. Stanton (eds.), Proceedings of the Ninth Southeastern Conference on Combinatorics, Graph Theory, and Computing. Held at Florida Atlantic University, Boca Raton, Fla., January 30- February 2, 1978. Congressus Numerantium, XXI. Utilitas Mathematica Publishing, Inc., Winnipeg, Man., 1978. ISBN: 0-919628-21-4, 269-274.

[5] Bin Xiong and Peng Yee Lee, Mathematical olympiad in China. Problems and solutions. World Scientific Publishing Co. Pte. Ltd., Hackensack, NJ; East China Normal University Press, Shanghai, 2007. xxii+251 pp. ISBN: 978-981-270-789-5; 981-270-789-1

[6] Bin Xiong and Peng Yee Lee, Mathematical Olympiad in China (2007-2008). Problems and solutions. Edited by World Scientific Publishing Co. Pte. Ltd., Hackensack, NJ; East China Normal University Press, Shanghai, 2009. xxvi+194 pp. ISBN: 978-981-4261-14-2; 981-4261-14-9

[7] Bin Xiong and Peng Yee Lee, Mathematical Olympiad in China (2009-2010). Problems and solutions. Translated by Mathematical Olympiad Series, 9. World Scientific Publishing Co. Pte. Ltd., Hackensack, NJ; East China Normal University Press, Shanghai, 2013. xxvi+178 pp. ISBN: 978-981-4390-21-7

[8] Coaching team of China national team in 2015, Towards IMO, Mathematical Olympiad questions (Chinese), Shanghai, 2015.

Bin Xiong*

School of Mathematical Sciences, East China Normal University,

Shanghai 200241, China

Shanghai Key Laboratory of Pure Mathematics and Mathematical Practice, Shanghai 200241, China

bxiong@math.ecnu.edu.cn

Gangsong Leng

Department of Mathematics, Shanghai University,

Shanghai 200444, China

gleng@staff.shu.edu.cn

* Corresponding author

