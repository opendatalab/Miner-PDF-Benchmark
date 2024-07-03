# D2D Assisted Multi-Antenna Coded Caching

Hamidreza Bakhshzad Mahmoodi?, Jarkko Kaleva?, Seyed Pooya Shariatpanahi∗and Antti Tolli ¨
? ? Centre for Wireless Communications, University of Oulu, P.O. Box 4500, 90014, Finland
∗ School of Electrical and Computer Engineering, College of Engineering, University of Tehran, Iran, firstname.lastname@oulu.fi, p.shariatpanahi@ut.ac.ir Abstract**— device-to-device (D2D) aided multi-antenna coded**
caching scheme is proposed to improve the average delivery rate and reduce the downlink (DL) beamforming complexity. deviceto-device (D2D) aided multi-antenna coded caching scheme is proposed to improve the average delivery rate and reduce the downlink (DL) beamforming complexity.A Novel beamforming and resource allocation schemes are proposed where local data exchange among nearby users is exploited. The transmission is split into two phases: local D2D content exchange and DL
transmission. In the D2D phase, subsets of users are selected to share content with the adjacent users directly. In this regard, a low complexity D2D mode selection algorithm is proposed to find the appropriate set of users for the D2D phase with comparable performance to the optimal exhaustive search. During the DL
phase, the base station multicasts the remaining data requested by all the users. We identify scenarios and conditions where D2D transmission can reduce the delivery time. Furthermore, we demonstrate how adding the new D2D phase to the DLonly scenario can significantly reduce the beamformer design complexity in the DL phase. The results further highlight that by partly delivering requested data in the D2D phase, the transmission rate can be boosted due to more efficient use of resources during the subsequent DL phase. As a result, the overall content delivery performance is greatly enhanced, especially in the finite signal-to-noise (SNR) regime.

## I. Introduction

The daily surge in network traffic has pushed the network providers towards advanced data delivery methods to meet the client's demands. Luckily, a vast share of the network traffic is for multimedia content, such as video streams, which can be proactively cached before hands [1], [2]. Specifically, considering the upcoming data-intensive applications such as extended reality (XR), which rely heavily on asynchronous content reuse [3]–[5], proactive caching at the end-users could relieve network congestion during busy hours. The aim is to leverage off-peak hours to move some content closer to the end-users, which will be used to relieve the network's load during peak hours. Coded caching (CC) has been recently proposed by Maddah-Ali and Niesen in [6], which improves the traditional caching schemes [7] by benefiting from the aggregated memory throughout the network. As a result, an additional *global caching gain* is achieved on top of traditional local caching gain in the CC scheme.

The CC scheme was initially proposed for the error-free shared link framework (e.g., [6], [8], and [9]), but it was promptly extended to wireless setup [10]–[13]. In this regard, the setup in [6] is extended in [10] to a multiple server scenario, where the effects of the network structure on the CC performance are investigated. Motivated by the results in [10], the authors in [11] propose different multi-antenna CC transmission schemes for the physical layer. Furthermore, focusing on high signal-to-noise-ratio (SNR) region analysis, authors in [12], [13] show that CC boosts the wireless network performance in terms of Degrees-of-Freedom (DoF).

Specifically, the global coded caching gain offered by the CC
and the spatial multiplexing gain provided by a multi-antenna transmitter are additive in a wireless broadcast channel [14].

Moreover, the multiantenna CC is also highly beneficial with finite SNR as long as the interference is appropriately compensated [15]–[17]. Specifically, while [15] and [16] use a rate-splitting approach to simultaneously benefit from the global caching and the spatial multiplexing gains, a general beamformer design was proposed in [17] to improve the finiteSNR performance of the coded caching in wireless networks.

Despite significant CC benefits in wireless networks, several practical challenges have been identified in the literature [18]–
[28]. For instance, users' privacy requirements to prevent information leakage have been specified in [18]. In this regard, authors in [19] extend the idea in [18] to a D2D CC network, using non-perfect secret sharing and one-time pad keying techniques. The number of file division requirements in CC,
known as *subpacketization* problem, is considered in [20]–
[25]. While authors in [20] benefit from the linear block code
(LBC) technique to reduce the subpacketization, authors in
[21], [22] benefit from the number of antennas at the transmitter. In a similar work, the effect of the subpacketization on the achievable rate in the low-SNR region was also investigated in [23]. Finally, authors in [24], [25] propose the shared cache scheme to efficiently control the subpacketization requirement.

Another crucial issue in the CC wireless setting is *near-far* problem. Explicitly, in conventional CC delivery schemes, a common message is transmitted to several users. Thus, the rate is always limited by the user with the worst channel condition to ensure every user can decode the common message [17]. In this regard, the authors in [26] propose a congestion control to avoid serving users in a fading state, while the authors in [27]
propose to serve users when they are in favorable conditions via appropriate scheduling. Using a different approach, authors in [28] benefit from deep reinforcement learning (DRL) to jointly design caching and scheduling schemes, tackling the near-far problem. Unlike [27] and [26], which apply traditional XORing of data elements, authors in [29] and [3] allocate different rates to users with different channel conditions by altering the modulation scheme. Finally, one critical drawback of the traditional wireless CC delivery is the high complexity of the optimized beamforming solutions, which can render multiantenna CC infeasible for large networks [17].

The CC cache placement must be carefully designed so that every user has some data needed by others [6]. On the other hand, in many particular use cases, such as immersive viewing applications, groups of users are being served together [3]–[5].

In such scenarios, users can intermingle at close distances, making the device-to-device (D2D) communication quite alluring. Motivated by this, a two-phase transmission scheme is proposed in this paper, where the downlink (DL) multicasting of the file fragments in [17] is complemented by the direct D2D exchange of local cache contents.

## A. Related Works

D2D communication has been studied extensively in wireless scenarios for traditional caching methods, where an entire file is placed at the end-user (see for example [7], [30]–[32]).

The idea is that utilizing D2D communication results in less congested servers, improved network energy efficiency (EE), mitigated near-far problems, etc. On the other hand, currently, interest is increasing in machine learning (ML) tools such as deep deterministic policy gradient (DDPG) [33] as a means for various wireless resource allocation problems (e.g., [34]). In this regard, authors have considered applying ML in cacheaided data delivery, including D2D communications [35].

Specifically, ML tools can be utilized for cache placement or delivery schedules for cache-aided networks [35], including coded caching [28].

Interestingly, D2D ideas have been extended to the CC
wireless networks to improve network throughput [36]–[42].

An infrastructure-less CC network is considered in [36], where the D2D is the only transmission link. Moreover constructive achievable coding strategies and information-theoretic bounds are also specified in [36]. Later, the authors in [37]
characterized the optimal load-memory trade-off under the uncoded placement and one-shot delivery assumptions. Yet, the authors in [37] extend the system model in [36] such that robustness against random user inactivity is achieved via maximum distance separation (MDS) coding. Users with different available memories are considered in [38] to extend the scenario in [36] to a more practical one. On the other hand, the authors in [39] show that the frequency reuse gain and CC multicasting gain are additive when users move inside the D2D network. The authors in [40] extend [36] to a general framework by utilizing the placement delivery array (PDA),
alleviating the subpacketization problem.

