# A $5.2 \mathrm{~mW}$ IEEE 802.15.6 HBC Standard Compatible Transceiver With Power Efficient Delay-Locked-Loop Based BPSK Demodulator 

Hyunwoo Cho, Student Member, IEEE, Hyungwoo Lee, Student Member, IEEE, Joonsung Bae, Member, IEEE,<br>and Hoi-Jun Yoo, Fellow, IEEE


#### Abstract

A Low-power IEEE 802.15.6 human body communication (HBC) fully compatible transceiver is implemented in 130 nm CMOS process. In this work, the proposed HBC transceiver satisfying all the standard requirements has four key features for low power consumption which includes: 1) low-power analog active filters for TX spectral mask: $\mathbf{3 0 \%}$ power reduction; 2) delayed locked loop (DLL) based BPSK receiver with the S/H operation for turning off unnecessary blocks: $\mathbf{4 0} \%$ power reduction; 3) low-power mode (LP-mode) receiver with the received signal strength indicator (RSSI) output data: 50\% power reduction; and 4) reconfigurable LNA with RSSI output data: $60 \%$ power reduction. As a result, the proposed transceiver can fully satisfy the HBC standard requirements while consuming $5.2 \mathrm{~mW}$ from the $1.2 \mathrm{~V}$ supply.


Index Terms-Costas loop, delayed-locked loop (DLL), human body communication (HBC), IEEE 802.15.6, received signal strength indicator (RSSI), spectral mask, standard, wireless body area network (WBAN).

## I. INTRODUCTION

$\mathbf{R}$ ECENTLY, wireless body area network (WBAN) is getting more and more attention in the emerging applications which combines healthcare and consumer electronics around the human body. The major design challenge associated with the WBAN is to extend the lifetime of the WBAN devices under limited energy source. Human body communication (HBC) which uses the human body as a communication channel is considered as a power-efficient wireless communication solution of the WBAN because high conductivity of the human body in a low frequency band enables low power communication. Since the HBC was firstly presented in [1], the physical communication principle and a variety of power efficient HBC transceivers have been presented [2]-[14], and eventually in 2012 the WBAN is standardized as IEEE 802.15.6 [15]. However, fully satisfying all requirements of $\mathrm{HBC}$ standard (Fig. 1) while consuming low power for long battery life is very difficult because of 1) transmitter (TX) mask with low[^0]

spectrum floor, sharp slope and wide frequency bandwidth, 2) low sensitivity, and 3) received energy detection capability for PHY/MAC protocol.

The previous HBC transceiver was proposed in 2013 [9], but it was not optimized for low power consumption. In the TX, the power-consuming high-order digital filter which consists of high speed DAC with high speed clock generation ( $>840 \mathrm{MHz}$ ) to avoid aliasing effect was adopted to satisfy the mask requirements. In the RX, the power-hungry VCO-based BPSK demodulator with I (in phase) and Q (quadrature phase) dual data paths for coherent receiving was employed in RX, which requires significant power consumption. In addition, the energy detector was not implemented which is an essential block for PHY/MAC protocol.

In this paper, we propose a low power and fully IEEE 802 . 15.6 HBC compatible transceiver satisfying all the tight specifications by adopting 4 key techniques. First, in the TX, an analog active filter rather than the high speed DAC reduces the power consumption by $30 \%$ because bandwidth requirement of analog active filter is much lower than the DAC in [9]. Second, the delay-locked-loop (DLL) based BPSK demodulator mitigates $40 \%$ of power consumption by turning off synchronization circuits in Q-path data path with the help of sample and hold (S/H) circuit which retains the control voltage of the DLL. Third, the received signal strength indicator (RSSI), which measures the received signal power to obtain the energy detection capability for the energy-efficient PHY/MAC operation, enables the operation of the low-power mode (LP-mode) receiver composed of amplifiers used in RSSI and digital demodulator while turning off all blocks of the DLL-based BPSK receiver with $50 \%$ power reduction. At last, by utilizing the information of the input signal power, the noise and linearity performance of the LNA can be adaptively controlled with the $60 \%$ reduced bias current consumption.

The rest of this paper is organized as follows. In the Section II, the overall architecture of the proposed HBC transceiver will be introduced. In the Section III and IV, the detail design of the transmitter with the analog active filter and DLL-based BPSK receiver will be explained, respectively. In Section V, the low power schemes including LP-mode receiver and reconfigurable LNA will be presented with the RSSI design. After illustrating the measurement results in Section VI, the conclusion will be summarized in Section VII.

