# Finding Stable Price Zones in European Electricity Markets: Aiming to Square the Circle? 

Teodora Dobos ${ }^{\mathrm{a}, *}$, Martin Bichler ${ }^{\mathrm{a}}$, Johannes Knörr ${ }^{\mathrm{a}}$<br>${ }^{a}$ School of Computation, Information and Technology, Technical University of Munich, Boltzmannstrasse<br>3, Garching, 85748, Germany


#### Abstract

The European day-ahead electricity market is split into multiple bidding zones. Within these zones, a uniform energy price is computed for each hour. Large bidding zones have been under scrutiny. The fact that zonal clearing ignores the transmission capacities within zones and the increase in renewables lead to a growing number of interventions in the generation of energy sources and large redispatch costs. The European Union Agency for the Cooperation of Energy Regulators (ACER) proposed alternative bidding zone configurations that should be analyzed as part of the Bidding Zone Review. For Germany, four alternative configurations were suggested. Bidding zones shall be stable and based on long-term, structural congestion in the grid. We analyzed the proposed configurations considering different clustering algorithms and periods. We found that the configurations do not reduce the price standard deviations within zones considerably, while the average prices across zones are similar. Other configurations identified based on clustering prices lead to lower price standard deviations but are not geographically coherent. Importantly, different configurations emerge depending on clustering features, algorithm, and period considered. Given the substantial changes in energy supply and demand that can be expected in the future, defining stable configurations appears to be a moving target.

Keywords: Energy pricing, Price zones, Bidding Zone Review, Electricity markets, Energy policy


[^0]
## 1. Introduction

The European electricity market is split into multiple bidding zones (BZs), aka. price zones. Within these zones, market participants can submit bids and offers, which are subsequently matched without considering the capacities of the transmission network 1$]$ BZs are generally defined depending on national borders, such that a country represents a single bidding zone (e.g., France and Poland). However, there are also countries that are divided into several BZs, such as Norway, Sweden and Italy, or BZs that consist of more than one country, like the German-Luxembourgish bidding zone.

An important characteristic of BZs is that in the day-ahead market, they implement a uniform pricing mechanism, meaning that a single market-clearing electricity price applies to all participants belonging to a BZ. A uniform price in a BZ promotes transparency due to a simple single price signal in a large region, and it limits the market power that individual parties can exercise. However, a uniform electricity price also leads to significant negative ramifications. There are no local incentives to adapt to changes in the volatile supply of renewables, there are significant welfare losses due to the uniform price constraint, and large redispatch costs. The latter is because transmission constraints are ignored within a BZ when supply is matched with demand (Energywende 2018), and the market-based allocation is not physically feasible. In addition, uniform prices do not set appropriate investment incentives.

The German-Luxembourgish BZ is a case in point. Strong winds along the North Sea and Baltic Coast often contribute to elevated power production from wind farms in Northern Germany. The energy produced in the north must be transported to the main power consumption areas, which are located in the south and west of the country. However, the transmission lines connecting these regions often become congested and thus electricity cannot be delivered as determined in the day-ahead market. To stabilize the grid, redispatch by the Transmission System Operators (TSOs) is required. TSOs often need to throttle the generation of Northern conventional and wind power plants. At the same time, they instruct power plants in the south to increase energy production. Such redispatch actions incur substantial costs. In 2022, the redispatch costs in Germany were 4.2[^1]billion Euros 2

Furthermore, the lack of sufficient transmission lines in the German grid caused problems in neighboring countries. Poland and the Czech Republic have installed phase-shifters at their borders with Germany to reduce loop flows in their networks 3 These loop flows lead to suboptimal crosszonal trading opportunities and are a negative consequence of the large German bidding zone and its limited transmission grid.

Given these considerations, in August 2022 the European Union Agency for the Cooperation of Energy Regulators (ACER) decided that alternative bidding zone configurations should be analyzed as part of the Bidding Zone Review (BZR), which is organized by the European Network of Transmission System Operators for Electricity (ENTSO-E 2023). The goals of the BZR are described on a high level in different documents. According to Commission Regulation (EU) 2015/1222 and 2019/943, bidding zones "should be defined in a manner to ensure efficient congestion management and overall market efficiency" (Commission 2015) and "shall be based on long-term, structural congestions in the transmission network" (Commission 2019).

Annex I of ACER's decision on alternative bidding zone configurations to be considered in the bidding zone review process (ACER 2022a) describes that different configurations were identified by solving a clustering problem "based on nodal prices as clustering feature". The document argues that nodal prices "can be used as proxies for economic efficiency, in line with the objectives of the Electricity Regulation", and that the objective of clustering algorithms is to "minimize price dispersion within each bidding zone." The document discusses three clustering algorithms: constrained K-Means clustering, Spectral Clustering with constrained K-Means, and Spectral Clustering with Constrained Deterministic Iterative Refinement Clustering (CDIRC). Moreover, a constraint related to the minimum size of each zone was included 4

Based on this ACER methodology (ACER 2020), TSOs were tasked to calculate locational marginal prices (essentially, a nodal price for each substation in the transmission grid $\sqrt{5}$ for the[^2]target year 2025, for which generation and demand scenarios were created. These scenarios originate from ENTSO-E's Data \& Models working group. Weather data from 1989, 1995, and 2009 was used to create scenarios for representative reference climate years. The grid model, the demand, the generation capacities, and prices for gas, coal and $\mathrm{CO}_{2}$ were based on predictions for 2025. ENTSOE computed nodal prices for the respective weeks in a report published in June 2022 (ENTSO-E 2022). As outlined above (ACER 2022b), the time series of nodal prices represented the clustering features that were used to partition the set of nodes in the transmission network into a predefined number of clusters or BZs. A BZ configuration or a clustering thus represents the assignment of every node to a specific cluster or price zone. Finally, ACER suggested four alternative bidding zone configurations for Germany ACER (2022a) based on the results from the Locational Marginal Pricing (LMP) Study (ENTSO-E 2022, 2023). The evaluation of these configurations proposed by ACER in the BZR is ongoing at the time of writing. In this process, the TSOs are evaluating 22 indicators related to market efficiency, network security, and the stability and robustness of the proposed configurations ACER 2020).

In this paper, we leverage the data provided by ENTSO-E and study how stable and robust the configurations of price zones (or, clusterings) proposed by ACER are with respect to different time frames, different inputs (i.e., nodal prices with or without geographic coordinates), and different clustering algorithms. We define three criteria for analyzing clustering stability and robustness and conduct a thorough empirical evaluation of the suggested configurations using the data published by ENTSO-E. Following ACER's methodology, we implement K-Means and Spectral Clustering and evaluate the clusterings computed with these methods. We want to understand if the clustering algorithms compute the same clusters when nodal prices of different time periods are considered. How different are clusters resulting from different clustering algorithms? Also, how similar are the clusters of a particular configuration with respect to prices, and how large are the price standard deviations within clusters?

We find that the configurations proposed by ACER are not stable across time and algorithm used. Moreover, the configurations do not reduce the price standard deviations within zones considerably, and the average prices between zones are similar. If we recompute the clusters and take only
prices into account $\sqrt{6}$ we can reduce the price standard deviation within clusters more. However, these alternative clusters are not of equal size and are not geographically coherent. Importantly, neither the configurations proposed by ACER nor the clusters that we computed are stable across time. Depending on the time frame taken into account, different clusterings would result. Note that our analysis is performed based on the same target year 2025 as in the BZR. Given the significant changes in supply and demand and in the weather over time, we can expect substantial changes in the supply in future years. In particular, Germany has ambitious goals concerning the share of renewable energies and aims for $80 \%$ in 2030,7 There is a danger that even if a good configuration is selected for 2025, it might be outdated soon after.

This paper is structured as follows. In Section 2 we discuss the literature related to our work, while in Section 3 we describe the algorithms we implement to compute clusterings and introduce the metrics considered to evaluate stability. The data we use in our experiments is discussed in Section 4. while the experimental results are presented in Section 5. Finally, we summarize our main findings and their policy implications in Section 6 .

## 2. Related Literature

This paper complements existing literature computing bidding zone configurations. In particular, we draw on a unique data set with LMP prices that is provided by ENTSO-E. Bovo et al. (2019) identifies the main network indicators that should be considered for defining suitable bidding zone configurations. LMPs and power transfer distribution factors (PTDFs) represent such indicators. While some papers focus on identifying configurations by clustering PTDFs (e.g., $\overline{\mathrm{Ku}-}$ mar et al. 2004) and (Kłos et al. 2014), most works use LMPs as clustering features (Stoft 1997). Burstedde (2012) computes LMPs for the scenario years 2015 and 2020 considering a simplified 72-node representation of the European grid, and evaluates the shapes and sizes of the zones obtained by clustering these LMPs using hierarchical clustering. Breuer et al. (2013) implement a[^3]genetic algorithm and apply it on a dataset consisting of $380 \mathrm{kV}$ nodes considering a projected system for 2016 and 2018. Based on six scenarios, Felling \& Weber (2018) compute robust price zone configurations for Central Western Europe by employing hierarchical clustering based on the LMPs of approximately 2,200 nodes and assigning weights to nodes depending on their demandand supply situation. These configurations are robust in the sense that LMPs from multiple scenarios are integrated into their computation. Considering a network model consisting of around 2,700 nodes, Brouhard et al. (2023) design nine zone delineations for Continental Europe by implementing K-Means and hierarchical clustering. The authors calculate LMPs for multiple, independent singleperiod optimization problems (i.e., optimal power flow with direct current approximation), and use geographic coordinates and these prices as clustering features. Sarfati et al. (2015) introduce five indicators to assess the impact of bidding zone configurations in zonally-priced electricity markets. The indicators include commercial exchange and welfare evolution, as well as price convergence and divergence, and were analyzed on the Nordic 32-bus example system.

In terms of the German-Luxembourgish bidding zone, Zinke (2023) identifies north-south splits using hierarchical clustering based on the LMPs associated to approximately 500 nodes that are computed within a linear market and grid model for four scenario years. The author considers uncertain factors such as short-term weather patterns and long-term system changes to evaluate the potential decrease in redispatch costs resulting from such splits. Moreover, Ambrosius et al. (2020) consider a scenario for the year 2035 and determine welfare-maximizing price zones and available transfer capacities for a simplified representation of the German market area consisting of 28 nodes. Such zones are identified based on a mixed-integer nonlinear model that incorporates a graph partitioning problem on the first level. The prior literature used different data sources for these analyses.

## 3. Methodology

The process of computing price zones can be reduced to solving a clustering problem. Formally,

given a set of $N D$-dimensional data points $X=\left\{x_{1}, x_{2}, \ldots, x_{N}\right\}$ with $x_{i} \in \mathbb{R}^{D}$ and a number of clusters $k$, the objective of the clustering problem is to find for each point $x_{i}$ the corresponding
assignment $z_{i} \in\{1, \ldots, k\}$ to one of the $k$ clusters such that (1) points within the same cluster are similar to each other and (2) points between different clusters are dissimilar from each other. A clustering is a solution to this problem and is denoted by $\mathcal{C}=\left\{C_{1}, \ldots, C_{k}\right\}$, where $C_{i}=\left\{x_{j}: z_{j}=i\right\}$ is a cluster. The centroid of a cluster $C_{i}$ is defined as the mean of the data points assigned to $C_{i}$ and is depicted by $c_{i}$. In our setting, the data points are the nodes in the transmission network and the dimensions represent the features we use to compute clusters (see Section 4.1).

### 3.1. Clustering Algorithms

Following ACER's approach to identify alternative price zone configurations, we consider two clustering algorithms in this paper. ACER used three clustering approaches (ACER 2022b), i.e., K-Means, Spectral Clustering with constrained K-Means and Spectral Clustering with CDIRC, but the implementation details are not publicly available. Therefore, it is impossible to reproduce the exact algorithmic configuration ACER implemented. Instead, we consider the same family of clustering methods to evaluate alternative price zone configurations. In what follows, we briefly describe the clustering algorithms we implement.

### 3.1.1. K-Means

K-Means (Lloyd 1982) is a simple algorithm that clusters data points by minimizing withincluster variances, i.e., squared Euclidean distances. The method consists of three main steps. In the first step, the centroids are initialized randomly. In the second step, each data point is assigned to its nearest centroid with respect to the Euclidean distance, specifically to its corresponding cluster. The third step consists of updating the centroids, given the new points assigned to the clusters. The last two steps are repeated until the difference between the old and the new centroids is below a threshold. Importantly, the final clusters might differ depending on the initialization of centroids.

A constrained version of K-Means was considered in the BZR analysis (ACER 2022b), in which the centroids are initialized such that they are spread out spatially. We note that this version of K-Means is known as K-Means++ Arthur \& Vassilvitskii 2007). We implement the constrained version of K-Means by Bennett et al. (2000) and incorporate constraints for the minimum size of points included in each cluster. We update the clusters until the squared Euclidean distance
between each old and new centroid is smaller than 0.1. Moreover, we standardize the data such that all features have a mean of 0 and a standard deviation of 1.