Authors in [41] extend the network in [6] to the case where users can cooperate via D2D links. Therein, the D2D and DL transmissions are assumed to be carried out in parallel without interference. Thus, to minimize the total transmission time, the authors in [41] optimally divide the transmission load into D2D and DL parts. Unlike [36]–[41] with fixed rates assumption, the authors in [42] consider a multi-user singleinput-single-output (SISO) scenario where transmission rates are changed depending on channel conditions. In this regard, D2D transmissions are utilized along with the DL transmission to decrease the transmission time. Specifically, the BS decides whether to transmit a sub-file in DL or D2D fashion based on users' neighboring conditions. Furthermore, different amounts of memory are dedicated to the D2D and DL sub-files in [42]
to minimize the delivery time.

## 2 B. Main Contribution

Although CC-based D2D communication has been thoroughly investigated in the literature for single-antenna transceivers [36]–[42], a D2D framework supporting CCbased multi-antenna communication is still missing considering the current multi-antenna transmission support in the 5G standards [43]. In this regard, this paper extends the framework studied in the previous studies [36]–[42] to a multiantenna transmitter scenario, where we consider a single-cell multi-user multiple-input single-output (MISO) network. The proposed delivery scheme in this work comprises D2D links as a complementary transmission phase to the DL transmission.

The cache placement is based on [6]; thus, every user has some data that can be shared with other users. The goal is to minimize the total transmission time by delivering a part of the requested data via D2D transmissions while the rest is delivered by the base station (BS). To find the optimal combination of D2D and DL transmissions, we should be able to compare the available D2D and the DL rates. However, the optimal D2D/DL mode selection is a combinatorial problem, requiring an exhaustive search for D2D opportunities over a group of users. Hence, due to the NP-hard nature of the problem, the exhaustive search quickly becomes computationally intractable. On the other hand, to know the exact achievable DL rate, all the beamformers should be first designed for all possible combinations. As mentioned before, this is challenging due to the high computational complexity of multicast beamforming. Consequently, we propose an approximation for the DL achievable rate without computing the beamformers to resolve the beamforming complexity issue. Next, based on the approximated DL rate, we provide a low complexity mode selection algorithm, which allows efficient determination of D2D opportunities even for a large number of users.

The computational complexity of the proposed algorithm is significantly reduced compared to the exhaustive search with similar performance.

In infrastructure-less networks, as in [36], the geographical separation of users severely affects the total transmission time.

However, using the D2D transmission phase as a complementary phase for the DL transmission results in steadier behavior against geographical separation than in the DL-only case in [17] and the D2D-only case in [36]. In addition, it significantly shortens the delivery time. On the other hand, by allowing direct D2D exchange of file fragments, the interference management among a reduced number of downlink

List of Notations

W Library Zk Cache content

τ Global caching gain Wn,V Subfile n

dk Request index D(t) D2D set

RD(i) D2D receiver set XD2D

i D2D transmit signal

Pd User transmit power N0 Noise variance

hik D2D channel yk Received signal

zk Receiver noise X˜ S

T DL transmit message

wS

T DL beamformer hk DL channel

TD2D D2D delivery time TDL DL delivery time RU Symmetric rate PT BS transmit power

xDL DL transmit signal ID2D(D) D2D user set indicator

C(.) DL file size ΩS , ΩS,V Set of D2D user sets

ΩS Set of DL messages ΩS

k Needed message set

Ik Interference set NiS

, NiV DL message count

TABLE I

THE LIST OF MAIN NOTATIONS.

multicast streams becomes more efficient than in [17]. Finally, we thoroughly investigate the complexity reduction of the DL
beamformer due to the proposed complementary D2D phase.

This paper extends our earlier conference papers [44], [45] to a general D2D-aided multiantenna CC framework without any group size restrictions and also provides a more detailed analysis of beamforming complexity. Note that this work focuses on instantaneous channel knowledge for D2D/DL mode selection and does not consider any ML-based technique. The reason is that due to numerous practical challenges, satisfactory utilization of ML techniques for cache-aided networks is still missing. A thorough survey on ML utilization challenges for cache-aided networks (e.g., data integrity, dynamic environment, utilization of big data) can be found in [46].

## C. Organization And Notations

The rest of the paper is organized as follows. In Section II the system model is introduced. In Section III we illustrate the main elements of the proposed scheme via two examples.

Then, Section IV demonstrates the proposed scheme for the general case. Section V analyzes the complexity reduction of the DL beamforming due to the complementary D2D
phase. Section VI presents numerical results, and Section VII
concludes the paper.

Notations: Matrices and vectors are presented in boldface upper and lower case letters, respectively. The Hermitian of the matrix A is denoted as AH. Cardinality of a discrete set A
is given by |A|. Let C denote the set of complex numbers and k.k be the norm of a complex vector. Also, [m] denotes the set of integer numbers {1*, ..., m*}, and ⊕ represents addition in the corresponding finite field. Finally, Table I collects the main notations used in this paper.

## Ii. System Model

We consider a system consisting of a single L antenna BS
and K single antenna users. The BS has a library of N files, namely W = {W1*, . . . , W*N }, where each file has the size of F bits. The normalized cache size (memory) of each user is M files. Each user k stores a fragment of each file, denoted by Zk(W1*, . . . , W*N ) during the *cache placement* phase (cache placement is identical to [6]). Thus, for the case τ =
KM
N∈ N,



each file is divided into K
τ non-overlapping subfiles, i.e.,
Wn = {Wn,V : V ⊂ [K], |V| = τ}, ∀n ∈ [N]. Each user k stores all the subfiles V 3 k, i.e., Zk = {Wn,V | k ∈ V, V ⊂
[K], |V| = τ, ∀n ∈ [N]}. During the *content delivery phase*,
user k ∈ [K] makes a request for the file Wdk
, dk ∈ [N].

We envision a scenario where a group of users is being served simultaneously. These users are free to move inside the coverage area, and at specific times, they request some content from the server. The immersive viewing application illustrated in [3], and [4] can be considered a specific use case. Thus, it is very likely to have some nearby users at each time instance who can share some content among themselves via D2D transmissions. Accordingly, the delivery phase starts with the D2D sub-phase, divided into a number of D2D time slots. In each time slot t, a group of nearby users, denoted by set D(t),
are instructed by the BS to locally exchange data. Furthermore, each D2D time slot is divided into |D(t)| orthogonal D2D
transmissions (see Fig. 1). In each D2D transmission, a user i ∈ D(t) transmits a coded message denoted by XD2D
ito an intended set of receivers RD(i) ⊆ D(t). Thus, the message XD2D
ican be transmitted at rate1

$$R_{i}^{\mathcal{D}}=\min_{k\in\mathcal{R}^{\mathcal{D}}(i)}\log\left(1+\frac{P_{d}|h_{i k}|^{2}}{N_{0}}\right),\tag{1}$$

where Pd is the user's available transmit power, and hik ∈ C
is the channel coefficient between user i and user k. Note that in each D2D transmission, a single user in D multicasts a message to the rest of the group members. Hence, the weakest receiver limits the rate. Furthermore, following [36], each subfile is transmitted in a D2D group *|D|−*1 times. Therefore, 1In this paper, we assume all D2D user groups D(t) are served using time-division multiplexing. Further improvement can be achieved by allowing parallel mutually interfering transmissions within multiple groups.



