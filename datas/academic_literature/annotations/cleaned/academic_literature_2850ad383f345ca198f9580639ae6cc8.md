Two-Dimensional Lorentz Force Image Reconstruction for Magnetoacoustic Tomography with Magnetic Induction

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2010 Chinese Phys. Lett. 27084302

(http://iopscience.iop.org/0256-307X/27/8/084302)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 136.186.1.81

This content was downloaded on 18/05/2015 at 08:37

Please note that terms and conditions apply.

# Two-Dimensional Lorentz Force Image Reconstruction for Magnetoacoustic Tomography with Magnetic Induction * 

LI Yi-Ling(李宜令) $)^{1}$, LIU Zhen-Bo(刘振波) $)^{3}$, MA Qing-Yu(马青玉) ${ }^{2 * *}$, GUO Xia-Sheng(郭霞生) ${ }^{3}$,<br>ZHANG Dong(章东 $)^{3}$<br>${ }^{1}$ Department of Educational Technology, Nanjing Normal University, Nanjing 210097<br>${ }^{2}$ Key Laboratory of Optoelectronics of Jiangsu Province, School of Physics and Technology, Nanjing Normal University,<br>Nanjing 210046<br>${ }^{3}$ Institute of Acoustics, Key Laboratory of Modern Acoustics (Ministry of Education), Nanjing University,<br>Nanjing 210093

(Received 1 June 2010)


#### Abstract

Magnetoacoustic tomography with magnetic induction has shown potential applications in imaging the electrical impedance for biological tissues. We present a novel methodology for the inverse problem solution of the 2-D Lorentz force distribution reconstruction based on the acoustic straight line propagation theory. The magnetic induction and acoustic generation as well as acoustic detection are theoretically provided as explicit formulae and also validated by the numerical simulations for a multilayered cylindrical phantom model. The reconstructed 2-D Lorentz force distribution reveals not only the conductivity configuration in terms of shape and size but also the amplitude value of the Lorentz force in the examined layer. This study provides a basis for further study of conductivity distribution reconstruction of MAT-MI in medical imaging.


PACS: 43. 80. $E v, 72.55 .+s, 73.50 . R b$

Magnetoacoustic tomography with magnetic induction (MAT-MI) ${ }^{[1]}$ is a recently proposed modality for electrical impedance imaging of biological tissues, in which, under a static magnetic field and a pulsed time-varying magnetic field, the conductive target object emits acoustic signals because of the acoustic vibration of the Lorentz force ${ }^{[2,3]}$ and the collected acoustic signal comprising the conductivity information of the target can be used to reconstruct the conductivity distribution. ${ }^{[4,5]}$ Compared with the other electrical impedance imaging technologies, ${ }^{[6-9]}$ MATMI methodology shows the advantage of avoiding the "shielding effect" caused by the low-conductivity surface tissue layers of the human body by employing the magnetic excitation. Furthermore, high spatial resolution could be achieved in MAT-MI with high frequency magnetic excitation and acoustic detection.

MAT-MI has attracted much research interest in the past decades. Researchers have performed pilot studies in both theory and experiment. ${ }^{[1-5]}$ Li et $a l .{ }^{[10]}$ carried out a 3-D MAT-MI numerical simulation for the concentric and eccentric spherical conductivity models using the finite element method. Brinker and Roth ${ }^{[11]}$ proposed an improved method by considering the electrical anisotropy of the biological tissues. Although the reconstructed images display the configuration of the measured layer, the detailed information inside each medium is invisible. ${ }^{[2-5]}$ Therefore, it is a key issue to reconstruct the interior details from the detected acoustic signals in MAT-MI.

In this Letter, an improved methodology for the inverse problem solution of the 2-D Lorentz force distribution reconstruction is theoretically investigated. All the acoustic signals are assumed to be generated from point sources, while their propagation in a 3 D free space follows the classical straight line theory. The formulae of the acoustic generation are provided for a multilayered circular cylinder phantom model with the conductivity close to the biological tissues. In contrast to the previous studies ${ }^{[2-5]}$ on MAT-MI, the acoustic pressures are deconvolved from the detected waveforms, and the Lorentz force image reconstruction algorithm is then presented as the inverse problem solution to achieve the Lorentz force distribution inside the target.

