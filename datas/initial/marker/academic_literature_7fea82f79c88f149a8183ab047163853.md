# Formation Of Coalition Structures As A Non-Cooperative Game 2: Applications Dmitry Levando, ∗

## Abstract

The paper uses a non-cooperative simultaneous game for coalition structure formation (Levando, 2016) to demonstrate some applications of the introduced game: a cooperation, a Bayesian game within a coalition with intra-coalition externalities, a stochastic game, where states are coalition structures, self-enforcement properties of **non-cooperative**
equilibrium and construction of a non-cooperative stability criterion.

Keywords: **Noncooperative Games, Cooperation, Bayesian Games, Stochastic Games,**
JEL **: C72, C73**

## 1 Subject Of The Paper

The previous paper, Levando (2016), introduced a non-cooperative game to study coalition structures formation as a non-cooperative game. The suggested game consisted of a set of players N1, a coalition structure construction mechanism ({K,P(K), R(K)}**), and individual properties of players,**
1

## Γ(K) = Dk, {K,P(K), R(K)},(Si(K), Ui(K))I∈N E,

where K **is a maximum coalition size or a maximum number of deviators,** P(K**) is a family of coalition structures such that any coalition size (a number** of deviators ) does not exceed K, R(K**) is a family of specific coalition**
structure formation rules, Si(K**) is a corresponding set of strategies of** i ∈ N
induced by K, Ui(K**) is family of specific coalition structure payoffs for** i in every partition P ∈ P(K). Games for all relevant K **make a nested family**

Γ = {Γ(K = 1), . . . , Γ(K), . . . Γ(K = N)}: Γ(K **= 1)** ⊂ Γ(K) ⊂ Γ(K = N).

The family of games is characterized by a list of equilibrium strategy profiles, σ
∗
(1), . . . , σ∗(K)**, . . . , σ**∗(K = N)
**, where** σ
∗
(K**) = (**σ
∗

i
(K))i∈N **. and**
by a list of equilibrium partitions, {P
∗}(1)**, . . . ,** {P
∗}(K)**, . . . ,** {P
∗}(K =
N)
, {P
∗}(K) ⊂ P(K). Every game Γ(K**) from a family Γ, which has an**
equilibrium may be in mixed strategies.

This paper demonstrates applications of the constructed game for: selfinterest cooperation, a Bayesian stochastic game, studying self-enforcing properties of an equilibrium and construction of a non-cooperative **criterion** of coalition structure stability.

## 2 Cooperation

To explain formally cooperation we will retell with necessary changes the example from the corporate dinner game in Levando (2016). The result of this example will be used to explain formal definition of what a cooperation in allocations of self-interest players can be. In this section the term "cooperation" means only a cooperation of players in allocations over coalitions.

Cooperation in payoffs is not addressed here.

## 2.1 Cooperation In A Corporate Dinner Game

Consider a game of 4 players: A is a President; B is a senior vice-president; C1, C2 are two other vice-presidents. Coalition is a group of players at one table. Every player may sit only at one table. Coalition structure is an allocation of all players over no more than four tables. Empty tables **are not** taken into account.

Individual set of strategies is a set of all coalition structures for the players. Any player can choose a coalition structure. A set of strategies in the game is a direct (Cartesian) product of four individual strategy sets. A choice of all players is a point in the set of strategies of the game.

Preferences are such that everyone (besides A) would like to have **a dinner**
with A, but A only with B. Everyone wants players outside his table to eat individually, due to possible dissipation of rumors or information exchange. No one can enforce others to form or not to form coalitions.

In every partition any coalition (i.e. a table with players who eat at the table) is formed only if everybody at the table agrees to have dinner together, otherwise the player eats alone. The same coalition belongs to different coalitions, but with different allocations of other players over other coalitions.

The game is simultaneous and one shot. Realization of the final partition
( a coalition structure) depends on choices of coalition structures of all players. Example. Let player A choose {{A, B}, {C1}, {C2}}**; player B choose**
{{A, B}, {C1}, {C2}}; player C1 choose {{A, C1}, {B}, {C2}}**, and player** C2 choose {{A, C2}, {B}, {C2}}. Then the final partition is {{**A, B**}, {C1}, {C2}}.

It is clear that strong Nash equilibrium (Aumann, 1960), which is based on a deviation of a coalition of any size, does not discriminate between coalition structures mentioned above.

