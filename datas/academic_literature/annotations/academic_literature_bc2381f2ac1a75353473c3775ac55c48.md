# Measuring Arbitrage Losses and Profitability of AMM Liquidity 

Robin Fritsch<br>ETH Zurich<br>Zurich, Switzerland<br>rfritsch@ethz.ch

Andrea Canidio<br>Cow Protocol<br>Lisbon, Portugal<br>andrea@cow.fi


#### Abstract

This paper presents the results of a comprehensive empirical study of losses to arbitrageurs (following the formalization of loss-versusrebalancing by [Milionis et al., 2022]) incurred by liquidity on automated market makers (AMMs). Through a systematic comparison between historical earnings from trading fees and losses to arbitrageurs, our findings indicate an insufficient compensation from fees for arbitrage losses across many of the largest AMM liquidity pools (on Uniswap). Remarkably, we identify a higher profitability among less capital-efficient Uniswap v2 pools compared to their Uniswap v3 counterparts.

Moreover, we investigate a possible LVR mitigation by quantifying how arbitrage losses reduce with shorter block times. We observe notable variations in the manner of decline of arbitrage losses across different trading pairs. For instance, when comparing $100 \mathrm{~ms}$ block times to Ethereum's current 12-second block times, the decrease in losses to arbitrageurs ranges between $20 \%$ to $70 \%$, depending on the specific trading pair.


## KEYWORDS

Automated Market Maker, Arbitrage profits, Loss-versus-rebalancing

## 1 INTRODUCTION

Automated market makers (AMMs) have emerged as a cornerstone of decentralized finance, holding billions in liquidity and facilitating trillions in total trading volume. Ever since their inception, the profitability of providing liquidity to AMMs has been a widely discussed research topic - both in theory and in practice. The central question remains: Do earnings from trading fees adequately compensate liquidity providers (LPs) on AMMs for the risks they are exposed to? The answer to this question is crucial, as the long-term sustainability of AMMs, and by extension, much of decentralized finance, relies heavily on LPs receiving sufficient compensation.

While earning trading fees, liquidity providers on AMMs face adverse selection costs. Although any form of market-making activity generally involves such costs, liquidity on AMMs is exposed to a distinct form of losses to arbitrageurs that is unique to this model. The prevalent type of AMM, the constant function market maker (CFMM), by design, incurs a loss with each price movement on external markets. The intuitive reason is that a CFAMM offers to trade at an outdated ("stale") price compared to continuous-time off-chain markets at the beginning of each block. Arbitrageurs capitalize on this price difference, earning profits at the expense of the AMM's LPs. ${ }^{1}$

In an influential contribution to measuring LP profitability, Milionis et al. [14] formalized these losses to arbitrageurs by comparing[^0]

AMM liquidity to a rebalancing portfolio that executes the same trades as an AMM position, but at the external market price. They coin the term loss-versus-rebalancing (or short LVR) for the difference between the value of the liquidity position and the rebalancing portfolio. The concept offers a new angle to measuring LP profitability by quantifying adverse selection costs that AMM liquidity faces beyond market risk, since the rebalancing portfolio hedges the position's market risk at any point in time.

Building upon this notion, a liquidity position can be deemed as unprofitable if its earnings from fees fall short of the losses incurred to arbitrageurs. Note that, throughout this paper, we use the expressions arbitrage losses, losses to arbitrageurs and arbitrage profits interchangeably to refer to the losses that LPs suffer to arbitrage trades due to outdated prices on the AMM, or equivalently, the profits that the arbitrageurs make on these trades. In the continuoustime setting without pool fees, this value aligns with LVR. We apply the concept to the real-world setting characterized by discrete trade times (whenever a new block is appended to the blockchain) and the presence of AMM trading fees.

In this paper, we study empirically, using historical data, the profitability of liquidity provision. In other words, we measure whether earnings from trading fees sufficiently compensate liquidity provided to AMMs for the incurred arbitrage losses. Our results also quantify the potential benefits of some recently-suggested AMM designs aiming to capture arbitrage profits for liquidity providers (e.g. [10], [12] and [5]).

