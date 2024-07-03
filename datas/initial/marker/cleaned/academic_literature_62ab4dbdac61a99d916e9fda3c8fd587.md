# Finding Stable Price Zones In European Electricity Markets: Aiming To Square The Circle?

Teodora Dobosa,∗, Martin Bichlera, Johannes Kn¨orra a*School of Computation, Information and Technology, Technical University of Munich, Boltzmannstrasse* 3, Garching, 85748, Germany

## Abstract

arXiv:2404.06489v1 [econ.GN] 9 Apr 2024 The European day-ahead electricity market is split into multiple bidding zones. Within these zones, a uniform energy price is computed for each hour. Large bidding zones have been under scrutiny. The fact that zonal clearing ignores the transmission capacities within zones and the increase in renewables lead to a growing number of interventions in the generation of energy sources and large redispatch costs. The European Union Agency for the Cooperation of Energy Regulators
(ACER) proposed alternative bidding zone configurations that should be analyzed as part of the Bidding Zone Review. For Germany, four alternative configurations were suggested. Bidding zones shall be stable and based on long-term, structural congestion in the grid. We analyzed the proposed configurations considering different clustering algorithms and periods. We found that the configurations do not reduce the price standard deviations within zones considerably, while the average prices across zones are similar. Other configurations identified based on clustering prices lead to lower price standard deviations but are not geographically coherent. Importantly, different configurations emerge depending on clustering features, algorithm, and period considered. Given the substantial changes in energy supply and demand that can be expected in the future, defining stable configurations appears to be a moving target.

Keywords: Energy pricing, Price zones, Bidding Zone Review, Electricity markets, Energy policy 1

## 1. Introduction

The European electricity market is split into multiple bidding zones (BZs), aka. price zones. Within these zones, market participants can submit bids and offers, which are subsequently matched without considering the capacities of the transmission network.1 BZs are generally defined depending on national borders, such that a country represents a single bidding zone (e.g., France and Poland). However, there are also countries that are divided into several BZs, such as Norway, Sweden and Italy, or BZs that consist of more than one country, like the German-Luxembourgish bidding zone.

An important characteristic of BZs is that in the day-ahead market, they implement a *uniform* pricing mechanism, meaning that a single market-clearing electricity price applies to all participants belonging to a BZ. A uniform price in a BZ promotes transparency due to a simple single price signal in a large region, and it limits the market power that individual parties can exercise. However, a uniform electricity price also leads to significant negative ramifications. There are no local incentives to adapt to changes in the volatile supply of renewables, there are significant welfare losses due to the uniform price constraint, and large redispatch costs. The latter is because transmission constraints are ignored within a BZ when supply is matched with demand (Energywende 2018),
and the market-based allocation is not physically feasible. In addition, uniform prices do not set appropriate investment incentives.

The German-Luxembourgish BZ is a case in point. Strong winds along the North Sea and Baltic Coast often contribute to elevated power production from wind farms in Northern Germany.

The energy produced in the north must be transported to the main power consumption areas, which are located in the south and west of the country. However, the transmission lines connecting these regions often become congested and thus electricity cannot be delivered as determined in the day-ahead market. To stabilize the grid, redispatch by the Transmission System Operators (TSOs) is required. TSOs often need to throttle the generation of Northern conventional and wind power plants. At the same time, they instruct power plants in the south to increase energy production. Such redispatch actions incur substantial costs. In 2022, the redispatch costs in Germany were 4.2 2

## Billion Euros.2

Furthermore, the lack of sufficient transmission lines in the German grid caused problems in neighboring countries. Poland and the Czech Republic have installed phase-shifters at their borders with Germany to reduce loop flows in their networks.3 These loop flows lead to suboptimal crosszonal trading opportunities and are a negative consequence of the large German bidding zone and its limited transmission grid.

Given these considerations, in August 2022 the European Union Agency for the Cooperation of Energy Regulators (ACER) decided that alternative bidding zone configurations should be analyzed as part of the Bidding Zone Review (BZR), which is organized by the European Network of Transmission System Operators for Electricity (ENTSO-E 2023). The goals of the BZR are described on a high level in different documents. According to Commission Regulation (EU) 2015/1222 and 2019/943, bidding zones "should be defined in a manner to ensure efficient congestion management and overall market efficiency" (Commission 2015) and "shall be based on long-term, structural congestions in the transmission network" (Commission 2019).

