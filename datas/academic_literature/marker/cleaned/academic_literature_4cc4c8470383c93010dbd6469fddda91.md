# Why Is Soccer So Popular: Understanding Underdog Achievement And Randomness In Team Ball Sports

L. N. Vicente T. N. Alleck T. Giovannelli R. Mitchell O. Remen April 11, 2024

## Abstract

In this paper, we examine team ball sports to investigate how the likelihood of weaker teams winning against stronger ones, referred to as underdog achievement, is influenced by inherent randomness factors that affect match outcomes in such sports. To address our research question, we collected data on match scores and computed corresponding team rankings from major international competitions for 12 popular team ball sports: basketball, cricket, field hockey, futsal, handball, ice hockey, lacrosse, roller hockey, rugby, soccer, volleyball, and water polo. Then, we developed an underdog achievement score to identify the sports with the highest occurrences of weaker teams prevailing over stronger ones, and we designed a randomness model consisting of factors that contribute to unexpected match outcomes within each sport. Our findings indicate that soccer is among the sports in which a weaker team is most likely to win. Through principal component analysis (PCA) and correlation analysis, we demonstrate that our randomness model can explain such a phenomenon, showing that the underdog achievement can be attributed to numerous factors that can randomly influence match outcomes.

## 1 Introduction

Team ball sports have been the subject of growing research over the past decade, and most of the papers are within the domain of sports medicine literature [15]. In our work, we do not focus on medicine applications. Instead, we aim to provide novel insights into team ball sports by determining which sports are more likely to see weaker teams win, referred to as underdog achievement, and which randomness factors contribute to such an outcome. Since certain teams consistently outperform others in all sports, it is clear that outcomes of matches are not purely random. The question of whether a team wins due to chance or their own skills has been discussed in non-scholarly books. For example, in [14], the authors claim that soccer, which is universally recognized as the world's most popular sport [4], is also the most random, and its inherent randomness is what makes soccer so popular. Similar conclusions were confirmed in the academic literature by [2], where the authors analyzed the English Football Association and four major North American professional sports leagues (MLB for baseball, NBA for basketball, arXiv:2404.06626v1 [stat.AP] 9 Apr 2024 NFL for American football, and NHL for hockey), finding that soccer is the sport with the most random outcomes. In general, the randomness element adds excitement and unpredictability, making a sport enjoyable to watch. However, one should also notice that excessive randomness can diminish interest, as viewers prefer a balance between unpredictability and skill [13].

A novel research question is whether a weak team is more likely to win than a strong one as a consequence of certain random and situational conditions. Such a question has recently emerged as a research focus and has been studied by [16], where the authors use data from the English Premier League to show that the influence of randomness on goals in soccer decreases as the match progresses. Such a decreasing trend was observed to be disadvantageous for weaker teams, as they rely more on randomness to score. The study in [16] also identifies variables of randomness that affect the outcome during a match and cannot be entirely attributed to skills. Examples of such variables include the degree of involvement of the defending team and the chances to score goals from outside the penalty area. Additionally, the analysis includes situational variables that may influence the outcome by affecting the motivation of players, such as match location and current score. We conclude our literature review with [12], where a Bayesian state-space model was proposed to study the randomness in match outcomes for four major North American professional sports leagues (once again, MLB, NBA, NFL, and NHL). Probability-based metrics derived from betting market data were used to quantify the influence of chance on the outcomes. Their findings indicate that the MLB and NHL exhibit the highest levels of randomness in match outcomes (and we found a similar result for ice hockey in our study). However, soccer was not included in their analysis.

Previous studies examining underdog achievement have focused on a limited range of team ball sports and have not systematically identified the randomness factors contributing to underdog victories. The ultimate goal of our paper is to investigate how the likelihood of weaker teams winning against stronger ones is influenced by inherent randomness factors in team ball sports. To achieve our goal, we selected major international competitions for 12 popular team ball sports: basketball, cricket, field hockey, futsal, handball, ice hockey∗, lacrosse, roller hockey, rugby, soccer, volleyball, and water polo. The official names of the competitions selected for each sport are included in Table 1. Note that such competitions are all men's events, for which more data is available. We notice that certain popular team ball sports, such as American football, baseball, and tennis, were not included in our analysis. This decision was made due to either the absence of international competitions for these sports or the smaller size of their teams compared to the sports considered in this paper (for instance, in tennis, teams consist of at most two players, whereas all the other sports discussed in our paper involve teams with much more than two players).