| Modulation | FSDT (Digital BPSK) |
| :---: | :---: |
| Frequency | $21 \mathrm{MHz}$ |
| Bandwidth | $5.25 \mathrm{MHz}$ |
| Data-rate | $161.4 \mathrm{kbps}-1.3125 \mathrm{Mbps}$ |
| Sensitivity | $-97.35 \mathrm{dBm} @ 161.4 \mathrm{kbps}$ |
| Clock <br> Accuracy | Under 100ppm |



Fig. 1. IEEE 802.15.6 HBC standard requirements.



Fig. 2. Overall architecture of the proposed HBC transceiver.

## II. Overall Architecture

Fig. 2 shows the overall transceiver architecture which is composed of a transmitter with a spectral mask filter, a direct conversion receiver with a BPSK synchronizer, a RSSI and a digital baseband (PHY and MAC). In the transmitter, the baseband data from the $\mathrm{PHY} / \mathrm{MAC}$ is modulated with $21 \mathrm{MHz}$ carrier frequency. The modulation is the frequency selective digital transmission (FSDT) which is the same with the rectangular wave modulated BPSK. The spectral mask filter suppresses the low frequency band and high frequency band of the modulated data, and the driver transmits the data through the human body. In the receiver, the direct conversion receiver with the BPSK synchronizer recovers the received data from the LNA. The differential input LNA is adopted to generate differential output without noise figure growth which is essential for the direct conversion receiver configuration. Since the TX is disconnected when the receiver is operated, it does not generate LNA input mismatch. I and Q data paths of the direct conversion receiver consists of active mixers, baseband amplifiers, baseband lowpass filters, and limiting amplifiers. The DLL-based BPSK synchronizer adjusts its local RX clock signal to the rising and falling edge of the input data. Especially compared with the VCO-based architecture [15], [16], the DLL-based architecture can promptly synchronize its clock with the input data without any stability problem. Moreover, the proposed synchronizer in $\mathrm{Q}$ data path including mixer, baseband amplifier, low pass filter
Previous Work



(a)



(b)

Fig. 3. Previous HBC transmitter architecture. (b) Proposed HBC transmitter architecture.

and limiting amplifier is disabled to significantly decrease its power consumption when the phase synchronization loop is stabilized. The RSSI is composed of a seven stage limiting amplifier with seven rectifiers and 8-bit single-slope ADC. The RSSI measures the received input power with a range of $-100 \mathrm{dBm}$ to $-10 \mathrm{dBm}$. Based on the output of the RSSI, the operation mode of the LNA is controlled to optimize its consuming power while satisfying the sensitivity requirements, resulting in $60 \%$ power



(a)



(c)



(b)



(d)

Fig. 4. Spectrum simulation results. (a) Original data (b) Active filter (c) Non-linear modeling (c) off chip filtering.


Fig. 5. The 3rd-order low pass filter and high pass filter architecture.

reduction. In addition, to further reduce the power consumption when the input power is larger than $-35 \mathrm{dBm}$, the direct conversion receiver circuits are turned off, and only the LP-mode receiver with the limiting amplifier and digital demodulator for BPSK is turned on to recover the data. In the LP-mode receiver, over $50 \%$ of power consumption can be reduced.

## III. TransmitTer Design

Fig. 3(a) shows the previous transmitter architecture [9] including the digital FSDT modulator, 8th-order digital band-pass filter, 8 bit DAC and driver. The DAC based mask filter is commonly utilized in many RF transceivers because the digital filter enables the convenient simulation environment, and it is insensitive to the PVT variation. However, the DAC is not suitable for the HBC mask filter because the end frequency of the mask is very high. Since the high frequency edge of the mask requirement is $400 \mathrm{MHz}$, the digital filter and DAC should be operate at least $800 \mathrm{MHz}$, and a high-Q analog low-pass filter is also re- quired to remove the harmonic frequency and alias terms, which leads to the significant power consumption.

Fig. 3(b) shows the proposed transmitter architecture [13] with the low-power consuming analog active filters. Compared with the high speed DAC and digital filter, the analog active filter consumes much lower power because the OTA bandwidth requirement in the analog filter is much lower than the DAC. Since the spectral mask is falling at the $23.625 \mathrm{MHz}$ and the end frequency is $400 \mathrm{MHz}$, the $3 \mathrm{~dB}$ frequency and gain bandwidth should be large than $23.625 \mathrm{MHz}$ and $400 \mathrm{MHz}$, respectively. In this work, we designed the OTA $3 \mathrm{~dB}$ bandwidth as $100 \mathrm{MHz}$ which is larger than the $23.625 \mathrm{MHz}$. Compared with the DAC which requires at least $800 \mathrm{MHz}$ sampling frequency, the analog filter requires only $100 \mathrm{MHz}$ bandwidth, and this bandwidth reduction leads to $30 \%$ power reduction in the transmitter design. Although the proposed analog active filters require off-chip digitally controlled tuning to compensate the frequency characteristics variation caused by the process variation, it takes small



