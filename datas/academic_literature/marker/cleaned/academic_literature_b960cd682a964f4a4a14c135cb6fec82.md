# Model-Based End-To-End Learning For Wdm Systems With Transceiver Hardware Impairments

Jinxiang Song, *Student Member, IEEE*, Christian Hager, ¨ *Member, IEEE*, Jochen Schroder, ¨ *Member, IEEE*,
Alexandre Graell i Amat, *Senior Member, IEEE*, and Henk Wymeersch, *Senior Member, IEEE*
(Invited Paper)
Abstract**—We propose an autoencoder (AE)-based transceiver**
for a wavelength division multiplexing (WDM) system impaired by hardware imperfections. We design our AE following the architecture of conventional communication systems. This enables to initialize the AE-based transceiver to have similar performance to its conventional counterpart prior to training and improves the training convergence rate. We first train the AE in a singlechannel system, and show that it achieves performance improvements by putting energy outside the desired bandwidth, and therefore cannot be used for a WDM system. We then train the AE in a WDM setup. Simulation results show that the proposed AE significantly outperforms the conventional approach. More specifically, it increases the spectral efficiency of the considered system by reducing the guard band by 37% and 50% **for a rootraised-cosine filter-based matched filter with** 10% and 1% **roll-off,**
respectively. An ablation study indicates that the performance gain can be ascribed to the optimization of the symbol mapper, the pulse-shaping filter, and the symbol demapper. Finally, we use reinforcement learning to learn the pulse-shaping filter under the assumption that the channel model is unknown. Simulation results show that the reinforcement-learning-based algorithm achieves similar performance to the standard supervised endto-end learning approach assuming perfect channel knowledge.

Index Terms**—Autoencoders, deep learning, digital signal processing, end-to-end learning, reinforcement learning, wavelengthdivision multiplexing.**

## I. Introduction

The ever-growing demand for higher data rates drives the rapid development of optical fiber communication systems.

One of the most important developments is wavelength division multiplexing (WDM) transmission, where parallel data channels are transmitted on different wavelengths simultaneously. The throughput of modern WDM systems often exceeds tens of Tb/s with more than 100 channels [2]. However, the overall bandwidth of fiber systems is limited by the bandwidth of erbium-doped fiber amplifiers (EDFAs) that periodically amplify the signals along the fiber link [3]. Optimizing the spectral efficiency (SE), i.e., the number of bits that can be transmitted per unit time and frequency, is therefore crucial to further increase the throughput of fiber optical systems.

Over the last decade, most works have focused on increasing the per-channel SE via advanced modulation formats using coherent detection. The fiber nonlinearity and hardware impairments, such as the effective number of bits (ENOBs)
of the digital-to-analog converter (DAC), however, severely limit the per-channel SE. Furthermore, spectrum gaps between individual channels, which are often referred to as guard bands, waste significant bandwidth and limit the overall system throughput. Hence, the guard bands between channels need to be minimized. The most promising solution has been the application of flexible grids, which allows for transmission with flexible channel bandwidths thus enabling simultaneous transmission of mixed bit rates [4] and allowing to reduce SE loss from guard bands for optical filtering.

To minimize the guard bands between channels, it is common to employ pulse shaping to create a near-rectangular spectrum in the frequency domain with a bandwidth close to the symbol rate. However, in practice, generating a rectangular spectrum is difficult due to the finite pulse-shaping (PS) filter and transceiver hardware impairments, requiring computation expensive digital signal processing to eliminate performance degradation caused by inter-channel interference (ICI) [5]. Guard bands therefore remain a major contributor to SE loss in WDM systems.

In recent years, the rapid improvement of machine learning techniques has led to a resurgence of interest in applying deep learning techniques for communication systems [29],
[30]. Most work has focused on supervised learning for a specific functional block, e.g., modulation recognition [31],
carrier recovery [32], and fiber nonlinearity mitigation [33],
with the aim of finding better performing (or less complex) algorithms by replacing the conventional model-based methods with neural networks (NNs). In contrast to focusing on specific functional blocks, *end-to-end learning* has been proposed to design the transmitter and receiver jointly [6]. The key idea is to interpret the transceiver design as a reconstruction task, whereby the transmitter and the receiver can be implemented as an autoencoder (AE) and thus jointly optimized. This method has led to several applications for both wireless [6],
[9], [10] and optical communications [21], [22], [28]. A broad, but non-exhaustive overview of existing work is listed in Table I. We observe that (i) a majority of works relate to wireless rather than optical communication; (ii) geometric constellation shaping for different channels and applications TABLE I: Applications of end-to-end AE-learning in communication systems

2



| Ref.                                                                                        | year   | Application                 | isolated ch.   | ICI ch.   | sim.                                                         | exp.                                                       | Description   |
|---------------------------------------------------------------------------------------------|--------|-----------------------------|----------------|-----------|--------------------------------------------------------------|------------------------------------------------------------|---------------|
| [6]                                                                                         | 2017   | geom. shaping               | X              | X         | const. mapper/demapper training over an AWGN channel         |                                                            |               |
| [7]                                                                                         | 2017   | geom. shaping               | X              | X         | const. mapper/demapper training for PAPR reduction           |                                                            |               |
| [8]                                                                                         | 2017   | geom. shaping & precoding   | X              | X         | MIMO precoding/decoding                                      |                                                            |               |
| [9]                                                                                         | 2017   | geom. shaping               | X              | X         | X                                                            | mapper/demapper training in sim., demapper tuning in exp.  |               |
| [10]                                                                                        | 2018   | geom. shaping               | X              | X         | mapper/demapper training for OFDM system                     |                                                            |               |
| [11]                                                                                        | 2018   | geom. shaping               | X              | X         | mapper/demapper training over a learned channel via GAN      |                                                            |               |
| [12]                                                                                        | 2018   | geom. shaping               | X              | X         | X                                                            | mapper/demapper training without knowing the channel model |               |
| [13]                                                                                        | 2019   | geom. shaping               | X              | X         | mapper/demapper training for PAPR reduction                  |                                                            |               |
| [14]                                                                                        | 2019   | joint channel/source coding | X              | X         | Joint channel and source coding/decoding                     |                                                            |               |
| [15]                                                                                        | 2019   | geom. & prob. shaping       | X              | X         | Joint geom. and prob. shaping/demapping                      |                                                            |               |
| [16]                                                                                        | 2020   | geom. shaping & coding      | X              | X         | X                                                            | mapper/demapper learning and error correction code design  |               |
| [17]                                                                                        | 2020   | geom. shaping               | X              | X         | mapper/demapper training for OFDM and multi-user system      |                                                            |               |
| [18]                                                                                        | 2021   | geom. shaping               | X              | X         | mapper/demapper training for OFDM system                     |                                                            |               |
| [19]                                                                                        | 2021   | geom. shaping & waveform    | X              | X         | X                                                            | Joint transceiver training                                 |               |
| [20]                                                                                        | 2018   | geom. shaping & waveform    | X              | X         | X                                                            | Joint tranceiver learning for IM/DD system                 |               |
| [21]                                                                                        | 2018   | geom. shaping               | X              | X         | mapper/demapper training for the nonlinear fiber channel     |                                                            |               |
| [22]                                                                                        | 2018   | geom. shaping               | X              | X         | mapper/demapper training for the fiber channel               |                                                            |               |
| [23]                                                                                        | 2019   | geom. shaping               | X              | X         | mapper/demapper training for optimizing GMI                  |                                                            |               |
| [24]                                                                                        | 2019   | geom. shaping & waveform    | X              | X         | X                                                            | Joint transceiver learning for IM/DD system                |               |
| [25]                                                                                        | 2020   | geom. shaping               | X              | X         | mapper/demapper training for optimizing GMI                  |                                                            |               |
| [26]                                                                                        | 2020   | geom. shaping & waveform    | X              | X         | Joint transceiver learning for single channel transmission   |                                                            |               |
| [27]                                                                                        | 2020   | Prob. shaping               | X              | X         | Prob. shaping                                                |                                                            |               |
| [28]                                                                                        | 2021   | geom. shaping               | X              | X         | mapper/demapper training for varying SNR and laser linewidth |                                                            |               |
| [1]                                                                                         | 2021   | geom. shaping & waveform    | X              | X         | X                                                            | Joint transceiver design for superchannel systems          |               |
| This work                                                                                   | 2021   | geom. shaping & waveform    | X              | X         | X                                                            | Joint transceiver design for densely-spaced WDM systems    |               |
| isolated ch.: the channel does not suffer from ICI; ICI ch.: channel that suffers from ICI. |        |                             |                |           |                                                              |                                                            |               |