Figure 1 illustrates the arrangement of the present MAT-MI system. A conductive object is placed in a static magnetic field $\boldsymbol{B}_{0}=B_{0} \hat{z}$. A time-varying pulsed magnetic field $\boldsymbol{B}_{1}=B_{1}(t) \hat{z}$ in the same region is produced by a stimulating coil and is assumed to be homogeneous. The interaction between the magnetically induced eddy current in the conductive object and the static magnetic field $\boldsymbol{B}_{0}$ causes acoustic vibration at $\boldsymbol{r}(x, y, z)$ due to the Lorentz force. The generated acoustic signals transmit through the object and are detected by the transducers placed around the object. The acoustic pressure generated by the induced Lorentz force in the object is governed by the[^0]equation $^{[12]}$

$$
\nabla^{2} p-\frac{1}{c^{2}} \frac{\partial^{2} p}{\partial t^{2}}=\nabla \cdot\left[\boldsymbol{J}(\boldsymbol{r}) \times \boldsymbol{B}_{0}\right]
$$

where $p$ is the acoustic pressure, the vibration source $\nabla \cdot\left[\boldsymbol{J}(\boldsymbol{r}) \times \boldsymbol{B}_{0}\right]$ is a given function at the source point $\boldsymbol{r}, \nabla^{2}$ is the Laplacian operator, $c$ is the acoustic velocity in the transmission medium, and $\boldsymbol{J}(\boldsymbol{r})$ is the induced eddy current. The alternative Lorentz force is described as $\boldsymbol{F}_{L}(\boldsymbol{r})=\boldsymbol{J}(\boldsymbol{r}) \times \boldsymbol{B}_{0}$ along the normal direction of the induced eddy current. As both the induced eddy current and the corresponding Lorentz force exist in the $x y$ plane, the acoustic vibration source is considered in a 2-D configuration for the measured layer.



Fig. 1. Illustration of the present MAT-MI system.

As shown in Fig. 1, the target is supposed to be a two-layer structure object with the uniform conductivities $\sigma_{2}$ and $\sigma_{1}$ of the inner and outer media, and it is put into an insulating medium of $\sigma_{0}=0 \mathrm{~s} / \mathrm{m}$ for acoustic coupling. Based on Faraday's principle, the induced electrical field $\boldsymbol{E}$ is determined by the pulsed magnetic field $\boldsymbol{B}_{1}$ as $\nabla \times \boldsymbol{E}=-\partial \boldsymbol{B}_{1}(t) / \partial t$, and the generated electrical field is in the $x y$ plane with its direction perpendicular to the pulsed magnetic field. The acoustic pressure $p(\boldsymbol{r})$ generated at $\boldsymbol{r}$ is proportional to the intensity of the vibration source as $p(\boldsymbol{r})=\nabla \cdot\left[\boldsymbol{F}_{L}(\boldsymbol{r})\right]=\nabla \cdot\left\{\left[\sigma(\boldsymbol{r}) E(\boldsymbol{r}) B_{0}\right] \hat{n}\right\}$, where $\hat{n}$ is the unit normal vector of the induced eddy current. According to Green's function ${ }^{[13]}$ of the acoustic diffraction transmission for each point source, the detected acoustic pressure transmitted from $\boldsymbol{r}$ to $\boldsymbol{r}^{\prime}$ can be described as

$$
p\left(\boldsymbol{r}^{\prime}, \boldsymbol{r}\right)=\frac{\frac{\partial}{\partial \hat{n}}\left[\boldsymbol{F}_{L}(\boldsymbol{r})\right]}{4 \pi\left|\boldsymbol{r}^{\prime}-\boldsymbol{r}\right|} \otimes \delta\left(t-\left|\boldsymbol{r}^{\prime}-\boldsymbol{r}\right| / c\right)
$$

