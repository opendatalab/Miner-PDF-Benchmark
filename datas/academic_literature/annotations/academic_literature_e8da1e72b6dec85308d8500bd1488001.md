# Random matching in balanced bipartite graphs: The (un)fairness of draw mechanisms used in sports 

László Csató*<br>Institute for Computer Science and Control (SZTAKI)<br>Hungarian Research Network (HUN-REN)<br>Laboratory on Engineering and Management Intelligence<br>Research Group of Operations Research and Decision Systems<br>Corvinus University of Budapest (BCE)<br>Institute of Operations and Decision Sciences<br>Department of Operations Research and Actuarial Sciences<br>Budapest, Hungary

11th April 2024

"In these circumstances, any non-random assignment of resources is likely to be asymmetric and perceived as unfair. Randomization can restore symmetry, and thus a measure of fairness." 1


#### Abstract

The draw of some knockout tournaments requires finding a perfect matching in a balanced bipartite graph. The problem becomes challenging if there are draw constraints: the two field-proven procedures used in sports are known to be nonuniformly distributed, which may threaten fairness. Therefore, we compare the biases of both mechanisms, each of them having two forms, for reasonable subsets of balanced bipartite graphs up to 16 nodes. The UEFA Champions League Round of 16 draw is verified to apply the best design among the four available options. However, considerable scope remains to improve the performance of the known randomisation procedures.


Keywords: bipartite graph; constrained assignment; fairness; mechanism design; OR in sports

MSC class: 90-10, 90B90, 91B14

JEL classification number: $\mathrm{C} 44, \mathrm{C} 63, \mathrm{Z} 20$[^0]

## 1 Introduction

The knockout competition is one of the basic tournament designs (Scarf et al., 2009; Sziklai et al., 2022). If the brackets are not predetermined, then two sets of teams should often be paired randomly against each other. Other constraints can be formulated by the organiser to avoid repeated matchups and ensure geographic diversity. Perhaps the most famous example is the UEFA Champions League Round of $16 \mathrm{draw}$, where the eight group winners and the eight runners-up qualifying from the group stage have been matched against each other between the 2003/04 and 2023/24 seasons. However, the assignment has not been allowed to contain any pair of teams coming from the same group or national association.

This leads to a well-known mathematical problem: finding a perfect matching in a balanced bipartite graph (Hopcroft and Karp, 1973; Tanimoto et al., 1978). In order to guarantee the fairness of the draw, any team needs to play against any other team with the same probability as if a perfect matching would be chosen randomly. Otherwise, a team will get stronger opponents in expected terms and might feel cheated.

In theory, the required property can be easily achieved by either choosing uniformly from the set of all valid assignments (if the number of nodes is relatively small), or using a uniform rejection sampler (that produces a random perfect matching of the associated complete bipartite graph, which is repeated until the matching satisfies all constraints). However, these fair algorithms have at least two weaknesses: (1) the drama or entertainment value of the draw would be lost; and (2) all stakeholders should "trust" the computer to sample correctly, while their interests are often opposed. Even though the first issue can be solved via a Metropolis or swap algorithm (Klößner and Becker, 2013; Roberts and Rosenthal, 2023), transparency remains a challenging requirement. Indeed, it would be impossible to detect fraud and prevent conspiracy theories if a computer generates a perfect matching that is said random but certainly favours some teams at the expense of others.

Therefore, the draw mechanism should also be perceived and understood as fair by all participants, which necessitates the verification of each calculation at least ex-post. For instance, a mistake was recognised in the 2021/22 UEFA Champions League Round of 16 draw, hence, the whole process was repeated three hours later (Guyon, 2021).

According to our knowledge, there are two field-proven draw procedures in the realm of sports that can be used to find a random perfect matching in a balanced bipartite graph. The first, applied in European club football competitions, is called here the Drop mechanism. The second, applied in the group draw of various tournaments, including the FIBA Basketball World Cup and the FIFA World Cup, is called the Skip mechanism. In addition, both the Drop and Skip mechanisms have two forms depending on the side of the bipartite graph where they start, similar to the Gale-Shapley algorithm.

Naturally, there is no "free lunch" and all these transparent draw procedures are unfair, i.e., the feasible outcomes are not equally likely. Previous literature has analysed the distortions of the Drop (Kiesl, 2013; Klößner and Becker, 2013; Boczoń and Wilson, 2023) and the Skip (Csató, 2024; Roberts and Rosenthal, 2023) mechanism. However, they have never been compared, which will be attempted in the current paper. Since analytical calculations are cumbersome and should be done separately for each graph, the study is mainly limited to numerical results, analogous to the papers listed above. Nonetheless, we investigate a relatively large set of balanced bipartite graphs up to 16 nodes, which is also a crucial extension compared to the extant literature.

Our main contributions are as follows:

- The smallest bipartite graph is found for which the two mechanisms are unfair (Proposition 1);
- The Skip mechanism is proved to dominate the Drop mechanism on the set of balanced bipartite graphs containing eight nodes and constraints analogous to the UEFA Champions League Round of 16, which represents a potential draw of the quarterfinals in a sports tournament (Section 5.2);
- Some sufficient conditions are provided for the fairness of the Drop and Skip mechanisms (Section 5.4);
- It is documented that the mechanism currently used in the UEFA Champions League Round of 16 draw is the best option among the four known transparent and field-proven procedures (Section 5.5).

Furthermore, we refine and, to some degree, challenge previous results on the UEFA Champions League Round of 16 draw:

- In contrast to Boczoń and Wilson (2023, p. 3482), the potential gain from a fairness-optimal randomisation turns out to be far from being marginal in certain instances (Section 5.6);
- In contrast to Klößner and Becker (2013, Footnote 19), the effect of the draw order (the difference between the two forms of the Drop mechanism) is non-negligible (Section 5.6).

An important message for practitioners is that usually, more than one transparent randomisation procedure exists for a given allocation or assignment problem. It is advised to consider all field-proven solutions and choose the most appropriate lottery for the given setting after analysing their performance with respect to various theoretical properties such as fairness.

## 2 Related literature

Our paper is connected to two distinct lines of literature: the theory of random allocation mechanisms and fairness in tournament design.

The assignment problem, widely discussed in the field of market design, aims to allocate $n$ indivisible objects among $n$ agents such that any agent receives exactly one object, and monetary transfers are prohibited. Examples include assigning of jobs to workers or time slots to users of a common good. Using a lottery is a straightforward trick for guaranteeing fairness: the random priority mechanism draws a random ordering of the agents from the uniform distribution and lets them successively choose an object (Abdulkadiroğlu and Sönmez, 1998). However, while uniform draw is traditionally used in sports as will turn out in Section 3, the policy of choosing the opponents is rarely applied (Guyon, 2022; Hall and Liu, 2024; Lunander and Karlsson, 2023).

Hylland and Zeckhauser (1979) and Bogomolnaia and Moulin (2001) have developed an alternative solution to random assignment by directly identifying an expected assignment matrix that contains the probabilities with which the agents should get the objects. Budish et al. (2013) expand this theory to a much wider class of matching and assignment environments to accommodate multi-unit allocations and various real-world constraints,
such as different quotas. Boczoń and Wilson (2023) verify the power of this market design tool in the normative assessment of the UEFA Champions League Round of 16 draw.

The second approach, finding a procedure to reproduce an expected assignment matrix is natural in our setting since the ideal probabilities under uniform distribution can be easily calculated by a uniform rejection sampler (Roberts and Rosenthal, 2023). Indeed, Boczoń and Wilson (2023) conclude that the current design of the UEFA Champions League Round of 16 draw is near-optimal. However, they barely compare the official mechanism with reasonable alternatives, which will be presented in the following.

The draw of sports tournaments has been analysed in operational research and statistics, too. Before Boczoń and Wilson (2023, Proposition 2), the non-uniformity of the Drop mechanism has already been demonstrated by Guyon (2014); Kiesl (2013); Klößner and Becker (2013); Wallace and Haigh (2013). Even though the distortions in the probabilities seem to be marginal, these small biases may change the expected revenue of some teams by more than 10 thousand euros due to the substantial amount of prize money (Klößner and Becker, 2013). Thus, Roberts and Rosenthal (2023) have proposed various algorithms that guarantee uniform distribution - but they are more difficult to implement and understand than the Drop and Skip mechanisms.

Since draw constraints can be used in tournaments to achieve certain strategic goals such as minimising the threat of unfair behaviour (Csató, 2022b), the number and complexity of these conditions are expected to increase in the future. Section 3.2 will bring some evidence for this development, which probably increases the role of the draw procedure.

Naturally, random matching in a balanced bipartite graph makes sense only if at least one valid assignment exists. That can be checked by Hall's marriage theorem as shown by Kiesl (2013) and Wallace and Haigh (2013) for the UEFA Champions League Round of 16 draw.

Finally, note that, in contrast to the assignment problem in market design, the preferences of teams are ignored in sports competitions (and in our paper, too) since the organiser does not want to maximise welfare but approximate uniform distribution, guaranteeing that all outcomes are equally likely. An alternative interpretation can be that the teams have the same preference ordering on the set of their possible opponents because, for example, the strength of any team is given by a real number, which is common knowledge.

## 3 Randomisation procedures used in sports