subfiles are further divided into *|D| −*1 smaller parts for D2D
transmissions to ensure fresh content is transmitted.

The D2D subphase is followed by the downlink phase, where the BS multicasts coded messages containing all the remaining file fragments so that all users can decode their requested content. The received downlink signal at user terminal k ∈ [K] is given by

$$y_{k}=\mathbf{h}_{k}^{\mathrm{H}}\sum_{T\subseteq S}\mathbf{w}_{T}^{S}{\bar{X}}_{T}^{S}+z_{k},$$
T + zk, (2)
where X˜ S
T
is the multicast message chosen from a unit power complex Gaussian codebook dedicated to all the users in subset T of set S ⊆ [K] (provided that subset T has not been considered in D2D transmissions). The channel vector between the BS and user k is denoted by hk ∈ C
L, the receiver noise is given by zk ∼ CN(0, N0), and wS
Tis the beamforming vector dedicated to X˜ S
T
. The channel state information at the transmitter (CSIT) of all K users is assumed to be perfectly known. Finally, the total achievable rate (per user) over the above-described two phases is given by

$$R_{\mathrm{U}}={\frac{F}{T_{\mathrm{D2D}}+T_{\mathrm{DL}}}},$$

, (3)
where TD2D and TDL denote the transmission time for the D2D
and DL sub-phases, respectively.

## Iii. D2D Aided Beamforming Explained: Example

In this section, we illustrate the main idea of the proposed scheme via two examples. In the first example, we have a network of 3 users, and in the second example, the number of users is increased to 4.

## A. Example 1: K = 3, N = 3, M = 1, And L = 2

In this example, the network is comprised of K = 3 users and a library W = {*A, B, C*} of N = 3 files, where each user has the cache size M = 1 file. The base station is equipped with L = 2 transmit antennas. To begin with, the cache content Zk at each user k = 1*, . . . , K* is Z1 = {A1, B1, C1}, Z2 =
{A2, B2, C2}, Z3 = {A3, B3, C3}. Note that each file is divided into three equal-sized sub-files, following the cache placement in [6]. In this example, we assume users 1 and 2 are close to each other (c.f. Fig. 2).

Without loss of generality, assume users 1, 2, and 3 request files A, B, and C, respectively. Now, the delivery is carried out in two phases. In the first phase, i.e., the D2D phase, users 1 and 2 are assumed to share their local cache content through the D2D transmission. Thus, a single D2D time slot with D = {1, 2} exists. It is evident that user 2 would request B1 from user 1, and user 1 would request A2 from user 2. The D2D transmission is assumed to be half-duplex, i.e., two uni-directional D2D transmissions are included in each time slot. The time required for the D2D phase is given by TD2D = T1 → RD(1)+ T2 → RD(2)=
F/3 RD
1+
F/3 RD
2
, where RD(1) = {2}, RD(2) = {1}, and

$${\mathrm{(2)}}$$

RD
1 = log 1 + Pdkh12k 2 N0
, RD
2 = log 1 + Pdkh21k 2 N0
. Note that F3 fractions of the requested files are delivered in each transmission.

In the second phase (i.e., DL transmission), the BS multicasts the remaining content via coded messages. In the given example, user 3 is not served in the D2D phase and still needs C1 and C2. However, users 1 and 2 only require A3 and B3, respectively. These contents are XOR coded over two messages for user pairs (1, 3) and (2, 3). Namely, the messages are X1,3 = A3 ⊕ C1 and X2,3 = B3 ⊕ C2. Note that X1,3 simultaneously benefits both users 1 and 3. Similarly, X2,3 is a coded message intended for users 2 and 3. Accordingly, the multicast beamformer vectors w1,3 and w2,3 are associated with messages X1,3 and X2,3, respectively. The downlink signal is then formed as xDL = X˜1,3w1,3 + X˜2,3w2,3, where X˜ stands for the modulated X, chosen from a unit power complex Gaussian codebook [17]. Here, user 3 is assumed to use a successive-interference-cancellation (SIC) receiver to decode both intended messages (interpreted as a multipleaccess-channel (MAC)). In contrast, users 1 and 2 get served with a single message, with the other seen as interference.

Now, assume user 3 can decode *both* messages X˜1,3 and X˜2,3 with the equal rate2 R3MAC =

$\min\left(\frac{1}{2}R_{Sum}^{3},R_{1}^{3},R_{2}^{3}\right)$, where the rate region corresponding to $\tilde{X}_{1,3}$ and $\tilde{X}_{2,3}$ is limited by $R_{1}^{3}=\log\left(1+\frac{|\mathbf{h}_{2}^{H}\mathbf{w}_{1,3}|^{2}}{N_{0}}\right),R_{2}^{3}=\log\left(1+\frac{|\mathbf{h}_{2}^{H}\mathbf{w}_{2,3}|^{2}}{N_{0}}\right)$, and $R_{Sum}^{3}=\log\left(1+\frac{|\mathbf{h}_{2}^{H}\mathbf{w}_{1,3}|^{2}+|\mathbf{h}_{3}^{H}\mathbf{w}_{2,3}|^{2}}{N_{0}}\right)$. Accordingly,
$$({\boldsymbol{3}})$$
the corresponding downlink beamforming problem can be expressed as maxw2,3,w1,3 min(R3MAC, R1 1
, R2 1
), where the rates of users 1 and 2 are given as

$$\begin{array}{l}{{R_{1}^{1}=\log\left(1+\frac{|{\bf h}_{1}^{H}{\bf w}_{1,3}|^{2}}{|{\bf h}_{1}^{H}{\bf w}_{2,3}|^{2}+N_{0}}\right),}}\\ {{R_{1}^{2}=\log\left(1+\frac{|{\bf h}_{2}^{H}{\bf w}_{2,3}|^{2}}{|{\bf h}_{2}^{H}{\bf w}_{1,3}|^{2}+N_{0}}\right).}}\end{array}$$

Here, due to D2D transmissions, the beamforming problem differs from the one proposed in [17]. The partial file exchange in the D2D phase allows focusing the available DL
power on fewer multicast streams. In addition, it alleviates the DL phase's inter-stream interference conditions, making the DL multicast beamforming more efficient and easier to 2Symmetric rate is imposed to minimize the time needed to receive both messages X˜1,3 and X˜2,3.

 

design (see Section V). On the other hand, the D2D transmission requires an orthogonal allocation in the time domain.

This introduces an inherent trade-off between the number of resources allocated to the D2D and DL phases.

Finally, the corresponding symmetric rate maximization is given as

max wi,j ,γk l ,r r s. t. r ≤ 1 2 log(1 + γ 3 1 + γ 3 2 ), r ≤ log(1 + γ 3 1 ), r ≤ log(1 + γ 3 2 ), r ≤ log(1 + γ 1 1 ), r ≤ log(1 + γ 2 1 ), γ1 1 ≤|h H 1 w1,3| 2 |hH 1 w2,3| 2+N0 , γ 2 1 ≤|h H 2 w2,3| 2 |hH 2 w1,3| 2+N0 , γ3 1 ≤ |h H 3 w1,3| 2 N0, γ 3 2 ≤ |h H 3 w2,3| 2 N0, kw1,3k 2 + kw2,3k 2 ≤ PT .
Where PT is the total available power at the BS. The rate constraints can be written as a convex second-order cone problem as shown in [17]. However, the signal-to-interferenceplus-noise ratio (SINR) constraints are non-convex and require an iterative solution. A successive convex approximation
(SCA) solution for the SINR constraints can be found, e.g.,
in [17]. Please notice that, here, due to D2D transmission in the first phase, we have only two beamformer vectors (w1,3 and w2,3), which means we can dedicate more power to our intended signals (X1,3 and X2,3) compared to [17]. The time required for the DL phase is given by TDL =
F/3 r =
F/3 maxw2,3,w1,3 min(R3MAC,R1 1
,R2 1
)
. Here, similar to the first phase, all users are served with coded messages of size F3bits.