Our main contributions can be summarized as follows:
- We collected a vast amount of data containing information related to match scores, and we computed corresponding team rankings for each edition of the competitions in Table 1. This data represents valuable information for researchers in the field of sports analytics.

- We developed an underdog achievement score to determine the sports with the highest and lowest occurrences of weaker teams defeating stronger ones when focusing on a much broader range of team ball sports than the ones considered in the literature. In accordance with the limited existing literature (again, see [2, 14]), soccer is among the sports with the highest underdog achievement.

∗We include ice hockey among the team ball sports, even though it technically uses a puck.

- We designed a randomness model consisting of 14 factors that contribute to unexpected match outcomes within each sport, providing quantitative values for each of the factors.

- We performed principal component analysis (PCA) and correlation analysis to identify the randomness factors with the greatest impact on underdog achievement and demonstrate that our randomness model can explain underdog achievement.
Our paper is organized as follows. In Section 2, we detail our data collection process.

In Section 3, we develop an underdog achievement score and in Section 4, we present our randomness model. In Section 5, we perform PCA and correlation analysis to demonstrate how our randomness model can explain underdog achievement. In Section 6, we conclude our paper with some remarks and ideas for future work.

| Sport         | Competition                         |
|---------------|-------------------------------------|
| Basketball    | Summer Olympic Games                |
| Cricket       | ICC Men's Cricket World Cup         |
| Field Hockey  | Men's FIH Hockey World Cup          |
| Futsal        | FIFA Futsal World Cup               |
| Handball      | Summer Olympic Games                |
| Ice Hockey    | Winter Olympic Games                |
| Lacrosse      | World Lacrosse Men's World Cup      |
| Roller Hockey | World Skate Roller Hockey World Cup |
| Rugby         | Rugby World Cup                     |
| Soccer        | FIFA World Cup                      |
| Volleyball    | FIVB Volleyball Men's World Cup     |
| Water Polo    | FINA Men's Water Polo World Cup     |

Table 1: Major international competitions selected for the team ball sports included in our paper.

## 2 Data Collection: Match Scores And Team Rankings

To perform our analysis, for each sport, we collected real data on match scores and computed corresponding team rankings from all available editions of the major international sports competitions in Table 1. The complete table with the years of the editions of each competition is provided in Table 7 of Appendix A. To obtain match score data for each edition, we conducted web scraping of match information from Wikipedia pages. All this data was aggregated into a match score dataset, which contains information related to individual matches, including the names of the two opposing teams and their respective scores. Given the match score dataset, we then computed a team ranking for each edition. Finally, for each competition, we aggregated the team rankings across all the edition years included in Table 7 into a weighted team ranking.

Our code is publicly available on GitHub.†
We will now introduce some general notation that will allow us to formally describe the match score dataset, the team ranking for each edition, and the weighted team ranking. Denoting as S
†https://github.com/thaksheel/randomness-team-ball-sports.git

| S                            | Set of sports.                                                                                                                |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| E                            | Set of editions for the given competition.                                                                                    |
| Pe = {p1, p2, . . . , pNe }  | Set of all teams playing in edition e ∈ E.                                                                                    |
| Me ⊆ Pe × Pe                 | Set of matches in edition e ∈ E.                                                                                              |
| scoree ij (i), scoree ij (j) | Scores obtained by teams i and j when facing each other, where (i, j) ∈ Me.                                                   |
| De                           | Match score dataset for edition e ∈ E, as defined in (2.1).                                                                   |
| Re                           | Team ranking for edition e ∈ E, as defined in (2.2).                                                                          |
| E = (e1, e2, . . . , e|E|)   | Set of editions written as an ordered list of elements, where e1 is the earliest edition and e|E| is the most recent edition. |
| P⩽e                          | Union of the sets of teams up to edition e ∈ E, as defined in (2.3).                                                          |
| N⩽e                          | Cardinality of the set P⩽e.                                                                                                   |
| c(i, Re)                     | Position of a team i ∈ Pe in the team ranking Re.                                                                             |
| W⩽e                          | Weighted team ranking up to edition e ∈ Es, as defined in (2.5).                                                              |
| wr⩽e                         | Sorting function used to assign each team to their position in W⩽e, as defined in (2.4).                                      |
| c(i, W⩽e)                    | Position of a team i ∈ P⩽e in the weighted team ranking W⩽e.                                                                  |
| |c(i, Re) − c(j, Re)|        | Rank difference between teams i ∈ Pe and j ∈ Pe in Re.                                                                        |
| |c(i, W⩽e) − c(j, W⩽e)|      | Rank difference between teams i ∈ P⩽e and j ∈ P⩽e in W⩽e.                                                                     |
| τ                            | Rank difference threshold used to identify weak teams, as defined in (3.1).                                                   |
| λ                            | Decay factor used in wr⩽e to determine past edition relevance. Table 2: Notation.                                             |

