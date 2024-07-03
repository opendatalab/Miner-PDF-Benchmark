# Maximum-Rate Optimization Of Hybrid Intelligent Reflective Surface And Relay Systems

Alberto Rech, Federico Moretto, and Stefano Tomasin Department of Information Engineering, University of Padova, Italy.

Emails: rechalbert@dei.unipd.it, federico.moretto.1@unipd.it, tomasin@dei.unipd.it arXiv:2109.08378v1 [eess.SP] 17 Sep 2021 Abstract**—We consider a wireless communication system,**
where a transmitting source is assisted by both a reconfigurable intelligent reflecting surface (IRS) and a decode-and-forward half-duplex relay (*hybrid IRS-relay scheme***) to communicate with** a destination receiver. All devices are equipped with multiple antennas, and transmissions occur in two stages. In stage 1, the source splits the transmit message into two sub-messages, transmitted to the destination and the relay, respectively, using block diagonalization to avoid interference. Both transmissions will benefit from the IRS. In stage 2, the relay re-encodes the received sub-message and forwards it (still through the IRS) to the destination. We optimize power allocations, beamformers, and configurations of the IRS in both stages, in order to maximize the achievable rate at the destination. We compare the proposed hybrid approach with other schemes (with/without relay and IRS), and confirm that high data rate is achieved for the hybrid scheme in case of optimal IRS configurations.

Index Terms**—Beamforming, IRS, MIMO, rate optimization,**
relay.

## I. Introduction

A reconfigurable intelligent reflecting surface (IRS) is a programmable metasurface that can alter the phase and amplitude of an impinging signal by dynamically adjusting the reflection coefficients of its elements. Recently, IRSs have drawn enormous research interest as a promising technology for the sixth generation (6G) of cellular networks [1], due to their ability of controlling the wireless propagation environment. Before the advent of IRSs, relays have been studied and used in cellular networks to increase coverage and improve the received signal quality. Among various solutions, decode-and-forward (DF)
relays are half-duplex (HD) devices that alternate two stages, one wherein they receive a message from the source, and a second wherein they re-encode the message and transmit it to the destination.

The alternative use of IRSs and relays has been widely investigated. In [2], IRSs and single-antenna DF relays are compared in terms of power consumption, whereas in [3] the energy efficiency of systems using IRSs is compared to a system with multi-antenna amplify-and-forward (AF) relays. A comparison between IRSs and DF HD/full-duplex (FD) relays is presented in [4], proving that sufficiently large IRSs yield higher spectral and energy efficiency than relay-aided systems.

Nevertheless, due to the expensive deployment of IRSs, *hybrid* IRS-relay systems, wherein both devices are jointly adopted, will be a cost-effective solution for the near future of smart electromagnetic environments. In [5], the combination of a HD DF relay and an IRS is investigated and tight upper bounds for the achievable rate (AR) are derived. A hybrid system with a FD DF relay is studied in [6], showing that the performance further improves, as long as the relay self-interference is low.

However, both works consider source and destination equipped with a single antenna each. In [7], a system wherein an IRS
assists both a relay and a destination (and the source has no direct link with either the relay and the destination) is considered, with source, relay, and destination again having all one antenna each. For a system with multiple relays, still in the presence of an IRS, the selection of one relay to assist communication between a source and a destination is solved by machine-learning in [8].

In this paper, we consider a hybrid IRS-relay multipleinput multiple-output (MIMO) system, which generalizes the systems considered in [5], [6], and [7], as we now assume that all devices are equipped with multiple antennas. Moreover, contrary to [7], we also consider the link between the source and the relay. The relay is HD and operates in the DF mode.

We propose a transmission protocol operating in two stages.

In stage 1, the source splits the transmit message into two sub-messages, transmitted to the destination and the relay, respectively, using block diagonalization to avoid interference.

Both transmissions will benefit from the IRS. In stage 2, the relay re-encodes the received sub-message and forwards it (still through the IRS) to the destination. We optimize power allocations, beamformers, and configurations of the IRS in both stages, to maximize the AR at the destination. In particular, we split the AR optimization problem into two subproblems, one for each stage, then coupled by the choice of the IRS configuration and the power split between the signal for the relay and the destination in stage 1. Lastly, we compare the proposed hybrid approach with other schemes (with/without relay and IRS), and confirm that a high data rate is achieved for the hybrid scheme in case of optimal IRS configuration.