It is a common problem in sports to divide the set of $n=k m$ contestants into $k$ sets of $m$. The allocation is often subject to some rules, such as the existence of $m$ seeding pots (when the $k$ highest-ranked teams are placed in the first pot, the next $k$ strongest in the second pot, and so on) to guarantee balancedness (Laliena and López, 2019), and different criteria that ensure geographical diversity for increasing attractiveness (Guyon, 2015). The seeding pots themselves do not imply any challenge since balls representing the teams can be drawn sequentially from urns associated with the seeding pots, which guarantees uniform distribution. However, the presence of other constraints makes some assignments invalid, and the draw procedure should produce an admissible matching. According to our knowledge, there are two draw mechanisms used to that end. They will be presented in Sections 3.1 and 3.2, respectively.

### 3.1 The UEFA Champions League Round of 16 draw and the Drop mechanism

The UEFA Champions League is the most prestigious European football club competition. Teams can qualify primarily based on the results of the domestic leagues in the previous year. Since the 1997/98 season, multiple entrants are allowed from the top national leagues.

The Champions League has been organised in the same format between the 2003/04 and 2023/24 seasons: a group stage played in eight home-away round-robin groups, where the top two teams qualify for the knockout stage (Csató et al., 2024). In the Round of 16, the eight group winners and the eight runners-up are divided into eight mutually disjoint pairs subject to the following restrictions:

- Bipartite constraint: a group winner should play against a runner-up;
- Group constraint: teams from the same group are not allowed to be paired;
- Association constraint: clubs from the same country cannot be matched.

The first restriction reduces the number of valid assignments to $8 !=40,320$ as every outcome can be represented by a permutation of the eight groups. The second restriction means that only a derangement (a permutation without a fixed point, where no element appears in its original position) is allowed, which decreases the number of feasible solutions to $! 8=\lfloor 8 ! / e+1 / 2\rfloor=14,833$ (Klößner and Becker, 2013) (the number of derangements of an $n$-element set is denoted by $! n$ ). Finally, the impact of the association constraint depends on the identity of the teams, and no simple combinatorial formula exists to determine the number of possible draw outcomes. For instance, there have been 9,200 feasible assignments in the 2005/06 season, but only 3,876 in the 2022/2023 season.

UEFA uses the following mechanism in the Round of 16 draw:

- Eight balls containing the names of the eight runners-up are placed in a bowl;
- A ball is drawn from the bowl, and the team drawn plays at home in match 1 ;
- The computer shows which group winners are eligible to play as the visiting team in match 1 ;
- Balls representing these teams are placed in another bowl;
- A ball is drawn from the second bowl to complete the pairing for match 1 ;
- The above procedure is repeated for the remaining matches.

The computer may indicate that only one group winner is allowed to play as the visiting team when this team is automatically assigned to the match.

In the following, this procedure will be called the Drop mechanism. It has two forms, depending on the side of the bipartite graph where it is started: UEFA draws the runner-up first, but the group winner can also be drawn first.

The Drop mechanism is more complicated than it seems at first glance because it should be checked not only whether draw conditions apply for the runner-up chosen at the moment, but also whether draw conditions are anticipated to apply for the teams still to be drawn. Let us see an illustration.

Table 1: Teams playing in the 2012/13 UEFA Champions League Round of 16

| Group |  | Runner-up |  | Group winner |  |
| :---: | :--- | :--- | :--- | :--- | :---: |
|  | Club | Country | Club | Country |  |
| A | Porto | Portugal | Paris Saint-Germain | France |  |
| B | Arsenal | England | Schalke 04 | Germany |  |
| C | Milan | Italy | Málaga | Spain |  |
| D | Real Madrid | Spain | Borussia Dortmund | Germany |  |
| E | Shakhtar Donetsk | Ukraine | Juventus | Italy |  |
| F | Valencia | Spain | Bayern München | Germany |  |
| G | Celtic Glasgow | Scotland | Barcelona | Spain |  |
| H | Galatasaray | Turkey | Manchester United | England |  |

Example 1. (Klößner and Becker, 2013) The participants of the 2012/13 UEFA Champions League Round of 16 are shown in Table 1. The draw happened as follows:

1. The runner-up Galatasaray was drawn first. Its eligible opponents were all teams except for Manchester United owing to the group constraint. Out of the seven group winners, Schalke 04 was drawn.
2. The runner-up Celtic Glasgow was drawn second. Its possible opponents were all teams except for Schalke 04 (already drawn), and Barcelona (group constraint). Out of the six group winners, Juventus was drawn.
3. The runner-up Arsenal was drawn third. Its admissible opponents were all teams except for Schalke 04, Juventus (already drawn), and Manchester United (association constraint). The group constraint was ineffective. Out of the five group winners, Bayern München was drawn.
4. The runner-up Shakhtar Donetsk was drawn fourth. Its eligible opponents were all teams except for Schalke 04, Juventus, and Bayern München (already drawn). Out of the five remaining group winners, Borussia Dortmund was drawn.
5. The runner-up Milan was drawn fifth. The computer indicated that it should be paired with Barcelona, hence, no draw was carried out.

Does this indicate a flaw? Naturally not. Four group winners (Paris Saint-Germain, Málaga, Barcelona, Manchester United) remained to be drawn. Málaga was prohibited by the group constraint. If Milan had played against the French or English team, then three pairings would have been left with four Spanish clubs (Real Madrid, Valencia, Málaga, Barcelona), and the association constraint would have been violated.

However, two (Real Madrid, Valencia) out of the three remaining runners-up still could have faced either Paris Saint-Germain or Manchester United. Therefore, the draw was not finished in the fifth round after Milan was drawn.

The same algorithm is used in other UEFA club competitions, too (Guyon and Meunier, 2023). The UEFA Cup Round of 32 draw was organised with both the association and the group constraints from 2004/05 until its final season of 2008/09 (UEFA, 2004). The competition was renamed to UEFA Europa League and retained both restrictions in the Round of 32 draw until the 2020/21 season (UEFA, 2009; Csató, 2022a). Between the

2021/22 and 2023/24 seasons, both the UEFA Europa League and the UEFA Europa Conference League contained knockout round play-offs contested by 16 teams as well as the Round of 16 , where the association constraint applied but the group constraint was not considered (UEFA, 2021a,b).

A live probability calculator for the UEFA club competitions in the 2023/24 season, based on the Drop mechanism, is available at https://julienguyon.github.io/UEFAdraws/. (Guyon and Meunier, 2023) summarise the mathematical background of the calculator.

### 3.2 The traditional algorithm for restricted group draw: the Skip mechanism

The FIFA World Cup is intended to contain geographically diverse groups since at least 1990. However, the draw of the 1990 (Jones, 1990), 2006 (Rathgeber and Rathgeber, 2007), and 2014 (Guyon, 2015) tournaments were seriously unfair. Hence, the French mathematician Julien Guyon has proposed using the Drop mechanism for the FIFA World Cup draw (Guyon, 2014) (this recommendation is missing from the published version of Guyon (2015)). FIFA has heard the message and adopted a credible and transparent draw procedure (Guyon, 2018): the team drawn is assigned to the first available slot in alphabetical order as indicated by the computer, meaning that a free slot may be "skipped". Let us see an illustration.

Example 2. Take the 2012/13 UEFA Champions League Round of 16 draw with the teams presented in Table 1. Assume that the runners-up are drawn first in the order Galatasaray, Celtic Glasgow, Arsenal, Shakhtar Donetsk, Milan, Real Madrid, Porto, and Valencia. After the urn of the runners-up is emptied, the draw continues with the urn of the group winners.

1. Schalke 04 is drawn first and matched with Galatasaray.
2. Juventus is drawn second and assigned to Celtic Glasgow.
3. Manchester United is drawn third and matched with Shakhtar Donetsk (the association constraint applies to Arsenal).
4. Bayern München is drawn fourth and assigned to Arsenal, which has had no opponent before.
5. Borussia Dortmund is drawn fifth and matched with Porto.

Why does Borussia Dortmund skip both Milan and Real Madrid? The situation is analogous to Example 1. Three group winners (Paris Saint-Germain, Málaga, Barcelona) remain to be drawn. If Milan plays against Borussia Dortmund, then three pairings will be left with four Spanish teams, and the association constraint will be violated. Furthermore, Real Madrid is not allowed to play against Borussia Dortmund due to the group constraint.

This procedure will be called the Skip mechanism.

It is used more extensively than the Drop mechanism, including the following contests:

- FIBA Basketball World Cup: 2019 (FIBA, 2019), 2023 (FIBA, 2023);
- FIFA World Cup: 2018 (FIFA, 2017), 2022 (FIFA, 2022);
- European qualifiers for the FIFA World Cup: 2018 (UEFA, 2015), 2022 (UEFA, 2020a);
- UEFA Euro qualifying: 2016 (UEFA, 2014), 2020 (UEFA, 2018a), 2024 (UEFA, 2022);
- UEFA Nations League: 2018/19 (UEFA, 2018b), 2020/21 (UEFA, 2020b), 2022/23 (UEFA, 2021c), 2024/25 (UEFA, 2024).

Interestingly, the set of constraints has somewhat evolved over the years. For example, the 2016 UEFA Euro qualifying draw and the draw of the European qualifiers for the 2018 FIFA World Cup contained only some prohibited clashes and required five teams to be drawn into larger groups, while the 2020 UEFA Euro qualifying draw applied restrictions due to host nations, prohibited clashes, winter venue, and excessive travel.