has been the main focus; (iii) there are few experimental validations. Studies that also learn waveforms and equalizers are limited to [19], [20], [26]. In [20], the whole transceiver is implemented as an AE, and transmission is demonstrated over a short-haul intensity modulation/direct detection (IM/DD)
system. However, the NN in [20] is used as a "black-box" and it is difficult to interpret the learned solution. In [26], the transmitter is implemented as a trainable constellation mapper combined with a trainable PS filter, and it is shown that the PS
filter can be learned to mitigate chromatic dispersion and Kerr effect. An explicit low-pass filter is used to reduce information loss and thus avoid out-of-band (OOB) emissions. A related approach has recently been applied in [19], where flexible constellations and waveforms for wireless dispersive channels under OOB power leakage constraints were learned.

In this paper, we apply end-to-end learning to an multichannel WDM system. Similar to [19], [26] (for a singlechannel system), we consider designing several transceiver blocks —constellation mapper, PS filter, digital pre-distortion
(DPD), and demapper—jointly. Such an AE design incorporates the expert domain knowledge of conventional communication systems and therefore allows for (i) training speed improvements via meaningful parameter initialization and (ii) performance gain explanation through an ablation study. The main contributions of this paper are:
- We propose a novel end-to-end AE for WDM transceivers with non-ideal DAC and in-phase and quadrature modulator (IQM). We decompose the transmitter NN into a concatenation of small (simple) NNs, each corresponding to a functional block of a conventional communication system. Our approach differs from [19], [26] in terms of the considered hardware impairments and how OOB
emissions are accounted for: instead of a low-pass filter [26] or a constraint [19], we show that the AE
automatically learns to avoid/adapt OOB emissions to minimize the end-to-end loss.

- We highlight the potential pitfalls when using end-toend AE-learning for designing hardware-impaired communication systems. In particular, we show that when the AE is trained for a single-channel system, it achieves performance improvements by putting energy outside the desired signal bandwidth, which would cause large ICI in WDM systems when the channels are closely spaced. We demonstrate that if the AE is instead trained with three channels, it learns to limit ICI while still outperforming the considered baseline. However, care must be taken for the sampling rates or bandwidths used during training to match experimental constraints to avoid unrealistic gains.

- We conduct a thorough ablation study and show that the performance improvement of the AE-based system is ascribed to the optimization of the constellation mapper, the PS filter, and the demapper. Therefore, we show that our proposed method increases the interpretability compared to conventional AE-based systems. Additionally, we provide reproducible open-source implementations of our AEs and benchmark scheme.1
- We extend the model-free training algorithm proposed in [12], [34], so that the reinforcement learning (RL)
based transmitter training algorithm can be applied to train the PS filter, for which memory effects need to be considered. The resulting training algorithm is shown to achieve similar performance to the standard end-to-end learning approach assuming a perfect channel model. This opens the door toward experimental implementation of the proposed AE.

The remainder of this paper is structured as follows. In Section II, we give a brief introduction to DL basics and the concept of AE-based communications. Then, in Section III, we 1The complete source code to reproduce all results in this paper is available at https://github.com/JSChalmers/AE-Based-WDM-Transceivers.



introduce the generic setup of closely-spaced WDM systems and the main hardware limitations. Section IV introduces the proposed AE-based WDM system and simulation results are provided in Section V. Finally, the paper is concluded in Section VI.

Notation: Z, R, and C denote the sets of integers, real numbers, and complex numbers, respectively. Column vectors will be denoted with lower case letters in bold (e.g., x), with xn referring to the n-th entry in x, and x
(L)
n denotes the column vector consisting of (n−L)-th to (n+L)-th elements of x; |·| returns the absolute value of a real number, and |={x}| and |={x}| return the absolute value of the real and imaginary part of each element in x, respectively; (·)> and
(·)
H denote transpose and conjugate transpose, respectively.

Matrices will be denoted in bold capitals (e.g., X), and IN
denotes identity matrix of size N; [*a, b*]M is the M-fold Cartesian product of the interval [*a, b*]. Lastly, E{·} denotes the expectation operator.

## Ii. Deep Learning And Autoencoder-Based Communication Systems

In this section, we start by reviewing the general theory behind DL, followed by a brief introduction to the concept of AE-based communication systems. Then, we introduce the training of AE-based communication systems under two assumptions: (i) the channel model is known and differentiable, and (ii) the channel model is unknown or not differentiable.

## A. Neural Networks And Gradient-Based Learning

1) Feedforward NN: A feedforward NN with K layers is a parametric function f(r0; θ) : R
N0 → R
NK that maps an input vector r0 ∈ R
N0to an output vector rK ∈ R
NK through K sequential processing steps according to

$$r_{k}=f_{k}(r_{k-1};\theta_{k}),\quad k=\{1,\ldots,K\}\,,$$

where fk(rk−1; θk) : R
Nk−1 → R
Nk is the mapping carried out by the k-th layer. Here, the mapping of the k–th layer is defined by the set of parameters θk, and the entire NN
is defined by θ = {θ1*, . . . ,* θK}. A commonly used type of feedforward NN is the fully connected NN in which all layers have the form

$$f_{k}(\mathbf{r}_{k-1};\mathbf{\theta}_{k})=\sigma(W_{k}\mathbf{r}_{k-1}+\mathbf{b}_{k})\,,$$

where Wk ∈ R
Nk−1×Nk is a weight matrix, bk ∈ R
Nk is a bias vector, and σ(·) is a point-wise *activation* function.

Hence, the set of trainable parameters of the k-th layer is θk =
{Wk, bk}. An example of a fully connected NN is shown in the transmitter and the receiver in Fig. 1.

2) Gradient-based learning: Training of the NN can be performed in an iterative fashion with data-driven gradientbased optimization methods. Given a set of labeled training data *D ⊂ {X × Y}*, where X and Y are the input and output alphabets, the training objective is to find the set of parameters θ such that the average loss

$${\mathcal{L}}_{\mathcal{D}}(\mathbf{\theta})={\frac{1}{|{\mathcal{D}}|}}\sum_{(x,y)\in{\mathcal{D}}}\ell(f(x;\mathbf{\theta}),y)\qquad\qquad{\mathrm{(3)}}$$