Players have preferences over coalition structures. Payoff profile of the game should be defined for every final coalition structure. Table 1 presents coalition structures only with the best individual payoffs.2 **Thus only some**
partitions from the big set of all strategies deserve attention. The first column is a number of a strategy. The second column is an allocation of players over a coalition structure, i.e. a strategy, and also a list of best final coalition structures. The third column is a payoff profile for all players of every listed coalition structure. The fourth column is a list of coalition values in the listed coalition structure, if to calculate values from the cooperative game theory.

Payoffs are defined for a game of four players in such a way, that an increase in the size of a maximum coalition from K = 2 to K = 3, **4 only decreases individual payoffs. Thus from one side there is "an optimal" coalition**
size, from another an increase in a maximum coalition size does not change the equilibrium. The last property will be addressed formally in one of the following sections of the current paper.

| num                  | Best final partitions   | Non-cooperative payoff profile   | Values of coalitions as in   |
|----------------------|-------------------------|----------------------------------|------------------------------|
| (UA, UB, UC1 , UC2 ) | cooperative game theory |                                  |                              |
| 1                    | {{A, B}, {C1}, {C2}}    | (10,10,3,3)                      | 20AB, 3C1 , 3C2              |
| 2 ∗                  | {{A, B}, {C1, C2}}      | (8,8,5,5)                        | 16AB, 10C1,C2                |
| 3                    | {{A, C1}, {B, C2}}      | (3,5,10,5)                       | 13AC1 , 10BC2                |
| 4                    | {{A, C1}, {B}, {C2}}    | (3,3,10,3)                       | 13AC1 , 3B, 3C2              |
| 5                    | {{A, C2}, {B, C1}}      | (3,5,5,10)                       | 13AC2 , 10BC1                |
| 6                    | {{A, C2}, {B}, {C1}}    | (3,3,3,10)                       | 13AC1 , 3B, 3C1              |
| 7                    | all other partitions    | (1,1,1,1)                        | ≤ 4                          |

Table 1: Strategies and payoffs in the corporate dinner game The game runs as follows. Players simultaneously and independently announce choices of desirable coalition structures, then the final **coalition**
2**All other coalition structures have significantly lower payoffs.**
structure is formed according to the rule above, and payoffs are assigned.

The rule is not formalized for a shorter exposition.

Players A and B would always like to be together, then with C1 or C2.

Being rational A and B **would choose coalition structure with the highest**
payoff, i.e. the strategy 1. The first best choices of C1 and C2 **is to have**
a dinner with A**. However, A will never choose to be with either of them.**
Hence, non-realization of this option makes a potential loss for both C1 and C2.

Both players C1 and C2 **are aware of this. Another common knowledge,**
that they both know about each other, is that if they make a coalition of two, each will be better off. This behavior meets sociological understanding of cooperation - to unite in order to prevent a loss, to which each is individually exposed to.

A cooperation between C1 and C2 does not demolish the coalition {**A, B**},
but only reduces payoffs for it's members. At the same time players A and B cannot prevent cooperation between C1 and C2 **(or to insure against).**
On the other hand, if players A and B choose strategy 2 they will obtain coalition {A, B} **in any case. In terms of mixed strategies this means that**
an equilibrium mixed strategy for A and for B **is the whole probability space**
over two points, two coalition structures.

From the forth column we can see that the corresponding cooperative game has an empty core. Strong Nash equilibrium cannot be applied here also. Coalition value approach also supports the idea of cooperation, but without an explicit allocation of payoffs. This means it ignores individual rationality and incentive compatibility to participate in a coalition. For example, how players C1 and C2 **should divide the value of a joint coalition**
{C1, C2} **equal to 10?**
The constructed game has a unique equilibrium, which in terms of individual payoffs is characterized as the second-best efficient for every player.

There are two coalitions in the equilibrium coalition structure.

## 2.2 Formal Definition Of Cooperation

This section formalizes an idea of cooperation presented in the example above. We demonstrate only one way for defining cooperation, when it is intentional and complete.

Definition 1 (complete cooperation in a coalition). In a game Γ(K) **with** an equilibrium σ
∗
(K**) = (**σ
∗

i
)i∈N a set of players g, **completely cooperate**
in a coalition g ex ante if for every player i ∈ g **there is** ex ante : for every i in g, a desirable coalition g **always belongs to a chosen**
coalition structure, i.e such if siis chosen by i**, then** si ∈ Si(Pi), g ∈ Pi, where Piis a coalition structure chosen by i**, however coalition**
structures chosen by different players may be different.