### 3.1.2. Spectral Clustering

Spectral clustering is a technique used for clustering network data. Given a graph $G=(V, E)$, the method clusters the set of vertices $V$ based on a low-dimensional spectral embedding of $G$ and consists of three main steps. First, the Laplacian matrix $L$ is constructed. Then, the first $r$ eigenvectors (i.e., the eigenvectors corresponding to the $r$ smallest eigenvalues of $L$ ) are computed. In the last step, a matrix $\tilde{X} \in \mathbb{R}^{n \times r}$ is considered, whose columns are the selected eigenvectors and the $i$-th row is an embedding of the $i$-th node in $G$. The graph nodes are then clustered by applying, e.g., K-Means on the node embeddings. We refer to Aggarwal \& Wang (2010) for a comprehensive overview of Spectral Clustering.

For our setting, we define a complete graph $G$ in which $V$ is the set of nodes considered in the BZR analysis. We set the weight $w_{e}$ of an edge $e=(u, v) \in E$ as the similarity between nodes $u$ and $v$ and compute it using the radial basis function kernel. Thus, with $x_{u}, x_{v}$ denoting the

features corresponding to nodes $u$ and $v$, respectively, we define $w_{e}=\exp \left(-\frac{\left\|x_{u}-x_{v}\right\|^{2}}{2 \sigma^{2}}\right)$, where $\sigma$ is a parameter that controlls the width of node-neighborhoods. We normalize the edge weights such that $w_{e} \in[0,1]$ for all $e \in E$ and set $\sigma=1$. To cluster the nodes using $\tilde{X} \in \mathbb{R}^{n \times r}$, we apply the constrained version of K-Means mentioned in Section 3.1.1. Moreover, we set $r=k$ and thus consider the first $k$ eigenvectors as clustering features.

### 3.2. Stability Evaluation

In what follows, we discuss three criteria that we consider to evaluate the stability of pricing zones. Given a period $t$ and a node $x$, we denote by $x^{t}$ the vector containing the time series of prices corresponding to $x$ in period $t$. We define $\bar{x}^{t}$ as the average price of node $x$ in period $t$, which is simply the average over all values in $x^{t}$. We also denote the distance between two points $x$ and $y$ in period $t$ by $d^{t}(x, y)$ and define it as $d^{t}(x, y)=\left|\bar{x}^{t}-\bar{y}^{t}\right|$. Whenever the period we are referring to is evident, we simplify notation by omitting the reference to $t$ in $d^{t}(x, y)$.

### 3.2.1. Intra- and Inter-Cluster Similarity

In this section, we assume that a clustering $\mathcal{C}=\left\{C_{1}, \ldots, C_{k}\right\}$ is given for a period $t$. We consider $\mathcal{C}$ to be stable if it is comprised of clusters having points that are similar with respect to their prices. In other words, $\mathcal{C}$ has large intra-cluster similarity. To analyze intra-cluster similarity, we consider the price standard deviation of each cluster $C_{i}$ and denote it by $\sigma_{i}$. We compute $\sigma_{i}$ based on the vectors $x^{t}$ corresponding to the nodes assigned to $C_{i}$. The average price standard deviation $\sigma(\mathcal{C})$ of a clustering $\mathcal{C}$ is the average of all cluster price standard deviations $\sigma_{i}, C_{i} \in \mathcal{C}$. Whenever the clustering we are referring to is clear, we simplify notation by dropping the reference to $\mathcal{C}$. A low average price standard deviation indicates large intra-cluster similarity.

Furthermore, a stable clustering is characterized by low inter-cluster similarity or, equivalently, large inter-cluster dissimilarity. With $\mu_{i}$ denoting the mean price of a cluster $C_{i}^{8}$ we define the following distance measures to assess the dissimilarity between two clusters $C_{i}, C_{j} \in \mathcal{C}$ :

The average distance between cluster mean prices quantifies the distinctiveness of clusters based on mean prices:

$$
d_{\mu}\left(C_{i}, C_{j}\right)=d\left(\mu_{i}, \mu_{j}\right)
$$

The nearest neighbor cluster distance reflects how well-separated the clusters are:

$$
d_{\min }\left(C_{i}, C_{j}\right)=\min _{x \in C_{i}, y \in C_{j}} d(x, y)
$$

The average distance between clusters considers all pairs of points to measure the dissimilarity between $C_{i}$ and $C_{j}$ :

$$
d_{\mathrm{avg}}\left(C_{i}, C_{j}\right)=\frac{1}{\left|C_{i}\right| \cdot\left|C_{j}\right|} \sum_{x \in C_{i}} \sum_{y \in C_{j}} d(x, y)
$$

The following quantity is used to evaluate the global inter-cluster dissimilarity of $\mathcal{C}$ :

$$
\Delta_{q}(\mathcal{C})=\frac{1}{\left(\begin{array}{c}
K \\
2
\end{array}\right)} \sum_{\substack{C_{i}, C_{j} \in \mathcal{C} \\
i<j}} d_{q}\left(C_{i}, C_{j}\right)
$$[^4]where $q$ is one of $\{\mu, \min$, avg $\}$.

We also consider the Davies-Bouldin index to assess both the intra-cluster similarity and intercluster dissimilarity of $\mathcal{C}$. With $s_{i}$ denoting the diameter ${ }^{9}$ of cluster $C_{i}$ and $d_{i j}$ the distance between $c_{i}$ and $c_{j}$, the Davies-Bouldin Index [15] is defined as:

$$
D B=\frac{1}{k} \sum_{i=1}^{K} \max _{i \neq j} R_{i j}
$$

were $R_{i j}=\frac{s_{i}+s_{j}}{d_{i j}}$. Intuitively, $D B$ quantifies the average similarity of every cluster with its most similar cluster. Here, similarity is defined as the ratio of within-cluster distances to between-cluster distances. A low $D B$ index indicates a good clustering, and the minimum value is 0 . Clusters that are well-separated and less dispersed are rewarded by the $D B$ index.

### 3.2.2. Temporal Stability

While geographic coordinates are static across time, prices are time-sensitive. Therefore, we are interested to see if pricing zones are stable over time. To decide this, we compare two clusterings $\mathcal{C}_{1}$ and $\mathcal{C}_{2}$ that are computed for two different time periods with the same algorithm and considering the same features. For this comparison, we use the Rand index, which measures the similarity between $\mathcal{C}_{1}, \mathcal{C}_{2}$ considering all pairs of data points and counting the pairs that are assigned to the same or to different clusters in both $\mathcal{C}_{1}$ and $\mathcal{C}_{2}$ :

$$
R I\left(\mathcal{C}_{1}, \mathcal{C}_{2}\right)=\frac{\sum_{1 \leq l<r \leq N} \gamma\left(x_{l}, x_{r}\right)}{\left(\begin{array}{c}
N \\
2
\end{array}\right)}
$$

where

