Home Search Collections Journals About Contact us My IOPscience





Two-Dimensional Lorentz Force Image Reconstruction for Magnetoacoustic Tomography with Magnetic Induction This content has been downloaded from IOPscience. Please scroll down to see the full text. 2010 Chinese Phys. Lett. 27 084302 (http://iopscience.iop.org/0256-307X/27/8/084302) View the table of contents for this issue, or go to the journal homepage for more Download details: IP Address: 136.186.1.81 This content was downloaded on 18/05/2015 at 08:37 Please note that terms and conditions apply.

# Two-Dimensional Lorentz Force Image Reconstruction For Magnetoacoustic Tomography With Magnetic Induction *

LI Yi-Ling(李宜令)
1, LIU Zhen-Bo(刘振波)
3, MA Qing-Yu(马青玉)
2**, GUO Xia-Sheng(郭霞生)
3, ZHANG Dong(章东)
3 1*Department of Educational Technology, Nanjing Normal University, Nanjing 210097* 2*Key Laboratory of Optoelectronics of Jiangsu Province, School of Physics and Technology, Nanjing Normal University,*
Nanjing 210046 3*Institute of Acoustics, Key Laboratory of Modern Acoustics (Ministry of Education), Nanjing University,*
Nanjing 210093

## (Received 1 June 2010)

Magnetoacoustic tomography with magnetic induction has shown potential applications in imaging the electrical impedance for biological tissues. We present a novel methodology for the inverse problem solution of the 2-D
Lorentz force distribution reconstruction based on the acoustic straight line propagation theory. The magnetic induction and acoustic generation as well as acoustic detection are theoretically provided as explicit formulae and also validated by the numerical simulations for a multilayered cylindrical phantom model. The reconstructed 2-D Lorentz force distribution reveals not only the conductivity configuration in terms of shape and size but also the amplitude value of the Lorentz force in the examined layer. This study provides a basis for further study of conductivity distribution reconstruction of MAT-MI in medical imaging.

PACS: 43. 80. Ev, 72. 55. +s, 73. 50. Rb DOI: 10.1088/0256-307X/27/8/084302 Magnetoacoustic tomography with magnetic induction (MAT-MI)[1]is a recently proposed modality for electrical impedance imaging of biological tissues, in which, under a static magnetic field and a pulsed time-varying magnetic field, the conductive target object emits acoustic signals because of the acoustic vibration of the Lorentz force[2,3] and the collected acoustic signal comprising the conductivity information of the target can be used to reconstruct the conductivity distribution.[4,5] Compared with the other electrical impedance imaging technologies,[6−9] MATMI methodology shows the advantage of avoiding the
"shielding effect" caused by the low-conductivity surface tissue layers of the human body by employing the magnetic excitation. Furthermore, high spatial resolution could be achieved in MAT-MI with high frequency magnetic excitation and acoustic detection.

MAT-MI has attracted much research interest in the past decades. Researchers have performed pilot studies in both theory and experiment.[1−5] Li et al.

[10]carried out a 3-D MAT-MI numerical simulation for the concentric and eccentric spherical conductivity models using the finite element method. Brinker and Roth[11] proposed an improved method by considering the electrical anisotropy of the biological tissues. Although the reconstructed images display the configuration of the measured layer, the detailed information inside each medium is invisible.[2−5] Therefore, it is a key issue to reconstruct the interior details from the detected acoustic signals in MAT-MI.

In this Letter, an improved methodology for the inverse problem solution of the 2-D Lorentz force distribution reconstruction is theoretically investigated.

All the acoustic signals are assumed to be generated from point sources, while their propagation in a 3- D free space follows the classical straight line theory. The formulae of the acoustic generation are provided for a multilayered circular cylinder phantom model with the conductivity close to the biological tissues.

In contrast to the previous studies[2−5] on MAT-MI,
the acoustic pressures are deconvolved from the detected waveforms, and the Lorentz force image reconstruction algorithm is then presented as the inverse problem solution to achieve the Lorentz force distribution inside the target.

Figure 1 illustrates the arrangement of the present MAT-MI system. A conductive object is placed in a static magnetic field 0 = 0ˆ. A time-varying pulsed magnetic field 1 = 1()ˆ in the same region is produced by a stimulating coil and is assumed to be homogeneous. The interaction between the magnetically induced eddy current in the conductive object and the static magnetic field 0 causes acoustic vibration at (*, ,* ) due to the Lorentz force. The generated acoustic signals transmit through the object and are detected by the transducers placed around the object. The acoustic pressure generated by the induced Lorentz force in the object is governed by the equation[12]

$$\nabla^{2}p-{\frac{1}{c^{2}}}{\frac{\partial^{2}p}{\partial t^{2}}}=\nabla\cdot\left[\mathbf{J}(\mathbf{r})\times\mathbf{B}_{0}\right],$$
= ∇ · [() × 0] , (1)
where  is the acoustic pressure, the vibration source
∇ · [() × 0] is a given function at the source point
, ∇2is the Laplacian operator,  is the acoustic velocity in the transmission medium, and () is the induced eddy current. The alternative Lorentz force is described as () = () × 0 along the normal direction of the induced eddy current. As both the induced eddy current and the corresponding Lorentz force exist in the  plane, the acoustic vibration source is considered in a 2-D configuration for the measured layer.



As shown in Fig. 1, the target is supposed to be a two-layer structure object with the uniform conductivities 2 and 1 of the inner and outer media, and it is put into an insulating medium of 0 = 0 s/m for acoustic coupling. Based on Faraday's principle, the induced electrical field  is determined by the pulsed magnetic field 1 as ∇ ×  = −∂1()/∂,
and the generated electrical field is in the  plane with its direction perpendicular to the pulsed magnetic field. The acoustic pressure () generated at is proportional to the intensity of the vibration source as () = ∇ · [()] = *∇ · {*[()()0]ˆ}, where ˆ is the unit normal vector of the induced eddy current. According to Green's function[13] of the acoustic diffraction transmission for each point source, the detected acoustic pressure transmitted from  to 
′can be described as

$$p(\mathbf{r}^{\prime},\mathbf{r})={\frac{{\frac{\partial}{\partial{\hat{n}}}}[\mathbf{F}_{L}(\mathbf{r})]}{4\pi|\mathbf{r}^{\prime}-\mathbf{r}|}}\otimes\delta(t-|\mathbf{r}^{\prime}-\mathbf{r}|/c),\quad\quad(2)$$

where ( − |
′ − |/) is the time delay for the transmission distance |
′ − |, and ⊗ is the convolution operator. For a focused transducer with an ideal infinitesimal aperture, only the acoustic signals with the

$$(1)$$

transmission direction perpendicular to the transducer surface as ˆ = ±(
′ − )/|
′ − | can be collected, which is indicated by the straight line theory in classical acoustics. As the entire target object is considered, the time series acoustic pressure detected at 
′can be expressed as the integral of all the acoustic sources within the whole object volume,

$$p(\mathbf{r}^{\prime},t)=\iiint_{V}{\frac{{\frac{\partial}{\partial{\hat{n}}}}[F_{L}(\mathbf{r}){\hat{n}}]}{4\pi|\mathbf{r}^{\prime}-\mathbf{r}|}}d\mathbf{r}\otimes\delta(t-|\mathbf{r}^{\prime}-\mathbf{r}|/c),\ (3)$$

where () is the amplitude of the Lorentz force with the direction ˆ. By performing integral operation along the normal direction ˆ for both sides of Eq. (3), we obtain

$$\int p(\mathbf{r}^{\prime},t)d{\hat{n}}$$ $$=\int d{\hat{n}}\int\!\!\!\int\!\!\!\int_{V}\frac{\frac{\partial}{\partial{\hat{n}}}[F_{L}(\mathbf{r}){\hat{n}}]}{4\pi|\mathbf{r}^{\prime}-\mathbf{r}|}d\mathbf{r}\otimes\delta(t-|\mathbf{r}^{\prime}-\mathbf{r}|/c).\tag{4}$$

The normal direction of the induced eddy current is
consistent with that of the Lorentz force (), which
is a linear function over time , so ˆ can be replaced by  in the calculation for ˆ = . Thus, Eq. (4) is
rewritten as
 Rewritten as  $ \int p(\mathbf{r}',t)cdt=\iiint_{V}\frac{F_{L}(\mathbf{r})}{4\pi|\mathbf{r}'-\mathbf{r}|}d\mathbf{r}\otimes\delta(t-|\mathbf{r}'-\mathbf{r}|/c).$  Note that the collection are continuous from below the ... 
Note that the collecting acoustic waveform by the transducer is a convolution between the detected
acoustic pressure (
′, ) and the impulse response ℎ()
of the transducer as
$$w(\mathbf{r}^{\prime},t)=p(\mathbf{r}^{\prime},t)\otimes h(t),$$
$$(6)$$
′, ) ⊗ ℎ(), (6)
where (
′, ) and (
′, ) both are the timedependent functions. Equation (6) can be expressed with their product in the frequency domain as () = ()(), where (), () and () are the Fourier spectra of (
′, ), (
′, ) and ℎ(), respectively. Based on the least mean square error estimation, (
′, ) can be restored with the Wiener filter for the deconvolution in the presence of noise,

$$p(\mathbf{r}^{\prime},t)=\mathrm{FFT}^{-1}\left({\frac{W(\omega)H^{*}(\omega)}{H(\omega)H^{*}(\omega)+C}}\right),\qquad(7)$$

where FFT−1denotes the inverse Fourier transform operation, the asterisks mean the complex conjugation and  is approximated by a constant based on the spectral density ratio of signal to noise.

With the deconvolved (
′, ), the 2-D distribution of the Lorentz force () can be reconstructed by using the simplified tomographic algorithm,[13]

$$F_{L}(\mathbf{r})={\frac{1}{2\pi c}}\int_{0}^{2\pi}{\frac{\hat{n}(\mathbf{r}-\mathbf{r}^{\prime})}{|\mathbf{r}^{\prime}-\mathbf{r}|^{2}}}\int p(\mathbf{r}^{\prime},t)d t d\phi,\ \ \ \ \ (8)$$

084302-2 where  is the angle of the transducer placed at 
′ =  exp() with the rotation radius of .

In the simulations, measurements are performed on a circled line with a radius of 100 mm, and the spatial and temporal grids are chosen to be 0.1 mm and 6.67 ns, respectively. The acoustic velocity is set to 1500 m/s approximately equal to that in water or biological soft tissues. The frequency of the pulsed magnetic field and the central frequency of the transducer both are set to 0.5 MHz. Figure 2 presents the cross section of the simulated conductivity distribution of the cylindrical phantom model, where gray scales represent different conductivity values. The conductivities for the three types of tissues A, B and C are set to 0.3 S/m, 0.6 S/m and 0.9 S/m with the corresponding radii of 80, 30 and 20 mm, respectively.



 

The generated acoustic signals are stimulated at different angles by using Eq. (3). Figure 3 illustrates the waveform measured at the angle of 62∘, where the six wave clusters are introduced by the impulse response of the transducer in the convolution process described by Eq. (6). The transmission distance in Fig. 3 represents the distance between 
′ and , and it can be calculated by |
′ − | =  with the time series waveforms. The wave amplitudes reflect the Lorentz force change between the adjacent tissues, which is determined by the conductivity difference and the geometry of the examined layer, and it is validated by the experimental results[2−5]in the previous studies.

Through low-frequency signal elimination using a narrow band-pass filter with a central frequency of 0.5 MHz, the deconvolution algorithm is applied to all the 360 detected waveforms without noise consideration. Therefore, the acoustic pressures (
′, ) could be extracted from the measured waveforms (
′, ),
while the corresponding result for the 62∘ measurement (i.e. referred to Fig. 3) is displayed in Fig. 4.

The impact behaving of the acoustic pressure is generated at the conductivity boundary with corresponding amplitude and polarity, which is introduced by the divergence effect of the Lorentz force.

 

 

The reconstructed 2-D image is presented in Fig. 5, in which the normalized color scale represents the relative amplitude of the Lorentz force. The amplitude difference in different tissues can be obviously displayed with clear tissue configuration. Meanwhile, the amplitude difference in each tissue can also be seen, which is produced by the vector superposition of the 084302-3 induced eddy currents. However, the eddy current at each acoustic source point is a 2-D vector in MATMI, which is perpendicular to the Lorentz force in the plane. The detected acoustic waveforms can only provide the acoustic pressures without the directional information and the corresponding direction of each Lorentz force could not be achieved with the proposed image reconstruction technique. In addition, the obvious transition zones at the conductivity boundaries are produced by the tomographic imaging algorithm. As a result, only the relative amplitude of the Lorentz force distribution in the examined layer can be imaged.

In conclusion, a new theory for the inverse problem of MAT-MI has been proposed for the reconstruction of 2-D Lorentz force distribution of the measured layer. A deconvolution algorithm is applied to extract acoustic pressures from the waveforms measured with transducers placed around the target object. The acoustic straight line theory is adopted for the description of acoustic wave propagation. With the magnetic stimulation of a coil, numerical stimulations are conducted for a multilayered cylindrical phantom model with its electrical conductivity close to native tissues. The 1-D acoustic pressure deconvolution and the 2-D Lorentz force distribution reconstruction are performed as the inverse problem solution.

The simulated results are in good agreements with the theoretical predictions. The proposed technique can provide the inner information of each medium inside the object and can be used to solve the problem of only reconstructing the conductivity boundary in MAT-MI, which is beneficial for further study on conductivity image reconstruction. The favorable results suggest the potential application of MAT-MI as a non-invasive electrical impedance imaging technology with improved spatial resolution and image contrast for medical imaging.

## References

[1] Xu Y and He B 2005 *Phys. Med. Biol.* 50 5175
[2] Li X, Xu Y and He B 2006 *J. Appl. Phys.* 99 066112
[3] Li X, Xu Y and He B 2007 *IEEE Trans. Biomed. Eng.* 54 323
[4] Ma Q Y and He B 2008 *IEEE Trans. Biomed. Eng.* 55 813 [5] Xia R M, Li X and He B 2007 *Appl. Phys. Lett.* 91 083903 [6] Xiang L Z, Xing D, Gu H M, Zhou F F, Yang D Wu, Zeng L M and Yang S H 2007 *Chin. Phys. Lett.* 24 751
[7] Su Y X, Wang R K, Zhang F and Yao J Q 2006 Chin. Phys. Lett. 23 512
[8] Kwon O, Woo E, Yoon J and Seo J K 2002 IEEE
Trans. Biomed. Eng. 49 160
[9] Wen H, Shah J and Balaban S 1998 IEEE
Trans. Biomed. Eng. 45 119
[10] Li X, Li X, Zhu S N and He B 2009 *Phys. Med. Biol.* 54 2667
[11] Brinker K and Roth B J 2008 *IEEE Trans. Biomed. Eng.*
55 1637
[12] Morse P M and Feshbach H 1953 Methods of Theoretical Physics (New York: McGraw-Hill)
[13] Xu Y and Wang L H 2004 *Phys. Rev. Lett.* 92 033902