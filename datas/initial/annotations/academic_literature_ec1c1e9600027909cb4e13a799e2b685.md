# A theoretical framework for dynamical fee choice in AMMs 

Abe Alexander* ${ }^{* 1}$ and Lars Fritz ${ }^{\dagger 2}$<br>${ }^{2}$ Institute for Theoretical Physics and Center for Extreme Matter<br>and Emergent Phenomena, Utrecht University, Princetonplein 5,<br>3584 CC Utrecht, The Netherlands

April 8, 2024


#### Abstract

In the ever evolving landscape of decentralized finance automated market makers (AMMs) play a key role: they provide a market place for trading assets in a decentralized manner. For so-called bluechip pairs, arbitrage activity provides a major part of the revenue generation of AMMs but also a major source of loss due to the so-called 'informed orderflow'. Finding ways to minimize those losses while still keeping uninformed trading activity alive is a major problem in the field. In this paper we will investigate the mechanics of said arbitrage and try to understand how AMMs can maximize the revenue creation or in other words minimize the losses. To that end, we model the dynamics of arbitrage activity for a concrete implementation of a pool and study its sensitivity to the choice of fee aiming to maximize the value retention. We manage to map the ensuing dynamics to that of a random walk with a specific reward scheme that provides a convenient starting point for further studies.


## 1 Introduction

Decentralized Finance (DeFi) has emerged as a groundbreaking ecosystem within the cryptocurrency space, offering a wide array of financial services without intermediaries. One of the key strategies employed within DeFi is arbitrage, a practice where traders capitalize on price discrepancies of assets across different platforms or exchanges.

Arbitrage in DeFi operates similarly to traditional finance but with distinct advantages stemming from the decentralized nature of blockchain technology. Participants can exploit price differentials between decentralized exchanges[^0]

(DEXs), lending protocols, liquidity pools, and other DeFi platforms. These opportunities arise due to variations in supply and demand dynamics, transaction delays, or inefficiencies in pricing algorithms.

One of the primary drivers of arbitrage in DeFi is the concept of composability, wherein various protocols can be seamlessly integrated to create complex financial strategies. For instance, a trader might exploit price disparities between a decentralized exchange and a lending protocol by borrowing assets at a lower rate on one platform and immediately selling them at a higher price on another.

Arbitrageurs play a crucial role in maintaining market efficiency within the DeFi ecosystem. By exploiting pricing inefficiencies, they help align prices across different platforms and contribute to overall market stability. However, arbitrage opportunities are often short-lived as they attract other traders, leading to rapid price convergence.

Despite its potential for profit, arbitrage in DeFi carries certain risks, including impermanent loss, transaction fees, and smart contract vulnerabilities. Moreover, regulatory uncertainties and protocol risks add further complexity to $\mathrm{DeFi}$ arbitrage strategies.

In conclusion, arbitrage in DeFi represents a dynamic and lucrative aspect of decentralized finance, allowing traders to capitalize on price differentials across various protocols. While offering significant profit potential, it requires a deep understanding of market dynamics, smart contract mechanics, and risk management principles. As DeFi continues to evolve, arbitrage will remain a fundamental strategy shaping the landscape of decentralized finance.

In the context of automated market makers (AMMs), arbitrage is a major factor in the revenue generation but also loss due to the so-called 'informed orderflow'. Looking over a variety of AMMs reveals that the main source of fee generation are so-called bluechip pairs that exists all over DeFi but also on centralized exchanges (CEXs). It is sometimes assumed that more than $80 \%$ of trading activity in those pairs is in arbitrage deals.

For the purpose of this paper, we thus model the trading activity of an AMM based on the assumption that trading is exclusively via arbritrage. To that end we simulate a source of infinite liquidity which provides a quote at every point in time. This quote follows Brownian motion with a drift, while we make not further assumptions. In parallel, we simulate an AMM. We chose for a constant function type of pool but the results can easily be extended to more complex types of AMMs, such as a concentrated liquidity implementation like the Uniswap v3 pools.

In Sec. 2, we introduce the mathematical framework of an AMM as well as the principles of arbitrage carried out by an agent acting optimally. While there is a general gain from arbitrage, it turns out that through the setting of the fee, the AMM participates in those gains. It turns out, that for a given price mismatch, there is an optimal fee choice which allows the AMM to retain $2 / 3$ of the gains, while the arbitrageur has to content with $1 / 3$. Furthermore, we find that the threshold gain in arbitrage processes (threshold defined as the minimal price difference required for successful arbitrage) is proportional to the square
of the fees and inversely proportional to the price impact (non-linear price).