Naturally, the Skip mechanism has $m$ ! variants according to the possible orders of the pots. It usually starts with the pot containing the strongest teams, although the European qualifiers for the 2018 FIFA World Cup and the UEFA Nations League until 2022/23 have followed a reversed order. As our investigation is limited to bipartite graphs, the Skip mechanism has two different forms.

## 4 Methodology

The current section details the methodology of our study. Section 4.1 presents the basic mathematical notions connected to the setting. Section 4.2 overviews the graphs on which the draw mechanisms described in Section 4.3 are investigated. Last but not least, Section 4.4 discusses the comparison metrics.

### 4.1 Preliminaries

The nodes of a bipartite graph can be divided into two disjoint and independent sets $U$ and $V$ such that every edge is between a node in $U$ and a node in $V$. A bipartite graph is called balanced if $|U|=|V|=n$. A perfect matching is an independent edge set of size $n$.

For every bipartite graph $G$, the set of prohibited pairs, that is, the complement of graph $G$ will be considered. There are two kinds of constraints: pair constraints and type constraints. Each node in $U$ has a pair in $V$ and vice versa, and it might not be allowed for the perfect matching to contain these $n$ edges called pair constraints. Furthermore, every node has a type, which is different from the type of its pair. Type constraints imply that the perfect matching cannot contain any edge between two nodes of the same type.

In the complement of a graph $G$, the degree sequence of the set $U(V)$ lists the degrees of nodes in $U(V)$ in a non-increasing order. Without loss of generality, the degree sequence of the set $U$ is assumed not to be lexicographically smaller than the degree sequence of the set $V$ in the complement of any balanced bipartite graph $G$. In all figures, nodes of $U$ will be on the left-hand side, while nodes of $V$ on the right-hand side.

### 4.2 The choice of balanced bipartite graphs

Three kinds of balanced bipartite graphs will be studied. The first set consists of all graphs for $n=4$, both with and without pair constraints. The impact of adding one or two pairs of nodes with no additional type constraints will also be evaluated. The second set
is provided by the 20 historical UEFA Champions League seasons between 2003/04 and 2022/23. The third set contains the graph given by the 2017/18 Champions League Round of 16 (where set $U$ contains the runners-up since their degree sequence is lexicographically higher), and seven graphs of the same flavour.

For $n=4$, Figure 1 presents all the 31 possible graphs $G_{1}-G_{31}$ with pair constraints if the type of each node and its pair is different. The last four graphs $\left(G_{28}-G_{31}\right)$ have valid assignments only if $n \geq 5$. These graphs may represent the draw of the quarterfinals in a sports tournament, where four group winners and four runners-up should be matched such that teams from the same group cannot play against each other and no group contains more than one team of each type.

For $n=4$, Figure 2 presents all the 20 possible graphs $H_{1}-H_{31}$ without pair constraints. Their labelling follows the graphs $G_{1}-G_{31}$, for instance, $H_{12-14}$ can be obtained from either $G_{12}$, or $G_{13}$, or $G_{14}$ by removing the pair constraints. These graphs may represent the draw of the quarterfinals in a sports tournament, where four group winners and four runners-up should be matched such that teams from the same group are allowed to play against each other but no group contained more than one team from each type.

Finally, Figure 3 shows eight graphs, all representing possible outcomes in the UEFA Champions League Round of 16. From at most two national associations, five clubs can play in the group stage: five German (Spanish) teams have participated in the 2022/23 $(2023 / 24)$ season.

### 4.3 Draw mechanisms analysed

The Uniform mechanism is uniformly distributed over the set of perfect matchings, it chooses one matching randomly.

The Standard Drop mechanism is the Drop mechanism starting from the set $V$ (nodes on the right-hand side), while the Reversed Drop mechanism is the Drop mechanism starting from the set $U$ (nodes on the left-hand side).

The Standard Skip mechanism is the Skip mechanism starting from the set $U$ (nodes on the left-hand side), while the Reversed Skip mechanism is the Drop mechanism starting from the set $V$ (nodes on the right-hand side).

### 4.4 Quantifying unfairness

The (un)fairness of the draw mechanisms will be evaluated by focusing on the probability of matching two nodes. Let $p_{i j}$ be the ideal probability that nodes $i$ and $j$ are matched under the Uniform mechanism, and $p_{i j}^{M}$ be the probability of this event if mechanism $M$ is used to obtain a feasible assignment. Two fairness distortion measures for mechanism $M$ are introduced as follows:

$$
\begin{aligned}
& A F D(M)=100 \cdot \frac{\sum_{i, j}\left|p_{i j}-p_{i j}^{M}\right|}{\sum_{i, j} \#\left\{p_{i j}>0\right\}} \\
& M F D(M)=100 \cdot \max _{i, j}\left|p_{i j}-p_{i j}^{M}\right|
\end{aligned}
$$

where $\sum_{i, j} \#\left\{p_{i j}>0\right\}$ is the number of pairs with a positive probability.

AFD is called average fairness distortion and MFD is called maximal fairness distortion. Obviously, AFD allows the draw mechanism to compensate for the increased unfairness regarding a particular pair of nodes with a reduction in other pairs, while this is not possible
(a) $G_{1}: 0 / 9$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=211&width=263&top_left_y=303&top_left_x=314)

(e) $G_{5}: 2 / 5$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=208&width=257&top_left_y=570&top_left_x=317)

(i) $G_{9}: 4 / 2$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=206&width=257&top_left_y=831&top_left_x=317)

(m) $G_{13}: 3 / 3$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=205&width=257&top_left_y=1094&top_left_x=317)

(q) $G_{17}: 4 / 2$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=205&width=257&top_left_y=1351&top_left_x=317)

(u) $G_{21}: 5 / 1$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=206&width=257&top_left_y=1616&top_left_x=317)

(y) $G_{25}: 6 / 1$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=214&width=259&top_left_y=1875&top_left_x=316)

(b) $G_{2}: 1 / 6$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=203&width=260&top_left_y=304&top_left_x=704)

(f) $G_{6}: 3 / 4$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=208&width=257&top_left_y=570&top_left_x=708)

(j) $G_{10}: 4 / 4$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=200&width=257&top_left_y=834&top_left_x=708)

(n) $G_{14}: 3 / 2$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=205&width=260&top_left_y=1094&top_left_x=704)

(r) $G_{18}: 4 / 1$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=205&width=254&top_left_y=1351&top_left_x=707)

(v) $G_{22}: 5 / 2$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=206&width=260&top_left_y=1619&top_left_x=704)

(z) $G_{26}: 6 / 1$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=209&width=257&top_left_y=1877&top_left_x=708)

(c) $G_{3}: 2 / 4$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=200&width=260&top_left_y=308&top_left_x=1098)

(g) $G_{7}: 3 / 3$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=202&width=257&top_left_y=573&top_left_x=1096)

(k) $G_{11}: 2 / 3$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=206&width=257&top_left_y=828&top_left_x=1096)

(o) $G_{15}: 4 / 2$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=205&width=257&top_left_y=1094&top_left_x=1096)

(s) $G_{19}: 4 / 1$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=205&width=257&top_left_y=1351&top_left_x=1096)

(w) $G_{23}: 4 / 1$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=206&width=257&top_left_y=1619&top_left_x=1096)

(aa) $G_{27}: 8 / 1$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=209&width=257&top_left_y=1877&top_left_x=1096)

(d) $G_{4}: 2 / 4$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=208&width=272&top_left_y=307&top_left_x=1486)

(h) $G_{8}: 3 / 3$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=212&width=263&top_left_y=565&top_left_x=1482)

(1) $G_{12}: 3 / 2$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=206&width=260&top_left_y=828&top_left_x=1486)

(p) $G_{16}: 4 / 2$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=200&width=260&top_left_y=1096&top_left_x=1483)

(t) $G_{20}: 4 / 3$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=205&width=272&top_left_y=1351&top_left_x=1483)

(x) $G_{24}: 5 / 1$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=202&width=260&top_left_y=1618&top_left_x=1483)

(ab) $G_{28}: 3 / 0$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=206&width=257&top_left_y=1876&top_left_x=1485)

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=251&width=249&top_left_y=2096&top_left_x=515)

(ad) $G_{30}: 5 / 0$

(ae) $G_{31}: 6 / 0$
![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-10.jpg?height=204&width=648&top_left_y=2142&top_left_x=904)

Figure 1: Balanced bipartite graphs with eight nodes, pair and type constraints

Notes: Dashed lines indicate the pair constraints, solid lines indicate the type constraints.

The first (second) number shows the number of type exclusions (the number of valid assignments).

under $M F D$. Furthermore, the value of $M F D$ has a more straightforward interpretation:

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-11.jpg?height=1330&width=1456&top_left_y=243&top_left_x=308)

(a) $H_{1}: 0 / 24$

(e) $H_{9-10}: 4 / 9$

(i) $H_{17}: 4 / 8$

(m) $H_{24}: 5 / 4$

(q) $H_{28}: 3 / 6$ (b) $H_{2}: 1 / 18$

(f) $H_{11}: 2 / 12$

(j) $H_{18-20}: 4 / 8$

(n) $H_{25}: 6 / 4$

(r) $H_{29}: 4 / 6$ (c) $H_{3-5}: 2 / 14$

(g) $H_{12-14}: 3 / 10$

(k) $H_{21-22}: 5 / 6$

(o) $H_{26}: 6 / 4$

(s) $H_{30}: 5 / 6$ (d) $H_{6-8}: 3 / 11$

