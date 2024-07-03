# Binary Trees and Taxicab Correspondence Analysis of Extremely Sparse Binary Textual Data : A Case Study 

Choulakian V, Université de Moncton, vartan.choulakian@umoncton.ca

Allard J, Université de Moncton, jacques.allard@gmail.com

Kenett R, Samuel Neaman Institute, Technion, ron@kpa-group.com

11 avril 2024


#### Abstract

Résumé This is a case study, where Taxicab Correspondence Analysis reveals that the underlying structure of an extremely sparse binary textual data set can be represented by a binary tree, where the nodes representing clusters of words can be interpreted as topics. The textual data set represents Israel's Declaration of Independence text and 40 diverse Israeli Interviewees. The analysis provides for a compare and contrast study of textual data coming from two different sources. Furthermore, we propose an adjusted sparsity index which takes into account the size of the data table.

Key Words : Binary tree, Taxicab Correspondence Analysis, binary textual data, adjusted sparsity index, visualization.


## 1 Introduction

The motivation of this paper is the statistical analysis of an extremely sparse binary (presence/absence) $0 / 1$ valued textual data set $\mathbf{Z}=\left(z_{i j}\right)$ of size $1730 \times 343$; where $z_{i j}=1$ means the presence of the token (word) or term (collection of words) $i$ in the document (phrase) $j$, and $z_{i j}=0$ means the absence of the token (word) or term (collection of words) $i$ in the document (phrase) $j$. The data set is constructed from (40+1) texts : the 40 texts represent interviews done in Israel during the Covid in 2021, plus the text of the Declaration of Independence (DOI) of the State of Israel announced by David Ben Gurion in 1948. It provides an approach to compare and contrast unstructured data from different sources. This ability to integrate
the analysis of text from different origins is demonstrated here with a case study.

According to Kenett et al. (2023) "40 personal in-depth interviews with a series of well-known and influential Israeli individuals from various groups and genders, who are involved in various areas of endeavour, positioned all over the political spectrum and are of diverse ages and worldviews : a 'representative sample' (that includes) male and female, Jewish, Druze, and Arab, secular, religious and ultra-Orthodox, and young and older respondents holding a broad range of social and political positions. Those interviewed included senior academics, writers and scientists, former politicians, media figures and publicists, rabbis, economists, social entrepreneurs, strategists, and retired military officers. Most of the interviews were conducted in January-February 2021 via Zoom, and typically lasted between sixty to ninety minutes. They expressed their viewpoints and attitudes towards the question representing 'organizing principles' and values on which Israeli society should be predicated in the decades to come. A qualitative, intuitive, analysis of the interviews led the researchers to the conclusion that there is indeed a broad common denominator among those with a wide variety of opinions, which is closely linked with the major principles of the Declaration of Independence (DOI) of the State of Israel."

The data has been analyzed by Kenett et al. (2023) by latent semantic analysis (LSA), which consists of singular value decomposition (SVD) of the tf-idf coded data set.

The approach differs in this paper : It is based on the joint use of correspondence analysis (CA) and its robust $l_{1}$ variant named taxicab CA (TCA). TCA is able to reveal the underlying structure of the extremely sparse data in a complete binary tree; which represents the interpretable diagonal blocks structure of the data set; that is, biclustring of the rows and the columns simultaneously. It is important to note that visualization via maps plays pivotal role in the interpretation by CA and TCA approaches. Furthermore, we propose an adjusted sparsity index which takes into account the size of the data table.

In section 2, we analyze in detail the Declaration of Independence (DOI) text by CA and TCA, where all the details of the computation are shown. In sections 3, 4 and 5, we analyze the full (40+1) corpus of texts from interviews; in section 6 we propose the adjusted sparsity index; and we conclude in section 7.

Benzécri (1966) is the reference source on the linguistic foundations of $\mathrm{CA}$; while the reference book on applied textual data analysis by $\mathrm{CA}$ is Benzécri (1981), where binary textual data are discussed in pages 259-359.

Lebart (2024) describes the analysis of binary data by PCA and CA : With the influence of rare observations (words) we often see the common practice of eliminating words with marginal frequencies less than 10. See also Qi et al. (2023, page 17). This practice in CA of textual data dates since Benzécri (1981); where the elimination of rare columns or rows is done to obtain interpretable maps by CA. TCA, being robust, eliminates only rows or columns with zero marginals ; see Choulakian et al. $(2006,2023)$ and this paper.

## 2 The analysis of the Declaration of Independence

"The Declaration of Independence (DOI) has, basically, three parts :

Part a) Historical : It links the State of Israel to its historical-Biblical roots;

Part b) Operational : It includes statements about how the state would operate;

Part c) Visionary : This is the most pivotal section, comprising statements protecting civil liberties and expressing aspirations for peace and coexistence.

In the next subsection, we reproduce DOI text from Kenett et al. (2023) : It is composed of 21 rows (phrases) and 43 different words (terms) will represent the columns of the binary table to be analyzed in detail by CA and TCA.

### 2.1 Declaration of Independence text

R1) THE STATE OF ISRAEL will be open for Jewish immigration and for the Ingathering of the Exiles

R2) it will foster the development of the country for the benefit of all its inhabitants ;

R3) it will be based on freedom, justice and peace as envisaged by the prophets of Israel;

R4) it will ensure complete equality of social and political rights to all its inhabitants irrespective of religion, race or sex;

R5) it will guarantee freedom of religion, conscience, language, education and culture;

*R6) it will safeguard the Holy Places of all religions; and