the set of sports, let Es be the set of editions for the competition selected for sport s ∈ S in Table 1 (one can think of such a set as a set of edition years) and let P
s e = {p1, p2*, . . . , p*Ns e
} be the set of all teams playing in edition e ∈ Es, where Ns e is the total number of teams in that edition. We will denote as Mse ⊆ Ps e × Ps e the set of matches in edition e, represented as a set of tuples (*i, j*), where i and j are opposing teams belonging to P
s e
. For the rest of this section, we will omit the subscript s to simplify the notation. All the notation used in our paper is summarized in Table 2.

Match score dataset. For any edition e ∈ E and match (i, j) ∈ Me, let scoree ij (i) denote the score that team i obtained when playing against team j (for example, if "5-6" is the outcome of the match (*i, j*), then scoree ij (i) = 5 and scoree ij (j) = 6). The match score dataset for edition e can be represented by the following set

$${\mathcal{D}}_{e}=\{(i,j,\mathrm{score}_{i j}^{e}(i),\mathrm{score}_{i j}^{e}(j))\mid(i,j)\in{\mathcal{M}}_{e}\}.$$
ij (j)) | (i, j) ∈ Me}. (2.1)
To populate such a dataset, we web-scraped information related to individual matches from the Wikipedia pages corresponding to each edition year of a competition. All sports competitions typically include a group stage, where teams are divided into groups and each team plays against the others in its group to collect the maximum number of points and advance in the competition, and a knockout stage (or bracket stage), where teams are eliminated from the competition if they lose a match. The knockout stage typically consists of the following additional phases:
rounds of 16, quarterfinals, semifinals, and finals. For more details, we refer to [1].

Team rankings. Based on the match score dataset De in (2.1), for each edition e ∈ E, we generated a team ranking by sorting teams based on the following criteria, listed in order of priority: number of matches played, number of victories, number of draws, number of losses, and total score across all matches. The sorting was in descending order for each criterion except for the number of losses, for which an ascending order was used. The choice to use the number of matches played as a sorting criterion is due to the fact that teams reaching the final stages of a competition typically play the largest number of matches, reflecting their strength.

For each edition e, the team ranking obtained through the sorting criteria above is represented as an ordered list of teams Re = (i1, i2*, . . . , i*Ne
), (2.2)