We compare the historical earnings from trading fees to the amount of incurred arbitrage losses for the most-traded Uniswap v2 and v3 pools. This covers a considerable fraction of the total liquidity in AMMs, as Uniswap v3 is the market-leading and highestvolume AMM on Ethereum. Uniswap v2, the market leader prior to the inception of its successor, further maintains a substantial amount of liquidity (about $70 \%$ as much as Uniswap v3, at the time of writing). Earnings from fees are computed based on the historical trading activity within the liquidity pools. To simulate arbitrage losses, we assume that the pools are consistently arbitrated against external market prices. For price data, we use historical prices on Binance, the most liquid cryptocurrency exchanges.

Moreover, this paper also studies a proposed measure to reduce LVR: the reduction of block times. To do so, we quantify how arbitrage losses depend on the time interval between blocks.

Our analysis reveals several notable findings. First, we confirm what has previously been mostly known anecdotally: Fees do not sufficiently compensate for arbitrage losses in most of the largest Uniswap liquidity pools, i.e. historically, returns from fees have been smaller than losses to arbitrageur. This questions the high amount of liquidity (worth billions USD at the time of writing) currently being provided to these AMM pools. On the other hand,
we do find some profitable pools (according to the LVR-measure) among pools with less-trade tokens.

Another result that stands out is the fact that Uniswap v2 pools, which the more capital-efficient v3 pools have largely superseded, perform remarkably well when comparing fees to arbitrage losses. In particular, the most-traded Uniswap v2 pools are significantly more profitable than the corresponding Uniswap v3 pools for the same pair and trading fee.

Lastly, we observe varying behavior in the relationship between arbitrage losses and blockchain block times across trading pairs. While faster block times, as expected, reduce losses for all studied pairs, the extent and speed of the decline varies notably. We find that losses to arbitrageurs are reduced by between $20 \%$ and $70 \%$ with $100 \mathrm{~ms}$ block times compared to Ethereum's current 12 seconds, depending on the trading pair.

## 2 RELATED WORK

The prevalent type of AMM utilized in DeFi today, i.e. the constant product, or more broadly, constant function market maker, was initially discussed in 2016 [4], and later formalized in [3]. Specifically, the AMMs analyzed in this study, namely versions v2 [1] and v3 [2] of the Uniswap protocol, are based on these concepts.

The profitability of liquidity on AMMs has been discussed since early in their existence, focusing mostly on so-called "impermanent loss" or "divergence loss", which compares the development of the value of a liquidity position to holding the liquidity outside the AMM [15]. Empirically, the literature has studied the profitability of liquidity providers (LPs) on automated market makers across various AMMs, token pairs, and time frames. Heimbach et al. [9] investigate LP's behavior (and their profitability) on Uniswap $\mathrm{v} 2$, while following works, such as $[7,8,11]$, studied liquidity on Uniswap v3.

These investigations have in common that they primarily focus on comparing LP positions to (loss-versus-holding, "impermanent loss") as a key indicator of LP profitability. In contrast, this paper follows the approach formalized by Milionis et al. [14] to measure LP performance versus a "rebalancing portfolio" that hedges the price risk of the liquidity position. The paper also includes an empirical measurement of LVR for the Uniswap v2 WETH-USDC pool. This work offers a more comprehensive study, importantly including liquidity on Uniswap v3 - which has superseded v2 as the marketleading AMM on Ethereum. Markout profits of Uniswap v3 liquidity, which are closely related to LVR, have been explored in Twitter and blog posts, see e.g. [6], again for a limited set of pools. A small subset of the results presented in this paper were previously used in the empirical part of [5] which discusses an AMM design utilizing batch auction to prevent LVR.

In follow-up work, Milionis et al. extend their model to incorporate discrete block times and positive AMM fees [13]. In particular, their work provides theoretical predictions for the relationship between block times and losses to arbitrageurs, which we measure empirically in this work. We discuss in detail how the theoretical and empirical results compare in the results section.

## 3 COMPARING FEES AND ARBITRAGE LOSSES

### 3.1 Methodology

For each liquidity pool we study, we consider a hypothetical liquidity position existing from January 2022 to December 2023. We calculate the fee that such a position would have earned using historical trade data. We also simulate the arbitrage losses that the liquidity position would incur assuming the AMM pool is consistently arbitraged to Binance prices, the most liquid centralized exchange.