Fig. 6. Principle of the proposed DLL-based BPSK receiver.



Fig. 7. The overall architecture of the proposed DLL-based BPSK receiver.


Fig. 8. Schematic of the reconfigurable LNA, and the noise figure and linearity graph.

cost because the tuning is required only at the first time and the process variation can be avoided by using post layout simulation and common centroid layout technique. The proposed transmitter is composed of the level shifter, analog active filters, driver and off-chip analog filters. The signal flow in each stage in the transmitter will be explained in Fig. 4. Since the data is modulated with the rectangular wave swinging from $0 \mathrm{~V}$ to $1.2 \mathrm{~V}$, there are excessive DC power and harmonics in high fre- quency. Second, the data after the level shifter which reduces the swing range in order to avoid the non-linear effect in the following analog circuits is attenuated by 6th-order low-pass filter and 9th-order high-pass filter (Fig. 4(b)). The excessive spectrum power in DC and high frequency band is suppressed under the mask, but the non-linear characteristics of the analog active filter and driver increases the sideband spectrum, which is called spectrum regrowth effect (Fig. 4(c)). The amount of



Fig. 9. Active mixer and its replica bias circuit.



Fig. 10. Delay circuit with the linear bias control circuit.

this increased low frequency spectrum power cannot be exactly predicted due to the PVT variation, so we adopt the simple R-C off-chip 2nd-order high-pass filter to additionally attenuate the low frequency power. After the off-chip 2nd-order high-pass filter, all the excessive spectrum power is removed, and finally, the output spectrum can satisfy the spectral mask requirement (Fig. 4(d)).

Fig. 5 shows the circuit of the 3rd-order active low-pass filter and high pass filter. The active filter adopts the multiple feedback architecture which can obtain the $-60 \mathrm{~dB}$ /decade slope with only one OTA. The OTA has folded cascade configuration with the frequency compensation technique [14].

## IV. RECEIVER DESIGN

## A. DLL-Based BPSK Receiver

Fig. 6 shows the analysis of the DLL-based BPSK receiver. In the BPSK receiver, the local clock synchronization path, which is called Costas loop, is essential. The receiver should have I path and $\mathrm{Q}$ path to calculate the phase difference between the input data and local clock by multiplying output of both paths. Since the multiplied output of I and Q path is proportional to $\sin 2 \theta$, the phase difference can be zero by composing the synchronization loop to make the $\sin 2 \theta$ zero. In the conventional works [16], [17], the Costas loop uses the VCO to calibrate the input signal and local clock, which is quite similar with the PLL. Such implementations, however, may have stability



Fig. 11. Measured delay time with respect to the delay control voltage.

concerns. In this work, we proposed a DLL-based Costas loop, which avoid the stability issues associated with 2nd (or higher order) phase-locked loops. Since the frequency of local clock is not changed with respect to the control voltage, the delay cell control voltage can be held with the help of sample and hold buffer while turning off the Q path blocks, reducing $40 \%$ of power consumption. The phase error due to the $\mathrm{S} / \mathrm{H}$ buffer offset ( $<2$ degrees) is negligible. In addition, the clock difference between the TX and RX can be calibrated in the packet domain. In the HBC standard packet, the pilot which is composed of



Fig. 12. Received signal strength indicator (RSSI) principle and architecture.



Fig. 13. Schematic of the rectifier and current adder.



Fig. 14. LP-mode receiver architecture.


Fig. 15. Signal recovery process and demodulator circuit.



Fig. 16. Reconfigurable LNA operation.


Fig. 17. TX spectrum measurement results.


Fig. 18. Eye diagram of the main and LP-mode receiver.

simple $0,1,0,1$ for clock calibration must be inserted if the payload length is longer than 64 bytes. Since the clock drift of the crystal oscillator is usually under $10 \mathrm{ppm}$ and it must be smaller than $100 \mathrm{ppm}$ in HBC standard, the clock offset can be periodically calibrated at the pilot time without BER degradation.

Fig. 7 shows the detailed block diagram of the proposed DLL-based BPSK receiver. I path and Q path are composed of mixer buffer, mixer, baseband filter, and limiting amplifier. The voltage to current converter and a capacitor make the 1st-order loop filter, and S/H buffer with a switch is employed for holding the control voltage while turning off the Q path blocks. The delayed $21 \mathrm{MHz}$ reference clock signal through the delay cell in Costas loop works as a local clock of the RX.