Annex I of ACER's decision on alternative bidding zone configurations to be considered in the bidding zone review process (ACER 2022a) describes that different configurations were identified by solving a clustering problem "*based on nodal prices as clustering feature*". The document argues that nodal prices "can be used as proxies for economic efficiency, in line with the objectives of the Electricity Regulation", and that the objective of clustering algorithms is to "minimize price dispersion within each bidding zone." The document discusses three clustering algorithms: constrained K-Means clustering, Spectral Clustering with constrained K-Means, and Spectral Clustering with Constrained Deterministic Iterative Refinement Clustering (CDIRC). Moreover, a constraint related to the minimum size of each zone was included.4 Based on this ACER methodology (ACER 2020), TSOs were tasked to calculate locational marginal prices (essentially, a nodal price for each substation in the transmission grid5) for the 3 target year 2025, for which generation and demand scenarios were created. These scenarios originate from ENTSO-E's Data & Models working group. Weather data from 1989, 1995, and 2009 was used to create scenarios for representative reference climate years. The grid model, the demand, the generation capacities, and prices for gas, coal and CO2 were based on predictions for 2025. ENTSO-
E computed nodal prices for the respective weeks in a report published in June 2022 (ENTSO-E
2022). As outlined above (ACER 2022b), the time series of nodal prices represented the clustering features that were used to partition the set of nodes in the transmission network into a predefined number of clusters or BZs. A BZ configuration or a clustering thus represents the assignment of every node to a specific cluster or price zone. Finally, ACER suggested four alternative bidding zone configurations for Germany ACER (2022a) based on the results from the Locational Marginal Pricing (LMP) Study (ENTSO-E 2022, 2023). The evaluation of these configurations proposed by ACER in the BZR is ongoing at the time of writing. In this process, the TSOs are evaluating 22 indicators related to market efficiency, network security, and the *stability and robustness* of the proposed configurations (ACER 2020).

In this paper, we leverage the data provided by ENTSO-E and study how stable and robust the configurations of price zones (or, clusterings) proposed by ACER are with respect to different time frames, different inputs (i.e., nodal prices with or without geographic coordinates), and different clustering algorithms. We define three criteria for analyzing clustering stability and robustness and conduct a thorough empirical evaluation of the suggested configurations using the data published by ENTSO-E. Following ACER's methodology, we implement K-Means and Spectral Clustering and evaluate the clusterings computed with these methods. We want to understand if the clustering algorithms compute the same clusters when nodal prices of different time periods are considered.

How different are clusters resulting from different clustering algorithms? Also, how similar are the clusters of a particular configuration with respect to prices, and how large are the price standard deviations within clusters?

We find that the configurations proposed by ACER are not stable across time and algorithm used. Moreover, the configurations do not reduce the price standard deviations within zones considerably, and the average prices between zones are similar. If we recompute the clusters and take only prices into account6, we can reduce the price standard deviation within clusters more. However, these alternative clusters are not of equal size and are not geographically coherent. Importantly, neither the configurations proposed by ACER nor the clusters that we computed are stable across time. Depending on the time frame taken into account, different clusterings would result. Note that our analysis is performed based on the same target year 2025 as in the BZR. Given the significant changes in supply and demand and in the weather over time, we can expect substantial changes in the supply in future years. In particular, Germany has ambitious goals concerning the share of renewable energies and aims for 80% in 2030.7 There is a danger that even if a good configuration is selected for 2025, it might be outdated soon after.

This paper is structured as follows. In Section 2 we discuss the literature related to our work, while in Section 3 we describe the algorithms we implement to compute clusterings and introduce the metrics considered to evaluate stability. The data we use in our experiments is discussed in Section 4, while the experimental results are presented in Section 5. Finally, we summarize our main findings and their policy implications in Section 6.

## 2. Related Literature

This paper complements existing literature computing bidding zone configurations. In particular, we draw on a unique data set with LMP prices that is provided by ENTSO-E. Bovo et al. (2019) identifies the main network indicators that should be considered for defining suitable bidding zone configurations. LMPs and power transfer distribution factors (PTDFs) represent such indicators. While some papers focus on identifying configurations by clustering PTDFs (e.g., (Kumar et al. 2004) and (K los et al. 2014)), most works use LMPs as clustering features (Stoft 1997).

Burstedde (2012) computes LMPs for the scenario years 2015 and 2020 considering a simplified 72-node representation of the European grid, and evaluates the shapes and sizes of the zones obtained by clustering these LMPs using hierarchical clustering. Breuer et al. (2013) implement a 5 genetic algorithm and apply it on a dataset consisting of 380 kV nodes considering a projected system for 2016 and 2018. Based on six scenarios, Felling & Weber (2018) compute robust price zone configurations for Central Western Europe by employing hierarchical clustering based on the LMPs of approximately 2,200 nodes and assigning weights to nodes depending on their demandand supply situation. These configurations are robust in the sense that LMPs from multiple scenarios are integrated into their computation. Considering a network model consisting of around 2,700 nodes, Brouhard et al. (2023) design nine zone delineations for Continental Europe by implementing K-Means and hierarchical clustering. The authors calculate LMPs for multiple, independent singleperiod optimization problems (i.e., optimal power flow with direct current approximation), and use geographic coordinates and these prices as clustering features. Sarfati et al. (2015) introduce five indicators to assess the impact of bidding zone configurations in zonally-priced electricity markets.