The rest of this paper is organized as follows. Section II describes transmission characteristics and the two-stage protocol.

In Section III we formalize the maximum-rate optimization problem and describe the alternating optimization solution. In Section IV we discuss numerical results before the conclusions are taken in Section V.

Notation: Scalars are denoted by italic letters, vectors and matrices by boldface lowercase and uppercase letters, respectively, and sets are denoted by calligraphic uppercase letters.

diag(a) indicates a square diagonal matrix with the elements of a on the principal diagonal. AH denotes the conjugate



transpose of matrix A. E[·] denotes the statistical expectation.

Ix is the identity matrix of size x.

## Ii. System Model

We consider the narrowband single-user MIMO communication system shown in Fig. 1, wherein the transmission from a source (S) to a destination (D) is assisted by both a relay (R) and an IRS (I). We assume that S and R have maximum transmit powers PS and PR, respectively.

S, D, and R are equipped with uniform linear arrays (ULAs)
with NS, ND, and NR antennas, respectively, whereas I is a uniform planar array (UPA) with NI passive reflective elements.

We denote with HSI ∈ C
NI×NS and HSR ∈ C
NR×NS the S-R and S-I channels, with HRI ∈ C
NI×NR and HRD ∈
C

ND×NR the R-I and R-D channels, and with HIR = HTRI
and HID ∈ C
ND×NIthe I-R and I-D channels. We consider narrowband mmWave channels [9], each having M non-lineof-sight (NLOS) components. Hence, channel matrix HXY
between transmitter X and receiver Y is

$$\mathbf{H}_{\rm XY}=\frac{1}{\sqrt{M}}\sum_{m=1}^{M}g_{m}\rho(d)\mathbf{a}\left(\mathbf{\omega}_{\rm X,}m\right)\mathbf{a}^{H}\left(\mathbf{\omega}_{\rm Y,}m\right),\tag{1}$$
$\text{sin}\,x\text{sin}\,y$ 4. 
where gm *∼ CN* (0, 1) is the gain of the m-th path, ρ(d)
is the path loss attenuation factor, with d being the distance between X and Y, ω·,m = (ξ·,m, ψ·,m) is the vector of azimuth (ξ·,m) and elevation (ψ·,m) angles, and a (ω·,m) =
1*, . . . , e*jπ[x sin(ψ·,m) cos(ξ·,m)+y sin(ψ·,m) sin(ξ·,m)]*, . . .*Tis the array response vector for the m-th path, with 1 ≤ x ≤ NX −1 and 1 ≤ y ≤ NY − 1. We assume all devices operate in HD
and have perfect channel state information.

## A. Irs Model

Each element of the IRS acts as an omnidirectional antenna element that captures and reflects signals, introducing an attenuation and a phase shift on the baseband-equivalent signal. Following the model of [10], we denote with φn = An(θn)e jθn the reflection coefficient of the n-th IRS element, where θn ∈ [−*π, π*) is the induced phase shift and A2n(θn) ∈ [0, 1]
is the corresponding power attenuation factor. Indicating with x ∈ C
1×NIthe impinging signal on the IRS, the reflected signal y ∈ C
1×NIis y = Φx, with Φ = diag(φ1*, . . . , φ*NI),
which is the IRS reflection matrix, also denoted *IRS configuration*.

We consider the realistic baseband-equivalent model of the IRS described in [10], where

  **The described in [10], where**  $$A_{n}(\theta_{n})=(1-A_{\rm min})\left(\frac{\sin\theta_{n}-\zeta+1}{2}\right)^{\nu}+A_{\rm min},\tag{2}$$  **with $A_{\rm min}\geq0$, $\zeta\geq0$, and $\nu\geq0$ being IRS-specific.**
parameters, assumed to be identical for all IRS elements.

