# The PEAL Method: a mathematical framework to streamline securitization structuring 

Andrea Pinto<br>Private Practice<br>Neuture.ai<br>andrea.pinto@neuture.ai

Antonio Scala<br>Institute for Complex Systems<br>CNR<br>antonio.scala@cnr.it

April 9, 2024


#### Abstract

Securitization is a financial process where the cash flows of incomegenerating assets are sold to institutional investors as securities, liquidating illiquid assets. This practice presents persistent challenges due to the absence of a comprehensive mathematical framework for structuring asset-backed securities. While existing literature provides technical analysis of credit risk modeling, there remains a need for a definitive framework detailing the allocation of the inbound cash flows to the outbound positions. To fill this gap, we introduce the PEAL Method: a 10-step mathematical framework to streamline the securitization structuring across all time periods.

The PEAL Method offers a rigorous and versatile approach, allowing practitioners to structure various types of securitizations, including those with complex vertical positions. By employing standardized equations, it facilitates the delineation of payment priorities and enhances risk characterization for both the asset and the liability sides throughout the securitization life cycle.

In addition to its technical contributions, the PEAL Method aims to elevate industry standards by addressing longstanding challenges in securitization. By providing detailed information to investors and enabling transparent risk profile comparisons, it promotes market transparency and enables stronger regulatory oversight.

In summary, the PEAL Method represents a significant advancement in securitization literature, offering a standardized framework for precision and efficiency in structuring transactions. Its adoption has the potential to drive innovation and enhance risk management practices in the securitization market.


## Contents

1 Unboxing securitizations ..... 4
1.1 Introduction ..... 4
1.2 Securitization definition ..... 4
1.3 Securitization: asset-side basic variables ..... 5
1.4 Securitization: liability-side basic variables ..... 7
1.5 Inputs, Events, Scenarios \& Clusters definition ..... 7
2 The PEAL Method to structure a securitization ..... 9
$2.1 \quad$ Structuring a securitization ..... 10
3 Step 1: Select the Type of Exposures ..... 10
4 Step 2: Select the LE \& generate the Scenarios ..... 11
5 Step 3: Basic inbound building-blocks (BIB) ..... 11
5.1 Asset building-block (A) ..... 12
5.2 Loss building-block (L). ..... 12
5.3 Event recovery building-block (E) ..... 13
5.4 Disambiguating spot vs non-spot cash flows ..... 13
6 Step 4: Composite inbound building-blocks (CIB) ..... 15
6.1 Optimization inbound building-block ..... 15
6.2 Total Inbound Cash Flows (ICF) ..... 15
6.3 Total Available Funds (TAF) ..... 16
6.4 Total Loss (TL) ..... 16
6.5 Total Net Loss (TNL) ..... 16
6.6 Total Loss Tranching ..... 17
6.6.1 Tranching definition ..... 17
6.6 .2 FLT substantial margin ..... 19
7 Step 5: Select the number of Positions ..... 19
7.1 Position definition ..... 20
7.2 Position Qualities ..... 21
7.3 Embedded Positions ..... 22
7.3.1 Super Senior Embedded Positions ..... 23
7.3.2 Super Junior Embedded Positions ..... 24
7.4 Compute the number of Positions ..... 24
8 Step 6: Positions' Designing to absorb the Tranches ..... 24
8.1 Designing definition ..... 25
8.2 Virtual Positions ..... 26
8.3 Horizontal Components ..... 27
8.4 Vertical Components ..... 27
8.5 Positions' Designing ..... 28
8.6 Illustrative example ..... 29
8.7 A particular Design of a general method ..... 29
9 Step 7: Dimension the Gross Cost \& Gross Notes ..... 29
9.1 Gross Dimensioning definition ..... 30
9.2 Select the frequencies ..... 30
9.3 Frequency transformation function ..... 31
9.4 Compute GV ..... 31
9.5 Compute GC \& GN ..... 32
9.6 Compute GH ..... 32
9.7 Horizontal rule g-check ..... 32
10 Step 8: Dimension the Net Costs \& Net Notes ..... 33
10.1 Net Dimensioning Definition ..... 33
10.2 Gross Dimensioning Matrix ..... 33
10.3 Net Dimensioning Matrix ..... 34
10.3.1 Step 1: compute the total gross position ..... 34
10.3.2 Step 2: compute the total net position ..... 35
10.3.3 Step 3: compute the net dimensioning matrix ..... 36
10.4 Vertical Components Net Dimensioning ..... 36
10.5 Cost \& Note Net Dimensioning ..... 37
10.6 Cost \& Note Losses ..... 37
11 Step 9: Compute the relevant Features ..... 38
11.1 Exposure Performance (EP) ..... 38
11.2 Position Thickness (TH) ..... 40
11.2.1 The Thickness regulatory definition, ..... 40
11.2.2 The PEAL Method Thickness definition ..... 42
11.3 Regulatory Capital (RC) ..... 42
11.4 Coefficient of Variation Adjusted (CVA) ..... 44
11.5 Fair Value (FV) ..... 44
11.6 Internal Rate of Return (IRR). ..... 45
12 Step 10: Optimize the Structuring Method ..... 47
13 Next steps ..... 47
14 Conclusions ..... 49
A Description of the elements of any List of Events ..... 51

## 1 Unboxing securitizations

### 1.1 Introduction

Securitization is a financial process where the cash flows of income-generating assets are sold to institutional investors as securities, liquidating illiquid assets. Despite securitization modelling complexity, the literature addressing the requisite mathematical modeling is sparse. While there are a few notable exceptions - such as the two excellent books describing in detail the issues encountered in structuring asset-backed securities (Bluhm and Overbeck, 2006; Bluhm et al., 2010) - a comprehensive mathematical framework describing how the inbound cash flows are allocated to the outbound positions is lacking. This paper introduces the PEAL Method, a 10-step mathematical framework designed to streamline securitization structuring while encompassing a comprehensive analysis across all time periods. It offers a standardized mathematical approach adaptable to various scenarios, ensuring compliance with regulations and enabling transparent risk assessment for both the asset and the liability sides. Inspired by Queuing Theory, which elucidates queuing system dynamics, we present securitization as a mathematical study akin to optimizing queuing processes. By establishing a link between inbound and outbound cash flows in 10 steps, our method aims to enhance efficiency and affordability in structuring securitizations, ultimately fostering transparency and regulatory compliance.

### 1.2 Securitization definition

European Regulation No 2402/2017 (Reg 2402), Article 2(1), defines securitization as a "transaction or scheme, whereby the credit risk associated with an exposure or a pool of exposures" (Exposures) "is tranched, having all of the following characteristics: (a) payments" [to the securitization positions (Positions, see definition in Sec. 7.1)] "in the transaction or scheme are dependent upon the performance" of the Exposures; "(b) the subordination of tranches determines the distribution of losses during the ongoing life of the transaction or scheme; (c) the transaction or scheme does not create exposures which possess all of the characteristics listed in Article 147(8) of Regulation No 575/2013".

Article 2(1)(a) requires that the payments toward the Positions be dependent upon the performance of the Exposures. Therefore a scheme or transaction is not considered a securitization if the Exposures ongoing losses are always zero $\forall t$. In fact, if this were the case, there would be no credit risk to "tranche", and thus the letter (b) requirement would not be satisfied. Whilst it is necessary the presence of potential losses, it is not sufficient per sé. Article 2(1)(b) additionally requires to "tranche the credit risk" in such a way that the losses be allocated to the different Positions so as to reflect the subordination of tranches continuously during their ongoing life.

Thus, Reg 2402 defines securitization in mathematical terms: in order to classify a scheme or transaction as a securitization, both the Exposures' ongoing losses and the Positions' cash flows must be calculated and jointly analyzed. To our best knowledge, there is no prior paper that has defined a clear relationship between these two elements. Indeed, we aspire to fill this gap, identifying the main inbound and outbound building-blocks needed to structure a securitization and providing a conceptual and mathematical definition of each element individually and in correlation to the others.

This paper ${ }^{1}$ introduces the PEAL Method ${ }^{2}$ that, correlating the inbound to the outbound cash flows, opens up the securitization black-box and enables more sophisticated and robust statistical analyses. Our mathematical approach leaves less room for possible arrangers' misjudgments, all while easing the Public Authorities supervision.

### 1.3 Securitization: asset-side basic variables

Let the asset-side of a securitization be composed of $K \geq 1$ portfolios, and let each portfolio $k$ have a number of Exposures $N_{k}$. Each of the $n=$ $1, \ldots, N_{k}$ Exposures of portfolio $k$ is amortized over $T_{k, n}$ months, that are pooled together into the securitization at month $\hat{\tau}_{k}$ (where $T_{k, n}$ and $\hat{\tau}_{k} \in N$ ). By exploiting these definitions, let a securitization be Basic when all the portfolios $K$ are structured at the same initial time $\hat{\tau}_{1}=\hat{\tau}_{2}=\ldots \hat{\tau}_{K}=\hat{\tau}^{*}$. On the other hand, let a securitization be Rolling when at least one of the portfolios $K \geq 2$ is structured at a time $\hat{\tau}_{k}>\hat{\tau}^{*}$. We indicate by $N$

$$
N=\sum_{k=1}^{K} N_{k}
$$

the total number of Exposures generating inbound cash flows. If $T_{k}$

$$
T_{k}=\max _{n=1 \ldots N_{k}} T_{k, n}+\hat{\tau}_{k}
$$

is the duration of each portfolio $k$, then the Exposures maximum duration is

$$
T=\max _{k} T_{k}
$$

We assume that the time when Exposures are pooled together is

$$
\hat{\tau}^{*}=\min _{k} \hat{\tau}_{k}
$$

where $\hat{\tau}^{*}$ is the origin of our timeline that, when not differently specified, is $\hat{\tau}^{*}=0$. Then for each Exposure $(k, n)$ we define the installments $R_{k, n}(t)$ as

$$
R_{k, n}(t)=C_{k, n}(t)+I_{k, n}(t)
$$[^0]where $C_{k, n}(t)$ and $I_{k, n}(t)$ are the quota capital and interest of the Exposure amortization schedule. We assume that $C_{k, n}$ and $I_{k, n}$ be zero outside the time interval where they are defined, i.e $C_{k, n}(t)=I_{k, n}(t)=0$ for $t<\hat{\tau}^{*}$ or $t>T_{k, n}$. Notice that with $\hat{\tau}^{*}=0$, the first installment is due at the beginning of the subsequent period $t=1 \ldots T$. Then, the total capital due by Exposure $(k, n)$ is

$$
C_{k, n}=\sum_{t=0}^{T} C_{k, n}(t)
$$

and the outstanding capital of Exposure $(k, n)$ is

$$
O C_{k, n}(t)=C_{k, n}-\sum_{\tau=0}^{t} C_{k, n}(\tau)=\sum_{\tau=t+1}^{T} C_{k, n}(\tau)
$$

while the total securitization capital is

$$
C=\sum_{k=1}^{K} \sum_{n=1}^{N_{k}} C_{k, n}
$$

The total interest due by Exposure $(k, n)$ is

$$
I_{k, n}=\sum_{t=0}^{T} I_{k, n}(t)
$$

and the outstanding interest of Exposure $(k, n)$ is

$$
O I_{k, n}(t)=I_{k, n}-\sum_{\tau=0}^{t} I_{k, n}(\tau)=\sum_{\tau=t+1}^{T} I_{k, n}(\tau)
$$

while the total securitization interest is

$$
I=\sum_{k=1}^{K} \sum_{n=1}^{N_{k}} I_{k, n}
$$

We can then define the total securitization outstanding balance as

$$
O B(t)=O C(t)+O I(t)=\sum_{k=1}^{K} \sum_{n=1}^{N_{k}} O C_{k, n}(t)+O I_{k, n}(t)
$$

We call a securitization "Islamic" when the total interest $I_{k, n}(t)$ of any Exposure $(N, K)$ is always $0 \forall t$, and "European" otherwise. Independently if the securitization were to be Basic or Rolling, Islamic or European, the equations in this paper would hold true.

### 1.4 Securitization: liability-side basic variables

Let a securitization liability-side be composed of $P \geq 2$ Positions (see definition in Sec. 77). Each of the $p=1, \ldots, P$ Positions is amortized over $T_{p}$ months. All $P$ Positions start their amortization period at the same time $\hat{\tau}^{*}$, and their maximum duration is

$$
T P=\max _{p} T_{p}
$$

where $T P \in N$ and $T P \leq T$. Indeed, because there is a mismatch between the inbound and the outbound cash flow lifespan, often $T P<T$ : for example, it might happen that the securitization Positions' lifespan be 15 years while some Exposures might pay installments for 17 years. Currently, most practitioners would discount the extra 2-years Exposures' cash flows from year 17 -th back to year 15 -th implicitly assuming that the securitization will be able to sell those extra cash flows to interested 3-rd parties when the time come. This approach is not consistent with a pure cash-flow method, that requires to consider only cash flows that will certainly materialize within the Position maximum duration $T P$. Therefore, for the purpose of this paper, any inbound cash flow obtained after $T P$ will not be considered in computing the Positions' outbound cash flows (i.e. $O C F(t)=0 \forall t>T P$ ).

### 1.5 Inputs, Events, Scenarios \& Clusters definition

We define as a Base Input $\phi$ any initial parameter to compute the inbound cash flows defined at the time $\hat{\tau}^{*}$ of structuring. We call $\Phi$ the set of those unique Base Inputs. We define an Event $\lambda$ to be any action or situation that might affect, in positive or negative, the Base Inputs at a certain time $\hat{t}$. We call the set of those unique Events List of Events $\Lambda$ or LE. An Event of the LE $(\lambda \in \Lambda)$ may affect each Exposure $(k, n)$ at a certain time $\hat{t}_{k, n}^{\lambda}$, where $0 \leq \hat{t}_{k, n}^{\lambda} \leq T_{k, n}$. Let us recall that the Kronecker delta symbol is defined as

$$
\delta_{a, b}= \begin{cases}0 & \text { if } a \neq b \\ 1 & \text { if } a=b\end{cases}
$$

while the Heaviside theta symbol is defined as

$$
\theta_{a, b}= \begin{cases}0 & \text { if } a<b \\ 1 & \text { if } a \geq b\end{cases}
$$

Thus, if any Event $\lambda$ of the List of Event $\Lambda$ affects the performance of the Exposure ( $k, n$ ) from (or at) happening at time $\hat{t}_{k, n}^{\lambda}$, then $\delta_{t, \hat{t}_{k, n}}$ allows us to account for the impact of spot Events, while $\theta_{t, \hat{\hat{t}_{k, n}}}$ allows us to account for continuous Events whose impact extends from time $\hat{t}_{k, n}^{\lambda}$ on. In the following,
to simplify the notation we indicate in formulas $\hat{t}_{k, n}^{\lambda}$ with $t_{\lambda}$ when it does not give rise to ambiguities.

We define a Scenario as a combination of the possible Events affecting the Base Inputs of all the Exposures $N$. We define the Base Scenario as the unique Scenario that is unaffected by any Event. The inbound cash flows computed in the Base Scenario can be considered as the initial estimated "budget" at the time $\hat{\tau}^{*}$ of structuring of the securitization. The inbound cash flows computed in any other Scenarios $s$ will diverge from the Base Scenario for a certain amount: if it is positive it is a gain while if it is negative it is a loss. In all other Scenarios, the probability of each Event affecting each Base Input $\phi$ of any Exposure $(k, n)$ differs according to their respective risk profile. In every Scenario, each Exposure $(k, n)$ can be affected over time by one or more elements of the List of Events. Due to the combinatorial explosion problem, it is impossible to use a brute force approach to enumerate the total number of Scenarios $|S|$ underlying the securitization (or even only the number of Scenarios $\left|S_{k}\right|$ of portfolio $k$ ). Thus, it is necessary to use a sampling approach like the Monte Carlo Method. The reason is simple: if we consider only IF an element of the List of the Events materializes, the number of potential Scenarios $|S|$ depends on the number of elements $N E$; such quantity grows exponentially with the number $N_{k}$ of Exposures composing the $K$ portfolios as