*R7) it will be faithful to the principles of the Charter of the United Nations.

R8) THE STATE OF ISRAEL is prepared to cooperate with the agencies and representatives of the United Nations in implementing the resolution of the General Assembly of the 29th November, 1947, and

R9) will take steps to bring about the economic union of the whole of Eretz-Israel.

R10) WE APPEAL to the United Nations to assist the Jewish people in the building-up of its State and

R11) to receive the State of Israel into the comity of nations.

R12) WE APPEAL - in the very midst of the onslaught launched against us now for months -

R13) to the Arab inhabitants of the State of Israel to preserve peace and participate in the upbuilding of the State

R14) on the basis of full and equal citizenship and due representation in all its provisional and permanent institutions.

R15) WE EXTEND our hand to all neighboring states and their peoples in an offer of peace and good neighborliness, and

R16) appeal to them to establish bonds of cooperation and mutual help with the sovereign Jewish people settled in its own land.

R17) The State of Israel is prepared to do its share in a common effort for the advancement of the entire Middle East.

R18) WE APPEAL to the Jewish people throughout the Diaspora to rally round the Jews of Eretz-Israel

*R19) in the tasks of immigration and upbuilding and to stand by them

R20) in the great struggle for the realization of the age-old dream - the redemption of Israel.

R21) HEREBY DECLARE THE ESTABLISHMENT OF A JEWISH STATE IN ERETZ-ISRAEL, TO BE KNOWN AS THE STATE OF ISRAEL.

### 2.2 Construction of the binary data table

The DOI text is divided into 21 phrases numbered from R1 to R21. 18 phrases are described by 43 apriori chosen words, from which the presence/absence (0/1) coded table $\mathbf{Z}$ of size $I \times J=18 \times 43$ is formed. Such a table is called a document term matrix (DTM) with binary weights.

Phrases R6, R7 and R19, starred above, are deleted and not included in the statistical analysis since they do not include any of the 43 words analyzed here.

By applying Benzécri's principle of distributional equivalence, $\mathbf{Z}$ is equivalent to the contingency table $\mathbf{N}$ of size $I \times J=18 \times 24$. The apparent
sparsity of $\mathbf{Z}$ is $92.38 \%$; while the sparsity of $\mathbf{N}$ is $90.74 \%$, which represents the sparsity of the data. The contingency table $\mathbf{N}$ can be found in the Appendix.

Table 1 represents the distributions of the row and column marginals of the CA (TCA) equivalent data sets $\mathbf{Z}$ and $\mathbf{N}$.

Table 1 : CA equivalent data sets $\mathrm{Z}$ and $\mathrm{N}$ of DOI.

|  | column marginals |  |  |  |  |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  | $\mathbf{Z}$ of size $18 \times 43$ |  |  |  | $\mathbf{N}$ of size $18 \times 24$ |  |  |  |  |  |
| values | 1 | 2 | 35 | 6 | 1 | 2 | 3 | 4 | 5 | 6 |
| counts | 36 |  | 2 1 | 1 | 4 | 12 | 4 | 2 | 1 | 1 |
|  | row marginals of $\mathbf{Z}$ or $\mathbf{N}$ |  |  |  |  |  |  |  |  |  |
| values | 1 | 2 |  | 5 |  |  |  |  |  |  |
| counts | 1 |  | 66 | 2 |  |  |  |  |  |  |

A hapax is a word used once in the text; that is its marginal count is 1. It is a common practice in $\mathrm{CA}$, specially in textual data analysis by $\mathrm{CA}$, to eliminate hapaxes; see for instance Lebart (2024). If we eliminate hapaxes in $\mathbf{Z}$, then we eliminate 36 columns (words), see Table 1. If we eliminate hapaxes in $\mathbf{N}$, then we eliminate 4 columns (words). For instance, the 4 hapaxes (social, political, equality, rights) in $\mathbf{Z}$ are no more hapaxes in $\mathbf{N}$ : they represent the term (social + political + equality + rights) and are found in phrase R4; moreover they represent important concept of human and democratic rights; thus eliminating them carries information loss. Similarly for the term (economic + take + bring + whole) found in the phrase R9.

### 2.3 Correspondence analysis (CA)

We use the $\mathrm{R}$ package ca of Greenacre et al. (2022) to analyze the contents of $\mathbf{N}$. First, we look at the singular values :

res.caNmerged $\$$ sv

[1] 1.00000001 .00000001 .00000000 .98063440 .94818510 .93271780 .9292113

0.8599820

[9] 0.84584540 .81649660 .79756320 .75959740 .75069880 .71482110 .6614619 0.5756657

The first 3 singular values are equal to 1 , which shows that the underlying structure of $\mathbf{N}$ is 4-blocks diagonal (see the CA map in the appendix) :

$$
\mathbf{N}=\left(\begin{array}{cccc}
\mathbf{B}_{1} & & & \\
& \mathbf{B}_{2} & & \\
& & \mathbf{B}_{3} & \\
& & & \mathbf{B}_{4}
\end{array}\right)
$$

where each of the 3 blocks $\mathbf{B}_{1}, \mathbf{B}_{2}$ and $\mathbf{B}_{3}$ is made of the cells ( $\left.\mathrm{R} 2, \mathrm{C} 11\right)$, (R12,C9), (R14,C20), where

C11 is the term "country + development" in phrase R2

C9 is the term "us + now" in phrase R12

C20 is the term "basis + full + equal" in phrase R14;

and the remaining cells form the 4 th block, $\mathbf{B}_{4}$ of size $15 \times 21$. So CA of