between the NN output yˆ = f(x, θ) and the true label y ∈ Y
is minimized. Here, |D| is the size of the training data set and
`(f(x; θ), y) is the per-example loss function associated with returning the output yˆ = f(x; θ) when y is the true label.

In practice, when the training data set D is large, computing the gradients of the average loss over the whole training data set is computationally expensive, and the parameter set θ is commonly optimized by using stochastic gradient descent
(SGD) or its variants as follows. For each training iteration t, a minibatch Bt is sampled from D. Then, the parameter set θ is updated according to

## Θt+1 = Θt − Α∇Θlbt(Θt), (4)

where α > 0 is the learning rate. In practice, SGD sometimes suffers from slow convergence rate due to problems like small gradients at suboptimal values of θ. To improve the convergence rate of SGD, many variants of SGD using momentum [35] or adaptive learning rate [36] have been proposed. B. End-to-End AE Learning-Based Communication Systems

$$(2)$$

1) AE-based Communication Systems: End-to-end learning of AE-based communication systems was originally proposed in [6], where the transceiver for a given channel with channel law p(y|x) is implemented by a pair of NNs fτ : M →
C

N and fρ : C
N → [0, 1]M. Here, M = {1*, . . . , M*} is the message set, N is the number of complex channel uses, and τ and ρ are the sets of trainable NN parameters. Fig. 1 depicts the general setup of an AE-based communication system.

Transmitter: Given a message mk ∈ M, it is first encoded as an M-dimensional "one-hot" vector, where the mk-th element is 1 and all the others are 0.

2 Then, the transmitter NN
takes this "one-hot" vector as input and generates a vector of 2N outputs xk = fτ (mk), where the 2N outputs correspond to the real and imaginary part of the transmitted vectors. The average transmit power constraint E{||xk||2} ≤ NPT , where PT is the average transmit power per channel use, is enforced by a normalization layer [6].

Receiver: The symbol xk is sent over the channel in N
complex channel uses, after which yk is observed at the receiver. The receiver NN processes the received vector yk by generating an M-dimensional probability vector qk = fρ(yk),
where the components of qk can be interpreted as the estimated posterior probabilities of the messages. Finally, the transmitter generates the estimate of the transmitted message according to mˆ k = arg maxm[qk]m, where [x]m returns the m-th element of x.

2) End-to-End Training With a Known Channel Model:
To optimize the transmitter and receiver parameters, it is crucial to have a suitable optimization criterion. Due to the fact that the optimization relies on the empirical computation of gradients, a criterion like block error rate (BLER), i.e.,
Pr{mˆ k 6= mk}, cannot be used directly (as the BLER is not differentiable). Instead, a commonly used criterion is the crossentropy loss [6], defined by

4
$${\mathcal{L}}(\tau,\rho)=-\mathbb{E}\{\log[f_{\rho}(y_{k})]_{m_{k}}\},$$
where the dependence of L(τ , ρ) on τ is implicit through the distribution of the channel output yk, which is a function of the channel input fτ (mk).

The transmitter and receiver parameters are optimized in an iterative fashion as follows. In each training iteration t, the transmitter maps a minibatch of |Bt| randomly chosen uniformly distributed training examples to symbols and then sends them over the channel. The receiver takes the channel observations y1, *· · ·* , y|Bt| as input and generates |Bt| probability vectors fρ(y1), · · · , fρ(y|Bt|). Finally, the receiver computes the empirical cross-entropy loss associated with the |Bt| training examples according to

$$\mathcal{L}_{\mathcal{B}_{t}}(\boldsymbol{\tau},\boldsymbol{\rho})=-\frac{1}{|\mathcal{B}_{t}|}\sum_{k=1}^{|\mathcal{B}_{t}|}\log[f_{\boldsymbol{\rho}}(\boldsymbol{y}_{k})]_{m_{k}},\tag{6}$$  remitter and receiver parameters are optimized.  
and the transmitter and receiver parameters are optimized following (4). This training process is repeated iteratively until a certain criterion is satisfied (e.g., a fixed number of training iterations, or a fixed number of iterations during which the loss has not significantly decreased).

3) Training Without a Channel Model: In case the channel is unknown or not differentiable, e.g., an experimental channel, the transmitter optimization becomes challenging due to the fact that the gradient of the instantaneous channel transfer 2The "one-hot" encoding is the standard way of representing categorical values in most machine learning algorithms [37] and facilitates the minimization of the symbol error rate (SER). However, the dimension of the "one-hot" vector grows exponentially with the number of bits in each message and therefore increases the NN size. Alternative embeddings [38] and multi-hot sparse categorical cross-entropy loss can be used to alleviate this problem.

function is unknown, thus hindering the numerical computation of the transmitter gradients. One way to circumvent this limitation is to first learn a surrogate channel model, e.g., through supervised learning [39], [40] or an adversarial process [11], [41], and use the surrogate model to train the transmitter. However, the performance of the resulting system severely degrades if the surrogate model deviates from the real channel. A different approach based on a stochastic transmitter was proposed in [12], [34]. For this approach, the transmitter is regarded as an RL agent, and the transmitter and receiver are optimized in an alternating fashion which we review next.

Receiver training: The receiver training is similar as before. However, this time, the transmitter parameters τ are assumed to be fixed. At each training iteration, the transmitter maps a minibatch of |Bt| uniformly distributed training examples to symbols and sends them over the channel. The receiver takes the channel observations y1*, . . . ,* y|Bt| as input and generates |Bt| probability vectors fρ(y1)*, . . . , f*ρ(y|Bt|).

Then, the receiver takes one optimization step according to ρt+1 = ρt−α∇ρLBt
(τt, ρt), where τt is fixed during receiver training. This training process is repeated iteratively until a certain stop criterion is satisfied.

Transmitter training: For the transmitter optimization, the receiver parameters are assumed to be fixed. At each training iteration, the transmitter performs the symbol mapping as before. In order to allow for the transmitter gradients computation, a small Gaussian perturbation is applied such that x˜ = x + w, w ∈ CN (0, σ2 pIN ), is sent over the channel.

Therefore, the transmitter can be interpreted as stochastic and is described by

$$(S)$$

$$\pi_{\mathbf{\tau}}(\tilde{\mathbf{x}}_{k}|m_{k})=\frac{1}{(\pi\sigma_{p}^{2})^{N}}\exp\left(-\frac{||\tilde{\mathbf{x}}_{k}-f_{\mathbf{\tau}}(m_{k})||_{2}^{2}}{\sigma_{p}^{2}}\right).\tag{7}$$

Based on the received channel observations, the receiver computes per-example losses `k = − log([fρ(yk)]mk
), and sends them back to the transmitter. Finally, the transmitter parameters τ are updated according to τt+1 = τt−α∇τLBt
(τt),
where ∇τLBt
(τ ) is approximated by

$$\nabla_{\mathbf{\tau}}{\cal L}_{{\cal B}_{t}}(\mathbf{\tau})=\frac{1}{N_{T}}\sum_{k=1}^{N_{T}}\ell_{k}\nabla_{\mathbf{\tau}}\log\pi_{\mathbf{\tau}}(\tilde{\mathbf{x}}_{k}|m_{k}),\tag{8}$$

for which a theoretical justification can be found in [34].

Similar to the receiver training, the transmitter learning process is repeated iteratively until a certain stopping criterion is satisfied. Then, the alternating optimization continues again with the receiver learning.

## Iii. Wdm System And Main Hardware Limitations A. System Model

Fig. 2 illustrates the considered WDM system. For each channel, a sequence of |Bt| messages m ∈ M|Bt|, where M = {1*, . . . , M*}, are mapped individually to constellation points according to a constellation C ∈ CM, to form the sequence of baseband symbols x ∈ C|Bt|. The baseband symbols x are then upsampled to get u ∈ C|Bt|R, after which a PS filter is applied to get the discrete-time baseband signals



s ∈ C|Bt|R, where R is the upsampling rate.3 To mitigate the performance degradation caused by the hardware imperfections (in this paper ENOB of the DAC and IQM nonlinearity),
a DPD algorithm is applied. Then, the real and imaginary part of the pre-distorted signals y ∈ C|Bt|R are separately fed to the DACs of the in-phase and quadrature branches.

