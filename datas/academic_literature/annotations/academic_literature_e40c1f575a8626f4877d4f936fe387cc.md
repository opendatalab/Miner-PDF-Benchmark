# D2D Assisted Multi-Antenna Coded Caching 

Hamidreza Bakhshzad Mahmoodi, Jarkko Kaleva ${ }^{\star}$, Seyed Pooya Shariatpanahi* and Antti Tölli^ $\star$ Centre for<br>Wireless Communications, University of Oulu, P.O. Box 4500, 90014, Finland<br>* School of Electrical and Computer Engineering, College of Engineering, University of Tehran, Iran,<br>firstname.lastname@oulu.fi, p.shariatpanahi @ut.ac.ir


#### Abstract

D2D) aided multi-antenna coded caching scheme is proposed to improve the average delivery rate and reduce the downlink (DL) beamforming complexity. deviceto-device (D2D) aided multi-antenna coded caching scheme is proposed to improve the average delivery rate and reduce the downlink (DL) beamforming complexity.A Novel beamforming and resource allocation schemes are proposed where local data exchange among nearby users is exploited. The transmission is split into two phases: local D2D content exchange and DL transmission. In the D2D phase, subsets of users are selected to share content with the adjacent users directly. In this regard, a low complexity D2D mode selection algorithm is proposed to find the appropriate set of users for the D2D phase with comparable performance to the optimal exhaustive search. During the DL phase, the base station multicasts the remaining data requested by all the users. We identify scenarios and conditions where D2D transmission can reduce the delivery time. Furthermore, we demonstrate how adding the new D2D phase to the DLonly scenario can significantly reduce the beamformer design complexity in the DL phase. The results further highlight that by partly delivering requested data in the D2D phase, the transmission rate can be boosted due to more efficient use of resources during the subsequent DL phase. As a result, the overall content delivery performance is greatly enhanced, especially in the finite signal-to-noise (SNR) regime.


## I. INTRODUCTION

The daily surge in network traffic has pushed the network providers towards advanced data delivery methods to meet the client's demands. Luckily, a vast share of the network traffic is for multimedia content, such as video streams, which can be proactively cached before hands [1], [2]. Specifically, considering the upcoming data-intensive applications such as extended reality (XR), which rely heavily on asynchronous content reuse [3]-[5], proactive caching at the end-users could relieve network congestion during busy hours. The aim is to leverage off-peak hours to move some content closer to the end-users, which will be used to relieve the network's load during peak hours. Coded caching (CC) has been recently proposed by Maddah-Ali and Niesen in [6], which improves the traditional caching schemes [7] by benefiting from the aggregated memory throughout the network. As a result, an[^0]

additional global caching gain is achieved on top of traditional local caching gain in the CC scheme.

The CC scheme was initially proposed for the error-free shared link framework (e.g., [6], [8], and [9]), but it was promptly extended to wireless setup $[10]-[13]$. In this regard, the setup in [6] is extended in [10] to a multiple server scenario, where the effects of the network structure on the CC performance are investigated. Motivated by the results in [10], the authors in [11] propose different multi-antenna CC transmission schemes for the physical layer. Furthermore, focusing on high signal-to-noise-ratio (SNR) region analysis, authors in [12], [13] show that CC boosts the wireless network performance in terms of Degrees-of-Freedom (DoF). Specifically, the global coded caching gain offered by the CC and the spatial multiplexing gain provided by a multi-antenna transmitter are additive in a wireless broadcast channel [14]. Moreover, the multiantenna $\mathrm{CC}$ is also highly beneficial with finite SNR as long as the interference is appropriately compensated [15]-[17]. Specifically, while [15] and [16] use a rate-splitting approach to simultaneously benefit from the global caching and the spatial multiplexing gains, a general beamformer design was proposed in [17] to improve the finiteSNR performance of the coded caching in wireless networks.

Despite significant CC benefits in wireless networks, several practical challenges have been identified in the literature [18][28]. For instance, users' privacy requirements to prevent information leakage have been specified in [18]. In this regard, authors in [19] extend the idea in [18] to a D2D CC network, using non-perfect secret sharing and one-time pad keying techniques. The number of file division requirements in CC, known as subpacketization problem, is considered in [20][25]. While authors in [20] benefit from the linear block code (LBC) technique to reduce the subpacketization, authors in [21], [22] benefit from the number of antennas at the transmitter. In a similar work, the effect of the subpacketization on the achievable rate in the low-SNR region was also investigated in [23]. Finally, authors in [24], [25] propose the shared cache scheme to efficiently control the subpacketization requirement.

Another crucial issue in the $\mathrm{CC}$ wireless setting is near-far problem. Explicitly, in conventional CC delivery schemes, a common message is transmitted to several users. Thus, the rate is always limited by the user with the worst channel condition to ensure every user can decode the common message [17]. In this regard, the authors in [26] propose a congestion control to avoid serving users in a fading state, while the authors in [27] propose to serve users when they are in favorable conditions via appropriate scheduling. Using a different approach, authors
in [28] benefit from deep reinforcement learning (DRL) to jointly design caching and scheduling schemes, tackling the near-far problem. Unlike [27] and [26], which apply traditional XORing of data elements, authors in [29] and [3] allocate different rates to users with different channel conditions by altering the modulation scheme. Finally, one critical drawback of the traditional wireless CC delivery is the high complexity of the optimized beamforming solutions, which can render multiantenna CC infeasible for large networks [17].

The CC cache placement must be carefully designed so that every user has some data needed by others [6]. On the other hand, in many particular use cases, such as immersive viewing applications, groups of users are being served together [3]-[5]. In such scenarios, users can intermingle at close distances, making the device-to-device (D2D) communication quite alluring. Motivated by this, a two-phase transmission scheme is proposed in this paper, where the downlink (DL) multicasting of the file fragments in [17] is complemented by the direct D2D exchange of local cache contents.

## A. Related works

D2D communication has been studied extensively in wireless scenarios for traditional caching methods, where an entire file is placed at the end-user (see for example [7], [30]-[32]). The idea is that utilizing D2D communication results in less congested servers, improved network energy efficiency (EE), mitigated near-far problems, etc. On the other hand, currently, interest is increasing in machine learning (ML) tools such as deep deterministic policy gradient (DDPG) [33] as a means for various wireless resource allocation problems (e.g., [34]). In this regard, authors have considered applying ML in cacheaided data delivery, including D2D communications [35]. Specifically, ML tools can be utilized for cache placement or delivery schedules for cache-aided networks [35], including coded caching [28].

Interestingly, D2D ideas have been extended to the CC wireless networks to improve network throughput [36]-[42]. An infrastructure-less CC network is considered in [36], where the D2D is the only transmission link. Moreover constructive achievable coding strategies and information-theoretic bounds are also specified in [36]. Later, the authors in [37] characterized the optimal load-memory trade-off under the uncoded placement and one-shot delivery assumptions. Yet, the authors in [37] extend the system model in [36] such that robustness against random user inactivity is achieved via maximum distance separation (MDS) coding. Users with different available memories are considered in [38] to extend the scenario in [36] to a more practical one. On the other hand, the authors in [39] show that the frequency reuse gain and CC multicasting gain are additive when users move inside the D2D network. The authors in [40] extend [36] to a general framework by utilizing the placement delivery array (PDA), alleviating the subpacketization problem.

Authors in [41] extend the network in [6] to the case where users can cooperate via D2D links. Therein, the D2D and DL transmissions are assumed to be carried out in parallel without interference. Thus, to minimize the total transmission time, the authors in [41] optimally divide the transmission load into D2D and DL parts. Unlike [36]-[41] with fixed rates assumption, the authors in [42] consider a multi-user singleinput-single-output (SISO) scenario where transmission rates are changed depending on channel conditions. In this regard, D2D transmissions are utilized along with the DL transmission to decrease the transmission time. Specifically, the BS decides whether to transmit a sub-file in DL or D2D fashion based on users' neighboring conditions. Furthermore, different amounts of memory are dedicated to the D2D and DL sub-files in [42] to minimize the delivery time.

## B. Main contribution

Although CC-based D2D communication has been thoroughly investigated in the literature for single-antenna transceivers $[36]-[42]$, a D2D framework supporting CCbased multi-antenna communication is still missing considering the current multi-antenna transmission support in the 5G standards [43]. In this regard, this paper extends the framework studied in the previous studies $[36]-[42]$ to a multiantenna transmitter scenario, where we consider a single-cell multi-user multiple-input single-output (MISO) network. The proposed delivery scheme in this work comprises D2D links as a complementary transmission phase to the DL transmission. The cache placement is based on [6]; thus, every user has some data that can be shared with other users. The goal is to minimize the total transmission time by delivering a part of the requested data via D2D transmissions while the rest is delivered by the base station (BS). To find the optimal combination of D2D and DL transmissions, we should be able to compare the available D2D and the DL rates. However, the optimal D2D/DL mode selection is a combinatorial problem, requiring an exhaustive search for D2D opportunities over a group of users. Hence, due to the NP-hard nature of the problem, the exhaustive search quickly becomes computationally intractable. On the other hand, to know the exact achievable DL rate, all the beamformers should be first designed for all possible combinations. As mentioned before, this is challenging due to the high computational complexity of multicast beamforming. Consequently, we propose an approximation for the DL achievable rate without computing the beamformers to resolve the beamforming complexity issue. Next, based on the approximated DL rate, we provide a low complexity mode selection algorithm, which allows efficient determination of D2D opportunities even for a large number of users. The computational complexity of the proposed algorithm is significantly reduced compared to the exhaustive search with similar performance.

In infrastructure-less networks, as in [36], the geographical separation of users severely affects the total transmission time. However, using the D2D transmission phase as a complementary phase for the DL transmission results in steadier behavior against geographical separation than in the DL-only case in [17] and the D2D-only case in [36]. In addition, it significantly shortens the delivery time. On the other hand, by allowing direct D2D exchange of file fragments, the interference management among a reduced number of downlink

| List of Notations |  |  |  |
| :--- | :--- | :--- | :--- |
| $\mathcal{W}$ | Library | $Z_{k}$ | Cache content |
| $\tau$ | Global caching gain | $W_{n, \mathcal{V}}$ | Subfile $n$ |
| $d_{k}$ | Request index | $\mathcal{D}^{\mathcal{L}(\mathrm{t})}$ | D2D set |
| $\mathcal{R}^{\mathcal{D}}(i)$ | D2D receiver set | $X_{i}^{\mathrm{D}}$ LD | D2D transmit signal |
| $P_{d}$ | User transmit power | $N_{0}$ | Noise variance |
| $h_{i k}$ | D2D channel | $y_{k}$ | Received signal |
| $z_{k}$ | Receiver noise | $\bar{X}_{T}^{S}$ | DL transmit message |
| $\mathbf{w}_{T}^{S}$ | DL beamformer | $\mathbf{h}_{k}$ | DL channel |
| $T_{\text {D2D }}$ | D2D delivery time | $T_{\text {DL }}$ | DL delivery time |
| $R_{\mathrm{U}}$ | Symmetric rate | $P_{T}$ | BS transmit power |
| $\mathbf{x}_{D L}$ | DL transmit signal | $I_{\text {D2D }}(\mathcal{D})$ | D2D user set indicator |
| $C()$. | DL file size | $\overline{\Omega^{S}}, \overline{\Omega^{\mathcal{S}}, \mathcal{V}}$ | Set of D2D user sets |
| $\Omega^{\mathcal{S}}$ | Set of DL messages | $\Omega_{k}^{S}$ | Needed message set |
| $\mathcal{I}_{k}$ | Interference set | $N_{\mathcal{S}}, N_{\mathcal{V}}^{i}$ | DL message count |

TABLE I

THE LIST OF MAIN NOTATIONS

multicast streams becomes more efficient than in [17]. Finally, we thoroughly investigate the complexity reduction of the DL beamformer due to the proposed complementary D2D phase. This paper extends our earlier conference papers [44], [45] to a general D2D-aided multiantenna CC framework without any group size restrictions and also provides a more detailed analysis of beamforming complexity. Note that this work focuses on instantaneous channel knowledge for D2D/DL mode selection and does not consider any ML-based technique. The reason is that due to numerous practical challenges, satisfactory utilization of ML techniques for cache-aided networks is still missing. A thorough survey on ML utilization challenges for cache-aided networks (e.g., data integrity, dynamic environment, utilization of big data) can be found in [46].

## C. Organization and notations

The rest of the paper is organized as follows. In Section II the system model is introduced. In Section $\Pi$ we illustrate the main elements of the proposed scheme via two examples. Then, Section IV demonstrates the proposed scheme for the general case. Section $\mathrm{V}$ analyzes the complexity reduction of the DL beamforming due to the complementary D2D phase. Section VI presents numerical results, and Section VII concludes the paper.

Notations: Matrices and vectors are presented in boldface upper and lower case letters, respectively. The Hermitian of the matrix $\mathbf{A}$ is denoted as $\mathbf{A}^{\mathrm{H}}$. Cardinality of a discrete set $\mathcal{A}$ is given by $|\mathcal{A}|$. Let $\mathbb{C}$ denote the set of complex numbers and $\|$.$\| be the norm of a complex vector. Also, [m]$ denotes the set of integer numbers $\{1, \ldots, m\}$, and $\oplus$ represents addition in the corresponding finite field. Finally, Table $\square$ collects the main notations used in this paper.

## II. System ModeL