(h) $H_{15-16}: 4 / 8$

(1) $H_{23}: 4 / 4$

(p) $H_{27}: 8 / 4$

(t) $H_{31}: 6 / 6$

Figure 2: Balanced bipartite graphs with eight nodes and type constraints

Notes: Solid lines indicate the type constraints.

The first (second) number shows the number of type exclusions (the number of valid assignments).

how much is the probability of a potential pair changed by mechanism $M$ compared to the uniform draw in the worst case. The multiplier 100 in formulas (1) and (2) means that both fairness distortions can be interpreted as a percentage.

The maximum of $\sum_{i, j} \#\left\{p_{i j}>0\right\}$ is $n(n-1)$, which is reached if the type constraint is ineffective. However, this has never happened in the UEFA Champions League, where the denominator varies between 43 (2019/20) and 53 (five seasons).

Note that not only the Uniform mechanism may be undistorted. However, if a draw procedure implies that each team has the same probability to play against any of its possible opponents as under the Uniform mechanism, no team can effectively argue against this draw procedure.

Two draw procedures $M_{1}$ and $M_{2}$ are said to coincide for graph $G$ if $p_{i j}^{M_{1}}=p_{i j}^{M_{2}}$ for every $i \in U$ and $j \in V$.

For $n \leq 6$ (Sections 5.1-5.3), we compute the exact probabilities via complete enumeration. If $n=8$ (Sections 5.5 and 5.6), the draw mechanisms are simulated $N=10^{8}$ times, which leads to 95 percent confidence intervals smaller than $\pm 0.00015$ based on Boczoń and Wilson (2023, Proposition 4). This upper bound takes into account that a conservative estimate for the assignment probability is 0.5 rather than 0.25 since the probability of
(a) $I_{1}: 7$ excl., \#4238

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-12.jpg?height=400&width=259&top_left_y=308&top_left_x=316)

(e) $I_{5}: 9$ excl., \#3077

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-12.jpg?height=403&width=259&top_left_y=792&top_left_x=316)

(b) $I_{2}: 8$ excl., $\# 3620$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-12.jpg?height=399&width=260&top_left_y=306&top_left_x=704)

(f) $I_{6}: 9$ excl., \#2896

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-12.jpg?height=402&width=260&top_left_y=787&top_left_x=704)

(c) $I_{3}: 8$ excl., 3854

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-12.jpg?height=397&width=260&top_left_y=310&top_left_x=1092)

(g) $I_{7}: 8$ excl., \#3779

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-12.jpg?height=396&width=257&top_left_y=790&top_left_x=1096)

(d) $I_{4}: 9$ excl., \#3002

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-12.jpg?height=397&width=260&top_left_y=310&top_left_x=1486)

(h) $I_{8}: 9$ excl., \#3152

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-12.jpg?height=397&width=257&top_left_y=787&top_left_x=1485)

Figure 3: Some balanced bipartite graphs with 16 nodes

Notes: Dashed lines indicate the pair constraints, solid lines indicate the type constraints. The number after \# shows the number of valid assignments.

Barcelona versus Chelsea is $43.75 \%$ in the 2017/18 UEFA Champions League Round of 16 .

Boczoń and Wilson (2023) use a more complicated quantification of fairness that computes the average absolute difference in the match likelihoods across all valid pairwise comparisons. Consequently, their distortion metric equals zero only in the absence of draw constraints, and increases with the number of restricted pairs. On the other hand, both $A F D$ and MFD are zero for the Uniform mechanism.

## 5 Results

This section presents our findings. Section 5.1 shows the smallest balanced bipartite graph, for which the Drop and Skip mechanisms are unfair. Section 5.2 presents the distortions on the graphs displayed in Figures 1 and 2. Section 5.3 analyses the same graphs after adding one or two pairs of nodes without further type constraints. Based on these calculations, Section 5.4 provides sufficient conditions for the fairness of our draw procedures. Section 5.5 investigates the graphs provided by the 20 historical Champions League seasons, while Section 5.6 discusses the graphs shown in Figure 3.

### 5.1 The unfairness of the draw mechanisms: a minimal example

The first statement uncovers the simplest case when the draw mechanisms used in sports are distributed non-uniformly. The calculation is not especially interesting, but it clearly reveals why the derivation of general analytical results is close to impossible.

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-13.jpg?height=440&width=440&top_left_y=228&top_left_x=814)

Figure 4: The only balanced bipartite graph up to six nodes where unfairness emerges Note: Solid lines indicate the type constraints.

Proposition 1. Assume that $n \leq 3$. The Standard Drop, Reversed Drop, Standard Skip, and Reversed Skip mechanisms coincide and there exists only one graph for which they are unfair.

Proof. All bipartite graphs with $n \leq 3$ have been checked via complete enumeration. The unique graph for which unfairness emerges is shown in Figure 4. In the case of all draw mechanisms, we compute the probability of nodes $a$ and $B$ being matched.

Uniform mechanism: There are $3 !=6$ assignments in the absence of the constraints. Both the first (nodes $a$ and $A$ ) and the second (nodes $b$ and $B$ ) type constraints exclude $2 !=2$ assignments, respectively. However, $1 !=1$ among them is counted twice, thus, the number of valid assignments equals 3 . Nodes $a$ and $B$ are matched in $2 !=2$ assignments, the corresponding probability is $2 / 3$.

Drop mechanism: Five cases will be distinguished with respect to the draw order of the nodes in $U$ :

- Node $a$ is drawn first (this event has a chance of $1 / 3$ ): Node $a$ has two possible pairs $(B$ and $C$ ), $B$ is chosen with a probability of $1 / 2$.
- Node $a$ is drawn second and node $b$ is drawn first (this event has a chance of $1 / 6$ ): Node $b$ has two possible pairs $(A$ and $C$ ).

If $b$ is assigned to $A$, node $a$ has two possible pairs ( $B$ and $C$ ) among the remaining nodes, $B$ is chosen with a probability of $1 / 2$.

If $b$ is assigned to $C$, node $a$ has only one possible pair ( $B$ ) among the remaining nodes.

- Node $a$ is drawn second and node $b$ is drawn third (this event has a chance of $1 / 6)$ : Node $c$ has three possible pairs.

If $c$ is assigned to $A$, node $a$ has two possible pairs ( $B$ and $C$ ) among the remaining two nodes. However, $b$ cannot be assigned to $B$, hence, $B$ is chosen with a probability of 1 .

If $c$ is assigned to $B$, node $a$ cannot be matched with $B$.

If $c$ is assigned to $C$, node $a$ has only one possible pair ( $B$ ) among the remaining two nodes.

- Node $a$ is drawn third and node $b$ is drawn first (this event has a chance of $1 / 6$ ): Node $b$ has two possible pairs $(A$ and $C$ ).

If $b$ is assigned to $A$, node $c$ has two possible pairs ( $B$ and $C$ ) among the remaining
two nodes. Thus, the probability that $a$ is paired with $B$ equals $1 / 2$.

If $b$ is assigned to $C$, node $c$ has two possible pairs $(A$ and $B$ ) among the remaining two nodes. However, $a$ cannot be assigned to $A$, hence, the probability that $a$ is paired with $B$ equals 1.

- Node $a$ is drawn third and node $b$ is drawn second (this event has a chance of $1 / 6)$ : Node $c$ has three possible pairs.

If $c$ is assigned to $A$, node $b$ has only one possible pair $(C)$ among the remaining two nodes, and node $a$ will certainly be matched with $B$.

If $c$ is assigned to $B$, node $a$ cannot be matched with $B$.

If $c$ is assigned to $C$, node $b$ has only one possible pair ( $A$ ) among the remaining two nodes, and node $a$ will certainly be matched with $B$.

Consequently, the probability that node $a$ is assigned to node $B$ equals

$$
\begin{array}{r}
\frac{1}{3} \cdot \frac{1}{2}+\frac{1}{6} \cdot\left(\frac{1}{2} \cdot \frac{1}{2}+\frac{1}{2} \cdot 1\right)+\frac{1}{6} \cdot\left(\frac{1}{3} \cdot 1+\frac{1}{3} \cdot 0+\frac{1}{3} \cdot 1\right)+\frac{1}{6} \cdot\left(\frac{1}{2} \cdot \frac{1}{2}+\frac{1}{2} \cdot 1\right)+ \\
+\frac{1}{6} \cdot\left(\frac{1}{3} \cdot 1+\frac{1}{3} \cdot 0+\frac{1}{3} \cdot 1\right)=\frac{1}{6}+\frac{1}{8}+\frac{1}{9}+\frac{1}{8}+\frac{1}{9}=\frac{23}{36}
\end{array}
$$

Skip mechanism: Six cases will be distinguished with respect to the draw order of the nodes in $U$, each of them having a chance of $1 / 6$ to occur:

- Node $a$ is drawn first and node $b$ is drawn second: Node $B$ will be assigned to node $a$ if (a) node $B$ is drawn first from $V$; or (b) node $A$ is drawn first and node $B$ is drawn second from $V$ (because node $A$ "skips" node $a$ ). This has a probability of $1 / 2$ because the nodes in $V$ have $3 !=6$ permutations.
- Node $a$ is drawn first and node $b$ is drawn third: Node $B$ will be assigned to node $a$ if (a) node $B$ is drawn first from $V$; or (b) node $A$ is drawn first (when node $A$ "skips" node $a$ ).