$\mathbf{R}_{e}=(t_{1},t_{2},...,t_{N_{e}})$, $\mathbf{R}_{e}=(t_{1},t_{2},...,t_{N_{e}})$, $\mathbf{R}_{e}=(t_{1},t_{2},...,t_{N_{e}})$, $\mathbf{R}_{e}=(t_{1},t_{2},...,t_{N_{e}})$, $\mathbf{R}_{e}=(t_{1},t_{2},...,t_{N_{e}})$, $\mathbf{R}_{e}=(t_{1},t_{2},...,t_{N_{e}})$, \(\mathbf{R}_{e}=(t_{1},t_{2},.  
where ij ∈ Pe for any j ∈ {1, 2*, . . . , N*e}.

Weighted team ranking. The weighted team ranking aggregates team rankings from the earliest available edition up to a given edition. When referring to the weighted team ranking, we will explicitly write the set of editions as an ordered list of elements as follows E = (e1, e2, . . . , e|E|),
where e1 is the earliest available edition and e|E| is the most recent edition. In such a case, for any h ∈ {1, 2, . . . , *|E|}*, we will denote as

$$\left|\mathcal{Z}.\right\rangle$$
$${\mathcal{P}}_{\leqslant e_{h}}=\cup\{{\mathcal{P}}_{e_{\bar{h}}}\mid e_{\bar{h}}\in{\mathcal{E}}{\mathrm{~and~}}\bar{h}\leq h\}$$
$$(2.3)$$
$e_{1}$ to edition $e_{h}$. We will denote as $N_{\leq e_{h}}$ the 
| eh¯ ∈ E and h¯ ≤ h} (2.3)
the union of the sets of teams from edition e1 to edition eh. We will denote as N⩽eh the cardinality of the set P⩽eh
.

To build the weighted team ranking that aggregates team rankings up to an arbitrary edition e ∈ E, denoted as W⩽e, we use a sorting function wr⩽e : P⩽e → R to assign each team to their position in such a weighted team ranking. For any i ∈ P⩽e, the higher the value of wr⩽e(i),
the higher the position of team i in the weighted team ranking. To show how we compute the weighted team ranking W⩽e, let us denote as c(i, Re) ∈ [1, Ne] the position of a team i ∈ Pe in the team ranking Re in (2.2). For any eh ∈ E = (e1, e2, . . . , e|E|), with h ∈ {1, 2, . . . , *|E|}*, we compute wr⩽eh
(i) as follows

$$wr_{\leqslant e_{h}}(i)\;=\;\begin{cases}(N_{e_{h}}-c(i,\mathcal{R}_{e_{h}})),&\text{if}i\in\mathcal{P}_{e_{h}}\text{and}h=1,\\ (N_{e_{h}}-c(i,\mathcal{R}_{e_{h}}))+\lambda\,wr_{\leqslant e_{h-1}}(i),&\text{if}i\in\mathcal{P}_{e_{h}}\text{and}h\in\{2,\ldots,|\mathcal{E}|\},\\ 0,&\text{if}i\not\in\mathcal{P}_{e_{h}},\end{cases}$$
$$(2.4)$$

where λ ∈ [0, 1] is a decay factor that dictates the rate at which past editions become irrelevant.

The weighted team ranking up to edition e is represented as an ordered list of teams

$${\mathcal{W}}_{\leqslant e}=(i_{1},i_{2},\ldots,i_{N_{\leqslant e}}),$$
), (2.5)
where $i_{j}\in\mathcal{P}_{\leqslant e}$ for any $j\in\{1,2,\ldots,N_{\leqslant e}\}$ and $wr_{\leqslant e}(i_{j})\geq wr_{\leqslant e}(i_{j+1})$ for any $e\in\mathcal{E}$ and $j\in\mathcal{N}$.  
{1, 2*, . . . , N*⩽e − 1}.

## 3 Underdog Achievement

To quantify the underdog achievement, we first need to determine criteria that allow us to distinguish weak teams from strong ones. As noticed in the literature related to soccer [16],

$\left(2.5\right)^{\frac{1}{2}}$
determining a team's strength is a difficult task because of the interaction between skills and randomness. Different approaches have been proposed to evaluate a team's strength, such as using the positions of teams in team rankings [5], the total number of points scored in a competition [6], ELO-ratings [7], or betting odds [16]. In this paper, weak teams are identified based on their positions in the weighted team ranking described in Section 2. Identifying weak teams. Given the weighted team ranking in (2.5), one can consider two strategies to identify weak teams. A first strategy consists of considering the top p% teams in the weighted team ranking as strong and the bottom p% teams as weak. However, in our case, this strategy proved unsuccessful because teams in the bottom p% rarely, if ever, defeat teams in the top p%, regardless of the sport. When p = 50, for some sports, it occasionally happens that teams in the bottom half defeat teams in the top half, while in others, it never happens.

Nevertheless, this is just noise occurring due to teams in mid-ranking positions, and so it is not a reliable indication of weak teams prevailing over strong ones. Therefore, we considered a second strategy, described below.