$\mathbf{N}$ is equivalent to $\mathbf{C A}$ of $\mathbf{B}_{4}$. $\mathbf{B}_{4}$ is of size $15 \times 21$ and its sparsity is $88.25 \%$.

The singular values resulting from $\mathrm{CA}$ of $\mathbf{B}_{4}$ are identical to to the singular values of $\mathrm{CA}$ of $\mathbf{N}$ which are different from 1, as can be seen below :

res.caB $4 \$$ sv

[1] 0.98063440 .94818510 .93271780 .92921130 .85998200 .84584540 .8164966 0.7975632

[9] 0.75959740 .75069880 .71482110 .66146190 .57566570 .3178244

Figure 1 represents the principal map of dimensions 1 and 2 obtained from $\mathrm{CA}$ of $\mathbf{B}_{4}$, which is identical to the principal map of dimensions 4 and 5 of $\mathrm{CA}$ of $\mathbf{N}$.



Figure 1: CA map.

Visually, we see that there are at least 3 clusters in Figure 1. We show that there are 4 clusters : The one on the right is evident, while the boundaries of the 3 clusters on the left are fuzzy. A clearer picture of the 4 clusters is obtained by TCA, which we present in the next subsection.

### 2.4 Taxicab correspondence analysis (TCA)

We use the R package TaxicabCA of Allard and Choulakian (2019) to obtain TCA Figure 2, which displays TCA principal map of $\mathbf{B}_{4}$, and Figure 3 displays the associated TCA contribution principal map of $\mathbf{B}_{4}$. It is evident that there are 4 clusters, where one cluster is found in each quadrant. The 4 extreme points in Figure 3 succinctly describe the topics elaborated in the DOI : State of Israel (political), jewish people (ethnic identity), economic (development) and social+political+equality+rights (human rights). Here, we describe in more detail the 4 clusters (topics). The interpretation of each cluster is based on the contribution (displayed in parenthesis) of each point (row or column). Note that the 4 clusters are denoted by PP, PN, NP and $\mathbf{N N}$, where $N=$ negative and $P=$ positive.

Cluster NP in the upper left quadrant: The words \{social +political +equality +rights (7.45), education + culture (3.36), religion (2.92), freedom (2.56)\} appear in the two phrases R4 (5.86), R5 (4.51)

R4) it will ensure complete equality of social and political rights to all its inhabitants irrespective of religion, race or sex

R5) it will guarantee freedom of religion, conscience, language, education and culture

Cluster PP in the upper right quadrant: The words \{state of israel (4.46), establishment + jewish state (3.05), Jewish+open (3.05), common + middle east (3.06), general (0.72)\} appear in the phrases R21 (2.93), R1 (2.87), R17 (1.71), R8 (1.14), R11 (0.57) :

R21) HEREBY DECLARE THE ESTABLISHMENT OF A JEWISH STATE IN ERETZ-ISRAEL, TO BE KNOWN AS THE STATE OF ISRAEL

R1) THE STATE OF ISRAEL will be open for Jewish immigration and for the Ingathering of the Exiles

R17) The State of Israel is prepared to do its share in a common effort for the advancement of the entire Middle East

R8) THE STATE OF ISRAEL is prepared to cooperate with the agencies and representatives of the United Nations in implementing the resolution of the General Assembly of the 29th November, 1947

R11) to receive the State of Israel into the comity of nations

Cluster NN in the lower left quadrant : The words \{economic + take + bring+whole (5.65), good + states + hand (5.10), peace (2.97),
great +struggle (2.82), israel (2.81), based (1.43)\} appear in in the R9 (5.28), R15 (4.14), R20 (3.17), R3 (2.74) phrases :

R9) will take steps to bring about the economic union of the whole of Eretz-Israel

R15) WE EXTEND our hand to all neighboring states and their peoples in an offer of peace and good neighborliness, and

R20) in the great struggle for the realization of the age-old dream the redemption of Israel

R3) it will be based on freedom, justice and peace as envisaged by the prophets of Israel

Cluster PN in the lower right quadrant : The words \{jewish people (4.01), help + land (3.21), jews + diaspora (3.21), state (3.05), building (1.53), arab (1.53)\} appear in the phrases R16 (3.50), R18 (3.36), R13 (2.98), R10 (2.96) :

R16) appeal to them to establish bonds of cooperation and mutual help with the sovereign Jewish people settled in its own land

R18) WE APPEAL to the Jewish people throughout the Diaspora to rally round the Jews of Eretz-Israel

R13) to the Arab inhabitants of the State of Israel to preserve peace and participate in the upbuilding of the State

R10) WE APPEAL to the United Nations to assist the Jewish people in the building-up of its State and

### 2.5 Underlying structure of $\mathrm{B}_{4}$

According to Benzécri (1973), there is a lateral ordering in the structure of the data set $\mathbf{B}_{4}$ because the value of the first principal singular value $\rho_{1}=0.9806>0.837$. This lateral ordering can be of 2 kinds : quasi-multi blocks diagonal or quasi-diagonal (Guttman effect). For extremely sparse data sets, such as of $\mathbf{B}_{4}$ whose sparsity is $88.25 \%$, it is often difficult to distinguish between these 2 cases.

Table 2 : QSR (\%) for the first 4 dimensions of DOI.

