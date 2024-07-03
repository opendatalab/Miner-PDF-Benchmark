# The Echo Chamber Effect Resounds On Financial Markets: A Social Media Alert System For Meme Stocks

Ilaria Gianstefania,∗, Luigi Longoa, and Massimo Riccabonia aInstitute for Advanced Studies Lucca, Piazza S.Francesco, 19, 55100 Lucca (LU)
March 28, 2022

## Abstract

The short squeeze of Gamestop (GME) has revealed to the world how retail investors pooling through social media can severely impact financial markets. In this paper, we devise an early warning signal to detect suspicious users' social network activity, which might affect the financial market stability. We apply our approach to the subreddit *r/WallStreetBets*, selecting two meme stocks (GME and AMC) and two non-meme stocks (AAPL and MSFT) as case studies. The alert system is structured in two stpng; the first one is based on extraordinary activity on the social network, while the second aims at identifying whether the movement seeks to coordinate the users to a bulk action. We run an event study analysis to see the reaction of the financial markets when the alert system catches social network turmoil. A regression analysis witnesses the discrepancy between the meme and non-meme stocks in how the social networks might affect the trend on the financial market. Keywords: Market manipulation, Social network analysis, Alert system, Event study, Reddit.

JEL codes: G14; G18; G41; 039.

## 1 Introduction

Retail investors have always been considered as noise traders in the financial and market microstructure literature: their choices are not driven by the knowledge of the fundamentals of a stock or any sophisticated analysis of the market, but they are guided mainly by their emotional and irrational beliefs. Noise traders market impact has always been considered negligible compared to the influence of large players (such as investment banks and hedge funds). However, this picture of nonthreatening amateur investors seems outdated: the progressive diffusion of social media combined with low cost trading platforms are making investment strategies more and more widespread. The impact they have on the financial market is anything but negligible. The most striking episode is the shortsqueeze that some retail investors triggered on GameStop stock (ticker symbol on NYSE: GME) by coordinating themselves on Reddit, a micro-blogging social network (Anand and Pathak, 2021).

Reddit is a website1composed of user-generated content and related discussions. The site's content is divided into forums, communities known as "subreddits", which deal with a specific topic. As a network of communities, Reddit's core content consists of posts (submissions) from its users. Users can comment on others' posts to continue the conversation, and they can collect positive or negative votes (score). The number of upvotes or downvotes determines the posts' visibility on the site; the more popular the content is, the higher the number of people it is displayed.

One of the most popular and active subreddit is *r/WallStreetBets*, a community focused on financial markets and stock trading. In this community, users boast very aggressive trading strategies and what they did at the end of January 2021 with GameStop is no exception. GameStop (GME) is the world's largest American retailer of video games and accessories. The market for physical video games started its decay in 2017 due to the downloadable version of many games and services offered by the main consoles.

GameStop started facing a sharp decline in sales that determined a share-price dropping in the financial market. The COVID-19 pandemic was a severe beating for the company, and its fundamentals faced another shock. The stock price decline led many institutional investors to sell the stock short. Conversely, some retail investors, considering the stock undervalued, went against the trend of the big players. In January 2021, a coordinated effort orchestrated by the community of the subreddit r/WallStreetBets surged the price of GME (US Securities and Exchange Commission, 2021). Apart from what happened on the financial market, the squeeze of the price and the consequent losses faced by the short-sellers, the high volatility of traded volumes and the liquidity issues, the most striking part of this episode is to comprehend how an apparently harmless group of noise traders were able to provoke such a substantial effect on a market usually dominated by the big players.

Stylizing the phenomenon can be helpful to detect eventual anomalies based on indicators of coordination. This is relevant in a perspective of policy-making to prevent this kind of shock from happening or at least to tackle the harmful effects.

Besides the specific case of GameStop, which is dramatic in terms of magnitude and subsequent effects, the interest in how social media networks impact the financial price formation of meme stocks is gaining growing attention (Pedersen, 2021; Costola et al., 2021). Furthermore, an ever-increasing decentralization of the financial system and the ease to access it via user-friendly online trading platforms are potential destabilizers for the financial ecosystem2. The fintech (r)evolution and the capillary diffusion of the online social network, which allow us to receive the up-to-date information as they happen, lay the foundations for a reinterpretation of market manipulation steering through social networks. Hence, here is the urgent need to create an alert system to pinpoint episodes of misconduct behaviors in online social network that can result in potential market manipulation. With misconduct behaviors, in this paper we refer to an inappropriate activity at the social network level that might potentially translate into market manipulation, a deliberate attempt to interfere with the free and fair operation of the market.

Although there is no regulation legislating on the relationship between social media coordination and the financial market, the U.S. securities and exchange commission (SEC)
defines as market manipulation3 all the actions where someone artificially affects the supply or demand for a security. Social network variables on mass coordination are valuable tools for building nowcasting 2 systems and scheduling real-time interventions to ensure stability. Our paper contributes to the extant literature by designing an alert system to detect potential misconducting behaviors or suspicious activity on the social network to eventually prevent the harmful coordination from creating instability in financial markets. The methodology relies on social listening and social network analysis to identify the red light days to monitor. The rest of the paper proceeds as follows: Section 2 reviews the literature on the topic, Section 3 presents the data and their features, Section 4 describes the alert system we develop, and Section 5 introduces the empirical results. Finally, Section 6 concludes.

## 2 Literature Review

Digital and online social network revolutions are deeply affecting the functioning of financial markets. One manifestation of this revolution is the rising importance of retail traders. In the classical market microstructure models (Glosten and Milgrom, 1985; Kyle, 1985), noise traders are considered as a residual category because of their randomness in the trades and are usually ignored in the price formation process because of their irrational impact on the market (which temporary makes the price to diverge from the fundamental value) is predominated and counterbalanced by rational agents on the market.

One of the first models to recognize the relevance of noise traders in the financial ecosystem is the one described by De Long et al. (1990) where the authors model them as irrational traders with erroneous stochastic beliefs whose unpredictability creates a risk in the price of an asset. As a result, prices can diverge significantly from fundamental values even without fundamental risk. This paper was highly enlightened and forward-looking as it perceived how the agents, so far targeted as irrelevant, are effectively impacting the asset price formation in certain circumstances. Thanks to user-friendly, low-cost online trading platforms, the widespread diffusion of social media and the easiness of accessing financial markets have significantly transformed the market dynamics. As pointed out by Zheludev et al. (2014), the proliferation of the internet has improved our ability to access information in real-time, and in particular, the diffusion of social media allows us to get in contact with the moods, thoughts, and opinions of a large part of the world's traders in an aggregated and real-time manner. Many are the researches aim to analyze the impact of social media on the financial markets both under a perspective of the volume of the social activity, the search engine traffic, and the prevailing sentiment of the agents. A consistent branch of the literature focuses, using various techniques, on the impact of social media activity on the financial markets
(Mao et al., 2012; Bordino et al., 2012; Ruiz et al., 2012; Preis et al., 2013) . Most of the results presented so far are based on empirical extrapolation. In Renault (2018), the author focuses on a specific type of market manipulation: the pump-and-dump scheme. He finds that an abnormal activity on social media about a specific stock is associated with a sharp increase in volume and price on the day of the event, while the price presents a reversal over the following trading week. Pedersen (2021)
proposes a new model that revolutionizes the vision of the so-called noise traders. He describes how investment strategies propagate in a social network and how they affect the market. Four typologies of investors are considered: besides the classic prototypes of rational short- (who tries to predict the sentiment changes among naive investors based on social network dynamics) and long-term investor (focused on the fundamental value of assets), it portrays two new types of agents: the 'fanatics' (investors with a stubborn view that can influence many people thanks to their popularity on social media) and naive investors (agents learning and relying on investment strategies proposed on social networks). The model explains the belief formation process on the social network and how it affects the fluctuations of prices and trading volumes on the financial market. Modern social media, such as Reddit, allows envisioning (and downloading) the data generating process that leads to the coordination of the agents on the network and analyzes the underlying forces behind the event. To the extent of our knowledge, there are no works devoted to studying the network evolution and consequent market impact. Suppose social network activity does generate a force that drives the financial market dynamics. In such a case, the GameStop saga can be an exciting case study to understand the network indicators to monitor to prevent extreme phenomena like the one that happened at the end of January 2021. Hence, as recommended by Pedersen (2021) in the conclusion of his paper, the availability of data from social media might open *'new research possibilities to* test model's prediction using data on networks and market behaviors'.

