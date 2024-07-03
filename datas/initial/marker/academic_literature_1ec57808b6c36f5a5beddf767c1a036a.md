# The Peal Method: A Mathematical Framework To Streamline Securitization Structuring

Antonio Scala Institute for Complex Systems CNR
antonio.scala@cnr.it Andrea Pinto Private Practice Neuture.ai andrea.pinto@neuture.ai April 9, 2024

## Abstract

Securitization is a financial process where the cash flows of incomegenerating assets are sold to institutional investors as securities, liquidating illiquid assets. This practice presents persistent challenges due to the absence of a comprehensive mathematical framework for structuring asset-backed securities. While existing literature provides technical analysis of credit risk modeling, there remains a need for a definitive framework detailing the allocation of the inbound cash flows to the outbound positions. To fill this gap, we introduce the PEAL
Method: a 10-step mathematical framework to streamline the securitization structuring across all time periods.

The PEAL Method offers a rigorous and versatile approach, allowing practitioners to structure various types of securitizations, including those with complex vertical positions. By employing standardized equations, it facilitates the delineation of payment priorities and enhances risk characterization for both the asset and the liability sides throughout the securitization life cycle.

In addition to its technical contributions, the PEAL Method aims to elevate industry standards by addressing longstanding challenges in securitization. By providing detailed information to investors and enabling transparent risk profile comparisons, it promotes market transparency and enables stronger regulatory oversight.

In summary, the PEAL Method represents a significant advancement in securitization literature, offering a standardized framework for precision and efficiency in structuring transactions. Its adoption has the potential to drive innovation and enhance risk management practices in the securitization market.

## Contents

| 1     | Unboxing securitizations                            | 4   |    |
|-------|-----------------------------------------------------|-----|----|
| 1.1   | Introduction                                        | 4   |    |
| 1.2   | Securitization definition                           |     | 4  |
| 1.3   | Securitization: asset-side basic variables          |     | 5  |
| 1.4   | Securitization: liability-side basic variables      | 7   |    |
| 1.5   | Inputs, Events, Scenarios & Clusters definition     |     | 7  |
| 2     | The PEAL Method to structure a securitization       | 9   |    |
| 2.1   | Structuring a securitization                        |     | 10 |
| 3     | Step 1: Select the Type of Exposures                | 10  |    |
| 4     | Step 2: Select the LE & generate the Scenarios      | 11  |    |
| 5     | Step 3: Basic inbound building-blocks (BIB)         | 11  |    |
| 5.1   | Asset building-block (A)                            | 12  |    |
| 5.2   | Loss building-block (L)                             | 12  |    |
| 5.3   | Event recovery building-block (E)                   | 13  |    |
| 5.4   | Disambiguating spot vs non-spot cash flows          |     | 13 |
| 6     | Step 4: Composite inbound building-blocks (CIB)     | 15  |    |
| 6.1   | Optimization inbound building-block                 |     | 15 |
| 6.2   | Total Inbound Cash Flows (ICF)                      |     | 15 |
| 6.3   | Total Available Funds (TAF)                         |     | 16 |
| 6.4   | Total Loss (TL)                                     | 16  |    |
| 6.5   | Total Net Loss (TNL)                                |     | 16 |
| 6.6   | Total Loss Tranching                                | 17  |    |
| 6.6.1 | Tranching definition                                |     | 17 |
| 6.6.2 | FLT substantial margin                              |     | 19 |
| 7     | Step 5: Select the number of Positions              | 19  |    |
| 7.1   | Position definition                                 |     | 20 |
| 7.2   | Position Qualities                                  | 21  |    |
| 7.3   | Embedded Positions                                  |     | 22 |
| 7.3.1 | Super Senior Embedded Positions                     | 23  |    |
| 7.3.2 | Super Junior Embedded Positions                     |     | 24 |
| 7.4   | Compute the number of Positions                     | 24  |    |
| 8     | Step 6: Positions' Designing to absorb the Tranches | 24  |    |
| 8.1   | Designing definition                                |     | 25 |
| 8.2   | Virtual Positions                                   |     | 26 |
| 8.3   | Horizontal Components                               |     | 27 |
| 8.4   | Vertical Components                                 |     | 27 |