ex post 1 : every realized coalition structure contains g, i.e. g ∈ ∀P
∗
,
where P
∗
**is a formed equilibrium partition of** Γ(K),
ex post 2 EUΓ(K)
i σ
∗
(K)
≥ EUΓ(K)
i σ
∗

i(K), σ∗−i(K)
**, for** ∀σi(K) 6= σ
∗

i(K),
First of all, cooperation is defined for a game Γ(K**). If a game changes due**
to a change in the number of deviators K**, the cooperation may evaporate.**
Every player chooses a partition with the desirable coalition g **with positive probability. But individually chosen coalition structures by all players**
may be different.

After the game is over the coalition g always belongs to every final equilibrium coalition structure, disregard allocation of players over other **coalitions.**
A final partition may differ from a chosen one, but in any case it will contain the desirable coalition.

The defined cooperation assumes agents are acting from self-interest motivations. The lunch game example further expands the case, where there is imperfect cooperation.

The dinner game example has the complete cooperation for players C1 and C2**. The definition does not exclude inter and intra-coalition interaction.**
If we relax some conditions of the definition we will obtain weaker conditions for cooperation. Cooperation in repeated games is of special interest and will be addressed in one of the next papers.

## 3 Bayesian Games

In this section we demonstrate how intra-coalition externalities of the grand coalition may happen from equilibrium mixed strategies. In order to show that, a standard Battle of Sexes game is modified.

Let there be two players, Ann and Bob. Each has two options: to be together with another or to be alone. In every option each can choose where to go: to Box or to Opera. Hence every player has four strategies. A set of strategies of the game leads to 16 outcomes. Every outcome consists of payoff profile and a partition (or a coalition structure). Both players have preferences over coalition structures: they prefer to be together, then be separated.

The rules of coalition structure formation mechanism are:
1. If they both choose to be together, i.e. both choose the coalition structure Pjoint = {Ann, Bob} **then:**
(a) if both choose the same action for Pjoint **(i.e. both choose Box or**
both choose Opera), then they go to where they both choose to go,
(b) otherwise they do not go anywhere, but enjoy just being together; 2. if at least one of them chooses to stay alone, i.e. chooses a partition Psepar = {{Ann}, {Bob}}**, then each goes alone to where she/he**
chooses, may be to different Opera or different Box performances.

Formally the rules are:

| BBob,Psepar   | OBob,Psepar   | BBob,Pjoint    | OBob,Pjoint          |
|---------------|---------------|----------------|----------------------|
| (2; 1)∗,K=1   | (0;0)         | (2;1)          | (0;0)                |
| {{1}, {2}}    | {{1}, {2}}    | {{1}, {2}}     | {{1}, {2}}           |
| (0;0)         | (1; 2)∗,K=1   | (0;0)          | (1;2)                |
| {{1}, {2}}    | {{1}, {2}}    | {{1}, {2}}     | {{1}, {2}}           |
| ∗,K=2         |               |                |                      |
| (2;1)         | (0;0)         | (2 + ǫ; 1 + ǫ) |                      |
| {{1}, {2}}    | {{1}, {2}}    | (ǫ;ǫ)          |                      |
| {1, 2}        | {1, 2}        |                |                      |
| (0;0)         | (1;2)         | (ǫ;ǫ)          | (1 + ǫ; 2 + ǫ) ∗,K=2 |
| {{1}, {2}}    | {{1}, {2}}    | {1, 2}         | {1, 2}               |

$\mathcal{R}(K=1)\colon S(K=1)\mapsto S(\{\{1\},\{2\}\}),$  $\forall s\in S_{i}(K=1)=\{O_{Ann,P_{separ}},B_{Ann,P_{separ}}\}\times\{O_{Bob,P_{separ}},B_{Bob,P_{separ}}\}$
and

$$\mathcal{R}(K=2)\colon S(K=2)\mapsto\begin{cases}S(\{1,2\}),\\ \text{if}s\in\{O_{A m n,P_{v e a r}},B_{A m n,P_{v e a r}}\}\times\{O_{B o b,P_{v e a r}},B_{B o b,P_{v e a r}}\}\\ S(K=2)\setminus S(\{1,2\}),\quad\text{otherwise}\end{cases}$$