Finally, the DACs outputs ZI (t) and ZQ(t) are separately amplified to drive the IQM, where the driving voltages of the in-phase and quadrature branches are denoted by VI (t) and VQ(t), respectively. Similar to [42]–[44], the channel model we consider in this paper is restricted to a back-to-back setup, and only additive white Gaussian noise (AWGN) with constant power is added to simulate the noise introduced by the booster amplifier. At the receiver, the received signals are passed through an analog-to-digital converter (ADC), after which the digitized channel observations yˆ ∈ C|Bt|R are convolved with a matched filter (MF) and then down-converted with rate R.

Finally, the downsampled signals xˆ ∈ C|Bt|are individually mapped to the estimates mˆ ∈ M|Bt| of the transmitted messages.Note that, as optical filters and multiplexers would prevent close channel spacing due to their finite response, we assume that channels are combined using broadband passive couplers. Thus, there are no optical filters in our system; such a system is often referred to as *superchannel* system.

IQM Model: The coherent optical transmitter used for highorder modulation schemes such as M–QAM, M–PAM is often based on a dual parallel Mach-Zehnder modulator (MZM).

For an ideal dual parallel MZM biased at the null point, it has been shown that its transfer function becomes [45]

$$E(t)=E_{0}\left[\sin\left(\frac{\pi V_{I}(t)}{2V_{\pi}}\right)+j\sin\left(\frac{\pi V_{Q}(t)}{2V_{\pi}}\right)\right],\tag{9}$$  where $E_{0}$ is the amplitude of the magnitude of the electric 
field, Vπ is the required voltage difference to switch ON/OFF
the modulator, and VI (t) and VQ(t) are the driving voltage of the in-phase and quadrature branches, respectively. The intrinsic sinusoidal form of the MZM leads to strong signal distortions when driving with a high peak voltage Vp, which must be compensated, e.g., by pre-distortion with an *arcsin* function. Alternatively, one can use a low-driving voltage to operate in the near-linear regime of the modulator. However, this significantly increases the modulator loss, which results 3An upsampler with N× upsampling rate increases the sample rate by inserting N − 1 zeros between samples. Moreover, the transients from the convolution operation, eg., PS filtering and matched filtering, are assumed to be removed.

in a degraded optical signal-to-noise ratio (SNR) after adding the booster amplifier noise.

PA Model: The power amplifier (PA) used for amplifying the DAC outputs behaves as a nonlinear memory system, i.e.,
the PA output at any time instant depends on the current instantaneous input as well as the inputs at previous time instances. Denoting the memory depth by L, the PA denoted by fPA : R
L+1 → R, can be defined by

$$V(t)=f_{\mathrm{PA}}(Z(t),\ldots,Z(t-L)),$$
$$(10)$$
* [16] M. C.  

where fPA is a nonlinear function and Z(t) is the DAC output of the real/imaginary branch. For an ideal PA without memory effect, its transfer function becomes V (t) = GZ(t), where G
is the PA gain.

DAC Model: DACs used for high-bandwidth optical communications typically have low resolution. Currently, devices on the market provide 8 nominal bits. However, due to the sampling and jitter effects, the noise introduced by quantization is usually enhanced. One parameter to assess the amount of noise introduced by the DAC is the ENOB, which is defined as [46]

$$\mathrm{ENOB}={\frac{\mathrm{SNDR(dB)}-1.76}{6.02}},\qquad\qquad(11)$$

where the signal-to-noise-plus-distortion ratio (SNDR) is a measurable quantity, and is typically around 35 dB. Typically, high-speed DACs with 8-bit nominal resolution can be translated into ENOB ≤ 6 for operation within the device bandwidth. However, it should be noted that ENOB is a varying quantity and it changes over frequency. In this paper, for the sake of simplicity, the ENOB is assumed to be constant over the considered bandwidth and is set to 6.4 We model the ENOB noise introduced by the DAC as AWGN with variance determined by the ENOB of the device [47]

$\mathfrak{u}\mathfrak{i}\mathfrak{o}$ (SNDR), is
$$\sigma_{q}^{2}=\frac{1}{12}\left(\frac{E_{\rm peak}}{2^{\rm ENOB-1}-1}\right)^{2},\tag{12}$$  where $E_{\rm peak}=\max(\max(|\Re\{\mathbf{y}\}|),\max(|\Im\{\mathbf{y}\}|))$ is the peak.  
$$12)$$
amplitude of the input signals. Note that the finite bitresolution of the DAC limits the strength of the *arcsin*-based pre-distortion that can be applied, because it increases the peak amplitude, thereby resulting in higher noise. Therefore, there exists an optimum DAC driving voltage which balances SNR degradation from MZM losses when driving in the linear 4This is a reasonable assumption for current generation transceivers.



regime of the modulator and SNR degradation from limited compensation of MZM nonlinearity when driving at high voltages.

## Iv. Proposed End-To-End Wdm System

In this section, we start by introducing the proposed AE
implementation for the WDM system. The symbol rate and modulation formats are assumed to be the same for all channels, and we consider using the same AE configurations for all channels.

## A. Autoencoder Design

In principle, the entire transmitter and receiver can be implemented as an AE and trained by end-to-end learning as proposed in [6]. However, this leads to:
(a) Difficulty in interpretation: In contrast to conventional communication systems, where the performance of each transmitter/receiver blocks can be measured separately, the AE implementation is a "black-box", and it is hard to interpret the learned solution and to quantify the origin of the performance improvement.

(b) High training complexity: The transmitter needs to perform several tasks, such as symbol mapping, PS, and pre-distortion jointly, and learning the transmitted waveform involves sequential input data, which significantly increases the NN size with the "one-hot" encoding being applied, therefore increasing the training complexity.

(c) Parameter initialization: It is difficult to know which parameter choice leads to good performance prior to training, and random parameters initialization can slow down or even completely stall the convergence process [48].

To address these issues, we design our AE following the architecture of conventional communication systems as shown in Fig. 3. The policy π(·|s) can be ignored for now. The transmitter NN is decomposed into a concatenation of three simpler (small) NNs, each corresponding to one functional block of a conventional communication system. By doing this, the parameters of these NNs can be initialized such that they initially perform close to their conventional counterparts.

Moreover, the "block-wise" transceiver NN design allows for an ablation study and therefore makes it possible to partially explain the learned solution. As a result, the proposed scheme
has *decreased training complexity* and *increased interpretability* as compared to a conventional AE.5 1) Transmitter: At the transmitter, the symbol mapper, the PS filter, and the DPD of the conventional communication system are replaced by three NNs. We denote these three NNs by fθ1
(·), fθ2
(·), and fθ3
(·), where θ1, θ2, and θ3 are the sets of trainable parameters. We define these three NNs in the following:

(i) NN1 fθ1
: M → C maps each message mk ∈ m to a constellation point according to xk = fθ1
(mk), where an average power constrain E{|xk| 2} = 1 is enforced.

(ii) NN2 fθ2
: C
2L1+1 → C generates each of the pulseshaped baseband signals according to sk = fθ2(u
(L1)
k),
where u
(L1)
k = [uk−L1*, . . . , u*k+L1]>. Here, NN2 only has a single layer applying a linear activation function and can be interpreted as a standard finite impulse response (FIR) filter. Therefore, the generation of the pulse-shaped signal can be described by sk = θ>
2 u
(L1)
k.

(iii) NN3 fθ3
: C → C generates each of the predistorted signals according to yk = fθ3(s0k
), where fθ3
(·) operates separately on the in-phase and quadrature branches, and −1 ≤ <{s0k}, ={s0k} ≤ 1 is obtained by normalizing sk according to s0k =
sk/ max{max{|<{s}|}, max|={s*}|}}*, where s is the pulse-shaped signal sequence.
2) Receiver: At the receiver, only the symbol demapper is replaced by an NN, denoted by NN4 fθ4
: C → M, which maps each of the downsampled signal yk to the estimate of the transmitted message as described in Section II-B1. We note that, in principle, the MF can also be implemented by an NN.