| 8.5                                            | Positions' Designing                           |     | 28   |
|------------------------------------------------|------------------------------------------------|-----|------|
| 8.6                                            | Illustrative example                           | 29  |      |
| 8.7                                            | A particular Design of a general method        |     | 29   |
| 9                                              | Step 7: Dimension the Gross Cost & Gross Notes | 29  |      |
| 9.1                                            | Gross Dimensioning definition                  | 30  |      |
| 9.2                                            | Select the frequencies                         | 30  |      |
| 9.3                                            | Frequency transformation function              |     | 31   |
| 9.4                                            | Compute GV                                     |     | 31   |
| 9.5                                            | Compute GC & GN                                |     | 32   |
| 9.6                                            | Compute GH                                     |     | 32   |
| 9.7                                            | Horizontal rule g-check                        | 32  |      |
| 10 Step 8: Dimension the Net Costs & Net Notes | 33                                             |     |      |
| 10.1 Net Dimensioning Definition               | 33                                             |     |      |
| 10.2 Gross Dimensioning Matrix                 |                                                | 33  |      |
| 10.3 Net Dimensioning Matrix                   |                                                | 34  |      |
| 10.3.1                                         | Step 1: compute the total gross position       |     | 34   |
| 10.3.2                                         | Step 2: compute the total net position         |     | 35   |
| 10.3.3                                         | Step 3: compute the net dimensioning matrix    |     | 36   |
| 10.4 Vertical Components Net Dimensioning      |                                                | 36  |      |
| 10.5 Cost & Note Net Dimensioning              |                                                | 37  |      |
| 10.6 Cost & Note Losses                        | 37                                             |     |      |
| 11 Step 9: Compute the relevant Features       | 38                                             |     |      |
| 11.1 Exposure Performance (EP)                 | 38                                             |     |      |
| 11.2 Position Thickness (TH)                   | 40                                             |     |      |
| 11.2.1                                         | The Thickness regulatory definition            | 40  |      |
| 11.2.2                                         | The PEAL Method Thickness definition           |     | 42   |
| 11.3 Regulatory Capital (RC)                   | 42                                             |     |      |
| 11.4 Coefficient of Variation Adjusted (CVA)   |                                                | 44  |      |
| 11.5 Fair Value (FV)                           | 44                                             |     |      |
| 11.6 Internal Rate of Return (IRR)             | 45                                             |     |      |
| 12 Step 10: Optimize the Structuring Method    | 47                                             |     |      |
| 13 Next steps                                  | 47                                             |     |      |

14 Conclusions 49 A Description of the elements of any List of Events 51

## 1 Unboxing Securitizations 1.1 Introduction

Securitization is a financial process where the cash flows of income-generating assets are sold to institutional investors as securities, liquidating illiquid assets. Despite securitization modelling complexity, the literature addressing the requisite mathematical modeling is sparse. While there are a few notable exceptions - such as the two excellent books describing in detail the issues encountered in structuring asset-backed securities (Bluhm and Overbeck, 2006; Bluhm et al., 2010) - a comprehensive mathematical framework describing how the inbound cash flows are allocated to the outbound positions is lacking. This paper introduces the PEAL Method, a 10-step mathematical framework designed to streamline securitization structuring while encompassing a comprehensive analysis across all time periods. It offers a standardized mathematical approach adaptable to various scenarios, ensuring compliance with regulations and enabling transparent risk assessment for both the asset and the liability sides. Inspired by Queuing Theory, which elucidates queuing system dynamics, we present securitization as a mathematical study akin to optimizing queuing processes. By establishing a link between inbound and outbound cash flows in 10 steps, our method aims to enhance efficiency and affordability in structuring securitizations, ultimately fostering transparency and regulatory compliance.

## 1.2 Securitization Definition

European Regulation No 2402/2017 (Reg 2402), Article 2(1), defines securitization as a "transaction or scheme, whereby the credit risk associated with an exposure or a pool of exposures" (Exposures) "is tranched, having all of the following characteristics: (a) payments" [to the securitization positions (Positions, see definition in Sec. 7.1)] "in the transaction or scheme are dependent upon the performance" of the Exposures; "(b) the subordination of tranches determines the distribution of losses during the *ongoing life* of the transaction or scheme; (c) the transaction or scheme does not create exposures which possess all of the characteristics listed in Article 147(8) of Regulation No 575/2013".

Article 2(1)(a) requires that the payments toward the Positions be dependent upon the performance of the Exposures. Therefore a scheme or transaction is not considered a securitization if the Exposures *ongoing losses* are always zero ∀ t. In fact, if this were the case, there would be no credit risk to "tranche", and thus the letter (b) requirement would not be satisfied.

Whilst it is necessary the presence of potential losses, it is not sufficient per sé. Article 2(1)(b) additionally requires to "tranche the credit risk" in such a way that the losses be allocated to the different Positions so as to reflect the subordination of tranches continuously during their *ongoing life*.