$$
\gamma\left(x_{l}, x_{s}\right)= \begin{cases}1 & \text { if } x_{l} \text { and } x_{r} \text { are in the same cluster in } \mathcal{C}_{1} \text { and in } \mathcal{C}_{2} \\ 1 & \text { if } x_{l} \text { and } x_{r} \text { are in different clusters in } \mathcal{C}_{1} \text { and in } \mathcal{C}_{2} \\ 0 & \text { otherwise }\end{cases}
$$[^5]

Rand indices are between 0 and 1 , and 1 indicates a perfect match, that is, the same clustering is obtained in both time periods.

### 3.2.3. Spatial Coherence

We evaluate clustering stability also with respect to whether the clusters are geographically separated. Geographically separated or spatially cohesive clusters can be identified on the map as groups of points (nodes) that are geographically close.

We assess whether clusters are spatially cohesive considering spatial autocorrelation. Thus, for a clustering $\mathcal{C}$, a positive spatial autocorrelation indicates that $\mathcal{C}$ has spatially cohesive clusters since neighboring locations are more likely to share similar prices and belong to the same cluster. To measure spatial autocorrelation, we use Global Moran's I Moran 1950, which is defined as:

$$
I=\frac{N}{W} \frac{\sum_{x \in X} \sum_{y \in X} w_{x y}(c(x)-\bar{c})(c(y)-\bar{c})}{\sum_{x \in X}(c(x)-\bar{c})^{2}}
$$

where $c(x)$ is the centroid of the cluster to which point $x$ is assigned, $w_{x y}$ denotes the spatial distance between points $x, y$ and $W=\sum_{x \in X} \sum_{y \in X} w_{x y}$. Also, $\bar{c}$ represents the average of all centroids. $I$ values are between -1 and +1 , where +1 defines perfect clustering of similar values, 0 indicates no correlation and -1 suggests perfect clustering of dissimilar values.

## 4. Data

The data we use in our experiments was published as part of the locational pricing study conducted by ENTSO-E ${ }^{10}$ and includes locational (i.e., nodal) prices. In this study, 24 weeks spanned across 3 years were analyzed: 1989 (weeks 04, 10, 11, 17, 20, 31, 40, 52), 1995 (weeks 02, 12, 16, 21, 27, 36, 38, 49) and 2009 (weeks 04, 08, 11, 15, 16, 21, 31, 48). For each day in these weeks, nodal prices for every 2-hour interval are available. The file containing the prices for the German-Luxembourgish bidding zone includes 6,090 unique node IDs and 14,170,464 nodal prices. Moreover, for 1,893,024 ( $\approx 13 \%$ ) nodal prices, which correspond to 939 distinct nodes, the node ID[^6]is "nan". Consequently, these prices cannot be considered in our experiments, as insufficient data is provided for identifying the nodes to which these prices correspond.

Note that ENTSO-E did not publish the geographic coordinates of the nodes analyzed in the locational pricing study. However, these are essential for identifying and analyzing price zones. Therefore, we implement the following approach to obtain the geographic location of nodes. We consider the XML files describing the German grid model that we obtained from the Bidding Zone Review website (ENTSO-E 2023). The grid is composed of elements such as substations, voltage levels and topological nodes, which form a hierarchy as follows: substations consist of one or multiple voltage levels and voltage levels consist of one or multiple topological nodes. Altogether, the German grid encompasses 834 substations, 1,697 voltage levels and 2,898 topological nodes. The name of each substation is included in the XML files and based on this we identified the geographic location of each substation using OpenStreetMap and (JAO) Static Grid Mode ${ }^{11}$. Since a topological node is mapped to a specific substation, in this process we also obtain the geographic coordinates of the topological nodes.

Next, we identify the prices corresponding to the topological nodes. We do this based on the IDs of these nodes and the IDs of the 6,090 nodes included in the file containing LMPs. For 2,200 out of 2,898 topological nodes we could identify their IDs in this file. These nodes belong to 714 substations across Germany. Looking at the different LMP prices computed by ENTSO-E ordered by substation, it turns out that prices for different topological nodes associated with a substation are the same or very close. So, with the 714 substations covered in our study, we could reconstruct most of the German substations, their prices and location across Germany.

### 4.1. Clustering Features 83 Periods

We apply K-Means and Spectral Clustering for two feature configurations. In the first configuration we use time series of nodal prices as clustering features, that is, a feature represents the nodal price of a specific point in time. In the second configuration, we additionally consider latitude and longitude. We compute one clustering for every year analyzed in the bidding zone review, i.e., 1989,[^7]

1995 and 2009. For each year, 672 prices are reported per node (12 hours $\times 7$ days $\times 8$ weeks), which implies that 672 and 674 features are considered for the first and second configuration, respectively. Note that the first configuration was also used by ACER (ACER 2021).

## 5. Results

In this section, we first analyze the price zone configurations proposed by ACER. Then, we evaluate the optimal price zone configurations computed with K-Means and Spectral Clustering for the years 1989, 1995 and 2009. Considering the metrics defined in Section 3.2, we assess the stability of the resulting clusterings and compare them to those proposed by ACER.

### 5.1. Analysis of the price zone configurations proposed by ACER

The configurations proposed by ACER for Germany are the following: two configurations with two price zones (DE2 (k-means) and DE (spectral)), one with three price zones (DE3 (spectral)) and one with four price zones (DE4 (spectral)). Appendix A contains approximations of these configurations given the nodes we consider in our experiments and based on the maps provided by ACER (ACER 2022a). Since it is difficult to manually obtain an accurate geographic separation of the zones within the proposed configurations, the configurations from Appendix $\AA$ are just approximations. In what follows, we analyze these configurations.

First, we want to understand the extent to which the geographic coordinates of the nodes contribute to the determination of price zones. To do this, we apply K-Means with latitude and


shown in Figure 1.

Result 1. Clustering nodes based solely on latitude and longitude leads to price zones that closely resemble the configurations proposed by ACER.

We notice that DE2 (k-means), DE3 (spectral) and DE4 (spectral) are similar to the clusterings computed by K-Means. In fact, the configurations proposed by ACER seem to be adjustments of the zones illustrated in Figure 1 such that their borders do not cross any federal state, with few[^8]

Figure 1: Price zones computed with K-Means for $k \in\{2,3,4\}$ based on latitude and longitude

exceptions at the borders between North Rhein-Westphalia \& Lower Saxony (for DE2 (spectral)) and Hesse \& North Rhein-Westphalia \& Lower Saxony (for DE3 (spectral) and DE4 (spectral)). Further below, we discuss clusterings that take prices into account and compare them to those of ACER.

Before this, we analyze the nodal prices for 1989, 1995 and 2009 in the configurations proposed by ACER. For each year and week, we compute the cluster price standard deviations and average prices corresponding to configurations DE2 (k-means), DE2 (spectral), DE3 (spectral) and DE4 (spectral), respectively. The purpose of this analysis is to see what benefit multiple price zones have on the reduction of the price standard deviation inside zones. Furthermore, we study whether the clusters are well-defined, i.e., whether, for a given configuration, the cluster average prices are different.

The evolution of cluster price standard deviations across the weeks in 1989, 1995 and 2009 is illustrated in Appendix B.1. We also observe the price standard deviations corresponding to a single price zone or cluster (Figure 4). Clearly, the average cluster price standard deviations decrease as we consider configurations with 2, 3 or 4 clusters. This is in fact an implicit objective of clustering nodes based on prices. However, this reduction is not substantial. For instance, for 2009, the percentage decreases in average price standard deviations compared to a single zone range from 1.92 to 5.69 depending on the configuration. Moreover, the decrease in average cluster
price standard deviation is not monotonic with respect to the number of clusters. That is, a larger number of clusters does not necessarily imply smaller average cluster price standard deviations. For instance, for 2009 and configuration DE2 (k-means), the average price standard deviation is 10.85, while DE3 (spectral) leads to an average price standard deviation of around 11.26. An explanation for this behavior is that the average cluster prices are heavily influenced by outliers, which are nodes having very large or low prices compared to the majority of nodes. For smaller clusters, that is, for configurations with a larger number of clusters, the influence of outliers is stronger. Moreover, if we compare the configuration with one price zone to any configuration with multiple zones (clusters), we notice that a reduction in average price standard deviation does not necessarily imply that all cluster standard deviations are lower.

Next, we analyze how different the average cluster prices are for each configuration. These values are shown in Appendix B. 2

Result 2. The difference in the average prices of clusters in the proposed configurations is low. For all configurations, the yearly differences between the average cluster prices are less than 6 EUR/MWh and $4.16 \mathrm{EUR} / \mathrm{MWh}$ on average.

The differences between the average prices in Germany and the average prices in the neighboring countries are generally larger than $6 \mathrm{EUR} / \mathrm{MWh}{ }^{13}$ The German-Austrian price zone was split in 2018. The average electricity spot market price in 2018 was 41.74 EUR/MWh in Germany and 59.92 EUR/MWh in Austria, which implies a price difference of 18.18 EUR/MWh between these zones. Our analysis indicates that the configurations proposed by ACER do not lead to well-defined clusters in terms of average prices. As the tables in Appendix B. 2 showcase, the cluster average prices are generally similar, regardless of the configuration, week or year.

Let us now compare the configurations proposed by ACER to the clusterings computed with our implementation of K-Means and Spectral Clustering. Given the nodal prices for 1989, 1995 and 2009, respectively, we apply both clustering algorithms to identify clusterings (i.e., price zones) for each year. The goal of this comparison is to understand whether the proposed configurations[^9]by ACER are stable over time. We say that the ACER configurations are stable if they are similar to the optimal clusterings identified for different years.

As described in Section 4.1, we compute clusterings for two scenarios. The first scenario uses, as clustering features, the time series of nodal prices, while the second scenario additionally considers the location coordinates. Table 1 shows Rand indices measuring the similarity between the clusterings proposed by ACER and the clusterings computed with each algorithm for 1989, 1995 and 2009 .