Dim (2021) analyzes the implications on the financial markets of non-preofessional social media investment analysts that publish investment strategies shaping the views and actions of many retail investors. This study highlights how the interplay of social media and retail trading poses new challenges for financial markets and regulators, which requires a deeper understanding of belief formation on social media. Our paper works towards defining some indicators and parameters to monitor on the social network to detect extreme situations that might affects the financial market stability. Inspired by the setting proposed in Costola et al. (2021), our alert system has two consecutive red flags: if the first one, based on extraordinary activity on the social network, activates, we start monitoring the structure of the user social network.

In the network analysis, distinguishing the various roles the users can play is crucial. Many works are devoted to this categorization (R´ıos et al., 2019; Choi et al., 2015; Thukral et al., 2018). A special role is played by the influencers, aka the leaders, or to use a term proposed Pedersen (2021), the "fanatics". We track the users' activity within the network, catch the agents distinguishing for their ability to be central and vocal in the network by proposing relevant contributions. Before delving into the core of our paper, we cross-reference all the works dealing with the GameStop case, the triggering factor of this piece of literature devoted to creating an alert system to prevent the dysfunctional social network activity destabilizing the financial market. Investment recommendation (Bradley et al., 2021), social network activity volume and tone (obtained with sentiment analysis) (Long et al., 2021; Umar et al., 2021) influence the GME returns and traded volume on the financial market. Also, the Google trend researches with keywords related to the event are positively correlated with the financial GameStop performance (Klein, 2021; Vasileiou et al., 2021). Hasso et al. (2021) profile the agents participating in the frenzy and describe their average performance; they have proven to be relatively inexperienced and unsophisticated (Eaton et al., 2021).

Eaton et al. (2021) also infers that a large portion of agents acting on the subreddit r/WallStreetBets uses Robinhood as a trading app. Robinhood is a zero commission, no account minimum, and an easy-to-use interface trading app widely used among young investors. During the most turbulent period of GME frenzy, the trading app went down or malfunctioned several times, avoiding investors from acting on the financial market and loosing the best moments to trade. Many were the complains about this malfunction reported on a website *DownDetector.com*4, an online platform that provides users with information about the status of various websites and services based upon user outage reports.

The disruptive effect would have been milder if only the financial market presented more substantial barriers to entry. Finally, in Fusari et al. (2021), they report as a case study the extreme event of GME, demonstrating that they can predict the bubble using a model based on options.

## 3 Data

Our analysis is run on four NYSE-listed stocks in the period October 2020 - June 2021 for the following stocks (NYSE ticker is reported in parenthesis): GameStop (GME),
American Multi-Cinema Entertainment (AMC), Apple Inc. (AAPL) and Microsoft Corporation (MSFT). For each stock, we download the financial daily data on price and trading volume and all the post on the social network Reddit containing the ticker. GME
and AMC are two examples of meme stocks, meaning stock that gains popularity among retail investors through social media. As reported in US Securities and Exchange Commission (2021), a meme stock is characterized by a confluence of all these factors: large price moves, large volume changes, large short interest, frequent mentions on social media and significant coverage in the mainstream media. At the contrary, AAPL and MSFT
are two non-meme stock to use as controls.

## 3.1 Market Data

We download the time series with daily resolution of price and traded number of share
(volume) from October 1st 2020 to June 30th 2021. For each stock we compute the daily returns:

$$R_{t,s}=\frac{P_{t,s}-P_{t-1,s}}{P_{t-1,s}}\tag{3.1}$$

where Pt,s is the closing price of stock s on day t. The daily trading volume is denoted as V olt,s.

## 3.2 Reddit Data 7

Rooting our analysis in the theoretical framework proposed by Pedersen (2021), we design a model to study the interaction of agents on the social platform, evaluate their coordination effort and quantify the impact of their action on the financial market. Modern social media contain an outstanding informative potential related to the users' sentiment evolution and opinion formation. If properly squeezed, the confidential information can be a forerunner for upcoming events.