Fig. 19. TX output power measurement results.



(a)



(b)

Fig. 20. (a) FM-radio input power measurement results (b) Measurement results of the relationship between $100 \mathrm{MHz}$ FM blocker input power and receiver sensitivity.

## B. Circuit Design

Fig. 8 shows the schematic of the reconfigurable LNA [8]. The common gate LNA with the $\mathrm{g}_{\mathrm{m}}$-boosting cross coupled NMOS is adopted for low noise characteristics. The size of the input NMOS $M_{1}$ and $M_{2}$ are controlled by 6 bit control code to adaptively change the LNA performance for low-power consumption which will be explained in Section V, and the noise figure and the $1 \mathrm{~dB}$ compression point value in accordance with the control code is shown in Fig. 8.

Fig. 9 shows the schematic of the active mixer and replica bias circuit. The active mixer has a simple Gilbert mixer configuration, and resistor $R_{H}$ is added to reducing the switching noise and increasing the linearity of mixer. The resistor $M_{7} \sim M_{9}$ and $4 \mathrm{R}_{\mathrm{H}}$ are composing the replica bias circuit. It has a same configuration of the half circuit of the Gilbert mixer, but resistor value is four times larger and size of transistor is four times smaller than the original ones, reducing the current consumption of the replica bias circuit by $25 \%$.

Fig. 10 presents the delay cell and delay control bias circuit. The delay cell is composed of six stages inverter based unit delay cells whose bias current is supplied by the delay control bias circuit. In the bias circuit, the output current is linearly changed by the input control voltage $\mathrm{V}_{\mathrm{ctrl}}$. The two differential MOS pairs $\left(M_{1}-M_{4}\right)$ remove the 2nd-order harmonics to increase the linearity while consuming more power consumption. Fig. 11 shows the measurement results of the delay time of the delay cell in accordance with the control voltage $\mathrm{V}_{\mathrm{ctrl}}$ and bias current.

## V. RSSI AND LOW-POWER RECEIVER

## A. RSSI Design

In the PHY/MAC protocol for multi-nodes operation, the energy detection block is an essential. Fig. 12 shows the principle and architecture of the RSSI for energy detection [18]-[20]. The RSSI is composed of seven amplifiers, seven rectifiers, current adder with low-pass filter and ADC. Since the number of the amplifiers decides the dynamic range of the RSSI and we need $-10 \mathrm{dBm}$ to $-100 \mathrm{dBm}$ input dynamic range to sense the HBC input signal power, seven amplifiers with the voltage gain of 15 $\mathrm{dB}$ and seven rectifiers are adopted. Each amplifier and rectifier



Fig. 21. RSSI measurement results.

covers the different input power range, and we can achieve wide dynamic range by adding all rectifiers' results.

Fig. 13 shows the schematic of the rectifier and current adder. The output current of each of the rectifier with the size ratio of $\mathrm{k}$ can be expressed as

$$
\begin{array}{r}
I_{o u t}=-2(K-1) K \beta V^{2}-4 K \beta|V| \sqrt{(K+1) \frac{I_{b}}{\beta}-K V^{2}} \\
+\frac{2 K I_{b}}{K+1}
\end{array}
$$

Since the output current is proportional to the input voltage, we can know that the rectifier converts the voltage value to the power value. The output current of each rectifiers are added by simple current mirror, and R-C load is adopted to sense the DC value while attenuating the voltage ripple with the frequency of the input carrier signal.

## B. LP-Mode Receiver

The FM-radio band from $80 \mathrm{MHz}$ to $110 \mathrm{MHz}$ becomes the strong interference to the HBC transceiver due to the body antenna effect. The direct conversion BPSK receiver consumes large amount of power to achieve good selectivity, but RSSI and the proposed LP-mode receiver can relax the selectivity overhead. Fig. 14 shows the concept and the architecture of the



|  | Process | SMIC $0.13 \mu \mathrm{m}$ |
| :---: | :---: | :---: |
|  | Frequency Band | $18.375 \mathrm{MHz}-23.625 \mathrm{MHz}$ |
|  | Modulation | $\overline{\text { FSDT }}$ |
|  | Data-rate | $164 \mathrm{kbps}-1.313 \mathrm{Mbps}$ |
|  | Sensitivity | -98.3dBm @ 1.313Mbps |
|  | LNA Gain | $18.2 \mathrm{~dB}$ |
|  | Post LNA Gain | $0-35.4 \mathrm{~dB}$ |
|  | Input Impedance | $100 \Omega$ |
|  | eceiver Noise Figure | $8.1 \mathrm{~dB}$ |
|  | Supply Voltage | $1.2 \mathrm{~V}$ |
| Power Consumption |  |  |
|  | Transmitter | $1.3 \mathrm{~mW}-1.4 \mathrm{~mW}$ |
| $\mathrm{RX}$ | Direct Conversion <br> @ Sample Time | $7.4 \mathrm{~mW}-8.4 \mathrm{~mW}$ |
|  | Direct Conversion <br> @ Hold Time | $5 m W-6 m W$ |
|  | Amp-Type <br> $\left(@ P_{\text {in }}>-30 \mathrm{dBm}\right)$ | $2 \mathrm{~mW}$ |
|  | Energy / bit | $4.8 \mathrm{~nJ} / \mathrm{b}$ |