|  |  | Without loc. |  |  | With loc. |  |  |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  | 1989 | 1995 | 2009 | 1989 | 1995 | 2009 |
| K-Means | DE2 (k-means) | 0.5 | 0.5 | 0.51 | 0.5 | 0.5 | 0.51 |
|  | DE2 (spectral) | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
|  | DE3 (spectral) | 0.51 | 0.53 | 0.52 | 0.52 | 0.52 | 0.52 |
|  | DE4 (spectral) | 0.6 | 0.5 | 0.56 | 0.6 | 0.58 | 0.57 |
| Spectral | DE2 (k-means) | 0.51 | 0.51 | 0.51 | 0.51 | 0.51 | 0.51 |
|  | DE2 (spectral) | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
|  | DE3 (spectral) | 0.52 | 0.44 | 0.52 | 0.52 | 0.44 | 0.52 |
|  | DE4 (spectral) | 0.55 | 0.45 | 0.57 | 0.56 | 0.46 | 0.56 |

Table 1: Comparison of alternative price configurations to the price zones proposed by ACER. The table shows Rand indices, which are in $[0,1], 1$ indicating perfect similarity. The clusterings analyzed in this table were computed with K-Means or Spectral Clustering using time series of nodal prices (columns "Without loc.") or time series of nodal prices and the location coordinates of nodes (columns "With loc.").

Result 3. The price zone configurations proposed by ACER are not stable over time. Given the nodal prices corresponding to 1989, 1995 and 2009, respectively, K-Means and Spectral Clustering compute price zones that are considerably different from the proposed configurations.

We recall from Section 3.2 that the Rand index measures the similarity between two clusterings by considering all pairs of nodes and counting the pairs that are assigned to the same or to different clusters in both clusterings. As Table 1 indicates, Rand indices vary considerably when different years are analyzed. For instance, for DE4 (spectral) and the clustering computed with Spectral Clustering with price and location features we get $R I=0.56$ for $1989, R I=0.46$ for 1995 and $R I=0.56$ for 2009. Thus, our analysis suggests that the configurations proposed by ACER are not stable over time, regardless of the number of price zones. An explanation is that nodal prices vary both temporally and spatially. As a result, the spatial distribution of the optimal clusters (i.e., obtained based on the prices corresponding to a specific time frame) is different each year.

The plots included in Appendix D show that the clusterings indeed differ across time.

### 5.2. Analysis of the optimal price zone configurations for 1989, 1995 and 2009

In what follows, we analyze alternative price zones computed with K-Means and Spectral Clustering for the years 1989, 1995 and 2009. Previously we showed that the configurations proposed by ACER are not stable over these years. Now we are interested to see whether other price zone configurations exist that are more stable with regards to the criteria defined in Section 3.2. We report the results of K-Means and Spectral Clustering as described in Section 3.1. We evaluate the clusterings computed for each year using (1) time series of nodal prices as features, and (2) time series of nodal prices and the location coordinates of nodes.

Based on the results provided in Appendix C, we first evaluate the intra-cluster similarity and the inter-cluster dissimilarity of the clusterings computed for all three years. For each year, we want to understand whether the clusters are well-defined. Well-defined clusters are characterized by low price standard deviation within clusters (or, large intra-cluster similarity) and different cluster average prices (or, large inter-cluster dissimilarity).

Result 4. The clusterings computed with K-Means for 1989, 1995 and 2009 based only on prices exhibit lower average price standard deviations compared to the configurations proposed by ACER.

Tables 2, 3 and 4 show the average price standard deviations for different configurations with 1, 2, 3 or 4 price zones or clusters. The configurations refer to (1) a single price zone (column 'Single price zone'), (2) the configurations proposed by ACER (columns ACER DE2 (k-means), DE2 (spectral), DE3 (spectral), DE4 (spectral)) and (3) the optimal configurations computed with K-Means and Spectral Clustering based on nodal prices (columns 'K-Means' and 'Spectral Clustering').

We observe that the average price standard deviations $\sigma$ differ depending on the clustering algorithm. For instance, for $k=3$, K-Means (Spectral Clustering) leads to $\sigma=12.11(14.81)$ for 1989, $\sigma=12.47(15.56)$ for 1995 and $\sigma=10.06(11.11)$ for 2009. However, regardless of the year and the number of clusters, the clusterings we compute with K-Means based on nodal prices lead to average price standard deviations that are generally lower compared to the configurations proposed by ACER. Recall that the average price standard deviations for the configurations proposed by

|  | Single price zone | ACER DE2 (k-means) | ACER DE2 (spectral) | K-Means | Spectral |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1989 | 14.54 | 13.09 | 13.98 | 13.40 | 13.39 |
| 1995 | 14.31 | 12.93 | 13.80 | 11.16 | 15.16 |
| 2009 | 11.55 | 10.85 | 11.33 | 10.80 | 11.61 |

Table 2: Average price standard deviations of configurations with 1 or 2 price zones

|  | Single price zone | ACER DE3 (spectral) | K-Means | Spectral |
| :---: | :---: | :---: | :---: | :---: |
| 1989 | 14.54 | 13.86 | 12.11 | 14.81 |
| 1995 | 14.31 | 13.65 | 12.47 | 15.56 |
| 2009 | 11.55 | 11.26 | 10.06 | 11.11 |

Table 3: Average price standard deviations of configurations with 1 or 3 price zones

|  | Single price zone | ACER DE4 (spectral) | K-Means | Spectral |
| :---: | :---: | :---: | :---: | :---: |
| 1989 | 14.54 | 13.14 | 12.86 | 12.23 |
| 1995 | 14.31 | 13.02 | 11.12 | 15.09 |
| 2009 | 11.55 | 10.87 | 10.05 | 10.73 |

Table 4: Average price standard deviations of configurations with 1 or 4 price zones

ACER are up to 13.98. Nevertheless, the clusters we compute with K-Means and Spectral Clustering are not necessarily balanced, that is, the clusters may not contain a similar number of nodes. This fact can be observed in the plots provided in Appendix D. Given this observation and the fact that the configurations proposed by ACER appear to be balanced (see Appendix A), it explains that the price standard deviations inside the clusters we compute with K-Means and Spectral Clustering are lower.

Result 5. The clusterings computed with K-Means and Spectral Clustering for 1989, 1995 and 2009 are characterized by low inter-cluster dissimilarity and are thus not well-defined. Regardless of algorithm or clustering features, the yearly differences between the average cluster prices are less than $6 E U R / M W h$ and $3.45 E U R / M W h$ on average.

To evaluate inter-cluster dissimilarity, we analyze the values of $\Delta_{\mu}, \Delta_{\text {min }}$ and $\Delta_{\text {avg }}$ included in Appendix C. We recall from Section 3.2.1 that $\Delta_{\mu}$ denotes the global average distance between cluster mean prices, $\Delta_{\min }$ represents the global nearest neighbor cluster distance, while $\Delta_{\text {avg }}$ encodes the global average distance between clusters. For a given period, the distance between two nodes is simply the absolute difference between their average prices in this period. We notice that, regardless of the year, algorithm or clustering features, $\Delta_{\mu}$ is smaller than $6 \mathrm{EUR} / \mathrm{MWh}$, which suggests that, in terms of average prices, clusters are rather similar to each other. Moreover, all values of $\Delta_{\min }$
are smaller than 1, indicating that clusters are not well-separated. This means that there exist nodes that have very similar prices (i.e., their price difference is less than 1) that are assigned to different clusters. We also observe that the values of $\Delta_{\text {avg }}$ are in the interval $[2.51,5.20]$ and become slightly smaller as we consider configurations with multiple clusters. In other words, the average price distance between any pair of two nodes assigned to different clusters is below 6 EUR/MWh.

Finally, we analyze the Davies-Bouldin indices to measure the average similarity of every cluster with its most similar cluster. We notice that these indices are quite large and fluctuate depending on the clustering algorithm and clustering features, ranging from 0.45 to 7.75. We recall from Section 3.2.1 that Davies-Bouldin indices are in $[0, \infty)$, where 0 indicates a good clustering having wellseparated and less dispersed clusters. Interestingly, there is no clear evidence that using location coordinates in the clustering computation leads to smaller indices.

Given these observations, we conclude that the price zones computed for 1989, 1995 and 2009 with K-Means and Spectral Clustering generally exhibit larger intra-cluster similarity and similar inter-cluster dissimilarity compared to the configurations proposed by ACER. Large intra-cluster similarity indicates strong cohesion inside clusters and is a consequence of unbalanced clusters relative to the ACER configurations.

Next, we evaluate temporal stability considering the Rand indices included in Table 5 .

Result 6. The clusterings computed with K-Means and Spectral Clustering are not temporally stable. A signficant number of nodes would be assigned to different clusters in different years.

We notice that Rand indices fluctuate considerably when different pairs of years are considered and lie in the intervals $[0.57,0.95]$ for $k=2,[0.48,0.95]$ for $k=3$ and $[0.44,0.86]$ for $k=4$. This suggests that clusterings are not temporally stable. The price zone configuration identified for a specific year might be far from the optimal configuration corresponding to a different year. This challenges the goal of finding price zones that reflect stable long-term patterns in nodal prices.

Last but not least, we analyze how spatially coherent the clusterings computed with K-Means and Spectral Clustering for 1989, 1995 and 2009 are. Figure 2 illustrates the Global Moran's I values of the clusterings computed using (1) nodal weekly prices and (2) nodal weekly prices and the location coordinates of nodes as features.

|  |  | 1989 |  |  | 1995 |  |  | 2009 |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  | $k=2$ | $k=3$ | $k=4$ | $k=2$ | $k=3$ | $k=4$ | $k=2$ | $k=3$ | $k=4$ |
| K-Means | 1989 | - | - | - | 0.57 | 0.69 | 0.7 | 0.87 | 0.88 | 0.83 |
|  | 1995 | 0.57 | 0.69 | 0.7 | - | - | - | 0.61 | 0.78 | 0.67 |
|  | 2009 | 0.87 | 0.88 | 0.83 | 0.61 | 0.78 | 0.67 | - | - | - |
| Spectral | 1989 |  |  |  | 0.68 | 0.5 | 0.5 | 0.72 | 0.48 | 0.78 |
|  | 1995 | 0.68 | 0.5 | 0.5 | - | - | - | 0.7 | 0.48 | 0.44 |
|  | 2009 | 0.72 | 0.48 | 0.78 | 0.7 | 0.48 | 0.44 | - | - | - |