Thus, Reg 2402 defines securitization in mathematical terms: in order to classify a scheme or transaction as a *securitization*, both the Exposures' ongoing losses and the Positions' cash flows must be calculated and jointly analyzed. To our best knowledge, there is no prior paper that has defined a clear relationship between these two elements. Indeed, we aspire to fill this gap, identifying the main inbound and outbound building-blocks needed to structure a securitization and providing a conceptual and mathematical definition of each element individually and in correlation to the others.

This paper1introduces the PEAL Method2that, correlating the inbound to the outbound cash flows, opens up the securitization black-box and enables more sophisticated and robust statistical analyses. Our mathematical approach leaves less room for possible arrangers' misjudgments, all while easing the Public Authorities supervision.

## 1.3 Securitization: Asset-Side Basic Variables

Let the asset-side of a securitization be composed of K ≥ 1 portfolios, and let each portfolio k have a number of Exposures Nk. Each of the n =
1*, . . . , N*k Exposures of portfolio k is amortized over Tk,n months, that are pooled together into the securitization at month τˆk (where Tk,n and τˆk ∈ N).

By exploiting these definitions, let a securitization be *Basic* when all the portfolios K are structured at the same initial time τˆ1 = ˆτ2 = *. . .* τˆK = ˆτ
∗.

On the other hand, let a securitization be *Rolling* when at least one of the portfolios K ≥ 2 is structured at a time τˆk > τˆ
∗. We indicate by N

$$N=\sum_{k=1}^{K}N_{k}$$
$$\left(1\right)$$
$${\mathrm{i}}{\mathrm{h~flows.~If~}}T_{k}$$
$\left(2\right)$. 
$\left(3\right)$. 
Nk (1)
the total number of Exposures generating inbound cash flows. If Tk

$$T_{k}=\operatorname*{max}_{n=1,\dots N_{k}}\;T_{k,n}+\hat{\tau}_{k}$$
Tk,n + ˆτk (2)
is the duration of each portfolio k, then the Exposures maximum duration is T = max k Tk (3)
We assume that the time when Exposures are pooled together is

$$T=$$
$$T_{k}$$
$${\mathrm{gether~is~}}$$
$${\hat{\tau}}^{*}=\operatorname*{min}_{k}\ {\hat{\tau}}_{k}$$
$\left(4\right)$. 
k
τˆk (4)
where τˆ
∗is the origin of our timeline that, when not differently specified, is τˆ
∗ = 0. Then for each Exposure (*k, n*) we define the installments Rk,n(t) as Rk,n(t) = Ck,n(t) + Ik,n(t) (5)
where Ck,n(t) and Ik,n(t) are the quota capital and interest of the Exposure amortization schedule. We assume that Ck,n and Ik,n be zero outside the time interval where they are defined, i.e Ck,n(t) = Ik,n(t) = 0 for t < τˆ
∗
or t > Tk,n. Notice that with τˆ
∗ = 0, the first installment is due at the beginning of the subsequent period t = 1 *. . . T*. Then, the total capital due by Exposure (*k, n*) is

$$C_{k,n}=\sum_{t=0}^{T}C_{k,n}(t)$$

and the outstanding capital of Exposure (*k, n*) is

$$O C_{k,n}(t)=C_{k,n}-\sum_{\tau=0}^{t}C_{k,n}(\tau)=\sum_{\tau=t+1}^{T}C_{k,n}(\tau)$$
$$({\mathfrak{h}})$$
$$\left(7\right)$$
$$({\mathfrak{s}})$$

while the total securitization capital is

$$C=\sum_{k=1}^{K}\sum_{n=1}^{N_{k}}C_{k,n}$$
Ck,n (8)
The total interest due by Exposure (*k, n*) is

$$I_{k,n}=\sum_{t=0}^{T}I_{k,n}(t)$$
Ik,n(t) (9)
and the outstanding interest of Exposure (*k, n*) is

$$O I_{k,n}(t)=I_{k,n}-\sum_{\tau=0}^{t}I_{k,n}(\tau)=\sum_{\tau=t+1}^{T}I_{k,n}(\tau)$$
$$({\mathfrak{g}})$$

$$(10)$$
$$(11)$$

while the total securitization interest is

$$I=\sum_{k=1}^{K}\sum_{n=1}^{N_{k}}I_{k,n}$$

We can then define the total securitization outstanding balance as

$$O B(t)=O C(t)+O I(t)=\sum_{k=1}^{K}\sum_{n=1}^{N_{k}}O C_{k,n}(t)+O I_{k,n}(t)\qquad\quad(12)$$