Finally, the achievable rate over the D2D and DL phases is given in (3).

## B. Example 2: K = 4, N = 4, M = 2, And L = 2

In this example, we consider a scenario where K = 4 users and a library W = {*A, B, C, D*} of N = 4 files, and each user has a cache for storing M = 2 files. Also, the base station is equipped with L = 2 transmit antennas. Following the cache placement in [6], each file is split into K
τ
=42
= 6 subfiles as follows

$$A=\{A_{1,2},A_{1,3},A_{1,4},A_{2,3},A_{2,4},A_{3,4}\},$$
$B=\{B_{1,2},B_{1,3},B_{1,4},B_{2,3},B_{2,4},B_{3,4}\}$, $C=\{C_{1,2},C_{1,3},C_{1,4},C_{2,3},C_{2,4},C_{3,4}\}$, $D=\{D_{1,2},D_{1,3},D_{1,4},D_{2,3},D_{2,4},D_{3,4}\}$.  
Each file WT is cached at user k if k ∈ T . Let us assume that users 1 − 4 request files A − D, respectively.

In this example, we assume users 1, 2, and 3 are close to each other, while user 4 is far from them as illustrated in Fig. 3. Then, during this phase, the first three users (collected in D = {1, 2, 3}) locally exchange content in three orthogonal D2D transmissions. Following [36], each subfile is further divided into |D(t)| − 1 = 2 fragments, discriminated by their superscript indices. Then, in the first D2D transmission of length T1 → RD(1)seconds, user 1 multicasts XD2D
1 = B1 1,3 ⊕ C
1 1,2 to RD(1) = {2, 3}. In the second D2D transmission, user 2 transmits XD2D
2 = A12,3 ⊕ C
2 1,2 to RD(2) = {1, 3}, which will take T2 → RD(2)seconds. Finally, in the third D2D transmission of length T3 → RD(3)
seconds, user 3 transmits XD2D
3 = A22,3 ⊕ B2 1,3 to RD(3) =
{1, 2}. These transmissions require the total time of TD2D =
T1 → RD(1)+ T2 → RD(2)+ T3 → RD(3), in which Ti → RD(i)=
F/12 RD
i
, i = 1, 2, 3 and RD
i
, i =
1, 2, 3 is given in (1).

In the DL phase, the BS transmits a message comprised of the remaining subfiles xDL = X˜1,2,4w1,2,4 + X˜1,3,4w1,3,4 + X˜2,3,4w2,3,4, where X1,2,4 = A2,4 ⊕ B1,4 ⊕ D1,2, X1,3,4 =
A3,4⊕C1,4⊕D1,3, and X2,3,4 = B3,4⊕C2,4⊕D2,3 3, and X˜T
is the modulated version of XT . At the end of this phase, user 1 is interested in decoding {X1,2,4, X1,3,4}, user 2 is interested in decoding {X1,2,4, X2,3,4}, user 3 is interested in decoding
{X1,3,4, X2,3,4}, and, user 4 is interested in decoding all the three terms {X1,2,4, X1,3,4, X2,3,4}. Thus, from the perspective of users 1, 2, and 3, there exists a MAC channel with two useful terms and one interference term. However, from the perspective of the user 4, there exists a MAC channel with three useful terms. In this regard, for users 1, 2, and 3 the MAC
rate region is given as RkMAC = min( 12Rk sum, Rk 1
, Rk 2
), k =
1, 2, 3. For instance, for user 1, we have R1 1 =
log 1 + |h H
1 w1,2,4| 2 |hH
1 w2,3,4| 2+N0
, R1 2 = log 1 + |h H
1 w1,3,4| 2 |hH
1 w2,3,4| 2+N0
,
and R1 sum = log 1 + |h H
1 w1,2,4| 2+|h H
1 w1,3,4| 2 |hH
1 w2,3,4| 2+N0
.

$=2,\:and\:L=2$. 
To derive the fourth user's rate region, we face a MAC with three messages. Thus, we have 7 MAC region inequalities, which will result in R4MAC. Then, the corresponding rate 3For convenience, the superscript S = {1, 2, 3, 4} in wS
T X˜ S
T
has been omitted in this example.

constraints for the MAC channel are listed below

6
R 4 1 = log 1 + |h H 4 w1,2,4| 2 N0 ! , R4 2 = log 1 + |h H 4 w1,3,4| 2 N0 ! , R 4 3 = log 1 + |h H 4 w2,3,4| 2 N0 ! , R 4 1,2 = log 1 + |h H 4 w1,2,4| 2 + |h H 4 w1,3,4| 2 N0 ! , R 4 1,3 = log 1 + |h H 4 w1,2,4| 2 + |h H 4 w2,3,4| 2 N0 ! , R 4 2,3 = log 1 + |h H 4 w1,3,4| 2 + |h H 4 w2,3,4| 2 N0 ! , R 4 1,2,3 = log 1 + |h H 4 w1,2,4| 2 + |h H 4 w1,3,4| 2 + |h H 4 w2,3,4| 2 N0 ! .
Thus, the MAC rate region for user 4 is expressed as follows

$$R_{\mathrm{MAC}}^{4}=\operatorname*{min}(\frac{1}{3}R_{1,2,3}^{4},\frac{1}{2}R_{1,2}^{4},\frac{1}{2}R_{1,3}^{4},\frac{1}{2}R_{2,3}^{4},R_{1}^{4},R_{2}^{4},R_{3}^{4}).$$
When all the MAC inequalities for all the users are considered
together, the common multicast rate is driven as follows
max
w*i,j,l*,γkm,r
r
subject to
r ≤
1
2
log(1 + γ
k
1 + γ
k
2 ), k = 1, 2, 3,
r ≤ log(1 + γ
k
m), k = 1, 2, 3, m = 1, 2,
r ≤
1
3
log(1 + γ
4
1 + γ
4
2 + γ
4
3 ), r ≤
1
2
log(1 + γ
4
1 + γ
4
2 ),
r ≤
1
2
log(1 + γ
4
1 + γ
4
3 ), r ≤
1
2
log(1 + γ
4
2 + γ
4
3 ),
r ≤ log(1 + γ
4
m), m = 1, 2, 3
γ
1
1 ≤|h
H
1 w1,2,4|
2
|hH
1 w2,3,4|
2+N0
, γ1
2 ≤|h
H
1 w1,3,4|
2
|hH
1 w2,3,4|
2+N0
,
γ
2
1 ≤|h
H
2 w1,2,4|
2
|hH
2 w1,3,4|
2+N0
, γ2
2 ≤|h
H
2 w2,3,4|
2
|hH
2 w1,3,4|
2+N0
,
γ
3
1 ≤|h
H
3 w1,3,4|
2
|hH
3 w1,2,4|
2+N0
, γ3
2 ≤|h
H
3 w2,3,4|
2
|hH
3 w1,2,4|
2+N0
,
γ
4
1 ≤ |h
H
4 w1,2,4|
2/N0, γ4
2 ≤ |h
H
4 w1,3,4|
2/N0,
γ
4
3 ≤ |h
H
4 w2,3,4|
2/N0,
kw1,2,4k
2 + kw1,3,4k
2 + kw2,3,4k
2 ≤ PT .
$$\quad(4)$$