|  | 1989 |  |  |  |  |  |  |  |  | 1995 |  |  | 2009 |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  | $k=2$ | $k=3$ | $k=4$ | $k=2$ | $k=3$ | $k=4$ | $k=2$ | $k=3$ | $k=4$ |  |  |  |  |  |
| K-Means | 1989 | - | - | - | 0.95 | 0.95 | 0.76 | 0.59 | 0.93 | 0.86 |  |  |  |  |  |
|  | 1995 | 0.95 | 0.95 | 0.76 | - | - | - | 0.57 | 0.92 | 0.66 |  |  |  |  |  |
|  | 2009 | 0.59 | 0.93 | 0.86 | 0.57 | 0.92 | 0.66 | - | - | - |  |  |  |  |  |
|  | 1989 | - | - | - | 0.69 | 0.5 | 0.46 | 0.71 | 0.78 | 0.76 |  |  |  |  |  |
| Spectral | 1995 | 0.69 | 0.5 | 0.46 | - | - | - | 0.7 | 0.49 | 0.5 |  |  |  |  |  |
|  | 2009 | 0.71 | 0.78 | 0.76 | 0.7 | 0.49 | 0.5 | - | - | - |  |  |  |  |  |

Table 5: Temporal stability evaluation. Tables show Rand indices, which are always in $[0,1], 1$ indicating perfect similarity. In the first table, the results refer to clusterings computed based on prices. In the second table, the results relate to clusterings computed based on prices and location coordinates.


Figure 2: Global Moran's I values of the clusterings computed with K-Means and Spectral Clustering

For all years we consider, the Global Moran's I values are between 0.01 and 0.5 , indicating that clusterings exhibit moderate positive spatial autocorrelation. Neighboring nodes are more likely to have similar prices and to belong to the same cluster. Also, considering the location coordinates in the K-Means computation leads to better Global Moran's I scores which are quite stable across time. However, the plots from Figure 2 show that the clusterings obtained with Spectral Clustering exhibit scores that vary considerably across years.

Analyzing the clusters on the map of Germany, we notice that isolated points assigned to a specific cluster are sometimes located in the geographic area predominantly occupied by points belonging to a different cluster. This behavior can also be observed when latitude and longitude are included as features and is independent of the number of clusters or clustering algorithm. Therefore, a post-processing step is required to obtain spatially coherent price zones. This is because prices alone do not define geographically well-separated or spatially coherent clusters. This phenomenon can be observed in Figures 12 and 11 from Appendix D.

## Sensitivity Analysis regarding Outliers

In what follows, we briefly discuss the influence of outliers on the resulting price zones. We classify a node as an outlier if it has a price lower than 0 EUR/MWh or larger than $100 \mathrm{EUR} / \mathrm{MWh}$ in any of the periods considered in the clustering computation. Out of 1,478,400 nodal prices reported for a specific year, $38,378(\approx 2.59 \%)$ lie outside the interval $[0,100]$. Interestingly, this number is identical in all three years we consider. We want to understand the influence of outliers on the clustering computation. To do this, we clip the prices to the interval $[0,100]$ and apply the clustering algorithms. Table 6 contains the average yearly prices of the clusters computed with K-Means and Spectral Clustering after clipping the prices. We observe that these prices are similar to the average yearly prices shown in Table 13, in which clusterings were computed without clipping prices. The global average distances between cluster mean prices (i.e., $\Delta_{\mu}$ ) illustrated in Table 6 are also close to the average distances included in Table 13. In particular, the differences between the values of $\Delta_{\mu}$ shown in these tables are smaller than 6 EUR/MWh. Hence, the impact of outliers on the resulting clusters or price zones is not considerable.

|  | K-Means |  |  |  |  |  |  |  | Spectral |  |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Year | $k$ | Loc. | $\Delta_{\mu}$ | $\mu_{1}$ | $\mu_{2}$ | $\mu_{3}$ | $\mu_{4}$ | $\Delta_{\mu}$ | $\mu_{1}$ | $\mu_{2}$ | $\mu_{3}$ | $\mu_{4}$ |  |  |  |
| 1989 | 2 |  | 5.7 | 46.59 | 40.89 | - | - | 3.2 | 43.66 | 46.86 | - | - |  |  |  |
| 1995 | 2 |  | 5.89 | 41.54 | 47.43 | - | - | 3.2 | 43.66 | 46.86 | - | - |  |  |  |
| 2009 | 2 |  | 5.9 | 47.44 | 41.54 | - | - | 3.2 | 43.66 | 46.86 | - | - |  |  |  |
| 1989 | 2 | $\mathrm{x}$ | 5.79 | 41.25 | 47.04 | - | - | 3.13 | 43.63 | 46.76 | - | - |  |  |  |
| 1995 | 2 | $\mathrm{x}$ | 5.68 | 46.55 | 40.87 | - | - | 3.13 | 43.63 | 46.76 | - | - |  |  |  |
| 2009 | 2 | $\mathrm{x}$ | 5.79 | 41.32 | 47.11 | 3.13 | 43.63 | 46.76 | - | - |  |  |  |  |  |
| 1989 | 3 |  | 3.95 | 41.52 | 41.47 | 47.39 | - | 2.21 | 43.39 | 46.64 | 46.7 | - |  |  |  |
| 1995 | 3 |  | 4.27 | 41.2 | 47.6 | 46.04 | - | 3.67 | 43.94 | 46.9 | 41.4 | - |  |  |  |
| 2009 | 3 |  | 4.44 | 40.91 | 47.57 | 44.16 | - | 3.76 | 43.96 | 41.26 | 46.9 | - |  |  |  |
| 1989 | 3 | $\mathrm{x}$ | 4.75 | 42.43 | 47.38 | 40.26 | - | 3.71 | 43.91 | 46.85 | 41.29 | - |  |  |  |
| 1995 | 3 | $\mathrm{x}$ | 5.06 | 41.36 | 46.72 | 48.95 | - | 3.71 | 43.91 | 46.85 | 41.29 | - |  |  |  |
| 2009 | 3 | $\mathrm{x}$ | 5.02 | 48.61 | 41.08 | 46.43 | - | 3.71 | 43.91 | 46.85 | 41.29 | - |  |  |  |
| 1989 | 4 |  | 3.96 | 47.1 | 41.02 | 41.76 | 39.43 | 3.04 | 43.74 | 46.28 | 46.57 | 41.33 |  |  |  |
| 1995 | 4 |  | 4.7 | 40.72 | 43.74 | 48.92 | 47.32 | 2.86 | 40.94 | 46.27 | 46.58 | 46.51 |  |  |  |
| 2009 | 4 |  | 3.94 | 41.34 | 47.48 | 40.24 | 43.25 | 3.07 | 43.72 | 46.53 | 41.33 | 46.54 |  |  |  |
| 1989 | 4 | $\mathrm{x}$ | 4.2 | 41.21 | 47.48 | 43.73 | 39.92 | 1.85 | 43.16 | 46.64 | 46.61 | 45.94 |  |  |  |
| 1995 | 4 | $\mathrm{x}$ | 3.82 | 40.62 | 43.89 | 41.62 | 47.5 | 1.79 | 42.99 | 46.21 | 46.25 | 46.56 |  |  |  |
| 2009 | 4 | $\mathrm{x}$ | 4.5 | 41.51 | 47.69 | 45.65 | 40.06 | 1.85 | 43.16 | 46.64 | 46.61 | 45.94 |  |  |  |

Table 6: Cluster average prices after clipping nodal prices to [0,100] (EUR/MWh)

## 6. Conclusions and Policy Implications

In this paper, we analyzed the alternative price zone configurations proposed by ACER for Germany, namely DE2 (k-means), DE2 (spectral), DE3 (spectral) and DE4 (spectral). Similar to ACER's approach (the algorithms used are publicly known, but the implementation details are not), we computed alternative price zone configurations by solving a clustering problem using K-Means and Spectral Clustering.

Interestingly, clusterings that we obtained with K-Means using only latitude and longitude as features are similar to the configurations proposed by ACER. It only takes minor adjustments of the clusterings computed with K-Means such that the cluster borders do not cross a federal state of Germany, with a few isolated exceptions. Note that ACER might have had access to a more complete dataset covering all substations and also the clustering algorithms might differ in details. However, we computed quite different clusterings based on the nodal prices only, as it is described in the guidelines by ACER (2022a).

Independent of how the clusterings were determined by ACER, our main finding is that none of
them is stable across time. We evaluated how different configurations proposed by ACER reduce the average price standard deviations within clusters, and found that the configurations do not reduce the price standard deviations within zones much. Moreover, the decrease in average price standard deviation is not monotonic with respect to the number of clusters. Configurations with 3 or 4 price zones do not reduce the average price standard deviation as compared to configurations with 1 or 2 price zones. We also observed that the average prices of all proposed configurations do not differ considerably across clusters. For all three years we considered, the annual differences between the average cluster prices are less than 6 EUR/MWh.

Additionally, we computed alternative configurations by taking nodal prices or nodal prices and geographic coordinates into account and compared them with the configurations proposed by ACER. The resulting price zones are significantly different from the proposed ACER configurations. Importantly, neither the ACER configurations nor the newly computed clusterings are stable across time. What appears to be a good cluster in one time period might turn out suboptimal in another time period. Moreover, our results show that clusters with "minimal price dispersion within each bidding zone" (ACER 2022a) are not geographically coherent on the map, and they do not have similar numbers of nodes.

Importantly, our analysis is made with respect to the target year 2025, which is in line with the Bidding Zone Review. With the ambitious goals for renewable energy in Germany until 2030 and beyond, and the increasing electrification of the traffic and heat sectors, supply and demand will change substantially and the analysis will soon be outdated. Splitting price zones incurs high transition costs and there is a danger that new reconfigurations of the bidding zones might be in order in a few years again.

## Acknowledgements

We would like to thank Karsten Neuhoff and Maximilian Rinck for many helpful comments. We gratefully acknowledge the financial support of the Kopernikus-Project "SynErgie" by the Federal Ministry of Education and Research of Germany (BMBF) and the project supervision by the project management organization Projektträger Jülich (PtJ).