The phase shifts θn are controllable, thus indirectly controlling also the attenuations. Moreover, since continuousphase shifts are hardly implementable [11]-[12], we assume that the phase shifts are chosen from a discrete set n Fθ =
0, 2π 2 b *, . . . ,*
2π(2b−1)
2 bo, where b > 0 is the IRS phase shift resolution, i.e., the number of bits employed to control the phase shifts. The source has full control of the phase shifts, which can be optimized together with beamforming. B. Two-stage Communication Protocol For a HD DF relay, signal reception and transmission have to occur in two stages, here assumed to be of the same duration.

Stage 1: S splits the message into two sub-messages, and encodes/modulates them into the two signals xSR and xSD, intended for R and D, respectively. The two signals are precoded with block diagonalization (BD) precoders BSR and BSD before transmission, such that they are received only at the indented destination, without mutual interference. The signal transmitted by S is thus s = BSRxSR + BSDxSD. (3)
Then, for a given IRS configuration Φ1, the received signals at R and D are, respectively,

$$\begin{array}{c}{{\mathbf{y}_{R,1}=\underbrace{(\mathbf{H}_{\mathrm{SR}}+\mathbf{H}_{\mathrm{IR}}\mathbf{\Phi}_{1}\mathbf{H}_{\mathrm{SI}})\mathbf{B}_{\mathrm{SR}}}\,\mathbf{x}_{\mathrm{SR}}+\mathbf{n}_{R,1},}}\\ {{\mathbf{\bar{H}}_{\mathrm{SR}}(\mathbf{\Phi}_{1})}}\\ {{\mathbf{y}_{D,1}=\underbrace{\mathbf{H}_{\mathrm{ID}}\mathbf{\Phi}_{1}\mathbf{H}_{\mathrm{SI}}\mathbf{B}_{\mathrm{SD}}}_{\tilde{H}_{\mathrm{SD}}(\mathbf{\Phi}_{1})}\mathbf{x}_{\mathrm{SD}}+\mathbf{n}_{D,1},}}\end{array}$$

where H˜SR(Φ1) (H˜SD(Φ1)) is the S-R (S-D) equivalent channel matrix (we highlight their dependency on the IRS configuration), and nR,1 ∼ CN 0, σ2INR
(nD,1 ∼
CN 0, σ2IND
) is the complex Gaussian noise vector at R
(D).

Stage 2: S remains silent, while R decodes the submessage received by S in stage 1 and re-encodes/re-modulates it into the signal xRD. Then, R transmits xRD to D with the IRS using a new configuration Φ2. D receives the signal vector

$$\mathbf{y}_{D,2}=\underbrace{\left(\mathbf{H}_{\text{RD}}+\mathbf{H}_{\text{ID}}\mathbf{\Phi}_{2}\mathbf{H}_{\text{RI}}\right)\mathbf{x}_{\text{RD}}+\mathbf{n}_{D,2}},\tag{6}$$

where H˜ RD(Φ2) is the R-D equivalent channel matrix, and nD,2 ∼ CN 0, σ2IND
is the complex Gaussian noise vectors at D.

Note that, in both stages, the IRS configurations Φ1 and Φ2 are provided by S, which has full control of the phase shifts.

## Iii. Maximum-Rate Problem

We now first derive the AR and then, we formulate the problem of maximizing the AR.

## A. Achievable Rate

For the first stage, the transmit beamformers BSD and BSR are chosen such that xSR and xSD do not generate interference at D and R, respectively. To this end, BD is applied (see [13]), using in general a reduced set of streams for the two links. Let HSD = USDΓSDVSD and the singular value decomposition (SVD) of HSD; a subset SSD of streams
(corresponding to diagonal elements of ΓSD) is selected for transmission to D. The BD beamformer for transmission to R
is BSR = NSDB0SR, where NSD collects the columns of VSD
with indices not in the set SSD, while B0SR is the capacityachieving precoder for the resulting S-R channel. A similar procedure is applied for the definition of the S-D precoder BSD, for which SSR streams are selected. We must also have |SSR| + |SSR| ≤ NS. Lastly, xSD and xSR, are zero-mean complex Gaussian vectors with independent entries of size |SSD| and |SSR|.

For the second stage, R applies capacity-achieving precoding, and xRD zero-mean complex Gaussian vectors with independent entries of size NR.

As a result, the S-D MIMO equivalent channel can be decomposed into |SSD| independent parallel additive white Gaussian noise (AWGN) channels with gains {γSD(i)}.