Finally, the delivery time of the DL phase is TDL =
F/6 r
.

It should be noted that compared to [17], one term is removed from the DL transmission herein, i.e., X˜1,2,3w1,2,3.

We have taken care of this term in the D2D phase, enhancing the performance of the DL phase for two reasons. First, since we removed one term from DL transmission, the transmit power is shared by fewer beamformers. Second, since one term is removed, the number of conditions in the optimization problem is less than [17]. This will reduce the complexity of the optimization problem as discussed in Sec. V.

## C. Example 2: D2D Group Sizes Less Than Τ + 1

So far, based on the scheme proposed in [36], we have considered D2D group size |D| = τ + 1 = 3. However, given the scenario presented in Fig. 3, there are still some useful contents in the cache of the three users, which can be shared among them in D2D groups of size |D| = 2, i.e., D(1) = {1, 2}, D(2) = {1, 3}, D(3) = {2, 3}. In this regard, user 1 transmits B1,4 and C1,4 to users 2 and 3, user 2 transmits A2,4 and C2,4 to users 1 and 3, and user 3 transmits A3,4 and B3,4 to users 1 and 2, respectively. Therefore, compared to section III-B, six more time slots are needed in the D2D phase in this case, where the transmission scheme is similar to section III-A. Then, since user 4 has not received any data in the D2D phase, it still needs to receive all three missing subfiles through DL transmission. On the other hand, users 1, 2, and 3 have received all the missing data through D2D
transmissions. Thus, the downlink transmission is changed to xDL = X˜1,2,4w1,2,4 + X˜1,3,4w1,3,4 + X˜2,3,4w2,3,4, where X˜1,2,4 = D1,2, X˜1,3,4 = D1,3, and X˜2,3,4 = D2,3. The rate expression can be formulated similar to (4) with seven MAC conditions comprised of γ 4 1
, γ4 2
, and γ 4 3
. However, since the BS only serves one user in this special case, the DL phase can be simplified to unicast transmission. To this end, the DL message can be expressed as xˆDL = w4X˜4, where X˜4 = [D1,2, D1,3, D2,3] is the concatenated version of the three missing parts with the total size of F2bits.

Then, the corresponding beamformer can be expressed as a maximum ratio transmitter (MRT), i.e., w∗
4 =
h4PT
|h4|
. Note that, though the number of messages in the xDL (in this case)
remains the same as in Section III-B, the complexity of the beamformer design is greatly reduced. As a result, the rate for DL transmission is further enhanced, which in turn leads to a potential reduction of the total transmission time.

## Iv. D2D Aided Beamforming: The General Case

In this section, we formulate and analyze the proposed scheme in the general setting. We first consider D2D group size |D| = τ +1, then in section IV-D, we extend the results to group sizes smaller than τ + 1. The cache placement phase is identical to the one proposed in [6]. In general, similar to [17],
min(τ + *L, K*) users are served in each data transmission.

However, in our proposed scheme, the data is delivered over separate D2D and DL phases.

Before the delivery process, an exhaustive search among the D2D subsets is required to find the potential D2D groups for the first phase. However, since there are τ+L
τ+1different D2D subsets (of size τ + 1) among τ + L number of users, the exhaustive search would require 2
(
τ+L
τ+1)evaluations of (3).

Moreover, all the beamformers must be solved in each of these evaluations, and the total rate must be computed. Then, the case with the lowest delivery time is selected. However, this is practically infeasible due to the significant overhead. Thus, to reduce the computational burden, a less complex heuristic mode selection method is introduced in Section IV-B.

To simplify the notation, we consider an indicator function ID2D(D), which specifies whether the corresponding subset has been allocated for D2D transmission. Moreover, we denote C(*K, τ, L*) = F
(
K
τ )(K−(τ+1)
L−1 )
as the size of the transmitted subfiles [17].

A. Total delivery time TD2D + TDL
First, the D2D delivery time for a given selection of D2D
subsets is given as

$$T_{\mathrm{D2D}}=\sum_{\mathcal{D}\subseteq\overline{{{\Omega^{S}}}}}\sum_{k\in\mathcal{D}}{\frac{{\frac{C(K,\tau,L)}{(|\mathcal{D}|-1)}}}{R_{k}^{\mathcal{D}}}},\qquad\qquad(5)$$

where ΩS := {D ⊆ S, |D| = τ + 1, ID2D(D) = 1}, and RD
k is given in (1). Since in each D2D subset, each user transmit a1 |D|−1 fraction of a subfile, the corresponding data size in each D2D transmission is C(*K,τ,L*)
(*|D|−*1) (see section III-B).

Next, the DL beamforming is done using the SCA approach proposed in [17]. Compared to [17], we do not consider all the τ + 1 subsets. Here, subsets D for which ID2D(D) =
0 is considered in the DL phase, reducing the interference among parallel streams significantly. The DL phase throughput is given by

$$R_{C}\left(\mathcal{S},\{\mathbf{w}_{\mathcal{D}}^{\mathcal{S}},\mathcal{D}\subseteq\mathcal{S},|\mathcal{D}|=\tau+1,I_{D2D}(\mathcal{D})=0\}\right)=$$ $$\max_{\{\mathbf{w}_{\mathcal{D}}^{\mathcal{S}}\}}\min_{k\in\mathcal{S}}R_{MAC}^{k}\left(\mathcal{S},\{\mathbf{w}_{\mathcal{D}}^{\mathcal{S}},\mathcal{D}\subseteq\mathcal{S},I_{\mathrm{D2D}}(\mathcal{D})=0\}\right),\tag{6}$$

and