Uniswap v3 liquidity. In a simple constant-product liquidity pool (such as Uniswap v2 pools), all liquidity positions are available over the entire $[0, \infty]$ price range. Uniswap v3 pools, instead, employ the concept of "concentrated liquidity", that is, liquidity providers can choose a specific price range they want to provide liquidity to [2]. Within each range, liquidity positions act according to a regular constant-product AMM. When a swap occurs, it is executed only against liquidity provided around the price at which the swap occurred. Correspondingly, the swap fees are distributed pro rata among the liquidity available at that price.

For Uniswap v3 pools, we simulate a full-range liquidity position, i.e., a position that provides liquidity the entire price range $[0, \infty]$, as is the case for all Uniswap v2 positions. Note that, as long as the price stays within the price range of a concentrated liquidity position, it behaves similar to a full-range position. In particular, the concentrated position earns fees and incurs arbitrage losses in the same way as a full-range position, but requires a smaller amount of reserves to be deposited. This means that the returns from fees as well as the arbitrage losses relative to the liquidity value scale linearly with the concentration factor of a liquidity position, as long as the position stays in range ${ }^{2}$.

Hence, our results, especially the calculated ratios of fees and arbitrage losses, are also relevant for general liquidity positions in v3 pools.

Binance prices. We consider only Uniswap pools whose tokens are traded on Binance. Moreover, ETH, BTC, USDC, and USDT are traded directly against each other on Binance. For the remaining pairs, i.e. LDO-ETH, LINK-ETH, MATIC-ETH, and UNI-ETH, we derived the Binance prices by combining the prices of the two corresponding USDT pairs.

For all Binance pairs, we retrieve second-by-second price data. Then, for each Ethereum block, we consider the opening price in the second determined by the block's timestamp.

Finally, note that USDC was not traded on Binance between September 2022 and March 2023. ${ }^{3}$ We substitute the missing data by using the corresponding USDT pairs. We expect the effect of this substitution on the results to be negligible since this is precisely the case when both USDC and USDT prices are available.

Simulated losses to arbitrageurs. Using the price data from Binance, for each Uniswap pool, we simulate the amount of arbitrage[^1]losses a full-range liquidity position would incur as follows. The liquidity position is deposited into the pool at the beginning of the observation period. Subsequently, at the time of each block (using the timestamps of Ethereum blocks), we consider the external price on Binance. If the difference to the current AMM pool price is sufficient to create a profitable arbitrage opportunity between the pool and the external market (i.e., Binance), we simulate the AMM (and thereby the simulated position) being rebalanced by the optimal arbitrage trade. That is, arbitrageurs trade with the pool until the marginal price (taking fees into account), equals the Binance price. Note that since we consider that the pool charges a trading fee, the price difference needs to be larger than the fee for a profitable arbitrage opportunity to exist.

The difference between the price at which the arbitrage trade is executed (against the liquidity position) and the external price leads to a profit for the arbitrageurs and a loss to liquidity providers. For each arbitrage trade, we calculate the size of the loss relative to the value of the liquidity position, and apply the loss to the liquidity position in a compounding manner over time.

Historical fees. To compute historical returns from fees, we extract all swap transactions from Ethereum events. For each swap, we retrieve the amount swapped, the fees paid, and the amount of liquidity available at the swap's price (more precisely at the marginal price after the swap). Then, by comparing the size of the simulated position to the available liquidity, we are able to calculate the amount of fees that the simulated position receives. We put this in relation to the current position value to calculate the relative profit and compound the profit into the liquidity position ${ }^{4}$. Note that we assume the size of the simulated position to be small compared to the pool size, in the sense that its presence does not affect the behavior of traders and other LPs.

This method of fee computation makes an implicit assumption, namely that during a swap, the price stays within a price range with constant liquidity. For Uniswap v3 pools, this can lead to small inaccuracies when swaps cause large price movements, and available liquidity varies across these price ranges. Besides these potential inaccuracies being non-systematic, such situations are expected to occur only rarely as we consider highly liquid pools on Uniswap where the price impact of single swaps is generally small ${ }^{5}$.

### 3.2 Results