## References

ACER (2020). ACER Decision on the methodology and assumptions that are to be used in the bidding zone review process and for the alternative bidding zone configurations to be considered Annex I. Methodology and assumptions that are to be used in the bidding zone review process. https://acer. europa.eu/s ites/default/files/documents/Official_documents/Acts_of_the_Agency/Individual\%20deci sions\%20Annexes/ACER\%20Decision\%20No\%2029-2020_Annexes/ACER\%20Decision\%2029-2020\%20 on\%20the\%20BZR\%20-\%20Annex\%20I\%20_\%20\%20BZR\%20methodology.pdf. Accessed: 2024-02-09.

ACER (2021). High-level approach to identify alternative bidding zone configurations for the bidding zone review. https://acer.europa.eu/en/Documents/Presentations\ Webinars/20210624_Public_w ebinar_alternative_BZ_configurations.pdf. Accessed: 2024-02-09

ACER (2022a). ACER's Decision on the alternative bidding zone configurations to be considered in the bidding zone review process. Annex I. List of alternative bidding zone configurations to be considered for the bidding zone review. https://www.acer.europa.eu/Individual\ Decisions_annex/ACER $\% 20$ Decision $\% 2011-2022 \% 20$ on $\% 20$ alternative $\% 20$ BZ $\% 20$ configurations $\% 20-\% 20$ Annex $\% 20$. pdf

Accessed: 2023-12-01.

ACER (2022b). ACER's Decision on the alternative bidding zone configurations to be considered in the bidding zone review process. Annex IV. Description of the clustering algorithms. https://www.acer .europa.eu/Individual\%20Decisions_annex/ACER\%20Decision $\% 2011-2022 \% 20$ on $\% 20$ alternative \%20BZ\%20configurations\%20-\%20Annex\%20IV.pdf. Accessed: 2024-02-09.

Aggarwal, C. C. \& Wang, H. (2010). Managing and Mining Graph Data (1st ed.). Springer Publishing Company, Incorporated.

Ambrosius, M., Grimm, V., Kleinert, T., Liers, F., Schmidt, M., \& Zöttl, G. (2020). Endogenous price zones and investment incentives in electricity markets: An application of multilevel optimization with graph partitioning. Energy Economics, 92, 104879.

Arthur, D. \& Vassilvitskii, S. (2007). K-means++: The advantages of careful seeding. Proceedings of the Eighteenth Annual ACM-SIAM Symposium on Discrete Algorithms, SODA '07, 1027-1035.

Bennett, K., Bradley, P., \& Demiriz, A. (2000). Constrained k-means clustering. Technical Report MSRTR-2000-65. https://www.microsoft.com/en-us/research/publication/constrained-k-means -clustering/

Bovo, C., Ilea, V., Carlini, E., Caprabianca, M., Quaglia, F., Luzi, L., \& Nuzzo, G. (2019). Review of the mathematic models to calculate the network indicators to define the bidding zones. 2019 54th

International Universities Power Engineering Conference (UPEC), 1-6. https://doi.org/10.1109/ UPEC. 2019.8893576

Breuer, C., Seeger, N., \& Moser, A. (2013). Determination of alternative bidding areas based on a full nodal pricing approach. 1-5. https://doi.org/10.1109/PESMG.2013.6672466

Brouhard, T., Hennebel, M., Petit, M., \& Gisbert, C. (2023). A clustering approach to the definition of robust, operational and market efficient delineations for european bidding zones. IET Generation, Transmission 8 Distribution.

Burstedde, B. (2012). From nodal to zonal pricing: A bottom-up approach to the second-best. 2012 9th International Conference on the European Energy Market, 1-8. https://doi.org/10.1109/EEM. 20 12.6254665

Commission, E. (2015). Commission regulation (eu) 2015/1222 of 24 july 2015 establishing a guideline on capacity allocation and congestion management (text with eea relevance). Official Journal of the European Union. Accessed: 2024-01-19.

Commission, E. (2019). Regulation (eu) 2019/943 of the european parliament and of the council of 5 june 2019 on the internal market for electricity (recast) (text with eea relevance.). Official Journal of the European Union. Accessed: 2024-01-19.

Davies, D. L. \& Bouldin, D. W. (1979). A cluster separation measure. IEEE Transactions on Pattern Analysis and Machine Intelligence, PAMI-1(2), 224-227. https://doi.org/10.1109/TPAMI . 1979.4766909

Energywende (2018). The german electricity grid: notoriously swamped? https://energytransition.org 12018/03/the-german-electricity-grid-notoriously-swamped. Accessed: 2024-01-18.

ENTSO-E (2022). Report on the locational marginal pricing study of the bidding zone review process. https: //eepublicdownloads.blob.core.windows.net/public-cdn-container/clean-documents/Pub lications/Market\%20Committee\%20publications/ENTSO-E\%20LMP\%20Report_publication.pdf

Accessed: 2024-02-09

ENTSO-E (2023). Bidding zone review. https://www.entsoe.eu/network_codes/bzr/. Accessed: 2024-01-18.

Felling, T. \& Weber, C. (2018). Consistent and robust delimitation of price zones under uncertainty with an application to central western europe. Energy Economics, 75, 583-601. https://doi.org/https: //doi.org/10.1016/j.eneco.2018.09.012

Kumar, A., Srivastava, S., \& Singh, S. (2004). A zonal congestion management approach using real and
reactive power rescheduling. IEEE Transactions on Power Systems, 19(1), 554-562. https://doi.or g/10.1109/TPWRS.2003.821448

Kłos, M., Wawrzyniak, K., Jakubek, M., \& Oryńczak, G. (2014). The scheme of a novel methodology for zonal division based on power transfer distribution factors. IECON 2014 - 40th Annual Conference of the IEEE Industrial Electronics Society, 3598-3604. https://doi.org/10.1109/IECON . 2014.7049033

Lloyd, S. (1982). Least squares quantization in pcm. IEEE Transactions on Information Theory, 28(2), 129-137. https://doi.org/10.1109/TIT.1982.1056489

Moran, P. A. P. (1950). Notes on continuous stochastic phenomena. Biometrika, 37(1/2), 17-23. http: //www.jstor.org/stable/2332142

Sarfati, M., Hesamzadeh, M. R., \& Canon, A. (2015). Five indicators for assessing bidding area configurations in zonally-priced power markets. 2015 IEEE Power $\mathfrak{E}$ Energy Society General Meeting, 1-5.

Stoft, S. (1997). Transmission pricing zones: simple or complex? The Electricity Journal, 10(1), 24-31. https://doi.org/https://doi.org/10.1016/S1040-6190(97)80294-1

Zinke, J. (2023). Two prices fix all? on the robustness of a german bidding zone split. Technical report, Energiewirtschaftliches Institut an der Universitaet zu Koeln (EWI).

A. Approximations of the alternative configurations proposed by ACER


Figure 3: Approximations of the alternative configurations proposed by ACER

## B. Cluster price analysis for the alternative configurations proposed by ACER

## B.1. Cluster price standard deviations

Table 7 shows the average price standard deviations of a single price zone configuration as well as of the configurations proposed by ACER.

|  | 1989 | 1995 | 2009 |
| :---: | :---: | :---: | :---: |
| Single price zone | 14.54 | 14.32 | 11.48 |
| DE2 (k-means) | 13.09 | 12.93 | 10.85 |
| DE2 (spectral) | 13.98 | 13.80 | 11.22 |
| DE3 (spectral) | 13.86 | 13.65 | 11.26 |
| DE4 (spectral) | 13.14 | 13.02 | 10.87 |

Table 7: Average price standard deviations of configurations with 1, 2, 3 or 4 price zones

The following plots illustrate, for every configuration, the cluster price standard deviation corresponding to each week in 1989, 1995, and 2009. A point represents the price standard deviation of a specific cluster in a specific week. Depending on the configuration (i.e., number of clusters), multiple points are shown for the same week. Figure 4 highlights the weekly price standard deviation of a single price zone for each year we consider.


Figure 4: Single price zone (cluster)


Figure 5: DE2 (k-means)


Figure 6: DE2 (spectral)


Figure 7: DE3 (spectral)


Figure 8: DE4 (spectral)

## B.2. Average cluster prices

In the following tables, $\Delta_{\mu}^{\text {year }}$ represents the average distance between cluster mean prices for a specific year, i.e., $\Delta_{\mu}^{\text {year }}=\frac{1}{8} \sum_{i \in\{1, \ldots, 8\}} \Delta_{\mu}^{\mathrm{W}_{i}}$, where $\Delta_{\mu}^{\mathrm{W}_{i}}$ is the average distance between cluster mean prices for week $\mathrm{W}_{i}$ (see Section 3.2.1).

|  |  | W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8 | $\Delta^{\text {year }}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1989 | Cluster 1 | 50.49 | 46.72 | 41.99 | 49.88 | 48.52 | 39.52 | 40.22 | 45.50 | - |
| 1995 | Cluster 1 | 39.87 | 28.09 | 45.89 | 46.11 | 48.61 | 38.35 | 51.76 | 54.50 | - |
| 2009 | Cluster 1 | 50.49 | 51.94 | 41.99 | 47.66 | 45.89 | 46.11 | 39.52 | 40.91 | - |

Table 8: Cluster average prices (EUR/MWh) - Single price zone (cluster)