We call a securitization "Islamic" when the total interest Ik,n(t) of any Exposure (*N, K*) is always 0 ∀ t, and "European" otherwise. Independently if the securitization were to be Basic or Rolling, Islamic or European, the equations in this paper would hold true.

## 1.4 Securitization: Liability-Side Basic Variables

Let a securitization liability-side be composed of P ≥ 2 Positions (see definition in Sec. 7). Each of the p = 1*, . . . , P* Positions is amortized over Tp months. All P Positions start their amortization period at the same time τˆ
∗, and their maximum duration is

$$T P=\operatorname*{max}_{p}\,T_{p}$$
$$(13)$$
pTp (13)
where T P ∈ N and T P ≤ T. Indeed, because there is a mismatch between the inbound and the outbound cash flow lifespan, often *T P < T*: for example, it might happen that the securitization Positions' lifespan be 15 years while some Exposures might pay installments for 17 years. Currently, most practitioners would discount the extra 2-years Exposures' cash flows from year 17-th back to year 15-th implicitly assuming that the securitization will be able to sell those extra cash flows to interested 3-rd parties when the time come. This approach is not consistent with a pure cash-flow method, that requires to consider only cash flows that will certainly materialize within the Position maximum duration T P. Therefore, for the purpose of this paper, any inbound cash flow obtained after T P will not be considered in computing the Positions' outbound cash flows (i.e. OCF(t) = 0 ∀ *t > T P*).

## 1.5 Inputs, Events, Scenarios & Clusters Definition

We define as a Base Input ϕ any initial parameter to compute the inbound cash flows defined at the time τˆ
∗ of structuring. We call Φ the set of those unique Base Inputs. We define an Event λ to be any action or situation that might affect, in positive or negative, the Base Inputs at a certain time tˆ.

We call the set of those unique Events List of Events Λ or LE. An Event of the LE (λ ∈ Λ) may affect each Exposure (*k, n*) at a certain time tˆλ k,n, where 0 ≤ tˆλ k,n ≤ Tk,n. Let us recall that the Kronecker delta symbol is defined as

$$\delta_{a,b}=\begin{cases}0&{\mathrm{if~}}a\neq b\\ 1&{\mathrm{if~}}a=b\end{cases}$$
$$\left(14\right)$$

while the Heaviside theta symbol is defined as

$$\theta_{a,b}={\begin{cases}0&{\mathrm{if~}}a<b\\ 1&{\mathrm{if~}}a\geq b\end{cases}}$$
$$(15)$$

Thus, if any Event λ of the List of Event Λ affects the performance of the Exposure (*k, n*) from (or at) happening at time tˆλ k,n, then δt,tˆλ k,n allows us to account for the impact of *spot* Events, while θt,tˆλ k,n allows us to account for continuous Events whose impact extends from time tˆλ k,n on. In the following, to simplify the notation we indicate in formulas tˆλ k,n with tλ when it does not give rise to ambiguities.

We define a Scenario as a combination of the possible Events affecting the Base Inputs of all the Exposures N. We define the Base Scenario as the unique Scenario that is unaffected by any Event. The inbound cash flows computed in the Base Scenario can be considered as the initial estimated
"budget" at the time τˆ
∗ of structuring of the securitization. The inbound cash flows computed in any other Scenarios s will diverge from the Base Scenario for a certain amount: if it is positive it is a gain while if it is negative it is a loss. In all other Scenarios, the probability of each Event affecting each Base Input ϕ of any Exposure (*k, n*) differs according to their respective risk profile. In every Scenario, each Exposure (*k, n*) can be affected over time by one or more elements of the List of Events. Due to the combinatorial explosion problem, it is impossible to use a brute force approach to enumerate the total number of Scenarios |S| underlying the securitization (or even only the number of Scenarios |Sk| of portfolio k). Thus, it is necessary to use a sampling approach like the Monte Carlo Method. The reason is simple: if we consider only IF an element of the List of the Events materializes, the number of potential Scenarios |S| depends on the number of elements NE; such quantity grows exponentially with the number Nk of Exposures composing the K portfolios as

$$|S|=\prod_{k=1}^{K}N E^{N_{k}}$$
$$\left(16\right)$$

NENk (16)
On the other hand, for the PEAL Method, it is not only relevant IF an Exposure is affected by an Event, but also WHEN: the impact on its performance can be sensibly different if an Event happens at time t or at t+ 12.

Therefore, the probability of the Scenario's cash flows depends on the probability of each Event impacting over time each Exposure (*k, n*) composing that Scenario. Thus, the number of Scenarios |S| for a securitization composed of K portfolios, each with Nk Exposures with the same amortization period Tk,1 = Tk,2 *· · ·* = Tk and the same number of Events NE is