Figure 1a shows the difference between fees and arbitrage losses for a simulated full-range liquidity position for the most liquid Uniswap v3 ETH and BTC pools. Downwards trending lines indicate fees being consistently lower than arbitrage losses over the two-year observation period. We observe this to be the case for most ETH and BTC pools, including the highest-traded Uniswap pool during most of the observation periods, the WETH-USDC 5bp pool.[^2]

![](https://cdn.mathpix.com/cropped/2024_04_26_58017573dc0e2780ca6bg-3.jpg?height=493&width=832&top_left_y=282&top_left_x=1102)

(a) The difference between historical fees and simulated losses to arbitrageurs relative to the liquidity value for a full-range liquidity position. An upwards trend indicates fees being larger than losses.

![](https://cdn.mathpix.com/cropped/2024_04_26_58017573dc0e2780ca6bg-3.jpg?height=507&width=838&top_left_y=901&top_left_x=1099)

(b) Historical fees relative to simulated losses to arbitrages overtime (30-day moving average).

Figure 1: ETH and BTC pairs on Uniswap v3.

This fact can also be observed in Figure 1b, which shows the 30-day moving average of fees earned as a percentage of arbitrage losses for a subset of the pools. For instance, in the WETH-USDC $5 \mathrm{bp}$ pool, the historical returns from fees hover around $80 \%$ of arbitrage losses.

The WETH-USDT 5bp pool (together with the WBTC-USDC $30 \mathrm{bp}$ pool) is an exception among the large pools in this regard, roughly breaking even during most times. It also exhibits a brief period in March 2023 when fees reached twice as high as losses due to high trading volumes during the time of a UDSC depeg in March 2023.

Figure 2 shows the corresponding results for a number of less traded tokens. For these pairs, fees tend to compensate for arbitrage losses, sometimes even being $50 \%$ higher on average, e.g. for the MATIC-ETH and LINK-ETH pools.

Finally, Figure 3 shows a significantly different picture for Uniswap v2 pools. Here, fees consistently compensate LPs for arbitrage losses, especially in the second year of the observation period. Notably, fees are consistently three times larger than losses during this time, as Figure $3 b$ shows.

![](https://cdn.mathpix.com/cropped/2024_04_26_58017573dc0e2780ca6bg-4.jpg?height=502&width=853&top_left_y=280&top_left_x=170)

(a) The difference between historical fees and simulated losses to arbitrageurs relative to the liquidity value for a full-range liquidity position. An upwards trend indicates fees being larger than losses.

![](https://cdn.mathpix.com/cropped/2024_04_26_58017573dc0e2780ca6bg-4.jpg?height=504&width=846&top_left_y=911&top_left_x=173)

(b) Historical fees relative to simulated losses to arbitrages overtime (30-day moving average).

Figure 2: Less liquid trading pairs on Uniswap v3

### 3.3 Discussion

It is notable that earnings from fees are smaller than losses to arbitrageurs in the majority of the largest Uniswap pools, which hold hundreds of million USD. It raises the question of why LPs nevertheless allocate their capital to these pools. Since LPs face or must pay to hedge market risk on top of LVR, it could be expected for LPs to seek being compensated substantially higher than their losses to arbitrageurs.

Moreover, the results show how impactful mechanisms to reduce LVR in AMMs could be on the profitability of AMM liquidity.

Finally, the fact that fees relative to the amount of (in-range) liquidity are significantly higher for v2 pools compared to v3 pools, even when comparing pools with equal fee tiers $(0.3 \%)$ is arguably surprising. It would be expected that arbitrage volume (from arbitrageurs rebalancing to external prices) is proportional to the amount of in-range liquidity: Larger pools should attract proportionally larger arbitrage trades. Moreover, larger pools, which generally are the v3 pools, could potentially see higher relative arbitrage volume: When taking fixed costs per swap, such as blockchain transaction fees, into account, arbitrage could be profitable more often for them.

![](https://cdn.mathpix.com/cropped/2024_04_26_58017573dc0e2780ca6bg-4.jpg?height=496&width=832&top_left_y=286&top_left_x=1102)

(a) The difference between historical fees and simulated losses to arbitrageurs relative to the liquidity value for a full-range liquidity position. An upwards trend indicates fees being larger than losses.

![](https://cdn.mathpix.com/cropped/2024_04_26_58017573dc0e2780ca6bg-4.jpg?height=504&width=838&top_left_y=924&top_left_x=1099)

(b) Historical fees relative to simulated losses to arbitrages overtime (30-day moving average).

Figure 3: Trading pairs on Uniswap v2

The same should be true for retail trading volume, if these trades are routed optimally. Again, larger pools should see proportionally more volume (assuming trading fees are equal). So the ratio of fees to in-range liquidity, and thereby the returns from fees, would be expected to similar (when comparing v2 and v3 pools with the same fee.)

One possible explanation for the difference in earnings from fees could lie in an important distinction between Uniswap v3 and v2: Uniswap v3 allows for competition between LPs. Its design enables active LPs to move their liquidity around when prices change in order to optimize their earning from fees, thereby possibly diminishing the share of fees going to passive LPs who do not move their liquidity position. The liquidity position considered in this work is passive meaning its earnings from fees could potentially suffer from this competition.

## 4 LOSSES TO ARBITRAGEURS AND BLOCK TIMES

The intuition behind shorter block times reducing losses to arbitrageurs is that smaller price differences between blocks lead to

![](https://cdn.mathpix.com/cropped/2024_04_26_58017573dc0e2780ca6bg-5.jpg?height=1103&width=678&top_left_y=300&top_left_x=257)

Figure 4: ETH and BTC pairs with a trading fee of $0.05 \%$ : Simulated losses to arbitrageurs relative to the liquidity value for different block intervals (100ms - 16s). The current Ethereum block time is 12s. The lower plots show the same data with logarithmic axes.

smaller arbitrage opportunities. We quantify this effect for block times between $100 \mathrm{~ms}$ and $16 \mathrm{~s}$ (and up to $5 \mathrm{~min}$ in the appendix).

### 4.1 Methodology

To simulate arbitrage losses under varying block times, we obtain six months of Binance order book data (June 2023 to November $2023)^{6}$. More specifically, we download all updates to the best bid and ask prices, which allows us to deduce the current bid and ask prices at arbitrary regular time intervals. Note that we do not consider the amount of liquidity in the order book at these prices. Instead, we implicitly assume arbitrageurs are able to buy and sell sufficient amounts at the best bid and ask prices. The rationale is that, with Binance being the most-liquid exchange, its prices are in sync with the overall market, which offers sufficiently deep liquidity.[^3]![](https://cdn.mathpix.com/cropped/2024_04_26_58017573dc0e2780ca6bg-5.jpg?height=1072&width=680&top_left_y=297&top_left_x=1183)

Figure 5: Less-liquid trading pairs with of fee of $0.03 \%$ : Simulated losses to arbitrageurs relative to the liquidity value for different block intervals (100ms - 16s). The current Ethereum block time is $12 \mathrm{~s}$. The lower plots show the same data with logarithmic axes.

We then simulate a hypothetical AMM position in a constantproduct pool for different block times between $100 \mathrm{~ms}$ and $15 \mathrm{~s} \mathrm{simi-}$ larly as described in the precious section: For each block time, we assume that arbitrageurs rebalance the AMM pool at each every block if it is profitable for them. This is the case if and only if the current price on the AMM taking fees into account is below the current best bid price or above the current best ask price.

We assume the pools to have the following trading fees, which, at the time of writing, represent the most-common fee for these kinds of pairs on the most-used AMMs: $0.05 \%$ for ETH and BTC pairs, and $0.3 \%$ for less-liquid "altcoin" pairs.

Note that the results do not depend on the size of the initial liquidity position. Larger positions incur proportionally larger losses to arbitrageurs leading to the same loss relative to the position's value.

### 4.2 Results

Our results (see Figures 4 and 5) show varying relationships between arbitrage losses and block times for different trading pairs. Besides the overall magnitude of the losses, the manner of their
decline with shorter block times also varies across pairs. The reduction in losses to arbitrageurs when block time is $100 \mathrm{~ms}$ block (compared to Ethereum's 12s), ranges between $20 \%$ and $70 \%$ depending on the pair. For most token pairs, an acceleration in the reduction trends can be observed for short block times.

The log-log plots in the lower figures show the general dependence on block times. A slope of $c$ in these plots would indicate that arbitrage losses are proportional to the block interval to the power of $c$. The slope is about $1 / 3$ for most pairs and block times above $1 \mathrm{~s}$, while it is significantly flatter for blocks times shorter than 1 .

Finally, we see in Figures 4 and 5 that arbitrage losses begin flattening out for longer block times. This effect can be seen even more pronounced in Figure 6 in the appendix, which reports results for up to $5 \mathrm{~min}$ block times. While the results are somewhat noisy, they generally indicate arbitrage profits leveling off at about twice the current rate at 12 s block times for block intervals larger than 2 min.

### 4.3 Discussion

The relationship between arbitrage profits and block times has been studied theoretically in [13]. For short block times, their theoretical model predicts that arbitrage profits are proportional to the square root of the length of the average block intervals. While our empirical findings come close to this model for most pairs and block times larger than 1s, we observe a different regime for block times shorter than 1s. More precisely, arbitrage profits appear to decline more slowly than the theoretical model would suggest.

The deviating behavior could stem from the differences between the theoretical model and our simulation setup. Firstly, their model assumes blocks arrive according to a stochastic process while we operate with fixed intervals between blocks. Secondly, the asset prices are assumed to follow a geometric Brownian motion whereas base our analysis on historical price data.

On a related note, we remark that when examining arbitrage losses for varying pool fees (simulated in the same way as for block times), the simulation results match the expected inversely proportional relationship predicted by [13] as Figure 7 in the appendix shows.

## 5 CONCLUSION

Our study, to the best of our knowledge, provides the most comprehensive measurement of LP losses to arbitrageurs (LVR), spanning multiple token pairs, AMM design, and also block time. We derive several significant and somewhat surprising findings. Moreover, it motivates further study in this direction of research.

First, we show that large amounts of liquidity (worth billions USD) are contributed to AMMs as liquidity despite LPs lose more to arbitrageurs than they make in fees. This striking result begs the question of why LPs contribute liquidity at all. Second, the difference in profitability between Uniswap v2 and v3 pools is striking and should be studied further, as it could reveal important insights on how to design AMMs that are profitable (for LPs) and hence sustainable. Finally, quantifying how LP losses to arbitrageurs change with the intervals between trading opportunities can help make informed decisions when choosing block times when designing blockchains.

## ACKNOWLEDGMENTS

The authors wish to thank Jason Milionis and Ciamac Moallemi for helpful discussions and comments.

## REFERENCES

[1] Hayden Adams, Noah Zinsmeister, and Dan Robinson. 2020. Uniswap v2 Core. Technical Report.

[2] Hayden Adams, Noah Zinsmeister, Moody Salem moody, uniswapor River Keefer, and Dan Robinson. 2021. Uniswap v3 Core. Technical Report.

[3] Guillermo Angeris, Hsien-Tang Kao, Rei Chiang, Charlie Noyes, and Tarun Chitra. 2021. An Analysis of Uniswap markets. Cryptoeconomic Systems 0, 1 (apr 5 2021). https://cryptoeconomicsystems.pubpub.org/pub/angeris-uniswap-analysis.

[4] Vitalik Buterin. 2016. Let's run on-chain decentralized exchanges the way we run prediction markets. https://www.reddit.com/r/ethereum/comments/55m04x/ lets_run_onchain_decentralized_exchanges_the_way/

[5] Andrea Canidio and Robin Fritsch. 2023. Arbitrageurs' profits, LVR, and sandwich attacks: batch trading as an AMM design response. arXiv:2307.02074 [cs.DC]

[6] Crocswap. 2022. Usage of Markout to Calculate LP Profitability in Uniswap V3. https://crocswap.medium.com/usage-of-markout-to-calculate-lpprofitability-in-uniswap-v3-e32773b1a88e

[7] Robin Fritsch. 2021. Concentrated Liquidity in Automated Market Makers. In Proceedings of the 2021 ACM CCS Workshop on Decentralized Finance and Security (Virtual Event, Republic of Korea) (DeFi '21). Association for Computing Machinery, New York, NY, USA, 15-20. https://doi.org/10.1145/3464967.3488590

[8] Lioba Heimbach, Eric Schertenleib, and Roger Wattenhofer. 2023. Risks and Returns of Uniswap V3 Liquidity Providers. In Proceedings of the 4th ACM Conference on Advances in Financial Technologies (Cambridge, MA, USA) (AFT '22). Association for Computing Machinery, New York, NY, USA, 89-101. https: //doi.org/10.1145/3558535.3559772

[9] Lioba Heimbach, Ye Wang, and Roger Wattenhofer. 2021. Behavior of Liquidity Providers in Decentralized Exchanges. In 2021 Crypto Valley Conference on Blockchain Technology (CVCBT), Rotkreuz, Switzerland.

[10] Josojo. 2022. MEV capturing AMM (McAMM). https://ethresear.ch/t/mevcapturing-amm-mcamm/13336 Online forum post.

[11] Stefan Loesch, Nate Hindman, Mark B Richardson, and Nicholas Welch. 2021. Impermanent Loss in Uniswap v3. arXiv:2111.09192 [q-fin.TR]

[12] Conor McMenamin, Vanesa Daza, and Bruno Mazorra. 2022. Diamonds are forever, loss-versus-rebalancing is not. Cryptology ePrint Archive (2022)

[13] Jason Milionis, Ciamac C Moallemi, and Tim Roughgarden. 2023. Automated Market Making and Arbitrage Profits in the Presence of Fees. arXiv preprint arXiv:2305.14604 (2023).

[14] Jason Milionis, Ciamac C Moallemi, Tim Roughgarden, and Anthony Lee Zhang. 2022. Automated market making and loss-versus-rebalancing. arXiv preprint arXiv:2208.06046 (2022)

[15] Pintail. 2019. Uniswap: A good deal for liquidity providers? https://pintail. medium.com/uniswap-a-good-deal-for-liquidity-providers-104c0b $6816 \mathrm{f} 2$

Measuring Arbitrage Losses and Profitability of AMM Liquidity

## 6 APPENDIX

![](https://cdn.mathpix.com/cropped/2024_04_26_58017573dc0e2780ca6bg-7.jpg?height=748&width=678&top_left_y=678&top_left_x=257)

(a) ETH and BTC pairs, trading fee: $\mathbf{0 . 0 5 \%}$

![](https://cdn.mathpix.com/cropped/2024_04_26_58017573dc0e2780ca6bg-7.jpg?height=748&width=678&top_left_y=1491&top_left_x=260)

(b) Less liquid pairs, trading fee: $0.3 \%$

Figure 6: Simulated losses to arbitrageurs relative to the liquidity value for block intervals up to $300 \mathrm{~s}(5 \mathrm{~min}$ ). The current Ethereum block time is $12 \mathrm{~s}$.

![](https://cdn.mathpix.com/cropped/2024_04_26_58017573dc0e2780ca6bg-7.jpg?height=718&width=672&top_left_y=297&top_left_x=1147)

Figure 7: Simulated losses to arbitrageurs relative to the liquidity value for different pool trading fees.


[^0]:    ${ }^{1}$ In practice, competition between arbitrageurs leads to most of these profits being handed on to validators for the privilege of being the first transaction in a block to interact with the pool.

[^1]:    ${ }^{2} \mathrm{~A}$ liquidity position that requires $k$-times less capital will experience $k$-times larges fee returns and arbitrage losses relative to its value.

    ${ }^{3}$ During this period, Binance converted USDC and other stablecoins to its own stablecoin, BUSD (see https://www.binance.com/en/support/ announcement/binance-to-auto-convert-usdc-usdp-tusd-to-busd-binance-usde62f703604a94538a1f1bc803b2d579f).

[^2]:    ${ }^{4}$ In practice, fees automatically compound in Uniswap v2 pools while they do not in v3 pools. There, liquidity providers need to repeatedly add earned fees to their position to achieve compounding.

    ${ }^{5}$ To illustrate this, we calculate that the difference between assuming liquidity to be constant over a full block instead of over each swap is $0.01 \%$ over 6 months for the WETH-USDC $0.05 \%$ pool. We expect the inaccuracies from assuming the liquidity to be constant during each swap to be even smaller.

[^3]:    ${ }^{6}$ Note that Binance offers access to order book data only for perpetual futures, and not for spot trading pairs. Hence, in this section, we consider the perpetual future prices for each of the pairs. See here for a description of Binance's perpetual futures: https://www.binance.com/en/feed/post/168298