Relying on the informative power of the social network and with the help of PRAW (an acronym for 'Python Reddit API Wrapper', a Python package that allows accessing Reddit's API), we downloaded all the posts containing as keyword the ticker of the stock to investigate. We limit the data download to the subreddit *r/WallStreetBets* in the period from October 2020 to June 2021. For each post we obtained the related comment forests and attributes. We downloaded the data and run the analysis for the following keywords, standing for the stock tickers: GME, AMC, AAPL, and MSFT. Precisely, we extracted every post (in Reddit jargon 'Submission') satisfying the conditions above and the related comment tree.5 We are interested in the emerging collective phenomena when the retail investors cooperate to determine a significant effect on the financial market.

We exclude from our analysis the messages generated automatically from the bots (that in our dataset are denoted with the tag 'moderator' in the variable distinguished). A
conversation thread can be modeled as a directed tree T
k t,s = (Mk t,s, Ck t,s). Mk t,s the set of nodes represented by the messages in the tree k (where the initial submission represents the root of the tree and the comments are the following-up branching) and C
k t,s is the set of edges, each of them connecting two messages linked by commenting activity. The direction of the edge points to the parent node to which the comment is addressed. Figure 1 reports the number of daily posts (i.e. the number of trees) containing as keyword the ticker in the title of each subgraph and related comments (i.e. the number of nodes excluding the initial submission). Each subgraph has a double scale y-axis; on the left in red is the scale measuring the absolute value of daily submissions, on the right in blue is the corresponding measure for the number of related comments. We note that for the meme stocks (GME and AMC), the activity on the social network is massive compared to 5See the Appendix A for more details of downloaded data.

other well-known but not meme stocks (like AAPL and MSFT). Furthermore, when the social network is active on a specific topic, the correlation between creating new content and commenting activity is high. Similarly, Figure 2 shows the time series of the daily

![8_image_0.png](8_image_0.png)

number of users who write content containing the ticker in the title of each subgraph and the daily number of users who take part in the conversation threads. In red on the left is the y-axis for the submitters; in blue on the right side is the corresponding one for commenters. The analysis is ideally in line with the one done for Figure 1.

The social network data informativeness is not limited to its extent over time. It can be further squeezed by analyzing the interaction among users to identify their roles within the network.

## 3.2.1 Social Network Analysis

We extrapolate the daily agent interplay from the tree-level raw data by reconstructing their discussing interchanges. We define a network where the nodes represent the active 8

![9_image_0.png](9_image_0.png)

users on the day t, and the edges are users' interactions through the comments: the network structure is outlined by Gt,s = (Nt,s, Et,s). The set of active users on the day t for ticker s, Nt,s, represents the graph's nodes. The commenting activity establishes the links among them: Et,s is the set of directed edges from the user writing the comment to the author of the initial submission. Following R´ıos et al. (2019), we adopt a simplification in the user-network reconstruction
(see Figure 3): the links always point to the author of the initial submission even if the comment is a reply to a second or higher-order comment. The ratio underlying this network reduction is due to the need to identify the users acting like hubs, gaining popularity, consensus, and driving a potentially impactful movement with their contents.

In addition, the stylization is still a realistic representation of the social dynamic: when scrolling the blog, the user first reads the main submission; then, if attracted by the topic, she opens the cascade of comments. Our reduction considers all the comments as first-level comments. This structure emphasizes the submitter that becomes the central actor of a thread and, eventually, the driver of a particular message or idea. Figure 4 depicts an example of interaction among users. The network represents the interaction on Reddit on January 14st, 2021, based on submissions containing the ticker GME.

There are 6,465 users (represented by the nodes) interacting on the platform throughout commenting activity (the 8,741 edges connecting them). The social network has a huband-spoke structure, with the colored users representing the hubs (i.e., central nodes in the network). In Appendix B we report similar examples of networks for AMC, AAPL and MSFT.

![10_image_0.png](10_image_0.png)

## 4 Methodology

This section presents the backbone of our analysis. We describe the design and the functioning of the alert system to detect situations of misconducting behavior at social network level. Subsequently, we illustrate how we structure an event study analysis to check whether the alert system is capable of anticipating potential attempts of market manipulation.

## 4.1 Alert System

We devise an alert system based on social-network-retrieved information. Cooperation among users can translate into a dangerous impact on financial market stability. Detecting potential misconduct behaviors and anticipating a coordinated action concocted on social media might be beneficial for the financial market well-functioning. The alert system is query-dependent, meaning that we have to instruct the system on which keyword we want to monitor. For the sake of practical usability, two consecutive stpng compose the structure.

## 4.1.1 First Stage

The first stage of the alert system consists of a screening of the days where the tickerrelated activity on the social network is extensive compared to the previous days. We use the volume-related metrics to implement the first stage: we skim the days, identifying when ticker-related activity is extraordinary. Technically speaking, for every day and each ticker, we determine:

- The number of submissions citing the ticker in their content;
- The number of active users discussing that ticker;
- The overall6 activity on the subreddit, both in terms of submissions and users.
And construct the following variables:

(1) Relative number of daily submission: the ratio between the submissions citing ticker and the total submissions on the subreddit, to identify the portion of the activity on that topic during the day;
(2) Absolute number of daily submission: the total number of daily submissions about that ticker, to identify the magnitude of the movement in absolute terms;
(3) Relative percentage change in the number of daily submissions: the percentage variation of number of ticker-related submissions with respect to the previous day; 6Meaning the whole activity during the day on the subreddit *r/WallStreetBets*, not specifically related to a ticker.

(4) Relative number of daily users: the ratio between the number of users citing ticker and total users on the subreddit, to identify the portion of the community discussing that topic during the day;
(5) Absolute number of daily users: computed as the total number of daily users citing that ticker, to identify the magnitude of the user-trend in absolute terms;
(6) Relative percentage change in the number of daily users: the percentage variation of number of ticker-related users with respect to the previous day;
The first stage of the alert system switches on when at least four variables exceed their threshold. For the relative and the absolute number of daily submissions (users), variables
(1), (2), (4), (5), the threshold for the day t is the mean value of the variable over the previous ten days plus one mean absolute deviation computed over the same period. We define the mean value of the variable as

$$\bar{V}_{t,s}^{(v)}=\frac{1}{I}\sum_{i=1}^{I}V_{t-i,s}^{(v)}$$
$$(4.1)$$

The mean absolute deviation as

$$M A D(V_{t,s}^{(v)})=\frac{1}{I}\sum_{i=1}^{I}\left(V_{t-i,s}^{(v)}-\bar{V}_{t,s}^{(v)}\right)$$
$$(4.2)$$
$$(4.3)$$

Hence, the threshold is defined as

$$T_{t,s}^{(v)}=\bar{V}_{t,s}^{(v)}+M A D(V_{t,s}^{(v)})$$
t,s ) (4.3)
where v refers to the variables j = 1, 2, 4, 5, t indicates the day, s the ticker s =
GME, AMC, AAP L, MSF T and I is the length of the window over which we compute the threshold, in our case I = 10. For the relative percentage change in the number of daily submissions (users), variables (3) and (6), the threshold to overcome is 100%,
hence when on the day t they double the value with respect to the previous day t − 1.

When the social network conditions determine the activation of the alert, we approach the situation in a prudential and conservative way: we keep monitoring the stock until the average number of active indicators over the previous three days is below three. In this way, we keep controlling the situation even if it is not exceptional compared to the 12 earlier days, but it is still turbulent.

A single indicator (or variable) switches on when it overcomes its critical threshold defined in (4.3):

$$I_{V_{t,s}^{(v)}}=\begin{cases}1,&\text{if}V_{t,s}^{(v)}>T_{t,s}^{(v)}\\ \\ 0,&\text{otherwise}\end{cases}$$
$$(4.4)$$

The minimum alert-activation condition is:

$$\sum_{v=1}^{5}I_{V_{t,s}^{(v)}}\geq4$$
6
$$(4.5)$$
≥ 4 (4.5)
The alert remains on until the following condition verifies:

$${\frac{1}{3}}\sum_{i=1}^{3}\sum_{v=1}^{6}I_{V_{t-i,s}^{(v)}}\leq3$$
$$(4.6)$$

Step one of the alert system detects the days when the activity is exceptional, calling for further controls on the network structure.

## 4.1.2 Second Stage

The second stage of the alert system activates only for those days recognized as an alert state by the first one.

For each day selected by the first step, we reconstruct the network structure to model the interaction among the agents, Gt,s = (Nt,s, Et,s) in the manners set in the previous paragraph: the links always point to the author of the initial submission even if the comment is a reply to a second or higher-order comment. We also implement other filters in the network modeling: creating a nowcasting alert system requires the tool to be quick and smartly devised, beyond the fact that it has to detect the bigwigs. Hence, the network reconstruction is made of only the users whose submission obtained a score above the median and with a cascade of at least ten comments.

We now move to the detection of the users acting like leaders, able to gain trustworthiness, popularity, prestige, leadership, and authority, essential features for a virtual user to lead a movement that can translate its effects on the real economy.

We rank the users according to their in-degree centrality (fraction of nodes its incoming 13 edges are connected to) for each day in the subset of first-stage-detected days:

$$C_{D}(n^{(i)}_{t,s})=\frac{\sum_{j}a^{ij}_{t,s}}{N_{t,s}}\tag{4.7}$$