1 The capacity of the S-D channel is therefore

$$C_{\mathrm{SD}}=\sum_{i\in{\mathcal{S}}_{\mathrm{SD}}}\log_{2}\left[1+\gamma_{\mathrm{SD}}(i){\frac{P_{\mathrm{SD}}(i)}{\sigma^{2}}}\right],\qquad\qquad(7)$$

where PSD(i) is the power allocated to channel i. Similarly, the S-R and R-D channels can be decomposed into |SSR| and |SRD| parallel AWGN channels, with gains {γSR(i)} and
{γRD(i)}, respectively, and the S-R and R-D capacities CSR
and CRD can be written as in (7), where subscript SD is replaced by subscripts SR and RD, respectively.

The AR of the considered two-stage scheme is therefore

$$C_{\rm HYB}=\frac{1}{2}(C_{\rm SD}+\min\{C_{\rm SR},C_{\rm RD}\}),\tag{8}$$  where the two stages requires twice the time of direct trans
where the two stages requires twice the time of direct transmission, hence the factor 1/2.

Note that for a transmission using only the relay, the AR
Crelay is still given by (8), with the IRS switched off (An(θ) =
0, ∀θ). A transmission using only the IRS can instead be performed in a single stage and the AR is CIRS = CSD. In both cases, no BD is needed. Note also that IRS- or relay-only transmissions occur if no streams are selected for the S-R or S-D links, i.e., if |SSR| = 0 or |SSD| = 0, respectively.

1γSD(i) is the i-th singular value of H˜SD(Φ1)H˜ H

$${}_{1})H_{\mathrm{SD}}^{H}(\Phi_{1}).$$

## B. Optimization Problem

With this choice of beamformers, we are left with the problem of optimizing a) the transmit power, b) the IRS
configurations in both stages, and c) the set of streams assigned to R and D in stage 1. The AR maximization problem can be formalized as follows:

argmax Φ1,Φ2 SSD,SSR,SRD {PSD(i)},{PSR(j)},{PRD(k)} (CSD + CSR), (9a) s.t. Φk = diag(φ1,k, . . . , φNI,k), k = 1, 2, (9b) φn,k = An,k(θn,k)e jθn,k, 1 ≤ n ≤ NI, k = 1, 2, (9c) θn,k ∈ Fθ, 1 ≤ n ≤ NI, k = 1, 2, (9d) X i∈SSD PSD(i) + X j∈SSR PSR(j) ≤ PS, (9e) X k∈SRD PRD(k) ≤ PR, (9f) i∈SSD PSD(i) + X j∈SSR PSR(j) + X k∈SRD PRD(k) ≤ Pmax, X (9g) CSR ≤ CRD (9h) SSD, SSR ∈ {1, . . . , NS}, (9i) 0 < |SSD| + |SSR| ≤ NS. (9j)
$$(9\mathrm{a})$$
 (9b)  $\text{}$  (9c)  (9d)  (9e)  $\text{}$  (9f)
 $\mathrm{max}$,  (9g)  (9h)  (9i)  (9j)
The minimum in (8) is now reflected by constraint (9h).

Constraints (9b)-(9d) are related to the control of IRS phase shifts, and constraints (9e) and (9g) are power constraints at the devices, and we added the total power constraint Pmax. This constraint will make the comparison with schemes using only the IRS more fair, by imposing Pmax the maximum power for S. Constraints (9i)-(9j) are relative to the stream assignment.

## C. Alternating Optimization Solution

Notice that constraint (9c) makes the problem non-convex, thus we resort to an alternating optimization solution, where we optimize over the IRS configurations and stream sets, and for each considered configuration we optimize the transmission powers.

For fixed IRS configurations and stream selections, the optimization problem (9) becomes

$$\begin{array}{c c}{{\mathrm{\boldmath~\arg\operatorname{~}~}\left(C_{\mathrm{SD}}+C_{\mathrm{SR}}\right),}}&{{\mathrm{s.t.~(9e)-(9h).}}}\\ {{\{P_{\mathrm{SD}}(i)\},\{P_{\mathrm{SR}}(j)\},\{P_{\mathrm{RD}}(k)\}}}&{{}}\end{array}$$