Fig. 22. Chip photograph and performance summary.

LP-mode receiver. When the input power we can know from the RSSI is over $-35 \mathrm{dBm}$ which is $10 \mathrm{~dB}$ larger than maximum FM-radio input power, the LP-mode receiver which reuses the amplifiers in RSSI and digital demodulator can replace the direct conversion receiver. Since the power consumption of the direct conversion receiver becomes zero and the power consumption of the reused amplifiers are very low because of low required bandwidth $(21 \mathrm{MHz})$, the LP-mode receiver can reduce the $60 \%$ of power consumption.

Fig. 15 shows the signal recovery flow and demodulator circuit. Data from the human body is recovered to the digital data by amplifier chain. In the demodulator, the input data is firstly sampled by $42 \mathrm{MHz}$ clock. A Logic with several gates which is shown in Fig. 16 helps to find the data non-inverting time to demodulate the BPSK data. The phase ambiguity can be solved in the PHY processor by comparing the input data with the promising data sequence of preamble stage in data packet.

## C. Reconfigurable LNA With RSSI

Fig. 16 shows the operation of the reconfigurable LNA. If the voltage gain of the LNA is fixed, LNA should have both good sensitivity and good linearity to cover the both weak input and strong input, resulting in large power consumption in LNA. On the other hand, since we can know the input signal power by using the RSSI, the LNA can adaptively control the sensitivity and linearity performance with much lower power consumption. For instance, if the input signal is strong, the LNA is controlled to locate in (1) with the good linearity, and if the input signal is weak, the LNA is adjusted to locate in (3) with the good noise performance, which leads to reducing the power consumption by $60 \%$.

## VI. MEASUREment Results

Fig. 17 shows the TX spectrum measurement results. The spectrum with various data rate is measured and white line shows the required mask. All the measurement results satisfy the mask requirements. The spectrum of low frequency band and high frequency band cannot be shown in one screen due to the noise floor of the spectrum analyzer.

Fig. 18 shows the measured eye diagram of the direct conversion receiver and LP-mode receiver. The eye diagram of the direct conversion receiver is measured with the $-70 \mathrm{dBm}$ input power at $1.3125 \mathrm{Mbps}$ data rate. The eye diagram, of the LP-mode receiver is measured with $-30 \mathrm{dBm}$ input power at 1.3125 Mbps.

Fig. 19 shows the measurement results of the transmitter output power. The output power is controlled by changing the MOS size of the transmitter driver. The maximum output power is around $-10 \mathrm{dBm}$, and measured EVM of the BPSK modulated data from the TX driver is $6.4 \%$. The error is mainly caused by analog filters.

Fig. 20(a) shows the blocker measurement results. Since the human body height is similar to the half of the FM-radio wavelength, the FM-radio signal can be easily coupled to the human body. The maximum input power of the FM-radio interference, or FM-blocker, is $-38 \mathrm{dBm}$. Fig. 20(b) shows the relationship between input FM-blocker power and receiver sensitivity. If the FM-blocker power is larger than $-35 \mathrm{dBm}$, the BER becomes larger than $10 \%$. The sensitivity becomes lower when the input FM-blocker becomes lower.

Fig. 21 shows the RSSI measurement results. The $\mathrm{X}$ axis is the input signal power, left $\mathrm{Y}$ axis is output RSSI output voltage and right $\mathrm{Y}$ axis is the error between input signal power and calculated input power from the RSSI output voltage. The measured input dynamic range is from $-10 \mathrm{dBm}$ to $-100 \mathrm{dBm}$ and the measured error is under $2 \mathrm{dBm}$ in $-20 \mathrm{dBm}$ to $-80 \mathrm{dBm}$ input range.

Fig. 22 shows the chip photograph and performance summary table. The proposed HBC transceiver is implemented in SMIC $130 \mathrm{~nm}$ process and it satisfies all the standard requirements including sensitivity, data-rate, modulation, spectral mask and

TABLE I

PERFORMANCE COMPARISON TABLE