The indicators include commercial exchange and welfare evolution, as well as price convergence and divergence, and were analyzed on the Nordic 32-bus example system.

In terms of the German-Luxembourgish bidding zone, Zinke (2023) identifies north-south splits using hierarchical clustering based on the LMPs associated to approximately 500 nodes that are computed within a linear market and grid model for four scenario years. The author considers uncertain factors such as short-term weather patterns and long-term system changes to evaluate the potential decrease in redispatch costs resulting from such splits. Moreover, Ambrosius et al. (2020) consider a scenario for the year 2035 and determine welfare-maximizing price zones and available transfer capacities for a simplified representation of the German market area consisting of 28 nodes. Such zones are identified based on a mixed-integer nonlinear model that incorporates a graph partitioning problem on the first level. The prior literature used different data sources for these analyses.

## 3. Methodology

The process of computing price zones can be reduced to solving a clustering problem. Formally, given a set of N D-dimensional data points X = {x1, x2*, ..., x*N } with xi ∈ R
D and a number of clusters k, the objective of the clustering problem is to find for each point xi the corresponding assignment zi ∈ {1*, ..., k*} to one of the k clusters such that (1) points within the same cluster are similar to each other and (2) points between different clusters are dissimilar from each other. A
clustering is a solution to this problem and is denoted by C = {C1*, . . . , C*k}, where Ci = {xj : zj = i}
is a cluster. The centroid of a cluster Ciis defined as the mean of the data points assigned to Ci and is depicted by ci. In our setting, the data points are the nodes in the transmission network and the dimensions represent the features we use to compute clusters (see Section 4.1).

## 3.1. Clustering Algorithms 7

Following ACER's approach to identify alternative price zone configurations, we consider two clustering algorithms in this paper. ACER used three clustering approaches (ACER 2022b), i.e.,
K-Means, Spectral Clustering with constrained K-Means and Spectral Clustering with CDIRC,
but the implementation details are not publicly available. Therefore, it is impossible to reproduce the exact algorithmic configuration ACER implemented. Instead, we consider the same family of clustering methods to evaluate alternative price zone configurations. In what follows, we briefly describe the clustering algorithms we implement.

## 3.1.1. K-Means

K-Means (Lloyd 1982) is a simple algorithm that clusters data points by minimizing withincluster variances, i.e., squared Euclidean distances. The method consists of three main steps. In the first step, the centroids are initialized randomly. In the second step, each data point is assigned to its nearest centroid with respect to the Euclidean distance, specifically to its corresponding cluster.

The third step consists of updating the centroids, given the new points assigned to the clusters.

The last two steps are repeated until the difference between the old and the new centroids is below a threshold. Importantly, the final clusters might differ depending on the initialization of centroids.

A constrained version of K-Means was considered in the BZR analysis (ACER 2022b), in which the centroids are initialized such that they are spread out spatially. We note that this version of K-Means is known as K-Means++ (Arthur & Vassilvitskii 2007). We implement the constrained version of K-Means by Bennett et al. (2000) and incorporate constraints for the minimum size of points included in each cluster. We update the clusters until the squared Euclidean distance between each old and new centroid is smaller than 0.1. Moreover, we standardize the data such that all features have a mean of 0 and a standard deviation of 1.

## 3.1.2. Spectral Clustering

Spectral clustering is a technique used for clustering network data. Given a graph G = (*V, E*),
the method clusters the set of vertices V based on a low-dimensional spectral embedding of G and consists of three main steps. First, the Laplacian matrix L is constructed. Then, the first r eigenvectors (i.e., the eigenvectors corresponding to the r smallest eigenvalues of L) are computed.

In the last step, a matrix X˜ ∈ R
n×ris considered, whose columns are the selected eigenvectors and the i-th row is an embedding of the i-th node in G. The graph nodes are then clustered by applying, e.g., K-Means on the node embeddings. We refer to Aggarwal & Wang (2010) for a comprehensive overview of Spectral Clustering.

For our setting, we define a complete graph G in which V is the set of nodes considered in the BZR analysis. We set the weight we of an edge e = (*u, v*) ∈ E as the similarity between nodes u and v and compute it using the radial basis function kernel. Thus, with xu, xv denoting the features corresponding to nodes u and v, respectively, we define we = exp(−
∥xu−xv∥
2 2σ2 ), where σ is a parameter that controlls the width of node-neighborhoods. We normalize the edge weights such that we ∈ [0, 1] for all e ∈ E and set σ = 1. To cluster the nodes using X˜ ∈ R
n×r, we apply the constrained version of K-Means mentioned in Section 3.1.1. Moreover, we set r = k and thus consider the first k eigenvectors as clustering features.