$$
|S|=\prod_{k=1}^{K} N E^{N_{k}}
$$

On the other hand, for the PEAL Method, it is not only relevant IF an Exposure is affected by an Event, but also WHEN: the impact on its performance can be sensibly different if an Event happens at time $t$ or at $t+12$. Therefore, the probability of the Scenario's cash flows depends on the probability of each Event impacting over time each Exposure $(k, n)$ composing that Scenario. Thus, the number of Scenarios $|S|$ for a securitization composed of $K$ portfolios, each with $N_{k}$ Exposures with the same amortization period $T_{k, 1}=T_{k, 2} \cdots=T_{k}$ and the same number of Events $N E$ is

$$
|S|=\prod_{k=1}^{K}\left((N E-1) \cdot T_{k}+1\right)^{N_{k}}
$$

Thus, for example for a securitization composed of just one portfolio $K=1$, with $N_{k}=100$ Exposures, with an average $T_{k, n}$ between 36 and 60 months and a LE composed of only 3 elements $(\Lambda=3)$, the total number of Scenarios $|S|$ range between $73^{100}$ and $121^{100}$, that is well above the total estimated number of atoms in the universe (i.e. $10^{82}$ ). Therefore, direct enumeration of all possible Scenarios is out of reach and it becomes mandatory to use an indirect approach for the computations, like the Monte Carlo Method.

Finally, we define a Cluster as a set of homogeneous Exposures with the same risk profile: thus, we consider each portfolio $k$ to correspond to a single Cluster. For example, let a securitization originate from a single portfolio whose Exposures can be described by two different probability density functions (PDF): since the portfolio is described by two different Clusters, we consider them as two separate portfolios, and thus $K=2$.

## 2 The PEAL Method to structure a securitization

After having defined in Sec. 1.2 the cases under which a transaction or a scheme must be considered a securitization, this Section introduces the PEAL Method structuring process. In abstract terms, a securitization has a balance sheet similar to the one of a traditional company: on the asset side there are the Exposures that generate inbound cash flows, and on the liability side there are the Positions to whom the securitization, at certain conditions, has the obligation to pay outbound cash flows. Such outbound payments must follow a univocal and unambiguous order, such that it must always be possible to describe it as a deterministic algorithm ${ }^{3}$. Equity is often negligible, thus we will not consider it in the modelling.

To date, the established structuring practice for the asset side often uses a macro-approach that entails that the total inbound cash flows be impacted by the negative Events historical loss averages. Thus, on the liability side, the documentation provided to investors - commonly known as investment memorandum - only shows the average Scenario without any data related to any risk metric of the Positions, especially to time-dependent metrics, that would allow investors and supervisory authorities to be continuously updated on the evolution of the Positions' performances. Indeed, such metrics are nowadays almost impossible to calculate with the current macro-approach.

The PEAL Method, by considering on the asset side the statistical properties of every single Exposure $N_{k}$ in different Scenarios $S$, adopts a microapproach for calculating the securitization risk analysis on the liability side. This is analogous to the development of statistical mechanics, an area of physics that, by studying the behavior of large groups of microscopic components (atoms, molecules) has allowed to explain the laws of classical thermodynamics, which studies the relationships among macroscopic quantities characterizing materials like temperature, pressure, and heat capacity. It is worth noting that there is an exponential number of micro-states in statistical mechanics, which contributes to the complexity of the system. At the same time, such complexity enables better characterization of the fluctuations of the system. On the same footing, this paper considers the statistical[^1]dynamics of the exponential number of possible outcomes to better characterize the ongoing Positions' risk profiles and time Features.

### 2.1 Structuring a securitization

In the PEAL framework a Structuring Method is a set of mathematical rules to build a robust process where the total inbound cash flows are allocated as outbound cash flows among the different Positions respecting Reg 2402 provisions. All Structuring Methods follow the same 10-steps process. There are 4 Steps to characterize the asset side:

- Step 1: select the Exposures Type;
- Step 2: select the $\operatorname{LE} \Lambda$ and generate the Scenarios $\mathcal{S} ;{ }^{4}$
- Step 3: compute the basic inbound building-blocks (BIB);
- Step 4: compute the composite inbound building-blocks (CIB).

Then there are 4 Steps to characterize the liability side:

- Step 5: select the number of X Cost and Y Note Positions;
- Step 6: design the Positions to absorb the Tranches;
- Step 7: dimension the Gross Cost (GC) and Gross Notes (GN);
- Step 8: compute the Net Cost (NC) and Net Notes (NN).

Finally, there are 2 Steps to optimize the securitization Structuring Methods:

- Step 9: compute the relevant Features;
- Step 10: optimize the chosen Features.

In the next 10 Sections, we describe each of the above steps more in detail.

## 3 Step 1: Select the Type of Exposures

Let a group of Exposures that exhibit similar characteristics be defined as a Type. The 1st Step of any Structuring Method is to select, for each portfolio $k$, the Type of Exposures (TE). The following is a non-exhaustive list of the eleven most used Types in Italy to date:

1. Corporate Loan (CL): loan provided to a company;
2. Mortgages Loan (ML): loan with an immovable asset as collateral;[^2]
3. Auto Loan (AL): loan with a car or truck as collateral;
4. Student Loan (SL): loan provided to a student for education;
5. Credit Card Loan (CC): money borrowed per credit card expenses;
6. Cessione Quinto Pensione (QP): pension-backed loan;
7. Cessione Quinto Salario (QS): salary-backed loan;
8. Real Estate (RE): property-generating income (e.g. lands, buildings);
9. Energy Estate (EE): equipment producing clean energy;
10. Exotic Asset (EA): perishable assets (e.g. wine, reggiano parmesan);
11. Negative Event Exposures (NE): any loan that is affected by a negative Event by the time of structuring $\hat{\tau}_{k}$ (so-called unlikely-to-pay or non-performing-exposures).

Notice that, although it is mathematically possible to structure a securitization composed of $K$ portfolios with heterogeneous Types, European supervisory authorities have forbidden this provision in Reg 2402. Thus, to date all $K$ portfolios composing an European securitization must be homogeneous in Type. Notice that Clusters further refine the definition of Types: in fact, the Exposures of the same Cluster not only have the same Type but also the same risk profile. Thus, a securitization based on Auto Loans with ratings A and B, would consist of $K=2$ portfolios (Clusters) with the same Type.

## 4 Step 2: Select the LE \& generate the Scenarios

The 2nd Step of any Structuring Method is to select, for each portfolio $k$, the List of Events $(L E) \Lambda$ that best describe the selected Type of Exposures, used to compute the Clusters. Some of the most relevant Events that might affect each Type of Exposure are listed in Table 1 in Appendix A. Consider that any Structuring Method might use only a subset of the List of Events $\Lambda$ in Table 1. As an example, if the List of Events were just: prepayments ("pe") and defaults ("de"), then the $\Lambda=\{p e, d e\}$. Once selected the $L E$, the arranger must generate the relative Scenarios via Monte Carlo, respecting the Clusters' risk profile distributions and correlations.

## 5 Step 3: Basic inbound building-blocks (BIB)

As will be further explained in this Section, the inbound cash flows can be allocated to 3 basic mutually exclusive and commonly exhaustive buildingblocks (the Basic Inbound building-Blocks or BIB) that allow designing
uniquely the securitization asset-side: the assets $(\mathbf{A})$, the losses $(\mathbf{L})$; and the events recovery (E). The 3rd Step of any Structuring Method is to compute the BIB. See Sec. 11.1 for the definition of Full-Performing, Performing, Non-Performing, and Super-Performing Exposures.

### 5.1 Asset building-block (A)

Let the inbound cash flows of the $(K, N)$ Exposures in the Base Scenario be defined as Gross Asset $G A(t)$. Exploiting this definition, the Base Scenario $b$ inbound cash flows of an Exposure $(k, n)$ is

$$
R_{k, n}^{(b)}(t)=R_{k, n}(t)=C_{k, n}(t)+I_{k, n}(t)
$$

while the overall securitization Base Scenario inbound cash flows is

$$
G A(t)=\sum_{k=1}^{K} \sum_{n=1}^{N_{k}} R_{k, n}^{(b)}(t)
$$

Then, the Scenario $s$ inbound cash flows of a Performing Exposure $(k, n)$ is

$$
R_{k, n}^{(s)}(t)=C_{k, n}(t) \cdot \prod_{\lambda \in \Lambda}\left(1-\theta_{t, t_{\lambda, s}^{c}}\right)+I_{k, n}(t) \cdot \prod_{\lambda \in \Lambda}\left(1-\theta_{t, t_{\lambda, s}^{i}}\right)
$$

while the overall securitization Scenario $s$ inbound cash flows is

$$
A^{(s)}(t)=\sum_{k=1}^{K} \sum_{n=1}^{N_{k}} R_{k, n}^{(s)}(t)
$$

that is the Asset building-block. Notice that $\lambda$ is any Event of the List of Events $\Lambda$, affecting in a particular Scenario the Exposure $(k, n)$; and $\theta_{t, t_{\lambda}}$ is the Heaviside function as explained in Sec. 1.5. There exist Events that may impact only the capital $C_{k, n}(t)$ at time $t_{\lambda}^{c}$ or only the interest $I_{k, n}(t)$ at time $t_{\lambda}^{i}$. Considering that the $\prod_{\lambda \in \Lambda}\left(1-\theta_{t, t_{\lambda}}\right)$ is the same as multiplying the cash flows for $\left(1-\theta_{t, \hat{t}_{\lambda}}\right)$, where $t_{\lambda}$ is the first occurrence in each Scenario $s$ of any Event. We can then simplify Equation 20) to

$$
R_{k, n}^{(s)}(t)=C_{k, n}(t) \cdot\left(1-\theta_{t, \hat{t}_{\lambda, s}^{c}}\right)+I_{k, n}(t) \cdot\left(1-\theta_{t, \hat{t}_{\lambda, s}^{i}}\right)
$$

### 5.2 Loss building-block (L)

Let the Scenario $s$ inbound cash flows of Non-Performing \& Super-Performing Exposures be defined as the Losses building-block $L^{(s)}(t)$. Exploiting this definition, the Scenario $s$ inbound cash flows of a Non-Performing or SuperPerforming Exposure $(k, n)$ is

$$
L_{k, n}^{(s)}(t)=R_{k, n}^{(b)}(t)-R_{k, n}^{(s)}(t)
$$

then Scenario $s$ total losses are

$$
L^{(s)}(t)=\sum_{k=1}^{K} \sum_{n=1}^{N_{k}} L_{k, n}^{(s)}(t)=G A(t)-A^{(s)}(t)
$$

When in a particular Cluster all the $(\lambda \in \Lambda)$ Events affecting the Exposures of the $K$ portfolios are MECE, the previous Equation (24) becomes

$$
L^{(s)}(t)=\sum_{k=1}^{K} \sum_{n=1}^{N_{k}} R_{k, n}^{(b)}(t) \cdot \sum_{\lambda \in \Lambda} \theta_{t, t_{\lambda, s}}
$$

where $\sum_{\lambda \in \Lambda} \theta_{t, t_{\lambda}} \in\{0,1\}$. Then, the Scenario cumulative Loss is

$$
L^{(s)}=\sum_{t=0}^{T} L^{(s)}(t)
$$

Exploiting $L^{(s)}$ definition is possible to establish a liability-independent metric to compute the asset-side losses. Indeed, any Financial Institution, given the same assets inputs and with comparable risk models, would get an equivalent $L^{(s)}(t)$ distribution, despite substantially different Waterfall Configurations, and thus different payment priorities (see definition in Sec. 8).

### 5.3 Event recovery building-block (E)

Let the spot inbound cash flows mitigating negative or deriving by positive Events in the Scenario $s$ be defined as the event recovery building-block $E^{(s)}(t)$. For example, in Corporate Loans Type if the List of Events where $\Lambda=\{p e, d e, e u\}$, then the Exposure $(k, n)$ event recovery $E_{k, n}(t)$ would be the sum of "spot" recoveries such as the prepayments $p_{k, n}(t)$ and the recovery of collateral $d_{k, n}(t)$ as

$$
E_{k, n}^{(s)}(t)=p_{k, n}^{(s)}(t)+d_{k, n}^{(s)}(t)
$$

while the total inbound event recovery in Scenario $s$ would be

$$
E^{(s)}(t)=\sum_{k=1}^{K} \sum_{n=1}^{N_{k}} E_{k, n}^{(s)}
$$

### 5.4 Disambiguating spot vs non-spot cash flows

In the previous Sections we have explained that non-spot $5^{5}$ inbound cash flows shall be described by the Gross Assets $G A(t)$, the Assets $A(t)$ and the Losses[^3]$L(t)$. On the other hand, the spot ${ }^{6}$ inbound cash flows shall be described by the event recovery $E(t)$.

For example, if we consider the Corporate Loans Type of Exposures we know from Table 1 that the main Events that apply are $\Lambda=\{p e, d e, t r l, e u\}$ \}] Thus, an Exposure $(k, n)$ is expected to prepay voluntarily at time $t_{k, n}^{p p}$ if it is affected by the prepayment Event $p e$ : whilst the negative effect impacts the Assets $A(t)$, the positive prepayment cash flow is spot at time $t_{k, n}^{p p}$ and thus shall be absorbed by the event recovery building-block $E(t)$ as $p(t)$. The same approach can be used for the default Event $d e$, so the positive recovery of collateral cash flow is spot at time $t_{k, n}^{r e c}$ and thus shall be absorbed by the event recovery building-block $E(t)$ as $d(t)$. On the other hand, if an Exposure $(k, n)$ that has defaulted at time $t_{k, n}^{d f}$, is affected by the "return-tolife" Event $r t l$ at a time $t_{k, n}^{r t l}$ such that $t_{k, n}^{d f} \leq t_{k, n}^{r t l}<t_{k, n}^{r e c}$, then $d(t)=0$ and $A(t)$ will have the form:

$$
R_{k, n}^{(s)}(t)=R_{k, n}(t) \cdot\left(1-\theta_{t, t_{k, n}^{d f}}+\theta_{t, t_{k, n}^{r t l}}\right)
$$

where $\theta_{t, r_{k, n} t,}$ "reactivates" the cash flows after the recovery time $t_{k, n}^{r t l}$.

The same dynamic applies to the Euribor Event $e u$, where we expect the Euribor to change overtime versus its Base Input, and thus we need to account for the change of installment for each Exposure $(k, n)$ whose interest is dependant on the change of euribor. A positive or negative variation of the euribor from its Base Input value/function changes the Exposure $(k, n)$ total installment and therefore we can consider that the impact of the Euribor Event $e u$ is non-spot and thus shall be accounted in $A(t)$. Notice that if the new $A(t)$ is lower than the Base Input $G A(t)$, the $L_{k, n}\left(t \geq t_{k, n}^{e u}\right)>0$. On the other hand, if the new $A(t)$ is higher than the Base Input $G A(t)$, the $L_{k, n}\left(t \geq t_{k, n}^{e u}\right)<0$. Lastly, it is important to remember that a change in euribor shall not be immediately reflected in a change in the payments toward Positions: indeed, an increase in euribor is likely to increase the probability of default, and a decrease in euribor is likely to trigger an increase of prepayments, with respect to the default and the prepayment distribution values that were expected initially. Further analyses on the implication of the Euribor Event against the excess losses deriving from changes versus the Base Inputs shall be done.

The disambiguation logic applied in the previous example for Corporate Loans can be applied to any Event in any Type of Exposure. When deciding whether an inbound cash flow shall be allocated to Gross Assets $G A(t)$, Assets $A(t)$ or Events recovery $E(t)$, always consider if its cash flows are indeed spot or non-spot, and allocate accordingly the relative cash flows to the proper inbound building-block.[^4]

## 6 Step 4: Composite inbound building-blocks (CIB)

As will be further explained in this Section, the basic inbound building-blocks can be used to compute different composite inbound building-blocks (CIBs). The 4th Step of any Structuring Method is to compute all the following CIB:

1. $\operatorname{ICF}(t)$ : total inbound cash flows as in Eq. (31);
2. $T A F^{(s)}(t)$ : total available funds as in Eq. (32);
3. $T L^{(s)}(t)$ : inbound total loss as in Eq. (33);
4. $T N L^{(s)}(t)$ : inbound total net loss as in Eq. (35);
5. Tranches: first loss, second loss, and complementary loss tranches.

### 6.1 Optimization inbound building-block

Notice that, in calculating all the following composite inbound buildingblocks, we will introduce a new block that is dimensioned at the end of the structuring process, in the optimization phase of Step 10 (see Sec. 12). This "new" block represents an inbound cash flow paid by a 3rd-party, often una-tantum at time $t=0$, as a lump sum that is neither reimbursed nor remunerated (e.g. the upfront payment provided to cover the first agents' expenses in Negative Event Exposures) and will be called zero $(t)$ or $z(t)$. In the first structuring cycle, such amount shall be considered null $(z(t)=0)$, and only in the optimization phase the arranger will have the choice to dimension $z(t)$. To date, we define the Base Scenario $b$ initial endowment inbound cash flows as $z^{(b)}(t)$ and the Scenario $s$ initial endowment inbound cash flows $z^{(s)}(t)$. Normally, the difference between these two amount is always zero, but there might exist theoretical situations where $\left(z^{(b)}(t)>0\right)$ and $\left(z^{(s)}(t)=0\right)$ due to unexpected situations like the bankruptcy of the trustee hosting the cash flows or the default of the bonds in which the cash reserve is invested. In some cases, the difference might be due to a delay in the upfront payment by the 3-rd party.

### 6.2 Total Inbound Cash Flows (ICF)

We define the Base Scenario total inbound cash flows $I C F(t)$ as

$$
I C F(t)=G A(t)+E^{(b)}(t)+z^{(b)}(t)
$$

considering that in the Base Scenario $E^{(b)}(t)=0 \forall t$ then

$$
I C F(t)=G A(t)+z^{(b)}(t)
$$

that represents the maximum initial endowment given the Base Inputs.

### 6.3 Total Available Funds (TAF)

We define the inbound cash flows that can be allocated at any time $t$ as an outbound cash flows to the Positions in any Scenario $s$ as total available funds $T A F^{(s)}(t)$ as

$$
T A F^{(s)}(t)=A^{(s)}(t)+E^{(s)}(t)+z^{(s)}(t)
$$

### 6.4 Total Loss (TL)

We define the sum of Scenario $s$ Losses $L^{(s)}(t)$ and the difference between the Base Scenario $b$ and the Scenario $s$ optimization inbound block $z(t)$ plus the Super Senior Embedded Position $S S E^{(s)}(t)$ (see definition in Sec. 7.3 as Total Loss $T L^{(s)}(t)$

$$
\begin{aligned}
T L^{(s)}(t) & =L^{(s)}(t)+\left[z^{(b)}(t)-z^{(s)}(t)\right]+S S E^{(s)}(t) \\
& =\left[G A(t)-A^{(s)}(t)\right]+\left[z^{(b)}(t)-z^{(s)}(t)\right]+S S E^{(s)}(t) \\
& =\left[G A(t)+z^{(b)}(t)\right]-\left[A^{(s)}(t)+z^{(s)}(t)\right]+S S E^{(s)}(t) \\
& =I C F(t)-\left[T A F^{(s)}(t)-E^{(s)}(t)\right]+S S E^{(s)}(t) \\
& =\left[I C F(t)-T A F^{(s)}(t)\right]+E^{(s)}(t)+S S E^{(s)}(t) \\
& =T N L^{(s)}(t)+E^{(s)}(t)+S S E^{(s)}(t)
\end{aligned}
$$

where the $I C F(t)$ is Equation (31), the $T A F^{(s)}(t)$ is Equation (32), the $E^{(s)}(t)$ is Equation (28), the $T N L^{(s)}(t)$ is the Total Net Loss of Equation (35), and $S S E^{(s)}(t)$ is Equation (45).

Notice that the Super Senior Embedded Position $S S E^{(s)}(t)$ components are either additional expenses (see Excessive Costs or Cost of Recovery in Sec. 7.3) or reduced outbound cash flows for the Positions (see Excess Recovery in Section 7.3 that reduce the total available funds $T A F^{(s)}(t)$. Therefore, $S S E^{(s)}(t)$ shall be treated as "additional losses" and shall be added to the total loss $T L^{(s)}(t)$ to provide a clear picture of the securitization ongoing riskiness to the institutional investors and the public authorities. Finally, it is worth noticing that, by default, the Losses $L^{(s)}(t)$ are always "smooth" whilst the Total Losses $T L^{(s)}(t)$, absorbing the spot inbound cash flows, can have loss spikes. As shown in Sec. 6.6, by computing the Tranching on the distribution both of the $L^{(s)}(t)$ and of the $T L^{(s)}(t)$ it is possible to understand what percentage of risk depends on the non-spot functions and what percentage from the spot functions.

### 6.5 Total Net Loss (TNL)

We define the difference between the Scenario $s$ losses $L^{(s)}(t)$ and the Scenario $s$ events recovery $E^{(s)}(t)$ as the net loss $N L^{(s)}(t)$

$$
N L^{(s)}(t)=L^{(s)}(t)-E^{(s)}(t)
$$

Then, we define the difference between the Scenario $s$ total losses $T L^{(s)}(t)$ and the Scenario $s$ events recovery $E^{(s)}(t)$ as the total net loss $T N L^{(s)}(t)$

$$
\begin{aligned}
T N L^{(s)}(t) & =T L^{(s)}(t)-E^{(s)}(t) \\
& =\left[L^{(s)}(t)+z^{(b)}(t)-z^{(s)}(t)+S S E^{(s)}(t)\right]-E^{(s)}(t) \\
& =\left[G A(t)-A^{(s)}(t)\right]+\left[z^{(b)}(t)-z^{(s)}(t)\right]-E^{(s)}(t)+S S E^{(s)}(t) \\
& =\left[G A(t)+z^{(b)}(t)\right]-\left[A^{(s)}(t)+E^{(s)}(t)+z^{(s)}(t)\right]+S S E^{(s)}(t) \\
& =I C F(t)-T A F^{(s)}(t)+S S E^{(s)}(t)
\end{aligned}
$$

When relevant, prefer the total loss $T L^{(s)}(t)$ over the total net loss $T N L^{(s)}(t)$ to compute the Features, as a more robust metric to compare risk profiles across securitizations.

### 6.6 Total Loss Tranching

This Section is divided in 2 parts: in Sec. 6.6.1 we define the concept of first, second and complementary loss tranches from a regulatory perspective; and in Sec. 6.6 .2 we explain how to compute the significant margin within the First Loss Tranche.

### 6.6.1 Tranching definition

As previously stated, Reg 2402, Article 2(1)(b), explains that in a securitization the subordination of tranches determines the distribution of losses during the ongoing life of the transaction scheme. From this article we can infer two things: (i) the risk is segmented in more than one tranche; (ii) the tranches shall be evaluated on an "ongoing basis". In this paper, we will consider 3 types of tranches: the first loss tranche (FLT), the second loss tranche (SLT), and the complementary loss tranche (CLT).

Reg 2402, Article 2(18), defines the first loss tranche as "the most subordinated tranche in a securitization that is the first tranche to bear losses incurred on the exposures and thereby provides protection to the second loss and, where relevant, higher ranking tranches". What we can deduce from Article 2(18) is that in a securitization there must be at least two Positions $(P \geq 2)$ absorbing the different tranches. Therefore, each tranche must be covered by at least one Position, and each Position can "absorb" risk from more than one tranche. In addition, European Capital Requirement Regulation No 575/2013 consolidated version of January 2024 (CRR), Article 244(1)(a), explains that an "originator institution of a traditional securitization may exclude underlying exposures from its calculation of risk-weighted exposure amounts if $[\ldots]$ significant credit risk associated with the underlying exposures has been transferred to third parties". Article 244(2)(b) explains that "significant credit risk shall be considered as transferred" if "the
originator can demonstrate that the exposure value of the first loss tranche exceeds a reasoned estimate of the expected loss of the underlying exposure by a substantial margin". Thus the CRR links the FLT to the Exposure expected loss (EL or $\mu$ ) plus a substantial margin (sm). The CRR does neither provide further details on which distribution to compute the $E L$ nor on how to compute the "substantial margin". For the purpose of this paper, as distribution we will use the total net $\operatorname{loss} T N L^{(s)}(t)$, whilst for how to asses weather or not there exist $s m$ we recommend to see next Section (6.6.2). Putting aside for a moment the "significant margin", the computation of the $F L T(t)$ is as follows

$$
F L T(t)=\max (0, \mu(t))
$$

where

$$
\mu(t)=\left\langle T N L^{(s)}(t)\right\rangle
$$

where $\mu(t)$ is the mean with respect to the total net losses $T N L^{(s)}(t)$.

Whilst for the $F L T(t)$ there is an indication on how to compute it, for what concerns the second loss tranche $S L T(t)$, to the best of our knowledge, there is no jurisprudence. After having interviewed tens of practitioners, we believe that the most used method to compute the SLT - a measure of the Unexpected Loss - is the expected shortfal ${ }^{8}$ or "value at risk" (VaR). Thus the SLT is the mean of the total net losses $T N L^{(s)}(t)$, restricted to the values exceeding a certain $\alpha \%$ quantile, minus the first loss tranche $F L T(t)$ as

$$
S L T(t)=V a R_{\alpha}(t)-F L T(t)
$$

where

$$
V a R_{\alpha}(t)=\mu\left(T N L^{(s)}(t) \geq \hat{q}_{\alpha}\right)
$$

is the value at risk $V A R$ and

$$
\hat{q}_{\alpha}=F_{T N L}^{-1}(\alpha)
$$

is $T N L^{(s)}(t)$ cumulative distribution function at $\alpha \%$ quantile.

Finally, we define the $C L T(t)$ as the difference between the total inbound cash flows $I C F(t)$ and the other tranches as

$$
C L T(t)=I C F(t)-S L T(t)-F L T(t)
$$

Notice that the $C L T(t)$ covers extreme losses like the one that materializes in the theoretical scenario where all Exposures turn Non-Performing at $t=0$ and all $E^{(s)}(t)=0 \forall t$. In this theoretical Scenario, as Equation (35) shows, being the $A^{(s)}(t)=E^{(s)}(t)=0 \forall t$ then the total net loss is equal to the inbound cash flows $T N L(t)=I C F(t)$. The complementary loss tranche is[^5]normally the tranche that is covered by the very first Positions, like the costs and the "first" note Positions (see next Sec. 7 for further details).

In any Structuring Method, for the sake of transparency, consistency, and cross-comparability, it should become customary to define always the FLT, the $S L T$, and the $C L T$ (together the Tranches). Indeed, these 3 categories exist in any Structuring Method since they are necessary to compute the regulatory capital (see Sec. 7.2 and Sec. 11.3). Considering that each Position (with $P \geq 2$ ) may absorb less or more than one of the abovementioned 3 Tranches, the arranger must be transparent in indicating what percentage of each Tranche each Position absorbs.

### 6.6.2 FLT substantial margin

In the previous Sec. 6.6.1 we explained that the CRR links the FLT computation to the concept of a "significant margin" sm, without mathematically defining it. To the best of our knowledge, there is no conclusive evidence on how the Supervisory Authorities apply this concept, and yet it is a core aspect in computing regulatory capital (see Sec. 11.3). When the CRR entered into force in 2013, practitioners computed the FLT on the cumulative PDF of the total net loss $T N L$ at the Positions' maximum duration $T P$

$$
T F L T=\left\langle\sum_{t=0}^{T P} T N L^{(s)}(t)\right\rangle
$$

instead of on an ongoing basis as currently required by the Reg 2402, that entered into force in 2017. Thus, we propose a solution in implementing the "significant margin" of the 2013's CRR that takes into account the ongoing nature of the FLT defined by Reg 2402. Indeed, the following ratio

$$
s m=\frac{\sum_{t=0}^{T P} F L T(t)}{T F L T}-1
$$

is $\geq 0$ when $F L T(t)$ is defined as equation (36), and $T F L T$ is defined as equation (42). A criterion to understand if the margin is "significant" could be to check that it covers more than a standard deviation of the total first loss tranche (i.e. $s m \geq \sigma_{T F L T} / T F L T$ ). By definition, our $F L T$ of equation (36) already has a "significant margin" embedded within its formulation versus the methodology applied back in 2013 when this concept was introduced. This is also why in the previous Sec. 6.6.1 we ignore the $s m$ parameter.

## 7 Step 5: Select the number of Positions

As further explained in this Section, the total inbound cash flows $\operatorname{ICF}(t)$ are allocated to one macro building-block called "Position", composed of 2 regulatory building-blocks called "Cost" and "Note" Positions and 1 "ephemeral"
called "Embedded" Position. The 5th Step of any Structuring Method is to select the number of $X$ Cost Positions and the number of $Y$ Note Positions. This Section is divided in 4 parts: in Sec. 7.1 we define the concept of Position from a regulatory perspective; in Sec. 7.2 we define the concept of Position "Quality"; in Sec. 7.3 we define the concept of Embedded Positions; and in Sec. 7.4 we explain how to compute the number of Positions.

### 7.1 Position definition

Reg 2402 does not define the concept of positions, instead its Article 2(19) only defines the concept of securitization position as "an exposure to a securitization". In the whole Reg 2402, the concept of position is used equivalently and indistinctly to securitization positions, thus we use the same hermeneutic interpretation of equating position with securitization position.

European Regulation No. 2401/2017 (Reg 2401), Article 242(6) defines senior securitization position as a Position "backed or secured by a first claim on the whole of the underlying exposures", disregarding for these purposes amounts due under interest rate or currency derivative contracts, fees or other similar payments, and irrespective of any difference in maturity with one or more other senior tranches with which that position shares losses on a pro-rata basis. The previous Article 242(6) points out something that is often overseen: "fees or other similar payments" has to be disregarded when assessing if a Position is "senior" or not. Indeed, in current Structuring Methods, servicing fees are often the ones with the utmost priority in the payments versus the most senior Note Positions. Thus, in the first place, if the servicing fees were not actually considered Positions by Reg 2401, then Article 242(6) would have not needed to carve them out from the "senior position" definition. It follows that Reg 2401 considers servicing fees a Position (Cost Position) not differently than the notes (Note Position). Indeed, since servicing fees receive a fraction of the total inbound cash flows $\operatorname{ICF}(t)$, they must be considered absorbing as well a fraction of credit risk (i.e. if the whole portfolio were to default at time $t=0$, then also the servicing fees would not be paid accordingly to the Base Scenario).

On the other hand, Reg 2401, Article 242(6), defines a mezzanine securitization position as a "position [...] which is subordinated to the senior [...] and more senior than the first loss tranche". Finally, neither Reg 2401 nor Reg 2402 defines the concept of junior securitization position but generally refers to the First Loss Tranche. Then, we can assume that a Position is "junior" if it absorbs the First Loss Tranche $F L T(t)$. Consequently, we can assume that a Position is "mezzanine" if it absorbs the Second Loss Tranche $S L T(t)$ and "senior" if it absorbs the Complementary Loss Tranche $C L T(t)$.

Notice that some practitioners do not consider the Costs as Positions because they net the total inbound cash flows of the various expenditures toward the servicers and agents before redistributing the cash flows to the

Notes Positions. This practice goes against many International Financial Reporting Standards (IFRS) principles described into the (IASB, 2018), in particular the one that requires to "separately reporting the components of financial statements". This principle emphasizes the importance of presenting revenues, expenses, and cash flows separately in financial statements rather than netting them together. It ensures transparency and provides users of financial statements with a clear understanding of an entity's financial performance and financial position. Therefore, the investment memorandum shall always respect the same IFRS principles and thus clearly shows the Cost Positions in at least 2 different forms: (i) the $x$-th Net Dimensioned Cost Positions $N C_{x}^{(s)}(t)$ as defined in Equation (10.5); and (ii) the ratio of $N C_{x}^{(s)}(t)$ to the total inbound cash flows $\operatorname{ICF}(t)$. These 2 Features should be reported not only as their average value, but also as their empirical (i.e. from the simulated scenarios) ongoing probability density function, because in certain Scenarios the cost of recovery $C R^{(s)}(t)$ of defaulted Exposures might be so relevant to impact both the mezzanine and the senior Positions, especially in Negative Event Exposures. Thus, it is crucial to not only consider the Costs as Positions, but to compute all the above Features to enable the investors to make an informed judgement on the real intrinsic riskiness of the Notes they are purchasing.

### 7.2 Position Qualities

Why is it important to define if a Position is "senior", "mezzanine", or "junior"? From a Structuring Method perspective, these regulatory definitions are mathematically irrelevant. Indeed, if at any time the Regulator were to decide to abolish these concepts, the securitization modelling would not be impacted. Therefore, the "seniority" is not an intrinsic element of any securitization, but more like a quality that a Position obtains depending on multiple factors. Assigning the right quality to a Position is not just an aesthetic quirk: in fact, to compute the Regulatory Capital (RC) we need to assess, for each Position, the relative risk weights (RWs) applicable to a slice or to the Position as a whole. Indeed, as it can be seen in the table of Reg 2401 Article 259(1), the regulator has assigned different RWs to senior or non-senior Positions and thus assigning the right quality has direct implications on the RC computation. In conclusion, the quality is not an embedded characteristic that each Position has by default, but depends on its Designing (i.e. defining the relative "location" of the X Cost relative to the Y Notes Positions, see next Sec. 8) and its Dimensioning (i.e. assigning a "value" to the Positions, see next Sec. 9) whose effect is only relevant when computing the RC. Given the same Dimensioning, a diverse Designing would assign to each Position a different quality.

See the next Sec. 11.3 for a deep-dive on Regulatory Capital: for now, just remember that for the purpose of this paper, to each Position, in part or
as a whole, is assigned over time one (or more!) of the following 3 Qualities:

- Senior: if a Position slice absorbs a \% of $C L T(t)$;
- Mezzanine: if a Position slice absorbs a \% of $S L T(t)$;
- Junior: if a Position slice absorbs a \% of $F L T(t)$.

since, as it will be further explained in the next Sec. 8, each Position might absorb different tranches of the risk depending on their Designing. Therefore a Position might not receive the "quality" of Senior, Mezzanine or Junior as a whole, but each different "slice" absorbing a tranche of the FLT, SLT or CLT should receive the consequent "quality".

Now, our statement about the Qualities might seem to contradict the previous Article 242(6) of Reg 2401, where it is clearly stated that a Cost Position cannot be considered Senior, whilst with our definition a Cost Position could get the quality of Senior if it were absorbing a slice of the complementary loss tranche $C L T(t)$. This contradiction will be resolved in the next Sec. 11.3 indeed, the Regulator removed Cost Positions ex-ante from the computation of $R C$, whilst instead of making Cost Positions lose their Qualities ex-ante, in the PEAL Method we assign to the Cost Positions a risk weight $R W=0$ ex-post as shown in Equation (74). In fact, as we will show in the next Sec. 8.1, our Structuring Method allows to design "vertical" Cost and Note Positions, and thus it becomes crucial to provide the securitization stakeholders with a transparent picture of which part of which Position has which Quality, irrespectively if a Position bears or not regulatory capital $(R C)$. Indeed, Qualities are currently used to intuitively understand the liability-side payment priorities of the Positions but, since our approach allows for "Vertical" Positions that can even be Senior, Mezzanine and Junior at the same time, the direct link between Qualities and payment priorities breaks. Thus, in general, Qualities should not be used as a proxy for the payment priorities, but only to calculate the Regulatory Capital.

### 7.3 Embedded Positions

Let a Position be "Embedded" if it is equal to zero for any $t$ in the Base Scenario: $E P^{(b)}(t)=0 \forall t$. Embedded Positions can be different from 0 only in some Scenario $s: E P^{(s)}(t) \geq 0$. Embedded Positions are divided into two: (i) Super Senior (SSE) and (ii) Super Junior (SJE). We introduced the Embedded Positions because currently they are not properly described within the documents provided to the stakeholders. Therefore, the information about these variables is often overseen and it becomes incredibly complex for 3rd-parties to clearly understand their impact on their overall returns. Following the same principles of clarity and transparency described in the previous Sec. 7.1 , we believe that the introduction of the Embedded

Positions makes the risk assessment in the different Scenarios $s$ way simpler for all stakeholders.

### 7.3.1 Super Senior Embedded Positions

The Super Senior Embedded (SSE) are those Positions that have always the first claim on the total available funds $T A F^{(s)}(t)$, irrespectively from any possible Designing (see next Sec. 8). To date, we have identified only 3 types of SSE that are the following:

- EC: stands for Excessive Costs, which are all the una-tantum fines issued by any authority in case of infringement of one or more national or sovra-national laws (e.g. tax fines) plus the legal costs to defend from such accusations. It is Super Senior because any legal fees have always the utmost priority in any possible Designing;
- CR: stands for Cost of Recovery, that are the costs that the securitization pays on an ongoing basis to recover the defaulted Exposures. It is Super Senior because the agents that recovery the distressed credits shall be paid before anyone else;
- ER: stands for Excessive Recovery, which are the eventual excess cash flows that in each Scenario $s$ derives from the difference between an Exposure $(k, n)$ outstanding capital at the time of the default $O C_{k, n}^{(s)}\left(t^{d f}\right)$, plus the cumulative recovery $\operatorname{Cost} C R_{k, n}^{(s)}(t)$, and the recovered value at the time of recovery $R V_{k, n}^{(s)}\left(t^{t r}\right)$ as

$$
E R_{k, n}^{(s)}(t)=\max \left(0, R V_{k, n}^{(s)}\left(t^{t r}\right)-O C_{k, n}^{(s)}\left(t^{d f}\right)-\sum_{t=0}^{t^{t r}} C R_{k, n}^{(s)}(t)\right)
$$

It is Super Senior because the Excessive Recovery belongs to the respective Exposures from which they have derived and must be revert as soon as the excessive cash is made available to the securitization, without further ado.

Therefore, the Scenario $s$ Super Senior Embedded Position $S S E^{(s)}(t)$ is

$$
S S E^{(s)}(t)=E C^{(s)}(t)+\sum_{k=1}^{K} \sum_{n=1}^{N} C R_{k, n}^{(s)}(t)+E R_{k, n}^{(s)}(t)
$$

whilst the average Scenario Super Senior Embedded Position $\overline{S S E}(t)$ is

$$
\overline{S S E}(t)=\left\langle S S E^{(s)}(t)\right\rangle
$$

### 7.3.2 Super Junior Embedded Positions

The Super Junior Embedded (SJE) are those Positions that have always the last claim on the total available funds $T A F^{(s)}(t)$, irrespectively from any possible Designing (see next Sec. 8). To date, we have identified only 1 type of SJE that is:

- B: stands for Buffer, which are those excess cash flows that in each Scenario $s$ derive from the difference between $A^{(s)}(t)$ and $G A(t)$ as

$$
B^{(s)}(t)=\max \left(0, A^{(s)}(t)-G A(t)\right)
$$

The $B^{(s)}(t)$ can be caused by an excess of euribor or other factors that generate a negative losses. The Buffer is Super Junior because it is an excess cash used to absorb the first loss tranche $F L T(t)$, even before any $p$-th Position, and it is normally paid out pari-passu to the "lower-tier" Positions.

### 7.4 Compute the number of Positions

As detailed in the previous Sec. 7.1, there are of 2 types of Positions: those owned by the securitization servicers (Cost Positions) whose total number is described by the letter $X$, and those issued as notes and detained by bondholders (Note Positions) whose total number is described by the letter $Y$. Thus, the total number of Positions $P$ is

$$
P=X+Y
$$

Pursuant Reg 2402, a transaction is a securitization if and only if $P \geq 2$, of which one must be a Cost Position $X \geq 1$ and one a Note Position $Y \geq 1$. Indeed, securitization vehicles are empty shells and need servicers to operate them. Notice that, for the purpose of this paper, if there are 3 service providers paid pari-passu, we can sum their cash flows and consider them being one single Cost Position when computing the payment priority waterfall. The same reasoning shall be applied to the notes: if two or more Note Positions are completely "pari-passu", sharing the same risk and being paid with the same frequency, then they shall be deemed as one single Note Position, summing their cash flows.

## 8 Step 6: Positions' Designing to absorb the Tranches

Positions' Designing determines the way the inbound risk is distributed among the outbound Positions. This Section is divided in seven parts: in Sec. 8.1 we define the process to organize the Positions to design a Waterfall Configuration; in Sec. 8.2 we introduce the concept of Virtual Positions; in

Sec. 8.3 we introduce the concept of Horizontal Components; in Sec. 8.4 we introduce the concept of Vertical Components; in Sec. 8.5 we introduce the concept of Positions' Designing; in Sec. 8.6 we analize in detail the illustrative Design of Figure 1, and finally in Sec. 8.7 we explain why the current traditional Horizontal Position Designs are particular cases of our general PEAL Method.

### 8.1 Designing definition

We define the process of organizing the $X$ Cost and the $Y$ Note Positions so as to absorb all the Tranches as Designing, and its synoptic graphical representation as a Waterfall Configuration? The 6th Step of any Structuring Method is to Design the $P$ Positions into a Waterfall Configuration. The Designing process is made of 4 steps (see Figure 11):

1. Virtual Positions: define a superstructure that bridges the inbound and the outbound cash flows;
2. Horizontal Components: define a superstructure that horizontally subdivide, and mathematically links, each Virtual Position in smaller horizontal rectangles;
3. Vertical Components: define a superstructure that vertically subdivides, and mathematically links, each Horizontal Position in smaller rectangles;
4. Positions Design: define the equations that logically connect each $x$ Cost and the $y$ Note Position to their relative Vertical Components.

To date, there are 3 Waterfall Configurations: horizontal; vertical; and hybrid. In the Horizontal Waterfall, each Position absorbs the Tranching in horizontal slices: the $T A F^{(s)}(t)$ flows down from the top to the bottom Position following the Designing (i.e. the Position $a$ has higher payment priority than the Position $b$ if and only if $a<b$ ). In the Vertical Waterfall, each Position absorbs the Tranching in vertical slices: the $T A F^{(s)}(t)$ is allocated to the vertical Positions pro-rata basis. In the Hybrid Waterfall, each Position absorbs the Tranching in a hybrid combination of horizontal and vertical: the $T A F^{(s)}(t)$ is allocated to the Positions indirectly, through the Virtual Components.[^6]

![](https://cdn.mathpix.com/cropped/2024_04_26_fd6261e9e9862aafa107g-26.jpg?height=600&width=1020&top_left_y=431&top_left_x=518)

Figure 1: Synoptic representation of the 4 steps required to Designing the Positions. In Step 1 we compute the Virtual Positions. In Step 2 we decide the number of Horizontal Components and their $h \%$ weight to their relative Virtual Positions. In Step 3 we decide the number of Vertical Components and their $v \%$ weight to their relative Horizontal Components. Finally, in Step 4 we design the Waterfall Configuration by connecting each $x$ Cost and $y$ Note Position to their Vertical Components.

### 8.2 Virtual Positions

Let a Virtual Position $V P$ be a mathematical superstructure that bridges the inbound and the outbound cash flows. Let $N P$ be the number of Virtual Positions (see Step 1 in Figure 1). In this paper, the number of Virtual Positions is fixed at $N P=3$. Thus, let the system of equations that connect the Virtual Positions outbound cash flows to the inbound cash flows be

$$
\left\{\begin{array}{l}
V P_{1}(t)=C L T(t) \\
V P_{2}(t)=S L T(t) \\
V P_{3}(t)=F L T(t)
\end{array}\right.
$$

This choice was made to simplify the regulatory capital optimization and computation. Indeed, as explained in the previous Sec. 7.2, the First Loss Tranche, the Second Loss Tranche, and the Complementary Loss Tranche on the asset-side correspond to the Junior Quality, the Mezzanine Quality, and the Senior Quality on the liability-side. It follows that $V P_{1}=$ Senior Quality, $V P_{2}=$ Mezzanine Quality, and $V P_{3}=$ Junior Quality.

Being a Horizontal Waterfall type, Virtual Positions are useful because they have a robust mathematical link to the inbound cash flows and introduce a clear priority in the Positions' payments, enabling simpler computation in preparation of the next steps. We will use the Virtual Positions as a
pivotal element to compute the net cash flows to the Positions in the different Scenario $s$ in the following Sec. 10

### 8.3 Horizontal Components

Let a Horizontal Component $H C$ be a mathematical superstructure that horizontally subdivides, and mathematically links, the $n p$-th Virtual Position into horizontal rectangles (see Step 2 in Figure 11). Let the set of horizontal slices of the $N P$ Virtual Positions be $H S=\left\{H_{1}, H_{2}, \ldots H_{N P}\right\}$ and

$$
H=\sum_{n p=1}^{N P} H_{n p}
$$

be the number of total horizontal slices, where $H \geq N P$. Notice that the first Horizontal Component is always the average Super Senior Embedded Position (i.e. $H_{1}(t)=\overline{S S E}(t)$ ). Let $j$ be the index of the $j$-th slice (from top to bottom) and let $h_{j}(t)$ be the Horizontal Percentage with respect to its Virtual Position $V P$. As an example, let consider the Step 2 in the previous Figure 1 where: $N P=3, H S=\{3,1,1\}, H=5$. We can infer that $h_{1}(t), h_{2}(t)$ and $h_{3}(t)$ "slice" $V P_{1}, h_{4}(t)$ "slices" $V P_{2}$ and $h_{5}(t)$ "slices" $V P_{3}$. Obviously, we have that $h_{1}(t)+h_{2}(t)+h_{3}(t)=100 \%, h_{4}(t)=100 \%$, and $h_{5}(t)=100 \%$. Then, the equations that connect the Virtual Positions to the Horizontal Components are

$$
\left\{\begin{array}{l}
H C_{1}(t)=V P_{1}(t) \cdot h_{1}(t) \\
H C_{2}(t)=V P_{1}(t) \cdot h_{2}(t) \\
H C_{3}(t)=V P_{1}(t) \cdot h_{3}(t) \\
H C_{4}(t)=V P_{2}(t) \cdot h_{4}(t) \\
H C_{5}(t)=V P_{3}(t) \cdot h_{5}(t)
\end{array}\right.
$$

where $V P_{1}(t) \cdot h_{1}(t)=\overline{S S E}(t)$ in any Structuring Method.

### 8.4 Vertical Components

Let a Vertical Component $V C$ be a mathematical superstructure that vertically subdivides, and mathematically links, the $j$-th Horizontal Component in smaller rectangles (see Step 3 in Figure 1). Let the set of vertical slices of the $H$ Horizontal Components be $V S=\left\{V_{1}, V_{2}, \ldots V_{H}\right\}$ and

$$
V=\sum_{j=1}^{H} V_{j}
$$

be the number of total rectangles composing the securitization liability-side, where $V \geq H$. Notice that the first Vertical Component cannot be subdivided and it is always equal to the Super Senior Embedded Position (i.e. $\left.H_{1}(t)=V_{1}(t)=\overline{S S E}(t)\right)$.

Let $i$ be the index of the $i$-th slice (from top to bottom, from left to right) and let $v_{i}(t)$ be the Vertical Percentages utilized to subdivide the Horizontal Components into their Vertical Components. As an example, let consider the Step 3 in the previous Figure 1 where: $N P=3, H S=\{3,1,1\}$, $H=5, V S=\{1,1,2,2,2\}, V=8$. We can infer that: $v_{1}(t)$ "slices" $H C_{1}$, $v_{2}(t)$ "slices" $H C_{2}, v_{3}(t)$ and $v_{4}(t)$ "slice" $H C_{3}, v_{5}(t)$ and $v_{6}(t)$ "slice" $H C_{4}$, and $v_{7}(t)$ and $v_{8}(t)$ "slice" $H C_{5}$. It naturally follows that $v_{1}(t)=100 \%$, $v_{2}(t)=100 \%, v_{3}(t)+v_{4}(t)=100 \%, v_{5}(t)+v_{6}(t)=100 \%, v_{7}(t)+v_{8}(t)=$ $100 \%$. Then, the equations that connect the Horizontal Components to the Vertical Components are

$$
\left\{\begin{array}{l}
V C_{1}(t)=H C_{1}(t) \cdot v_{1}(t) \\
V C_{2}(t)=H C_{2}(t) \cdot v_{2}(t) \\
V C_{3}(t)=H C_{3}(t) \cdot v_{3}(t) \\
V C_{4}(t)=H C_{3}(t) \cdot v_{4}(t) \\
V C_{5}(t)=H C_{4}(t) \cdot v_{5}(t) \\
V C_{6}(t)=H C_{4}(t) \cdot v_{6}(t) \\
V C_{7}(t)=H C_{5}(t) \cdot v_{7}(t) \\
V C_{8}(t)=H C_{5}(t) \cdot v_{8}(t)
\end{array}\right.
$$

Notice that, while the order of the Horizontal Components provides some information on their payment priorities, the order of the Vertical Components do not. Any order is acceptable because it is the arranger that provide the system of equations to link each $j$-th Horizontal Component to the relative $i$-th Vertical Component.

### 8.5 Positions' Designing

Let the process to mathematically connect each $x$ Cost and $y$ Note Position to their relative $V_{i}$ Vertical Components be defined as Positions' Designing (see Step 4 in Figure 1). Following on the example described in the previous Sections, we can define the system of equations of Step 4 of the previous Figure 1 that connect the Vertical Components outbound cash flows to each $x$ Cost and $y$ Note Position outbound cash flows as

$$
\left\{\begin{array}{l}
C_{1}(t)=V C_{1}(t)+V C_{2}(t) \\
N_{1}(t)=V C_{3}(t) \\
N_{2}(t)=V C_{5}(t) \\
N_{3}(t)=V C_{7}(t) \\
N_{4}(t)=V C_{4}(t)+V C_{6}(t)+V C_{8}(t)
\end{array}\right.
$$

### 8.6 Illustrative example

We choose the specific example of a design (Figure 1) to illustrate the utilization of horizontal and vertical components in defining Note Positions. Moreover, the introduction of this type of design could have significant implications in the practice of securitization.

Reg 2402, article 6(3)(a) requires that certain actors shall retain on an ongoing basis a material net economic interest which, in any event, shall not be less than $5 \%$ of the nominal value of each of the Tranches sold or transferred to investors (i.e. a vertical slice of the $Y$ Note Positions). In addition, pursuant article 5(1)(c) of Reg 2402, institutional investors are required to verify that the mandatory retention is maintained on an ongoing basis by the relevant actors. Unfortunately, the operation to verify the continuous maintaining of the mandatory retention is currently extremely impervious, and often times, almost impossible due to operative constraints. Thus, the possibility to create a vertical Note - $N_{4}$ in step 4 of Figure 1- dimensioned to respect the said $5 \%$ mandatory retention, might solve all the current operative issues at once. If $N_{4}$ be hold by a third-party, then any investor could just request at any point in time the trustee to certify that the $N_{4}$ vertical Position be in the possession of the relevant actors. This alone might automatically fulfill Reg 2402 due diligence requirements.

Therefore, the usage of vertical Positions is not just a theoretical or aesthetic choice, but has profound regulatory implications. Indeed, just by creating such Position, it would be possible to minimize the due diligence operative complexity and costs for both the institutional investors and the supervisory authorities.

### 8.7 A particular Design of a general method

As explained in the previous Sec. 8.1, there are 3 type of Waterfall Configurations. Nowadays, the most used Waterfall Configurations pertains of $X=1$ Cost Position and $Y=3$ Note Positions. Such notes follow the same order of Figure 1 where $N_{4}$ does not exist and $C_{1}=H C_{1}+H C_{2}, N_{1}=H C 3$, $N_{2}=H C_{4}$, and $N_{3}=H C_{5}$. Thus, the current typical Horizontal Waterfall Configurations are just particular cases of the PEAL Method general framework, where the $p=1 \ldots P$ Positions are perfectly superimposable to the $i=1 \ldots V$ Vertical Components and to the $j=1 \ldots H$ Horizontal Components. The Designing of Sec. 8, the Gross Dimensioning of Sec. 9, and the Net Dimensioning of Sec. 10 processes remain the same.

## 9 Step 7: Dimension the Gross Cost \& Gross Notes

In this section we outline the process of gross dimensioning divided into seven steps. In Sec. 9.1 we define the process to dimension the Gross Cost
$G C$ and Gross Notes $G N$. In Sec. 9.2 we introduce the concept of payment frequencies, that are crucial in understanding payment waterfalls, and discuss how to avoid incongruities with the specific rules of Reg 2402. In Sec. 9.3 we introduce the frequency transformation function to adjust cash flow vectors into constant intervals. in Sec. 9.4 we dimension the Gross Vertical Component $G V$; in Sec. 9.5 we dimension the Gross Cost $G C$ and the Gross Note $G N$; in Sec. 9.6 we dimension the Gross Horizontal Component $G H$; and finally in Sec. 9.7 we provide a simple test to check if we are correctly applying the "horizontal rule" of Reg 2402.

### 9.1 Gross Dimensioning definition

We define the process to indirectly dimension the Gross Cost $G C(t)$ and the Gross Note $G N(t)$ following the system of equations described in the previous Designing phase, putting their monthly cash flows at their relevant payment frequency, as Gross Dimensioning. The 7th Step in any Structuring Method is to compute $G C(t)$ and $G N(t)$. The Gross Dimensioning process is divided in 5 steps:

1. Frequencies: select the Vertical Components' payment frequencies;
2. GV: compute the Vertical Component Gross Dimensioning;
3. GC \& GN: compute Costs' and Notes' Gross Dimensioning;
4. GH: compute the Horizontal Components' Gross Dimensioning;
5. g-check: compute the $g$ ratio to check for coherence with Reg 2402 .

### 9.2 Select the frequencies

In any Structuring Method, the frequencies are the "keystones" to understand the functioning of the payment waterfalls. In a pure mathematical modelling perspective, any Vertical Component could have its own payment frequency $f(V C)$, without considering its relation with the others and without any regulatory restriction. In practice, there are some constraints that shall be respected in selecting the payment frequencies. Reg 2402 article 2(1)(b), requires that the distribution of losses on the ongoing life of the transaction be dependent on the subordination of the Tranches. In order to respect such prescription, the payment frequency must follow 3 rules:

- vertical: the "higher" Horizontal Components must have an higher payment frequency than the "lower" Horizontal Components (i.e. $f\left(H C_{1}\right) \geq$ $\left.f\left(H C_{2}\right) \geq \cdots \geq f\left(H C_{H}\right)\right)$
- multiple: the "lower" Horizontal Components must have a frequency that is a multiple of the "highest" Horizontal Component (i.e. $f\left(H C_{i}\right) \equiv$ $0\left(\bmod f\left(H C_{i+1}\right)\right)$;
- horizontal: the Vertical Components that belong to the same Horizontal Component must have the same frequency (i.e. $f\left(V C_{a}\right)=$ $f\left(V C_{b}\right)$ if $\left\{V C_{a}, V C_{b}\right\} \in H C$.

If we relax even just one of the above rules, some of the Features of the next Sec. 11 will show signs of incongruities. For example if we relax the "vertical rule" and we pay a "lower-tier" Horizontal Component (e.g. the $j$-th $\left.H C_{j} \in F L T\right)$ with a higher frequency than the "higher-tier" Horizontal Component (e.g. the $j$-th $H C_{j} \in C L T$ ), then in case of stressed scenarios the "higher-tier" might be less protected than the "lower-tier", and thus bear more losses than what it would have done otherwise, contradicting the Reg 2402 prescriptions. If we relax the "horizontal rule" and pay two Vertical Components that are virtually "pari-passu" with two different frequencies, we are making the part that is paid with a higher frequency less risky than the other on an ongoing basis, thus contradicting the Reg 2402. Finally, even if we respect both the "vertical" and "horizontal" rules, if we relax the "multiple" rule, then in certain periods we might be providing protection to a "lower-tier" Horizontal Component whose cash flows should have been used in the next periods to protect the "higher-tiers" from negative events, contradicting Reg 2402.

As we will further explain, we will use the Coefficient of Variation Adjusted CVA, described in the next Sec. 11, to detect breaches of Reg 2402 requirements: indeed, if any Horizontal Component line were to intersect during the ongoing life of the transaction it would mean that at that time a "lower-tier" Horizontal Component was less risky than a "higher-tier" Horizontal Component, contradicting Reg 2402 requirements.

### 9.3 Frequency transformation function

Since typically payments to the Positions have a lower frequency than the payments on the asset side, we need a function to transform the monthly inbound cash flows to the Position respective outbound cash flows frequencies. Let $c f(t)$ be the monthly cash flow vector to be transformed to a frequency $\omega_{c f}$ paid each $\tau_{c f}=12 / \omega_{c f}$ months. Then the transformation

$$
\mathbb{F}\left(c f(t), \omega_{c f}\right)= \begin{cases}\sum_{t^{\prime}=t-\tau_{c f}+1}^{t} c f\left(t^{\prime}\right) & \text { if } t=i \cdot \tau_{c f} \text { with } i \in \mathbb{N} \\ 0 & \text { otherwise }\end{cases}
$$

### 9.4 Compute GV

Let $G V_{i}(t)$ be the Gross Dimensioning of the $i$-th Vertical Component as

$$
G V_{i}(t)=\mathbb{F}\left(V C_{i}(t), \omega_{V C_{i}}\right)
$$

where $i=1 \ldots V, \mathbb{F}$ is defined as Equation (52) and $\omega_{V C_{i}}$ is the frequency of the outbound cash flows of the $i$-th Vertical Component $V C_{i}(t)$.

### 9.5 Compute GC \& GN

Let $G C_{x}(t)$ be the Gross Dimensioning of the $x$-th Cost Position as the sum of its Gross Dimensioned Vertical Components. Let $G N_{y}(t)$ be the Gross Dimensioning of the $y$-th Note Position as the sum of its Gross Dimensioned Vertical Components. Therefore, if we consider the $x$ Cost and $y$ Note Positions of the example of Sec. 8.5, the result is

$$
\left\{\begin{array}{l}
G C_{1}(t)=G V_{1}(t)+G V_{2}(t) \\
G N_{1}(t)=G V_{3}(t) \\
G N_{2}(t)=G V_{5}(t) \\
G N_{3}(t)=G V_{7}(t) \\
G N_{4}(t)=G V_{4}(t)+G V_{6}(t)+G V_{8}(t)
\end{array}\right.
$$

where $G V_{i}(t)$ is function (53).

### 9.6 Compute GH

Let $G H_{j}(t)$ be the Gross Dimensioning of the $j$-th Horizontal Component as the sum of its Gross Dimensioned Vertical Components. Thus, if we consider the $H$ Horizontal Components of the example of Sec. 8.4, the result is

$$
\left\{\begin{array}{l}
G H_{1}(t)=G V_{1}(t) \\
G H_{2}(t)=G V_{2}(t) \\
G H_{3}(t)=G V_{3}(t)+G V_{4}(t) \\
G H_{4}(t)=G V_{5}(t)+G V_{6}(t) \\
G H_{5}(t)=G V_{7}(t)+G V_{8}(t)
\end{array}\right.
$$

where $G V_{i}(t)$ is function $(53)$.

### 9.7 Horizontal rule g-check

Let $g_{i}(t)$ be the ratio of the $i$-th Gross Vertical to the $j$-th Gross Horizontal Component

$$
g_{i}(t)=\frac{G V_{i}(t)}{G H_{j}(t)}
$$

with $G V_{i}(t) \in G H_{j}(t)$ as described in each system of equations that will be used in the relative Structuring Method, as shown in the example of the previous Sec. 9.6. The $g$-check is a simple mechanism through which we immediately know if the payment frequencies we chose are respecting the 3 frequency rules explained in the previous Sec. 9.2. This test states that if
the $i$-th gross ratio $g_{i}(t)$ of a certain Gross Vertical Component $G V_{i}(t)$ to its $j$-th Gross Horizontal Component $G H_{j}(t)$ is equivalent to the $v_{i}(t)$ percentage used to transform the monthly $j$-th Horizontal Component $H C_{j}(t)$ into its monthly $i$-th Vertical Component $V C_{i}(t)$ (i.e. $\left.g_{i}(t)=v_{i}(t) \forall t\right)$ then the selected payment frequencies are respecting the "horizontal rule" of Reg 2402 prescriptions. Otherwise, if $g_{i}(t) \neq v_{i}(t)$ for any $t$ then it means that one or more Gross Vertical Components belonging to the same Horizontal Component do not have the same frequency. Therefore, although they shall be "pari-passu", they are partially not, thus breaching Reg 2402 .

## 10 Step 8: Dimension the Net Costs \& Net Notes

This Section is divided in six parts: in Sec. 10.1 we define the process to dimension the Net Cost $N C$ and Net Notes $N N$; in Sec. 10.2 we introduce the Gross Dimensioning Matrix $G D M$; in Sec. 10.3 we introduce the waterfall payment function $f w p$ used to compute the Net Dimensioning Matrix $N D M$; in Sec. 10.4 we dimension the Net Vertical Component $N V$; in Sec. 10.5 we dimension the Net Cost $N C$ and the Net Notes $N N$; and in Sec. 10.6 we compute the Cost Losses $L C$ and the Note Losses $L N$.

### 10.1 Net Dimensioning Definition

In a Scenario $s$, we define the indirect process to dimension the Net Cost $N C^{(s)}(t)$ and the Net Notes $N N^{(s)}(t)$ by computing the Net Dimensioning Matrix $N D M^{(s)}(t)$, allocating the total available funds $T A F^{(s)}(t)$ on the Gross Dimensioning Matrix $G D M(t)$ using the Waterfall Payment Function $f w p$, as Net Dimensioning. The 8th Step of any Structuring Method is to compute the Net Dimensioning of the Cost $N C^{(s)}(t)$ and the Note $N N^{(s)}(t)$ Positions. The Net Dimensioning process is divided in 5 steps:

1. GDM: define the Gross Dimensioning Matrix;
2. NDM: compute the Net Dimensioning Matrix;
3. NV: compute the Vertical Components Net Dimensioning;
4. NC \& NN: compute the Cost and Note Net Dimensioning;
5. $\mathbf{L C} \& \mathbf{L N}$ : compute the Cost and Note Losses.

### 10.2 Gross Dimensioning Matrix

Let the Gross Dimensioning Matrix $G D M(t)$ be the matrix whose columns follow the $G H_{j}(t)$ as $G D M(t)=\left[G H_{1}(t), G H_{2}(t), \ldots, G H_{H}(t)\right]$, where $j=1 \ldots H$. Notice that, the GDM is a pure Horizontal Configuration: as it will be shown in the next Sec. 10.3 , the Waterfall Payment Function $f w p$
allocates, on an ongoing basis, the total available funds $T A F^{(s)}(t)$ from left to right: thus, the first column on the left is the first Position to have a claim on the total available funds, the second column has the second claim and so forth until the last column $H$ whom has the last claim on any residual liquidity. Therefore, in order to perfectly match the Horizontal Components Designing described in the selected Waterfall Configuration, the Super Senior Embedded Position $S S E$ must always be the first column because it has anyway the first claim on any available funds. Then, the following columns, should be the other Gross Dimensioned Horizontal Components in an ascending order: indeed, we know that $G H_{1}(t)$ has always an higher claim than $G H_{2}(t)$ that has an higher claim on $G H_{3}(t)$ and so forth to $G H_{H}(t)$.

### 10.3 Net Dimensioning Matrix

Let the Waterfall Payment Function be the function that, in a Scenario $s$, allocates the inbound total available funds $T A F^{(s)}(t)$ on the Gross Dimensioning Matrix $G D M(t)$ to respect their loss allocation Designing and their Gross Dimensioning, thus computing the Positions' Net Horizontal Dimensioning $N H^{(s)}(t)$ synthesized into the Net Dimensioning Matrix $N D M^{(s)}(t)$. The Waterfall Payment Function is a system of recursive equations that loops from the top left to the bottom right of the GDM. The loop system is not obvious, and thus we decided to sub-divide it into 3 sequential steps:

1. Step 1: compute the total gross position $T G P(t)$;
2. Step 2: compute the total net position $T N P^{(s)}(t)$;
3. Step 3: compute the Net Dimensioning Matrix $N D M^{(s)}(t)$.

In synthesis, in any Scenario $s$, we first compute the total net position $T N P^{(s)}(t)$, allocating the total available funds $T A F^{(s)}(t)$ (plus eventual residual cash flows from previous periods) on the total gross position $T G P(t)$ (plus eventual debts from previous periods). Then, we compute the Net Dimensioning Matrix $N D M^{(s)}(t)$ by allocating the total net position $T N P^{(s)}(t)$ payments to each Horizontal Component according to its payment priorities.

### 10.3.1 Step 1: compute the total gross position

Let the sum of the $j=1 \ldots H$ Gross Dimensioned Horizontal Component $G H_{j}(t)$ be the total gross position $T G P(t)$ as

$$
T G P(t)=\sum_{j=1}^{H} G H_{j}(t)=\sum_{j=1}^{H} G D M_{j}(t)
$$

### 10.3.2 Step 2: compute the total net position

In any Scenario $s$, in each period $t$, let the allocation of the inbound total available funds $T A F^{(s)}(t)$ to the total gross position $T G P(t)$ be

$$
\left\{\begin{array}{l}
P A F^{(s)}(t)=T A F^{(s)}(t)+A D V^{(s)}(t-1) \\
T A D^{(s)}(t)=T G P(t)+D B T^{(s)}(t-1) \cdot h(\cdot) \\
A D V^{(s)}(t)=\max \left(P A F^{(s)}(t)-T A D^{(s)}(t), 0\right) \\
D B T^{(s)}(t)=\max \left(T A D^{(s)}(t)-P A F^{(s)}(t), 0\right) \cdot h(\cdot)+D B T^{(s)}(t-1) \cdot(1-h(\cdot))
\end{array}\right.
$$

that is a set of recursive Equations where $h(\cdot)$ is $h(T G P(t))$ and represents an indicator of when payments occur: in fact, $h(\cdot)$ is 1 if and only if any outbound payment to any Position is due at a given period $t$ as follow

$$
h(x)= \begin{cases}0 & \text { if } x \leq 0 \\ 1 & \text { if } x>0\end{cases}
$$

Notice that in a generic Scenario $s$ the periodical total available funds $P A F^{(s)}(t)$ can be in general larger than the total available funds $T A F^{(s)}(t)$, since there can be cash advances from the previous period. A simple example is when the Positions are paid starting from the second period: in this case, introducing a dummy variable $A D V^{(s)}(t)$ accounting for the total cash advances, $P A F^{(s)}(2)=T A F^{(s)}(2)+A D V^{(s)}(1)$. On the same footing, we have to introduce a dummy variable $D B T^{(s)}(t)$ accounting for the fact that, if in a payment period $t=1$ there is not enough cash to pay for the total gross position $T G P(1)$, then in the following payment period $t=2$ we consider what is due to the positions is $T G P(2)$ plus what was not paid at $t=1$. Thus, we indicate with $T A D^{(s)}(t)$ the total amount due to all the Positions. We have explicitly considered that if at period $t$ there is a payment, then the difference $P A F^{(s)}(t)-T A D^{(s)}(t)$ between available and due can either increase $A D V^{(s)}(t)$ or $D B T^{(s)}(t)$ according to the sign. Notice that it is also necessary to specify the initial value of the dummy variables; the natural choice is $A D V^{(s)}(0)=0, D B T^{(s)}(0)=0 . \mathrm{NB}$ : $T A D^{(s)}(t)$ is different from zero only at the payment periods. Finally, let the minimum between the periodical total available funds $P A F^{(s)}(t)$ and the total amount due to all the Positions $T A D^{(s)}(t)$ be

$$
T N P^{(s)}(t)=\min \left(P A F^{(s)}(t), T A D^{(s)}(t)\right)
$$

where the total net position $T N P^{(s)}(t)$ takes into account the maximum amount of periodical inbound cash flows that can be allocated to all the $H$ Positions at any given period $t$. Notice that $\sum_{t=0}^{T P} T N P^{(s)}(t)=\sum_{t=0}^{T P} T A F^{(s)}(t)$.

### 10.3.3 Step 3: compute the net dimensioning matrix

In any Scenario $s$, in each period $t$, let the Net Dimensioning Matrix $N D M^{(s)}(t)$ be the matrix whose columns are composed of the $j=1 \ldots H$ Net Dimensioned Horizontal Components $\mathrm{NH}_{j}(t)$, computed using the following system of recursive equations

$$
\left\{\begin{array}{l}
N D M_{j}^{(s)}(t)=\min \left(G D M_{j}(t)+D B T_{j}^{(s)}(t-1), R N P_{j-1}^{(s)}(t)\right) \\
D B T_{j}^{(s)}(t)=\min \left(0, G D M_{j}(t)-N D M_{j}^{(s)}(t)\right) \cdot h(\cdot)+D B T_{j}^{(s)}(t-1) \cdot(1-h(\cdot)) \\
R N P_{j}^{(s)}(t)=R N P_{j-1}^{(s)}(t)-N D M_{j}^{(s)}(t)
\end{array}\right.
$$

where, for compactness, we indicate $h\left(T G P_{j}(t)\right)$ as $h(\cdot)$. The expression for $N D M_{j}^{(s)}(t)$ in Equation (59) ensures that any $j$-th Horizontal Component cannot receive more than their respective $T G P_{j}(t)$ plus any eventual debt $D B T_{j}^{(s)}(t-1)$ of the previous period, and at most the cash amount $R N P_{j-1}^{(s)}(t)$ residual after paying the Horizontal Component $j-1$. The expression for $D B T_{j}^{(s)}(t)$ accounts for the eventual debt from the previous period and for the difference between the due amount $G D M_{j}(t)$ and the net amount that has really been paid net of any $\operatorname{loss} N D M_{j}^{(s)}(t)$.

We recall that $h\left(G D M_{j}(t)\right)$ indicates whether any payment to the $j$ th Horizontal Component is occurring at period $t . R N P_{j}^{(s)}(t)$ accounts for the fact that the residual cash for $j$-th Horizontal Component equals the difference between the residual cash for the Horizontal Component $j-1$ and what has been paid to that Horizontal Component. Also in this case it is necessary to specify the initial values of the dummy variables $R N P_{j=0}^{(s)}(t)=$ $T N P^{(s)}(t)$ and $D B T_{j}^{(s)}(0)=0$. Notice that $\sum_{j=1}^{H} N D M_{j}^{(s)}(t)=T N P^{(s)}(t)$.

### 10.4 Vertical Components Net Dimensioning

Let the product of $j$-th Net Dimensioned Horizontal Components $N D M_{j}(t)$ per their respective gross ratio $g_{i}$ be the Vertical Components Net Dimensioning $N V_{i}^{(s)}(t)$

$$
N V_{i}^{(s)}(t)=N D M_{j}^{(s)}(t) \cdot g_{i}
$$

where $g_{i}$ is Equation (54). So, given the example in Sec. 8.4 the result is

$$
\left\{\begin{array}{l}
N V_{1}^{(s)}(t)=N D M_{1}^{(s)}(t) \cdot g_{1}(t) \\
N V_{2}^{(s)}(t)=N D M_{2}^{(s)}(t) \cdot g_{2}(t) \\
N V_{3}^{(s)}(t)=N D M_{3}^{(s)}(t) \cdot g_{3}(t) \\
N V_{4}^{(s)}(t)=N D M_{3}^{(s)}(t) \cdot g_{4}(t) \\
N V_{5}^{(s)}(t)=N D M_{4}^{(s)}(t) \cdot g_{5}(t) \\
N V_{6}^{(s)}(t)=N D M_{4}^{(s)}(t) \cdot g_{6}(t) \\
N V_{7}^{(s)}(t)=N D M_{5}^{(s)}(t) \cdot g_{7}(t) \\
N V_{8}^{(s)}(t)=N D M_{5}^{(s)}(t) \cdot g_{8}(t)
\end{array}\right.
$$

### 10.5 Cost \& Note Net Dimensioning

Let $N C_{x}^{(s)}(t)$ be the Net Dimensioning of the $x$-th Cost Position as the sum of its Net Dimensioned Vertical Components. Let $N N_{y}^{(s)}(t)$ be the Net Dimensioning of the $y$-th Note Position as the sum of its Net Dimensioned Vertical Components. Therefore, if we consider the $x$ Cost and $y$ Note Positions of the example of Sec. 8.5, the result is

$$
\left\{\begin{array}{l}
N C_{1}^{(s)}(t)=N V_{1}^{(s)}(t)+N V_{2}^{(s)}(t) \\
N N_{1}^{(s)}(t)=N V_{3}^{(s)}(t) \\
N N_{2}^{(s)}(t)=N V_{5}^{(s)}(t) \\
N N_{3}^{(s)}(t)=N V_{7}^{(s)}(t) \\
N N_{4}^{(s)}(t)=N V_{4}^{(s)}(t)+N V_{6}^{(s)}(t)+N V_{8}^{(s)}(t)
\end{array}\right.
$$

where $N V_{i}^{(s)}(t)$ is function (60).

### 10.6 Cost \& Note Losses

Let $L C_{x}^{(s)}(t)$ be the Loss of the $x$-th Cost Position as the difference between the Gross Dimensioned Cost Position $G C_{x}^{(s)}(t)$ and the Net Dimensioned Cost Position $N C_{x}^{(s)}(t)$ as

$$
L C_{x}^{(s)}(t)=G C_{x}^{(s)}(t)-N C_{x}^{(s)}(t)
$$

Let $L N_{y}^{(s)}(t)$ be the Loss of the $y$-th Note Position as the difference between the Gross Dimensioned Note Position $G N_{y}^{(s)}(t)$ and the Net Dimensioned Note Position $N N_{y}^{(s)}(t)$ as

$$
L N_{y}^{(s)}(t)=G N_{y}^{(s)}(t)-N N_{y}^{(s)}(t)
$$

Notice that both the Cost and Note Losses amounts and probability density functions are information often not shared with the stakeholders, although
many institutional investors would appreciate to have access to these forecasting to hedge their Positions from excessive risk. Therefore, as with the other securitization Features computed in the next Sec. 11, these key performance indicators shall always be computed and made available to the interested third parties for the ongoing life of the securitization.

## 11 Step 9: Compute the relevant Features

As introduced in Sec. 10.6, there are a number of securitization key performance indicators that the servicers should always provide to the investors on an ongoing basis (Features) to enable better and more transparent risk assessments. The 9th Step of any Structuring Method is to compute, in every Scenario $s$, all the relevant Features. The following is a non-exhaustive list of some of the main Features that we strongly believe the servicers should always provide to the stakeholders on an ongoing basis:

- $E P:$ the $N$ Exposures Performance (Sec. 11.1);
- $T H$ : the Positions' Thickness (Sec. 11.2);
- $R C$ : the Regulatory Capital (Sec. 11.3);
- $C V A$ : the Coefficient of Variation Adjusted (Sec. 11.4);
- $F V$ : the Fair Value (Sec. 11.5);
- $g r$ : the gross internal rate of return (Sec. 11.6).

Inferring the Features statistics by Monte Carlo simulations allows for a better understanding of the real securitization ongoing intrinsic riskiness. It becomes easier to make all those advanced analyses that note-holders may need to demonstrate to their supervisory authorities that they have done proper risk due diligence during the purchasing and, afterwards, in the ongoing management process. Indeed, the PEAL Method increases the transparency that, in turn, might attract new investors and revive the securitization industry that, since 2008, has shown little sign of resilience. In fact, the European Corporate Loan niche alone lost more than $50 \%$ of new issuance between 2008 and 2017 (Kraemer-Eis, 2018) and has never recovered since.

### 11.1 Exposure Performance (EP)

Let the Exposure Performance $E P_{k, n}^{(s)}$ be the function that describes the "performance" of each Exposure $(k, n)$ in any Scenario $s$ assigning a Mutually Exclusive and Commonly Exhaustive "state". The 4 possible states are: \{FullPerforming, Performing, Non-Performing, Super-Performing $\}$. The $(K, N)$

Exposure Performance is the 1-st Feature that shall be provided to the securitization stakeholders on an ongoing basis.

When applying the IAS-IFRS accounting principles, Exposures mainly exist in 3 "states": (i) performing; (ii) unlikely-to-pay (UTP); and (iii) nonperforming (NPE). This typification does not provide any information on the real performance of the underlying Exposures in the different Scenarios $S$ versus the Base Scenario. For the purpose of standardization, we propose that the definition of performing and non-performing be shifted from the current IAS-IFRS accounting principles to the Exposures Performance EP, using the following Mutually Exclusive and Commonly Exhaustive function

$$
E P_{k, n}^{(s)}=\sum_{t=0}^{T P} \frac{\left[R_{k, n}^{(s)}(t)-R_{k, n}^{(b)}(t)\right]+E_{k, n}^{(s)}(t)-\left[C R_{k, n}^{(s)}(t)+E R_{k, n}^{(s)}(t)\right]}{\left(1+\eta_{t}\right)^{t}}
$$

where $R_{k, n}^{(s)}(t)$ is Equation (20); $R_{k, n}^{(b)}(t)$ is Equation (18); $E_{k, n}^{(s)}(t)$ is Equation (27); $C R_{k, n}^{(s)}(t)$ and $E R_{k, n}^{(s)}(t)$ are components of Equation 45); and finally $\eta$ is the annual expected inflation rate (e.g. $\eta=2 \%$ ) while $\eta_{t}$ is the monthly inflation rate (e.g. $\eta / 12$ ). Although some Events per se might be inherently negative (e.g. Exposure defaults) or positive (e.g. Exposure return to life), when more than one Event jointly affects the Exposure at different times $\hat{t}_{k, n}^{(\lambda)}$ in a specific Scenario $s$, it becomes extremely difficult ex-ante to define if the overall ex-post outcome. Considering that every Event materializes at a certain time $\hat{t}_{k, n}^{(\lambda)}$, where $0 \leq \hat{t}_{k, n}^{(\lambda)} \leq T_{k, n}$ (i.e. $\hat{t}_{k, n}^{\left(\lambda_{1}\right)}, \hat{t}_{k, n}^{\left(\lambda_{2}\right)}, \ldots$ ), then

$$
\hat{t}_{k, n}^{(s)}=\min \left(\hat{t}_{k, n}^{\left(\lambda_{1}\right)}, \hat{t}_{k, n}^{\left(\lambda_{2}\right)}, \ldots\right)
$$

is the first time when any Event affects the Exposure $(k, n)$ in Scenario $s$. In a Scenario $s$ let an Exposure $(k, n)$ be Performing in the range $r=$ $\hat{\tau}_{k} \leq t \leq \hat{t}_{k, n}^{(s)}$ : indeed Equation (63) is always 0 because when an Exposure is Performing it means that its paying exactly as expected in the Base Scenario and thus $E(t)=C R(t)=E R(t)=0 \forall t \in r$ and $R^{(b)}(t)-R^{(s)}(t)=$ $0 \forall t \in r$. In a Scenario $s$ let an Exposure $(k, n)$ be Full-Performing if $\hat{t}_{k, n}^{(s)}=T P$. In a Scenario $s$ let an Exposure $(k, n)$ be Non-Performing when $t \geq \hat{t}_{k, n}^{(s)}$ if $O P<0$. Finally, in a Scenario $s$ let an Exposure $(k, n)$ be Super-Performing when $t \geq \hat{t}_{k, n}^{(s)}$ if $O P>0$. Notice that, even Exposures that are natively $U T P$ or $N P L$ under the IAS-IFRS, in the PEAL Method can still be considered Fully-Performing, Performing or Super-Performing in the different Scenarios $s$ if they follow the rules of Equation (63).

The novel approach of this Section typifies the Exposures to provide concrete and timely information to stakeholders. Indeed, it is not irrelevant to make advanced risk analyses to properly communicate overtime the mean, the median, and the estimated likelihood of the number of Exposures that, in the various relevant Scenario $S$, are expected to be Full-Performing, Performing, Non-Performing, or Super-Performing.

### 11.2 Position Thickness (TH)

In this Section we will explain the regulatory definition of the $p$-th Position Thickness $T H_{p}(t)$, and then provide a simplified definition within the PEAL Method that is substantially equal, although formally different, as the ones of the European Regulations. The Position Thickness is the 2-nd Feature that shall be provided to the securitization stakeholders on an ongoing basis.

### 11.2.1 The Thickness regulatory definition

Reg 2401, Article 263(5), defines the $p$-th Position thickness percentage as

$$
T H P_{p}(t)=D P_{p}(t)-A P_{p}(t)
$$

where $p=1 \ldots P$ and where, pursuant Article 256 of Reg 2401, $D P_{p}(t)$ is the detachment point of Position $p$; and $A P_{p}(t)$ is the attachment point of Position $p$. Reg 2401 implicitly assumes that the $p=1 \ldots P$ Positions be perfectly superimposable at the $j=1 \ldots H$ Horizontal Components, and thus that any Design the arranger could come up with would have no Vertical Positions. Such an hidden assumption not only is extremely strong, but we have already debunked it in the example of the previous Figure 1. Therefore, it becomes mandatory to provide an alternative solution to the computation of the Positions' Thickness as the one proposed in the next Sec. 11.2.2

Reg 2401, Article 256(1), defines the attachment point of the $p$-th Position $A P_{p}(t)$ as "the threshold at which losses within the pool of underlying exposures would start to be allocated to the relevant securitization position. The attachment point shall be expressed as a decimal value between zero and one and shall be equal to the greater of zero and the ratio of the outstanding balance of the pool of underlying exposures in the securitization minus the outstanding balance of all tranches that rank senior or pari-passu to the tranche containing the relevant securitization position including the exposure itself to the outstanding balance of all the underlying exposures in the securitization". Then

$$
A P_{p}(t)=\frac{O B P(t)-\sum_{i=1}^{p} O B_{i}(t)}{O B P(t)}=\frac{\sum_{i=p+1}^{P} O B_{i}(t)}{O B P(t)}
$$

is the attachment point, where

$$
O B P(t)=\sum_{p=1}^{P} O B_{p}(t)
$$

is the total outstanding balance, and where

$$
O B_{p}(t)=\sum_{t=0}^{T P} G D M_{p}(t)-\sum_{\tau=0}^{t} G D M_{p}(\tau)=\sum_{\tau=t+1}^{T P} G D M_{p}(\tau)
$$

is the outstanding balance of the each $p$-th Position. Remember that $A P(t)_{p} \in$ $\{0,1\}$. Notice that $G D M_{p}(t)$ represents the $p$-th column of the Gross Dimensioning Matrix as explained in the previous Sec. 10.2 and that this formula works if and only if the $p=1 \ldots P$ Positions are perfectly superimposable to their Horizontal Components (i.e. the Waterfall Configuration is composed of only horizontal slices). In the moment that the Positions were vertical or had other shapes, the Regulatory approach would fail and the PEAL Method general equation would be required (see next Sec. 11.2.2).

On the other hand, Reg 2401, Article 256(2), defines the detachment point of the $p$-th Position $D P_{p}(t)$ as the "threshold at which losses within the pool of underlying exposures would result in a complete loss of principal for the tranche containing the relevant securitization position. The detachment point shall be expressed as a decimal value between zero and one and shall be equal to the greater of zero and the ratio of the outstanding balance of the pool of underlying exposures in the securitization minus the outstanding balance of all tranches that rank senior to the tranche containing the relevant securitization position to the outstanding balance of all the underlying exposures in the securitization". The most relevant aspect to stress about the above Article is that it defines the detachment point as "the loss [...] would result in a complete loss of principal [...] for the relevant securitization position". Indeed, as it happens in all financial products, the losses are firstly absorbed by the interest and only then by the capital. It follows that, in order to have a "complete loss of the principal", the relevant $p$-th Position must have absorbed a loss whose amount is the sum of its Gross Dimensioned interest and capital, represented by $G D M_{p}(t)$. It might seem strange that we stress this out, but even if this fact is lapalissian, there have been situations in which the arrangers have calculated the $p$-th Position detachment point using only the outstanding capital. This is particularly relevant when calculating the Regulatory Capital of those Positions absorbing the First Loss Tranche $F L T(t)$, for which purposely neglecting to consider the interests considerably diminishes the overall computation (see next Sec. 11.3). We want to point out that this blatantly incorrect practice provides a false representation of the Positions' intrinsic riskiness to the detriment of unaware investors. Then

$$
D P_{p}(t)= \begin{cases}1 & \text { if } p=1 \\ \frac{O B P(t)-\sum_{j=1}^{p-1} O B_{j}(t)}{O B P(t)}=A P_{p-1}(t) & \text { if } p>1\end{cases}
$$

is the detachment point of the $p$-th Position. Remember that $D P_{p}(t) \in$ $\{0,1\}$. Notice that each $D P_{p}(t)$ is obviously the $A P_{p}(t)$ of Position $(p-1)$ and the Position $p=1$ can fully default only in case of a $100 \%$ default of the whole portfolio at $t=0$. Finally, in order to obtain the $p$-th Position Thickness total amount, we multiply $T H P_{p}(t)$ per the total outstanding
balance $O B P(t)$ as

$$
T H_{p}(t)=O B P(t) \cdot T H P_{p}(t)
$$

### 11.2.2 The PEAL Method Thickness definition

The Thickness computational method defined in the EU Regulation has a fatal flow: it only works in Design with horizontal Positions. As we have shown in the previous Sec. 8, the Positions' Designing can have also vertical Positions: therefore, it becomes mandatory to develop a more general approach in computing the Position Thickness that could be used in any Designing, irrespectively by its complexity. Since, to compute other Features like the Regulatory Capital of Equation (74) we only need the $p$-th Position Thickness $T H_{p}(t)$, and since $T H P_{p}(t)=\overrightarrow{O B}_{p}(t) / O B P(t)$, then

$$
T H_{p}(t)=O B_{p}(t)
$$

Thus, the Thickness of the $x$-th Cost Position is

$$
T H C_{x}(t)=O B_{x}(t)=\sum_{t=0}^{T P} G C_{x}(t)-\sum_{\tau=0}^{t} G C_{x}(\tau)=\sum_{\tau=t+1}^{T P} G C_{x}(\tau)
$$

and the Thickness of the $y$-th Note Position is

$$
T H N_{y}(t)=O B_{y}(t)=\sum_{t=0}^{T P} G N_{y}(t)-\sum_{\tau=0}^{t} G N_{y}(\tau)=\sum_{\tau=t+1}^{T P} G N_{y}(\tau)
$$

and considering that we already have both the Gross Dimensioned Cost Position $G C_{x}(t)$ and the Gross Dimensioned Note Position $G N_{y}(t)$, we can compute their respective Thickness $T H C_{x}(t)$ and $T H N_{y}(t)$ without the need of their respective attachment points $A P_{p}(t)$ and detachment points $D P_{p}(t)$, simplifying the whole computation and model complexity, yet respecting the spirit of the European Regulations.

### 11.3 Regulatory Capital (RC)

The Regulatory Capital (RC), or capital requirement, is the amount of capital a bank or other financial institutions must hold in relation to the riskiness of their assets as required by their financial regulators. Therefore, as explained in the previous Sec. 7.2 , the $\mathrm{RC}$ is mathematically irrelevant to define a Structuring Method, and it is only an external requirement of some type of investors. In fact, if a Position were held by an investor that is not required to compute the $\mathrm{RC}$, this mere fact would not impact the securitization intrinsic characteristics. For this reason we explicitly said that the seniority is just a "quality" $q$ that each Position obtains depending on its

Designing and Gross Dimensioning, whose effect is only relevant when computing the Regulatory Capital. Indeed, given the same number of Positions $P$ and the same Gross Dimensioning, a diverse Designing would assign to each Position a different quality $q$.

Notice that the slice of $p$-th Position absorbing the Complementary Loss Tranche $C L T(t)$ gets the quality of Senior $(q=$ Senior or $q=S N)$. The slice absorbing the Second Loss Tranche $S L T(t)$ gets the quality of Mezzanine ( $q=$ Mezzanine or $q=M Z$ ) and the slice absorbing the First Loss Tranche $F L T(t)$ gets the quality of Junior $(q=J$ unior or $q=J R$ ). The Regulatory Capital of the $x$-th Cost and $y$-th Note Position is the 3-rd Feature that shall be provided to the securitization stakeholders on an ongoing basis.

As we explained in the previous Sec. 7, nowadays the Risk Weight of the Cost Position is zero $R W^{(C)}=0$ thus $R W C=0$. Therefore, for the purpose of this Section, we will compute the Regulatory Capital only on the $Y$ Note Positions $R C N_{y}(t)$. The general equation to compute the Regulatory Capital of the $y$-th Note Position is

$$
R C N_{y}(t)=\sum_{q} R C N_{(y, q)}(t)=R C N_{(y, S N)}(t)+R C N_{(y, M Z)}(t)+R C N_{(y, J R)}(t)
$$

where $y=1 \ldots Y$. The Note Position Regulatory Capital $R C N_{(y, q)}(t)$ for the quality $q$ is obtained by multiplying the risk-weighted asset $R W A_{i}$ of the $i$-th Gross Dimensioned Vertical Component $G V_{i}(t)$ that belongs to the $y$-th Note Position that absorbs the relative $q$ Tranche (see exemplified system of equations in Sec. 9.5), by the its capital adequacy ratio (CAR, see CRR, Article 92) as

$$
R C N_{(y, q)}(t)=\sum_{i} R W A_{(i, q)}(t) \cdot C A R=\sum_{i}\left(O B_{i}(t) \cdot R W_{(i, q)}\right) \cdot C A R
$$

where $O B_{i}(t)$ is Equation (73). Notice that Reg 2401 goes into great detail in explaining how to compute the different $R W_{(i, q)}$ as a function of the relative Thickness and other parameters. We will not deep dive into such aspects, but we will postpone its detailing to a next paper. Therefore, if we consider the example in Sec. 9.5 , the $y$-th Note Position Regulatory Capital $R C N_{y}(t)$ can be computed with the following system of equations

$$
\left\{\begin{array}{l}
R C N_{1}(t)=O B_{3}(t) \cdot R W_{(3, S N)} \cdot C A R \\
R C N_{2}(t)=O B_{5}(t) \cdot R W_{(5, M Z)} \cdot C A R \\
R C N_{3}(t)=O B_{7}(t) \cdot R W_{(7, J R)} \cdot C A R \\
R C N_{4}(t)=\left[O B_{4}(t) \cdot R W_{(4, S N)}+O B_{6}(t) \cdot R W_{(6, M Z)}+O B_{8}(t) \cdot R W_{(8, J R)}\right] \cdot C A R
\end{array}\right.
$$

where $O B_{i}(t)$ and $R W A_{(i, q)}(t)$ are components of the function (73).

### 11.4 Coefficient of Variation Adjusted (CVA)

Let the $x$ Cost Coefficient of Variation Adjusted $C V A C_{x}(t)$ be ratio between the Gross Dimensioned Cost Position $G C_{x}(t)$ minus the expected deviation of the Net Dimensioned Cost Position $N C_{x}^{(s)}(t)$ and the $x$-th Cost Position's total Thickness $T H_{x}$ and as

$$
C V A C_{x}(t)=\frac{G C_{x}(t)-\left\langle N C_{x}^{(s)}(t)\right\rangle}{T H_{x}}
$$

Let the $y$ Note Coefficient of Variation Adjusted $C V A N_{y}(t)$ be ratio between the Gross Dimensioned Note Position $G N_{y}(t)$ minus the expected deviation of the Net Dimensioned Note Position $N N_{y}^{(s)}(t)$ and the $y$-th Note Position's total Thickness $T H_{y}$ and as

$$
C V A N_{y}(t)=\frac{G N_{y}(t)-\left\langle N N_{y}^{(s)}(t)\right\rangle}{T H_{y}}
$$

The Coefficient of Variation Adjusted is the 3-rd Feature that shall be provided to the securitization stakeholders on an ongoing basis. Notice that the CVA $(t)$ of the $p$-th Positions absorbing the Complementary Loss Tranche $C L T(t)$ shall be systemically lower than those of the others, especially of the Positions absorbing the First Loss Tranche $F L T(t)$. If we have correctly applied all the PEAL Method requirements, then we know that a Structuring Method is not compliant with Reg 2402 if, by plotting all the Cost and Note CVA on the same graph, at any time $t$ the lines intersect. Indeed, if they do intersect it means that in $t$ a "higher-tier" Position is absorbing more risk than a "lower-tier" Position, resulting in a breach of Reg 2402 article 2(1)(b) provisions. The securitizations that do not respect this principle should not be allowed to be structured. In general, it is possible to avoid this kind of situation by having the Positions absorbing the FLT paid bullet at $T P$. With this little shrewdness, the arranger is always sure that any Structuring Method respect at least the spirit of Reg 2402.

### 11.5 Fair Value (FV)

The Fair Value $F V$ is the estimated price at which an asset, in our case the $y$-th Note Position, is bought or sold when both the buyer and seller freely agree on a price. The most accepted methodology to calculate an asset fair value is the so called "discounted cash flow" or "DCF", where we actualize with a certain discount factor $d$ the future asset free cash flows $F C F$ to a certain date $\tau=t$.

$$
D C F(t)=\sum_{\tau=t}^{T} \frac{F C F(\tau)}{\left(1+d_{\tau}\right)^{\tau}}
$$

In the PEAL Method we compute the $D C F(t)$ on a set of representative Scenarios $S$ deriving a probability density function $D C F^{(s)}(t)$, and we compute the Fair Value as

$$
F V Y_{y}(t)=\left\langle F V Y_{y}^{(s)}(t)\right\rangle
$$

that is the expected value of the $S$ Scenarios' value where

$$
F V Y_{y}^{(s)}(t)=\sum_{\tau=t}^{T} \frac{N N_{y}^{(s)}(\tau)}{\left(1+\eta_{\tau}\right)^{\tau}}
$$

where $N N_{y}^{(s)}(\tau)=F C F(\tau)$ because the Ned Dimensioned Note Position is already "net" of each Scenario $s$ losses; the discount factor $d=\eta$ as the annual expected inflation rate (e.g. $\eta=2 \%$ ) because if we were to discount the $F C F(t)$ for an higher rating the computation of the expected loss would lead to a double jeopardy; and $d_{\tau}=\eta_{\tau}$ as the monthly inflation rate (e.g. $\left.\eta_{\tau}=\eta / 12\right)$. The Fair Value is the 4-th Feature that shall be provided to the securitization stakeholders on an ongoing basis. For each $y$-th Note Position in any Scenario $s$, the Fair Value is the 4 -th Feature that shall be provided to the securitization stakeholders on an ongoing basis.

The Fair Value $F V Y_{y}(t)$ corresponds to the price that investors of a neutral and liquid market, with perfect information, would pay to buy the $Y$ Notes. It is a very useful synthetic measure that the servicers must always provide to the sellers, especially because it gives them an instrument to evaluate the fairness of a price. In fact, imputing the price offered by the buyer into the Fair Value's empirical cumulative distribution function, it is possible to derive the specific quantile to whom that price corresponds to: if the quantile is too far away from the average, it is an indication to the seller that, unless has a valid motive to do otherwise, shall avoid to sell rashly and wait for prices that are more aligned with the intrinsic riskiness of the Note Position. We believe that, in a rational market, the more information like this one is provided to the investors, the more the market is going to become liquid and efficient; to such an aim, the securitization servicers should provide this kind of information to the investors with high frequency and granularity.

### 11.6 Internal Rate of Return (IRR)

Investors use a synthetic metric call the "internal rate of return" irr to compute the annual rate of growth that an investment is expected to generate. Often this metric is used to compare different investments with similar standard deviation, and therefore is especially relevant as a "rule-of-thumb" measure. The following is the general equation

$$
\operatorname{irr}: \sum_{t=0}^{T P} \frac{E C F(t)}{(1+i r r)^{t}}=C_{0}
$$

where $E C F(t)$ represents the expected asset cash flows, $C_{0}$ represents the price paid at time $t=0$ to buy the asset, and $T P$ represent the fact that the investors are willing to buy the $(K, N)$ Exposures cash flows up to the Note Position maximum duration. The Internal Rate of Return irr is the 5 -th Feature that shall be provided to the securitization stakeholders on an ongoing basis. Let girr $_{y}$ be the gross irr of the $y$-th Note Position as

$$
\operatorname{girr}_{y}: \sum_{t=0}^{T P} \frac{G N_{y}(t)}{\left(1+\text { girr }_{y}\right)^{t}}=C Y_{(0, y)}
$$

where $E C F(t)$ is substituted by the $y$-th Gross Dimensioned Note Position $G N_{y}(t)$, and where $C Y_{(0, y)}$ represents the initial capital paid by the investors at time $t=0$ to buy the $y$-th Note Position. Let nirr $y$ be the net irr of the $y$-th Note Position as

$$
n i r r_{y}: \sum_{t=0}^{T P} \frac{N N_{y}(t)}{\left(1+n i r r_{y}\right)^{t}}=C Y_{(0, y)}
$$

where the asset expected cash flows $E C F(t)$ are substituted by the $y$-th Net Dimensioned Note Position cash flows $N N_{y}(t)$, and where $C Y_{(0, y)}$ represents the initial capital paid by the investors at $t=0$ to buy the $y$-th Note Position. Notice that $C Y_{(0, y)}$ is

$$
C Y_{(0, y)}=c p y_{y} \cdot C Y_{0}
$$

where $c p y_{y}$ is a percentage of the total price that the investors would pay to buy all the $Y$ Note Positions at once $C Y_{0}$, with $\sum_{y} c p y_{y}=100 \%$. Then

$$
C Y_{0}=\min \left(C_{0}, F V Y_{y}(0)\right)
$$

is the minimum between the initial $N$ Exposures total capital $C_{0}$ and the total Note Position Fair Value where the mean of the previous Equation (79) is substitute by the $\sum_{y} F V Y_{y}^{(s)}(t)$. In general terms, $C Y_{0}=F V Y(0)$ oftentimes when the Exposures are composed by Negative Event Exposures, in which the expected cash flows $E C F(t)$ are on average lower then the initial capital $C_{0}$, and thus the portfolio is sold at discount.

By considering the previous Equation (84), we can infer that the number $Y$ of Note Positions do have a great relevance in computing the various internal rate of return. Indeed, if $Y=1$ then $C Y_{(0,1)}=C Y_{0}$ and thus there is only "one" potential girr and nirr. When $Y=2$, then $C Y_{(0,1)}=c p y_{1} \cdot C Y_{0}$ and $C Y_{(0,2)}=\left(1-c p y_{1}\right) \cdot C Y_{0}$, generating an infinity of girr and nirr solutions in correspondence with the segment $C Y_{(0,1)}+C Y_{(0,2)}=C Y_{0}$, $C Y_{(0,1)}, C Y_{(0,2)} \geq 0$. When $Y>2$, then the infinities of girr and nirr solutions correspond to the intersection of the $\sum_{y} C Y_{(0, y)}=C Y_{0}$ plane with the positive orthant $C Y_{(0, y)} \geq 0$. It follows that, whilst the PEAL Method can determine the optimal Gross and Net cash flows to the $x$-th Cost and
$y$-th Note Position, it does not determine the girr and the nirr. Indeed, the $C Y_{(t, y)}$ definition is not an intrinsic characteristic of any securitization, but rather a decision that is totally market-driven, a choice done to meet the risk appetites of different investors. As $Y \geq 2$, the number of potential girr and nirr solutions becomes infinite. Therefore, it becomes imperative to explore reasonable constraints to narrow down these solutions to a manageable subset. This is especially crucial in alignment with the spirit of securitization regulations, which are primarily aimed at safeguarding investors and enhancing transparency. Investigating such constraints is essential to uphold investor protection and promote market integrity.

## 12 Step 10: Optimize the Structuring Method

The 10th Step of any Structuring Method is to optimize the Features of Step 9, by changing the $X$ Cost and $Y$ Note Positions Designing of Step 6 and Gross Dimensioning of Step 7 or by adding the optimization inbound building-block $z(t)$. Currently, Equation (49) has been set to be sure that the $X$ Cost and $Y$ Note Positions Designing of Step 6 and Gross Dimensioning of Step 7 are optimized for the Regulatory Capital calculation. In the end, there is no right or wrong optimization, since all depends on the arranger or the investors' needs. The only vinculum is to always pay attention to the Features' results respect, on an ongoing basis, the Reg 2402 provisions.

## 13 Next steps

The exploration of various opportunities for future investigation offers valuable insights into the complex landscape of securitization practices.

One such avenue involves standardising the modeling of the 11 different Types of Exposures outlined in steps 1 to 4, utilizing foundational equations provided in Sec. 1. This systematic analysis would allow both to shed light on the Features and risk management considerations associated with each Type, thereby informing decision-making processes and enhancing risk assessment practices within securitization transactions, and to produce standardised "templates" for new securitizations.

Another area that needs to be assessed is the evaluation of the impact of Euribor changes on Note Positions risk/return profiles: an accurate modelling of the Euribor dynamics is needed to understand whether resulting excess losses exceed excess interest paid to investors. Furthermore, investigating the potential significance of using excess returns to mitigate losses on "higher-tier" Positions could provide valuable insights into effective risk management strategies within securitization structures.

Future research endeavors could also delve into alternative approaches to compute the optimization inbound building-block $z(t)$. By exploring differ-
ent methodologies, we can deepen our understanding of optimization techniques and potentially uncover more efficient processes.

Another avenue for further investigation might be the exploration of various Position Designs and their respective Waterfall Configurations. Diving into different designs and configurations promises to enrich our understanding of the securitization process and its implications for risk management and feature computation.

Additionally, future research should explore the possibility of designing Waterfall Configurations that eliminate the so-called "Junior" Note, thereby structuring risk-intensive securitizations that may otherwise be deemed unfeasible due to excessive regulatory capital costs.

Further exploration is needed to define optimal frequencies in different Waterfall Configurations. This involves assessing the impact of relaxing one or more of the "3-frequency" rules presented previously and evaluating how these relaxations may influence risk management strategies. By investigating alternative configurations, we can contribute to the development of more robust securitization practices.

Another area ripe for exploration revolves around incorporating advanced risk weight calculation methods into the regulatory capital computation. By understanding the relationship between risk weights and Position Thickness, we can improve the precision and reliability of risk weight calculations, thereby enhancing risk management practices.

Furthermore, the development of constraint optimization models tailored for irr computation in securitization processes is essential. These models should optimize $i r r$ while satisfying regulatory requirements, investor preferences, and other relevant constraints, to enhance decision-making processes.

Clustering different Structuring Methods based on the outcome of their Features offers another avenue for exploration. This approach provides stakeholders with valuable insights into anticipated ongoing securitization performance, fostering the creation of shared best practices to expedite the structuring process without compromising soundness.

Moreover, developing ongoing management Key Performance Indicators to compare historic expected, historic real, and forward-looking real expected Scenarios offers valuable insights into actual securitization performance. Extending the methodology to ongoing management enhances our ability to monitor and optimize securitization performance throughout its life cycle.

Finally, estimating the time of risk hedging for each Position is crucial. Determining the date from which the cash Advances absorb the position losses, thus making the Position virtually risk free, allows us to manage risk effectively and adjust regulatory capital requirements accordingly.

In conclusion, the areas identified in this paper present promising avenues for further exploration, deepening our understanding of securitization mechanisms and contribute to the development of more effective Structuring Methods, risk management strategies, enhancing regulatory supervision.

## 14 Conclusions

This paper introduces the PEAL Method, a comprehensive 10-step mathematical framework designed to facilitate the structuring of securitizations across various Designing, including those with vertical Positions. It offers a universal approach applicable to any combination of Type of Exposures and Waterfall Configurations, positioning existing securitization structures as specific cases within our general framework. Moreover, it encompasses a comprehensive analysis across all time periods.

Our framework meticulously models the distribution of Exposures inbound cash flows from assets to outbound cash flows across positions. By providing a structured approach, we clarify payment priorities and enhance transparency regarding ongoing risk characterization for both the asset and liability sides of securitizations.

Moreover, our structured methodology encourages the explicit delineation of all relevant hypotheses, formulas, models, and algorithms used in the structuring phase. By incorporating these details into legal documentation, practitioners can furnish investors and supervisory authorities with comprehensive information necessary for replication and evaluation. This enhancement mirrors the transparency and reproducibility standards of scientific papers, enabling stakeholders to scrutinize underlying assumptions and test hypotheses reflected in legal contracts. Ultimately, this approach promises to simplify comparisons among different securitizations, foster transparency, and facilitate regulatory supervision, thereby mitigating potential disputes among stakeholders.

To further bolster stakeholder risk assessment, we advocate for the provision of a minimum set of features to investors on an ongoing basis. These metrics empower investors to gauge the risk characterization of positions more accurately, leading to pricing convergence closer to fair values. Consequently, our framework promotes standardization and cross-comparability among diverse structuring methods, augmenting market transparency and potentially curbing structuring and due diligence costs over time.

However, caution is warranted when employing complex designs, as they may obscure underlying mathematical intricacies and potentially disadvantage investors if not properly communicated.

In summary, this foundation paper proposes a novel securitization framework, offering a comprehensive methodology to design, evaluate, and compare different securitizations over time. Our approach facilitates the clustering of structuring methods based on expected features, providing stakeholders with valuable insights into anticipated ongoing securitization performance. By fostering the creation of best practices and promoting regulatory compliance without compromising soundness, our framework aims to contribute to the evolution and improvement of securitization practices.

## References

Bluhm, C. and L. Overbeck (2006). Structured credit portfolio analysis, baskets and CDOs. CRC Press.

Bluhm, C., L. Overbeck, and C. Wagner (2010). Introduction to Credit Risk Modeling. Tailor \& Francis.

IASB (2018). Conceptual Framework for Financial Reporting. International Accounting Standards Board IASB.

Kraemer-Eis, H. (2018). SME securitisation in europe. European Investment Fund, 51-58.

Rockafellar, R. and S. Uryasev (2000). Optimization of conditional value-at risk. J. of Risk 3, 21-41.

Rockafellar, R. T. and J. O. Royset (2010). On buffered failure probability in design and optimization of structures. Reliability engineering 83 system safety 95(5), 499-510.

## A Description of the elements of any List of Events

This is a non-exhaustive list of the main Events by Type of Exposures:

| TE | LE | NE | EX |
| :---: | :---: | :---: | :---: |
| QP | pe, dh | 2 | tm, oi |
| QS | pe, dh, npd, jl | 4 | tm, oi |
| CL | pe, de, eu, trl | 4 | tm |
| EA | imp, fr, ts, sp | 4 | en |
| NE | fr, trl, rr, tr | 4 | tm |
| EE | npd, fr, ts, sp | 4 | tm, en |
| CC | de, fr, eu, trl | 4 | tm, oi |
| SL | pe, de, dh, eu, trl | 5 | tm |
| ML | pe, de, cd, eu, trl | 5 | tm |
| AL | pe, de, cd, eu, trl | 5 | tm |
| RE | npd, fr, cd, ts, sp, nr | 6 | tm, en |

Table 1: List of Events by Type. TE stands for Type of Exposures; LE stands for List of Events); NE is the Number of elements in the List of Events; EX stands for Extreme Events, that are so rare that, unless there is a compelling reason to use them, they shall never be included in the LE $\Lambda$.

Hereby, a brief description of each Event of the previous Table 1.

- cd: stands for Collateral Depreciation, describes the negative Event where the securitization collateral diminishes in value versus its time of structuring $\hat{\tau}_{k}$;
- de: stands for Default Event, describes the negative Event where a borrower does not repay their obligations, and it is assumed that does not come back to life;
- dh: stands for DeatH, describes the negative Event where the borrower dies;
- en: stands for Extreme Natures, describes Events that can impair the collaterals;
- eu: stands for EUribor, describes a hybrid Event;
- fr: stands for FRaud, describes the negative Event where there exists some kind of fraud (the collateral does not exist, the credit card has been stolen, etc);
- imp: stands for IMPairment, describes the negative Event where a perishable asset is no more available to be sold or does not exist anymore;
- jl: stands for Job Loss, describes the negative Event where an individual backing the Exposure loses their job, impairing the Exposure's capacity to repay its obligations;
- npd: stands for Not PaiD, describes some possible negative Events (e.g. not being paid by an employer, renter not paying, etc);
- nr: stands for Not Rented, describes a hybrid Event;
- oi: stands for Over-Indebtedness, describes the negative Event where a judge rules the debt inside the securitization be noncollectable in part or in whole;
- pe: stands for Prepayment Event, describes the negative Event where a borrower decides voluntarily to pay back the capital before its end $T_{k, n} ;$
- rr: stands for Recovery Rate, describes a hybrid Event;
- sp: stands for Selling Price, describes a hybrid Event;
- tm: stands for Moratorium Time, describes the negative Event where a State may lawfully impose to accept the postponement of installments by $t_{m}$ months;
- trl: stands for Return to Life Time, describes the positive Event where a Negative Event Exposure starts to repay its debt;
- tr: stands for Recovery Time, describes a hybrid Event;
- ts: stands for Selling Time, describes a hybrid Event.

Notice that a hybrid Event changes, in positive or negative, vs its Base Input value at $\hat{\tau}_{k}$ of structuring. The mathematical description of each one of the asset $A(t)$ and event recovery $E(t)$ equations should be defined in future research papers.


[^0]:    ${ }^{1}$ Unless otherwise defined all terms of this paper have the same meaning of Reg 2402.

    ${ }^{2}$ PEAL stands for (P)ositions, (E)vents recovery, (A)ssets, and (L)osses and represents the name of the macro building-blocks that are at the basis of the Securitization Theory.

[^1]:    ${ }^{3}$ Notice that a strict usage of a deterministic algorithm to describe payments' priority removes ambiguities on who must be paid first and avoids litigations.

[^2]:    ${ }^{4}$ The set $\mathcal{S}$ must be a representative statistical sample of all the possible Scenarios $S$.

[^3]:    ${ }^{5}$ Non-Spot: cash flows different from zero more than once in different time $t$.

[^4]:    ${ }^{6}$ Spot: cash flows different from zero just at one specific time $t$.

    ${ }^{7}$ Events: prepayments, defaults, return to life, and variation of the euribor

[^5]:    ${ }^{8}$ The "expected shortfall" is also known as "conditional value at risk" Rockafellar and Uryasev, 2000), or "super quantile" (Rockafellar and Royset, 2010).

[^6]:    ${ }^{9}$ In technical jargon, we refer to a "Waterfall" because the cash "flows down" from the "higher-tier" Position to the "lower-tiers" Positions, in a way for which the "highertier" Positions are paid before the others, following the Waterfall Configuration, and the "lowest-tier" Position is paid only if there is any cash flow left.