In a real system, however, the MF is usually implemented as part of the adaptive equalizer, and we therefore have left it out of this discussion.

## B. Learning With A Channel Model

Assuming that all transfer functions of the components in the considered system are known and differentiable, the system can be optimized via standard end-to-end AE-learning [6]
5We note that such an AE implementation can potentially lead to performance degradation compared to the conventional AE, which we do not study in this paper.

TABLE II: NN parameters

| NN1 fθ1       | NN2 fθ2      | NN3 fθ3   | NN4 fθ4   |       |        |        |       |        |        |       |        |         |    |
|---------------|--------------|-----------|-----------|-------|--------|--------|-------|--------|--------|-------|--------|---------|----|
| layer         | input        | hidden    | output    | input | hidden | output | input | hidden | output | input | hidden | output  |    |
| # of layers   | -            | 3         | -         | -     | 0      | -      | -     | 3      | -      | -     | 2      | -       |    |
| (i)           | # of neurons | M         | 50        | 2     | 201    | -      | 1     | -      | 50     | -     | 2      | 20      | M  |
| act. function | -            | ReLU      | Linear    | -     | -      | Linear | -     | ReLu   | -      | -     | ReLu   | Softmax |    |

Algorithm 1 Optimization of the pulse shaping filter

7

1: **repeat**
2: . Transmitter 3: Symbol mapping and upsampling: m → x → u 4: Pulse shaping: u → s 5: Apply Gaussian: s → s˜
6: Apply DPD: s˜ → y 7: Send y 8: . Receiver 9: Receive: yˆ
10: Matched filtering and downsampling: yˆ → uˆ → xˆ
11: Compute per example loss: `k 12: Send `k 13: . Transmitter 14: Receive `k 15: Update NN2 parameters according to (16)
16: **until** Stop criterion is satisfied by minimizing the Monte-Carlo approximation of the crossentropy loss, defined by

$${\cal L}_{{\cal B}_{t}}(\mathbf{\theta}_{1},\mathbf{\theta}_{2},\mathbf{\theta}_{3},\mathbf{\theta}_{4})=\frac{1}{|{\cal B}_{t}|}\sum_{k=1}^{|{\cal B}_{t}|}\log[f_{\mathbf{\theta}_{4}}(y_{k})]_{m_{k}}.\tag{13}$$

$(\mathfrak{g}-\mathfrak{g})=\mathfrak{g}$
Similar to (5), the dependence of LBt
(θ1, θ2, θ3, θ4) on θ1, θ2, θ3 is implicit through the distribution of the downsampled signal yk, which is a function of the channel input g(˜sk),
where g(·) denotes the joint transfer function of the DAC, PA,
and IQM, and s˜k is dependent on NNs 1–3 as can be seen in Fig. 3. For the optimization, in order to have a faster and more stable convergence, all NNs are first initialized to mimic their model-based counterparts via pre-training. Then, the sets of parameters θ1, θ2, θ3, θ4 are jointly optimized using the Adam optimizer [49].

## C. Learning Without A Channel Model

In practice, training of the proposed AE in an experiment is challenging due to the fact that the instantaneous gradients of the physical channel are unknown. To solve this problem, we follow the alternative optimization approach that we reviewed in Section II-B3. The training of the demapper does not require differentiation of the channel can therefore be performed via supervised learning. For the transmitter training, since the transmitter consists of three NNs, one can perform the transmitter training by alternating between the optimization of the symbol mapper, the PS filter, and the DPD. In this paper however, we only focus on training of the PS filter, for which memory effects need to be taken into account. For the optimization of the mapper (i.e., NN1) or the DPD (i.e., NN3),
we refer the reader to [12], [34] and our recent paper [50]. To that end, the parameters of the mapper, the DPD, and the demapper (i.e., NN4) are assumed to be pretrained and fixed during the PS filter training.

For the PS filter optimization, the training algorithm described in Section II-B3 cannot be used directly due to the memory introduced by the matched filtering. Therefore, we extend the training approach as follows. In each training iteration t, the transmitter generates a batch of |Bt| random uniformly distributed messages within one message vector m ∈ M|Bt|and maps them individually to the baseband symbols after which R-time upsampling is applied. Then, the baseband transmitted signals are generated by convolving the upsampled signals with a real-valued trainable filter according to s = u> ∗θ>
2
, where ∗ denotes the convolution operator. To allow for the gradient computation of the trainable PS filter, we consider a Gaussian policy. To that end, a small perturbation wk ∈ CN (0, σ2) is applied to each of the pulse-shaped signals before applying the DPD. Therefore, the DPD input s˜ = s+w is stochastic and can be described by the PDF

$$\pi_{\theta_{2}}(\tilde{s}_{k}|\mathbf{u}_{k}^{(L2)})=\frac{1}{\sqrt{2\pi\sigma^{2}}}e^{-\frac{|\tilde{s}_{k}-\mathbf{\theta}_{2}^{\top}\mathbf{u}_{k}^{(L1)}|^{2}}{2\sigma^{2}}}.$$
$$(14)$$

At the receiver, the channel observations yˆ = [ˆy1*, . . . ,* yˆ|Bt|R]
are filtered by a MF and then downsampled with rate R. Then, the resulting signals xˆ = [ˆx1*, . . . ,* xˆ|Bt|] are used to compute the per-example loss defined by

$\ell_{k}=\log[f_{\theta_{4}}(\hat{x}_{k})]_{m_{k}}$, $k=1,\ldots,|\hat{B}_{t}|$,
, k = 1*, . . . ,* |Bt|, (15)
where xˆk = ˆukR. The per-example losses are sent back to the transmitter to perform the PS filter training. Due to memory effects introduced by the convolution operation in the MF
and PS filter, `k is related to a subset of the entire sequence x and m. We denote the total number of samples related to `k by 2G + 1. The training objective is to optimize θ2 such that the expected cross-entropy loss L(θ2) = E{`k} is minimized. Following [12], [34], we compute ∇θ2L(θ2) using the following proposition.

Proposition 1: The gradient of LBt
(θ2) can be approximated by

$$\nabla_{\theta_{2}}\mathcal{L}_{\mathcal{B}_{t}}(\theta_{2})\tag{16}$$ $$\approx\frac{1}{\sigma^{2}}\sum_{g=-G}^{G}\sum_{k=1}^{|\mathcal{B}_{t}|}\frac{1}{|\mathcal{B}_{t}|}\ell_{k}(\hat{\mathbf{y}},m_{k})(\tilde{s}_{kR+g}-[\mathbf{f}_{\theta_{2}}(\mathbf{f}_{\theta_{1}}(\mathbf{m}))]_{kR+g})$$ $$\times\nabla_{\theta_{2}}[\mathbf{f}_{\theta_{2}}(\mathbf{f}_{\theta_{1}}(\mathbf{m}))]_{kR+g},$$

where we wrote fθi to highlight that the relation is applied to the entire sequence in order to generate the entire corresponding output.

Proof: See Appendix A.

## V. Numerical Results

In this section, we provide extensive numerical results to verify and illustrate the effectiveness of the proposed AE-based WDM system. The system performance is measured in terms of SER, and for all the results presented below, the MF used is the root-raised-cosine (RRC) filter.

## A. Setup And Parameters

1) Simulation setup: We set M = 64, and consider a single channel system as well as a WDM system with 3 channels.

For the 3-channel setup, the guard band between the adjacent channels is ηfb (i.e., the channel spacing between neighboring channels is (1+η)fb), where η ≥ 0 and fb is the symbol rate.