where $\delta\left(t-\left|\boldsymbol{r}^{\prime}-\boldsymbol{r}\right| / c\right)$ is the time delay for the transmission distance $\left|\boldsymbol{r}^{\prime}-\boldsymbol{r}\right|$, and $\otimes$ is the convolution operator. For a focused transducer with an ideal infinitesimal aperture, only the acoustic signals with the transmission direction perpendicular to the transducer surface as $\hat{n}= \pm\left(\boldsymbol{r}^{\prime}-\boldsymbol{r}\right) /\left|\boldsymbol{r}^{\prime}-\boldsymbol{r}\right|$ can be collected, which is indicated by the straight line theory in classi$\mathrm{cal}$ acoustics. As the entire target object is considered, the time series acoustic pressure detected at $\boldsymbol{r}^{\prime}$ can be expressed as the integral of all the acoustic sources within the whole object volume,

$$
p\left(\boldsymbol{r}^{\prime}, t\right)=\iiint_{V} \frac{\frac{\partial}{\partial \hat{n}}\left[F_{L}(\boldsymbol{r}) \hat{n}\right]}{4 \pi\left|\boldsymbol{r}^{\prime}-\boldsymbol{r}\right|} d \boldsymbol{r} \otimes \delta\left(t-\left|\boldsymbol{r}^{\prime}-\boldsymbol{r}\right| / c\right)
$$

where $F_{L}(\boldsymbol{r})$ is the amplitude of the Lorentz force with the direction $\hat{n}$. By performing integral operation along the normal direction $\hat{n}$ for both sides of Eq. (3), we obtain

$$
\begin{aligned}
& \int p\left(\boldsymbol{r}^{\prime}, t\right) d \hat{n} \\
= & \int d \hat{n} \iiint_{V} \frac{\frac{\partial}{\partial \hat{n}}\left[F_{L}(\boldsymbol{r}) \hat{n}\right]}{4 \pi\left|\boldsymbol{r}^{\prime}-\boldsymbol{r}\right|} d \boldsymbol{r} \otimes \delta\left(t-\left|\boldsymbol{r}^{\prime}-\boldsymbol{r}\right| / c\right) .
\end{aligned}
$$

The normal direction of the induced eddy current is consistent with that of the Lorentz force $\boldsymbol{F}_{L}(\boldsymbol{r})$, which is a linear function over time $t$, so $d \hat{n}$ can be replaced by $d t$ in the calculation for $d \hat{n}=c d t$. Thus, Eq. (4) is rewritten as

$$
\int p\left(\boldsymbol{r}^{\prime}, t\right) c d t=\iiint_{V} \frac{F_{L}(\boldsymbol{r})}{4 \pi\left|\boldsymbol{r}^{\prime}-\boldsymbol{r}\right|} d \boldsymbol{r} \otimes \delta\left(t-\left|\boldsymbol{r}^{\prime}-\boldsymbol{r}\right| / c\right)
$$

Note that the collecting acoustic waveform by the transducer is a convolution between the detected acoustic pressure $p\left(\boldsymbol{r}^{\prime}, t\right)$ and the impulse response $h(t)$ of the transducer as

$$
w\left(\boldsymbol{r}^{\prime}, t\right)=p\left(\boldsymbol{r}^{\prime}, t\right) \otimes h(t)
$$

where $p\left(\boldsymbol{r}^{\prime}, t\right)$ and $w\left(\boldsymbol{r}^{\prime}, t\right)$ both are the timedependent functions. Equation (6) can be expressed with their product in the frequency domain as $W(\omega)=$ $P(\omega) H(\omega)$, where $W(\omega), P(\omega)$ and $H(\omega)$ are the Fourier spectra of $w\left(\boldsymbol{r}^{\prime}, t\right), p\left(\boldsymbol{r}^{\prime}, t\right)$ and $h(t)$, respectively. Based on the least mean square error estimation, $p\left(\boldsymbol{r}^{\prime}, t\right)$ can be restored with the Wiener filter for the deconvolution in the presence of noise,