The whole Table 2 corresponds to the game with K **= 2 where the game**
for K = 1 is a component. If Ann and Bob play the game with K **= 1 with a** single coalition structure {{Ann}, {Bob}}**, then the payoffs for this game are** in the two-by-two top-left corner of Table 2. If Ann and Bob are together, then each obtains an additional payoff ǫ**, and the corresponding cells make a**
two-by-two bottom-right corner.

Every game with K = 1 and K **= 2 has only one mixed strategies equilibrium and only one equilibrium partition. Mixed strategies equilibrium for**
K = 1 is described in every textbook. A change in K from K = 1 to K = 2 results in a changes of an equilibrium strategy profile and an equilibrium partition.

For K = 2 the game also has a mixed strategies equilibrium like for K **= 1.**
The difference is that now players have an allocation in a different coalition structure in comparison to the case of K **= 1. Mixed strategies equilibrium** for Ann is: σ
∗
(BAnn,Pjoint ) = (1+ǫ)/**(3+2**ǫ), σ
∗
(OAnn,Pjoint ) = (2+ǫ)/**(3+2**ǫ),
i ∈ {Ann,Bob}, what results in an equilibrium partition Pjoint**, what is the**
grand coalition. And there is an equilibrium intra-coalition activity.

The presented game allows to construct intra-coalition externalities from mixed strategies within one partition. Mixed intra-coalition externalities means that players are exposed to equilibrium fluctuations from strategic actions of another player.

A game as above can not be constructed within any cooperative game equilibrium concept. It is impossible to construct Shapley value (195) **here**
even if there is one coalition: players have equilibrium mixed strategies **inside** it.

## 4 Stochastic Games

Shapley (1953) defined stochastic games as " the play proceeds by **steps from**
position to position, according to transition probabilities controlled jointly by the two player". This section demonstrates how this type of games with coalition structures as states of a game may appear in the constructed game. The example differs from example above as a set of the equilibrium mixed strategies induces more than one equilibrium coalition structure. We **use a** game, similar to corporate dinner game, but with identical players.

## 4.1 Corporate Lunch Game

There is a set of four identical players N = {A, B, C, D}**. An individual** strategy is a coalition structure, or an allocation of all players across tables during lunch. A coalition structure is an allocation of players over no more than four tables, where possibly empty tables do not matter. A rule of coalition formation is a unanimous agreement to form a coalition. If player chooses a coalition, but other members of the coalition did not choose him, the player eats alone.

A player has preferences over coalition structures: she/he prefers to eat with someone and other players eat individually. If one eats alone he is **hurt** by a possible formed coalition of others. Coalition structures, and payoff profiles for the highest cases payoffs are presented in Table 3:
Table 3: Office lunch game: strategies and payoff profiles. Full set of **equilibrium mixed strategies are indicated only for player** A

| Coalition values        |                                     |                               |                |
|-------------------------|-------------------------------------|-------------------------------|----------------|
| num                     | Coalition structure                 | Payoff profile UA, UB, UC, UD | as in          |
| cooperative game theory |                                     |                               |                |
| 1 ∗                     | {A, B}, {C}, {D}: σ A = σ ∗ B = 1/3 | (10,10,3,3)                   | 20A,B, 3C, 3D  |
| ∗                       |                                     |                               |                |
| ∗                       | {A, C}, {B}, {D}: σ ∗               | ∗                             |                |
| 2                       | A = σ C = 1/3                       | (10,3,10,3)                   | 20A,C, 3B, 3D  |
| ∗                       | {A, D}, {C}, {B}: σ ∗               | ∗                             |                |
| 3                       | A = σ D = 1/3                       | (10,3,3,10)                   | 20A,C, 3C, 3B  |
| 4                       | {A}, {B}, {C, D}                    | (3,3,10,10)                   | 3A, 3B, 29C,D  |
| 5                       | {A}, {D}, {C, B}                    | (3,10,10,3)                   | 3A, 3B, 29C,D  |
| 6                       | {A}, {C}, {B, D}                    | (3,10,3,10)                   | 3A, 3B, 29C,D  |
| 7                       | {A}, {B}, {C}, {D}                  | (3,3,3,3)                     | 3A, 3B, 3C, 3D |
| 8                       | all other with K = 3, 4             | (0,0,0,0)                     | = 0            |

Payoffs in Table 3 are organized in the way that formation of a coalition by other players deteriorates payoffs for the rest. Formation of **two 2-player**