Observe that, due to constraint (9h), the problem is still nonconvex. However, the powers in stage 1 and stage 2 are coupled only through the constraint (9g). We can decouple the two problems by introducing the auxiliary variable PR,eff such that

$$\sum_{k\in{\mathcal{S}}_{\mathrm{RD}}}P_{\mathrm{RD}}(k)=P_{\mathrm{R,eff}},$$
$$(111)$$

so that the power that can be effectively used by S is, from
(9e), (9f), and (9g), as PS,eff = min{PS, Pmax −PR,eff}. With these new definitions, (10) can be split into the two (coupled)
problems, for given PR,eff,

$$C_{\rm RD}^{*}=\max_{\{P_{\rm RD}(k)\}}C_{\rm RD},\quad\mbox{s.t.}\sum_{k\in{\cal S}_{\rm RD}}P_{\rm RD}(k)=P_{\rm R,eff},\tag{12a}$$  and
and

$$\begin{array}{c}\mbox{argmax}\\ \{P_{\rm SD}(i)\},\{P_{\rm SR}(j)\}\end{array}\frac{1}{2}\left(C_{\rm SD}+C_{\rm SR}\right),\tag{13a}$$
s.t. $C_{\rm SR}\leq C_{\rm RD}^{*}$, (13b) $$\sum_{i\in{\cal S}_{\rm SD}}P_{\rm SD}(i)+\sum_{j\in{\cal S}_{\rm SR}}P_{\rm SR}(j)=P_{\rm S,eff}.$$ (13c)  Note that (12) and (13) are convex optimization problems.  
and, therefore, they can be solved in closed-form, as detailed in the next sub-section.

Then, we need to optimize the IRS reflection coefficients Φ1 and Φ2, the stream sets SSR, SSD, and SRD, and the auxiliary variable PR,eff, in what turns out to be a non-convex problem.

Thus, we resort to the discrete genetic algorithm (GA) [14],
which operates iteratively, solving sub-problems (13) and (12)
for given IRS configurations, power PR,eff, stream sets SSR, SSD, and SRD at each iteration.

## D. Decoupled Problem Solution

Solution of Problem (12): Since the capacity CSR is upper bounded by C
∗
RD from (13b), we first optimize the transmit powers {PRD(k)} at R, given PR,eff. Indeed, (12)
can be solved via the standard waterfilling algorithm [13] on channels with gains {γRD(i)} and total power PR,eff.

Solution of Problem (13): The Lagrangian function of
(13) is (with λ1 and λ2 multipliers)

$$\mathcal{L}=(C_{\text{SD}}+C_{\text{SR}})-\lambda_{2}\left(C_{\text{SR}}-C_{\text{RD}}^{*}+s\right)$$ $$\quad-\lambda_{1}\left(\sum_{i\in\mathcal{S}_{\text{SD}}}P_{\text{SD}}(i)+\sum_{j\in\mathcal{S}_{\text{SR}}}P_{\text{SR}}(j)-P_{\text{S,eff}}\right),\tag{14}$$

where s ≥ 0 is an additional slack variable. Setting to zero the derivative of the Lagrangian function, we obtain the following stationary points

$$P_{\mathrm{SD}}(i)=\frac{1}{\ln(2)\lambda_{1}}-\frac{1}{\gamma_{\mathrm{SD}}(i)},\;P_{\mathrm{SR}}(j)=\frac{1}{\ln(2)\lambda_{1}}-\frac{1}{\gamma_{\mathrm{SR}}(j)},\tag{15}$$

with λ1 such that (13c) is satisfied.

Now, letting s = C
∗
RD − CSR, if s ≥ 0 we have found the optimal solution. If instead s < 0, then we must assume s = 0, i.e., the S-R rate in stage 1 equals the R-D rate in stage 2. Consequently, we allocate the minimum power that satisfies this constraint to the S-R link, while all the remaining power is assigned to the S-D link. Hence, we first solve the following problem

$$\begin{array}{c}\mbox{argmin}\sum\limits_{j\in{\cal S}_{\rm SR}}P_{\rm SR}(j),\quad\mbox{s.t.}C_{\rm SR}=C_{\rm RD}^{*},\end{array}\tag{16}$$