|  |  | TCA |  |  |
| :--- | :--- | :--- | :--- | :--- |
| Axis $\alpha$ | $Q S R_{\alpha}\left(V_{+} U_{+}, V_{-} U_{-}\right)$ | $Q S R_{\alpha}\left(V_{-} U_{+}, V_{+} U_{-}\right)$ | $Q S R_{\alpha}$ | $\delta_{\alpha}$ |
| 1 | $(39.5,36.9)$ | $(-\mathbf{1 0 0},-74.3)$ | $\mathbf{5 2 . 7}$ | $\mathbf{0 . 8 8 8}$ |
| 2 | $(51.1,33.6)$ | $(-56.2,-74.5)$ | $\mathbf{4 9 . 6}$ | $\mathbf{0 . 8 5 4}$ |
| 3 | $(31.6,35.1)$ | $(-73.5,-87.1)$ | 46.9 | 0.836 |
| 4 | $(46.0,45.2)$ | $(-58.0,-58.4)$ | 51.1 | 0.802 |



Figure 2: TCA principal map.

In the framework of TCA, the QSR index also can be helpful in deriving the underlying structure of the extremely sparse set $\mathbf{B}_{4}$. Table 2 displays the QSR indices in \%. For the first principal dimension, we note that $Q S R_{1}\left(V_{-} U_{+}\right)=-100 \%$; this means that the underlying structure of $\mathbf{B}_{4}$ is reducible to :

$$
\mathbf{B}_{4} \equiv\left(\begin{array}{cc}
\dot{\mathbf{A}} & \mathbf{0} \\
\mathbf{C} & \mathbf{D}
\end{array}\right)
$$

### 2.6 Binary Tree Representation of the 4 clusters

Principal dimensions define the binary tree in any dimension reduction approach, in particular in TCA of extremely sparse data set.

Based on the first principal dimension, we represent the matrix $\mathbf{B}_{4}$ as a binary tree with 2 nodes

$$
\mathbf{B}_{4} \equiv\left(\begin{array}{ll}
\mathbf{N} & \\
& \mathbf{P}
\end{array}\right)
$$

where $\mathbf{N}$ represents the subtable representing the rows and the columns on the left side in Figure 2, and $\mathbf{P}$ represents the subtable representing the rows and the columns on the right side in Figure 2.

Based on the second principal dimension, we represent the matrix $\mathbf{B}_{4}$ as a binary tree with 4 nodes



Figure 3: TCA contribution map of dimensions 1 \& 2 .

$$
\mathbf{B}_{4} \equiv\left(\begin{array}{cccc}
\mathrm{NN} & & & \\
& \mathrm{NP} & & \\
& & \mathbf{P N} & \\
& & & \mathbf{P P}
\end{array}\right)
$$

## 3 The analysis of the binary data of $(40+1)$ texts

We follow exactly the same process in the analysis-visualization of the corpus of $(40+1)$ DTM data; where 40 represents the number of diverse Israeli interviewees and 1 the DOI text.

### 3.1 General statistics

The original presence/absence $(0 / 1)$ data set of size $1730 \times 343$, where 1730 represents the number of phrases in $(40+1)$ texts and 343 the number of distinct words (or terms). It has 70 rows with 0 marginal counts; by deleting them, we obtain the $(0 / 1)$ matrix $\mathbf{Z}$ of size $1660 \times 343$, whose apparent sparsity index is $98.72 \%$. By Benzécri's principle of distributional equivalence $\mathbf{Z}$ is equivalent to the contingency table $\mathbf{N}$ of size $1605 \times 343$ with the sparsity index of $98.68 \%$. Table 3 represents a comparison of the row and column marginals of $\mathbf{Z}$ and $\mathbf{N}$; where we notice that the number of hapaxes in $\mathbf{Z}$ is 169 , slightly more than twice 83 , the number of hapaxes in $\mathbf{N}$.

Table 3 : CA equivalent data sets $\mathrm{Z}$ and $\mathrm{N}$ of $(40+1)$ texts.

|  | row marginals of $\mathbf{Z}$ of size $1660 \times 343$ |  |  |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| values | 1 | 2 | 3 | 4 | 5 | 6 | 7 | $[9: 17]$ |
| counts | 169 | 238 | 303 | 268 | 239 | 133 | 114 | 196 |
|  | row marginals of $\mathbf{N}$ of size |  |  |  |  |  |  | $1605 \times 343$ |
| values | 1 | 2 | 3 | 4 | 5 | 6 | 7 | $[9: 17]$ |
| counts | 83 | 254 | 311 | 274 | 239 | 134 | 114 | 196 |
| summary of column marginals of $\mathbf{Z}$ or $\mathbf{N}$ |  |  |  |  |  |  |  |  |
|  | Min | $\mathrm{Q}_{1}$ | Median | Mean | $\mathrm{Q}_{3}$ | Max |  |  |
| values | 7 | 12 | 15 | 21.31 | 24 | 143 |  |  |



Figure 4: CA principal map of $\mathbf{Z}$.

### 3.2 Correspondence Analysis of $\mathrm{N}$ or $\mathrm{Z}$

Figure 4 displays the principal map of the 343 columns (words) obtained from $\mathbf{C A}$ of $\mathbf{N}$ or $\mathbf{Z}$, which is difficult to interpret. However, by checking in Table 4 the singular values $\rho$, the correlation coefficients of the row and column factor scores, we note that they are quite high, the first few around 0.7 ; which shows that there is some underlying structure which appears by using TCA.

Table 4 : CA dispersion values of the first 4 principal axes.