We consider a system consisting of a single $L$ antenna BS and $K$ single antenna users. The BS has a library of $N$ files, namely $\mathcal{W}=\left\{W_{1}, \ldots, W_{N}\right\}$, where each file has the size of $F$ bits. The normalized cache size (memory) of each user is $M$ files. Each user $k$ stores a fragment of each file, denoted by $Z_{k}\left(W_{1}, \ldots, W_{N}\right)$ during the cache placement phase (cache placement is identical to [6]). Thus, for the case $\tau=\frac{K M}{N} \in \mathbb{N}$,
![](https://cdn.mathpix.com/cropped/2024_05_09_d8867f52fbc810dc46cag-03.jpg?height=798&width=868&top_left_y=170&top_left_x=1084)

Fig. 1. Time division between D2D and DL transmission slots for a network with $K=7$ users and two D2D groups $\mathcal{D}(1)=\{1,2\}$ and $\mathcal{D}(2)=\{5,6,7\}$. The total transmission time to serve all the users is $T_{\mathrm{D} 2 \mathrm{D}}+T_{\mathrm{DL}}$

each file is divided into $\binom{K}{\tau}$ non-overlapping subfiles, i.e., $W_{n}=\left\{W_{n, \mathcal{V}}: \mathcal{V} \subset[K],|\mathcal{V}|=\tau\right\}, \forall n \in[N]$. Each user $k$ stores all the subfiles $\mathcal{V} \ni k$, i.e., $Z_{k}=\left\{W_{n, \mathcal{V}} \mid k \in \mathcal{V}, \mathcal{V} \subset\right.$ $[K],|\mathcal{V}|=\tau, \forall n \in[N]\}$. During the content delivery phase, user $k \in[K]$ makes a request for the file $W_{d_{k}}, d_{k} \in[N]$.

We envision a scenario where a group of users is being served simultaneously. These users are free to move inside the coverage area, and at specific times, they request some content from the server. The immersive viewing application illustrated in [3], and [4] can be considered a specific use case. Thus, it is very likely to have some nearby users at each time instance who can share some content among themselves via D2D transmissions. Accordingly, the delivery phase starts with the D2D sub-phase, divided into a number of D2D time slots. In each time slot $t$, a group of nearby users, denoted by set $\mathcal{D}(t)$, are instructed by the BS to locally exchange data. Furthermore, each D2D time slot is divided into $|\mathcal{D}(t)|$ orthogonal D2D transmissions (see Fig. 1). In each D2D transmission, a user $i \in \mathcal{D}(t)$ transmits a coded message denoted by $X_{i}^{\mathrm{D} 2 \mathrm{D}}$ to an intended set of receivers $\mathcal{R}^{\mathcal{D}}(i) \subseteq \mathcal{D}(t)$. Thus, the message $X_{i}^{\text {D2D }}$ can be transmitted at rate $\square^{1}$

$$
R_{i}^{\mathcal{D}}=\min _{k \in \mathcal{R}^{\mathcal{D}}(i)} \log \left(1+\frac{P_{d}\left|h_{i k}\right|^{2}}{N_{0}}\right)
$$

where $P_{d}$ is the user's available transmit power, and $h_{i k} \in \mathbb{C}$ is the channel coefficient between user $i$ and user $k$. Note that in each D2D transmission, a single user in $\mathcal{D}$ multicasts a message to the rest of the group members. Hence, the weakest receiver limits the rate. Furthermore, following [36], each subfile is transmitted in a D2D group $|\mathcal{D}|-1$ times. Therefore,[^1]

![](https://cdn.mathpix.com/cropped/2024_05_09_d8867f52fbc810dc46cag-04.jpg?height=417&width=875&top_left_y=190&top_left_x=164)

Fig. 2. Example 1: D2D enabled downlink beamforming system model, for $K=3, L=2$, and $\tau=1$.

subfiles are further divided into $|\mathcal{D}|-1$ smaller parts for D2D transmissions to ensure fresh content is transmitted.

The D2D subphase is followed by the downlink phase, where the BS multicasts coded messages containing all the remaining file fragments so that all users can decode their requested content. The received downlink signal at user terminal $k \in[K]$ is given by

$$
y_{k}=\mathbf{h}_{k}^{\mathrm{H}} \sum_{\mathcal{T} \subseteq \mathcal{S}} \mathbf{w}_{\mathcal{T}}^{\mathcal{S}} \tilde{X}_{\mathcal{T}}^{\mathcal{S}}+z_{k}
$$

where $\tilde{X}_{\mathcal{T}}^{\mathcal{S}}$ is the multicast message chosen from a unit power complex Gaussian codebook dedicated to all the users in subset $\mathcal{T}$ of set $\mathcal{S} \subseteq[K]$ (provided that subset $\mathcal{T}$ has not been considered in D2D transmissions). The channel vector between the BS and user $k$ is denoted by $\mathbf{h}_{k} \in \mathbb{C}^{L}$, the receiver noise is given by $z_{k} \sim \mathbb{C N}\left(0, N_{0}\right)$, and $\mathbf{w}_{\mathcal{T}}^{\mathcal{S}}$ is the beamforming vector dedicated to $\tilde{X}_{\mathcal{T}}^{\mathcal{S}}$. The channel state information at the transmitter (CSIT) of all $K$ users is assumed to be perfectly known. Finally, the total achievable rate (per user) over the above-described two phases is given by

$$
R_{\mathrm{U}}=\frac{F}{T_{\mathrm{D} 2 \mathrm{D}}+T_{\mathrm{DL}}}
$$

where $T_{\mathrm{D} 2 \mathrm{D}}$ and $T_{\mathrm{DL}}$ denote the transmission time for the D2D and DL sub-phases, respectively.

## III. D2D Aided Beamforming Explained: Example

In this section, we illustrate the main idea of the proposed scheme via two examples. In the first example, we have a network of 3 users, and in the second example, the number of users is increased to 4 .

## A. Example 1: $K=3, N=3, M=1$, and $L=2$

In this example, the network is comprised of $K=3$ users and a library $\mathcal{W}=\{A, B, C\}$ of $N=3$ files, where each user has the cache size $M=1$ file. The base station is equipped with $L=2$ transmit antennas. To begin with, the cache content $Z_{k}$ at each user $k=1, \ldots, K$ is $Z_{1}=\left\{A_{1}, B_{1}, C_{1}\right\}, Z_{2}=$ $\left\{A_{2}, B_{2}, C_{2}\right\}, Z_{3}=\left\{A_{3}, B_{3}, C_{3}\right\}$. Note that each file is divided into three equal-sized sub-files, following the cache placement in [6]. In this example, we assume users 1 and 2 are close to each other (c.f. Fig. 2).
Without loss of generality, assume users 1,2 , and 3 request files $A, B$, and $C$, respectively. Now, the delivery is carried out in two phases. In the first phase, i.e., the D2D phase, users 1 and 2 are assumed to share their local cache content through the D2D transmission. Thus, a single D2D time slot with $\mathcal{D}=\{1,2\}$ exists. It is evident that user 2 would request $B_{1}$ from user 1 , and user 1 would request $A_{2}$ from user 2. The D2D transmission is assumed to be half-duplex, i.e., two uni-directional D2D transmissions are included in each time slot. The time required for the D2D phase is given by $T_{\mathrm{D} 2 \mathrm{D}}=T\left(1 \rightarrow \mathcal{R}^{\mathcal{D}}(1)\right)+T\left(2 \rightarrow \mathcal{R}^{\mathcal{D}}(2)\right)=$ $\frac{F / 3}{R_{1}^{D}}+\frac{F / 3}{R_{2}^{D}}$, where $\mathcal{R}^{\mathcal{D}}(1)=\{2\}, \mathcal{R}^{\mathcal{D}}(2)=\{1\}$, and $R_{1}^{\mathcal{D}}=\log \left(1+\frac{P_{d}\left\|h_{12}\right\|^{2}}{N_{0}}\right), R_{2}^{\mathcal{D}}=\log \left(1+\frac{P_{d}\left\|h_{21}\right\|^{2}}{N_{0}}\right)$. Note that $\frac{F}{3}$ fractions of the requested files are delivered in each transmission

In the second phase (i.e., DL transmission), the BS multicasts the remaining content via coded messages. In the given example, user 3 is not served in the D2D phase and still needs $C_{1}$ and $C_{2}$. However, users 1 and 2 only require $A_{3}$ and $B_{3}$, respectively. These contents are XOR coded over two messages for user pairs $(1,3)$ and $(2,3)$. Namely, the messages are $X_{1,3}=A_{3} \oplus C_{1}$ and $X_{2,3}=B_{3} \oplus C_{2}$. Note that $X_{1,3}$ simultaneously benefits both users 1 and 3 . Similarly, $X_{2,3}$ is a coded message intended for users 2 and 3 . Accordingly, the multicast beamformer vectors $\mathbf{w}_{1,3}$ and $\mathbf{w}_{2,3}$ are associated with messages $X_{1,3}$ and $X_{2,3}$, respectively. The downlink signal is then formed as $\mathbf{x}_{D L}=\tilde{X}_{1,3} \mathbf{w}_{1,3}+\tilde{X}_{2,3} \mathbf{w}_{2,3}$, where $\tilde{X}$ stands for the modulated $X$, chosen from a unit power complex Gaussian codebook [17]. Here, user 3 is assumed to use a successive-interference-cancellation (SIC) receiver to decode both intended messages (interpreted as a multipleaccess-channel (MAC)). In contrast, users 1 and 2 get served with a single message, with the other seen as interference.

Now, assume user 3 can decode both messages $\tilde{X}_{1,3}$ and $\tilde{X}_{2,3}$ with the equal rat $\left.\right|^{2} R_{M A C}^{3}=$ $\min \left(\frac{1}{2} R_{\text {Sum }}^{3}, R_{1}^{3}, R_{2}^{3}\right), \quad$ where the rate region corresponding to $\tilde{X}_{1,3}$ and $\tilde{X}_{2,3}$ is limited by $R_{1}^{3}=\log \left(1+\frac{\left|\mathbf{h}_{3}^{H} \mathbf{w}_{1,3}\right|^{2}}{N_{0}}\right), R_{2}^{3}=\log \left(1+\frac{\left|\mathbf{h}_{3}^{H} \mathbf{w}_{2,3}\right|^{2}}{N_{0}}\right)$, and $R_{\text {Sum }}^{3}=\log \left(1+\frac{\left|\mathbf{h}_{3}^{H} \mathbf{w}_{1,3}\right|^{2}+\left|\mathbf{h}_{3}^{H} \mathbf{w}_{2,3}\right|^{2}}{N_{0}}\right)$. Accordingly, the corresponding downlink beamforming problem can be expressed as $\max _{\mathbf{w}_{2,3}, \mathbf{w}_{1,3}} \min \left(R_{\mathrm{MAC}}^{3}, R_{1}^{1}, R_{1}^{2}\right)$, where the rates of users 1 and 2 are given as

$$
\begin{aligned}
& R_{1}^{1}=\log \left(1+\frac{\left|\mathbf{h}_{1}^{H} \mathbf{w}_{1,3}\right|^{2}}{\left|\mathbf{h}_{1}^{H} \mathbf{w}_{2,3}\right|^{2}+N_{0}}\right) \\
& R_{1}^{2}=\log \left(1+\frac{\left|\mathbf{h}_{2}^{H} \mathbf{w}_{2,3}\right|^{2}}{\left|\mathbf{h}_{2}^{H} \mathbf{w}_{1,3}\right|^{2}+N_{0}}\right)
\end{aligned}
$$

Here, due to D2D transmissions, the beamforming problem differs from the one proposed in [17]. The partial file exchange in the D2D phase allows focusing the available DL power on fewer multicast streams. In addition, it alleviates the DL phase's inter-stream interference conditions, making the DL multicast beamforming more efficient and easier to[^2]

![](https://cdn.mathpix.com/cropped/2024_05_09_d8867f52fbc810dc46cag-05.jpg?height=512&width=876&top_left_y=178&top_left_x=153)

Fig. 3. Example 2: D2D enabled downlink beamforming system model, where $K=4, L=2$, and $\tau=2$.

design (see Section V). On the other hand, the D2D transmission requires an orthogonal allocation in the time domain. This introduces an inherent trade-off between the number of resources allocated to the D2D and DL phases.

Finally, the corresponding symmetric rate maximization is given as

$$
\begin{array}{cl}
\underset{\mathbf{w}_{i, j}, \gamma_{l}^{k}, r}{\max } & r \\
\text { s. t. } & r \leq \frac{1}{2} \log \left(1+\gamma_{1}^{3}+\gamma_{2}^{3}\right), r \leq \log \left(1+\gamma_{1}^{3}\right) \\
& r \leq \log \left(1+\gamma_{2}^{3}\right), r \leq \log \left(1+\gamma_{1}^{1}\right) \\
& r \leq \log \left(1+\gamma_{1}^{2}\right), \gamma_{1}^{1} \leq \frac{\left|\mathbf{h}_{1}^{H} \mathbf{w}_{1,3}\right|^{2}}{\left|\mathbf{h}_{1}^{\mathrm{H}} \mathbf{w}_{2,3}\right|^{2}+N_{0}} \\
& \gamma_{1}^{2} \leq \frac{\left|\mathbf{h}_{2}^{H} \mathbf{w}_{2,3}\right|^{2}}{\left|\mathbf{h}_{2}^{H} \mathbf{w}_{1,3}\right|^{2}+N_{0}}, \gamma_{1}^{3} \leq \frac{\left|\mathbf{h}_{3}^{H} \mathbf{w}_{1,3}\right|^{2}}{N_{0}} \\
& \gamma_{2}^{3} \leq \frac{\left|\mathbf{h}_{3}^{\mathrm{w}} \mathbf{w}_{2,3}\right|^{2}}{N_{0}},\left\|\mathbf{w}_{1,3}\right\|^{2}+\left\|\mathbf{w}_{2,3}\right\|^{2} \leq P_{T}
\end{array}
$$

Where $P_{T}$ is the total available power at the $\mathrm{BS}$. The rate constraints can be written as a convex second-order cone problem as shown in [17]. However, the signal-to-interferenceplus-noise ratio (SINR) constraints are non-convex and require an iterative solution. A successive convex approximation (SCA) solution for the SINR constraints can be found, e.g., in [17]. Please notice that, here, due to D2D transmission in the first phase, we have only two beamformer vectors ( $\mathbf{w}_{1,3}$ and $\mathbf{w}_{2,3}$ ), which means we can dedicate more power to our intended signals ( $X_{1,3}$ and $X_{2,3}$ ) compared to [17]. The time required for the DL phase is given by $T_{\mathrm{DL}}=\frac{F / 3}{r}=$ $\frac{F / 3}{\max _{\mathbf{w}_{2,3}, \mathbf{w}_{1,3}} \min \left(R_{\mathrm{MAc}}^{3}, R_{1}^{1}, R_{1}^{2}\right)}$. Here, similar to the first phase, all users are served with coded messages of size $\frac{F}{3}$ bits. Finally, the achievable rate over the D2D and DL phases is given in 3 .

## B. Example 2: $K=4, N=4, M=2$, and $L=2$

In this example, we consider a scenario where $K=4$ users and a library $\mathcal{W}=\{A, B, C, D\}$ of $N=4$ files, and each user has a cache for storing $M=2$ files. Also, the base station is equipped with $L=2$ transmit antennas. Following the cache placement in $[6]$, each file is split into $\binom{K}{\tau}=\binom{4}{2}=6$ subfiles as follows

$$
\begin{aligned}
& A=\left\{A_{1,2}, A_{1,3}, A_{1,4}, A_{2,3}, A_{2,4}, A_{3,4}\right\} \\
& B=\left\{B_{1,2}, B_{1,3}, B_{1,4}, B_{2,3}, B_{2,4}, B_{3,4}\right\} \\
& C=\left\{C_{1,2}, C_{1,3}, C_{1,4}, C_{2,3}, C_{2,4}, C_{3,4}\right\} \\
& D=\left\{D_{1,2}, D_{1,3}, D_{1,4}, D_{2,3}, D_{2,4}, D_{3,4}\right\}
\end{aligned}
$$

Each file $W_{\mathcal{T}}$ is cached at user $k$ if $k \in \mathcal{T}$. Let us assume that users $1-4$ request files $A-D$, respectively.

In this example, we assume users 1,2 , and 3 are close to each other, while user 4 is far from them as illustrated in Fig. 3 Then, during this phase, the first three users (collected in $\mathcal{D}=\{1,2,3\}$ ) locally exchange content in three orthogonal D2D transmissions. Following [36], each subfile is further divided into $|\mathcal{D}(t)|-1=2$ fragments, discriminated by their superscript indices. Then, in the first D2D transmission of length $T\left(1 \rightarrow \mathcal{R}^{\mathcal{D}}(1)\right)$ seconds, user 1 multicasts $X_{1}^{D 2 D}=B_{1,3}^{1} \oplus C_{1,2}^{1}$ to $\mathcal{R}^{\mathcal{D}}(1)=\{2,3\}$. In the second D2D transmission, user 2 transmits $X_{2}^{D 2 D}=A_{2,3}^{1} \oplus C_{1,2}^{2}$ to $\mathcal{R}^{\mathcal{D}}(2)=\{1,3\}$, which will take $T\left(2 \rightarrow \mathcal{R}^{\mathcal{D}}(2)\right)$ seconds. Finally, in the third D2D transmission of length $T\left(3 \rightarrow \mathcal{R}^{\mathcal{D}}(3)\right)$ seconds, user 3 transmits $X_{3}^{D 2 D}=A_{2,3}^{2} \oplus B_{1,3}^{2}$ to $\mathcal{R}^{\mathcal{D}}(3)=$ $\{1,2\}$. These transmissions require the total time of $T_{D 2 D}=$ $T\left(1 \rightarrow \mathcal{R}^{\mathcal{D}}(1)\right)+T\left(2 \rightarrow \mathcal{R}^{\mathcal{D}}(2)\right)+T\left(3 \rightarrow \mathcal{R}^{\mathcal{D}}(3)\right)$, in which $T\left(i \rightarrow \mathcal{R}^{\mathcal{D}}(i)\right)=\frac{F / 12}{R_{i}^{\mathcal{D}}}, \quad i=1,2,3$ and $R_{i}^{\mathcal{D}}, i=$ $1,2,3$ is given in (1).

In the DL phase, the BS transmits a message comprised of the remaining subfiles $\mathbf{x}_{D L}=\tilde{X}_{1,2,4} \mathbf{w}_{1,2,4}+\tilde{X}_{1,3,4} \mathbf{w}_{1,3,4}+$ $\tilde{X}_{2,3,4} \mathbf{w}_{2,3,4}$, where $X_{1,2,4}=A_{2,4} \oplus B_{1,4} \oplus D_{1,2}, X_{1,3,4}=$ $A_{3,4} \oplus C_{1,4} \oplus D_{1,3}$, and $X_{2,3,4}=B_{3,4} \oplus C_{2,4} \oplus D_{2,3} 3$, and $\tilde{X}_{\mathcal{T}}$ is the modulated version of $X_{\mathcal{T}}$. At the end of this phase, user 1 is interested in decoding $\left\{X_{1,2,4}, X_{1,3,4}\right\}$, user 2 is interested in decoding $\left\{X_{1,2,4}, X_{2,3,4}\right\}$, user 3 is interested in decoding $\left\{X_{1,3,4}, X_{2,3,4}\right\}$, and, user 4 is interested in decoding all the three terms $\left\{X_{1,2,4}, X_{1,3,4}, X_{2,3,4}\right\}$. Thus, from the perspective of users 1,2 , and 3 , there exists a MAC channel with two useful terms and one interference term. However, from the perspective of the user 4 , there exists a MAC channel with three useful terms. In this regard, for users 1,2 , and 3 the MAC rate region is given as $R_{\mathrm{MAC}}^{k}=\min \left(\frac{1}{2} R_{\text {sum }}^{k}, R_{1}^{k}, R_{2}^{k}\right), k=$ $1,2,3$. For instance, for user 1 , we have $R_{1}^{1}=$ $\log \left(1+\frac{\left|\mathbf{h}_{1}^{H} \mathbf{w}_{1,2,4}\right|^{2}}{\left|\mathbf{h}_{1}^{H} \mathbf{w}_{2,3,4}\right|^{2}+N_{0}}\right), R_{2}^{1}=\log \left(1+\frac{\left|\mathbf{h}_{1}^{H} \mathbf{w}_{1,3,4}\right|^{2}}{\left|\mathbf{h}_{1}^{H} \mathbf{w}_{2,3,4}\right|^{2}+N_{0}}\right)$, and $R_{\text {sum }}^{1}=\log \left(1+\frac{\left|\mathbf{h}_{1}^{\mathrm{H}} \mathbf{w}_{1,2,4}\right|^{2}+\left|\mathbf{h}_{1}^{\mathrm{H}} \mathbf{w}_{1,3,4}\right|^{2}}{\left|\mathbf{h}_{1}^{\mathrm{H}} \mathbf{w}_{2,3,4}\right|^{2}+N_{0}}\right)$.

To derive the fourth user's rate region, we face a MAC with three messages. Thus, we have 7 MAC region inequalities, which will result in $R_{\mathrm{MAC}}^{4}$. Then, the corresponding rate[^3]constraints for the MAC channel are listed below

$$
\begin{aligned}
& R_{1}^{4}=\log \left(1+\frac{\left|\mathbf{h}_{4}^{\mathrm{H}} \mathbf{w}_{1,2,4}\right|^{2}}{N_{0}}\right), R_{2}^{4}=\log \left(1+\frac{\left|\mathbf{h}_{4}^{\mathrm{H}} \mathbf{w}_{1,3,4}\right|^{2}}{N_{0}}\right) \\
& R_{3}^{4}=\log \left(1+\frac{\left|\mathbf{h}_{4}^{\mathrm{H}} \mathbf{w}_{2,3,4}\right|^{2}}{N_{0}}\right) \\
& R_{1,2}^{4}=\log \left(1+\frac{\left|\mathbf{h}_{4}^{\mathrm{H}} \mathbf{w}_{1,2,4}\right|^{2}+\left|\mathbf{h}_{4}^{\mathrm{H}} \mathbf{w}_{1,3,4}\right|^{2}}{N_{0}}\right) \\
& R_{1,3}^{4}=\log \left(1+\frac{\left|\mathbf{h}_{4}^{\mathrm{H}} \mathbf{w}_{1,2,4}\right|^{2}+\left|\mathbf{h}_{4}^{\mathrm{H}} \mathbf{w}_{2,3,4}\right|^{2}}{N_{0}}\right) \\
& R_{2,3}^{4}=\log \left(1+\frac{\left|\mathbf{h}_{4}^{\mathrm{H}} \mathbf{w}_{1,3,4}\right|^{2}+\left|\mathbf{h}_{4}^{\mathrm{H}} \mathbf{w}_{2,3,4}\right|^{2}}{N_{0}}\right) \\
& R_{1,2,3}^{4}=\log \left(1+\frac{\left|\mathbf{h}_{4}^{\mathrm{H}} \mathbf{w}_{1,2,4}\right|^{2}+\left|\mathbf{h}_{4}^{\mathrm{H}} \mathbf{w}_{1,3,4}\right|^{2}+\left|\mathbf{h}_{4}^{\mathrm{H}} \mathbf{w}_{2,3,4}\right|^{2}}{N_{0}}\right)
\end{aligned}
$$

Thus, the MAC rate region for user 4 is expressed as follows

$$
R_{\mathrm{MAC}}^{4}=\min \left(\frac{1}{3} R_{1,2,3}^{4}, \frac{1}{2} R_{1,2}^{4}, \frac{1}{2} R_{1,3}^{4}, \frac{1}{2} R_{2,3}^{4}, R_{1}^{4}, R_{2}^{4}, R_{3}^{4}\right)
$$

When all the MAC inequalities for all the users are considered together, the common multicast rate is driven as follows

$$
\begin{aligned}
& \max _{, \gamma^{k}} \eta \\
& \begin{array}{l}
\text { subiect to } \\
\text { sub, }
\end{array} \\
& r \leq \frac{1}{2} \log \left(1+\gamma_{1}^{k}+\gamma_{2}^{k}\right), k=1,2,3 \\
& r \leq \log \left(1+\gamma_{m}^{k}\right), k=1,2,3, m=1,2 \\
& r \leq \frac{1}{3} \log \left(1+\gamma_{1}^{4}+\gamma_{2}^{4}+\gamma_{3}^{4}\right), r \leq \frac{1}{2} \log \left(1+\gamma_{1}^{4}+\gamma_{2}^{4}\right), \\
& r \leq \frac{1}{2} \log \left(1+\gamma_{1}^{4}+\gamma_{3}^{4}\right), r \leq \frac{1}{2} \log \left(1+\gamma_{2}^{4}+\gamma_{3}^{4}\right) \\
& r \leq \log \left(1+\gamma_{m}^{4}\right), m=1,2,3 \\
& \gamma_{1}^{1} \leq \frac{\left|\mathbf{H}_{1}^{\mathrm{H}} \mathbf{w}_{1,2,4}\right|^{2}}{\left|\mathbf{h}_{1}^{\mathrm{H}} \mathbf{w}_{2}, 3,4\right|^{2}+N_{0}}, \gamma_{2}^{1} \leq \frac{\left|\mathbf{h}_{1}^{\mathrm{H}} \mathbf{w}_{1,3,3}\right|^{2}}{\left|\mathbf{h}_{1}^{\mathrm{H}} \mathbf{w}_{2,3,4}\right|^{2}+N_{0}}, \\
& \gamma_{1}^{2} \leq \frac{\left|\mathbf{h}_{2}^{H} \mathbf{w}_{1,2,4}\right|^{2}}{\left|\mathbf{h}_{2}^{H} \mathbf{w}_{1,3,4}\right|^{2}+N_{0}}, \gamma_{2}^{2} \leq \frac{\left|\mathbf{h}_{2}^{H} \mathbf{w}_{2,3,4}\right|^{2}}{\left|\mathbf{h}_{2}^{H} \mathbf{w}_{1,3,4}\right|^{2}+N_{0}}, \\
& \gamma_{1}^{3} \leq \frac{\left|\mathbf{h}_{3}^{\mathrm{H}} \mathbf{w}_{1,3,4}\right|^{2}}{\left|\mathbf{h}_{3}^{\mathrm{H}} \mathbf{w}_{1,2,4}\right|^{2}+N_{0}}, \gamma_{2}^{3} \leq \frac{\left|\mathbf{h}_{3}^{\mathrm{H}} \mathbf{w}_{2,3,4}\right|^{2}}{\left|\mathbf{h}_{3, \mathbf{w}}^{\mathrm{H}} \mathbf{w}_{1,2,4}\right|^{2}+N_{0}} \\
& \gamma_{1}^{4} \leq\left|\mathbf{h}_{4}^{\mathrm{H}} \mathbf{w}_{1,2,4}\right|^{2} / N_{0}, \gamma_{2}^{4} \leq\left|\mathbf{h}_{4}^{\mathrm{H}} \mathbf{w}_{1,3,4}\right|^{2} / N_{0}, \\
& \gamma_{3}^{4} \leq\left|\mathbf{h}_{4}^{\mathrm{H}} \mathbf{w}_{2,3,4}\right|^{2} / N_{0}, \\
& \left\|\mathbf{w}_{1,2,4}\right\|^{2}+\left\|\mathbf{w}_{1,3,4}\right\|^{2}+\left\|\mathbf{w}_{2,3,4}\right\|^{2} \leq P_{T}
\end{aligned}
$$

Finally, the delivery time of the DL phase is $T_{\mathrm{DL}}=\frac{F / 6}{r}$.

It should be noted that compared to [17], one term is removed from the DL transmission herein, i.e., $\tilde{X}_{1,2,3} \mathbf{w}_{1,2,3}$. We have taken care of this term in the D2D phase, enhancing the performance of the DL phase for two reasons. First, since we removed one term from DL transmission, the transmit power is shared by fewer beamformers. Second, since one term is removed, the number of conditions in the optimization problem is less than [17]. This will reduce the complexity of the optimization problem as discussed in Sec. $\mathrm{V}$

## C. Example 2: D2D group sizes less than $\tau+1$

So far, based on the scheme proposed in [36], we have considered D2D group size $|\mathcal{D}|=\tau+1=3$. However, given the scenario presented in Fig. 33, there are still some useful contents in the cache of the three users, which can be shared among them in D2D groups of size $|\mathcal{D}|=2$, i.e., $\mathcal{D}(1)=\{1,2\}, \mathcal{D}(2)=\{1,3\}, \mathcal{D}(3)=\{2,3\}$. In this regard, user 1 transmits $B_{1,4}$ and $C_{1,4}$ to users 2 and 3 , user 2 transmits $A_{2,4}$ and $C_{2,4}$ to users 1 and 3 , and user 3 transmits $A_{3,4}$ and $B_{3,4}$ to users 1 and 2 , respectively. Therefore, compared to section III-B six more time slots are needed in the D2D phase in this case, where the transmission scheme is similar to section III-A Then, since user 4 has not received any data in the D2D phase, it still needs to receive all three missing subfiles through DL transmission. On the other hand, users 1,2 , and 3 have received all the missing data through D2D transmissions. Thus, the downlink transmission is changed to $\mathbf{x}_{D L}=\tilde{X}_{1,2,4} \mathbf{w}_{1,2,4}+\tilde{X}_{1,3,4} \mathbf{w}_{1,3,4}+\tilde{X}_{2,3,4} \mathbf{w}_{2,3,4}$, where $\tilde{X}_{1,2,4}=D_{1,2}, \tilde{X}_{1,3,4}=D_{1,3}$, and $\tilde{X}_{2,3,4}=D_{2,3}$. The rate expression can be formulated similar to (4) with seven MAC conditions comprised of $\gamma_{1}^{4}, \gamma_{2}^{4}$, and $\gamma_{3}^{4}$. However, since the BS only serves one user in this special case, the DL phase can be simplified to unicast transmission. To this end, the DL message can be expressed as $\hat{\mathbf{x}}_{D L}=\mathbf{w}_{4} \tilde{X}_{4}$, where $\tilde{X}_{4}=\left[D_{1,2}, D_{1,3}, D_{2,3}\right]$ is the concatenated version of the three missing parts with the total size of $\frac{F}{2}$ bits. Then, the corresponding beamformer can be expressed as a maximum ratio transmitter (MRT), i.e., $\mathbf{w}_{4}^{*}=\frac{\mathbf{h}_{4} P_{T}}{\left|\mathbf{h}_{4}\right|}$. Note that, though the number of messages in the $\mathbf{x}_{D L}$ (in this case) remains the same as in Section III-B, the complexity of the beamformer design is greatly reduced. As a result, the rate for DL transmission is further enhanced, which in turn leads to a potential reduction of the total transmission time.

## IV. D2D Aided Beamforming: The General CaSE

In this section, we formulate and analyze the proposed scheme in the general setting. We first consider D2D group size $|\mathcal{D}|=\tau+1$, then in section IV-D, we extend the results to group sizes smaller than $\tau+1$. The cache placement phase is identical to the one proposed in [6]. In general, similar to [17], $\min (\tau+L, K)$ users are served in each data transmission. However, in our proposed scheme, the data is delivered over separate D2D and DL phases.

Before the delivery process, an exhaustive search among the D2D subsets is required to find the potential D2D groups for the first phase. However, since there are $\binom{\tau+L}{\tau+1}$ different D2D subsets (of size $\tau+1$ ) among $\tau+L$ number of users, the exhaustive search would require $2^{\binom{\tau+1}{\tau+1}}$ evaluations of (3). Moreover, all the beamformers must be solved in each of these evaluations, and the total rate must be computed. Then, the case with the lowest delivery time is selected. However, this is practically infeasible due to the significant overhead. Thus, to reduce the computational burden, a less complex heuristic mode selection method is introduced in Section IV-B To simplify the notation, we consider an indicator function $I_{D 2 D}(\mathcal{D})$, which specifies whether the corresponding subset has been allocated for D2D transmission. Moreover, we denote $C(K, \tau, L)=\frac{F}{\binom{K}{\tau}\binom{K-(\tau+1)}{L-1}}$ as the size of the transmitted subfiles [17].

## A. Total delivery time $T_{\mathrm{D} 2 \mathrm{D}}+T_{\mathrm{DL}}$

First, the D2D delivery time for a given selection of D2D subsets is given as

$$
T_{\mathrm{D} 2 \mathrm{D}}=\sum_{\mathcal{D} \subseteq \overline{\Omega^{S}}} \sum_{k \in \mathcal{D}} \frac{\frac{C(K, \tau, L)}{(|\mathcal{D}|-1)}}{R_{k}^{\mathcal{D}}}
$$

where $\overline{\Omega^{\mathcal{S}}}:=\left\{\mathcal{D} \subseteq \mathcal{S},|\mathcal{D}|=\tau+1, I_{\mathrm{D} 2 \mathrm{D}}(\mathcal{D})=1\right\}$, and $R_{k}^{\mathcal{D}}$ is given in 11. Since in each D2D subset, each user transmit a $\frac{1}{|\mathcal{D}|-1}$ fraction of a subfile, the corresponding data size in each D2D transmission is $\frac{C(K, \tau, L)}{(|\mathcal{D}|-1)}$ (see section III-B.

Next, the DL beamforming is done using the SCA approach proposed in [17]. Compared to [17], we do not consider all the $\tau+1$ subsets. Here, subsets $\mathcal{D}$ for which $I_{\text {D2D }}(\mathcal{D})=$ 0 is considered in the DL phase, reducing the interference among parallel streams significantly. The DL phase throughput is given by

$$
\begin{aligned}
& R_{C}\left(\mathcal{S},\left\{\mathbf{w}_{\mathcal{D}}^{\mathcal{S}}, \mathcal{D} \subseteq \mathcal{S},|\mathcal{D}|=\tau+1, I_{D 2 D}(\mathcal{D})=0\right\}\right)= \\
& \quad \max _{\left\{\mathbf{w}_{\mathcal{D}}^{\mathcal{S}}\right\}} \min _{k \in \mathcal{S}} R_{M A C}^{k}\left(\mathcal{S},\left\{\mathbf{w}_{\mathcal{D}}^{\mathcal{S}}, \mathcal{D} \subseteq \mathcal{S}, I_{\mathrm{D} 2 \mathrm{D}}(\mathcal{D})=0\right\}\right)
\end{aligned}
$$

and

$$
\begin{aligned}
& R_{M A C}^{k}\left(\mathcal{S},\left\{\mathbf{w}_{\mathcal{D}}^{\mathcal{S}}, \mathcal{D} \subseteq \mathcal{S}, I_{\mathrm{D} 2 \mathrm{D}}(\mathcal{D})=0\right\}\right) \\
= & \min _{\mathcal{B} \subseteq \Omega_{k}^{\mathcal{S}}}\left[\frac{1}{|\mathcal{B}|} \log \left(1+\frac{\sum_{\mathcal{D} \in \mathcal{B}}\left|\mathbf{h}_{k}^{H} \mathbf{w}_{\mathcal{D}}^{\mathcal{S}}\right|^{2}}{N_{0}+\sum_{\mathcal{D}^{\prime} \in \mathcal{I}_{k}}\left|\mathbf{h}_{k}^{\mathrm{H}} \mathbf{w}_{\mathcal{D}^{\prime}}^{\mathcal{S}}\right|^{2}}\right)\right]
\end{aligned}
$$

where $\mathcal{I}_{k}=\Omega^{\mathcal{S}} \backslash \Omega_{k}^{\mathcal{S}}:=\left\{\mathcal{D} \subseteq \mathcal{S}:|\mathcal{D}|=\tau+1, I_{\mathrm{D} 2 \mathrm{D}}(\mathcal{D})=\right.$ $0 \mid k \notin \mathcal{D}\}$ is the set of interfering messages at user $k$. Denote $\Omega^{\mathcal{S}}:=\left\{\mathcal{D} \subseteq \mathcal{S},|\mathcal{D}|=\tau+1, I_{\mathrm{D} 2 \mathrm{D}}(\mathcal{D})=0\right\}$ as the set of all the user subsets (of size $\tau+1$ ) that will be served in the DL phas $\triangleleft^{4}$, where the cardinality $\left|\Omega^{\mathcal{S}}\right|$ indicates the total number of messages delivered by the BS. Finally, let $\Omega_{k}^{\mathcal{S}}:=\left\{\mathcal{D} \subseteq \mathcal{S},|\mathcal{D}|=\tau+1, I_{\mathrm{D} 2 \mathrm{D}}(\mathcal{D})=0 \mid k \in \mathcal{D}\right\}$ denote the set of all the subsets in which user $k$ exists (i.e., the set of all the messages required by user $k$ ).

After computing the rate for the DL phase, $T_{\mathrm{DL}}$ is given as $T_{\mathrm{DL}}=\frac{C(K, \tau, L)}{R_{C}}$, while the symmetric delivery rate is given in (3). Note that solving (6) requires considerable computation due to the iterative convex approximation process and many constraints. Moreover, the exhaustive search would require computing (5) and (6) for each D2D subset evaluation. Therefore, considering the total number of different D2D mode allocations (i.e., different combinations of subsets) and the complexity of computing (6) for each of these modes, the exhaustive search becomes impractical for large networks. Therefore, in the following, we provide a low-complexity heuristic solution for the proposed mode assessment problem.

## B. Heuristic D2D mode selection with low complexity

To decrease the computational load of evaluating $T_{\mathrm{D} 2 \mathrm{D}}$ and $T_{\mathrm{DL}}$ for different $\mathrm{D} 2 \mathrm{D}$ mode allocations, we provide a throughput approximation for the D2D mode allocations without relying on the general SCA solution for the DL beamformer design. On the one hand, due to the orthogonal D2D and DL phases, each D2D content exchange between users adds extra time for delivering the content locally. On the other hand, each successful D2D transmission reduces the remaining number of subfiles to be transmitted by the BS. Therefore, there are fewer multicast messages and corresponding beamforming vectors $\mathbf{w}_{\mathcal{D}}^{\mathcal{S}}$ in the DL optimization problem.

${ }^{4}$ In Example $2, \Omega^{\mathcal{S}}=\{\{1,2,4\},\{1,3,4\},\{2,3,4\}\}$ and $\left|\Omega^{\mathcal{S}}\right|=3$.
As a result, a more efficient (less constrained) multicast beamformer design is possible, reducing the DL phase duration $T_{\mathrm{DL}}$. Therefore, the D2D mode selection is iteratively carried out as long as the following condition holds:

$$
\frac{\hat{T}_{\mathrm{DL}}^{i}}{N_{s}^{i}} \geq \hat{T}_{\mathrm{D} 2 \mathrm{D}}^{i}, \quad i \in\left[1,\binom{\tau+L}{\tau+1}\right]
$$

where $N_{s}^{i}=(\tau+1)\left(\binom{\tau+L}{\tau+1}-(i-1)\right)$ is the number of subfiles that is delivered in the DL phase assuming $i$ D2D subsets are selected. Moreover, $\hat{T}_{\mathrm{DL}}^{i}$ and $\hat{T}_{\mathrm{D} 2 \mathrm{D}}^{i}$ are the coarse approximated delivery times in the $i^{\text {th }}$ iteration.

In (8), we check if any D2D user subset will reduce the DL duration $T_{\mathrm{DL}}$ more than the added D2D duration. Note that in each D2D time slot, $|\mathcal{D}|=\tau+1$ subfiles are delivered through $\tau+1$ orthogonal D2D transmissions. On the other hand, all the remaining subfiles (i.e., $N_{s}^{i}$ subfiles) are delivered simultaneously in the DL phase. Thus, in (8), the average delivery time for a single subfile in the D2D and DL phases is compared. To this end, we divide the total approximated DL time $\left(\hat{T}_{\mathrm{DL}}^{i}\right)$ by the number of subfiles $\left(N_{s}^{i}\right)$, approximating the average transmission time for a single subfile. Thus, the average D2D transmission time for a subfile must be less than the corresponding average DL transmission time. In each iteration, we set a subset as a D2D candidate, i.e., the subset which provides the lowest delivery time. If a specific subset $\mathcal{D}$ in iteration $i$ satisfies (8), we set $I_{\mathrm{D} 2 \mathrm{D}}(\mathcal{D})=1$ for this subset, and the D2D transmission is done as in [36]. If (8) does not hold at any specific iteration, using more D2D transmissions will not improve the rate, and the iterative process is terminated. Therefore, at most, $\binom{\tau+L}{\tau+1}$ iterations are required for the proposed iterative process, while $2^{\binom{\tau+L}{\tau+1}}$ iterations are needed for the exhaustive search.

The D2D delivery time is coarsely approximated as

$$
\hat{T}_{\mathrm{D} 2 \mathrm{D}}^{i}=\min _{\mathcal{D} \subseteq \Omega^{\mathcal{s}}} \frac{1}{|\mathcal{D}|} \sum_{k \in \mathcal{D}} \frac{\frac{C(K, \tau, L)}{|\mathcal{D}|-1}}{R_{k}^{\mathcal{D}}}
$$

In each D2D transmission (see Fig. 1p, $\frac{1}{|\mathcal{D}|-1}$ fractions of each subfile (of size $C(K, \tau, L)$ ) are delivered by user $k \in \mathcal{D}$ at the rate $R_{k}^{\mathcal{D}}$. Moreover, in each D2D subset, $|\mathcal{D}|=\tau+1$ subfiles are delivered. Thus, in (9), the total required time is divided by $|\mathcal{D}|$ to compute the average delivery time for a single subfile. Note that for each iteration $i$, we only consider those subsets that have not yet been allocated for D2D transmissions.

To approximate $T_{\mathrm{DL}}$, we make the following assumptions. First, we assume the beamformer $\mathbf{w}_{\mathcal{D}}^{\mathcal{S}}$ can remove all the interference for user $k \in \mathcal{D}$. Thus, we may assume $\mathcal{I}_{k}=\emptyset$, $\forall k \in \mathcal{S}$ in (7). Second, we assume the beamformer $\mathbf{w}_{\mathcal{D}}^{\mathcal{S}}$ in (7) is matched to the channels of all the users in subset $\mathcal{D}$, i.e., the received SNR for $\hat{X}_{\mathcal{D}}^{\mathcal{S}}$ at receiver $k$ is $\mathrm{SNR}_{\mathcal{D}}^{k}=\frac{\left\|\mathbf{h}_{k}\right\|^{2} \mathrm{P}_{\mathcal{D}}}{N_{0}}$. Note that the beamformer $\mathbf{w}_{\mathcal{D}}^{\mathcal{S}}$ is designed such that all the users in subset $\mathcal{D}$ can decode the message $\hat{X}_{\mathcal{D}}^{\mathcal{S}}$. Thus, to reflect this, we make use of the user's channel gain for the heuristic mode selection process and limit the rate to the weakest user $\left[^{5}\right.$ Thus,[^4]the DL delivery time is coarsely approximated as

$$
\hat{T}_{\mathrm{DL}}^{i}=\frac{C(K, \tau, L)}{\min _{k \in[\mathcal{S}]} \frac{1}{\left|\Omega_{k}^{S}\right|} \log \left(1+\frac{\left\|\mathbf{h}_{k}\right\|^{2}}{N_{0}} \sum_{\mathcal{D} \subseteq \Omega_{k}^{s}} \mathbf{P}_{\mathcal{D}}\right)}
$$

where $\mathrm{P}_{\mathcal{D}}$ is the dedicated power to the message $\hat{X}_{\mathcal{D}}^{\mathcal{S}}$. Denote $\hat{R}_{k}^{i} \triangleq \frac{1}{\left|\Omega_{k}^{S}\right|} \log \left(1+\frac{\left\|\mathbf{h}_{k}\right\|^{2}}{N_{0}} \sum_{\mathcal{D} \subseteq \Omega_{k}^{S}} \mathbf{P}_{\mathcal{D}}\right)$ as the approximated rate of user $k$ assuming $i-1$ subsets have been chosen for D2D transmission. Note that $\hat{R}_{k}^{i}$ can be interpreted as the achievable rate of equivalent single-user MISO MAC channel with several (i.e., $\left|\Omega_{k}^{\mathcal{S}}\right|$ ) useful terms and no interference.

To reflect the max-min objective in (6), we assume the power is divided among different messages such that minimum received SNR for any two different messages are equal, i.e., $\min _{i \in \mathcal{U}}\left\|\mathbf{h}_{i}\right\|^{2} \frac{\mathrm{P}_{\mathcal{U}}}{N_{0}}=\min _{j \in \mathcal{D}}\left\|\mathbf{h}_{j}\right\|^{2} \frac{\mathrm{P}_{\mathcal{D}}}{N_{0}}, \forall\{\mathcal{D}, \mathcal{U}\} \in \Omega^{\mathcal{S}}, \mathcal{D} \neq$ $\mathcal{U}$. Accordingly, the closed-form solution for $P_{\mathcal{D}}$ is given as follows

$$
\mathrm{P}_{\mathcal{D}}=\frac{\prod_{\mathcal{U} \subseteq \Omega^{\mathcal{s}} / \mathcal{D}} \min _{k \in \mathcal{U}}\left\|\mathbf{h}_{k}\right\|^{2} P_{T}}{\sum_{\mathcal{V} \subseteq \Omega^{\mathcal{S}}} \prod_{\mathcal{U} \subseteq \Omega^{\mathcal{S}} / \mathcal{V}} \min _{i \in \mathcal{U}}\left\|\mathbf{h}_{i}\right\|^{2}}, \quad \forall \mathcal{D} \in \Omega^{\mathcal{S}}
$$

It is worth mentioning that when users experience similar channel conditions, the power allocated to each message can be assumed to be almost equal; therefore, (10) can be simplified to the approximated DL time in [45], i.e.,

$$
\hat{T}_{\mathrm{DL}}^{i} \sim \frac{C(K, \tau, L)}{\min _{k \in[\mathcal{S}]} \frac{1}{\left|\Omega_{k}^{\mathcal{S}}\right|} \log \left(1+\frac{\left|\Omega_{k}^{S}\right|\left\|\mathbf{h}_{k}\right\|^{2} P_{T}}{\left|\Omega^{S}\right| N_{0}}\right)}
$$

Once the user subsets for the D2D phase are selected, the final delivery time/rate is computed as in Section IV-A Note that when $I_{D 2 D}(\mathcal{D})=1$, the coded message corresponding to subset $\mathcal{D}$ is already delivered in the D2D phase. Thus, we can ignore such a subset in the DL phase, resulting in less intermessage interference and lower DL delivery time than [17]. Finally, the complete algorithm for the proposed two-phase delivery scheme is given in Algorithm 1 .

Remark 1: The proposed D2D/DL mode selection in Algorithm 1 is based on instantaneous channel knowledge and does not need any previous data history to approximate $\hat{T}_{\text {D2D }}$ or $\hat{T}_{\mathrm{DL}}$. However, the time approximation proposed in this work can be further improved by collecting statistics about users' channel conditions over a period and applying ML tools to approximate the D2D and DL transmission times.

## C. Heuristic D2D mode selection for restricted DoF

The proposed iterative D2D mode selection can be extended to the system setting with restricted DoF [17]. The authors in [17] propose limiting the DoF by serving $\tau+\alpha(\alpha \leq L)$ users at each transmission phase, resulting in a less complex beamformer design. Furthermore, they divide the users into $P$ distinct groups (for some $P \in \mathbb{N}$ ) to decrease the number of overlapping groups (c.f. [17]). The combination of D2D and DL transmissions proposed in this paper also applies to the $\alpha<L$ case. The difference is that the total number of different D2D subsets changes from $\binom{\tau+L}{\tau+1}$ to $P\binom{\tau+\beta}{\tau+1}$, where $\beta \triangleq \frac{\tau+\alpha}{P}-\tau$ is an integer. Accordingly, $\Omega^{\mathcal{S}}, \Omega_{k}^{\mathcal{S}}$, and $C(K, \tau, L)$ change to the ones defined in [17], and the process remains the same. This paper is a particular case of the system proposed in [17] where $P=1$, and $\alpha=\beta=L$.

## D. D2D aided beamforming for general group sizes

In this section, we extend the results in sections IV-A and $\mathrm{IV}-\mathrm{B}$ to general D2D group sizes. Let us define a new set $\Omega^{\mathcal{S}, \mathcal{V}}:=\left\{\mathcal{V} \subseteq \mathcal{S}, 2 \leq|\mathcal{V}| \leq \tau+1, I_{\text {D2D }}(\mathcal{V})=1\right\}$ as the set of D2D groups (of any size) selected for D2D phase. Now, for a given D2D subset selection, the $T_{\mathrm{D} 2 \mathrm{D}}$ is computed as the following

$$
T_{\mathrm{D} 2 \mathrm{D}}=\sum_{\mathcal{V} \subseteq \overline{\Omega^{S, \mathcal{V}}}} \sum_{k \in \mathcal{V}} \frac{\frac{a_{k}^{\mathcal{V}} C(K, \tau, L)}{(|\mathcal{V}|-1)}}{R_{k}^{\mathcal{V}}}
$$

where $a_{k}^{\mathcal{V}}$ is the number of transmitted messages by user $k \in$ $\mathcal{V}$. Please note that though $a_{k}^{\mathcal{V}}=1$ for $|\mathcal{V}|=\tau+1, a_{k}^{\mathcal{V}}$ can be any number for $|\mathcal{V}|<\tau+1$. The corresponding DL rate $\left(R_{C}\right)$ for the general group sizes is computed using (6). The heuristic mode selection criteria (8) changes as follows

$$
\frac{\hat{T}_{\mathrm{DL}}^{i}}{N_{v}^{i}} \geq \hat{T}_{\mathrm{D} 2 \mathrm{D}}^{i}, \quad i \in\left[1, \sum_{j=2}^{\tau+1}\binom{\tau+L}{j}\right]
$$

where $N_{v}^{i}$ is the total number of remaining subfiles delivered through DL transmission in the $i$ 'th iteration. Here, we first check the subsets of size $|\mathcal{V}|=\tau+1$ using (9); after all the subsets of size $|\mathcal{V}|=\tau+1$ are checked, we continue the procedure for $2 \leq|\mathcal{V}|<\tau+1$. We use the same approximation for $\hat{T}_{\mathrm{DL}}^{i}$ and $\hat{T}_{\mathrm{D} 2 \mathrm{D}}^{i}$ given in (9) and (10), respectively. However, for general group sizes, each transmitted message $\hat{X}_{\mathcal{D}}^{\mathcal{S}}$ in the DL phase may not be useful for all $k \in \mathcal{D}$ (some users in $\mathcal{D}$ may have received the transmitted useful term in D2D mode). Thus, in (11), the minimum is taken over those users who still need the message.

Similar to section IV-B, the D2D subset selection is carried out as long as 13 holds. The difference is that for group size less than $\tau+1$, each user may have several contents to transmit to the other users (i.e., $a_{k}^{\mathcal{V}} \neq 1$ ). When a subset $\mathcal{V}$ is selected for D2D transmission, users in $\mathcal{V}$ transmit all the useful data available in their cache to the other users in the selected subset (following the method in [36]) and $I_{\mathrm{D} 2 \mathrm{D}}(\mathcal{V})$ is set to one. We also set $I_{\mathrm{D} 2 \mathrm{D}}(\mathcal{D})$ to one if all the subfiles in $\mathcal{D}$ are transmitted through D2D groups of size $\mathcal{V}<\tau+1$. The rest of the process is the same as in Section IV-B After D2D subset assessment is done, the DL delivery time is computed using (10), and the D2D time is computed using (12).

It is worth mentioning that the main target in (8) and 13 is to reduce the overall transmission time (i.e., $T_{\mathrm{D} 2 \mathrm{D}}+T_{\mathrm{DL}}$ ) in (3). However, as we show in the following section, D2D transmission can also notably reduce the complexity of the beamforming process in the DL phase. To this end, we briefly illustrate the complexity involved in the beamformer design and the effect of D2D transmission on the process.

```
Algorithm 1 D2D Assisted Multi-Antenna Coded Caching
    procedure DELIVERY \(\left(W_{1}, \ldots, W_{N}, d_{1}, \ldots, d_{K}, \mathbf{H}=\left[\mathbf{h}_{1}, \ldots, \mathbf{h}_{K}\right]\right)\)
        \(\tau \leftarrow M K / N\)
        for \(i \in\left[1,\binom{\tau+L}{\tau+1}\right]\) do
            if \(\frac{\hat{T}_{\mathrm{D}}^{i}}{N_{s}^{i}} \geq \hat{T}_{\mathrm{D} 2 \mathrm{D}}^{i}\) then
                for all \(k \in \mathcal{D}\) do
                    Each sub-file is divided into \(\tau\) mini-file fragments.
                        \(X_{k}^{\mathcal{D}} \leftarrow \oplus_{i \in \mathcal{D} \backslash\{k\}} N E W\left(W_{d_{i}, \mathcal{D} \backslash\{i\}}\right)\)
                        User \(k\) multicasts \(X_{k}^{\mathcal{D}}\) to \(\mathcal{R}^{\mathcal{D}}(k)=\mathcal{D} \backslash\{k\}\) with the rate \(R_{k}^{\mathcal{D}}\) stated in (1)
            end for
                            \(I_{D 2 D}(\mathcal{D})=1\)
    end if
    end for
    for all \(\mathcal{S} \subseteq[K],|\mathcal{S}|=\min (\tau+L, K)\) do
        for all \(\mathcal{D} \subseteq \mathcal{S},|\mathcal{D}|=\tau+1, I_{D 2 D}(\mathcal{D})=0\) do
            \(X_{\mathcal{D}}^{\mathcal{S}} \leftarrow \oplus_{k \in \mathcal{D}} N E W\left(W_{d_{k}, \mathcal{D} \backslash\{k\}}\right)\)
        end for
            \(\left\{\mathbf{w}_{\mathcal{D}}^{\mathcal{S}}\right\}=\underset{\left\{\mathbf{w}_{\mathcal{D}}^{\mathcal{S}}, \mathcal{D} \subseteq \mathcal{S},|\mathcal{D}|=\tau+1, I_{D 2 D}(\mathcal{D})=0\right\}}{\arg } \max _{C}\left(\mathcal{S},\left\{\underline{\mathbf{w}}_{\mathcal{D}}^{\mathcal{S}}, \mathcal{D} \subseteq \mathcal{S},|\mathcal{D}|=\tau+1, I_{D 2 D}(\mathcal{D})=0\right\}\right)\)
        \(\underline{\mathbf{X}}(\mathcal{S}) \leftarrow \sum_{\mathcal{D} \subseteq \mathcal{S},|\mathcal{D}|=\tau+1, I_{D 2 D}}(\mathcal{D})=0, \mathbf{w}_{\mathcal{D}}^{\mathcal{S}} \tilde{X}_{\mathcal{D}}^{\mathcal{S}}\)
        transmit \(\underline{\mathbf{X}}(\mathcal{S})\) with the rate \(R_{C}\left(\mathcal{S},\left\{\mathbf{w}_{\mathcal{D}}^{\mathcal{S}}, \mathcal{D} \subseteq \mathcal{S},|\mathcal{D}|=\tau+1, I_{D 2 D}(\mathcal{D})=0\right\}\right)\).
    end for
end procedure
```


## V. BEAMFORMING COMPLEXITY ANALYSIS

In this section, we investigate the effects of D2D transmissions in computational complexity for the general case. Authors in [17] show that the number of MAC conditions and quadratic terms in the SINR constraints dominates the complexity of the DL beamformer design. Thus, we first introduce two boundaries for the number of MAC conditions, then discuss the effects of D2D on the beamformer design complexity.

Theorem 1: Considering $i(\tau+1)+m$ subfiles are delivered via D2D transmissions, among which $i(\tau+1)$ subfiles are delivered through D2D groups with size $(\tau+1)$, the number of MAC conditions for the DL phase is lower bounded by:

$$
\underline{M}(\tau, i, m, L)=(\tau+L-b)\left(2^{a}-1\right)+b\left(2^{a+1}-1\right),
$$

where

$$
\begin{aligned}
& a \triangleq\left\lfloor\frac{(\tau+1)\left(M_{\mathrm{T}}-i\right)-m}{\tau+L}\right\rfloor \\
& b \triangleq(\tau+1)\left(M_{\mathrm{T}}-i\right)-m-a(\tau+L) \\
& m \triangleq \sum_{\mathcal{V} \in \overline{\Omega^{\mathcal{S}, \mathcal{V}} \backslash \overline{\Omega^{\mathcal{S}}}}} \sum_{k \in \mathcal{V}} a_{k}^{\mathcal{V}}, \quad M_{\mathrm{T}} \triangleq\binom{\tau+L}{\tau+1}
\end{aligned}
$$

and the number of MAC conditions is upper bounded by

$$
\begin{aligned}
& \bar{M}(\tau, i, m, L)= \\
& \quad(\tau+L-U)\left(2^{W}-1\right)+\left(2^{W-X}-1\right) \\
& \quad+(U-(\phi+1))\left(2^{\left(W-\left({ }_{\tau}^{U-2}\right)\right)}-1\right)
\end{aligned}
$$

where

$$
\begin{aligned}
& U \triangleq \min _{\text {s.T. }\binom{U^{\prime}}{\tau+1} \geq i} U^{\prime}, X \triangleq i-\binom{U-1}{\tau+1} \\
& \phi \triangleq\left\lfloor\frac{m}{W-\binom{U-2}{\tau}}\right\rfloor, W \triangleq\binom{\tau+L-1}{\tau}
\end{aligned}
$$

Proof 1: Refer to Appendix $\mathrm{A}$

The number of MAC conditions varies between $\underline{M}($.$) and$ $\bar{M}$ (.) based on which particular subsets have been selected for the D2D phase. For better intuition consider Fig. 44, which shows the normalized maximum and minimum number of MAC conditions ( $K=10, L=9, \tau=1)$ for different number of D2D groups $i$. As shown, the number of MAC conditions decreases drastically by using just a few D2D transmissions, which in turn dramatically reduces the complexity of the DL beamformer design. For example, for the case depicted in Fig. 4, by choosing only five different subsets of users among 45 available subsets, the number of MAC conditions can be reduced to half. Therefore, D2D significantly improves the beamformer design complexity.

In the following, we provide the boundaries for the number of quadratic terms in the SINR constraints (the second important factor in the DL beamforming complexity).

Theorem 2: Considering $i(\tau+1)+m$ subfiles are delivered via D2D transmissions, among which $i(\tau+1)$ subfiles are delivered through D2D groups with size $(\tau+1)$, the number of quadratic terms is upper bounded by:

$$
\bar{Q}(\tau, i, m, L)=b A_{2} B_{2}+(\tau+L-b) A_{1} B_{1}
$$

where $A_{1} \triangleq a, A_{2} \triangleq a+1, B_{1} \triangleq M_{\mathrm{T}}-i-A_{1}+1, B_{2} \triangleq$ $M_{\mathrm{T}}-i-A_{2}+1$. Moreover, the number of quadratic terms is

![](https://cdn.mathpix.com/cropped/2024_05_09_d8867f52fbc810dc46cag-10.jpg?height=667&width=894&top_left_y=179&top_left_x=152)

Fig. 4. The normalized number of MAC conditions vs the number of subsets assigned for D2D transmissions with $K=10, L=9$ and $\tau=1$.

![](https://cdn.mathpix.com/cropped/2024_05_09_d8867f52fbc810dc46cag-10.jpg?height=670&width=910&top_left_y=1199&top_left_x=152)

Fig. 5. The normalized number of quadratic variables vs the number of subsets assigned for D2D transmissions with $K=10, L=9$ and $\tau=1$.

lower bounded by:

$$
\begin{aligned}
\underline{Q}(\tau, i, m, L)=(\tau & +L-U) A_{1}^{\prime} B_{1}^{\prime} \\
& +(U-(\phi+1)) A_{2}^{\prime} B_{2}^{\prime}+A_{3}^{\prime} B_{3}^{\prime}
\end{aligned}
$$

where $A_{1}^{\prime} \triangleq W, A_{2}^{\prime} \triangleq A_{1}^{\prime}-\binom{U-2}{\tau}, A_{3}^{\prime} \triangleq A_{1}^{\prime}-X, B_{1}^{\prime} \triangleq$ $\underline{M_{\mathrm{T}}}-A_{1}^{\prime}+1, B_{2}^{\prime} \triangleq \underline{M_{\mathrm{T}}}-A_{2}^{\prime}+1, B_{3}^{\prime} \triangleq \underline{M_{\mathrm{T}}}-A_{3}^{\prime}+1$. We denote $\underline{M_{\mathrm{T}}} \triangleq\left\lceil\frac{(\tau+1)\left(M_{\mathrm{T}}-i\right)-m}{\tau+1}\right\rceil$ as the lower approximation of the total number of messages sent by the BS. Moreover, $a$, $b, X, U, m, M_{\mathrm{T}}, W$ and $\phi$ are defined trough (16) to (20).

Proof 2: Refer to Appendix B

Fig. 5 depicts the upper and lower boundaries for the same scenario as in Fig. 4. The gap between these bounds is not as considerable as MAC conditions. Thus, compared to the quadratic terms, the number of MAC conditions is more affected by how different D2D subsets are selected for transmission. Nevertheless, the role of D2D transmissions in reducing the total number of quadratic terms is notable. For example, choosing five different D2D subsets for the considered case reduces the total number of quadratic terms by $20 \%$.

Remark 2: For ease of exposition, $\tau+L=K$ is assumed in the equations and algorithms throughout this paper. However, the proposed methods can be easily generalized to other regimes. For example, in case $\tau+L<K$, there are $\binom{K}{\tau+L}$ orthogonal transmission phases. All the equations in this paper are valid separately for each phase. Similarly, for the case $\tau+L>K, \tau+L$ should be replaced with $K$ in all the equations. Moreover, for the restricted spatial DoF scenario [17], discussed also in Section [IV-C, $\tau+L$ should be changed to $\tau+\alpha$. Finally, the $\beta$ parameter introduced in [17] can be easily applied to the proposed equations by changing $M_{\mathrm{T}}$ to $P\binom{\tau+\beta}{\tau+1}$, and $W$ to $\binom{\tau+\beta-1}{\tau}$, where $\alpha, \beta$ and $P$ are defined in Section IV-C

## VI. NUMERICAL RESULTS

In this section, we provide numerical examples for two scenarios with $K=3$ and $K=4$ users (see Fig. 2 and Fig. 3). Due to the complex beamforming procedure for the multiserver-based schemes (such as the one proposed in this paper), we have considered a limited number of users in the network. We consider a circular cell with a radius of $R=100$ meters, where the BS is located in the cell center. To investigate the effect of D2D transmission in different situations, we introduce a smaller circle with radius $r$ within the cell area, wherein the users are randomly scattered. Thus, the maximum distance between any two users is $2 r$. In contrast, the users' distance to $\mathrm{BS}$ varies between 0 and $R$. Hence, by changing $r$, the maximum users' separation in D2D mode is controlled, which helps us determine the beneficial users' distance in the D2D phase.

For D2D transmissions, the channel gains are generated as $h_{i k}=d_{i k}^{-\frac{n_{\mathrm{D} 2 \mathrm{D}}}{22}} g_{i k}$, where $g_{i k} \sim \mathbb{C N}(0,1), n_{\text {D2D }}=2$ is the path-loss exponent, and $d_{i k}$ is the inter-user distance. The channel vectors for DL transmission are generated from i.i.d statistics with $\mathbf{h}_{k}=d_{k}^{-\frac{n_{\mathrm{DL}}}{2}} \mathbf{g}_{k}$, where $\mathbf{g}_{k} \sim \mathbb{C N}(0, \mathbf{I}), n_{\mathrm{DL}}=3$ is the path-loss exponent, and $d_{k}$ is the BS-user distance. Transmit powers for D2D transmissions at the user side are adjusted so that the average received SNR at the receiver is $0 \mathrm{~dB}$ at a 10 -meter distance. The BS transmit power is adjusted such that the average received $\mathrm{SNR}$ is $0 \mathrm{~dB}$ at a 100-meter distance. For comparison, we have also consider two benchmark schemes [17] and [36] denoted as Multicasting only and D2D only, respectively. Note that the optimality of
the scheme in [36] is shown in [37], and the superiority of the proposed method in [17] over the traditional unicasting approaches has been shown therein. Hence, we compare the proposed D2D/DL delivery scheme to these two schemes in this work.

Fig. 6 shows average delivery rate for $K=3, L=2$ and $\tau=1$ (section III-A) as a function of inner circle radius $r$. The figure demonstrates that when users are close to each other, there is a significant gain from using a combination of multicasting and D2D transmissions. Compared to the D2D only rate that decreases drastically as the inter-user distance is increased, the proposed approach shows steadier behavior. The beneficial range for D2D transmission in this particular scenario appears to be between $r=0$ and $5 m$ ( $10 \mathrm{~m}$ maximum distance). The range can change if the path-loss exponent, the available power for both D2D and DL transmission, $\tau$, etc., are varied. The simulation results demonstrate that sending all the data only via D2D transmissions or only through multicasting results in a lower rate than the proposed approach with the optimized mode selection.

Fig. 7 /shows the average delivery rate versus the inner circle radius for $K=4, \tau=2, L=2$ (section III-B). In this case, the gain from D2D transmission among nearby users is larger than the case $K=3$ due to more D2D transmission opportunities. However, the gain of D2D transmission decreases more rapidly compared to the case $K=3$. In this case, $\tau$ equals 2 , so more users must be closer to each other to perform efficient D2D transmission. Therefore, it can be concluded that for a fixed number of users $K$, increasing $\tau$ results in fewer D2D opportunities and fewer D2D subset selection variants. However, with a fixed $\tau$, increasing the number of users $K$ will result in a more diverse D2D combination and higher gain over the $D 2 D$ only case.

It is worth mentioning that using the heuristic D2D mode selection criteria (defined in Section IV] results in a minimal average delivery rate loss, with a significantly reduced complexity compared to the exhaustive search. Simulation results show that the approximated rate in (10) is very close to the actual rate (7) for different $\Omega^{\mathcal{S}}$ and different network parameters (i.e., $\tau, L, K$, etc).

Fig. 8 depicts the average delivery rate for different D2D and DL SNRs, where all the users experience similar link conditions. As illustrated, the gap between the exhaustive search and the proposed scheme remains negligible in different SNR regions. When the received SNR of DL and D2D links are within the same range, i.e., the rate difference is not significant, choosing the right beneficial D2D groups is challenging. However, the proposed scheme still follows the exhaustive search in such scenarios. Since the curves have similar behavior for the two cases, we only represent the $K=4$ case.

Fig. 9 compares the proposed scheme for D2D group size $|\mathcal{D}|=\tau+1=3$ (proposed mode selection (8)) versus general D2D group size (proposed mode selection (13)) for different

![](https://cdn.mathpix.com/cropped/2024_05_09_d8867f52fbc810dc46cag-11.jpg?height=656&width=890&top_left_y=190&top_left_x=1081)

Fig. 6. Average delivery rate vs. inner circle radius $r$ for $K=3, L=2$ and $\tau=1$

![](https://cdn.mathpix.com/cropped/2024_05_09_d8867f52fbc810dc46cag-11.jpg?height=664&width=892&top_left_y=1197&top_left_x=1077)

Fig. 7. Average delivery rate vs. inner circle radius $r$ for $K=4, L=2$ and $\tau=2$.

D2D received $\operatorname{SNRs}]^{6}$ When users experience similar channel conditions, the authors in [36] show that the achievable rate of their proposed D2D scheme, which is also performed in the[^5]

![](https://cdn.mathpix.com/cropped/2024_05_09_d8867f52fbc810dc46cag-12.jpg?height=657&width=883&top_left_y=192&top_left_x=166)

Fig. 8. Average delivery rate Vs. D2D and DL SNR for $K=4, L=2$ $\tau=2$, and $m=0$.

D2D mode in this paper, is within a constant factor from the optimal value. The numerical example shown in Fig. 9 further demonstrates that when users experience similar channel conditions, considering $|\mathcal{D}|<\tau+1$ does not significantly improve the total delivery time (which corresponds to the results in $[36 \mid)$.

Note that the results in [36] are valid for the error-free D2D links with constant link capacity; however, when users experience different D2D link capacity, the results in [36] do not hold anymore. For instance, the message $\tilde{X}_{1,2,3}$ in section $\Pi$ III-B can still be transmitted through two D2D groups, e.g., $(1,2)$ and $(1,3)$, even if user pair $(3,2)$ is not in a favorable D2D condition (i.e., D2D group $\{1,2,3\}$ does not satisfy Eq. (8)). Fig. 10 illustrates the average delivery rate for the same scenario as in Fig. 9, but when D2D user pairs $(1,3)$ and $(2,4)$ are attenuated by $10 \mathrm{~dB}$, i.e., user pairs $(1,2),(1,4),(2,3)$, and $(3,4)$ experience similar D2D SNRs while D2D SNR for user pairs $(1,3)$ and $(2,4)$ is $10 \mathrm{~dB}$ less than the rest of the D2D pairs. The results show that considering D2D groups with various sizes is crucial when users experience uneven D2D link conditions.

## VII. CONCLUSION

A novel cache-aided delivery method, comprising orthogonal D2D and DL transmission phases, was proposed to improve the multiantenna CC- based content delivery. In the proposed method, the DL multicasting of file fragments is complemented by allowing direct D2D exchange of local cache content. The benefits of partial D2D offloading the content were investigated. We showed that the benefits of using D2D transmission are two-fold. First, nearby users may greatly benefit from direct content exchange providing a notably increased overall delivery rate. Second, the partial offloading of the contents in the D2D phase decreases the DL beamforming complexity. This is due to the reduced number of variables and conditions in the beamformer optimization problem.

We showed that the D2D optimal subset selection imposes high computational complexity due to the DL multicast de-

![](https://cdn.mathpix.com/cropped/2024_05_09_d8867f52fbc810dc46cag-12.jpg?height=654&width=911&top_left_y=188&top_left_x=1062)

Fig. 9. Average delivery rate Vs. D2D SNR for $K=4, \tau=2, L=2$, and $10 \mathrm{~dB}$ DL SNR.

![](https://cdn.mathpix.com/cropped/2024_05_09_d8867f52fbc810dc46cag-12.jpg?height=629&width=884&top_left_y=927&top_left_x=1076)

Fig. 10. Average delivery rate Vs. D2D SNR for $K=4, \tau=2, L=2$, and $0 \mathrm{~dB}$ DL SNR. User pairs $(1,3)$ and $(2,4)$ are attenuated by $10 \mathrm{~dB}$.

sign. On the other hand, it is a combinatorial problem and hence NP-hard. Therefore, we proposed an approximation for the DL achievable rate without computing beamformers to overcome these practical limitations. Next, based on the approximated DL rate, we provided a low complexity mode selection algorithm, which allows efficient determination of D2D opportunities even for many users. The simulation results demonstrated that the proposed heuristic mode selection performs comparably to the exhaustive search with significantly reduced complexity. Furthermore, further extension is possible by considering the users' energy expenditure in the D2D mode and the energy efficiency of the BS in the DL mode. Another direction includes applying ML-based tools for cache placement and D2D/DL mode selection. Particularly, users' movement patterns can be predicted using past data history, which can then be used to decide on partial file delivery in D2D mode. Finally, further overall improvement can be achieved by allowing parallel mutually interfering transmissions within multiple D2D groups.

## APPENDIX A <br> PROOF OF THEOREM 1

First, consider the case where no D2D transmission is available. In this case, the total number of messages transmitted to all the users is $M_{\mathrm{T}}=\binom{\tau+L}{\tau+1}$, and each user needs $W=\binom{\tau+L-1}{\tau}$ of these messages to decode its intended file. Then, the per-user number of MAC conditions is $J(\tau, i=$ $0, m=0, L)=2^{W}-1$. Accordingly, considering the $\tau+L$ number of users served in each transmission, the total number of MAC conditions in the beamformer optimization problem is $M(\tau, i=0, m=0, L)=(\tau+L) J_{0}$.

Now, when $i$ user groups of size $\tau+1$ are selected for the D2D phase, the total number of MAC conditions varies based on which user groups are selected. To illustrate, consider the simple scenario where $i=2$ and $\left\{\mathcal{S}_{1} \subset[K]:\left|\mathcal{S}_{1}\right|=\tau+1\right\}$ and $\left\{\mathcal{S}_{2} \subset[K]:\left|\mathcal{S}_{2}\right|=\tau+1\right\}$ denote the first and the second D2D groups, respectively. Then, the total number of MAC conditions varies based on the number of users in common between the two groups. In this regard, denoting $c_{u}$ as the number of users in common, i.e., $c_{u}=\left|\mathcal{S}_{1} \cap \mathcal{S}_{2}\right|$, the total number of MAC conditions varies as follows.

Case-1 $\left(c_{u}=0\right)$ : In this case, all the users in the two D2D groups receive one subfile. Thus, they need $W-1$ messages in the DL signal to decode their intended files. Accordingly, the number of MAC conditions for these users is $J(\tau, i=1, m=$ $0, L)=2^{W-1}-1$, and the total number of MAC conditions (in this case) is $M(\tau, i=1, m=0, L)=(L-\tau-2) J(\tau, i=$ $0, m=0, L)+2(\tau+1) J(\tau, i=1, m=0, L) \approx M(\tau, i=$ $0, m=0, L)-2(\tau+1) J(\tau, i=1, m=0, L)$.

Case-2 $\left(c_{u} \neq 0\right)$ : Denote $\mathcal{S}_{c}=\mathcal{S}_{1} \cap \mathcal{S}_{2}$ and $\mathcal{S}_{r}=$ $\mathcal{S}_{1} \cup \mathcal{S}_{2} \backslash \mathcal{S}_{1} \cap \mathcal{S}_{2}$ as the set of common/joint and uncommon/disjoint users, respectively. Then, in this case, the common users receive two subfiles, and the rest of the users in set $\mathcal{S}_{r}$ receive one subfile through the D2D phase. Thus, the common users need $W-2$ number of messages in the DL phase, and the number of MAC conditions for these users is $J(\tau, i=2, m=0, L)=2^{W-2}-1$, while the rest require $W-1$ number of subfiles in the DL phase. Accordingly, the total number of MAC conditions (in this case) is $\left.M(\tau, i=2, m=0, L)=\left(L-\tau-2+c_{u}\right)\right) J(\tau, i=0, m=$ $0, L)+\left(2 \tau+2-c_{u}\right) J(\tau, i=1, m=0, L)+c_{u} J(\tau, i=2, m=$ $0, L) \approx M(\tau, i=1, m=0, L)+c_{u} J(\tau, i=2, m=0, L)$.

Compared to the first case, the number of MAC conditions is more due to having common users. Therefore, when D2D transmissions occur uniformly among all users, the total number of MAC conditions is minimized. In other words, when all the users need almost the same number of subfiles in the DL phase, the number of MAC conditions is minimized. On the other hand, when D2D transmissions occur to a limited number of users, the number of MAC conditions is maximized.

## A. Minimum number of MAC conditions

Let us define a super set $\overline{\mathcal{V}}$ which includes all the D2D sets with size less than $\tau+1$, i.e., each element in $\overline{\mathcal{V}}$ is a set $\mathcal{V} \subset[K]$ such that $2 \leq|\mathcal{V}|<\tau+1$. We also define another super set $\overline{\mathcal{D}}$, where each element in $\overline{\mathcal{D}}$ is a set $\mathcal{D} \subseteq[K]$ such that $|\mathcal{D}|=\tau+1$, i.e.,

$$
\overline{\mathcal{D}}=\{\mathcal{D}|\mathcal{D} \subseteq[K],| \mathcal{D} \mid=\tau+1\}
$$

Now, assume $m$ subfiles are delivered through D2D groups in $\overline{\mathcal{V}}$, and $(\tau+1) i$ subfiles are delivered through D2D groups in $\overline{\mathcal{D}}$, where $|\overline{\mathcal{D}}|=i$. In this case, the total number of remaining subfiles in the DL signal is $(\tau+1)\left(\binom{\tau+L}{\tau+1}-i\right)-m$. Based on the previous paragraph, when these subfiles are uniformly allocated to all users, the total number of MAC conditions in the beamformer design is minimized. Therefore, in such cases, $\tau+L-b$ users receive $a=\left\lfloor\frac{(\tau+1)\left(\binom{\tau+L}{\tau+1}-i\right)-m}{\tau+L}\right\rfloor$ subfiles and $b \triangleq(\tau+1)\left(M_{\mathrm{T}}-i\right)-m-a(\tau+L)$ users receive $a+1$ subfiles in the DL phase. Consequently, the minimum number of MAC conditions in the DL phase is $\underline{M}(\tau, i, m, L)=(\tau+$ $L-b)\left(2^{a}-1\right)+b\left(2^{a+1}-1\right)$.

## B. Maximum number of MAC conditions

Let us first consider the $m=0$ case; as discussed earlier, the number of MAC conditions is maximized when D2D groups are selected from a limited number of users. Thus, to maximize the number of MAC conditions, we first denote $\mathcal{U} \subseteq[K]$ as the smallest set of users to form $i$ different D2D groups with size $\tau+1$, i.e., $U=\arg \min \binom{\hat{U}}{\tau+1}$ such that $\binom{\hat{U}}{\tau+1} \geq i$, where $U=|\mathcal{U}|$. Clearly, $U$ is not smaller than $\tau+1$ based on the definition. Then, we define $\overline{\mathcal{C}}_{n}(\mathcal{A})=\{\mathcal{B}|\mathcal{B} \subseteq \mathcal{A},| \mathcal{B} \mid=n\}$ as the collection of all the subsets of size $n$ from the set $\mathcal{A}$, where $\left|\overline{\mathcal{C}}_{n}(\mathcal{A})\right|=\binom{|\mathcal{A}|}{n}$. We also denote all the non-empty subsets of the set $\mathcal{U}$ as $\mathcal{S}$ i.e., $\mathcal{S} \subseteq \mathcal{U},|\mathcal{S}| \geq 1$. Moreover, we call such a set $\mathcal{S}$ to be a utilized-D2D-set if $\overline{\mathcal{C}}_{\tau+1}(\mathcal{S}) \subset \overline{\mathcal{D}}$, where $\overline{\mathcal{D}}$ is defined in (23). We represent the set of all the utilized-D2Dsets as $\overline{\mathcal{S}}(\mathcal{U})$, i.e., $\overline{\mathcal{S}}(\mathcal{U})=\left\{\mathcal{S} \mid \mathcal{S} \subseteq \mathcal{U}, \overline{\mathcal{C}}_{\tau+1}(\mathcal{S}) \subset \overline{\mathcal{D}}\right\}$. We are interested in the utilized-D2D-set with the largest number of users. We call such a set as the fully-utilized-D2D-set and denote it with $\hat{S}$. In other words, $\hat{S} \in \overline{\mathcal{S}}(\mathcal{U})$ and for every $\mathcal{S}_{0} \in \overline{\mathcal{S}}(\mathcal{U})$ we have $|\hat{S}| \geq\left|\mathcal{S}_{0}\right|$. Therefore, by the definition, $|\hat{\mathcal{S}}|=U-1$, and the users belonging to the set $\hat{\mathcal{S}}$ form $\binom{U-1}{\tau+1}$ D2D groups. The remaining $X=i-\binom{U-1}{\tau+1}$ D2D groups include $\tau$ number of users from the set $\hat{\mathcal{S}}$ and one remaining user denoted by $k_{r}$, where $k_{r}=\mathcal{U} \backslash \hat{\mathcal{S}}$.

Therefore, in this case, there exist 3 different types of users (see Fig. 11

- First type, Those who have not received any subfile in D2D transmissions. So they need $W=\binom{\tau+L-1}{\tau}$ number of subfiles in DL phase, and their total number is $K_{0}=$ $\tau+L-U$.
- Second type, Those who have received all the available subfiles in the set $\hat{\mathcal{S}}$. Thus, they need $W_{\hat{\mathcal{S}}}=\binom{\tau+L-1}{\tau}-$ $\binom{(U-1)-1}{\tau}$ number of subfiles in the DL phase, and their total number is $K_{1}=U-1$. For convenience, we ignore the received subfiles in the $X$ remaining D2D groups for $\forall k \in \hat{\mathcal{S}}$.
- Third type, The user $k_{r}$ who has received $X$ number of subfiles in the groups consisting of itself and $\tau$ members of the set $\hat{\mathcal{S}}$, so it needs $W_{k_{r}}=\binom{\tau+L-1}{\tau}-X$ number of subfiles in the DL phase.

![](https://cdn.mathpix.com/cropped/2024_05_09_d8867f52fbc810dc46cag-14.jpg?height=350&width=874&top_left_y=175&top_left_x=167)

Fig. 11. a) The limited D2D user selection case, where $K=10, \tau=1, i=$ $4, \overline{\mathcal{D}}=\{\{1,2\},\{1,3\},\{2,3\},\{2,4\}\}, \mathcal{U}=\{1,2,3,4\}, \hat{\mathcal{S}}=\{1,2,3\}$, and $k_{r}=4$. b) Uniform D2D subset selection case.

Therfore, the maximum number of MAC conditions for $|\overline{\mathcal{D}}|=$ $i$ and $m=0$ is upper bounded by $\bar{M}(\tau, i, m, L)=K_{0}\left(2^{W}-\right.$ 1) $+K_{1}\left(2^{W_{\hat{\mathcal{S}}}}-1\right)+\left(2^{W_{k_{r}}}-1\right)$.

For the case $m \neq 0$, suppose each D2D subset $\mathcal{V}$ delivers a single subfile to each of the users $k \in \mathcal{V}$; accordingly, each user $k \in \mathcal{V}$ requires one less subfile in the DL phase. Based on the previous discussion, removing $v$ subfiles from one user reduces the total number of MAC conditions less than removing one subfile for $v$ users, i.e.,

$$
M(\tau, i, 0, L)-v 2^{x-1}<M(\tau, i, 0, L)-2^{x-v}
$$

Therefore, we assume that each D2D subset of size $|\mathcal{V}|=v$ delivers all the subfiles to a single user. Also, to consider as limited D2D user sets as possible, we assume these $m$ subfiles are also shared among the second type of users. In this regard, considering total number of $m$ subfiles delivered through D2D groups in $\overline{\mathcal{V}}$, the minimum number of served users is $\phi=$ $\left\lfloor\frac{m}{W_{\hat{\mathcal{S}}}}\right\rfloor$. Therefore, the maximum number of MAC conditions for $|\overline{\mathcal{D}}|=i$ and $m \neq 0$ is upper bounded by $\bar{M}(\tau, i, m, L)=$ $K_{0}\left(2^{W}-1\right)+\left(K_{1}-\phi\right)\left(2^{W_{\hat{\mathcal{S}}}}-1\right)+\left(2^{W_{k_{r}}}-1\right)$.

## APPENDIX B

## PROOF OF THEOREM 2

When D2D transmission is not feasible, the BS transmits $M_{\mathrm{T}}$ messages in the DL phase, where each user needs $W$ number of these messages and considers the rest (i.e., $M_{\mathrm{T}}-W$ terms) as interference. In this case, for each intended message $\mathcal{D}$ of user $k$ ( $\mathcal{D}$ is the message index), one quadratic term for the intended message $\left(\left|\mathbf{h}_{k}^{H} \mathbf{w}_{\mathcal{D}}\right|^{2}, \mathcal{D} \in \Omega_{k}^{\mathcal{S}}\right)$ plus $M_{\mathrm{T}}-$ $W$ quadratic terms for the interfering messages $\left(\left|\mathbf{h}_{k}^{H} \mathbf{w}_{\mathcal{D}^{\prime}}\right|^{2}\right.$, $\mathcal{D}^{\prime} \in \mathcal{I}_{k}$ ) is considered in (7). Thus, in total, the BS considers $Q_{k}=W\left(M_{\mathrm{T}}-W+1\right)$ quadratic terms in its' optimization problem for each user. Therefore, the total number of quadratic variables $Q_{k}$ is a quadratic function in terms of $W$ (see Fig. 12 (a)), which is maximized when $\bar{W}=\frac{M_{\mathrm{T}}+1}{2}$. Moreover, when D2D transmission is not feasible, $W$ is equal to $\binom{\tau+L-1}{\tau}=$ $\frac{\tau+1}{\tau+L} M_{\mathrm{T}}$, where $W$ is greater than $\bar{W}$ for $1 \leq L<\tau+2$, and $W$ is less than $\bar{W}$ for $\tau+2<L$ (see Fig. 12 (a)).

For the case $|\overline{\mathcal{D}}|=i$ (assume $m=0$ ), let us define $W_{k}^{i}$ as the number of DL messages needed by user $k$ after $i$ D2D time slots. We also define $M_{\mathrm{T}}^{i}$ as the total number of transmitted messages in the DL phase after $i$ D2D time slots. In this case, $W_{k}^{i}$ is independent of $M_{\mathrm{T}}^{i}$, i.e., $0 \leq \frac{W_{k}^{i}}{M_{\mathrm{T}}^{i}} \leq 1$, and $Q_{k}^{i}=$ $W_{k}^{i}\left(M_{T}^{i}-W_{k}^{i}+1\right)$ is a quadratic function in terms of $W_{k}^{i}$.
We consider two extreme scenarios in this case (similar to Appendix A):

1) When the D2D subsets are selected uniformly among all the users.
2) When the D2D subsets are selected among a limited number of users.

In the first scenario, since all the users have received almost the same number of subfiles in the D2D phase, they all need almost the same number of messages in the DL phase (see Fig. 12 (b)). However, in the second scenario, since some users have received most of their intended files in the D2D phase, they need a few numbers of messages in the DL phase. In contrast, users who did not receive any subfile in the D2D phase need most of the subfiles in the DL phase. Thus, in this scenario, $W_{k}^{i} \mathrm{~s}$ are either on the right-hand side of the maximum point or on the left-hand side of it (see Fig.[12.(c)).

Therefore, these two cases are two extreme cases for the total number of quadratic variables as well. In this regard, the total number of quadratic variables is maximized when D2D subsets are uniformly selected among all the users. On the other hand, when a limited number of users are selected for D2D transmissions, $Q$ is minimized. Finally, the total number of quadratic variables (after $i$ D2D time slots) is computed as $Q^{i}=\sum_{k \in[\tau+L]} Q_{k}^{i}$. Substituting the total number of needed messages for each user, defined in appendix A equations 21 and $(22)$ are achieved.

For the case $m \neq 0, M_{T}^{i}$ can be lower-approximated by $\underline{M_{\mathrm{T}}}=\left[\frac{(\tau+1)\left(\binom{\tau+L}{\tau+1}-i\right)-m}{\tau+1}\right]$, where we assume each $\tau+1$ number of transmitted subfiles through D2D groups in $\overline{\mathcal{V}}$ removes one of the remaining messages in the DL phase. The $M_{T}^{i}$ is upper-approximated by $\overline{M_{\mathrm{T}}}=\binom{\tau+L}{\tau+1}-i$, where we assume no messages are being eliminated after D2D transmissions in D2D groups with size less than $\tau+1$. In this case, the total number of quadratic variables is computed as same as the $m=0$ case by substituting $M_{T}^{i}$ with $\overline{M_{\mathrm{T}}}\left(\underline{M_{\mathrm{T}}}\right)$ for upper bound (lower bound).

## REFERENCES

[1] E. Bastug, M. Bennis, and M. Debbah, "Living on The Edge: The Role of Proactive Caching in 5G Wireless Networks," IEEE Commun. Mag., vol. 52, no. 8, pp. 82-89, Aug 2014

[2] G. Paschos, E. Bastug, I. Land, G. Caire, and M. Debbah, "Wireless Caching: Technical Misconceptions and Business Barriers," IEEE Commun. Mag., vol. 54, no. 8, pp. 16-22, August 2016.

[3] H. B. Mahmoodi, M. Salehi, and A. Tölli, " Non-Symmetric Coded Caching for Location-Dependent Content Delivery," in Proc. IEEE Int. Symp. Inf. Theory (ISIT), pp. 712-717, July 2021.

[4] H. B. Mahmoodi, M.J. Salehi, and A. Tölli, "Non-Symmetric MultiAntenna Coded Caching for Location-Dependent Content Delivery," in Proc. IEEE Int. Conf. on Commun., pp. 5165-5170, Jun 2022.

[5] H. B. Mahmoodi, M.J. Salehi, and A. Tölli, "Asymmetric Multi-Antenna Coded Caching for Location-Dependent Content Delivery," in Proc. IEEE Global Commun. Conf., pp. 1930-1935, Dec. 2022.

[6] M. A. Maddah-Ali and U. Niesen, "Fundamental Limits of Caching," IEEE Trans. Inf. Theory, vol. 60, no. 5, pp. 2856-2867, May 2014.

[7] R. Amer, M. M. Butt, M. Bennis, and N. Marchetti, "Inter-Cluster Cooperation for Wireless D2D Caching Networks," IEEE Trans. Wireless Comтип., vol. 17, no. 9, pp. 6108-6121, Sep 2018.

[8] N. Karamchandani, U. Niesen, M. A. Maddah-Ali, and S. N. Diggavi, "Hierarchical Coded Caching," IEEE Trans. Inf. Theory, vol. 62, no. 6, pp. 3212-3229, Jun 2016.
![](https://cdn.mathpix.com/cropped/2024_05_09_d8867f52fbc810dc46cag-15.jpg?height=458&width=1726&top_left_y=178&top_left_x=167)
b)
![](https://cdn.mathpix.com/cropped/2024_05_09_d8867f52fbc810dc46cag-15.jpg?height=374&width=1096&top_left_y=247&top_left_x=796)

Fig. 12. Total number of quadratic variables for each user in different scenarios: a) no D2D case b) uniform scenario c) scenario with a limited number of users.

[9] R. Pedarsani, M. A. Maddah-Ali, and U. Niesen, "Online Coded Caching," IEEE/ACM Trans. on Networking, vol. 24, no. 2, pp. 836845, Apr 2016.

[10] S. P. Shariatpanahi et al., "Multi-Server Coded Caching," IEEE Trans. Inf. Theory, vol. 62, no. 12, pp. 7253-7271, Dec 2016.

[11] S. P. Shariatpanahi, G. Caire, and B. Hossein Khalaj, "Physical-Layer Schemes for Wireless Coded Caching," IEEE Trans. Inf. Theory, vol. 65, no. 5, pp. 2792-2807, Dec 2019

[12] N. Naderializadeh, M. A. Maddah-Ali, and A. S. Avestimehr, "Fundamental Limits of Cache-Aided Interference Management," IEEE Trans. Inf. Theory, vol. 63, no. 5, pp. 3092-3107, May 2017.

[13] - , "Cache-aided Interference Management In Wireless Cellular Networks," in Proc. IEEE Int. Conf. Commun., pp. 1-7, May 2017.

[14] S. P. Shariatpanahi et al., "Multi-antenna Coded Caching," in Proc. IEEE Int. Symp. Inf. Theory, pp. 2113-2117, Jun 2017.

[15] K. H. Ngo, S. Yang, and M. Kobayashi, "Scalable Content Delivery with Coded Caching in Multi-Antenna Fading Channels," IEEE Trans. Wireless Commun., vol. 17, no. 99, pp. 1-1, November 2017.

[16] E. Piovano, H. Joudeh, and B. Clerckx, "On Coded Caching in the Overloaded MISO Broadcast Channel," in Proc. IEEE Int. Symp. Inf. Theory, pp. 2795-2799, Jun 2017.

[17] A. Tölli, S. P. Shariatpanahi, J. Kaleva, and B. H. Khalaj, "MultiAntenna Interference Management for Coded Caching," IEEE Trans. Wireless Commun., vol. 19, no. 3, pp. 2091-2106, March 2020.

[18] V. Ravindrakumar, P. Panda, N. Karamchandani, and V. M. Prabhakaran, "Private Coded Caching," IEEE Trans. Inf. Forensics Security, vol. 13, no. 3, pp. 685-694, March 2018.

[19] A. A. Zewail and A. Yener, "Device-to-Device Secure Coded Caching," IEEE Trans. Inf. Forensics Security, vol. 15, pp. 1513-1524, Sep 2019.

[20] L. Tang and A. Ramamoorthy, "Coded Caching Schemes With Reduced Subpacketization from Linear Block Codes," IEEE Trans. Inf. Theory, vol. 64, no. 4, pp. 3099-3120, April 2018.

[21] E. Lampiris and P. Elia, "Adding Transmitters Dramatically Boosts Coded-Caching Gains for Finite File Sizes," IEEE J. Select. Areas Сотmип., vol. 36, no. 6, pp. 1176-1188, Jun 2018.

[22] M. Salehi, E. Parrinello, S. P. Shariatpanahi, P. Elia and A. Tölli, "Low-Complexity High-Performance Cyclic Caching for Large MISO Systems," IEEE Trans. Wireless Commun., vol. 21, no. 5, pp. 3263-3278, May 2022.

[23] M. Salehi, A. Tolli, S. P. Shariatpanahi, and J. Kaleva, "Subpacketization-Rate Trade-off in Multi-Antenna Coded Caching," in Proc. IEEE Global Telecommun. Conf., pp. 1-6, Dec 2019.

[24] E. Parrinello, A. Ünsal and P. Elia, "Fundamental Limits of Coded Caching With Multiple Antennas, Shared Caches and Uncoded Prefetching," in IEEE Transactions on Information Theory, vol. 66, no. 4, pp. 2252-2268, April 2020, doi: 10.1109/TIT.2019.2955384.

[25] M. Dutta and A. Thomas, "Decentralized Coded Caching for Shared Caches," in IEEE Communications Letters, vol. 25, no. 5, pp. $1458-$ 1462, May 2021, doi: 10.1109/LCOMM.2021.3052237.

[26] A. Destounis, A. Ghorbel, G. S. Paschos, and M. Kobayashi, "Adaptive Coded Caching for Fair Delivery Over Fading Channels," IEEE Trans. Inf. Theory, vol. 66, no. 7, pp. 4530-4546, July 2020.

[27] R. Combes, A. Ghorbel, M. Kobayashi, and S. Yang, "Utility Optimal Scheduling for Coded Caching in General Topologies," IEEE J. Select. Areas Commun., vol. 36, no. 8, pp. 1692-1705, Aug 2018.

[28] Z. Zhang, H. Chen, M. Hua, C. Li, Y. Huang, and L. Yang, "Double coded caching in ultra dense networks: Caching and multicast scheduling via deep reinforcement learning," IEEE Trans. Commun., vol. 68, no. 2, pp. 1071-1086, 2019.

[29] A. Tang, S. Roy and X. Wang, "Coded Caching for Wireless Backhaul Networks With Unequal Link Rates," IEEE Trans. Commun., vol. 66, no. 1, pp. 1-13, Jan 2018.

[30] D. Feng, L. Lu, Y. Yuan-Wu, G. Y. Li, S. Li, and G. Feng,"Device-todevice Communications in Cellular Networks," IEEE Commun. Mag., vol. 52, no. 4, pp. 49-55, April 2014.

[31] X. Li, X. Wang, P. Wan, Z. Han, and V. C. M. Leung, "Hierarchical Edge Caching in Device-to-Device Aided Mobile Networks: Modeling, Optimization, and Design," IEEE J. Select. Areas Commun., vol. 36, no. 8 , pp. $1768-1785$, Aug 2018

[32] J. Pedersen, A. Graell i Amat, I. Andriyanova, and F. Brännström, "Optimizing MDS Coded Caching in Wireless Networks With Deviceto-Device Communication," IEEE Trans. Wireless Commun., vol. 18, no. 1, pp. 286-295, Jan 2019.

[33] T. Tiong, I. Saad, K. T. K. Teo and H. b. Lago, "Deep Reinforcement Learning with Robust Deep Deterministic Policy Gradient," 2nd Int. Conf. on Elect., Cont. and Instrum. Engin. (ICECIE), Kuala Lumpur, Malaysia, pp. 1-5, 2020.

[34] L. Zhou, S. Leng, Q. Liu and Q. Wang, "Intelligent UAV Swarm Cooperation for Multiple Targets Tracking," IEEE Internet of Things Journal, vol. 9, no. 1, pp. 743-754, 2022.

[35] J. Shuja, et al., "Applying machine learning techniques for caching in next-generation edge networks: A comprehensive survey," Journal of Network and Computer Applications, vol. 181, pp. 103005, 2021

[36] M. Ji, G. Caire, and A. F. Molisch, "Fundamental Limits of Caching in Wireless D2D Networks," IEEE Trans. Inf. Theory, vol. 62, no. 2, pp. 849-869, Feb 2016.

[37] C. Yapar, K. Wan, R. F. Schaefer, and G. Caire, "On The Optimality of D2D Coded Caching with Uncoded Cache Placement and One-Shot Delivery," IEEE Trans. Commun., vol. 67, no. 12, pp. 8179-8192, Dec 2019.

[38] A. M. Ibrahim, A. A. Zewail, and A. Yener, "Device-to-Device CodedCaching with Distinct Cache Sizes," IEEE Trans. Commun., vol. 68, no. 5, pp. 2748-2762, May 2020.

[39] A. Shabani, S. P. Shariatpanahi, V. Shah-Mansouri, and A. Khonsari, "Mobility Increases Throughput of Wireless Device-to-Device Networks with Coded Caching," in Proc. IEEE Int. Conf. Commun., pp. 1-6, May 2016.

[40] J. Wang, M. Cheng, Q. Yan, and X. Tang, "Placement Delivery Array Design For Coded Caching Scheme In D2D Networks," IEEE Trans. Commun., vol. 67, no. 5, pp. 3388-3395, May 2019.

[41] J. Chen, H. Yin, X. You, Y. Geng, and Y. Wu, "Centralized Coded Caching with User Cooperation," in Proc. IEEE Inf. Theory Workshop, pp. 1-5, Aug 2019.

[42] L. Zhong, X. Zheng, J. Lin, Y. Cao, and S. Ju, "Adaptive Delay optimization Of Multicast-Enabled Coded Caching in Device-to-Device Networks," China Communications, vol. 17, no. 1, pp. 42-48, Jan 2020.

[43] E. Dahlman, S. Parkvall, and J. Skold, "5G NR: The next generation wireless access technology," Academic Press, 2020.

[44] H. B. Mahmoodi, J. Kaleva, and A. Tölli, "Complexity Reduction in Multicast Beamforming For D2D Assisted Coded Caching," in Proc. IEEE Int. Symp. on Wireless Commun. Systems, pp. 239-243, Aug 2019.

[45] H. B. Mahmoodi, J. Kaleva, S. P. Shariatpanahi, and A. Tölli, "D2D Assisted Beamforming for Coded Caching," in Proc. IEEE Wireless Commun. and Networking Conf., pp. 1-6, May 2020.

[46] M. Sheraz, et al., "Artificial intelligence for wireless caching: Schemes, performance, and challenges," IEEE Communications Surveys and Tutorials Vol. 23, pp. 631-661, 2020.


[^0]:    The authors are with Centre for Wireless Communications, University of Oulu P.O. Box 4500, FIN-90014 University of Oulu, Finland. Email: \{hamidreza.bakhshzadmahmoodi, antti.tolli, jarkko.kaleva\} @oulu.fi, p.shariatpanahi@ut.ac.ir

    Parts of this work has been submitted in the IEEE ISWCS, Oulu, Finland, 2019, the IEEE WCNC, Seoul, South Korea, 2020. This work was supported by the Academy of Finland under grants no. 319059 (Coded Collaborative Caching for Wireless Energy Efficiency) and 318927 (6Genesis Flagship).

[^1]:    ${ }^{1}$ In this paper, we assume all D2D user groups $\mathcal{D}(t)$ are served using time-division multiplexing. Further improvement can be achieved by allowing parallel mutually interfering transmissions within multiple groups.

[^2]:    ${ }^{2}$ Symmetric rate is imposed to minimize the time needed to receive both messages $\tilde{X}_{1,3}$ and $\tilde{X}_{2,3}$.

[^3]:    ${ }^{3}$ For convenience, the superscript $\mathcal{S}=\{1,2,3,4\}$ in $\mathbf{w}_{\mathcal{T}}^{\mathcal{S}} \tilde{X}_{\mathcal{T}}^{\mathcal{S}}$ has been omitted in this example.

[^4]:    ${ }^{5}$ Another interpretation for [10] is that the beamformer $\mathbf{w}_{\mathcal{D}}^{\mathcal{S}}$ is assumed to be matched to the weakest user in subset $\mathcal{D}$ without rate loss for other users with better channel condition in the subset.

[^5]:    ${ }^{6}$ Due to an excessively large number of different subset combinations, performing the exhaustive search is computationally challenging ( $\sim 2^{10}$ different cases must be evaluated); thus, only the two thresholds are being compared.