## 3.2. Stability Evaluation

In what follows, we discuss three criteria that we consider to evaluate the stability of pricing zones. Given a period t and a node x, we denote by x tthe vector containing the time series of prices corresponding to x in period t. We define x t as the average price of node x in period t, which is simply the average over all values in x t. We also denote the distance between two points x and y in period t by d t(*x, y*) and define it as d t(*x, y*) = |x t − y t|. Whenever the period we are referring to is evident, we simplify notation by omitting the reference to t in d t(*x, y*).

3.2.1. Intra- and Inter-Cluster Similarity In this section, we assume that a clustering C = {C1*, . . . , C*k} is given for a period t. We consider C to be stable if it is comprised of clusters having points that are similar with respect to their prices. In other words, C has large intra-cluster similarity. To analyze intra-cluster similarity, we consider the *price standard deviation* of each cluster Ci and denote it by σi. We compute σi based on the vectors x tcorresponding to the nodes assigned to Ci. The *average* price standard deviation σ(C) of a clustering C is the average of all cluster price standard deviations σi, Ci ∈ C.

Whenever the clustering we are referring to is clear, we simplify notation by dropping the reference to C. A low average price standard deviation indicates large intra-cluster similarity.

Furthermore, a stable clustering is characterized by low inter-cluster similarity or, equivalently, large inter-cluster dissimilarity. With µi denoting the mean price of a cluster Ci 8, we define the following distance measures to assess the dissimilarity between two clusters Ci, Cj ∈ C:
The *average distance between cluster mean prices* quantifies the distinctiveness of clusters based on mean prices:
dµ(Ci, Cj ) = d(µi, µj ).

The *nearest neighbor cluster distance* reflects how well-separated the clusters are:

$$d_{\operatorname*{min}}(C_{i},C_{j})=\operatorname*{min}_{x\in C_{i},y\in C_{j}}d(x,y).$$

The *average distance between clusters* considers all pairs of points to measure the dissimilarity between Ci and Cj :

$$d_{\mathrm{avg}}(C_{i},C_{j})={\frac{1}{|C_{i}|\cdot|C_{j}|}}\sum_{x\in C_{i}}\sum_{y\in C_{j}}d(x,y).$$

The following quantity is used to evaluate the *global* inter-cluster dissimilarity of C:

$$\Delta_{q}({\mathcal{C}})={\frac{1}{{\binom{K}{2}}}}\sum_{\stackrel{C_{i},C_{j}\in{\mathcal{C}}}{i<j}}d_{q}(C_{i},C_{j}),$$

9

## Where Q Is One Of {Μ, Min, Avg}.

We also consider the *Davies-Bouldin index* to assess both the intra-cluster similarity and intercluster dissimilarity of C. With si denoting the diameter9 of cluster Ci and dij the distance between ci and cj , the Davies-Bouldin Index [15] is defined as:

$$D B={\frac{1}{k}}\sum_{i=1}^{K}\operatorname*{max}_{i\neq j}R_{i j},$$

were Rij =
si+sj dij. Intuitively, DB quantifies the average similarity of every cluster with its most similar cluster. Here, similarity is defined as the ratio of within-cluster distances to between-cluster distances. A low DB index indicates a good clustering, and the minimum value is 0. Clusters that are well-separated and less dispersed are rewarded by the DB index.

## 3.2.2. Temporal Stability

While geographic coordinates are static across time, prices are time-sensitive. Therefore, we are interested to see if pricing zones are stable over time. To decide this, we compare two clusterings C1 and C2 that are computed for two different time periods with the same algorithm and considering the same features. For this comparison, we use the *Rand index*, which measures the similarity between C1, C2 considering all pairs of data points and counting the pairs that are assigned to the same or to different clusters in both C1 and C2:

$$R I(\mathcal{C}_{1},\mathcal{C}_{2})=\frac{\sum_{1\leq l<r\leq N}\gamma(x_{l},x_{r})}{{\binom{N}{2}}},$$
$$\mathrm{where}$$
$$\gamma(x_{l},x_{s})=\begin{cases}1&\text{if$x_{l}$and$x_{r}$are in the same cluster in$\mathcal{C}_{1}$and in$\mathcal{C}_{2}$}\\ 1&\text{if$x_{l}$and$x_{r}$are in different clusters in$\mathcal{C}_{1}$and in$\mathcal{C}_{2}$}\\ 0&\text{otherwise.}\end{cases}$$

9The diameter of a cluster is the maximum distance between any two points assigned to this cluster.