We use those insights in Sec. 3 to argue that a good effective model to describe things like effective time between arbitrage events and expected rewards is given by a random walk with a specific reward structure. The main finding in this section is that under steady conditions, the actual choice of a fee is relatively unimportant and the gains of the AMM are invariant under this choice. This can be traced back to an interplay between the specific arbitrage reward structure derived in Sec. 2 and fundamental properties of one-dimensional random walks.

In Sec. 4 we go to a more microscopic simulation where we do not impose the points of arbitrage but let the arbitrageur find its points in an optimal way. Our main finding is that we confirm the findings of the random walk discussion.

We end with a conclusion and with an outlook, see Sec. 5. Related literature:

AMMs can be traced back to Hanson(2007) and Othman et al.(2013) with early implementations discussed in [Lehar and Parlour(2021)], [Capponi and Jia(2021)], and Hasbrouck et al.(2022)]. Details of implementation are described in [Adams et al.(2020) and Adams et al.(2021)] as well as in a very recent textbook Ottina et al.(2023)].

We study ways to optimize fees based on an arbitrage-only assumption. Uniswap v3 (Adams et al.(2021)]) addresses this problem by letting liquidity providers choose between different static fee tiers. Other automated market makers have implemented dynamic fees on individual pools, including Trader Joe v2.1 ( MountainFarmer et al.(2022) $)$, Curve v2 ( Egorov and GmbH)(2021) $)$ and Mooniswap ([Bukov and Melnik(2020)]), Algebra ([Volosnikov et al.(2022)]), as well as Nezlobin(2023)].

## 2 The setup and statement of the problem

### 2.1 The setup

We consider the interplay between an AMM and a CEX as infinite liquidity source of arbitrage activity.

For simplicity, we assume that the AMM is described as a Uniswap v2 type constant function pool

$$
x_{A} * x_{B}=L^{2}
$$

where $x_{A}$ is the number of tokens of type $A$ and $x_{B}$ the number of tokens of type $B$. While we choose for a v2-style pool for simplicity, the analysis applies equally to a v3 style pool.

Returns from swaps are in general subject to price impact. There are, in principle, three prices worth discussing: the spot price, $p_{s}$, the effective swap price, $p_{\text {eff }}$, and the spot price after a swap, $p_{s}^{\prime}$. The price before a swap, the spot price, is simply defined by

$$
p_{s}=\frac{x_{B}}{x_{A}}
$$

We now consider a swap in which $\Delta A$ tokens are swapped for $\Delta B$ tokens. At this point, the effective price matters according to

$$
\Delta B=p_{\mathrm{eff}} \Delta A=\frac{p_{s}}{1+p_{i A} \Delta A} \Delta A
$$

where $p_{i A}$ accounts for the non-linearity of the pricing function, called price impact. In this expression we kept the price impact generic for it to apply to different types of AMMs. In the case of a constant function AMM it is simply given by $p_{i A}=1 / x_{A}$. The swap ends with a new spot price

$$
p_{s}^{\prime}=\frac{x_{B}-\Delta B}{x_{A}+\Delta A}
$$

There is a reverse swap with roles reversed and a corresponding inverse price impact $p_{i B}$

$$
\Delta A=\frac{p_{s}^{-1}}{1+p_{i B} \Delta B} \Delta B
$$

### 2.2 An arbitrage cycle

Now we look at one arbitrage cycle. An arbitrage agent observes that token B trades cheaper in the AMM than on the CEX. In concrete terms, this means that $p_{s} / p_{\mathrm{CEX}}>1$. The reason for arbitrage is obviously free profit. How can the arbitrage agent optimize the profit? To answer this, we need an equation that accounts for all gains and losses in the process. It is important to reiterate that we assume that the CEX is of infinite liquidity.

In the actual process, the arbitrageur takes a flashloan of size $\triangle F L$ (here we assume that it is taken in the denomination token A). For that, he will pay the fee $\Delta F L f_{\mathrm{fl}}$ with $f_{\mathrm{fl}}$. On the other Hand, the AMM charges a fee $f$ for swaps, meaning the actual $\delta A$ entering the pool will be

$$
\Delta A=\Delta F L(1-f)
$$

After the swap to $\Delta B$ is completed, $\Delta B$ is sold at the CEX for

$$
\Delta=\frac{1}{p_{C E X}} \Delta B
$$