$$
p\left(\boldsymbol{r}^{\prime}, t\right)=\mathrm{FFT}^{-1}\left(\frac{W(\omega) H^{*}(\omega)}{H(\omega) H^{*}(\omega)+C}\right)
$$

where $\mathrm{FFT}^{-1}$ denotes the inverse Fourier transform operation, the asterisks mean the complex conjugation and $C$ is approximated by a constant based on the spectral density ratio of signal to noise.

With the deconvolved $p\left(\boldsymbol{r}^{\prime}, t\right)$, the 2-D distribution of the Lorentz force $F_{L}(\boldsymbol{r})$ can be reconstructed by using the simplified tomographic algorithm, ${ }^{[13]}$

$$
F_{L}(\boldsymbol{r})=\frac{1}{2 \pi c} \int_{0}^{2 \pi} \frac{\hat{n}\left(\boldsymbol{r}-\boldsymbol{r}^{\prime}\right)}{\left|\boldsymbol{r}^{\prime}-\boldsymbol{r}\right|^{2}} \int p\left(\boldsymbol{r}^{\prime}, t\right) d t d \phi
$$

where $\phi$ is the angle of the transducer placed at $\boldsymbol{r}^{\prime}=R_{m} \exp (j \phi)$ with the rotation radius of $R_{m}$.

In the simulations, measurements are performed on a circled line with a radius of $100 \mathrm{~mm}$, and the spatial and temporal grids are chosen to be $0.1 \mathrm{~mm}$ and $6.67 \mathrm{~ns}$, respectively. The acoustic velocity is set to $1500 \mathrm{~m} / \mathrm{s}$ approximately equal to that in water or biological soft tissues. The frequency of the pulsed magnetic field and the central frequency of the transducer both are set to $0.5 \mathrm{MHz}$. Figure 2 presents the cross section of the simulated conductivity distribution of the cylindrical phantom model, where gray scales represent different conductivity values. The conductivities for the three types of tissues A, B and C are set to $0.3 \mathrm{~S} / \mathrm{m}, 0.6 \mathrm{~S} / \mathrm{m}$ and $0.9 \mathrm{~S} / \mathrm{m}$ with the corresponding radii of 80,30 and $20 \mathrm{~mm}$, respectively.



Fig. 2. Cross section of the conductivity distribution of the three-layer cylindrical phantom model, in units of $0.1 \mathrm{~mm}$.



Fig. 3. Transducer collected waveform at the angle of $62^{\circ}$.

The generated acoustic signals are stimulated at different angles by using Eq. (3). Figure 3 illustrates the waveform measured at the angle of $62^{\circ}$, where the six wave clusters are introduced by the impulse response of the transducer in the convolution process described by Eq. (6). The transmission distance in Fig. 3 represents the distance between $\boldsymbol{r}^{\prime}$ and $\boldsymbol{r}$, and it can be calculated by $\left|\boldsymbol{r}^{\prime}-\boldsymbol{r}\right|=c t$ with the time series waveforms. The wave amplitudes reflect the Lorentz force change between the adjacent tissues, which is determined by the conductivity difference and the geometry of the examined layer, and it is validated by the experimental results ${ }^{[2-5]}$ in the previous studies.

Through low-frequency signal elimination using a narrow band-pass filter with a central frequency of $0.5 \mathrm{MHz}$, the deconvolution algorithm is applied to all the 360 detected waveforms without noise consideration. Therefore, the acoustic pressures $p\left(\boldsymbol{r}^{\prime}, t\right)$ could be extracted from the measured waveforms $w\left(\boldsymbol{r}^{\prime}, t\right)$, while the corresponding result for the $62^{\circ}$ measurement (i.e. referred to Fig.3) is displayed in Fig. 4. The impact behaving of the acoustic pressure is generated at the conductivity boundary with corresponding amplitude and polarity, which is introduced by the divergence effect of the Lorentz force.