The indicator identifies the ten authors with the highest relative incoming links: users able to attract a vast portion of the community. To test whether the detected authors are trending and critically acclaimed, for each day t, we define a set of the most critical users according to the algorithm of PageRank (Page et al., 1999). We consider the network in the window [t − 20, t − 1] and identify the users who were standing out for the published content. According to the ranking, the first twenty users belong to the set of influencers at time t. We finally check whether some of the top in-degree centrality authors on the day t belong to the influencers set over the past twenty days7. If the intersection between the two sets is not empty, the second stage of the alert system switches on. The methodology narrows down the set of agents we monitor to avoid misconducting behaviors on the online social network and prevent repercussions on the financial stability. The method aims at pin down the users who might manage suspicious movements by promoting extreme investment strategies masked by financial pieces of advice. In a perspective of macroprudential stability, a regulatory authority using the tool can quickly pinpoint the users to check to analyze their contents throughout textual analysis tools and eventually ban the profiles.

## 4.2 Analysis Of Abnormal Returns

We finally check whether the algorithm based on social network analysis can adequately detect the financially unstable days. In order to evaluate the accuracy of our algorithm, we develop an event study analysis following MacKinlay (1997). We measure whether abnormal returns occur for the stock discussed in the Reddit community right after the alert turns on.

The abnormal returns are constructed by defining an estimation window that goes from T0 to T1, and an event date τ . The event window goes from T1 to T2 =. L1 = T1 − T0 and L2 = T2 − T1 are respectively the length of the estimation and the event window.

The abnormal returns are defined with the specification of the market model, to purge it by the market fluctuations:

$$AR_{\tau,s}=R_{\tau,s}-\hat{\alpha}_{s}-\hat{\beta}_{s}R_{\tau,m}\tag{4.8}$$

where Rτ,s is the return for security s at time τ , while Rτ,m is the market return. The parameters of the model are estimated via OLS over the estimation window [T0 : T1].

Under the null hypothesis, the abnormal returns, ARτ,s, are normally distributed with zero conditional mean and conditional variance σ 2(ARτ,s) is set to be the variance of the OLS residuals σ 2 εt
.

Under the null hypothesis, that event has no impact on the returns, the distribution of the abnormal returns in the event window is:

$$A R_{\tau,s}\sim N\left(0,\sigma^{2}\left(A R_{\tau,s}\right)\right)$$
$$(4.9)$$

ARτ,s ∼ N0, σ2(ARτ,s)(4.9)
The significance of the abnormal returns is tested via the non-parametric rank test by Corrado (1989). The abnormal returns are standardized as a ranked descending variable defined by:

$$K_{\tau,s}=\frac{\mathrm{rank}\left(A R_{\tau,s}\right)}{1+M_{s}}$$
$$(4.10)$$

where Ms are the the number of observations in the sample for security s. The ranked variable is uniformly distributed in a [0,1] interval.

The variance computed across all the stock s observations is:

$$S_{K}^{2}=\frac{1}{M_{s}}\sum_{t=0}^{T}\left(K_{s,t}-0.5\right)^{2}$$
$$(4.11)$$

where 0 and T stand for the first and last date of the sample. The significance is computed as a t-rank statistic for a standard uniform distribution with expected value of 0.5:

$$t_{\mathrm{rank}}\ =\left({\frac{K_{s,\tau}-0.5}{S_{K}}}\right)$$

These results can be used to make inference on the absolute returns for every security in the event window.

We also test the impact of the detected events on the trading volume. Specifically, we

$$(4.12)$$

15 consider the abnormal trading volume computed as the volume traded on a given day divided by the average volume traded on the estimation window [T0 : T1]. For each day τ , the abnormal trading volume is defined as:

$$AVol_{\tau,s}=\frac{Vol_{\tau,s}}{\frac{1}{L_{1}}\sum_{t=T_{0}}^{T_{1}}Vol_{t,s}}\tag{4.13}$$

## 5 Results

This section consists of an empirical application of the methodology we design in the previous section. We present the days spotted by the alert tool and evaluate the associated abnormal returns with an event study analysis. Subsequently, we provide a regression analysis to understand the main drivers of abnormal returns and how they differ between the meme and non-meme stocks. We find that social networks-related variables significantly explain the meme stock performance, while market-related variables primarily drive non-meme stocks.

## 5.1 Event Detection

In Figures 5, 6, 7, and 8 we report the daily time series of price and traded volume for the stocks under analysis, together with the the days the alert system detects extraordinary activity and cooperation on the social network. The alert tool identifies 21 suspicious movements on the social network for GME, 4 for AMC, 2 for AAPL, and 1 for MSFT.

GME is the stock facing the most incredible attention and chattering on social media. Let us consider the short squeeze that happened at the end of January 2020 as the most striking episode of social network cooperation impacting the financial economy. We appreciate that our alert tool can detect abnormal and suspecting movements on the network many days before the social coordination affects the financial market. In addition, the tool can narrow down the few users that drive the movement, simplifying the eventual inspection by a surveillance authority. In Table 1, we report all the dates and the users noticed by the alert system. The tool can trace the user acting like leaders for the movement.

In Appendix B, we show a user network to highlight how agents interacts on the social network.

Despite the lower media frenzy compared to GME, AMC experiences considerable attention on social media. Retail investors attempt a pump-and-dump scheme during the same days of the GME frenzy, but they create actual instability on the second mid of May 2021 when they considerably purge the price. The price has risen about seven times in ten days since the warning first lit on May 19th, 2021.

Unlike GME and AMC, the financial performance of prices and volumes of non-memestocks (AAPL and MSFT) is entirely unaffected by social media activity. Leading users ('fanatics') on social networks are aware that stocks with such high capitalization are challenging to implement pump-and-dump schemes or drive the price away from fundamental value. For this reason, the alert is rarely triggered and the identified alerting events are insignificant compared to those of meme-stocks.

## 5.2 Analysis Of The Abnormal Returns

The submissions from the influencers during the days of unusual activity, detected by the two stpng of the alert system, are considered as events potentially triggering a response in the financial market. We analyze abnormal returns constructed with a market model to evaluate whether the submission from the influencers triggers a reaction in the financial markets. For each detected event, i.e., when the alert system turns on (τ = 0), we compute the abnormal return on the estimation window [-21:-11], L1 = 10 and we consider as event window the period [-10:10], L2 = 21 trading days. The abnormal return is defined with a market model, specified in (4.8), with the CRSP index as a proxy for the market returns. We impose a minimum of 10 days between two events to avoid contagion on the event window and consider the events independent. If an event happens on a non-trading day, we consider the next trading day as the event date.

Under these conditions, we end up with eight events for GME, four events for AMC, two events for AAPL, and one for MSFT over the sample period. It is clear that influencers driving unusual activity on social are more present for memes than non-meme stocks.

Considering that Reddit users are mostly inexperienced retail investors, we assume they primarily trade with a long position on the stock. Indeed, their primary concern is to move the price up by massively buying the stock. For this reason, we report and evaluate the significance of the event that generates the highest positive abnormal returns in the ten 17