The approach used in our paper consists of comparing the positions of two teams in the weighted team ranking and considering as weak the team that is ranked significantly lower, if it exists. In other words, there must be a relatively high difference in positions between the teams in the weighted ranking to consider the lower-ranked team as weak. Using the notation introduced in Section 2, for each edition e ∈ E, we denote as c(i, W⩽e) ∈ [1, N⩽e] the position of a team i ∈ P⩽e in the weighted team ranking W⩽e. Given two teams i and j in P⩽e, we refer to |c(i, W⩽e) − c(j, W⩽e)| as the rank difference between teams i and j in the weighted team ranking W⩽e. Given a match (i, j) ∈ Me between teams i and j in edition e, we identify i as a weak team based on W⩽e if c(i, W⩽e) ≤ c(j, W⩽e) − τ, (3.1)
where τ is a positive threshold depending on the sport, to be determined. Note that (3.1) implies that the rank difference |c(i, W⩽e) − c(j, W⩽e)| is greater than τ . When (3.1) is not satisfied and, therefore, two teams have a rank difference less than or equal to the threshold τ , we assume that such teams have similar strengths and we do not classify either of them as weak.

Underdog achievement score. Recall E = (e1, e2, . . . , e|E|), where e1 is the earliest available edition and e|E| is the most recent edition, and recall the definition of weak team based on e ∈ E
in (3.1). For any h ∈ {2, . . . , *|E|}*, we define the underdog achievement score for edition eh ∈ E
as follows

$$\mathrm{UAS}_{e_{h}}\ =\ {\frac{\mathrm{Number}}{\mathrm{Number}}}$$

Number of victories or draws in edition eh by weak teams based on W⩽eh−1 Number of matches in edition eh with a weak team based on W⩽eh−1

$$\frac{\mathrm{on}\ {\mathcal W}_{\leqslant e_{h-1}}}{{\mathcal W}_{\leqslant e_{h-1}}}.\ \ (3.2)$$

Note that in (3.2), weak teams are identified using a weighted team ranking that incorporates all past editions except the current one to avoid biasing the results. One can interpret (3.2)
as the probability that a historically weaker team wins against a historically stronger one in a certain edition of a competition. For each sport, the average underdog achievement score across all editions is given by

$$\mathrm{UAS}\;=\;\frac{1}{|{\mathcal{E}}|-1}\sum_{h=2}^{|{\mathcal{E}}|}\mathrm{UAS}_{e_{h}}.$$
$$(3.3)$$

To investigate further definitions of underdog achievement, we will also consider the following alternative metric

emature matrix  $$\overline{\text{UAS}}\ =\ \frac{\bigcup_{h=2}^{K}\{\text{No.of victories/draws in edition}e_{h}\text{by weak teams based on}\mathcal{W}_{\leq e_{h-1}}\}}{\bigcup_{h=2}^{K]}\{\text{No.of matches in edition}e_{h}\text{with a weak team based on}\mathcal{W}_{\leq e_{h-1}}\}},\tag{3.4}$$
7
which aggregates the numerator and denominator of UASeh in (3.2) across all editions eh in E,
with h ∈ {2, . . . , *|E|}*.

Numerical results. In this subsection, we first perform a rank difference analysis to determine the value of the threshold τ , used to identify weak teams in (3.1), which affects the computation of UASeh and UAS in (3.2) and (3.3), respectively. Then, we quantify UAS for each sport. For each edition e ∈ E, we recall that c(i, Re) ∈ [1, Ne] denotes the position of a team i ∈ Pe in the team ranking Re. Given two teams i and j in Pe, we refer to |c(i, Re) − c(j, Re)| as the rank difference between teams i and j in the team ranking Re.

Figure 1 represents a box plot showing the distribution of the rank differences between teams i and j in the team ranking Re across all soccer matches for all editions, i.e., |c(i, Re) − c(j, Re)| for all (i, j) ∈ Me and e ∈ Esoccer (where Esoccer is the set of editions for soccer). One can see that the rank differences range from 1 to 30, and approximately half of the soccer matches occurred with a rank difference less than or equal to 7, which corresponds to the median value of the distribution. Similarly, Figure 2 represents box plots showing the distribution of the rank differences between teams i and j in the team ranking Re across all matches for all sports and editions, i.e., |c(i, Re) − c(j, Re)| for all (i, j) ∈ Me, e ∈ Es, and s ∈ S (where Es is the set of editions for sport s). One can observe that the medians of the rank difference distributions across all sports range from 2.5 for water polo to 7 for soccer. In particular, for all sports except soccer, the median of the rank difference distribution is less than or equal to 5. For the rest of the paper, we set the threshold τ in (3.1) equal to the median of the corresponding rank difference distribution for each sport (see Table 3).