at zero price impact. Overall, this cycle results in the profit

$$
\begin{aligned}
P_{A} & =\frac{1}{p_{C E X}} \Delta B-\Delta F L\left(1+f_{f l}\right)-T X N \\
& =\frac{p_{s}}{p_{C E X}} \frac{1}{1+p_{i A} \Delta F L(1-f)} \Delta F L(1-f)-\Delta F L\left(1+f_{f l}\right)-T X N(8)
\end{aligned}
$$

to the arbitrageur, where $T X N$ accounts for the cost of transactions. In the following, we use the parameter $\alpha=p_{s} / p_{C E X}$.

Condition for arbitrage: We can start by asking when an arbitrage can be performed successfully. Clearly, the question is equivalent to asking when do we have $P_{A}>0$ as a function of $f$. To answer this, we first rewrite

$$
\left.P_{A}=\Delta F L\left(\alpha \frac{1-f}{1+p_{i A} \Delta F L(1-f)}-\left(1+f_{f l}\right)-\frac{T X N}{\Delta F L}\right)\right)
$$

Arbitrage with $\Delta A>0$ can only happen for $\alpha>1$ (for $\alpha<1$ one can have the opposite arbitrage with $\Delta B$ in). We are assuming for now that transaction costs are negligible $(T X N=0)$, meaning we have a condition

$$
\alpha \frac{1-f}{1+p_{i A} \Delta F L(1-f)}-\left(1+f_{f l}\right)>0
$$

We find that there is a threshold condition on $\alpha$ for a set AMM fee $f$ which needs to be overcome defined by

$$
\alpha>\frac{1+f_{f l}}{1-f}
$$

In the remainder of this paper we will discuss $f_{\mathrm{fl}}=0$ which is realistic on many platforms.

There is an optimal $\Delta F L^{o p t}$ from the point of view of the arbitrageur which allows to maximize the gain $P^{A}$. This can be determined from

$$
\frac{d P^{A}}{d \Delta F L}=0
$$

The solution is given by

$$
\Delta F L^{o p t}=\frac{1}{p_{i A}(1-f)}(\sqrt{\alpha(1-f)}-1)
$$

which is guaranteed to be positive once we fulfil Eq. (11). Note that this is equivalent to asking which $\triangle F L$ aligns the new spot price after the swap, $p_{s}^{\prime}$, with the price of the CEX $p_{C E X}$. The last thing to check is what is the optimal gain. There we find

$$
P_{A}^{o p t}=\frac{(\sqrt{\alpha(1-f)}-1)^{2}}{p_{i A}(1-f)}
$$

which is positive for situations that fulfil Eq. (11). There is another important quantity which is the revenue of the AMM. This is given by

$$
R^{o p t}=\Delta F L^{o p t} f
$$

which assumes the form

$$
R^{o p t}=\frac{\sqrt{\alpha(1-f)}-1}{p_{i A}(1-f)}
$$

Limiting case of small fee $f$ : In general, it is a given that the fee $f \ll 1$ so while this is a limiting case, it is the most relevant case of them all. Furthermore, we will parametrize alpha $=1+\delta \alpha$ where $\delta \alpha$ is the relative price difference $\left(p_{s}-p_{C E X}\right) / p_{C E X}$ and generally $\delta \alpha \ll 1$. In general, this means that we can rephrase Eq. 111) to leading order as

$$
\delta \alpha>f
$$

which makes intuitive sense. This means that in general, for an arbitrage activity to happen we expect $\delta \alpha \propto f$. we can use this to approximate the profit of an arbitrageur as well as the revenue of the DEX as

$$
\begin{aligned}
P_{A}^{\mathrm{opt}} & =\frac{(\delta \alpha-f)^{2}}{4 p_{i A}} \propto \frac{f^{2}}{p_{i A}} \\
R^{o p t} & =\frac{f(\delta \alpha-f)}{2 p_{i A}} \propto \frac{f^{2}}{p_{i A}}
\end{aligned}
$$

There is another interesting question that can be asked which is whether for a given $\delta \alpha$, there is an optimal choice of fee, $f^{\text {opt }}$, that allows maximum value retention. It turns out that the best choice in that case is $f^{o p t}=\delta \alpha / 2$. For that choice, we find that the AMM retains $2 / 3$ of the arbitrage gain whereas the arbitrageur has to content with $1 / 3$.

## In summary:

1. The threshold for an arbitrage action behaves like $\delta \alpha \propto f$ and inversely proportional to the price impact.
2. The potential gain for the arbitrage agent behaves like $P \propto f^{2}$
3. The revenue of the DEX when arbitrage happens scales like $R \propto f^{2}$
4. The maximum part of the arbitrage gains that an AMM can retain is $2 / 3$ of it.

From this consideration it seems like the best thing for a DEX to do is to just raise the fee $f$ to optimize revenue, but it is not that simple. The fee $f$ determines how often the arbitrage threshold is reached which turns out to be another important quantity. The remainder of the paper is devoted to studying the interplay between these competing effects.

## 3 Effective model: A random walk with rewards

It turns out that the results of the preceding section motivate a very simple but powerful modeling of the the arbitrage activity. The effective model is a version of the well known random walk. This model has countless applications and originated in physics as a microscopic description of Brownian motion and
(a) Difference in rewarding schemes

I

![](https://cdn.mathpix.com/cropped/2024_04_26_8b4d692a99c3f373d62dg-07.jpg?height=190&width=401&top_left_y=526&top_left_x=515)

II

![](https://cdn.mathpix.com/cropped/2024_04_26_8b4d692a99c3f373d62dg-07.jpg?height=209&width=415&top_left_y=730&top_left_x=519)

## (b) Average equivalence of gains

Average gain (2 steps)

![](https://cdn.mathpix.com/cropped/2024_04_26_8b4d692a99c3f373d62dg-07.jpg?height=387&width=629&top_left_y=522&top_left_x=973)

Figure 1: (a) We distinguish two rewarding schemes. (I) rewards every step irrespective of the direction with +1 whereas (II) rewards being two levels up or down from the last point of arbitrage with +4 rewards. (b) One can easily show that both schemes return the same average gain for sideways motion.

diffusion. However, it also found applications in the field of finance. It is often used to model the Brownian motion of stock prices with a respective volatility and drift.

In this discussion, we will put a twist on it which allows to understand a heuristic observations from fee dynamics of AMMs: In calm times, the actual fee setting matters very little to the revenue generation of AMMs.

The rules of a random walk are simple. We consider a walker than can go up and down in steps of unit one (it cannot stand still). It does so with probability $\left[p_{\text {down }}, p_{\text {up }}\right]$ obeying $p_{\text {down }}+p_{\text {up }}=1$ meaning it allows for modelling a symmetric random walk as well as versions with drifts.

We consider a situation that applies in times of low volatility and no preferential drift, so-called 'sideways motion'. The idea is to connect the insights of the previous section with a random walk that can easily be analyzed and simulated. The key insight is this: a step in the random walk corresponds to the price at the CEX either lowering or increasing relative to the AMM. Now there are two situations: a step and the corresponding price difference is big enough to trigger an arbitrage activity. Alternatively, it is not. As we found in Sec. 2 we found that the reason can be different fee settings. More concretely, in Eq. (17) we showed that this arbitrage threshold grows linearly with the fee $f$. It as also shown that while the threshold grows linearly, the arbitrage gains and also the AMM revenue grows quadratically with said fee or threshold, see Eq. (18).

This suggests introducing two different fee schemes, leading to two different rewarding schemes. Subsequently, we called them strategy I and strategy II and Fig. 3(a) makes an attempt at a graphical representation of the key properties.

![](https://cdn.mathpix.com/cropped/2024_04_26_8b4d692a99c3f373d62dg-08.jpg?height=517&width=965&top_left_y=419&top_left_x=577)

Figure 2: Random walk with two different strategies giving identical yield
I. $f_{I}$ is chosen such that every single step in price is above the threshold, meaning there is an arbitrage activity. We distribute the corresponding reward +1 .

II. $f_{I I}=2 f_{I}$ meaning the arbitrage threshold is doubled compared to the previous case. In practice, this implies the last point of arbitrage needs to be two steps higher or lower than the current one to trigger an arbitrage activity. Regarding rewards, this implies that rewards are triggered less frequent, but according to Eq. (18) the corresponding reward is +4

The question we are now going to answer is this: which strategy is more profitable? Intuitively, the way to the answer is straightforward: If the rewards in strategy (II) are on average triggered faster than every four steps, it wins. If it takes longer, it looses, and if it takes four steps on average, it is identical for practical purposes.

We consider the symmetric version $\left(p_{\text {up }}=p_{\text {down }}=1 / 2\right)$ and ran this for 10000 steps and compared the cumulative return. As expected, the results are identical within errorbars, see Fig. 2

This can be understood in relative simple terms, see the discussion in Fig. 3 (b): the average gain over two steps is identical in both schemes.

This discussion hinges on discrete step sizes and reward schemes that are commensurate with the steps. However, the principle at play is more general and can be understood from the random walk again. The mean displacement from the starting point in a random walk is known to scale like

$$
\sigma(t) \propto \sqrt{t}
$$

with time (or number of steps, equivalently). To stick with our example, this means that if we compare to different fees, $f_{I}$ and $f_{I I}=2 f_{I}$ that define an
arbitrage threshold $\sigma_{I I}=2 \sigma_{I}$. This implies that the times to reach it are related according to $t_{I I}=4 t_{I}$. On the other hand, according to the discussion in Eq. (18) the fee setting implies that we have rewards $R_{I I}=4 R_{I}$. So indeed, time-averaged rewards are identical, as we expected and showed. The advantage of this argument is that it does not require a commensurate rewarding scheme.

## Summary:

In a situation in which the price moves sideways, the exact setting for fees does not matter (but it can be optimized, as we will show in a follow up study). This is a conspiracy of factors related to the properties of the random walk and the properties of an arbitrage swap which leads to perfect cancellation in the important limit. This statement is borne out by empirical observation.

## 4 Comparison against a full numerical simulation

We simulate an AMM with a pool that is of the Uniswap v2 type and has a relatively high liquidity. The pool is described as a constant product pool of the type

$$
x_{A} x_{B}=L^{2}
$$

and has a starting price $p_{s}=x_{B} / x_{A}$ which is identical to the CEX price $p_{C} E X$ at this moment in time. Furthermore, there is a fee for swaps that we call $f$. In parallel, we model the price action of the same pair on a CEX. For the purpose of our simulation, the CEX price $p_{C E X}$ will follow Brownian motion. For reference we assume that the starting price of the simulation is $p_{s}=p_{C E X}=1$ without loss of generality. The sequence of the simulation is like this: In the following time step, first $p_{C E X}$ will evolve according to a simulated Brownian motion with a specific volatility. Now the code checks whether the misalignment of the prices is sufficient to fulfill

$$
\alpha>\frac{1}{1-f}
$$

(or the reverse for the other swapping direction), see discussion around Eq. (11). Now it performs the optimal swap and aligns the price of the AMM with $p_{C} E X$. Afterwards, the steps repeat. Throughout, we assume the CEX has infinite liquidity and therefore any buys and sells have no price impact. This is the whole setup of the numerical experiment and we can now run it with a variety of parameter settings. What we are tracking are the fees that are generated by the DEX as a function of time and we want to explicitly study the connection between the fee setting and the volatility. There is the understanding that larger volatility requires larger fees in the community. We will show that while this is
![](https://cdn.mathpix.com/cropped/2024_04_26_8b4d692a99c3f373d62dg-10.jpg?height=290&width=1240&top_left_y=451&top_left_x=453)

Figure 3: The simulation was run for 100 steps with a volatility of 0.01 per step, an initial price of $p_{s}=p_{C E X}=1$ and a liquidity of 15000 . The fee setting was $f=0.005$, half the volatility. Left panel: the token of the pool as a function of the price activity; middle panel: A comparison of the price at the CEX and the price at the DEX. Orange curve is the price at CEX, whereas the blue curve is $1.02 \times p_{s}$ to make it distinguishable. We see that the blue curve follows the orange curve as a consequence of the arbitrage activity. Also, we find that certain arbitrage steps are left out because they are not profitable. Right panel: Fees generated in the process.

true in the short term limit, in the long term limit the differences level out and the average revenue generation through fees does not depend on the actual fee setting, in line with the discussion utilizing the simplified random walk. Before we start with the actual discussion of the statistics we want to show the data as collected in one run for a specific example. The results are shown in Figure. 3 .

In the following we are going to study in which region the conditions defined for the random walk apply. Remember that the main result: For sideways motion, the exact fee setting did not seem to matter. We will further substantiate this claim and point out when it actually holds based on a more 'microscopic' analysis. To this end, we have studied the following case: we simulate an equidistant price series of 1000 points with a starting price of $p_{s}=p_{C E X}=1$ and a volatility per time step of $\sigma=0.001$. The liquidity of the system is chosen to be $L=15000$. We have checked that those starting parameters are not important to the statements we are going to make. In a next step we have simulated 1000 statistically independent runs and studied the role of the fee. We find that the average return for a given volatility $\sigma$ as a function of the fee $f$ is quite sensitive to fees for $f<\sigma$ while it quickly levels off for fees higher than the volatility, see Fig. 4. The important point is that this validates our previous analysis while giving an indication for a lower bound for the optimal choice of the fees.

## 5 Conclusion

In this paper we developed a minimal model to model the return of a DEX for a core pool of heavily arbitraged pairs. We find that for 'sideways motion' the

![](https://cdn.mathpix.com/cropped/2024_04_26_8b4d692a99c3f373d62dg-11.jpg?height=745&width=1222&top_left_y=904&top_left_x=473)

Figure 4: The simulation was run for 1000 steps with a volatility of 0.001 per step, an initial price of $p_{s}=p_{C E X}=1$ and a liquidity of 15000 . We find that it is a reasonable choice to choose the fee according to the volatility, ideally slightly higher.
specific value of the fee is not important, as long as is is not chosen to be too high. We also find that a lower bound for the fee is the minimal price change between blocks. We confirm our analysis with both a full fledged numerical simulation as well as a minimal model based on a random walk with rewards. In a subsequent study we will study the influence of asymmetric fees in the case of directed price action.

## References

[Adams et al.(2020)] Hayden Adams, Noah Zinsmeister, and Dan Robinson. 2020. Uniswap v2 Core. Retrieved Jun 12, 2023 from https://uniswap.org/ whitepaper.pdf

[Adams et al.(2021)] Hayden Adams, Noah Zinsmeister, Moody Salem, River Keefer, and Dan Robinson. 2021. Uniswap v3 Core. Retrieved Jun 12, 2023 from https: //uniswap.org/whitepaper-v3.pdf

[Bukov and Melnik(2020)] Anton Bukov and Mikhail Melnik. 2020. Mooniswap by 1inch.exchange. Retrieved Sept 18, 2023 from https://mooniswap.exchange/ docs/MooniswapWhitePaper-v1.0.pdf

[Capponi and Jia(2021)] Agostino Capponi and Ruizhe Jia. 2021. The adoption of blockchain-based decentralized exchanges. arXiv preprint arXiv:2103.08842 (2021).

[Egorov and GmbH)(2021)] Michael Egorov and Curve Finance (Swiss Stake GmbH). 2021. Automatic market-making with dynamic peg. Retrieved Sept 18, 2023 from https://classic.curve.fi/files/crypto-pools-paper.pdf

[Hanson(2007)] Robin Hanson. 2007. Logarithmic markets coring rules for modular combinatorial information aggregation. The Journal of Prediction Markets 1, 1 (2007), 3-15.

[Hasbrouck et al.(2022)] Joel Hasbrouck, Thomas J Rivera, and Fahad Saleh. 2022. The need for fees at a dex: How increases in fees can increase dex trading volume. Available at SSRN (2022).

[Lehar and Parlour(2021)] Alfred Lehar and Christine A Parlour. 2021. Decentralized exchanges. Available at SSRN 3905316 (2021).

[MountainFarmer et al.(2022)] MountainFarmer, Louis, Hanzo, Wawa, Murloc, and Fish. 2022. JOE v2.1 Liquidity Book. Retrieved Sept 18, 2023 from https://github.com/traderjoe-xyz/LB-Whitepaper/blob/main/ Joe\%20v2\%20Liquidity\%20Book\%20Whitepaper.pdf

[Nezlobin(2023)] Alex Nezlobin. 2023. Twitter thread. Retrieved Dec 3, 2023 from https://twitter.com/0x94305/status/1674857993740111872

[Othman et al.(2013)] Abraham Othman, David M Pennock, Daniel M Reeves, and Tuomas Sandholm. 2013. A practical liquidity-sensitive automated market maker. ACM Transactions on Economics and Computation (TEAC) 1, 3 (2013), 1-25.

[Ottina et al.(2023)] M. Ottina, P.J. Steffensen, and J. Kristensen. 2023. Automated Market Makers: A Practical Guide to Decentralized Exchanges and Cryptocurrency Trading. Apress. https://books.google.nl/books?id=BKU6zwEACAAJ

[Volosnikov et al.(2022)] Vladislav Volosnikov, Vladimir Tikhomirov, Ilya Azhel, and Ilya Chizh. 2022. ALGEBRA Ecosystem: Decentralized exchange. https://algebra.finance/static/Algerbra\ Tech\% 20Paper-15411d15f8653a81d5f7f574bfe655ad.pdf


[^0]:    *abealexander@outlook.com

    †l.fritz@uu.nl