|  |  | $\mathrm{W} 1$ | $\mathrm{~W} 2$ | $\mathrm{~W} 3$ | $\mathrm{~W} 4$ | $\mathrm{~W} 5$ | $\mathrm{~W} 6$ | $\mathrm{~W} 7$ | $\mathrm{~W} 8$ | $\Delta_{\mu}^{\text {year }}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1989 | Cluster 1 | 49.09 | 45.71 | 39.18 | 49.32 | 47.94 | 35.84 | 37.44 | 44.38 | 4.3 |
|  | Cluster 2 | 52.55 | 48.21 | 46.10 | 50.69 | 49.39 | 44.91 | 44.28 | 47.15 |  |
| 1995 | Cluster 1 | 35.02 | 21.21 | 44.56 | 45.13 | 47.65 | 35.63 | 51.22 | 54.14 | 5.75 |
|  | Cluster 2 | 46.98 | 38.19 | 47.84 | 47.55 | 50.03 | 42.35 | 52.56 | 55.04 |  |
| 2009 | Cluster 1 | 49.09 | 51.21 | 39.18 | 47.11 | 44.56 | 45.13 | 35.84 | 37.25 | 4.67 |
|  | Cluster 2 | 52.55 | 53.01 | 46.10 | 48.46 | 47.84 | 47.55 | 44.91 | 46.28 |  |

Table 9: Cluster average prices (EUR/MWh) - DE2 (k-means)

|  |  | $\mathrm{W} 1$ | $\mathrm{~W} 2$ | $\mathrm{~W} 3$ | $\mathrm{~W} 4$ | $\mathrm{~W} 5$ | $\mathrm{~W} 6$ | $\mathrm{~W} 7$ | $\mathrm{~W} 8$ | $\Delta_{\mu}^{\text {year }}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1989 | Cluster 1 | 48.87 | 45.52 | 38.77 | 49.13 | 47.73 | 34.89 | 36.80 | 44.29 | 4.17 |
|  | Cluster 2 | 52.07 | 47.90 | 45.14 | 50.61 | 49.31 | 44.05 | 43.56 | 46.70 |  |
| 1995 | Cluster 1 | 34.06 | 20.40 | 44.22 | 44.91 | 47.36 | 35.03 | 51.08 | 54.08 | 5.46 |
|  | Cluster 2 | 45.56 | 35.63 | 47.53 | 47.29 | 49.84 | 41.61 | 52.44 | 54.91 |  |
| 2009 | Cluster 1 | 48.87 | 51.06 | 38.77 | 46.91 | 44.22 | 44.91 | 34.89 | 36.81 | 4.47 |
|  | Cluster 2 | 52.07 | 52.80 | 45.14 | 48.39 | 47.53 | 47.29 | 44.05 | 44.93 |  |

Table 10: Cluster average prices (EUR/MWh) - DE2 (spectral)

|  |  | $\mathrm{W} 1$ | $\mathrm{~W} 2$ | $\mathrm{~W} 3$ | $\mathrm{~W} 4$ | $\mathrm{~W} 5$ | $\mathrm{~W} 6$ | $\mathrm{~W} 7$ | $\mathrm{~W} 8$ | $\Delta_{\mu}^{\text {year }}$ |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1989 | Cluster 1 | 52.68 | 48.38 | 46.38 | 50.72 | 49.36 | 44.96 | 44.58 | 47.43 |  |
|  | Cluster 2 | 49.17 | 45.94 | 40.29 | 49.85 | 48.51 | 37.41 | 38.86 | 44.68 | 3.09 |
|  | Cluster 3 | 49.72 | 45.81 | 39.04 | 48.88 | 47.51 | 35.88 | 36.81 | 44.32 |  |
| 1995 | Cluster 1 | 47.30 | 38.88 | 47.80 | 47.66 | 50.05 | 42.57 | 52.58 | 55.08 |  |
|  | Cluster 2 | 36.69 | 23.49 | 45.31 | 45.88 | 48.37 | 36.26 | 51.77 | 54.24 | 3.99 |
|  | Cluster 3 | 35.34 | 21.51 | 44.37 | 44.53 | 47.18 | 36.21 | 50.73 | 54.18 |  |
| 2009 | Cluster 1 | 52.68 | 53.05 | 46.38 | 48.42 | 47.8 | 47.66 | 44.96 | 46.74 |  |
|  | Cluster 2 | 49.17 | 51.49 | 40.29 | 47.89 | 45.31 | 45.88 | 37.41 | 38.87 | 3.37 |
|  | Cluster 3 | 49.72 | 51.21 | 39.04 | 46.38 | 44.37 | 44.53 | 35.88 | 36.69 |  |

Table 11: Cluster average prices (EUR/MWh) - DE3 (spectral)

|  |  | $\mathrm{W} 1$ | $\mathrm{~W} 2$ | $\mathrm{~W} 3$ | $\mathrm{~W} 4$ | $\mathrm{~W} 5$ | $\mathrm{~W} 6$ | $\mathrm{~W} 7$ | $\mathrm{~W} 8$ | $\Delta_{\mu}^{\text {year }}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1989 | Cluster 1 | 49.03 | 46.0 | 39.51 | 49.91 | 48.52 | 36.68 | 38.28 | 44.48 |  |
|  | Cluster 2 | 52.30 | 47.85 | 45.41 | 50.94 | 49.77 | 44.74 | 43.06 | 46.37 | 3.14 |
|  | Cluster 3 | 49.00 | 45.41 | 38.73 | 48.84 | 47.44 | 34.78 | 36.55 | 44.25 |  |
|  | Cluster 4 | 52.62 | 48.50 | 46.44 | 50.37 | 48.91 | 44.81 | 45.46 | 47.86 |  |
| 1995 | Cluster 1 | 35.24 | 21.24 | 44.78 | 45.75 | 48.32 | 36.11 | 51.63 | 54.13 |  |
|  | Cluster 2 | 45.35 | 35.98 | 47.97 | 47.80 | 50.53 | 41.13 | 53.33 | 55.07 | 4.19 |
|  | Cluster 3 | 34.37 | 20.74 | 44.23 | 44.60 | 47.05 | 34.99 | 50.87 | 54.11 |  |
|  | Cluster 4 | 48.32 | 39.51 | 47.58 | 47.13 | 49.35 | 43.53 | 51.58 | 54.94 |  |
| 2009 | Cluster 1 | 49.03 | 51.29 | 39.51 | 47.72 | 44.78 | 45.75 | 36.68 | 37.71 |  |
|  | Cluster 2 | 52.30 | 53.05 | 45.41 | 49.11 | 47.97 | 47.80 | 44.74 | 44.95 | 3.34 |
|  | Cluster 3 | 49.00 | 51.07 | 38.73 | 46.6 | 44.23 | 44.60 | 34.78 | 36.69 |  |
|  | Cluster 4 | 52.62 | 52.87 | 46.44 | 47.67 | 47.58 | 47.13 | 44.81 | 47.18 |  |

Table 12: Cluster average prices - DE4 (spectral)

## C. Intra- and inter-cluster similarity evaluation