This has a probability of $2 / 3$.

- Node $a$ is drawn second and node $b$ is drawn first: Node $B$ will be assigned to node $a$ if (a) node $B$ is drawn first from $V$ (because $B$ cannot matched with $b$ ); or (b) node $B$ is drawn second from $V$; or (c) node $C$ is drawn first and node $B$ is drawn third from $V$ (when node $A$ "skips" node $a$ and is assigned to node $c$ ). This has a probability of $5 / 6$ since only the permutation $(A, C, B)$ is not appropriate.
- Node $a$ is drawn second and node $b$ is drawn third: Node $B$ will be assigned to node $a$ if (a) node $B$ is drawn second from $V$; or (b) node $B$ is drawn third from $V$ (when the node drawn second from $V$ "skips" node $a$ ).

This has a probability of $2 / 3$.

- Node $a$ is drawn third and node $b$ is drawn first: Node $B$ will be assigned to node $a$ if (a) node $B$ is drawn second and node $A$ is drawn third from $V$ (when node $B$ "skips" node $c$ ); or (b) node $B$ is drawn third from $V$.

This has a probability of $1 / 2$.

- Node $a$ is drawn third and node $b$ is drawn second: Node $B$ will be assigned to node $a$ if (a) node $B$ is drawn second from $V$ (when node $B$ "skips" node $b$ ); or (b) node $B$ is drawn third from $V$.

This has a probability of $2 / 3$.

Table 2: Assignment matrices for the balanced bipartite graph with six nodes in Figure 4

(a) Uniform mechanism: Probabilities for all pairs of nodes

|  | A | B | C |
| :---: | :---: | :---: | :---: |
| a | $2 / 3$ | 0 | $1 / 3$ |
| b | 0 | $2 / 3$ | $1 / 3$ |
| c | $1 / 3$ | $1 / 3$ | $1 / 3$ |

(b) Drop and Skip mechanisms: Probabilities for all pairs of nodes

|  | A | B | C |
| :---: | :---: | :---: | :---: |
| a | $23 / 36$ | 0 | $13 / 36$ |
| b | 0 | $23 / 36$ | $13 / 36$ |
| c | $13 / 36$ | $13 / 36$ | $5 / 18$ |

Consequently, the probability that node $a$ is assigned to node $B$ equals

$$
\frac{1}{6} \cdot\left(\frac{1}{2}+\frac{2}{3}+\frac{5}{6}+\frac{2}{3}+\frac{1}{2}+\frac{2}{3}\right)=\frac{1}{6} \cdot \frac{23}{6}=\frac{23}{36}
$$

The Standard and Reversed forms of the Drop and Skip mechanisms coincide since the sets $U$ and $V$ are exchangeable in the bipartite graph shown in Figure 4.

Example 3. The assignment matrices for the graph shown in Figure 4 are given in Table 2. Therefore,

$$
A F D=100 \cdot\left(2 \cdot\left|\frac{2}{3}-\frac{23}{36}\right|+4 \cdot\left|\frac{1}{3}-\frac{13}{36}\right|+\left|\frac{1}{3}-\frac{5}{18}\right|\right) \cdot \frac{1}{7}=\frac{100}{7} \cdot \frac{8}{36}=3 \frac{11}{63}
$$

The maximal distortion occurs for nodes $c$ and $C$ :

$$
M F D=100 \cdot\left|\frac{1}{3}-\frac{5}{18}\right|=5 \frac{5}{9}
$$

Section 5.6 will present a graph corresponding to a possible UEFA Champions League season $(n=8)$, for which maximal fairness distortion exceeds the value derived in Example 3.

Although Proposition 1 is mainly a theoretical result, it can have practical relevance. For example, the play-offs of the 2024 UEFA European Championship qualifying tournament determine the last three national teams that can play in the European Championship. While the play-offs contain three independent paths with four participants each, an alternative structure could be to organise two knockout rounds with pairing constraints. Then the assignment in the second knockout round may be given in Figure 4, when all the four draw mechanisms have the same level of unfairness.

### 5.2 The case of eight nodes

Figure 5 presents unfairness for balanced bipartite graphs with eight nodes such that no node could have the same type as its pair: Figure 5.a if the pair constraints are effective (graphs in Figure 1), while Figure 5.b if there are only type constraints (graphs in Figure 2).
(a) Graphs with pair constraints $\left(G_{1}-G_{31}\right.$, Figure 1)

Absolute distortion AFD (\%)

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-16.jpg?height=765&width=1545&top_left_y=383&top_left_x=244)

Maximal distortion MFD (\%)

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-16.jpg?height=751&width=745&top_left_y=390&top_left_x=1038)

(b) Graphs without pair constraints $\left(H_{1}-H_{31}\right.$, Figure 2)

Absolute distortion AFD (\%)

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-16.jpg?height=754&width=763&top_left_y=1316&top_left_x=241)

Maximal distortion MFD (\%)

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-16.jpg?height=754&width=756&top_left_y=1316&top_left_x=1027)

- Standard order $\quad \times$ Reversed order $\triangle$ Both orders

Figure 5: Fairness distortions of the Drop and Skip mechanisms for balanced bipartite graphs with eight nodes

In the presence of pair constraints, both the Drop and Skip mechanisms are fair for 20 graphs and unfair for seven graphs $\left(G_{2}, G_{4}, G_{5}, G_{8}, G_{11}, G_{13}, G_{20}\right)$. The absolute and maximal differences are quite high, the probability of matching two nodes can differ by at least five percentage points for all these seven graphs. The ranking of the graphs by the two measures is different, the worst case is $G_{4}$ for $A F D$ but $G_{2}$ for $M F D$.

Result 1. For a balanced bipartite graph with eight nodes, pair and type constraints such
that pair and type constraints cannot coincide:

- The two versions (Standard and Reversed) of the Drop and Skip mechanisms, respectively, coincide;
- The Skip mechanism dominates the Drop mechanism as it is less distorted for graph $G_{2}$.

If pair constraints are removed, then both the Drop and Skip mechanisms are fair for 14 graphs and unfair for the remaining six graphs $\left(H_{3-5}, H_{6-8}, H_{12-14}, H_{15-16}, H_{18-20}\right.$, $H_{21-22}$ ). Since the Drop mechanism is less unfair for graph $H_{18-20}$ and the Skip mechanism is less unfair for graph $H_{6-8}$, neither of them is preferred to the other. However, the Reversed Drop mechanism is fairer than the Standard Drop mechanism. The absolute and maximal distortions are generally lower compared to the graphs with pair constraints.

Result 2. For a balanced bipartite graph with eight nodes and type constraints such that no node has the same type as its pair, the Reversed Drop mechanism is fairer than the Standard Drop mechanism according to both measures AFD and MFD due to graph $H_{12-14}$.

In contrast to Result 1, the Reversed Drop mechanism does not dominate the Standard Drop mechanism on the set of bipartite graphs described in Result 2 as it is more distorted for some pairs of nodes.

There is no analogous relation for the Skip mechanism: the Reversed Skip mechanism is less unfair for graph $H_{12-14}$ but it is worse for graph $H_{15-16}$.

### 5.3 Increasing the number of nodes

In order to get more insight into the draw mechanisms, Figures 6 and 7 uncover their unfairness if one pair and two pairs of nodes are added (without further type constraints), respectively, to the previous graphs with $n=4$.

Under pair constraints, the Drop and Skip mechanisms are fair for six graphs if $n=5$ but only for two graphs if $n=6$. Neither the Drop nor the Skip mechanism is better than the other. The draw order has a surprising effect: for graph $G_{11}$ and $M F D$, the Reversed Drop mechanism has a higher unfairness by $2.2 \%$ compared to the Standard version if $n=5$, but a lower unfairness by $6 \%$ if $n=6$. Thus, merely adding a pair of nodes without type constraints can change the optimal draw order. Analogously, for graph $G_{26}$, the Reversed Skip mechanism is less fair according to both measures than the Standard Skip mechanism if $n=5$, but their order is changed if $n=6$. Maximal unfairness exceeds 8(\%) for graph $G_{22}$ if $n=5$, which indicates a quite serious problem. However, absolute distortions are not worse than in Example 1.

Adding a pair of nodes without type constraints does not necessarily improve fairness. For example, the unfairness of our mechanisms for graph $G_{18}$ is at least quintupled if $n=6$ compared to $n=5$, although the number of valid assignments increases from 10 to 93 .

For the graphs without pair constraints (Figures 6.b and 7.b), the Drop and Skip mechanisms are fair for five and unfair for the remaining 15 graphs. Among the latter, the Reversed Drop mechanism is usually better than the Standard version, for instance, its average fairness distortion is the same for nine graphs and is lower for six graphs. However, in the case of graph $H_{26}, M F D$ favours the Standard Drop mechanism for both $n=5$ and $n=6$. Similarly, the Reversed Skip mechanism is usually less unfair than the Standard Skip mechanism.

Regarding the Drop and Skip draw mechanisms, we have a stronger finding.
(a) Graphs with pair constraints ( $G_{1}-G_{31}$ plus one pair of nodes, Figure 1)

Absolute distortion $A F D(\%)$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-18.jpg?height=748&width=757&top_left_y=391&top_left_x=250)

Maximal distortion MFD (\%)

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-18.jpg?height=745&width=760&top_left_y=390&top_left_x=1019)

- Standard order $\quad \times$ Reversed order $\quad \Delta$ Both orders