|  | Axis |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :---: |
| data set | $\rho_{1}$ | $\rho_{2}$ | $\rho_{3}$ | $\rho_{4}$ |  |
| $\mathbf{Z}$ or $\mathbf{N}$ | 0.731 | 0.693 | 0.676 | 0.674 |  |
| DataPosPos | 0.812 | 0.797 | 0.790 | 0.786 |  |
| DataPosNeg | 0.907 | 0.902 | 0.870 | 0.836 |  |
| DataNegNeg | 0.866 | 0.848 | 0.842 | 0.830 |  |
| DataNegPos | 0.862 | 0.846 | 0.836 | 0.832 |  |



Figure 5: TCA principal map of $\mathbf{Z}$.

### 3.3 Taxicab Correspondence Analysis of $\mathrm{N}$ or $\mathrm{Z}$

Figure 5 displays the principal map of the 343 columns (words) obtained by TCA of $\mathbf{N}$ or $\mathbf{Z}$; where we see clearly 4 clusters. Some elementary statistics of TCA of $\mathbf{N}$ are provided in Table 5. The QSR values of axis 1 are quite low $[(17.0,25.2),(-30.6,-38.8), 25.5]$, which imply that these 4 clusters are quite heterogeneous given the high sparsity value $(98.68 \%)$ of N.

In Figure 5, there are 4 major clusters of words in 4 quadrants, that we designate by $(\operatorname{sign} 1, \operatorname{sign} 2)$, where $\operatorname{sign}=$ Pos or Neg.

We name the subset of the contingency table $\mathbf{N}$ which corresponds to the cluster in the upper right quadrant by DataPosPos. Similarly, we name the 3 remaining subsets of $\mathbf{N}$ by DataPosNeg (corresponding to th lower right
cluster), and DataNegPos and DataNegNeg. In the following sections we study these 4 subsets.

## 4 CA of each of the 4 data subsets

Here we enumerate some important points of $\mathrm{CA}$ of the 4 datasets DataPosPos, DataPosNeg, DataNegPos and DataNegNeg.

a) The size and sparsity index of each of these 4 datasets are displayed in Table 5, where we see that they are extremely sparse more than $96 \%$.

b) Similar to the CA map of $\mathbf{N}$ or $\mathbf{Z}$ (Figure 4), the CA map (not shown) of each of these 4 datasets is difficult to interpret.

c) However, there is a lateral ordering in each of these 4 datasets, because the first singular values are close or larger than Benzécri's empirical criterion of 0.835 , as can be seen in Table $4: 0.812,0.907,0.866$ and 0.862 .

## 5 TCA of each of the 4 data subsets

TCA numerical results of the 4 datasets DataPosPos, DataPosNeg, DataNegPos and DataNegNeg, are summarized in the Tables 5 through 9, and TCA maps are shown in Figures 6 through 9. Given that the analysis of each of these 4 datasets are very similar, so we present only the analysis of the dataset DataPosPos, then we conclude.

### 5.1 TCA of DataPosPos

Figure 6 displays the principal map of the 106 words in the subset DataPosPos, where clearly we notice 4 clusters. Table 5 displays some TCA statistics : We note that these QSR and dispersion $\delta_{\alpha}$ values are uniformly higher in absolute value than the corresponding values of TCA of $\mathbf{N}$ or $\mathbf{Z}$ shown in Table 5; which imply that the subset DataPosPos is much more structural than the set $\mathbf{N}$ or $\mathbf{Z}$. We designate the 4 subsets of DataPosPos by DataPosPos(sign1,sign2), where sign $=$ Pos or Neg. So we have 4 subsubsets named :

DataPosPos $(\operatorname{Pos}, \mathrm{Pos})=$ DataPPPP,

DataPosPos $(\mathrm{Pos}, \mathrm{Neg})=$ DataPPPN,

DataPosPos(Neg,Neg $)=$ DataPPNN,

DataPosPos(Neg,Pos $)=$ DataPPNP.

Table 5 : TCA QSR (\%) values of the first 2 dimensions .

| $\mathbf{4 0 + 1 )}$ | texts of size $1605 \times 343$, sparsity $=98.68 \%$ |  |  |  |
| :--- | :--- | :--- | :--- | :--- |
| Axis $\alpha$ | $Q S R_{\alpha}\left(V_{+} U_{+}, V_{-} U_{-}\right)$ | $Q S R_{\alpha}\left(V_{-} U_{+}, V_{+} U_{-}\right)$ | $Q S R_{\alpha}$ | $\delta_{\alpha}$ |
| 1 | $(17.0,25.2)$ | $(-30.6,-38.8)$ | 25.5 | $\mathbf{0 . 4 9 5}$ |
| 2 | $(16.7,19.5)$ | $(-25.3,-27.1)$ | 21.4 | $\mathbf{0 . 4 8 5}$ |

DataPosPos of size $431 \times 106$, sparsity $=97.13 \%$

| Axis $\alpha$ | $Q S R_{\alpha}\left(V_{+} U_{+}, V_{-} U_{-}\right)$ | $Q S R_{\alpha}\left(V_{-} U_{+}, V_{+} U_{-}\right)$ | $Q S R_{\alpha}$ | $\delta_{\alpha}$ |
| :--- | :--- | :--- | :--- | :--- |
| 1 | $(22.2,30.2)$ | $(-42.7,-55.5)$ | 33.4 | $\mathbf{0 . 6 2 4}$ |
| 2 | $(25.5,19.3)$ | $(-31.6,-33.5)$ | 26.2 | $\mathbf{0 . 5 9 1}$ |

DataPosNeg of size $418 \times 78$, sparsity $=96.78 \%$