$$|S|=\prod_{k=1}^{K}((N E-1)\cdot T_{k}+1)^{N_{k}}$$
$$(17)$$

((NE − 1) · Tk + 1)Nk (17)
Thus, for example for a securitization composed of just one portfolio K = 1, with Nk = 100 Exposures, with an average Tk,n between 36 and 60 months and a LE composed of only 3 elements (Λ = 3), the total number of Scenarios |S| range between 73100 and 121100, that is well above the total estimated number of atoms in the universe (i.e. 1082). Therefore, direct enumeration of all possible Scenarios is out of reach and it becomes mandatory to use an indirect approach for the computations, like the Monte Carlo Method.

Finally, we define a Cluster as a set of homogeneous Exposures with the same risk profile: thus, we consider each portfolio k to correspond to a single Cluster. For example, let a securitization originate from a single portfolio whose Exposures can be described by two different probability density functions (PDF): since the portfolio is described by two different Clusters, we consider them as two separate portfolios, and thus K = 2.

## 2 The Peal Method To Structure A Securitization

After having defined in Sec. 1.2 the cases under which a transaction or a scheme must be considered a securitization, this Section introduces the PEAL Method structuring process. In abstract terms, a securitization has a balance sheet similar to the one of a traditional company: on the asset side there are the Exposures that generate inbound cash flows, and on the liability side there are the Positions to whom the securitization, at certain conditions, has the obligation to pay outbound cash flows. Such outbound payments must follow a univocal and unambiguous order, such that it must always be possible to describe it as a deterministic algorithm3. Equity is often negligible, thus we will not consider it in the modelling.

To date, the established structuring practice for the asset side often uses a *macro-approach* that entails that the total inbound cash flows be impacted by the negative Events historical loss averages. Thus, on the liability side, the documentation provided to investors - commonly known as investment memorandum - only shows the average Scenario without any data related to any risk metric of the Positions, especially to time-dependent metrics, that would allow investors and supervisory authorities to be continuously updated on the evolution of the Positions' performances. Indeed, such metrics are nowadays almost impossible to calculate with the current *macro-approach*.

The PEAL Method, by considering on the asset side the statistical properties of every single Exposure Nk in different Scenarios S, adopts a *microapproach* for calculating the securitization risk analysis on the liability side.

This is analogous to the development of statistical mechanics, an area of physics that, by studying the behavior of large groups of microscopic components (atoms, molecules) has allowed to explain the laws of classical thermodynamics, which studies the relationships among macroscopic quantities characterizing materials like temperature, pressure, and heat capacity. It is worth noting that there is an exponential number of micro-states in statistical mechanics, which contributes to the complexity of the system. At the same time, such complexity enables better characterization of the fluctuations of the system. On the same footing, this paper considers the statistical 3Notice that a strict usage of a deterministic algorithm to describe payments' priority removes ambiguities on who must be paid first and avoids litigations.

dynamics of the exponential number of possible outcomes to better characterize the ongoing Positions' risk profiles and time Features.

## 2.1 Structuring A Securitization

In the PEAL framework a Structuring Method is a set of mathematical rules to build a robust process where the total inbound cash flows are allocated as outbound cash flows among the different Positions respecting Reg 2402 provisions. All Structuring Methods follow the same 10-steps process. There are 4 Steps to characterize the asset side:
- Step 1: select the Exposures Type;
- Step 2: select the LE Λ and generate the Scenarios S;
4

- Step 3: compute the basic inbound building-blocks (BIB);
- Step 4: compute the composite inbound building-blocks (CIB).
Then there are 4 Steps to characterize the liability side:
- Step 5: select the number of X Cost and Y Note Positions; - Step 6: design the Positions to absorb the Tranches;
- Step 7: dimension the Gross Cost (GC) and Gross Notes (GN); - Step 8: compute the Net Cost (NC) and Net Notes (NN).

Finally, there are 2 Steps to optimize the securitization Structuring Methods:
- Step 9: compute the relevant Features; - Step 10: optimize the chosen Features.

In the next 10 Sections, we describe each of the above steps more in detail.

## 3 Step 1: Select The Type Of Exposures

Let a group of Exposures that exhibit similar characteristics be defined as a Type. The 1st Step of any Structuring Method is to select, for each portfolio k, the Type of Exposures (TE). The following is a non-exhaustive list of the eleven most used Types in Italy to date:
1. Corporate Loan (CL): loan provided to a company; 2. Mortgages Loan (ML): loan with an immovable asset as collateral; 4The set S must be a representative statistical sample of all the possible Scenarios S.