(b) Graphs without pair constraints ( $H_{1}-H_{31}$ plus one pair of nodes, Figure 2)

Absolute distortion $A F D(\%)$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-18.jpg?height=745&width=743&top_left_y=1398&top_left_x=248)

Maximal distortion $M F D(\%)$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-18.jpg?height=751&width=762&top_left_y=1395&top_left_x=1018)

- Standard order $\quad \times$ Reversed order $\quad \Delta$ Both orders

Figure 6: Fairness distortions of the Drop and Skip mechanisms for selected balanced bipartite graphs with 10 nodes

Result 3. For a balanced bipartite graph with 10 or 12 nodes, and type constraints affecting at most four pairs of nodes such that no node has the same type as its pair, the Reversed (Standard) Drop mechanism is fairer than the Reversed (Standard) Skip mechanism according to both measures AFD and MFD.
(a) Graphs with pair constraints $\left(G_{1}-G_{31}\right.$ plus two pairs of nodes, Figure 1)

Absolute distortion AFD (\%)

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-19.jpg?height=751&width=782&top_left_y=387&top_left_x=246)

Maximal distortion MFD (\%)

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-19.jpg?height=748&width=743&top_left_y=391&top_left_x=1065)

- Standard order $\quad \times$ Reversed order $\quad \Delta$ Both orders

(b) Graphs without pair constraints ( $H_{1}-H_{31}$ plus two pairs of nodes, Figure 2)

Absolute distortion AFD (\%)

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-19.jpg?height=754&width=786&top_left_y=1393&top_left_x=241)

Maximal distortion MFD (\%)

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-19.jpg?height=751&width=743&top_left_y=1395&top_left_x=1065)

- Standard order $\quad \times$ Reversed order $\quad \Delta$ Both orders

Figure 7: Fairness distortions of the Drop and Skip mechanisms for selected balanced bipartite graphs with 12 nodes

In the examples without pair constraints, having an additional unconstrained pair of nodes generally reduces the level of unfairness, except if the draw mechanisms are fair only due to the symmetricity of the underlying graph such as $H_{9-10}$. However, this cannot explain the higher maximal fairness distortion of the Standard Skip mechanism for graph $H_{15-16}$ if $n$ is increased from 4 to 5 .

Table 3: The probability of the match Bayern München versus Liverpool in the 2022/23 UEFA Champions League Round of 16

| Mechanism | Probability | Bias |
| :--- | :---: | :---: |
| Perfect | $39.86 \%$ | - |
| Standard Drop | $37.13 \%$ | $2.73 \%$ |
| Reversed Drop | $36.91 \%$ | $2.95 \%$ |
| Standard Skip | $35.46 \%$ | $4.40 \%$ |
| Reversed Skip | $35.42 \%$ | $4.44 \%$ |

### 5.4 Sufficient conditions for fairness

The calculations in Sections 5.2 and 5.3 allow us to formulate sufficient conditions for the fairness of our draw procedures.

Result 4. The Drop and the Skip mechanisms are fair if one of the following conditions holds:

- There is only one valid matching (graphs $G_{18}, G_{19}, G_{21}, G_{23}-G_{27}$ if $n=4$ );
- There are no type constraints (graphs $G_{1}$ and $H_{1}$ );
- There are no pair constraints and the type constraints affect only one node on one side of the bipartite graph (graphs $H_{2}, H_{11}, H_{28}$ );
- The balanced bipartite graph can be decomposed into two unconnected balanced bipartite graphs such that the complement of the first subgraph is complete and the draw mechanism is fair for the second subgraph (graphs $G_{3}$ and $H_{23}$ ).


### 5.5 Graphs given by the UEFA Champions League Round of 16

Figure 8 compares the distortions of the Drop and Skip mechanisms for the 20 graphs given by the historical UEFA Champions League seasons. The officially used Drop mechanism is fairer in all cases according to $A F D$. This robust result almost holds with respect to maximal fairness distortion, too, except for the Standard Drop and Standard Skip mechanisms in the 2014/15 season (where the Reversed Drop is the best option).

Unsurprisingly, the level of unfairness strongly depends on the set of constraints, $A F D$ varies between $0.051(\%)$ and $0.363(\%)$ for the Drop mechanism and can exceed $0.5(\%)$ for the Skip mechanism. The results are even more different for MFD, the two disadvantageous outliers are the 2017/18 and the 2022/23 seasons. As an illustration, the probability of a match between Bayern München and Liverpool in the 2022/23 season is presented in Table 3.

Nonetheless, the performance of the Drop and Skip mechanisms is relatively similar, it is not possible to achieve a fundamental improvement by any draw procedure if the constraints have an unfavourable structure. This finding sheds new light on Boczoń and Wilson (2023, Result 2): they would probably have concluded that each of our four transparent mechanisms comes quantitatively close to a constrained-best.

The situation is more obvious after removing the pair constraints (Figure 8.b), when the superiority of the Drop mechanism becomes undeniable. Both procedures would have been fair in 2003/04 due to the third condition of Result 4. However, the Drop mechanism
(a) With pair constraints

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-21.jpg?height=836&width=1600&top_left_y=313&top_left_x=228)

Absolute distortion AFD (\%)

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-21.jpg?height=754&width=785&top_left_y=385&top_left_x=247)

Maximal distortion $M F D(\%)$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-21.jpg?height=757&width=748&top_left_y=381&top_left_x=1065)

-Standard order $\quad \times$ Reversed order

(b) Without pair constraints

Absolute distortion $A F D(\%)$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-21.jpg?height=757&width=803&top_left_y=1386&top_left_x=244)

Maximal distortion $M F D(\%)$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-21.jpg?height=759&width=748&top_left_y=1385&top_left_x=1065)

- Standard order $\quad \times$ Reversed order

Figure 8: Fairness distortions of the Drop and Skip mechanisms, graphs corresponding to the UEFA Champions League Round of 16 from 2003/04 to 2022/23

can decrease the average fairness distortion of the Skip mechanism from about 0.445(\%) to below $0.2(\%)$ for the graph corresponding to the 2013/14 season, which provides an interesting example because the distortions are much lower- $0.57(\%)$ for the Drop and 1.63(\%) for the Skip - with the eight additional pair constraints. On the other hand, the worst maximal fairness distortions are again associated with the 2017/18 and the 2022/23
seasons as in Figure 8.a.

Result 5. The Drop mechanism is (almost) always better than the Skip mechanism for the graphs corresponding to the historical draws of the UEFA Champions League Round of 16.

Result 5 can be illustrated by the fact that the cumulated MFD (AFD) over the 20 seasons is smaller by $40.7 \%$ (39.8\%) under the Standard Drop mechanism than under the Standard Skip mechanism.

Figure 9 focuses on the effect of the draw order. As expected, the difference between the Standard and Reversed versions is more moderated than the difference between the Drop and Skip mechanisms. The Skip mechanism is almost insensitive to the draw order, and removing the pair constraints also diminishes the role of draw order.

However, in the presence of draw constraints, the Reversed Drop mechanism seems to be better than the Standard Drop. This is quite remarkable for the 2017/18 season, where the Reversed form decreases both measures of unfairness by approximately $30 \%$. The issue will be further investigated in Section 5.6.

Note that both the Standard and the Reversed Drop mechanisms have the same chance to be fairer than the other version from a purely mathematical point of view: the assumption in Section 4.1 that the degree sequence of the set $U$ is not lexicographically smaller is arbitrary. In other words, if the Reversed Drop is preferred for a balanced bipartite graph but sets $U$ and $V$ are exchanged, then the Standard Drop becomes preferred.

However, this nice symmetry disappears in the UEFA Champions League, where the two sides are given by the group winners and the runner-up, and the type constraints are implied by the national associations of the clubs. According to Table 4, six leagues have had more than one club qualified for the Round of 16 in at least one year between 2003/04 and 2022/23. Due to England and, to a lesser extent, Spain, there are usually more group winners in these countries than runners-up. Consequently, the set $U$ is more likely to correspond to the runners-up - when, on the basis of Figure 9.a, the Reversed Drop procedure is better, that is, the draw needs to start on the side of the runners-up.

Result 6. The official UEFA mechanism is expected to be fairer than its reversed variant for the graphs corresponding to the historical draws of the UEFA Champions League Round of 16 .

Result 6 can be illustrated by the fact that the cumulated MFD (AFD) over the 20 seasons is smaller by $11.1 \%$ (3.3\%) under the currently used mechanism than under its reversed form.

In a sense, Results 5 and 6 are our most important findings: they uncover that UEFA has chosen the best randomisation procedure among the four field-proven alternatives.

### 5.6 Graphs with highly concentrated constraints

The Reversed Drop mechanism is the most unfair among the historical Champions League seasons in 2017/18, when the difference between the Standard and Reversed forms is the highest, too. The associated bipartite graph is $I_{1}$ in Figure 3. We have created seven further graphs having a similar structure, which are also shown in Figure 3. All of them contain at least one node with four (except for $I_{3}$ ) or two nodes with three $\left(I_{3}\right)$ type constraints.

As can be seen in Figure 10, the draw mechanisms are relatively unfair for these instances. The maximal error is above 4 for the three graphs $I_{2}, I_{4}$, and $I_{5}$. In particular,
(a) With pair constraints
![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-23.jpg?height=932&width=1600&top_left_y=316&top_left_x=228)