The oversampling rate is set to R = 2 except for part of Section V-B2, where we study the impact of the oversampling rate on the performance. Both the PS filter and the MF have 201 taps. The hardware impairments considered in this paper are restricted to the IQM nonlinearity and the limited ENOB
of the DAC, while the PA is assumed to be linear, as the PA
nonlinearity is negligible when compared to that of the MZM.

However, it should be noted that the proposed approach can be readily applied to a more general setup where the other transmitter components are not idealized (e.g., nonlinear PA
and bandwidth-limited DAC).

2) Transmitter and Receiver Networks: Following previous work, all NNs are implemented as multi-layer fully-connected NNs, where the ReLU function is chosen as the activation function for the hidden layers. The NN parameters used in this paper are summarized in Table II.

3) Training: NN initialization: All AEs are trained by minimizing the end-to-end cross-entropy loss, with the learning rate and batch size set to 0.0002 and 16000, respectively. For the 3-channel setup in particular, we consider using the same AE configuration for all 3 channels, and we therefore only minimize the cross-entropy loss of the center channel and then use the parameters of the center channel AE for the AEs of the side channels. All AEs are trained for 10000 training iterations.

In each training iteration, uniformly distributed training data are randomly generated, and a total number of 1.6 × 108 data samples are used for each AE optimization. For the performance evaluation, in order to avoid leakage of training data into the testing set, independent uniformly distributed data are randomly generated for testing.

4) Baseline: For the baseline, we use a geometrically shaped constellation that is obtained via training a standard AE [6] over an AWGN channel at SNR = 18 dB.

6 The PS
filter is chosen as the RRC filter with roll-off factor β, which is the same as the MF at the receiver. The DPD, which operates separately on the in-phase and quadrature components, is based on the *arcsin* operation combined with clipping that can be described as [51]





$$\tilde{s}_{k}=\begin{cases}\min(\frac{\pi}{2},V_{\text{clip}}\,\arcsin(s_{k}))&s_{k}\geq0\\ \max(-\frac{\pi}{2},V_{\text{clip}}\,\arcsin(s_{k}))&s_{k}<0,\end{cases}\tag{17}$$

where the arcsin linearizes the IQM response, while the clipping factor Vclip needs to be optimized to reduce the peakto-average power ratio.

## B. Results And Discussion

1) Single-Channel System: We start by investigating a single-channel scenario (e.g., there is no ICI in the system),
and we evaluate the performance of the proposed method with respect to the peak voltage Vp of the driving signals.

For notation convenience, the peak voltage of driving signals is normalized and the full swing of the MZM is used if Vp = 1. Due to the dependence of the MZM nonlinearity level on the driving voltage swing, a separate AE is trained for each considered Vp. Fig. 4 visualizes the SER of the proposed system when the receiver MF roll-off factor is set





to β = 10%. For a range of considered Vp, the proposed approach achieves significantly better performance than the considered baseline. However, by looking at the frequency response of the learned PS filter, as shown with the blue dashed curve in Fig. 5, we observe that compared to the RRC filter with 10% roll-off, the learned filter has a significant amount of OOB energy, which will introduce severe ICI between narrowly-spaced neighboring channels and make it unsuitable for high SE WDM systems. This result indicates that the system designed for the single-channel setup cannot always be directly applied to a multi-channel setup, and additional care should be taken when designing multi-channel systems.

2) WDM System With 3 channels: We now train the proposed AE in a 3-channel setup. Fig. 6 visualizes the filters learned with different guard band bandwidth. We start by looking at the impulse response of the learned filters, which appears to be very similar to the RRC filter. However, from the frequency responses we observe that the trainable filter learns to adjust its bandwidth according to the guard band between the neighboring channels. In particular, when the guard band is small (e.g., η = 0.04, Fig. 6 (e)) the filter learns to restrict the OOB energy and has a narrower frequency response than the RRC filter, indicating that the trainable filter learns to limit ICI. As we increase the guard band bandwidth, the bandwidth of the trainable filter increases as well. Similar to the singlechannel scenario, the filter learns to put a significant amount of energy in the unoccupied spectrum when the guard band is large (see Fig. 6 (h) for η = 0.2).

To train the multi-channel system it is necessary to use high oversampling rates to allow for placing the neighboring channels in the considered spectrum. We emphasize that, in this scenario, it is important to ensure that the PS filter cannot generate unrealistically high frequency components. This is illustrated in Fig. 7, which depicts the learned filters when the filter is trained with 5 channels and R = 4 times oversampling rate. Similar as before, the trainable filter learns to adjust its bandwidth according to the channel spacing. However, the filter also learns to put energy at high frequencies at the edges between the next two channels. Despite this interesting behavior, such a filter is not feasible in practice due to the fact that a practical system would not operate at such high sampling rate because of the hardware limitations as well as power constraints. This result reminds us again the importance of using realistic setups when applying DL techniques for designing communication systems. Instead of upsampling to the final oversampling rate before the PS, one should use R = 2 times oversampling rate for the PS and another upsampling step after the PS, which is the approach we followed for the other multi-channel simulations. An additional benefit of this method is that the number of filter taps is reduced for the same FIR filter length, which improves convergence.

We now evaluate the performance of the proposed system versus different guard band bandwidth, and we consider setting R = 2 and the receiver MF roll-off factor to β = 10%
and β = 1%. The achieved SER for the center channel is







shown in Fig. 8 for β = 10% and in Fig. 9 for β = 1%.

7 As a reference, the SER performance of the baseline scheme applying *arcsin* combined with clipping is also shown. We remark that the clipping factor Vclip and Vp are optimized for the baseline scheme, while Vp is set to 1 in the proposed scheme for simplicity. Potentially, the performance of the proposed scheme can be further improved by optimizing Vp—the optimal performance for the single-channel case is achieved at Vp = 0.9 (see Fig. 4). For roll-off factors of 10%
(Fig. 8) and 1% (Fig. 9), the proposed approach outperforms the baseline scheme over all considered guard bands. More importantly, compared to the baseline scheme, the guard band for the proposed scheme can be significantly reduced with limited impact on the SER performance —for the target SER
where the baseline performance starts to saturate, the guard band can be reduced by around 37% for 10% roll-off and around 50% for 1% roll-off. Such results indicate that the proposed approach can improve the SE of WDM systems by allowing to put the channels at a very narrow channel spacing.

However, it should be noted that the reduction in guard bands does not translate directly into the same gain in terms of SE,
as the explicit SE depends on the applied modulation formats, the channel spacing, and the resulting SER.

3) Learned Constellation: Fig. 10 visualizes the learned constellation when the AE is trained in the 3-channel setup with β = 10% and η = 0.05. The constellation optimized over the AWGN channel and used for the baseline is also shown as a reference. It is shown that the constellation optimized over the WDM setup has lower peak amplitude than the baseline, indicating the constellation optimized for the AWGN channel is suboptimal for a system that is impaired by hardware imperfections. One possible explanation for such observation is that the AE learns to limit the peak voltage Vp by restricting the maximum amplitude of the constellation, so as to limit the signal distortion caused by the nonlinear MZM.



4) Learned DPD: Fig. 11 visualizes the transfer function of the DPD (i.e., ANN3) learned for the 3-channel system with β = 10% and η = 0.05. The transfer functions of the conventional DPD employing *arcsin* and different clipping Vclip are also shown as references. It is shown that the baseline DPD with optimized clipping has a response similar to the learned DPD, suggesting that the considered DPD applying arcsin combined with optimized clipping is near optimal for the considered scenario.

5) Ablation study: In order to quantify the origin of the performance gains, we carry out an ablation study by first freezing all the pre-trained NNs and then individually unfreezing them in the order of NN4, NN3, NN2, and NN1. We start by unfreezing NN4. The resulting SER performance for β = 10% and β = 1% is shown in Fig. 8 and Fig. 9, respectively.