| Axis $\alpha$ | $Q S R_{\alpha}\left(V_{+} U_{+}, V_{-} U_{-}\right)$ | $Q S R_{\alpha}\left(V_{-} U_{+}, V_{+} U_{-}\right)$ | $Q S R_{\alpha}$ | $\delta_{\alpha}$ |
| :--- | :--- | :--- | :--- | :--- |
| 1 | $(26.3,28.8)$ | $(-48.0,-60.6)$ | 36.3 | $\mathbf{0 . 6 7 6}$ |
| 2 | $(19.4,30.4)$ | $(-32.8,-46.2)$ | 29.3 | $\mathbf{0 . 6 5 7}$ |

DataNegNeg of size $383 \times 77$, sparsity $=97.13 \%$

| Axis $\alpha$ | $Q S R_{\alpha}\left(V_{+} U_{+}, V_{-} U_{-}\right)$ | $Q S R_{\alpha}\left(V_{-} U_{+}, V_{+} U_{-}\right)$ | $Q S R_{\alpha}$ | $\delta_{\alpha}$ |
| :---: | :---: | :---: | :---: | :---: |
| 1 | $(32.7,23.3)$ | $(-64.3,-46.0)$ | 36.1 | 0.671 |
| 2 | $(19.8,30.1)$ | $(-30.9,-41.8)$ | 28.6 | 0.663 |
| DataNegPos of size $373 \times 82$, sparsity $=96.9 \%$ |  |  |  |  |
| Axis $\alpha$ | $Q S R_{\alpha}\left(V_{+} U_{+}, V_{-} U_{-}\right)$ | $Q S R_{\alpha}\left(V_{-} U_{+}, V_{+} U_{-}\right)$ | $Q S R_{\alpha}$ | $\delta_{\alpha}$ |
| 1 | $(22.6,33.4)$ | $(-45.5,-68.3)$ | 36.1 | 0.687 |
| 2 | $(19.2,31.6)$ | $(-33.7,-51.9)$ | 30.2 | 0.653 |



Fig. 6: TCA map of DataPosPos.

The interpretation of the 4 clusters (as topics) in Figure 6 are outlined in Table 6 by the words that contribute the most. To have a fuller understanding of a topic composed of few words, one has to read the phrases in which these words are found, as we applied in section 2 of DOI text analysis. We explain this on the cluster DataPPPP, whose 23 columns (words or terms) are plotted in the upper right quadrant of Figure 6.

### 5.1.1 Columns that contribute the most

Here are the 23 column labels ordered according to their contributions to the principal plane (in parenthesis) :

activity (0.479); favor (0.480); kind (0.481); allows (0.639);

according (0.639); side (0.639); components(0.799);

nation-state $(0.799)$; accept $(0.800)$; struggle $(0.959)$;

view $(0.959)$; actually $(0.959)$; talk $(0.959)$; concept $(0.960)$;

life $(1.12)$; peace $(1.12)$; clear (1.12) ; majority (1.60);

population $(1.76)$; identity $(1.92)$; democracy $(2.88)$; israeli (3.04) ; jewish (7.03)

### 5.1.2 Rows that contribute the most

Among the 106 phrases, here are the 6 rows (phrases) that contribute the most to the principal plane (in parenthesis) :

R1020 (2.72) : Interviewee 23, phrase 4 : A genuine peace with open borders that will attract millions of people from all nations creates a challenge and a strategic threat of being overtaken by others - a possible consequence of peace. And therefore, the lack of peace protects us from being flooded by foreigners and allows the Jewish-Zionist-Israeli state to prepare for peace.

R489 (2.68) : Interviewee 11, phrase 7 : From the Ultra-Orthodox aspect,this is a deal that has only one side : if we were afraid to integrate into the military, academia, work, in the Israeli sphere, so as not to lose our Ultra-Orthodox identity, an opportunity was created that we were willing to accept us.

R906 (2.65) : Interviewee 18, phrase 20 : The majority of the Ultra-Orthodox community "lives in peace" with "Jewish and democratic."

R450+R871 (2.65) : Interviewee 10(+17), phrase 20(+25) : Both Jewish and democratic (Jewish- Democratic was initially seen as a contrast, the "hyphen" should be clarified.)

R295 (2.04) : Interviewee 8, phrase 12 : What has been clearly forming over the past 100 years is the Jewish-Israeli group, which has clear common identity characteristics, despite the various groups within it (Ultra-Orthodox, etc.).

R1700 (2.03) : Interviewee 40, phrase 44 : We need to abandon our zero-sum game struggle with Iran that does not lead to a positive, clear and practical solution, and find a different, creative approach of regional understandings to learn perhaps from the Emirates who know how to be at peace with both the Americans and Iran! A "both" solution!

### 5.1.3 Interpretation

We see that the core of this cluster concerns Jewish-Israeli (10.07) society or state, and its characterization with the three words democracy (2.88), identity (1.92) and peace (1.12). Furthermore, democracy and identity pertain to the ultra-orthodox community; while peace pertains within the society or with the neighboring or enemy states like Iran.

This shows that the interpretation of a collection of words to represent a topic depends on the context used in a collection of phrases ("environment"); this is the fundamental structural concept of distributional analysis advanced by the linguist Harris, whom Benzécri (1966, subsection 4.2, page 336) cites "The distribution of an element will be understood as the sum of all its environment" and adds "l'originalité de Harris est d'opérer systématiquement sur un corpus (ou un texte unique) sans essayer de fabriquer des exemples selon les besoins, ni de considérer le sens"; that is "The originality of Harris is to act on a given corpus or a unique text". Then Benzécri compares his principle of distributional equivalence on which he developed the mathematics of CA and Harris's distributional analysis concept.