$$R_{MAC}^{k}\left(\mathcal{S},\{\mathbf{w}_{\mathcal{D}}^{S},\mathcal{D}\subseteq\mathcal{S},I_{\text{D2D}}(\mathcal{D})=0\}\right)$$ $$=\min_{\mathcal{B}\subseteq\Omega_{k}^{S}}\left[\frac{1}{|\mathcal{B}|}\log\left(1+\frac{\sum_{\mathcal{D}\in\mathcal{B}}|\mathbf{h}_{k}^{\text{H}}\mathbf{w}_{\mathcal{D}}^{S}|^{2}}{N_{0}+\sum_{\mathcal{D}^{\prime}\in\mathcal{I}_{k}}|\mathbf{h}_{k}^{\text{H}}\mathbf{w}_{\mathcal{D}^{\prime}}^{S}|^{2}}\right)\right],\tag{7}$$  where $\mathcal{I}_{k}=\Omega^{\mathcal{S}}\setminus\Omega_{k}^{S}:=\{\mathcal{D}\subseteq\mathcal{S}:|\mathcal{D}|=\tau+1,\ I_{\text{D2D}}(\mathcal{D})=\tau\}$
0 | k /*∈ D}* is the set of interfering messages at user k. Denote Ω
S := {D ⊆ S, |D| = τ + 1, ID2D(D) = 0} as the set of all the user subsets (of size τ + 1) that will be served in the DL phase4, where the cardinality |Ω
S | indicates the total number of messages delivered by the BS. Finally, let Ω
S
k
:= {D ⊆ S, |D| = τ + 1, ID2D(D) = 0 | k *∈ D}* denote the set of all the subsets in which user k exists (i.e., the set of all the messages required by user k).

After computing the rate for the DL phase, TDL is given as TDL =C(*K,τ,L*)
RC, while the symmetric delivery rate is given in (3). Note that solving (6) requires considerable computation due to the iterative convex approximation process and many constraints. Moreover, the exhaustive search would require computing (5) and (6) for each D2D subset evaluation.

Therefore, considering the total number of different D2D mode allocations (i.e., different combinations of subsets) and the complexity of computing (6) for each of these modes, the exhaustive search becomes impractical for large networks.

Therefore, in the following, we provide a low-complexity heuristic solution for the proposed mode assessment problem.

## B. Heuristic D2D Mode Selection With Low Complexity

To decrease the computational load of evaluating TD2D
and TDL for different D2D mode allocations, we provide a throughput approximation for the D2D mode allocations without relying on the general SCA solution for the DL
beamformer design. On the one hand, due to the orthogonal D2D and DL phases, each D2D content exchange between users adds extra time for delivering the content locally. On the other hand, each successful D2D transmission reduces the remaining number of subfiles to be transmitted by the BS.

Therefore, there are fewer multicast messages and corresponding beamforming vectors wSD in the DL optimization problem.

4In Example 2, ΩS = {{1, 2, 4}, {1, 3, 4}, {2, 3, 4}} and |ΩS | = 3.

As a result, a more efficient (less constrained) multicast beamformer design is possible, reducing the DL phase duration TDL. Therefore, the D2D mode selection is iteratively carried out as long as the following condition holds:

7
$$\frac{\hat{T}_{\rm DL}^{i}}{N_{s}^{i}}\geq\hat{T}_{\rm D2D}^{i},\quad i\in\left[1,\ \binom{\tau+L}{\tau+1}\right],\tag{8}$$  where $N_{s}^{i}=(\tau+1)\Big{(}\binom{\tau+L}{\tau+1}-(i-1)\Big{)}$ is the number of 
subfiles that is delivered in the DL phase assuming i D2D
subsets are selected. Moreover, TˆiDL and TˆiD2D are the coarse approximated delivery times in the i th iteration.

In (8), we check if any D2D user subset will reduce the DL duration TDL more than the added D2D duration. Note that in each D2D time slot, |D| = τ + 1 subfiles are delivered through τ + 1 orthogonal D2D transmissions. On the other hand, all the remaining subfiles (i.e., Ni s subfiles) are delivered simultaneously in the DL phase. Thus, in (8), the average delivery time for a single subfile in the D2D and DL phases is compared. To this end, we divide the total approximated DL
time (TˆiDL) by the number of subfiles (Ni s
), approximating the average transmission time for a single subfile. Thus, the average D2D transmission time for a subfile must be less than the corresponding average DL transmission time. In each iteration, we set a subset as a D2D candidate, i.e., the subset which provides the lowest delivery time. If a specific subset D in iteration i satisfies (8), we set ID2D(D) = 1 for this subset, and the D2D transmission is done as in [36].

If (8) does not hold at any specific iteration, using more D2D transmissions will not improve the rate, and the iterative process is terminated. Therefore, at most, τ+L
τ+1iterations are required for the proposed iterative process, while 2
(
τ+L
τ+1)
iterations are needed for the exhaustive search.

The D2D delivery time is coarsely approximated as

$$\hat{T}_{\mathrm{D2D}}^{i}=\operatorname*{min}_{\mathcal{D}\subseteq\Omega^{S}}{\frac{1}{|\mathcal{D}|}}\sum_{k\in\mathcal{D}}{\frac{\frac{C(K,\tau,L)}{|\mathcal{D}|-1}}{R_{k}^{\mathcal{D}}}}.\qquad\qquad(9)$$

In each D2D transmission (see Fig. 1), 1 |D|−1 fractions of each subfile (of size C(*K, τ, L*)) are delivered by user k ∈ D at the rate RD
k
. Moreover, in each D2D subset, |D| = τ + 1 subfiles are delivered. Thus, in (9), the total required time is divided by |D| to compute the average delivery time for a single subfile.

Note that for each iteration i, we only consider those subsets that have not yet been allocated for D2D transmissions.

To approximate TDL, we make the following assumptions.

First, we assume the beamformer wSD can remove all the interference for user k ∈ D. Thus, we may assume Ik = ∅,
∀k ∈ S in (7). Second, we assume the beamformer wSD in (7)
is matched to the channels of all the users in subset D, i.e., the received SNR for Xˆ SD at receiver k is SNRkD =
khkk 2PD
N0. Note that the beamformer wSD is designed such that all the users in subset D can decode the message Xˆ SD. Thus, to reflect this, we make use of the user's channel gain for the heuristic mode selection process and limit the rate to the weakest user.5 Thus, 5Another interpretation for (10) is that the beamformer wSD is assumed to be matched to the weakest user in subset D without rate loss for other users with better channel condition in the subset.

the DL delivery time is coarsely approximated as

8
$$\hat{T}_{\rm DL}^{i}=\frac{C(K,\tau,L)}{\min_{k\in[S]}\frac{1}{|\Omega_{k}^{2}|}\log\left(1+\frac{\|{\bf h}_{k}\|^{2}}{N_{0}}\sum_{{\cal D}_{\subseteq}\Omega_{k}^{S}}{\sf P}_{{\cal D}}\right)},\tag{10}$$
where PD is the dedicated power to the message Xˆ SD. Denote

$\hat{R}_{k}^{i}\triangleq\frac{1}{|\Omega_{k}^{s}|}\log\left(1+\frac{\|\mathbf{h}_{k}\|^{2}}{N_{0}}\sum\limits_{\mathcal{D}\subseteq\Omega_{k}^{s}}\mathbf{P}_{\mathcal{D}}\right)$ as the approximated rate of user $k$ assuming $i-1$ subsets have been chosen for D2D.  
transmission. Note that Rˆik can be interpreted as the achievable rate of equivalent single-user MISO MAC channel with several
(i.e., |Ω
S
k |) useful terms and no interference.

To reflect the max-min objective in (6), we assume the power is divided among different messages such that minimum received SNR for any two different messages are equal, i.e.,
mini∈U khik 2 PU
N0
= minj∈Dkhjk 2 PD
N0
, ∀{D, *U} ∈* Ω
S , D 6=
U. Accordingly, the closed-form solution for PD is given as follows

$$\mathrm{P}_{\mathcal{D}}=\frac{\prod\limits_{\mathcal{U}\subseteq\Omega^{\mathcal{S}}/\mathcal{D}}\min_{k\in\mathcal{U}}\|\mathbf{h}_{k}\|^{2}P_{T}}{\sum\limits_{\mathcal{V}\subseteq\Omega^{\mathcal{S}}}\prod\limits_{\mathcal{U}\subseteq\Omega^{\mathcal{S}}/\mathcal{V}}\min_{i\in\mathcal{U}}\|\mathbf{h}_{i}\|^{2}},\quad\forall\mathcal{D}\in\Omega^{\mathcal{S}}.\tag{11}$$

It is worth mentioning that when users experience similar channel conditions, the power allocated to each message can be assumed to be almost equal; therefore, (10) can be simplified to the approximated DL time in [45], i.e.,

$$\hat{T}_{\mathrm{DL}}^{i}\sim\frac{C(K,\tau,L)}{\operatorname*{min}_{k\in[\mathcal{S}]}\frac{1}{|\Omega_{k}^{\mathcal{S}}|}\log\left(1+\frac{|\Omega_{k}^{\mathcal{S}}||\mathbf{h}_{k}|^{2}P_{T}}{|\Omega^{\mathcal{S}}|N_{0}}\right)}.$$

Once the user subsets for the D2D phase are selected, the final delivery time/rate is computed as in Section IV-A. Note that when ID2D(D) = 1, the coded message corresponding to subset D is already delivered in the D2D phase. Thus, we can ignore such a subset in the DL phase, resulting in less intermessage interference and lower DL delivery time than [17].

Finally, the complete algorithm for the proposed two-phase delivery scheme is given in Algorithm 1.

Remark 1: The proposed D2D/DL mode selection in Algorithm 1 is based on instantaneous channel knowledge and does not need any previous data history to approximate TˆD2D or TˆDL. However, the time approximation proposed in this work can be further improved by collecting statistics about users' channel conditions over a period and applying ML tools to approximate the D2D and DL transmission times.

## C. Heuristic D2D Mode Selection For Restricted Dof

The proposed iterative D2D mode selection can be extended to the system setting with restricted DoF [17]. The authors in [17] propose limiting the DoF by serving τ + α (α ≤ L)
users at each transmission phase, resulting in a less complex beamformer design. Furthermore, they divide the users into P distinct groups (for some P ∈ N) to decrease the number of overlapping groups (c.f. [17]). The combination of D2D
and DL transmissions proposed in this paper also applies to the *α < L* case. The difference is that the total number of different D2D subsets changes from τ+L
τ+1to Pτ+β τ+1,where β ,τ+α P − τ is an integer. Accordingly, Ω
S , Ω
S k
, and C(*K, τ, L*) change to the ones defined in [17], and the process remains the same. This paper is a particular case of the system proposed in [17] where P = 1, and α = β = L.

## D. D2D Aided Beamforming For General Group Sizes

In this section, we extend the results in sections IV-A and IV-B to general D2D group sizes. Let us define a new set ΩS,V := {V ⊆ S, 2 *≤ |V| ≤* τ + 1, ID2D(V) = 1} as the set of D2D groups (of any size) selected for D2D phase. Now, for a given D2D subset selection, the TD2D is computed as the following

$$T_{\mathrm{D2D}}=\sum_{\mathcal{V}\subseteq\overline{{{\Omega^{S,\mathcal{V}}}}}}\sum_{k\in\mathcal{V}}\frac{\frac{a_{k}^{\mathcal{V}}C(K,\tau,L)}{(|\mathcal{V}|-1)}}{R_{k}^{\mathcal{V}}},\qquad\qquad(12)$$

where a V
k is the number of transmitted messages by user k ∈
V. Please note that though a V
k = 1 for |V| = τ + 1, a V k can be any number for |V| < τ + 1. The corresponding DL rate
(RC ) for the general group sizes is computed using (6). The heuristic mode selection criteria (8) changes as follows

$$\frac{\hat{T}_{\rm DL}^{i}}{N_{v}^{i}}\geq\hat{T}_{\rm D2D}^{i},\quad i\in\left[1,\,\sum_{j=2}^{\tau+1}\binom{\tau+L}{j}\right],\tag{13}$$

where Niv is the total number of remaining subfiles delivered through DL transmission in the i'th iteration. Here, we first check the subsets of size |V| = τ + 1 using (9); after all the subsets of size |V| = τ + 1 are checked, we continue the procedure for 2 ≤ |V| < τ+1. We use the same approximation for TˆiDL and TˆiD2D given in (9) and (10), respectively. However, for general group sizes, each transmitted message Xˆ SD in the DL phase may not be useful for all k ∈ D (some users in D
may have received the transmitted useful term in D2D mode).

Thus, in (11), the minimum is taken over those users who still need the message.

Similar to section IV-B, the D2D subset selection is carried out as long as (13) holds. The difference is that for group size less than τ + 1, each user may have several contents to transmit to the other users (i.e., a V
k 6= 1). When a subset V
is selected for D2D transmission, users in V transmit all the useful data available in their cache to the other users in the selected subset (following the method in [36]) and ID2D(V) is set to one. We also set ID2D(D) to one if all the subfiles in D are transmitted through D2D groups of size V < τ + 1. The rest of the process is the same as in Section IV-B. After D2D
subset assessment is done, the DL delivery time is computed using (10), and the D2D time is computed using (12).

It is worth mentioning that the main target in (8) and (13)
is to reduce the overall transmission time (i.e., TD2D + TDL)
in (3). However, as we show in the following section, D2D
transmission can also notably reduce the complexity of the beamforming process in the DL phase. To this end, we briefly illustrate the complexity involved in the beamformer design and the effect of D2D transmission on the process.

Algorithm 1 D2D Assisted Multi-Antenna Coded Caching procedure DELIVERY(W1, . . . , WN , d1*, . . . , d*K, H = [h1*, . . . ,* hK])
τ ← *MK/N*
for i ∈-1,τ+L
τ+1 do if TˆiDL
Nis
≥ TˆiD2D **then**
for all k ∈ D do

9
Each sub-file is divided into $\tau$ mini-file fragments.  $X_k^D\gets\oplus_{i\in\mathcal{D}\backslash\{k\}}NEW(W_{di,\mathcal{D}\backslash\{i\}}$  User $k$ multiclass $X_k^D$ to $\mathcal{R}^{\mathcal{D}}(k)=\mathcal{D}\backslash\{k\}$ with the rate $R_k^{\mathcal{D}}$ stated in (1) $I_{D\geq D}(\mathcal{D})=1$  **end for**  12. 
end if
end for for all S ⊆ [K], |S| = min(τ + L, K) do for all D ⊆ S, |D| = τ + 1, ID2D(D) = 0 do X S D ← ⊕k∈DNEW(Wdk,D\{k}) end for {wSD} = arg max {wSD,D⊆S,|D|=τ+1,ID2D(D)=0} RCS, {wSD, D ⊆ S, |D| = τ + 1, ID2D(D) = 0} X(S) ←PD⊆S,|D|=τ+1,ID2D(D)=0 wSDX˜ SD transmit X(S) with the rate RC (S, {wSD, D ⊆ S, |D| = τ + 1, ID2D(D) = 0}). end for end procedure

## V. Beamforming Complexity Analysis

In this section, we investigate the effects of D2D transmissions in computational complexity for the general case.

Authors in [17] show that the number of MAC conditions and quadratic terms in the SINR constraints dominates the complexity of the DL beamformer design. Thus, we first introduce two boundaries for the number of MAC conditions, then discuss the effects of D2D on the beamformer design complexity.

Theorem 1: Considering i(τ + 1) +m subfiles are delivered via D2D transmissions, among which i(τ + 1) subfiles are delivered through D2D groups with size (τ + 1), the number of MAC conditions for the DL phase is lower bounded by:

$$\underline{M}(\tau,i,m,L)=(\tau+L-b)(2^{a}-1)+b(2^{a+1}-1),\tag{14}$$

where

$$\begin{array}{l}{{a\triangleq\left\lfloor\frac{\left(\tau+1\right)\left(M_{\mathrm{T}}-i\right)-m}{\tau+L}\right\rfloor,}}\\ {{b\triangleq\left(\tau+1\right)\left(M_{\mathrm{T}}-i\right)-m-a\left(\tau+L\right),}}\\ {{m\triangleq\sum_{\mathcal{V}\in\Omega^{S,\mathcal{V}}\backslash\Omega^{S}}\sum_{k\in\mathcal{V}}a_{k}^{\mathcal{V}},\quad M_{\mathrm{T}}\triangleq\binom{\tau+L}{\tau+1},}}\end{array}$$
τ + 1, (17)
and the number of MAC conditions is upper bounded by M(*τ, i, m, L*) =

$$\begin{array}{l}{{d(\tau,i,m,L)=}}\\ {{\ (\tau+L-U)(2^{W}-1)+(2^{W-X}-1)}}\\ {{\ \ \ \ \ \ +(U-(\phi+1))(2^{(W-\binom{U-2}{\tau})}-1),}}\end{array}$$
τ )) − 1), (18)
where

$$\begin{array}{l l}{{U\triangleq\operatorname*{min}}}&{{\operatorname*{min}}}&{{U^{\prime},\ X\triangleq i-\dbinom{U-1}{\tau+1},}}\\ {{\mathrm{s.r.~}(\l_{\tau+1}^{U^{\prime}})\geq i}}&{{}}\\ {{\phi\triangleq\left\lfloor{\frac{m}{W-\dbinom{U-2}{\tau}}}\right\rfloor,\ W\triangleq\dbinom{\tau+L-1}{\tau}.}}\end{array}$$
(19)  $\binom{20}{2}$  . 

. (20)
Proof 1: Refer to Appendix A.

The number of MAC conditions varies between M(.) and M(.) based on which particular subsets have been selected for the D2D phase. For better intuition consider Fig. 4, which shows the normalized maximum and minimum number of MAC conditions (K = 10, L = 9, τ = 1) for different number of D2D groups i. As shown, the number of MAC
conditions decreases drastically by using just a few D2D transmissions, which in turn dramatically reduces the complexity of the DL beamformer design. For example, for the case depicted in Fig. 4, by choosing only five different subsets of users among 45 available subsets, the number of MAC conditions can be reduced to half. Therefore, D2D significantly improves the beamformer design complexity.

In the following, we provide the boundaries for the number of quadratic terms in the SINR constraints (the second important factor in the DL beamforming complexity).

Theorem 2: Considering i(τ + 1) +m subfiles are delivered via D2D transmissions, among which i(τ + 1) subfiles are delivered through D2D groups with size (τ + 1), the number of quadratic terms is upper bounded by:

$$\overline{{{Q}}}(\tau,i,m,L)=b A_{2}B_{2}+(\tau+L-b)A_{1}B_{1},$$
$$(18)$$

where A1 , *a, A*2 , a + 1, B1 , MT − i − A1 + 1, B2 ,
MT − i − A2 + 1. Moreover, the number of quadratic terms is





lower bounded by:

$$\underline{Q}(\tau,i,m,L)=(\tau+L-U)A^{\prime}_{1}B^{\prime}_{1}$$ $$+(U-(\phi+1))A^{\prime}_{2}B^{\prime}_{2}\ +A^{\prime}_{3}B^{\prime}_{3},\tag{22}$$  where $A^{\prime}_{1}\stackrel{{\triangle}}{{=}}W,\ A^{\prime}_{2}\stackrel{{\triangle}}{{=}}A^{\prime}_{1}-\binom{U-2}{\tau},\ A^{\prime}_{3}\stackrel{{\triangle}}{{=}}A^{\prime}_{1}-X,B^{\prime}_{1}\stackrel{{\triangle}}{{=}}M_{\rm T}-A^{\prime}_{1}+1,\ B^{\prime}_{2}\stackrel{{\triangle}}{{=}}M_{\rm T}-A^{\prime}_{2}+1,\ B^{\prime}_{3}\stackrel{{\triangle}}{{=}}M_{\rm T}-A^{\prime}_{3}+1.$ We
denote MT ,
τ+1(MT−i)−m τ+1 as the lower approximation of the total number of messages sent by the BS. Moreover, a, b, X, U, m, MT, W and φ are defined trough (16) to (20).

Proof 2: Refer to Appendix B.

Fig. 5 depicts the upper and lower boundaries for the same scenario as in Fig. 4. The gap between these bounds is not as considerable as MAC conditions. Thus, compared to the quadratic terms, the number of MAC conditions is more affected by how different D2D subsets are selected for transmission. Nevertheless, the role of D2D transmissions in reducing the total number of quadratic terms is notable.

For example, choosing five different D2D subsets for the considered case reduces the total number of quadratic terms by 20%.

Remark 2: For ease of exposition, τ + L = K is assumed in the equations and algorithms throughout this paper.

However, the proposed methods can be easily generalized to other regimes. For example, in case τ + *L < K*, there are K
τ+L
orthogonal transmission phases. All the equations in this paper are valid separately for each phase. Similarly, for the case τ + *L > K*, τ + L should be replaced with K
in all the equations. Moreover, for the restricted spatial DoF
scenario [17], discussed also in Section IV-C, τ +L should be changed to τ + α. Finally, the β parameter introduced in [17]
can be easily applied to the proposed equations by changing MT to Pτ+β τ+1, and W to τ+β−1 τ, where *α, β* and P are defined in Section IV-C.

## Vi. Numerical Results

In this section, we provide numerical examples for two scenarios with K = 3 and K = 4 users (see Fig. 2 and Fig. 3). Due to the complex beamforming procedure for the multiserver-based schemes (such as the one proposed in this paper), we have considered a limited number of users in the network. We consider a circular cell with a radius of R = 100 meters, where the BS is located in the cell center. To investigate the effect of D2D transmission in different situations, we introduce a smaller circle with radius r within the cell area, wherein the users are randomly scattered. Thus, the maximum distance between any two users is 2r. In contrast, the users' distance to BS varies between 0 and R. Hence, by changing r, the maximum users' separation in D2D mode is controlled, which helps us determine the beneficial users' distance in the D2D phase.

For D2D transmissions, the channel gains are generated as hik = d
−
nD2D
2 ik gik, where gik ∼ CN(0, 1), nD2D = 2 is the path-loss exponent, and dik is the inter-user distance. The channel vectors for DL transmission are generated from i.i.d statistics with hk = d
−
nDL
2 kgk, where gk ∼ CN(0, I), nDL = 3 is the path-loss exponent, and dk is the BS-user distance.

Transmit powers for D2D transmissions at the user side are adjusted so that the average received SNR at the receiver is 0 dB at a 10-meter distance. The BS transmit power is adjusted such that the average received SNR is 0 dB at a 100-meter distance. For comparison, we have also consider two benchmark schemes [17] and [36] denoted as Multicasting only and *D2D only*, respectively. Note that the optimality of