| GME             | AMC                             |                 |                             |
|-----------------|---------------------------------|-----------------|-----------------------------|
| Alert date (τ ) | Influencer(s)                   | Alert date (τ ) | Influencer(s)               |
| 09/11/2020      | DeNovaCain                      | 09/11/2020      | Killtrend                   |
| 10/11/2020      | Veryforestgreen                 | 31/01/2021      | dhiral1994 BrandinoGames    |
| 20/11/2020      | Neothedreamer Imboredsoyh       | 19/05/2021      | Realplayer16                |
| 21/11/2021      | Ackilles                        | 01/06/2021      | Nobjos                      |
| 22/11/2021      | Ackilles                        |                 |                             |
| 25//11/2021     | Ackilles                        |                 |                             |
| 27/11/2020      | SIR JACK A LOT                  |                 |                             |
| 26/12/2020      | Uberkikz11                      |                 |                             |
| 03/01/2021      | Uberkikz11                      |                 |                             |
| 14/01/2021      | DeepFuckingValue                |                 |                             |
| 18/01/2021      | Its-Loki                        |                 |                             |
| 19/01/2021      | Gardeeon DeepFuckingValue       |                 |                             |
| 21/01/2021      | Unlucky-Prize                   |                 |                             |
| 23/01/2021      | Unlucky-Prize                   |                 |                             |
| 25/01/2021      | DeepFuckingValue                |                 |                             |
| 28/01/2021      | DeepFuckingValue                |                 |                             |
| 29/01/2021      | DeepFuckingValue                |                 |                             |
| 09/03/2021      | dumbledoreRothIRA               |                 |                             |
| 15/04/2021      | OPINION IS UNPOPULAR            |                 |                             |
| 16/04/2021      | DeepFuckingValue                |                 |                             |
| 25/06/2021      | Chillznday # events = 21        | # events = 4    |                             |
| AAPL            | MSFT                            |                 |                             |
| Alert date (τ ) | Influencer(s)                   | Alert date (τ ) | Influencer(s)               |
| 24/12/2020      | Nafizzaki                       | 20/05/2021      | Mysterious—- EmphasisOk3036 |
| 22/06/2021      | Tilthefatladysings # events = 2 | # events = 1    |                             |

days after. Results are reported only for the case of meme stock. The event for the nonmeme stock does not generate a clear upward trend after the submission, although some abnormal returns are significant. The events reported for GME and AMC are respectively submissions by *u/DeepFuckingValue* on January 14th, 2021 and by *u/realplayer16* on May 19th, 2021.

| Day (τ )   | ARGME,t   | CARGME,t   | AV olGME,t   |
|------------|-----------|------------|--------------|
| -10        | 0.012     | 0.012      | 0.464        |
| -9         | -0.009    | 0.004      | 0.651        |
| -8         | -0.075    | -0.072     | 1.001        |
| -7         | 0.013     | -0.057     | 0.494        |
| -6         | 0.057     | -0.0009    | 0.551        |
| -5         | -0.011    | -0.011     | 0.554        |
| -4         | -0.043    | -0.054     | 0.492        |
| -3         | 0.104     | 0.049      | 1.060        |
| -2         | -0.038    | 0.011      | 0.568        |
| -1         | 0.534∗∗   | 0.545      | 11.521       |
| 0          | 0.233∗    | 0.778      | 7.379        |
| +1         | -0.152    | 0.626      | 3.801        |
| +2         | 0.078     | 0.704      | 6.117        |
| +3         | -0.030    | 0.674      | 2.657        |
| +4         | 0.082     | 0.756      | 4.571        |
| +5         | 0.493∗    | 1.249      | 17.338       |
| +6         | 0.164∗    | 1.412      | 16.173       |
| +7         | 0.935∗∗   | 2.347      | 20.292       |
| +8         | 1.349∗∗   | 3.697      | 11.961       |
| +9         | -0.443∗∗  | 3.253      | 7.463        |
| +10        | 0.630∗∗   | 3.883      | 2.503        |

| Day (τ )   | ARAMC,t   | CARAMC,t   | AV olAMC,t   |
|------------|-----------|------------|--------------|
| -10        | -0.012    | -0.012     | 0.710        |
| -9         | -0.016    | -0.028     | 1.069        |
| -8         | 0.054∗    | 0.026      | 0.982        |
| -7         | 0.020     | 0.045      | 1.067        |
| -6         | 0.012     | 0.057      | 1.156        |
| -5         | -0.0005   | 0.057      | 1.267        |
| -4         | 0.217∗∗   | 0.274      | 6.972        |
| -3         | 0.007     | 0.281      | 5.024        |
| -2         | 0.072∗    | 0.353      | 4.001        |
| -1         | 0.0007    | 0.354      | 4.438        |
| 0          | −0.098    | 0.256      | 2.277        |
| +1         | -0.007    | 0.248      | 1.569        |
| +2         | -0.031    | 0.217      | 1.329        |
| +3         | 0.135∗∗   | 0.353      | 2.866        |
| +4         | 0.202∗∗   | 0.555      | 5.241        |
| +5         | 0.203∗∗   | 0.758      | 9.941        |
| +6         | 0.365∗∗   | 1.123      | 18.382       |
| +7         | -0.033    | 1.090      | 10.702       |
| +8         | 0.202∗∗   | 1.293      | 6.592        |
| +9         | 0.919∗∗   | 2.212      | 8.603        |
| +10        | -0.215    | 1.996      | 5.868        |

Table 2 and 3 represents the abnormal returns, the cumulative abnormal returns and the abnormal volumes for the stocks GME and AMC over the event window [-10:10]. The event window presents significant abnormal returns for both stocks, but the significance is generally higher for GME and more concentrated after the event. Interestingly, in both stocks, we find a clear upward trend of the abnormal returns after the event, perfectly in line with the assumptions that users are coordinated on the Reddit community to buy the stock massively. Figure 9 corroborates the claim.

In Figure 10 we report the graphical representation of the event analysis for the abnormal volume (last column of Tables 2 and 3). In line with the analysis of (cumulative)
abnormal returns, the abnormal volume has a similar reaction after the event happens.

It presents a significant upward trend after detecting unusual and cooperative activity on the social network.

20 Overall, the event analysis suggests significant abnormal returns following the alert dates for the meme-stock only, GME and AMC. The alert for non-meme stocks (AAPL and MSFT) turns on rarely and without generating abnormal returns. The alert results mark significant differences between the meme and non-meme stocks. When the alert system turns on for the meme stocks, it is related to an attempt by retail traders to coordinate an action to drive the stock market price up. The alert system on the non-meme stock detects agents on the social network discussing the stock's performance without necessarily coordinating moves onto the market.

## 5.3 Regression Analysis

In this section we focus on the differences between the meme and non-meme stocks' abnormal returns. In particular, we assess the dependence between abnormal returns and social network-retrieved information, finding different patterns for the two stocks' categories. We run a time-series regression of abnormal stock returns on social networkrelated variables, controlling for market-related and stock-specific variables.

The contemporaneous regression is estimated via OLS with HAC estimator for the variance by Newey and West (1987) for each stock s:
ARt,s = αs+V olt,s+P
O
t,s+ARt−1,s+Rept+SubRankt+ABNt,s+Ot,RH+ABNt,s×Ot,RH+εt,s
(5.1)
Stock-specific financial variables are the transaction volume V olt,s and the stock openprice P
O
t,s; they enter the regression in the first difference to mitigate non-stationarity and trends. The lagged term for the abnormal returns ARt−1,s is included. We also include some subreddit specific variables: the variable Reptis the daily number of reports of non-functioning of the RobinHood trading application, which is very popular among young retail investors. The data is downloaded from DownDetector.com, an online platform that provides users with real-time information on various websites and services.