Table 6 : Summary of DataPosPos and its 4 clusters (topics).

|  | size |
| :---: | :---: |
| DataPosPos | sparsity $=97.13 \%$ |
| DataPPPP | sparsity $=91.63 \%$ |
| TopicPPPP | jewish,Israli,democracy,identity,peace, |
| Dat: | sparsity $=94.23 \%$ |
| Topi | Prime minister,promote,give,,contribute,discourse, <br> arrangements,solution,right,minority,two |
| Dat | sparsity $=93.57 \%$ |
| Topic | ration of inde |
| DataPPNP <br> TopicPPNP | $93 \times 13 \quad$ sparsity $=86.85 \%$ <br> state-of-israel.separation,role,judaism.zionis |



Fig.7: TCA principal map of DataPosNeg.

Table 7 : Summary of DataPosNeg and its 4 clusters (topics).

|  | size |
| :---: | :---: |
| DataPosNeg | sparsity $=96.78 \%$ |
| DataPNPP | sparsity $=91.63 \%$ |
| TopicPNPP | ultra-orthodox, haredim,integration,israeli society, <br> community,jews,arabs |
| DataPNPN | sparsity $=91.44 \%$ |
| TopicPNPN | Israel,military,army,service,issue,approach, <br> ultra-orthodox,arab |
| DataPNNN | sparsity $=89.47 \%$ |
| TopicPNNN | Palestinians,conflict,Middle-East,Iran,Arab |
| DataPNNP <br> TopicPNNP | $106 \times 23$ sparsity $=91.22 \%$ <br> society,countries,must,live,together,covenant,destiny  |



Fig. 8: TCA principal map of DataNegNeg.

Table 8 : Summary of DataNegNeg and its 4 clusters (topics).

|  | size |
| :---: | :---: |
| DataNegNeg | sparsity $=96.6 \%$ |
| DataNNPP | sparsity $=90.3 \%$ |
| TopicNNPP | important,security,deal,maintain,periphery,true, <br> public,cultural |
| DataNNPN | sparsity $=84.1 \%$ |
| TopicNNPN | education,system,personal,health,economics, <br> market,enable |
| DataNNNN | sparsity $=92 \%$ |
| TopicNNNN | economic,change,process,strong,power,basis |
| DataNNNP | sparsity $=92.8 \%$ |
| TopicNNNP | crisis,world,coronavirus,global,processes |



Fig.9: TCA principal map of dataNegPos.

Table 9 : Summary of DataNegPos and its 4 clusters (topics).

|  | siz |
| :---: | :---: |
| DataNegPos | sparsity $=96.9 \%$ |
| DataNPPP | sparsity $=92.6 \%$ |
| TopicNPPP | zionism,organizing-principle,constitution, <br> religious, ben gurion,mamlachtiutt |
| DataNPPN | sparsity $=92.5 \%$ |
| TopicNPPN | today,changes,large,past,story,act,sense, <br> make,able,lead,key,things,changing, |
| DataNPNN <br> TopicNPNN | $69 \times 14$ sparsity $=88.7 \%$ <br> ability,government,requires,longterm,planning  |
| DataNPNP <br> TopicNPNP | $79 \times 17$ sparsity $=89.8 \%$ <br> current,situation,leadership,difficult,time,level  |

### 5.2 Binary tree structure of the $(40+1)$ texts

Tables 6 through 9 show the existence of 16 clusters which we represent in a complete binary tree with four levels, see Table 10, each level represents the division of a subset of the data set by a principal dimension.

Table 10 : Binary tree of TCA of $(40+1)$ texts.

| level 4 | level 3 | level 2 | level 1 |
| :---: | :---: | :---: | :---: |
| PPPP | PPP | PP | P |
| PPPN |  |  |  |
| PPNP | PPN |  |  |
| PPNN |  |  |  |
| PNPP | PNP | PN |  |
| PNPN |  |  |  |
| PNNP | PNN |  | N |
| PNNN |  |  |  |
| NPPP | NPP | NP |  |
| NPPN |  |  |  |
| NPNP | NPN |  |  |
| NPNN |  |  |  |
| NNPP | NNP | NN |  |
| NNPN |  |  |  |
| NNNP | NNN |  |  |
| NNNN |  |  |  |

## 6 Adjusted sparsity index

We attempt to shed further light on the following observation : How come CA and TCA maps were interpretable of the DOI corpus, while the CA maps were difficult to interpret (respectively the TCA maps were easily interpretable) of the (40+1) corpus and its 4 subsets? Here we introduce the adjusted sparsity index which may be helpful to understand this fact based on some elementary basic results of Choulakian (2017) concerning CA and TCA of sparse data tables. We remind the reader that the influence of rare observations in CA is still an active area of research ; see in particular Nowak and Bar-Hen (2005), Greenacre (2013) and Lebart (2024).

Definition : A contingency table $\mathbf{N}$ of size $I \times J$ with only non-zero marginals is named sparsest if its sparsity in \% equals $100(1-1 / \min (I, J))$; and extremely sparse if its sparsity is very near to $100(1-1 / \min (I, J))$.

Note that in the above definition : First, the word sparsity means the real sparsity of a data set computed after applying Benzécri's principle of distributional equivalence and not the apparent sparsity. Second, The sparsest $(\mathrm{I}, \mathrm{J})$ tables are the tables of rank $\min (\mathrm{I}, \mathrm{J})$ with exactly $\min (\mathrm{I}, \mathrm{J})$ non-zero entries. This means the sparsest tables are such that by permuting the rows and the columns they become square diagonal data sets. Third, we define for a given data set $\mathbf{N}$