|  | JSSC 2009 <br> $[5]$ | JSSC 2012 <br> $[8]$ | ISSCC 2013 <br> $[12]$ | This Work |
| :---: | :---: | :---: | :---: | :---: |
| Frequency Band | $30-120 \mathrm{MHz}$ | $40-120 \mathrm{MHz}$ | $18.375-23.625 \mathrm{MHz}$ | $18.375-23.625 \mathrm{MHz}$ |
| Modulation | AFH <br> FSK | Double <br> FSK | FSDT (BPSK) | FSDT (BPSK) |
| Data-rate | $60 \mathrm{kbps}-10 \mathrm{Mbps}$ | $1 \mathrm{kbps}-10 \mathrm{Mbps}$ | $164 \mathrm{kbps}-1.3125 \mathrm{Mbps}$ | $164 \mathrm{kbps}-1.3125 \mathrm{Mbps}$ |
| Sensitivity | $-65 \mathrm{dBm}$ | $-66 \mathrm{dBm}$ | $-97.4 \mathrm{dBm}$ | $-98.3 \mathrm{dBm}$ |
| TX Power | $0.9 \mathrm{~mW}$ | $2 \mathrm{~mW}-3.8 \mathrm{~mW}$ | $2 \mathrm{~mW}$ | $1.4 \mathrm{~mW}$ |
| RX Power | $3.7 \mathrm{~mW}$ | $2.4 \mathrm{~mW}-3.2 \mathrm{~mW}$ | $3.2 \mathrm{~mW}$ <br> (not including //Q, Sync. Block) | $5 \mathrm{~mW}$ |
| Standard <br> Compatibility | $\mathrm{X}$ | $\mathrm{X}$ | $\triangle$ | $\mathrm{O}$ |

energy detection capability. The transmitter power consumption is $1.3 \mathrm{~mW}$ and the power consumption of the direct conversion receiver at sample time and at hold time is $6.2 \mathrm{~mW}$ and $3.8 \mathrm{~mW}$, respectively. The RSSI successfully measure the input signal power with the $-100 \mathrm{dBm}$ to $-10 \mathrm{dBm}$ input dynamic range. The LP-mode receiver and reconfigurable-LNA utilize the RSSI output to reduce the power consumption, resulting in $50 \%$ and $60 \%$ power reduction, respectively.

Table I shows the comparison table with previous HBC transceivers, The proposed transceiver in this work fully satisfies the HBC standard and lower power consumption, simultaneously, compared with the previous works.

## VII. CONCLUSION

In this paper, the IEEE 802.15.6 fully compatible HBC transceiver is proposed with four low-power features. First, compared with the high speed DAC architecture, analog active filter based TX mask filter is adopted with $30 \%$ power reduction. Second, the DLL-based BPSK receiver saves the $40 \%$ power consumption by turning off the $\mathrm{Q}$ data path with the $\mathrm{S} / \mathrm{H}$ operation. Third, the LP-mode receiver with the measured input power by RSSI reduces the $50 \%$ power consumption. At last, the reconfigurable LNA with the RSSI output information is adopted with $60 \%$ power reduction. As a result, the proposed standard compatible receiver implemented in $130 \mathrm{~nm}$ CMOS technology consumes as low as $5.2 \mathrm{~mW}$ power while satisfying all the standard requirements.

## REFERENCES

[1] T. Zimmerman, "Personal area network: Near-field intra-body communication," IBM Syst. J., vol. 35, no. 3-4, pp. 609-617, 1996.

[2] N. Cho et al., "The human body characteristics as a signal transmission medium for intra-body communication," IEEE Trans. Microw. Theory Techn., vol. 55, no. 5, pp. 1080-1086, May 2007.

[3] J. Bae et al., "The signal transmission mechanism on the surface of human body for body channel communication," IEEE Trans. Microw. Theory Techn., vol. 60, no. 3, pp. 582-593, Mar. 2012.

[4] S. Song et al., "A $0.9 \mathrm{~V} 2.6 \mathrm{~mW}$ Body-coupled scalable PHY transceiver for body sensor applications," in IEEE ISSCC Dig. Tech. Papers, 2007, pp. 366-367.
[5] N. Cho et al., "A $60 \mathrm{~kb} / \mathrm{s}$-to- $10 \mathrm{Mb} / \mathrm{s} 0.37 \mathrm{~nJ} / \mathrm{b}$ adaptive-frequency-hopping transceiver for interference resilient body channel communication," IEEE J. Solid-State Circuits, vol. 44, no. 3, pp. 708-717, Mar. 2009.

[6] N. Cho et al., "A $10.8 \mathrm{~mW}$ body channel communication/MICS dualband transceiver for a unified body sensor network controller," IEEE J. Solid-State Circuits, vol. 44, no. 12, pp. 3459-3468, Dec. 2009.

[7] A. Fazzi et al., "A $2.75 \mathrm{~mW}$ wideband correlation-based transceiver for body-coupled communication," in IEEE ISSCC Dig. Tech. Papers, 2009, pp. 204-205.

[8] J. Bae et al., "A 0.24-nJ/b wireless body-area-network transceiver with scalable double-FSK modulation," IEEE J. Solid-State Circuits, vol. 47, no. 1, pp. 310-322, Jan. 2012.

[9] H. Lee et al., "A $5.5 \mathrm{~mW}$ IEEE 802.15.6 wireless body area network standard transceiver for multi-channel electro-acupuncture application," in IEEE ISSCC Dig. Tech. Papers, 2013, pp. 452-453.

[10] J. Lee et al., "A $60 \mathrm{Mb} / \mathrm{s}$ wideband BCC transceiver with $150 \mathrm{pJ} / \mathrm{b} \mathrm{RX}$ and $31 \mathrm{pJ} / \mathrm{b}$ TX for emerging wearable applications," in IEEE ISSCC Dig. Tech. Papers, 2014, pp. 498-499.

[11] J. Bae et al., "A low energy crystal-less double-FSK transceiver for wireless body-area-network," in IEEE A-SSCC Dig. Tech. Papers, 2011, pp. 181-184.

[12] H. Lee et al., "A $33 \mu \mathrm{W} /$ node duty cycle controlled HBC transceiver system for medical BAN with 64 sensor nodes," in Proc. IEEE Custom Integrated Circuits Conf., 2014, pp. 1-8.

[13] H. Cho et al., "A 5.2 mW IEEE 802.15.6 HBC standard compatible transceiver with power efficient delay-locked-loop based BPSK demodulator," in IEEE A-SSCC Dig. Tech. Papers, 2014, pp. 297-300

[14] H. Cho et al., "A $79 \mathrm{pJ} / \mathrm{b} 80 \mathrm{Mb} / \mathrm{s}$ full-duplex transceiver and a 42.5 $\mu \mathrm{W} 100 \mathrm{~kb} / \mathrm{s}$ super-regenerative transceiver for body channel communications," in IEEE ISSCC Dig. Tech. Papers, 2015, pp. 380-381.

[15] IEEE Standard for Local and Metropolitan Area Networks: Part 15.6 Wireless Body Area Networks, IEEE Computer Society, IEEE Standards Association, Feb. 29, 2012.

[16] D. Kim et al., "A 622-Mb/s mixed-mode BPSK demodulator using a half-rate bang-bang phase detector," IEEE J. Solid-State Circuits, vol. 43, no. 10, pp. 2284-2292, Oct. 2008.

[17] S. Huang et al., "W-band BPSK and QPSK transceiver with Costasloop carrier recovery in 65 -nm CMOS technology," IEEE J. Solid-State Circuits, vol. 46, no. 12, pp. 3033-3046, Dec. 2011.

[18] M. Kitsunezuka et al., "A 30-MHz 2.4-GHz CMOS receiver with integrated RF filter and dynamic-range-scalable energy detector for cognitive radio systems," IEEE J. Solid-State Circuits, vol. 4, no. 5, pp. 1084-1093, May 2012.

[19] P. Huang et al., "A 2-V 10.7-MHz CMOS limiting amplifier/RSSI," IEEE J. Solid-State Circuits, vol. 35, no. 10, pp. 1474-1480, Oct. 2000.

[20] C. Wu et al., "A 110-MHz 84-dB CMOS programmable gain amplifier with integrated RSSI function," IEEE J. Solid-State Circuits, vol. 40, no. 6, pp. 1249-1258, Jun. 2005.



Hyunwoo Cho (S'10) received the B.S. degree from the Department of Physics, Korea Advanced Institute of Science and Technology (KAIST), Daejeon, Korea, in 2010, and the M.S. degree from the Department of Electrical Engineering, KAIST, in 2012, where he is currently working toward the Ph.D. degree.

He has worked on developing power and energyefficient CMOS wireless transceivers for portable and wearable devices working around the human body. His current research interest is low-power and low-energy body-area-network transceiver design and body-channel characteristics analysis.



Hyungwoo Lee (M'15) received the B.S., M.S., and Ph.D. degrees in electrical engineering from the Korea Advanced Institute of Science and Technology (KAIST), Daejeon, Korea, in 2010, 2012, and 2015, respectively. His Ph.D. research concerned wireless body area network circuits and systems and is focused on the network optimization among multiple sensor nodes using the human body communication PHY\&MAC.

Since 2015, he has been with Samsung Advanced Institute of Technology (SAIT), Samsung Electronics. He is currently a research staff member and his research interest is in low-energy system design for mobile healthcare applications.



Joonsung Bae ( $\mathrm{S}^{\prime} 07$ ) graduated from the Electrical Engineering Department of Korea Advanced Institute of Science and Technology (KAIST), Daejeon, Korea, in 2007 and received the M.S. and Ph.D. degrees in electrical engineering from KAIST in 2009 and 2013, respectively. His Ph.D. work concerned the Wireless Body Area Network (WBAN) circuits and systems.

In 2012, he was a visiting scholar of IMEC, Belgium, and researched noise analysis of the dry electrode for body channel communication. Since 2013, he has been with the Memory Business of Samsung Electronics, Korea, where he developed the SoC Design for the SSD (Solid-State Drive) and UFS (Universal Flash Storage). As a senior engineer, he designed the integrated circuits for PCI-Express 3.0 and M-PHY 3.0. In 2014, he joined the Information and Electronics Research Institute in KAIST as a postdoctoral researcher. Now he is an analog circuit designer in IMEC, Belgium, where he investigates ultra-lowpower biomedical circuits. His current research interests are high-speed serial interface PHY, short-range wireless connections, WBAN circuits and systems, and biomedical circuits and systems.

Dr. Bae received the Asian Solid-State Circuits Conference (A-SSCC) Best Design Awards in 2011 and the Global Internship Scholarship of National Research Foundation of Korea in 2012.



Hoi-Jun Yoo (M'95-SM'04-F'08) graduated from the Electronic Department of Seoul National University, Seoul, Korea, in 1983 and received the M.S. and Ph.D. degrees in electrical engineering from the Korea Advanced Institute of Science and Technology (KAIST), Daejeon, Korea, in 1985 and 1988 , respectively.

Since 1998, he has been on the faculty of the Department of Electrical Engineering at KAIST and now is a full Professor. From 2001 to 2005, he was the Director of Korean System Integration and IP Authoring Research Center (SIPAC). From 2003 to 2005, he was the full time Advisor to Minister of Korea Ministry of Information and Communication and National Project Manager for SoC and Computer. In 2007, he founded System Design Innovation \& Application Research Center (SDIA) at KAIST. Since 2010, he has served on the general chair of Korean Institute of Next Generation Computing. His current interests are computer vision SoC, body area networks, biomedical devices and circuits. He is a co-author of DRAM Design (Korea: Hongleung, 1996), High Performance DRAM (Korea: Sigma, 1999), Networks on Chips (Morgan Kaufmann, 2006), Low-Power NoC for High-Performance SoC Design (CRC Press, 2008), Circuits at the Nanoscale (CRC Press, 2009), Embedded Memories for Nano-Scale VLSIs (Springer, 2009), Mobile 3D Graphics SoC from Algorithm to Chip (Wiley, 2010), and Bio-Medical CMOS ICs (Springer, 2011).

Dr. Yoo received the Electronic Industrial Association of Korea Award for his contribution to DRAM technology in 1994, Hynix Development Award in 1995, the Korea Semiconductor Industry Association Award in 2002, Best Research of KAIST Award in 2007, Scientist/Engineer of this month Award from Ministry of Education, Science and Technology of Korea in 2010, Best Scholarship Awards of KAIST in 2011, and Order of Service Merit from Ministry of Public Administration and Security of Korea in 2011 and has been co-recipients of ASP-DAC Design Award 2001, Outstanding Design Awards of 2005, 2006, 2007, 2010, 2011 A-SSCC, Student Design Contest Award of 2007, 2008, 2010, 2011 DAC/ISSCC. He has served as a member of the executive committee of ISSCC, Symposium on VLSI, and A-SSCC and the TPC chair of the A-SSCC 2008 and ISWC 2010, IEEE Fellow, IEEE Distinguished Lecturer ('10-'11), Far East Chair of ISSCC ('11-'12), Technology Direction Sub-Committee Chair of ISSCC ('13), TPC Vice Chair of ISSCC ('14), and TPC Chair of ISSCC ('15).


[^0]:    Manuscript received February 18, 2015; revised May 05, 2015, July 06, 2015, and August 16, 2015; accepted August 17, 2015. This paper was approved by Guest Editor Gregory Chen.

    The authors are with the Korea Advanced Institute of Science and Technology (KAIST), Daejeon 305-701, Korea (e-mail: hwcho@kaist.ac.kr).

    Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

    Digital Object Identifier 10.1109/JSSC.2015.2475179