SubRanktis a metric computed internally by Reddit to compare the popularity across the various communities as a function of its users. For each community, they compute the number of subscribers and their popularity (according to the karma, the number of upvotes,..) and they rank the subreddits according to this indicator. Hence, the lower 21 the metric, the higher is the popularity of the subreddit. See Appendix C.

O*t,RH* is a dummy assuming a value of 1 when the website DownDetector.com reports the presence of malfunctioning of RobinHood. According to DownDetector.com, malfunctioning is related to the platform's outages or generic problems in the service (like Robinhood being slow in placing trades' orders)8.

The stock-specific social-network-related variable ABNt,s is the average branching number, a proxy of the daily virality of the comment-trees. The proxy of virality is inspired by Choi et al. (2015) where conversations' thread are defined as tree T
k t,s. The average branching number (virality) quantifies on average how many comments a node generates.

It is computed as the average number of children at each (non-leaf) node: number of non-root nodes (the volume of the tree minus one Mk t,s − 1, namely the number of edges)
divided by the number of non-leaf nodes (the number of nodes with children). In the equation (5.1) the average branching number interacts with the dummy O*t,RH*.

| Meme stock                                                         | Non meme stock   |           |            |            |
|--------------------------------------------------------------------|------------------|-----------|------------|------------|
| GME                                                                | AMC              | AAPL      | MSFT       |            |
| αt,s                                                               | 0.0262           | -0.0267   | 0.0021     | 0.0007     |
| (0.657)                                                            | (-1.559 )        | (1.464)   | (0.485)    |            |
| Volt,s                                                             | 0.0609∗∗∗        | 0.1791∗∗∗ | -0.0033∗∗  | -0.0041∗∗∗ |
| (3.026)                                                            | (4.358)          | (-1.976)  | (-3.573)   |            |
| P t,s                                                              | 0.1162∗∗∗        | 0.0469∗   | 0.0099∗∗∗  | 0.0066∗∗∗  |
| O                                                                  | (5.254)          | (1.878)   | (6.361)    | (3.408)    |
| ARt−1,s                                                            | -0.0597          | 0.0600    | -0.3247∗∗∗ | -0.2589∗∗  |
| (-0.551)                                                           | (0.878)          | (-3.320)  | (-2.126)   |            |
| Rept                                                               | 0.5224∗∗         | 0.5826∗∗∗ | 0.0026     | 0.0135∗∗∗  |
| (2.260)                                                            | (2.659)          | (0.363)   | (2.718)    |            |
| SubRankt                                                           | 0.0168∗∗         | 0.0204∗∗  | -0.0019    | -0.0019∗   |
| (2.121)                                                            | (2.009)          | (-1.493)  | (-1.860)   |            |
| ABNt,s                                                             | -0.0161          | 0.0026    | -0.0002    | 0.0008     |
| (-1.067)                                                           | (0.423)          | (-0.268)  | (0.674)    |            |
| Ot,RH                                                              | -0.2097∗∗        | -0.0815   | -0.0164∗∗∗ | -0.0003    |
| (-2.171)                                                           | (-1.648)         | (-3.834)  | (-0.099)   |            |
| ABNt,s × Ot,RH                                                     | 0.0738∗∗         | 0.0632∗∗  | -0.0513∗∗∗ | -0.0013    |
| (2.000)                                                            | (2.333)          | (-3.313)  | (-0.791)   |            |
| Observations:                                                      | 166              | 166       | 166        | 166        |
| Adjusted R2 :                                                      | 0.459            | 0.618     | 0.192      | 0.190      |
| AIC:                                                               | -118.5           | -92.07    | -884.6     | -947.6     |
| t statistics in parentheses * p < 0.05, ** p < 0.01, *** p < 0.001 |                  |           |            |            |

Table 4 summarizes regression results. The variable *Subrank*t presents significant and positive coefficients for the meme-stock, while it is negative and significant only for MSFT. An increase in the average rank of users on the Wallstreetbets community positively impacts the abnormal returns, meaning that the prestige of the users relates to a positive increase in the abnormal returns of the meme-stocks. The same does not happen for the non-meme stocks. The number of Robinhood outage reports has a positive and significant effect on the abnormal returns for the meme-stock. The effect of reports for AAPL is not significant, while for MSFT is still positive and significant, but lower in magnitude than the meme-stocks. The increase in the number of reports may be related to high activity in the stock market for buying stock discussed on the Wallstreetbets community. This effect is associated with an increase in abnormal returns, and it is even more marked for the meme-stock. Interestingly, the daily virality of the comment trees positively impacts the abnormal returns during the day of outages of the Robinhood platform. While interacting the average branching number with outages positively impacts abnormal returns for GME, the dummy outages alone is associated with negative abnormal returns. Intuitively, this might be related to big players' moves on the GME
stock. During the Robinhood outages, banks and hedge funds operated in the market without the noisy traders that usually invest through the Robinhood platform. Their action is associated with a fall in price. Indeed, during the day of the GME squeeze -
where the price peaked and started to fall vertiginously - the Robinhood platform was shut down. As the average branching number (virality) is related to the higher activity of the users on the Wallstreetbets community, considering it during the platform outages, may disentangle the effect of noisy traders rather than big corporations on the stock.

The price of the stock increase during days of high virality and platform outages, which might be related to the noisy traders' action. The coefficient on the transaction volume is negative for the non-meme stock, and in line with the standard liquidity theory9: a higher trading volume commands a lower expected stock return because liquidity is a desired stock feature for a risk-averse agent10. For the meme-stock case, the transaction volume has an unexpected significant positive effect on abnormal returns11.

To evaluate the echo chamber effects from Reddit to the stock market, we run a regression with the abnormal volume as a dependent variable: To evaluate the role of users in trading the meme and non-meme stocks, we run a regression where the dependent

$$AV_{t,s}=\alpha_{s}+Vol_{t,s}+P_{t,s}^{C}+AV_{t-1,s}+Sub_{t}+O_{t,RH}+Sub_{t}\times O_{t,RH}\tag{5.2}$$

The close price P
C
t,s is used as a regressor. The variable Subt represents the total number of subscribers to the Wallstreetbets community each day, and interacts with the dummy outages.

| Meme stock                                                         | Non-meme stock   |           |           |           |
|--------------------------------------------------------------------|------------------|-----------|-----------|-----------|
| GME                                                                | AMC              | AAPL      | MSFT      |           |
| αt,s                                                               | 0.1862∗∗         | 0.3565∗∗∗ | 0.0321∗∗∗ | 0.0373∗∗∗ |
| (2.539)                                                            | (3.058)          | (2.926)   | (2.661)   |           |
| Volt,s                                                             | 1.0646∗∗∗        | 0.2971∗∗∗ | -0.0033∗∗ | 0.2858∗∗∗ |
| (4.1555)                                                           | (8.350)          | (45.209)  | (63.264)  |           |
| P t,s                                                              | 0.0806           | -0.1437∗  | 0.0038    | -0.0004   |
| C                                                                  | (1.412)          | (-1.879)  | (0.956)   | (-0.137)  |
| AVt−1,s                                                            | 0.7315∗∗∗        | 0.0600    | 0.9596∗∗∗ | 0.9618∗∗∗ |
| (12.025)                                                           | (9.396)          | (73.303)  | (63.706)  |           |
| Subt                                                               | 0.0219           | -0.0109   | -0.0023   | -0.0010   |
| (0.464)                                                            | (-0.120)         | (-0.618)  | (-0.345)  |           |
| Ot,RH                                                              | 0.4222∗          | 0.1663    | 0.0062    | 0.0028    |
| (1.875)                                                            | (1.016)          | (0.906)   | (0.422)   |           |
| Subt × Ot,RH                                                       | -0.3487∗         | -0.2621   | 0.0038    | -0.0001   |
| (-1.908)                                                           | (-1.483)         | (0.542)   | (-0.017)  |           |
| Observations:                                                      | 166              | 166       | 166       | 166       |
| Adjusted R2 :                                                      | 0.759            | 0.731     | 0.977     | 0.989     |
| t statistics in parentheses * p < 0.05, ** p < 0.01, *** p < 0.001 |                  |           |           |           |