Maximal distortion $M F D(\%)$

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-23.jpg?height=759&width=743&top_left_y=380&top_left_x=1065)

-Drop mechanism

×Skip mechanism

(b) Without pair constraints

![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-23.jpg?height=922&width=1585&top_left_y=1321&top_left_x=241)

Absolute distortion AFD (\%)

Maximal distortion $M F D(\%)$
![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-23.jpg?height=766&width=1562&top_left_y=1378&top_left_x=246)

-Drop mechanism $\quad$ Skip mechanism

Figure 9: Fairness distortions and the role of draw order, graphs corresponding to the UEFA Champions League Round of 16 from 2003/04 to 2022/23

the probability of matching the two nodes with five restrictions, one type and four association constraints, is $61.76 \%$ under the Uniform procedure but only $53.35 \%$ (50.9\%) according to the Drop (Skip) mechanism. The two variants Standard and Reversed do not differ since the sets $U$ and $V$ are exchangeable. The implied MFD of 8.4(\%) is worrying since the nodes with five restrictions have three possible nodes to be assigned to them,

Table 4: Associations with more than one team in the UEFA Champions League Round of 16

| Season | England | France |  |  |  | Germany |  |  |  | Italy | Portugal |  |  | Spain |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  | 1 | 2 | $\Delta$ | 1 | 2 | $\Delta$ | 1 | 2 | $\Delta$ | 1 | 2 | $\Delta$ | 1 | 2 | $\Delta$ | 1 | 2 | $\Delta$ |
|  | 3 | 0 | 3 | 2 | 0 | 2 | 0 | 2 | -2 | 2 | 0 | 2 | 0 | 1 | -1 | 1 | 3 | -2 |
| $2004 / 05$ | 2 | 2 | 0 | 2 | 0 | 2 | 1 | 2 | -1 | 3 | 0 | 3 | 0 | 1 | -1 | 0 | 2 | -2 |
| $2005 / 06$ | $2^{*}$ | 1 | $0^{*}$ | 1 | 0 | 1 | 0 | 2 | -2 | 3 | 0 | 3 | 0 | 1 | -1 | 2 | 1 | 1 |
| $2006 / 07$ | 4 | 0 | 4 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 2 | -1 | 0 | 1 | -1 | 1 | 2 | -1 |
| $2007 / 08$ | 2 | 2 | 0 | 0 | 1 | -1 | 0 | 1 | -1 | 2 | 1 | 1 | 1 | 0 | 1 | 3 | 0 | 3 |
| $2008 / 09$ | 2 | 2 | 0 | 0 | 1 | -1 | 1 | 0 | 1 | 2 | 1 | 1 | 1 | 1 | 0 | 1 | 3 | -2 |
| $2009 / 10$ | 3 | 0 | 3 | 1 | 1 | 0 | 0 | 2 | -2 | 1 | 2 | -1 | 0 | 1 | -1 | 3 | 0 | 3 |
| $2010 / 11$ | 3 | 1 | 2 | 0 | 2 | -2 | 2 | 0 | 2 | 0 | 3 | -3 | 0 | 0 | 0 | 2 | 1 | 1 |
| $2011 / 12$ | 2 | 0 | 2 | 0 | 2 | -2 | 1 | 1 | 0 | 1 | 2 | -1 | 1 | 0 | 1 | 2 | 0 | 2 |
| $2012 / 13$ | 1 | 1 | 0 | 1 | 0 | 1 | 3 | 0 | 3 | 1 | 1 | 0 | 0 | 1 | -1 | 2 | 2 | 0 |
| $2013 / 14$ | 2 | 2 | 0 | 1 | 0 | 1 | 2 | 2 | 0 | 0 | 1 | -1 | 0 | 0 | 0 | 3 | 0 | 3 |
| $2014 / 15$ | 1 | 2 | -1 | 1 | 1 | 0 | 2 | 2 | 0 | 0 | 1 | -1 | 1 | 0 | 1 | 3 | 0 | 3 |
| $2015 / 16$ | 2 | 1 | 1 | 0 | 1 | -1 | 2 | 0 | 2 | 0 | 2 | -2 | 0 | 1 | -1 | 3 | 0 | 3 |
| $2016 / 17$ | 2 | 1 | 1 | 1 | 1 | 0 | 1 | 2 | -1 | 2 | 0 | 2 | 0 | 2 | -2 | 2 | 2 | 0 |
| $2017 / 18$ | 4 | 1 | 3 | 1 | 0 | 1 | 0 | 1 | -1 | 1 | 1 | 0 | 0 | 1 | -1 | 1 | 2 | -1 |
| $2018 / 19$ | 1 | 3 | -2 | 1 | 1 | 0 | 2 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 2 | 1 | 1 |
| $2019 / 20$ | 2 | 2 | 0 | 1 | 1 | 0 | 2 | 1 | 1 | 1 | 2 | -1 | 0 | 0 | 0 | 2 | 2 | 0 |
| $2020 / 21$ | 3 | 0 | 3 | 1 | 0 | 1 | 2 | 2 | 0 | 1 | 2 | -1 | 0 | 1 | -1 | 1 | 3 | -2 |
| $2021 / 22$ | 3 | 1 | 2 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 2 | -2 | 1 | 2 | -1 |
| $2022 / 23$ | 3 | 1 | 2 | 0 | 1 | -1 | 1 | 3 | -2 | 1 | 2 | -1 | 2 | 0 | 2 | 1 | 0 | 1 |
| Average | 1.15 |  | 0.05 |  |  | 0 |  | -0.05 |  | -0.35 |  | 0.5 |  |  |  |  |  |  |

Notes: Column 1 shows the number of group winners; Column 2 shows the number of runners-up; Column $\Delta$ shows the difference between the number of group winners and runners-up.

The last row shows the average of Column $\Delta$ for each country.

The number of exclusions for any national association equals the number of group winners times the number of runners-up. The only exception is the 2005/06 season when Chelsea and Liverpool both qualified from Group G, thus, the number of constraints due to England is one rather than two. In addition, a Russian group winner could not have played against a Ukrainian runner-up in 2015/16.

thus, every reasonable assignment rule should match these two nodes with at least a probability of $1 / 3$. Consequently, a naïve upper bound of maximal fairness distortion is $61.76-33.33 \approx 28.4(\%)$, and the Drop mechanism is not able to reduce this value by more than $71 \%$. Furthermore, the value of MFD exceeds the worst maximal fairness distortion for all graphs considered in Section 5.2 (see Figure 5), that is, the Round of 16 draw can be less fair than a potential draw of the quarterfinals under the same rules.

Result 7. The Drop mechanism does not come quantitatively close to the best possible lottery for certain graphs representing possible UEFA Champions League seasons.

Result 7 somewhat contradicts Boczoń and Wilson (2023, Result 3), which states that the Drop procedure continues to be close to a constrained-best if (i) the number of constraints; (ii) the likely location of the constraints in the graph; and (iii) the number of nodes in the graph is shifted.