Compared to the baseline scheme, it can be seen that the proposed approach achieves slightly better performance. Such result is what one would have expected, as the demampper trained over the AWGN channel is likely to be suboptimal for a channel impaired by hardware imperfections. We then further



arcsin w/ optimized Vclip arcsin w/ Vclip= 1 arcsin w/ Vclip= 1.8 Learned DPD

unfreeze the parameters of NN3 (i.e., NN1–2 are frozen).

The resulting performance is very similar (slightly better) to the case where NN1–3 are frozen. This result is consistent with what is shown in Fig. 11. Finally, the parameters of NN2 are also made trainable (i.e., only NN1 is fixed). In this case, the SER of the proposed approach improves significantly.

Particularly, the largest gain achieved for β = 10% is η = 0.04 while is η = 0.01 for β = 1%, indicating that the guard band can be optimized to improve the system performance. Finally, when all NNs are made trainable, the performance of the proposed method further improves, which is consistent with what is shown in Section. V-B3.

## C. Model-Free Training Of The Pulse-Shaping Filter

In this section, we extend our results to the case where a differentiable channel model is unknown. Here, we only consider training of the PS filter with the generalized training algorithm discussed in Section IV-C. The reason for only learning the PS filter is that PS filter training contributes to most of the performance gain as it is shown in the ablation study. RL-based training of the mapper and the DPD can be found in [12], [34], and [50], respectively.

Fig. 12 shows the achieved SER of the different schemes over a 3-channel WDM system. It is observed that the learned PS filter using the RL-based algorithm achieves very similar performance to the one using standard end-to-end learning assuming perfect channel knowledge. However, it should be noted that the RL-based approach allows for training of NNs in an experimental channel, and it has the potential to exceed the performance of the conventional end-to-end learning-based approach, as the performance of the latter is highly dependent on the accuracy of the model used for training.

−1 −0.5 0 0.5 1 DPD Input

## Vi. Conclusion And Future Work

We proposed a novel end-to-end AE for WDM systems that are impaired with non-ideal hardware components. In contrast to most of the conventional AEs, which are usually implemented as a pair of NNs, our AE design follows the architecture of conventional communication systems, and our transmitter is implemented by a concatenation of simple NNs.

Simulation results show that the proposed AE-based system achieves significantly better performance than the considered baseline, and allows to increase the SE of WDM systems by reducing the channel spacing without severe SER performance degradation. By means of an ablation study, we quantify the origin of the performance improvement. It is shown that the performance gain can be ascribed to the optimized constellation mapper, PS filter, and demapper. In addition, in case the channel model is unknown, we have shown that the PS filter can be trained using RL, and our simulation results indicate that the extended RL-based training approach can achieve similar performance to the standard end-to-end learning assuming perfect channel knowledge.

For future work, there are several important aspects concerning the use of AEs which deserve further study:

- Channel models: We have considered an optical back-toback channel due to the fact that the hardware distortions alone significantly degrade the system. However, practical systems further suffer from performance loss caused by the nonlinear crosstalk between adjacent channels. The AE-based method may help to reduce the impact of the crosstalk and provide significant performance improvement.

- The current AE design assumes that the WDM channels operate at the same rate. Practical systems, however, allow for transmission at different rates. New AE design and training methods may be needed to allow for flexible transmission rates.

## Appendix

We work with complete sequences, so that the loss is given by:

$$\mathcal{L}(\mathbf{\theta}_{2})=\mathbb{E}_{\mathbf{m},\mathbf{s},\mathbf{s},\mathbf{y},\mathbf{\dot{y}},\mathbf{\dot{x}}}\{\ell_{k}\}\tag{18}$$ $$=\mathbb{E}_{\mathbf{m},\mathbf{\dot{s}}|\mathbf{m},\mathbf{\dot{y}}|\mathbf{\dot{s}}}\{\ell_{k}\}$$

where in the second step we remove all the deterministic relations. Hence

$$\mathcal{L}(\mathbf{\theta}_{2})=\sum_{\mathbf{m}}\iint p(\mathbf{m})p(\bar{\mathbf{s}}|\mathbf{m})p(\hat{\mathbf{y}}|\bar{\mathbf{s}})\ell_{k}(\hat{\mathbf{y}},m_{k})\mathrm{d}\bar{\mathbf{s}}\mathrm{d}\hat{\mathbf{y}}\tag{19}$$ $$=\sum_{\mathbf{m}}\iint p(\mathbf{m})\pi(\bar{\mathbf{s}}|\mathbf{f}_{\mathbf{\theta}_{2}}(\mathbf{f}_{\mathbf{\theta}_{1}}(\mathbf{m})))p(\hat{\mathbf{y}}|\bar{\mathbf{s}})\ell_{k}(\hat{\mathbf{y}},m_{k})\mathrm{d}\bar{\mathbf{s}}\mathrm{d}\hat{\mathbf{y}},$$

where we wrote fθi to expressly denote that the relation is applied to the entire sequence in order to generate entire the corresponding output. Exploiting the policy gradient theorem
[34] and using the fact that ∇x log(g(x)) = ∇xg(x)
g(x), it then follows that