Table 5: Contemporaneous regression of daily abnormal volume. In each column the dependent variable is the abnormal volume AVt,s and the independent variables are stock or subreddit specific characteristics. The regression is estimated via OLS with HAC
estimator for the standard errors.

Interestingly, the market variables are highly significant for the non-meme stock
(mainly because they are less volatile and less driven by social networks-related variables), pushing towards the adjusted R2. The striking part of Table 4 is the first column, where the dependent variable is the abnormal volume for GME. The coefficient on outages is positive: this means that big corporations invested in the stock during the Robinhood 25 shutdown. The effect on the price was negative (Table 3): this led us to think that noisy traders on Reddit essentially move the price forward by massively buying the stock.

At the same time, big banks and hedge funds drove the fall in price on January 29th
(short-squeeze) when the platform was shut down. The number of subscribers during the Robinhood outages negatively impacts the abnormal volume; therefore, higher activity on the Wallstreetbets community is not associated with higher transaction volumes when Robinhood is shut down. This confirms that investors are inexperienced and noisy traders who mainly use the platform Robinhood to buy the stock.

## 6 Final Discussion

Social media are a powerful and impacting tool to disseminate information and stir a vast mass of people. This paper provides empirical evidence of the echo chamber effect on the financial market from the social network, a form of market manipulation (albeit indirect). Reddit and, in general, social media are great places to share advice and manipulate poorly-informed, unsophisticated, and prone to be convinced investors.