Figure 10 reinforces the message of Section 5.5. First, the Drop mechanism is clearly fairer compared to the Skip mechanism, it has a lower absolute fairness distortion by about
![](https://cdn.mathpix.com/cropped/2024_04_26_e49a3824be5e46326561g-25.jpg?height=918&width=1600&top_left_y=240&top_left_x=228)

-Drop mechanism

×Skip mechanism

Figure 10: Fairness distortions of the UEFA mechanisms for the graphs in Figure 3

30-40\% for our balanced bipartite graphs with 16 nodes. In addition, the draw order has a more moderated impact on the Skip mechanism. Second, the two versions of the Drop mechanism can substantially differ from each other, the distortion of the Reversed Drop mechanism is smaller by at least $17 \%$ for the three "unfavourable" graphs of $I_{1}, I_{2}$, and $I_{5}$. Furthermore, the MFD of the Standard Drop mechanism is above 3.2(\%) for graph $I_{6}$ but remains below 2(\%) under the Reversed Drop, implying a decrease of over $40 \%$.

Result 8. The draw order of the Drop mechanism has sometimes a non-negligible effect on the level of unfairness.

Result 8 disproves Klößner and Becker (2013, Footnote 19), which states that the probabilities of the UEFA procedure would change slightly if group winners were drawn first and only then matched with suitable runners-up.

## 6 Conclusions

Our paper has compared the basic randomisation procedures used in sports competitions to divide the teams into groups in the presence of draw constraints. Since uniform distribution over all valid assignments should be sacrificed for the sake of transparency, it is crucial to know what variant (Standard or Reversed) of which mechanism (Drop or Skip) performs the best in a given setting. Therefore, we have evaluated their unfairness for some sets of balanced bipartite graphs with two kinds of restrictions. Our results reveal that the UEFA Champions League Round of 16 draw has adopted the least unfair transparent field-proven algorithm.

There remains a wide scope for future research. First, the reason for the difference between the Drop and Skip mechanisms has not been fully explored, although the difficulty of the problem has hopefully been highlighted. Second, these draw procedures are
worth analysing in further settings. The advantage of the Drop mechanism in bipartite graphs suggests that it might be a competitive option for the FIFA World Cup drawhowever, having groups with more than two teams increases the complexity of the potential constraints. Last but not least, in contrast to Boczoń and Wilson (2023), we think tournament organisers should continue the quest for fairer but transparent lotteries since all previous proposals (Guyon, 2014; Klößner and Becker, 2013; Roberts and Rosenthal, 2023) have different weaknesses.

## Acknowledgements

This paper could not have been written without my father (also called László Csató), who has helped to code the simulations in Python.

Five anonymous reviewers and Ilia Tsetlin have provided valuable comments and suggestions on earlier drafts.

The research was supported by the National Research, Development and Innovation Office under Grant FK 145838.

## References

Abdulkadiroğlu, A. and Sönmez, T. (1998). Random serial dictatorship and the core from random endowments in house allocation problems. Econometrica, 66(3):689-701.

Boczoń, M. and Wilson, A. J. (2023). Goals, constraints, and transparently fair assignments: A field study of randomization design in the UEFA Champions League. Management Science, 69(6):3474-3491.

Bogomolnaia, A. and Moulin, H. (2001). A new solution to the random assignment problem. Journal of Economic Theory, 100(2):295-328.

Budish, E., Che, Y.-K., Kojima, F., and Milgrom, P. (2013). Designing random allocation mechanisms: Theory and applications. American Economic Review, 103(2):585-623.

Csató, L. (2022a). The effects of draw restrictions on knockout tournaments. Journal of Quantitative Analysis in Sports, 18(4):227-239.

Csató, L. (2022b). Quantifying incentive (in)compatibility: A case study from sports. European Journal of Operational Research, 302(2):717-726.

Csató, L. (2024). Group draw for the FIFA World Cup: Is uniform distribution really necessary? Manuscript. DOI: 10.48550/arXiv.2103.11353.

Csató, L., Molontay, R., and Pintér, J. (2024). Tournament schedules and incentives in a double round-robin tournament with four teams. International Transactions in Operational Research, 31(3):1486-1514.

FIBA (2019). Procedure for FIBA Basketball World Cup 2019 Draw. 15 March. https://www.fiba.basketball/basketballworldcup/2019/news/procedure-forfiba-basketball-world-cup-2019-draw.

FIBA (2023). The FIBA Basketball World Cup 2023 draw principles explained. 21 April. https://www.fiba.basketball/basketballworldcup/2023/news/the-fibabasketball-world-cup-2023-draw-principles-explained.

FIFA (2017). Close-up on Final Draw procedures. 27 November. https: //web.archive.org/web/20171127150059/http://www.fifa.com/worldcup/news/ $\mathrm{y}=2017 / \mathrm{m}=11 /$ news=close-up-on-final-draw-procedures-2921440. html.

FIFA (2022). Draw procedures. FIFA World Cup Qatar 2022 ${ }^{T M}$. https://digitalhub. fifa.com/m/2ef762dcf5f577c6/original/Portrait-Master-Template.pdf.

Guyon, J. (2014). Rethinking the FIFA World Cup ${ }^{\text {TM }}$ final draw. Manuscript. DOI: $10.2139 /$ ssrn. 2424376 .

Guyon, J. (2015). Rethinking the FIFA World $\mathrm{Cup}^{\mathrm{TM}}$ final draw. Journal of Quantitative Analysis in Sports, 11(3):169-182.

Guyon, J. (2018). Pourquoi la Coupe du monde est plus équitable cette année. The Conversation. 13 June. https://theconversation.com/pourquoi-la-coupe-du-mondeest-plus-equitable-cette-annee-97948.

Guyon, J. (2021). Ligue des champions : fallait-il annuler complètement le résultat du premier tirage? Le Monde. 14 December. https://www.lemonde.fr/sport/ article/2021/12/14/ligue-des-champions-fallait-il-annuler-completementle-resultat-du-premier-tirage_6106012_3242.html.

Guyon, J. (2022). "Choose your opponent": A new knockout design for hybrid tournaments. Journal of Sports Analytics, 8(1):9-29.

Guyon, J. and Meunier, F. (2023). UEFA draws: probability calculator. 13 December. https://julienguyon.github.io/UEFA-draws/ExactProbabilities_ ChampionsLeague_Round0f16_text_website-1.pdf.

Hall, N. G. and Liu, Z. (2024). Opponent choice in tournaments: winning and shirking. Journal of Quantitative Analysis in Sports, in press. DOI: 10.1515/jqas-2023-0030.

Hopcroft, J. E. and Karp, R. M. (1973). An $n^{5 / 2}$ algorithm for maximum matchings in bipartite graphs. SIAM Journal on Computing, 2(4):225-231.

Hylland, A. and Zeckhauser, R. (1979). The efficient allocation of individuals to positions. Journal of Political Economy, 87(2):293-314.

Jones, M. C. (1990). The World Cup draw's flaws. The Mathematical Gazette, 74(470):335338 .

Kiesl, H. (2013). Match me if you can. Mathematische Gedanken zur Champions-LeagueAchtelfinalauslosung. Mitteilungen der Deutschen Mathematiker-Vereinigung, 21(2):8488.

Klößner, S. and Becker, M. (2013). Odd odds: The UEFA Champions League Round of 16 draw. Journal of Quantitative Analysis in Sports, 9(3):249-270.

Laliena, P. and López, F. J. (2019). Fair draws for group rounds in sport tournaments. International Transactions in Operational Research, 26(2):439-457.

Lunander, A. and Karlsson, N. (2023). Choosing opponents in skiing sprint elimination tournaments. Journal of Quantitative Analysis in Sports, 19(3):205-221.

Rathgeber, A. and Rathgeber, H. (2007). Why Germany was supposed to be drawn in the group of death and why it escaped. Chance, 20(2):22-24.

Roberts, G. O. and Rosenthal, J. S. (2023). Football group draw probabilities and corrections. Canadian Journal of Statistics, in press. DOI: 10.1002/cjs.11798.

Scarf, P., Yusof, M. M., and Bilbao, M. (2009). A numerical study of designs for sporting contests. European Journal of Operational Research, 198(1):190-198.

Sziklai, B. R., Biró, P., and Csató, L. (2022). The efficacy of tournament designs. Computers 63 Operations Research, 144:105821.

Tanimoto, S. L., Itai, A., and Rodeh, M. (1978). Some matching problems for bipartite graphs. Journal of the ACM, 25(4):517-525.

UEFA (2004). Regulations of the UEFA Cup 2004/05. https://web.archive.org/web/ 20050405073702/http://www.uefa.com/newsfiles/19070.pdf.

UEFA (2009). Regulations of the UEFA Europa League 2009/10. https://web.archive. org/web/20090823205941/https://www.uefa.com/MultimediaFiles/Download/ Regulations/competitions/UEFACup/84/52/89/845289_DOWNLOAD .pdf.

UEFA (2014). UEFA EURO 2016 qualifying draw procedure. 23 February. https://www.uefa.com/MultimediaFiles/Download/competitions/Draws/02/ 04/64/31/2046431_DOWNLOAD.pdf.

UEFA (2015). 2018 FIFA World Cup Russia ${ }^{\text {TM }}$ Preliminary Competition Format \& Draw Procedures European Zone. https://web.archive.org/web/20150724213005/http: //resources.fifa.com/mm/document/tournament/preliminarydraw/02/66/71/27/ europe_drawprocedures_neutral.pdf.

UEFA (2018a). UEFA EURO 2020 qualifying draw. 2 December. https://www.uefa. com/european-qualifiers/news/newsid=2573388. html.

UEFA (2018b). UEFA Nations League 2018/19 - League phase draw procedure. https://www.uefa.com/MultimediaFiles/Download/uefaorg/General/02/52/ 51/09/2525109_DOWNLOAD.pdf.

UEFA (2020a). FIFA World Cup 2022 qualifying draw procedure. https: //www.uefa.com/MultimediaFiles/Download/competitions/WorldCup/02/64/ 22/19/2642219_DOWNLOAD.pdf.

UEFA (2020b). UEFA Nations League 2020/21 - league phase draw procedure. https://www.uefa.com/MultimediaFiles/Download/competitions/General/ 02/63/57/88/2635788_DOWNLOAD. pdf.

UEFA (2021a). Regulations of the UEFA Europa Conference League 2021-24 Cycle. 2021/22 Season. https://web.archive.org/web/20220208043024/https://documents.uefa. com/r/Regulations-of-the-UEFA-Europa-Conference-League-2021/22-Online.

UEFA (2021b). Regulations of the UEFA Europa League 2021-24 Cycle. 2021/22 Season. https://web.archive.org/web/20220207235133/https://documents.uefa. com/r/Regulations-of-the-UEFA-Europa-League-2021/22-Online.

UEFA (2021c). UEFA Nations League 2022/23 - league phase draw procedure. https://editorial.uefa.com/resources/026f-13c241515097-67a9c87ed1b21000/unl_2022-23_league_phase_draw_procedure_en.pdf.

UEFA (2022). UEFA EURO 2024 Qualifying Draw Procedure. https: //editorial.uefa.com/resources/0279-1627b29793e1-ffbe5a3c77a1-1000/ 08.01.00_euro_2024_qualifying_draw_procedure_en_20220920115210.pdf.

UEFA (2024). 2024/25 UEFA Nations League Draw Press Kit. https: //editorial.uefa.com/resources/028a-1a1e18631263-95c63cec8617-1000/ 202425_unl_qualifying.pdf.

Wallace, M. and Haigh, J. (2013). Football and marriage - and the UEFA draw. Significance, 10(2):47-48.


[^0]:    * E-mail:laszlo.csato@sztaki.hun-ren.hu

    ${ }^{1}$ Source: Budish et al. (2013, p. 585).