Fig. 4. Deconvolved 1-D acoustic pressure distribution.



Fig. 5. Reconstructed 2-D Lorentz force distribution image.

The reconstructed 2-D image is presented in Fig. 5, in which the normalized color scale represents the relative amplitude of the Lorentz force. The amplitude difference in different tissues can be obviously displayed with clear tissue configuration. Meanwhile, the amplitude difference in each tissue can also be seen, which is produced by the vector superposition of the
induced eddy currents. However, the eddy current at each acoustic source point is a 2-D vector in MATMI, which is perpendicular to the Lorentz force in the $x y$ plane. The detected acoustic waveforms can only provide the acoustic pressures without the directional information and the corresponding direction of each Lorentz force could not be achieved with the proposed image reconstruction technique. In addition, the obvious transition zones at the conductivity boundaries are produced by the tomographic imaging algorithm. As a result, only the relative amplitude of the Lorentz force distribution in the examined layer can be imaged.

In conclusion, a new theory for the inverse problem of MAT-MI has been proposed for the reconstruction of 2-D Lorentz force distribution of the measured layer. A deconvolution algorithm is applied to extract acoustic pressures from the waveforms measured with transducers placed around the target object. The acoustic straight line theory is adopted for the description of acoustic wave propagation. With the magnetic stimulation of a coil, numerical stimulations are conducted for a multilayered cylindrical phantom model with its electrical conductivity close to native tissues. The 1-D acoustic pressure deconvolution and the 2-D Lorentz force distribution reconstruction are performed as the inverse problem solution. The simulated results are in good agreements with the theoretical predictions. The proposed technique can provide the inner information of each medium inside the object and can be used to solve the problem of only reconstructing the conductivity boundary in MAT-MI, which is beneficial for further study on conductivity image reconstruction. The favorable results suggest the potential application of MAT-MI as a non-invasive electrical impedance imaging technology with improved spatial resolution and image contrast for medical imaging.

## References

[1] Xu Y and He B 2005 Phys. Med. Biol. 505175

[2] Li X, Xu Y and He B 2006 J. Appl. Phys. 99066112

[3] Li X, Xu Y and He B 2007 IEEE Trans. Biomed. Eng. 54 323

[4] Ma Q Y and He B 2008 IEEE Trans. Biomed. Eng. 55813

[5] Xia R M, Li X and He B 2007 Appl. Phys. Lett. 91083903

[6] Xiang L Z, Xing D, Gu H M, Zhou F F, Yang D Wu, Zeng L M and Yang S H 2007 Chin. Phys. Lett. 24751

[7] Su Y X, Wang R K, Zhang F and Yao J Q 2006 Chin. Phys. Lett. 23512

[8] Kwon O, Woo E, Yoon J and Seo J K 2002 IEEE Trans. Biomed. Eng. 49160

[9] Wen H, Shah J and Balaban S 1998 IEEE Trans. Biomed. Eng. 45119

[10] Li X, Li X, Zhu S N and He B 2009 Phys. Med. Biol. 54 2667

[11] Brinker K and Roth B J 2008 IEEE Trans. Biomed. Eng. $55 \quad 1637$

[12] Morse P M and Feshbach H 1953 Methods of Theoretical Physics (New York: McGraw-Hill)

[13] Xu Y and Wang L H 2004 Phys. Rev. Lett. 92033902


[^0]:    *Supported by the National Natural Science Foundation of China under Grant No 10974098, the Doctoral Fund of Ministry of Education of China (20093207120003), the Natural Science Foundation of Jiangsu Province (BK2009407), and the National Basic Research Program of China under Grant No 2010CB732600.

    **To whom correspondence should be addressed. Email: maqingyunjnu.edu.cn

    (c) 2010 Chinese Physical Society and IOP Publishing Ltd