We provide evidence that the manipulators, or to use a word a l`a Pedersen, the fanatics can coordinate many naive investors to provoke the desired stock price movement. The fanatics can effectively undermine the financial market stability by persuading inexperienced and easily reachable people.

We design an alert system to detect abnormal movement related to a specific stock on social media based on the extraordinary activity in terms of volume and the detection of a potential manipulator that coordinates the mass movement.

While it is far from our duty to evaluate whether the promotion and persuasion practice falls within the boundaries of the law, our consideration concerns the market microstructure models. In front of these episodes, the retail investors can no longer be relegated to a residual category of 'noise traders', but models should consider that many small and apparently harmless investors if aggregated and coordinated, can generate a disruptive effect on the financial market.

In the end, the entire analysis spots significant differences between the meme and nonmeme stocks. The detection system finds alerts for both categories. Still, they never turn into abnormal returns for the non-meme stocks, suggesting fewer chances of suspicious trading activity or market manipulation in those cases. Moreover, the regression analysis indicates that social network-retrieved information is significant for meme stock abnormal returns only, resulting in structural differences between the price formation of the two categories. Indeed, noisy traders may determine the price of meme stocks through social activity and potential coordination.

## Appendices A Data Download

For each tree, we have as many rows in the data frame as the number of comments, and each row contains the following information:

- title: the textual content of the initial submission;
- body: the textual content of the comment;
- name: the id of the author of the comment (each id is prefixed by 't1 ' to specify the author made a comment activity);
- parent id: the author of the parent comment to which the comment in question refers to (the parent id can be prefixed by 't1 ' if the author of the comment replies to an other comment or it can be prefixed by 't3 ' if the author of the comment replies to the top-level post, i.e. the submission);
- author name: the name of the author who post the initial submission;
- depth: the level of the comment tree at which the comment in question is located
(if a tree is composed by the initial submission only, the depth is 0; if the comment refers to the initial submission the depth is 1; if the comment refers to a comment in the first level, the depth is 2; and so on);
- score: the number of up-votes minus the number of down-votes obtained by the comment;
- score submission: the number of up-votes minus the number of down-votes obtained by the initial submission;
- upvote ratio: the percentage of upvotes on the total votes received by a submission;
- time submission: date and time at which the initial submission is published; - time comment: date and time at which the comment is published;
- num comment: number of comments below the initial submission that compose the tree;
- flair: a tag used to categorize the post according to the topic it deals with; they are subreddit specific and in the case of the subreddit *r/WallStreetBets* the users can select among the following ones:
- YOLO, the acronym for 'You Only Live Once, it can be used for posts presenting extremely aggressive investment strategies with a consistent value at risk;
- DD, the acronym for Due Diligence, must be applied to post presenting research on a specific company/sector/trade. It should include sources and citations;
- Discussion, an idea or article that you would like to talk about;
- Gain, to show off a solid winning trade;
- Loss, to show off a brutal, crushing loss;
- Earnings Thread, weekly earnings discussion thread or a specific earnings event;
- Daily Discussion, daily catch-all thread for discussions;
- Mods, only for official business.

- distinguished: if a bot automatically performs the commenting activity, the variable reports the wording 'Moderator', none otherwise, when a non-automatic user adds the comment.
Note that in the case of submission without comments below, the data frame has a single row with empty values for the comments-related variables.

## B The Social Network Of Reddit Users

In Figure 11, we present an example of network user graph on January 31st, 2021, where the main submissions contain the ticker AMC. There are 15.534 users (represented by the nodes) interacting among them on the platform throughout commenting activity (the 21.032 edges connecting them). The directed edges point from the comment's author to the author of the main submission. The peripheral nodes in the graph are the less connected users; in the central part of the network, the most connected and central users: the colored ones are the users with the highest in-degree centrality.

Figure 12 presents the network graph for AAPL a and MSFT on two alert dates, respectively June 22nd, 2021 for AAPL and on May 20th, 2021 for MSFT. Compared to the meme-stock case, the non-meme-stocks present a feeble activity on the social network even in extraordinary occasions that determine the alert activation.

## C Subscriber Rank

In Figure 13 we represent how the Reddit indicator 'Subscriber rank' varies over time, in the period 2013-2022.

## D Predictive Regression

This section aims at understanding whether social network information enhances the predictability of abnormal returns. We run a regression where future abnormal returns depend on market-related variables and variables from the social network.

ARt,s = αs + V olt−1,s + *V ol*t−2,s + P
O
t−1,s + P
O
t−2,s + rankt−1 + rankt−2 + Rept + εt,s (D.1)
The variable *rank*t represents the daily average rank between subscribers and users commenting on submissions.

| Meme stock                                                         |           |           |
|--------------------------------------------------------------------|-----------|-----------|
| GME                                                                | AMC       |           |
| αt,s                                                               | -0.0825∗  | -0.0942∗∗ |
| (-1.705)                                                           | (-2.602)  |           |
| Volt−1,s                                                           | 0.0350∗∗∗ | -0.0401   |
| (2.828)                                                            | (-1.063)  |           |
| Volt−2,s                                                           | 0.0157    | 0.0038    |
| (1.004)                                                            | (0.168)   |           |
| P t−1,s                                                            | -0.0341   | -0.0274   |
| O                                                                  | (-1.321)  | (-1.293)  |
| t−2,s                                                              | 0.0467∗∗  | 0.0212    |
| O                                                                  |           |           |
| P                                                                  | (2.529)   | (0.645)   |
| rankt−1,s                                                          | 0.0199∗∗  | 0.0252∗   |
| (2.042)                                                            | (1.663)   |           |
| rankt−2,s                                                          | 0.0040    | 0.0019    |
| (0.445)                                                            | (0.140)   |           |
| Rept,s                                                             | 0.6684∗∗  | 0.9110∗   |
| (2.290)                                                            | (1.697)   |           |
| Observations:                                                      | 164       | 164       |
| Adjusted R2 :                                                      | 0.243     | 0.211     |
| t statistics in parentheses * p < 0.05, ** p < 0.01, *** p < 0.001 |           |           |

Table 6: Predictive regression of daily abnormal return. In each column the dependent variable is the abnormal return ARt,s and the independent variables are the lagged stock or subreddit specific characteristics. The regression is estimated via OLS with HAC estimator for the standard errors.

We do not include non-meme stock results because they are not significant. The 1-day lagged volume is significant in predicting the abnormal returns of GME, while the 1-day lagged rank well predicts both GME and AMC abnormal returns. The number of reports remains significant when included in the regression with a positive coefficient. This regression shows how social network-retrieved information to standard market variables such as volume and stock price when predicting abnormal returns.

![33_image_0.png](33_image_0.png)

![34_image_0.png](34_image_0.png)

![34_image_1.png](34_image_1.png)

![35_image_0.png](35_image_0.png)

![35_image_1.png](35_image_1.png)

![36_image_0.png](36_image_0.png)

![37_image_0.png](37_image_0.png)

![37_image_1.png](37_image_1.png)

![38_image_0.png](38_image_0.png)

![39_image_0.png](39_image_0.png)

![39_image_1.png](39_image_1.png)

## References

Acharya, V., Pedersen, L., 2005. Asset pricing with liquidity risk. Journal of Financial Economics 77, 375–410.

Anand, A., Pathak, J., 2021. The role of reddit in the gamestop short squeeze. Economics Letters , 110249.

Bordino, I., Battiston, S., Caldarelli, G., Cristelli, M., Ukkonen, A., Weber, I., 2012. Web search queries can predict stock market volumes. PloS One 7, e40014.

Bradley, D., Hanousekb, J., Jamed, R., Xiaoe, Z., 2021. Place your bets? the market consequences of investment advice on reddit's wallstreetbets. - .

Choi, D., Han, J., Chung, T., Ahn, Y., Chun, B., Kwon, T., 2015. Characterizing conversation patterns in reddit: From the perspectives of content properties and user participation behaviors, in: COSN '15: Proceedings of the 2015 ACM on Conference on Online Social Networks, pp. 233–243. doi:10.1145/2817946.2817959.

Chordia, T., Subrahmanyam, A., Anshuman, V., 2001. Trading activity and expected stock returns. Journal of Financial Economics 59, 3–32.

Corrado, C.J., 1989. A nonparametric test for abnormal security-price performance in event studies. Journal of financial economics 23, 385–395.

Costola, M., Iacopini, M., Santagiustina, C.R., 2021. On the "mementum" of meme stocks. Economics Letters 207, 110021.

De Long, J., Shleifer, A., Summers, L., Waldmann, R., 1990. Noise trader risk in financial markets. Journal of Political Economy 98, 703––738.

Dim, C., 2021. Should retail investors listen to social media analysts? evidence from text-implied beliefs. - .

Eaton, G., Green, T., Roseman, B., Wu, Y., 2021. Zero-commission individual investors, high frequency traders, and stock market quality. - .

Fusari, N., Jarrow, R., Lamichhane, S., 2021. Testing for asset price bubbles using options data. Johns Hopkins Carey Business School Research Paper 20-12.

Glosten, L., Milgrom, P., 1985. Bid, ask and transaction prices in a specialist market with heterogeneously informed traders. Journal of Financial Economics 14, 71––100.

Hasso, T., M¨uller, D., Pelster, M., Warkulat, S., 2021. A note on gamestop, short squeezes, and autodidactic herding: An evolution in financial literacy? Finance Research Letters In press.

Klein, T., 2021. A note on gamestop, short squeezes, and autodidactic herding: An evolution in financial literacy? Finance Research Letters In press.

Kyle, A., 1985. Continuous auctions and insider trading. Economatrica 53, 1315––1336. Long, C., Lucey, B., Yarovaya, L., 2021. "i just like the stock" versus "fear and loathing on main street": The role of reddit sentiment in the gamestop short squeeze. Social Science Research Network preprint.

MacKinlay, A.C., 1997. Event studies in economics and finance. Journal of economic literature 35, 13–39.

Mao, Y.and Wei, W., Wang, B., Liu, B., 2012. Correlating s&p500 stocks with twitter data. - , –.

Newey, W.K., West, K.D., 1987. Hypothesis testing with efficient method of moments
estimation. International Economic Review , 777–787.

Page, L., Brin, S., Motwani, R., Winograd, T., 1999. The PageRank Citation Ranking:
Bringing Order to the Web. Technical Report 1999-66. Stanford InfoLab. URL: http:
//ilpubs.stanford.edu:8090/422/. previous number = SIDL-WP-1999-0120.

Pedersen, L., 2021. Game on: Social networks and markets. NYU Stern School of Business Forthcoming .

Preis, T., Susannah Moat, H., Stanley, E., 2013. Quantifying trading behavior in financial markets using google trends. Scientific Reports 3, 1684.

Renault, T., 2018. Market manipulation and suspicious stock recommendations on social media. (Forthcoming) .

Ruiz, E., Hristidis, V., Castillo, C., Gionis, A., Jaimes, A., 2012. Correlating financial time series with micro-blogging activity. - .

R´ıos, S., Aguilera, F., Nu˜nez-Gonzalez, J., Gra˜na, M., 2019. Semantically enhanced network analysis for influencer identification in online social networks. Neurocomputing 326, 71–81.

Thukral, S., Meisheri, H., Kataria, T., Agarwal, A., Verma, I., Chatterjee, A., Dey, L., 2018. Analyzing behavioral trends in community driven discussion platforms like reddit, in: 2018 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining (ASONAM), pp. 662–669. doi:10.1109/ASONAM.2018.8508687.

Umar, Z., Gubareva, M., Yousaf, I., Ali, S., 2021. A tale of company fundamentals vs sentiment driven pricing: The case of gamestop. Journal of Behavioral and Experimental Finance 30, 2214–6350.

US Securities and Exchange Commission, 2021. Staff report on equity and options market structure conditions in early 2021. - .

Vasileiou, E., Bartzou, E., Tzanakis, P., 2021. Explaining gamestop short squeeze using Ιntraday data and google searches. - .

Zheludev, I., Smith, R., Aste, T., 2014. When can social media lead financial markets?

Scientific Reports 4, 4213.