| Year | $k$ | Alg. | Loc. | $\sigma$ | $\Delta_{\mu}$ | $\Delta_{\min }$ | $\Delta_{\text {avg }}$ | $D B$ | $\mu_{1}$ | $\mu_{2}$ | $\mu_{3}$ | $\mu_{4}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1989 | 2 | K-Means |  | 13.4 | 5.91 | 0.0 | 5.91 | 0.63 | 47.28 | 41.37 | - | - |
| 1995 | 2 | K-Means |  | 11.16 | 4.66 | 0.0 | 4.97 | 0.76 | 48.47 | 43.81 | - | - |
| 2009 | 2 | K-Means |  | 10.8 | 3.68 | 0.0 | 3.68 | 0.71 | 45.29 | 48.97 | - | - |
| 1989 | 2 | Spectral |  | 13.39 | 3.57 | 0.0 | 4.3 | 1.44 | 43.61 | 47.18 | - <br> - | - |
| 1995 | 2 | Spectral |  | 15.16 | 2.87 | 0.0 | 3.57 | 1.89 | 44.74 | 41.87 | - |  |
| 2009 | 2 | Spectral |  | 11.61 | 0.31 | 0.0 | 2.19 | 13.76 | 46.68 | 46.37 | - | - |
| 1989 | 2 | K-Means | $\mathrm{x}$ | 13.0 | 5.91 | 0.0 | 5.93 | 0.62 | 41.64 | 47.55 | - <br> - | - |
| 1995 | 2 | K-Means | $\mathrm{x}$ | 13.03 | 5.9 | 0.0 | 5.93 | 0.56 | 47.88 | 41.98 | - | - |
| 2009 | 2 | K-Means | $\mathrm{x}$ | 9.97 | 2.44 | 0.0 | 2.91 | 0.84 | 46.36 | 48.8 | - | - |
| 1989 | 2 | Spectral | $\mathrm{x}$ | 5.46 | 1.29 | 0.0 | 3.97 | 5.72 | 44.05 | 42.76 | - | - |
| 1995 | 2 | Spectral | $\mathrm{x}$ | 14.2 | 3.0 | 0.0 | 4.41 | 2.26 | 44.11 | 47.11 | - |  |
| 2009 | 2 | Spectral | $\mathrm{x}$ | 11.68 | 0.39 | 0.0 | 2.25 | 9.3 | 46.64 | 46.25 | - | - |
| 1989 | 3 | K-Means |  | 12.11 | 4.24 | 0.19 | 4.51 | 1.65 | 41.64 | 47.44 | 48.0 | - |
| 1995 | 3 | $\mathrm{~K}-\mathrm{M}$ |  | 47 | 5.15 | $1.2 ?$ | 5.23 | 0.96 | 46.35 | 49.11 | 41. | - |
| 2009 | 3 | K-Means |  | 0.06 | 2.61 | 0.0 | 2.89 | 0.94 | 48.59 | 45.16 | 49 . |  |
| 1989 | 3 | Spectral |  | 1.81 | 4.66 | 0.01 | 4.83 | 1.4 | 47.46 | 41.69 | 40.47 | - |
| 1995 | 3 | Spectral |  | 5.56 | 2.24 | 0.0 | 2.91 | 3.86 | 45.04 | 41.82 | 41.68 | - |
| 2009 | 3 | Spectral |  | 11.11 | 2.51 | 0.0 | 2.57 | 1.09 | 48.81 | 45.04 | 46 | - <br> - |
| 1989 | 3 | K-Means | $\mathrm{x}$ | 1.78 | 4.95 | 0.5 | 5.01 | 0.88 | 46.66 | 48.78 | 41 | - |
| 1995 | 3 | K-Mean: | $\mathrm{x}$ | .99 | 4.45 | 0.0 | 4.83 | 1.08 | 47.42 | 41.86 | 48. | - |
| 2009 | 3 | K-Means | $\mathrm{x}$ | 10.17 | 2.88 | 0.43 | 3.03 | 1.17 | 48.47 | 45.11 | 49.43 | - |
| 1989 | 3 | Spe | $\mathrm{x}$ | 58 | 4.32 | 0.1 | 4.71 | 2.33 | 41.18 | 46.88 | 47 | - <br> - <br> -10 |
| 1995 | 3 | Spect | $\mathrm{x}$ | 13.93 | 5.11 | 0 . | 5.42 | 1.48 | 44.16 | 41.73 | 49 | _ |
| 2009 | 3 | Spectral | $\mathrm{x}$ | 10.97 | 2.1 | 0.0 | 2.47 | 1.43 | 45.42 | 46.36 | 48.57 | 5 |
| 1989 | 4 | K-Me |  | 86 | 4.38 | 0.14 | 4.58 | 1.77 | 48.51 | 41.28 | 44 | 47.05 |
| 1995 | 4 |  |  | .09 | 3.38 | 0 . | 3.73 | 1.39 | 42.62 | 48.68 |  | 47.71 |
| 2009 | 4 | K-Means |  | 10.73 | 2.8 | 0.45 | 2.97 | 1.57 | 47.6 | 44.85 | 50.31 | 48.05 |
| 1989 | 4 | Spectral |  | 2.23 | 4.33 | 0.2 | 4.39 | 1.6 | 41.25 | 47.21 | 49.12 | 44.86 |
| 1995 | 4 | Spectral |  | 5.09 | 3.78 | 0.0 | 4.32 | 3.54 | 44.62 | 41.73 | 1.73 | 48.32 |
| 2009 | 4 | Spectral |  | 10.73 | 2.46 | $0 .($ | 2.76 | 1.72 | 48.91 | 45.32 | 45.0 | 48.37 |
| 1989 | 4 | II | $\mathrm{x}$ | 4.65 | 4.33 | 1.2 | 4.35 | 0.83 | 41.21 | 47.53 | 79 | 43.96 |
| 1995 | 4 | $M_{0}$ | $\Lambda$ | 11.93 | 4.14 | 0.7 | 4.37 | 1.75 | 41.41 | 47.73 | 7 | 49.11 |
| 2009 | 4 | K-Means | $\mathrm{x}$ | 12.22 | 2.14 | 0.0 | 2.28 | 0.65 | 45.35 | 48.75 | 44.57 | 45.04 |
| 1989 | 4 | Spect | $\mathrm{x}$ | 12.36 | 3.53 | 0.25 | 4.12 | 3.85 | 46.28 | 47.44 | 40 | 47.57 |
| 1995 | 4 |  | $\mathrm{x}$ | 15.73 | $1.9 !$ | 0 . | 2.52 | 2.81 | 45 | 41.74 | 41.55 | 41.47 |
| 2009 | 4 | Spectral | $\mathrm{x}$ | 11.59 | 2.04 | 0.0 | 2.19 | 1.7 | 48.76 | 44.93 | 46.35 | 45.58 |

Table 13: $\sigma$ is the mean of all cluster price standard deviations, $\Delta_{\mu}$ is the average distance between cluster mean prices, $\Delta_{\min }$ is the mean nearest neighbour cluster distance, $\Delta_{\text {avg }}$ denotes the average distance between all points situated in different clusters, and $D B$ is the Davies-Bouldin index. $D B$ has values in $[0, \infty)$ and measures the average similarity of every cluster with its most similar cluster. A low $D B$ index indicates a good clustering. $\mu_{i}$ denotes the mean price of cluster $i$. All metrics were computed considering the yearly average price for each node.

## D. Clusterings visualization based on Rand indices



Figure 9: $\mathrm{RI}=0.44$ - left: D3 (spectral); right: Spectral Clustering based on prices; $k=3,2009$


Figure 10: $\mathrm{RI}=0.69$ - K-Means based on prices; $k=3$; left: 1989, right: 1995


Figure 11: RI $=0.83$ - K-Means based on prices; $k=4$; left: 1989, right: 2009


Figure 12: $\mathrm{RI}=0.93$ - K-means based on prices and geographic coordinates; $k=3$; left: 1989, right: 2009

## E. Single-day clustering analysis

The time granularity of the prices included in the clustering computation influences the stability of the resulting clusterings. In what follows, we analyze the stability of the clusterings identified given the prices corresponding to a single day. We select the day of January 22, 1989, and compute clusterings using K-Means and Spectral Clustering. As clustering feature(s), we consider (1) the time series of prices of a node (12 hours, i.e., 12 features) and (2) the time series of prices of a node and its geographic coordinates.

Table 14 shows the values of the inter- and intra-cluster similarity metrics introduced in Section 3.2.1. We observe the average distances between cluster mean prices $\left(\Delta_{\mu}\right)$ and the average distances between all points situated in different clusters ( $\Delta_{\text {avg }}$ ) are considerably lower compared to the values shown in Table 13, indicating that the clusters are similar to each other and thus not well-defined. We recall that the results illustrated in Table 13 correspond to clusterings obtained considering the annual time series of nodal prices as clustering features. With time series of smaller length, clusterings appear to be less stable.

| $k$ | Alg. | Loc. | $\sigma$ | $\Delta_{\mu}$ | $\Delta_{\min }$ | $\Delta_{\text {avg }}$ | $D B$ | $\mu_{1}$ | $\mu_{2}$ | $\mu_{3}$ | $\mu_{4}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 2 | K-Means |  | 12.78 | 0.81 | 0.0 | 0.8 | 0.94 | 56.31 | 57.12 | - | - |
| 2 | K-Means | $\mathrm{x}$ | 16.17 | 0.39 | 0.0 | 0.56 | 2.03 | 56.35 | 56.74 | - | - |
| 2 | Spectral |  | 13.23 | 0.76 | 0.0 | 0.78 | 1.01 | 56.32 | 57.08 | - | - |
| 2 | Spectral | $\mathrm{x}$ | 11.28 | 0.33 | 0.0 | 0.39 | 0.73 | 56.43 | 56.1 | - | - |
| 3 | K-Means |  | 11.16 | 0.73 | 0.09 | 0.75 | 0.83 | 56.34 | 56.07 | 57.17 | - |
| 3 | K-Means | $\mathrm{x}$ | 10.38 | 0.23 | 0.0 | 0.34 | 1.09 | 56.43 | 56.4 | 56.08 | - |
| 3 | Spectral |  | 12.62 | 0.77 | 0.0 | 0.78 | 1.04 | 56.36 | 57.13 | 55.97 | - |
| 3 | Spectral | $\mathrm{x}$ | 13.44 | 0.47 | 0.0 | 0.55 | 1.71 | 56.39 | 56.78 | 56.07 | - |
| 4 | K-Means |  | 12.88 | 0.57 | 0.08 | 0.57 | 1.11 | 56.61 | 56.13 | 57.23 | 56.47 |
| 4 | K-Means | $\mathrm{x}$ | 12.94 | 0.3 | 0.0 | 0.39 | 5.21 | 56.68 | 56.08 | 56.35 | 56.33 |
| 4 | Spectral |  | 13.02 | 0.67 | 0.0 | 0.68 | 0.94 | 56.39 | 57.2 | 55.97 | 56.08 |
| 4 | Spectral | $\mathrm{x}$ | 14.52 | 0.16 | 0.0 | 0.27 | 3.11 | 56.29 | 56.14 | 56.44 | 56.35 |

Table 14: $\sigma$ is the mean of all cluster price standard deviations, $\Delta_{\mu}$ is the average distance between cluster mean prices, $\Delta_{\min }$ is the mean nearest neighbour cluster distance, $\Delta_{\text {avg }}$ denotes the average distance between all points situated in different clusters, and $D B$ is the Davies-Bouldin index. $D B$ has values in $[0, \infty)$ and measures the average similarity of every cluster with its most similar cluster. A low $D B$ index indicates a good clustering. $\mu_{i}$ denotes the mean price of cluster $i$. All metrics were computed considering the yearly average price for each node.


[^0]:    ${ }^{*}$ Corresponding author

    Email addresses: dobos@cit.tum.de (Teodora Dobos), bichler@cit.tum.de (Martin Bichler), knoerr@cit.tum.de (Johannes Knörr)

[^1]:    ${ }^{1}$ We will use the terms price zone and bidding zone interchangeably.

[^2]:    $\sqrt[2]{\text { https://www.bundesnetzagentur.de/ }}$

    3 https://www.cleanenergywire.org/news/southern-and-western-states-oppose-splitting-germanys-pow er-price-zone

    ${ }^{4}$ The threshold depends on the number of price zones under analysis and is between $7 \%$ and $10 \%$ of the nodes.

    ${ }^{5}$ https://www.tennet.eu/news/bidding-zone-review-tsos-investigate-alternative-bidding-zone-configurations

[^3]:    ${ }^{6}$ This means that we do not include constraints in the clustering computation such that we obtain balanced clusters in terms of either the number of nodes or geographical coverage.

    https://www.energiewechsel.de/KAENEF/Navigation/DE/Energiewechsel/Erneuerbare-Energien/erneuerb are-energien.html

[^4]:    ${ }^{8}$ Note that, similar to $\sigma_{i}, \mu_{i}$ is computed based on the vectors containing the time series of prices corresponding to the nodes assigned to $C_{i}$.

[^5]:    ${ }^{9}$ The diameter of a cluster is the maximum distance between any two points assigned to this cluster.

[^6]:    ${ }^{10}$ The datasets can be accessed at https://www. entsoe.eu/network_codes/bzr/ (January 2024).

[^7]:    ${ }^{11}$ https://www.jao.eu/static-grid-model

[^8]:    ${ }^{12}$ We also imposed a threshold related to the minimum number of nodes to be included in a zone.

[^9]:    ${ }^{13}$ https://www.energy-charts.info/charts/price_average_map/chart.htm?I=en\&c=DE\&year=2018\&interval =year