∇θ2L(θ2) = X m Z Z p(m)∇θ2 π(s˜|fθ2(fθ1(m)))p(yˆ|s˜)`k(yˆ, mk)ds˜dyˆ = E{`k(yˆ, mk)∇θ2log π(s˜|fθ2(fθ1(m)))} = E{`k(yˆ, mk) R X |Bt| i=1 ∇θ2 log π(˜si|[fθ2 (fθ1 (m))]i)} ≈ E{`k(yˆ, mk) X G g=−G ∇θ2log π(˜skR+g|[fθ2(fθ1(m))]kR+g)} =1 σ 2 X G g=−G E{`k(yˆ, mk)(˜skR+g − [fθ2 (fθ1 (m))]kR+g) × ∇θ2 [fθ2 (fθ1 (m))]kR+g} ≈ 1 σ 2 X G g=−G X |Bt| 1 |Bt| `k(yˆ, mk)(˜skR+g − [fθ2 (fθ1 (m))]kR+g) k=1 × ∇θ2 [fθ2 (fθ1 (m))]kR+g,
which leads us to (16). The first approximation considers that
`k(yˆ, mk) is only affected by 2G + 1 surrounding samples, while the second approximation is used to compute the expectation by averaging over the batch. We ignored boundary effect at the start and end of the sequence.

## References

[1] J. Song *et al.*, "End-to-end autoencoder for superchannel transceivers with hardware impairment," in Proc. Optical Fiber Communications Conference and Exhibition, 2021.

[2] P. J. Winzer *et al.*, "Fiber-optic transmission and networking: the previous 20 and the next 20 years," *Optics express*, vol. 26, no. 18, pp. 24 190–24 239, 2018.

[3] M. Yamada *et al.*, "Gain-flattened tellurite-based EDFA with a flat amplification bandwidth of 76 nm," *Photonics Technology Letters*, vol. 10, no. 9, pp. 1244–1246, 1998.

[4] D. Rafique *et al.*, "Flex-grid optical networks: spectrum allocation and nonlinear dynamics of super-channels," *Optics Express*, vol. 21, no. 26, pp. 32 184–32 191, 2013.

[5] M. Mazur *et al.*, "Joint superchannel digital signal processing for ultimate bandwidth utilization," *arXiv preprint arXiv:1911.02326*, 2019.

[6] T. O'shea *et al.*, "An introduction to deep learning for the physical layer,"
Transactions on Cognitive Communications and Networking, vol. 3, no. 4, pp. 563–575, 2017.

[7] M. Kim *et al.*, "A novel PAPR reduction scheme for OFDM system based on deep learning," *Communications Letters*, vol. 22, no. 3, pp. 510–513, 2017.

[8] T. J. O'Shea *et al.*, "Physical layer deep learning of encodings for the MIMO fading channel," in *Proc. Annual Allerton Conference on* Communication, Control, and Computing, 2017, pp. 76–80.
[9] S. Dorner ¨ *et al.*, "Deep learning based communication over the air,"
Journal of Selected Topics in Signal Processing, vol. 12, no. 1, pp.

132–143, 2017.

[10] A. Felix *et al.*, "OFDM-autoencoder for end-to-end learning of communications systems," in *Proc. International Workshop on Signal Processing Advances in Wireless Communications*, 2018.

[11] H. Ye *et al.*, "Channel agnostic end-to-end learning based communication systems with conditional GAN," in *Globecom Workshops*, 2018.

[12] F. A. Aoudia *et al.*, "End-to-end learning of communications systems without a channel model," in Proc. Asilomar Conference on Signals, Systems, and Computers, 2018, pp. 298–303.

[13] M. Zhang *et al.*, "Neural network assisted active constellation extension for papr reduction of OFDM system," in *Proc. International Conference* on Wireless Communications and Signal Processing, 2019.

[14] K. Choi *et al.*, "Neural joint source-channel coding," in *Proc. International Conference on Machine Learning*, 2019, pp. 1182–1192. [15] M. Stark *et al.*, "Joint learning of geometric and probabilistic constellation shaping," in *Globecom Workshops*, 2019.

[16] S. Cammerer *et al.*, "Trainable communication systems: Concepts and prototype," *Transactions on Communications*, vol. 68, no. 9, pp. 5489–
5503, 2020.

[17] T. Van Luong *et al.*, "Deep learning-aided multicarrier systems," *Transactions on Wireless Communications*, vol. 20, no. 3, pp. 2109–2119, 2020.

[18] F. A. Aoudia *et al.*, "End-to-end learning for OFDM: From neural receivers to pilotless communication," *Transactions on Wireless Communications*, 2021.

[19] ——, "Waveform learning for next-generation wireless communication systems," *arXiv preprint arXiv:2109.00998*, 2021.

[20] B. Karanov *et al.*, "End-to-end deep learning of optical fiber communications," *Journal of Lightwave Technology*, vol. 36, no. 20, pp. 4843–4855, 2018.

[21] S. Li *et al.*, "Achievable information rates for nonlinear fiber communication via end-to-end autoencoder learning," in *Proc. European* Conference on Optical Communication, 2018.

[22] R. T. Jones *et al.*, "Geometric constellation shaping for fiber optic communication systems via end-to-end learning," *arXiv preprint* arXiv:1810.00774, 2018.

[23] ——, "End-to-end learning for GMI optimized geometric constellation shape," in *Proc. European Conference on Optical Communication*, 2019.

[24] B. Karanov *et al.*, "End-to-end optimized transmission over dispersive intensity-modulated channels using bidirectional recurrent neural networks," *Optics express*, vol. 27, no. 14, pp. 19 650–19 663, 2019.

[25] K. Gum¨ us¸¨ *et al.*, "End-to-end learning of geometrical shaping maximizing generalized mutual information," in *Proc. Optical Fiber Communications Conference and Exhibition*, 2020.

[26] T. Uhlemann *et al.*, "Deep-learning autoencoder for coherent and nonlinear optical communication," in *Proc. ITG-Symposium on Photonic* Networks, 2020.

[27] B. Karanov *et al.*, "End-to-end learning in optical fiber communications:
Experimental demonstration and future trends," in Proc. European Conference on Optical Communications, 2020.

[28] O. Jovanovic *et al.*, "End-to-end learning of a constellation shape robust to variations in SNR and laser linewidth," arXiv preprint arXiv:2106.00431, 2021.

[29] C. Jiang *et al.*, "Machine learning paradigms for next-generation wireless networks," *Wireless Communications*, vol. 24, no. 2, pp. 98–105, 2016.

[30] F. N. Khan *et al.*, "Machine learning methods for optical communication systems," in *Proc. Signal Processing in Photonic Communications*, 2017, pp. SpW2F–3.

[31] N. E. West *et al.*, "Deep architectures for modulation recognition," in Proc. International Symposium on Dynamic Spectrum Access Networks, 2017.

[32] D. Zibar *et al.*, "Machine learning techniques in optical communication,"
Journal of Lightwave Technology, vol. 34, no. 6, pp. 1442–1452, 2015.

[33] C. Hager ¨ *et al.*, "Nonlinear interference mitigation via deep neural networks," in *Proc. Optical Fiber Communications Conference and* Exposition, 2018.

[34] F. A. Aoudia *et al.*, "Model-free training of end-to-end communication systems," *Journal on Selected Areas in Communications*, vol. 37, no. 11, pp. 2503–2516, 2019.

[35] A. C. Wilson *et al.*, "The marginal value of adaptive gradient methods in machine learning," *arXiv preprint arXiv:1705.08292*, 2017.

[36] M. D. Zeiler, "Adadelta: an adaptive learning rate method," *arXiv* preprint arXiv:1212.5701, 2012.

[37] I. Goodfellow, Y. Bengio, and A. Courville, *Deep learning*. MIT press, 2016.

[38] P. a. Rodr´ıguez, "Beyond one-hot encoding: Lower dimensional target embedding," *Image and Vision Computing*, vol. 75, pp. 21–31, 2018.

[39] M. Li *et al.*, "End-to-end learning for optical fiber communication with data-driven channel model," in *Proc. Opto-Electronics and Communications Conference*, 2020.

[40] D. Wang *et al.*, "Data-driven optical fiber channel modeling: a deep learning approach," *Journal of Lightwave Technology*, vol. 38, no. 17, pp. 4730–4743, 2020.

[41] B. Karanov *et al.*, "Concept and experimental demonstration of optical im/dd end-to-end system optimization using a generative model," in Proc. Optical Fiber Communications Conference and Exhibition, 2020.

[42] V. Curri *et al.*, "Optimization of DSP-based Nyquist-WDM PM-16QAM
transmitter," in *Proc. European Conference and Exhibition on Optical* Communication. Optical Society of America, 2012.

[43] G. Khanna *et al.*, "A robust adaptive pre-distortion method for optical communication transmitters," *Photonics Technology Letters*, vol. 28, no. 7, pp. 752–755, 2015.

[44] P. W. Berenguer *et al.*, "Nonlinear digital pre-distortion of transmitter components," *Journal of lightwave technology*, vol. 34, no. 8, pp. 1739–
1745, 2015.

[45] A. Napoli *et al.*, "Digital pre-compensation techniques enabling highcapacity bandwidth variable transponders," *Optics Communications*, vol.

409, pp. 52–65, 2018.

[46] C. Laperle *et al.*, "Advances in high-speed DACs, ADCs, and DSP for optical coherent transceivers," *Journal of lightwave technology*, vol. 32, no. 4, pp. 629–643, 2014.

[47] A. Napoli *et al.*, "Digital compensation of bandwidth limitations for high-speed DACs and ADCs," *Journal of Lightwave Technology*, vol. 34, no. 13, pp. 3053–3064, 2016.

[48] D. Mishkin *et al.*, "All you need is a good init," arXiv preprint arXiv:1511.06422, 2015.

[49] D. P. Kingma *et al.*, "Adam: A method for stochastic optimization,"
arXiv preprint arXiv:1412.6980, 2014.

[50] J. Song *et al.*, "Over-the-fiber digital predistortion using reinforcement learning," *arXiv preprint arXiv:2106.04934*, 2021.

[51] Y. Tang *et al.*, "Coherent optical OFDM transmitter design employing predistortion," *Photonics Technology Letter*, vol. 20, no. 11, pp. 954– 956, 2008.