Figure 3 contains three sets of box plots representing the distribution of UASeh values across all editions eh ∈ E for each sport for three different values of the weight λ in (2.4). One can observe that regardless of the value of λ, field hockey, ice hockey, soccer, and water polo have consistently high values of UASeh compared to the other sports, while lacrosse, roller hockey, and rugby have consistently low values of UASeh
. Water polo is the sport for which the UASeh distribution has the highest median, followed by soccer. Conversely, lacrosse, roller hockey, and rugby are the sports for which the UASeh distribution has the lowest median. Similar results can also be observed for the average underdog achievement score in Figure 4, which shows the UAS value for each sport as a red point along with the corresponding confidence interval at a 95% confidence level when λ in (2.4) is equal to 1. The UAS values for each sport for three different values of λ are reported in Table 3.

Figure 5 shows a Laney proportion chart (or Laney p'-chart) representing the UAS value for each sports when λ in (2.4) is equal to 1. Laney p'-charts are statistical control charts used to monitor the proportion of nonconforming items in a stochastic process [11]. Control limits are included on the chart to help identify when the process is out of control, suggesting that special causes may be present. In our case, almost all sports fall outside the control limits, indicating that the UAS values across the sports do not follow the same distribution, which is expected





| UAS           |     |       |         |       |
|---------------|-----|-------|---------|-------|
| Sport         | τ   | λ = 1 | λ = 0.5 | λ = 0 |
| Basketball    | 4   | 0.25  | 0.19    | 0.16  |
| Cricket       | 4   | 0.15  | 0.11    | 0.08  |
| Field Hockey  | 4   | 0.31  | 0.22    | 0.20  |
| Futsal        | 5   | 0.17  | 0.13    | 0.07  |
| Handball      | 4   | 0.21  | 0.17    | 0.11  |
| Ice Hockey    | 3   | 0.30  | 0.21    | 0.18  |
| Lacrosse      | 4   | 0.08  | 0.07    | 0.06  |
| Roller Hockey | 5   | 0.05  | 0.02    | 0.01  |
| Rugby         | 5   | 0.07  | 0.04    | 0.03  |
| Soccer        | 7   | 0.36  | 0.27    | 0.22  |
| Volleyball    | 4   | 0.22  | 0.11    | 0.07  |
| Water Polo    | 2.5 | 0.37  | 0.34    | 0.32  |

since we are considering different sports. The reason why we decided to include this Laney p'- chart is to show that we obtain similar results in terms of underdog achievement regardless of the metric used, whether it is (3.2) in Figure 3, (3.3) in Figure 4, or (3.4) in Figure 5. In particular, from Figure 5, one can observe that soccer and water polo have the highest UAS values, followed by field hockey and ice hockey, while roller hockey and rugby have the lowest UAS values.

For simplicity, we will now perform statistical testing focusing on the case where λ in (2.4)
is equal to 1. To statistically confirm the differences in the UAS values across all the sports, we conducted a Kruskal-Wallis test [9], which yielded a p-value of 2.47 · 10−10, indicating significant differences at a 5% significance level. To identify the specific pairs of sports with statistically significant differences in their UAS values, we resorted to Dunn's test with Bonferroni correction [3], which performs multiple non-parametric pairwise comparisons among all the sports. The results of Dunn's test are included in Table 4 only for pairs of sports with significant differences in their UAS values at a 5% significance level. Such results confirm the observations from Figures 3–5, indicating that field hockey, ice hockey, soccer, and water polo exhibit higher underdog achievement compared to lacrosse, roller hockey, and rugby.

## 4 Randomness Model

In this section, we develop a model consisting of randomness factors that can affect match outcomes in team ball sports. In Section 5, such a model will be used to gain insights into the relationship between the randomness factors and underdog achievement. Unlike [16] and [10], which propose variables of randomness affecting goal scoring in soccer as the match progresses, our model focuses on static factors, assuming scores as given. Therefore, we exclude factors that may influence player motivation, such as match location and current score, which are known to impact all sports and are not of interest to our analysis.

The factors that contribute to the inherent randomness observed in match outcomes are listed in Table 5 and categorized into three main groups: physical environment, player, and team. We