with the Lagrangian multipliers method, providing

$$P_{\rm SR}^{*}(j)=\left[\left(\frac{2^{C_{\rm RD}^{*}}}{\prod_{j\in{\cal S}_{\rm SR}}\gamma_{\rm SR}(j)}\right)^{\frac{1}{|{\cal S}_{\rm SR}|}}-\frac{1}{\gamma_{\rm SR}(j)}\right]^{+},\tag{17}$$

where (x)
+ = x if x ≥ 0, while (x)
+ = 0 otherwise. For the obtained optimal powers PSR(j)
∗, we solve

$$\begin{array}{c}\mbox{argmax}C_{\rm SD},\quad\mbox{s.t.(13c)},\\ \{P_{\rm SD}(i)\}\end{array}$$  which is similar to (12) and can be solved likewise.  
IV. NUMERICAL RESULTS
In this section, we assess the performance of the proposed protocol. S, R, D, and I have coordinates (0, 0, 3), (10, −10, 3),
(20, 0, 1.5), and (10, yI, 3) m, respectively (see Fig. 1), and yIis a parameter to be set. We consider M = 2 NLOS
components for each mmWave link. S, R, and D are equipped with ULAs of NS = 16, NR = 8, and ND = 4 antennas, respectively, whereas the IRS is an UPA with NI = 36 elements and parameters (see [10]) Amin = 0.2, ζ = 0.43π, and ν = 1.6. Angles in the array response vector are chosen according to a uniform random distribution, in particular, ψ·,m ∼ U[0, 2π) and ξI,m ∼ U[0*, π/*2) for the IRS, while ξ·,m = 0 for other devices with ULA. The transmit signalto-noise ratio (SNR) is Pmax/σ2 = 10 (10 dB). The path loss term is modelled as ρ(d) = K0(d/d0)
−α/2, where K0 = ρ(d0) = 0 dB is the path loss at the reference distance d0 = 10 m, and α = 5.76 is the path loss exponent [15]. We compare five schemes: the proposed optimized hybrid IRSrelay scheme (Hyb. Opt.), a hybrid scheme with random IRS configuration (Hyb. Rand.), a scheme without relay and an optimized IRS (IRS Opt.), a scheme with a random IRS (IRS Rand.), and a scheme without IRS and a relay
(Relay).

Fig. 2 shows the AR as a function of the IRS phase shift resolution b for yI = 20 m and PS/Pmax = 0.5. For b = 0 we consider a fixed IRS configuration with phase shifts θn = π,





∀n, corresponding to the maximum value of A(·). For all schemes, the AR saturates with just b = 1 or 2 bits per element, thus, as already observed in the literature, a very limited number of configurations are enough to achieve the gains provided by the IRS. In the following, we will consider b = 2. The schemes with randomly configured IRS show a penalty for higher resolution, since configurations with lower gains A(·) are used.

Fig. 3 shows the AR as a function of the fractional available power at S, i.e., PS/Pmax for yI = 20 m. The Hyb. Opt.

scheme provides the highest AR for all values of PS/Pmax. Still, for low PS/Pmax, the relay has a considerable fraction of power, thus the Relay scheme is close to optimal. Instead, at high PS/Pmax, the constraint on CRD limits the AR at the relay, and the IRS Opt. scheme attains higher performance. The IRS Rand. scheme yields very poor performance, due to the absence of the relay and the random configuration of the IRS.

Fig. 4 shows the AR as a function of the IRS distance



yI, when PS/Pmax = 0.5. For small yI values, the IRS
link is dominant with respect to the relay link, making the Hyb. Opt. scheme transmit exclusively towards the IRS,
thus avoiding the half-rate penalty of the two-stage protocol, and approaching the AR. On the other hand, the IRS assistance becomes marginal as yI grows, resulting in similar performance between Hyb. and Relay schemes.

Finally, Fig. 5 shows the AR as a function of the number of reflecting elements NI, for PS/Pmax = 0.5 and yI = 20 m.

As expected, due to the huge beamforming gain introduced by large IRSs, the AR grows with the number of reflecting elements.

## V. Conclusions

In this paper, we considered an hybrid IRS-relay system, optimizing power allocation, IRS configurations, and stream sets to maximize the AR. Numerical results showed that, in the considered scenarios, large phase-optimized IRSs yield higher ARs than systems using only either the relay or the IRS. Indeed, the best performance is achieved by different uses of the relay and the IRS under different positions of the devices or power split among the source and the relay. This suggests that the proposed hybrid solution, which is able to switch among the various uses, is always advantageous.

REFERENCES

[1] W. Long, R. Chen, M. Moretti, W. Zhang, and J. Li, "A promising technology for 6G wireless networks: Intelligent reflecting surface," J. of Commun. and Inf. Net., vol. 6, no. 1, pp. 1–16, 2021.

[2] E. Bjornson, O. Ozdogan, and E. G. Larsson, "Intelligent reflecting surface versus decode-and-forward: How large surfaces are needed to beat relaying?" *IEEE Wireless Commun. Lett.*, vol. 9, no. 2, pp. 244–
248, Oct. 2020.

[3] C. Huang, A. Zappone, G. C. Alexandropoulos, M. Debbah, and C. Yuen, "Reconfigurable intelligent surfaces for energy efficiency in wireless communication," *IEEE Trans. on Wireless Commun.*, vol. 18, no. 8, pp. 4157–4170, Jun. 2019.

[4] M. Di Renzo *et al.*, "Reconfigurable intelligent surfaces vs. relaying:
Differences, similarities, and performance comparison," *IEEE Open J.* of the Commun. Soc., vol. 1, pp. 798–807, Jun. 2020.
[5] Z. Abdullah, G. Chen, S. Lambotharan, and J. A. Chambers, "A
hybrid relay and intelligent reflecting surface network and its ergodic performance analysis," *IEEE Wireless Commun. Lett.*, vol. 9, no. 10, pp.

1653–1657, Oct. 2020.

[6] ——, "Optimization of intelligent reflecting surface assisted full-duplex relay networks," *IEEE Wireless Commun. Lett.*, vol. 10, no. 2, pp. 363–
367, Feb. 2021.

[7] I. Yildirim, F. Kilinc, E. Basar, and G. C. Alexandropoulos, "Hybrid RIS-empowered reflection and decode-and-forward relaying for coverage extension," *IEEE Commun. Lett.*, pp. 1–1, 2021.

[8] C. Huang, G. Chen, Y. Gong, M. Wen, and J. A. Chambers, "Deep reinforcement learning based relay selection in intelligent reflecting surface assisted cooperative networks," *IEEE Wireless Commun. Lett.*,
pp. 1–1, 2021.

[9] M. R. Akdeniz *et al.*, "Millimeter wave channel modeling and cellular capacity evaluation," *IEEE J. on Sel. Areas in Commun.*, vol. 32, no. 6, pp. 1164–1179, 2014.

[10] S. Abeywickrama, R. Zhang, Q. Wu, and C. Yuen, "Intelligent reflecting surface: Practical phase shift model and beamforming optimization,"
IEEE Trans. Commun., vol. 68, no. 9, pp. 5849–5863, 2020.

[11] X. Tan, Z. Sun, J. M. Jornet, and D. Pados, "Increasing indoor spectrum sharing capacity using smart reflect-array," in *Proc. Int. Conf. on* Commun. (ICC). IEEE, May 2016.

[12] X. Tan, Z. Sun, D. Koutsonikolas, and J. M. Jornet, "Enabling indoor mobile millimeter-wave networks based on smart reflect-arrays," in *Proc.* Int. Conf. on Computer Commun. (INFOCOM). IEEE, Apr. 2018.

[13] N. Benvenuto, G. Cherubini, and S. Tomasin, *Algorithms for Communication Systems and their applications*, 2nd ed. Wiley, 2021.

[14] J. H. Holland, *Adaptation in Natural and Artificial Systems: An Introductory Analysis with Applications to Biology, Control and Artificial* Intelligence. MIT Press, 1992.

[15] Y. Azar *et al.*, "28 GHz propagation measurements for outdoor cellular communications using steerable beam antennas in new york city," in Proc. Int. Conf. on Commun. (ICC). IEEE, Jun. 2013, pp. 5143–5147.