Table 11 provides a numerical summary of the 4 terms that appear in the above definition concerning the 6 data sets which we analyzed in this paper by CA and TCA; we also added the SACRED data set discussed by Choulakian and Allard (2023). In Table 11, among the 7 data sets, only the CA map of the first data set (DOI) was interpretable, while the CA maps of the last 6 data sets were difficult to interpret. So based on Table 11, we conjecture the following : Let $\mathbf{N}$ be a real data set that does not have an underlying structure of blocks diagonal form, that is, the CA singular values are strictly smaller than 1; then: The CA maps are difficult to interpret if adjusted sparsity $(\mathbf{N}) \geq \mathbf{9 8} \%$.

Table 11 : The adjusted sparsity values of the 7 data sets.

| data set | size | sparsity $\%$ | upper boundary $\%$ | adjusted sparsity(N) $\%$ |
| :---: | :---: | :---: | :---: | :---: |
| DOI | $15 \times 21$ | 88.25 | 93.33 | $\mathbf{9 4 . 5 5}$ |
| $(40+1)$ | $1605 \times 343$ | 98.68 | 99.71 | 98.9 |
| DataPosPos | $431 \times 106$ | 97.13 | 99.06 | 98.06 |
| DataPosNeg | $418 \times 78$ | 96.78 | 98.72 | 98.04 |
| DataNegNeg | $383 \times 77$ | 97.13 | 98.70 | 98.4 |
| DataNegPos | $373 \times 82$ | 96.9 | 98.78 | 98.10 |
| SACRED | $589 \times 4864$ | 98.65 | 99.83 | 98.8 |

## 7 Conclusion

In the early 1960 's, Benzécri developed CA specially for textual data analysis; he considered the interpretability of the numerical outputs via maps the most essential aspect of CA. We followed his approach in this paper, where we focused on the interpretability of the numerical outputs via maps and the interpretation of the anchor words (words that contribute the most to the principal plane) in a cluster by choosing the phrases that contribute the most to the creation of that cluster.

We summarize our results of this paper on the application of CA and TCA on extremely sparse nonnegative data sets :

a) We presented the joint use of CA and TCA in the analysis-visualization of 2 data sets of different sizes : DOI text of small size (almost the size of an ordinary poem) and (40+1) texts (almost the size of an ordinary collection of poems).

b) TCA was able to reveal the underlying structure of extremely sparse textual data sets as binary trees.

c) We attempted to shed further light on the interpretability of the CA maps by the introduction of the adjusted sparsity index of a sparse data set.

Finally, we provide here an approach for integrating unstructured data from different sources. This capability is becoming essential, for example, in the analysis of textual data scraped from social media and transliterations of text in call center recordings. In a long term perspective, the analysis of big data requires an ability to integrate unstructured data with images, voice and sensor based technologies. Here we handle nominal values captured by a document term matrix.

## Acknowledgement

Choulakian's research has been supported by the Natural Sciences and Engineering Research of Canada (Grant no. RGPIN-2017-05092).

## References

Allard J, Choulakian V (2019) Package TaxicabCA in R

https ://CRAN.R-project.org/package=TaxicabCA

Benzécri JP (1966) Linguistique et mathématique. Revue Philosophique de la France et de l'Étranger, 156, pp. 309-374

Benzécri JP (1981) Pratique de L'Analyse Des Données : Volume 3, Linguistique \&3 Lexicologie. Dunod

Choulakian V (2017) Taxicab correspondence analysis of sparse two-way contingency tables. Italian Journal of Applied Statistics, 29 (2-3), 153-179

Choulakian V, Kasparian S, Miyake M, Akama H, Makoshi N, Nakagawa M (2006) A Statistical Analysis of the Synoptic Gospels. Journées internationales d'Analyse statistique des Données Textuelles, $8: 281-88$

Choulakian V, Allard J (2023) Visualization of extremely sparse contingency table by taxicab correspondence analysis : A case study of textual data. Available at https ://arxiv.org/pdf/2308.03079.pdf

Greenacre, M. (2013). The contributions of rare objects in correspondence analysis. Ecology, 94(1) : 241-249

Greenacre M, Nenadic O, Friendly M (2022) Package ca in R

https ://CRAN.R-project.org/package=ca

Kenett RS, Gal R, Adres E, Ali N, Glickman H (2023) The Israeli society common denominator : a text analytic study. Israel Affairs, pp 1-11, DOI : $10.1080 / 13537121.2023 .2206250$

Lebart L (2024) Low lexical frequencies in textual data analysis. In Beh, Lombardo, Clavel (eds): Analysis of Categorical Data from Historical Perspectives : Essays in Honour of Shizuhiko Nishisato, pp 319-334, Springer.

https ://doi.org/10.1007/978-981-99-5329-5_19

Nowak E, Bar-Hen A (2005) Influence function and correspondence analysis. Journal of Statistical Planning and Inference. 134 : 26-35

Qi Q, Hessen DJ, Deoskar T, van der Heijden PGM (2023) A comparison of latent semantic analysis and correspondence analysis of document-term matrices. Natural Language Engineering, pp 1-31, doi :10.1017/S135132492300024

## Appendix

Table 0: Contingency table $\mathbf{N}$ of size $18 \times 24$.


Figure 0: CA map of the 4 blocks.

