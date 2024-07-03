Proceedings of the 17th **International Conference on Nuclear Engineering** 
ICONE17 July 12-16, 2009, Brussels, Belgium 

# Icone17-75578 Next Generation Safety Analysis Methods For Sfrs (8) Analyses Of Eutectics Between Fuel And Steel In Metal Fuel With Fpmd Code Vasp

Masashi Himi, Yuichi Yamamoto Analysis and Simulation Div., Japan Systems Corporation, Minami-cho, Kawasaki-ku, Kawasaki, Kanagawa 210-0015, Japan E-mail: himi.masashi@jskk.co.jp Yasuo Nagamine, Noriyuki Shirakawa, Yasushi Uehara The Institute of Applied Energy 

## Tatsumi Arima

Kyushu University 

## Abstract

There are two main objectives in this study. One is to estimate atomic diffusion coefficients in eutectic reaction between metal fuel and cladding materials in order to establish the atomic diffusion model for the COMPASS code. The other is to estimate their material properties such as Young's modulus in high temperature up to near melting points in core disruptive accidents (CDAs) in Sodium-cooled Fast Reactors (SFRs). We used the first principle molecular dynamics (FPMD) code VASP to realize the two objectives. 

We tried to understand the initiation mechanism of eutectics based on change of electronic state energy accompanied by change of Kohn-Sham energy, including phonon effect. 

In this project [1], three methods, phase diagram calculation (CALPHAD), classical molecular dynamics (CMD), and FPMD, are employed to understand the mechanism of eutectics and to introduce dynamic characteristics in eutectic phenomena into the COMPASS code. 

RI
v
**: Coordinate of nucleus or ion** I
r v
**: Coordinate of electron** 
s: sound velocity t**: Time** T: Temperature u **: Displacement of an atom around the node point of** 
lattice due to thermal fluctuation VH
: Hartree energy x**: mixing ratio of metal atoms** 
kD **: wave number at Debye temperature** 
Greek Symbols α **: Index for Lindemann's criterion of melting** 
i ε **: Energy of state of the Kohn-Sham orbital** i ω **: Frequency of phonon** 
ΘD
: Debye temperature Subscript I,J: **Nucleus or ion number** i,j: **Electron number** 
I **: Nucleus or ion** 
1 INTRODUCTION 
Eutectic reaction between metal fuel and steel cladding and/or steel structures is possibly caused in SFR's CDA. We have been studying this phenomenon with three kind of methods, CALPHAD, CMD, and FPMD since FY2005 [1,2,3]. 

In this paper, results of the analyses performed with the VASP code [4] until the end of FY2007, will be presented. 

We have investigated phase transition and eutectics in the systems containing small number of atoms of solid solution with 

NOMENCLATURE 

a**: Lattice constant** D**: Diffusion coefficient of ions or atoms** E

KS**: Kohn-Sham energy** 

EXC**: Exchange correlation energy** 

EB

: Band structure energy 

B

k **: Boltzmann constant** 

Nion**: Number of ions** 

n**: One-body density of electron** R**: Gas constant** 

multi-kind of atoms and pure metal. We carried out FPMD
analyses of the systems of Zr-U and U-Fe each with 16-atom and tried to extract physical characteristics describing eutectics from electronic states, where the characteristics are Kohn-Sham energy, band structure energy, exchange-correlation energy etc.

These analyses suggested that eutectics occur mainly depending on the intensity of metallic bond that depends on atomic composition.

We have also evaluated the phase diagram for the crystal structure of U-Fe 16-atom, by introducing phonons into free energy formulation to realize finite temperature state from the crystal structure optimized in OK. In this investigation, we showed the process to evaluate the phase diagram of eutectics quantum-mechanically, which would be utilized to judge eutectics occurrence.

FPMD has been also applied to the evaluation of metal fuel material properties. We evaluated melting points based on the change of Kohn-Sham energy in order to simulate empirical solidus line of U-Pu-Zr metal fuel. However, evaluated line was not in good agreement due to small number of atoms and small number of calculation cases.

Calculating the system of U-Pu-Zr contacting with Fe until 1ps, we observed melting on the interface judging from Lindemann's criterion on melting. Using these results, we evaluated atomic diffusion coefficient across the interface, extracting issues with respect to computing time and the derived limitations. The coefficient could be meaningfully evaluated even in this small time interval and could be utilized in the atomic diffusion model for COMPASS code [1] .

## Analyses Of Energy States Of Metal Fuel 2

AND Fe After preparing "optimized state", which is the crystal state of mixed metal fuel and Fe atoms that has minimum energy at near zero pressure and OK obtained by adjusting lattice constants, energy states were analyzed by FPMD method with phonon effect, increasing temperature.

## Analyses Of U-Fe And U-Zr Systems 2.1

Potential energy of eutectic atomic system such as U-Fe becomes smaller than the average potential energy of U-U and Fe-Fe [3]. We related this fact to energy change of electronic state to systematically understand eutectic initiation.

We selected and analyzed two mixed 16-atomic systems, one is U-Zr that had no eutectics and the other is U-Fe that had eutectics. Phase diagrams of U-Zr and U-Fe are shown in Fig.1 and Fig.2 calculated with the ThermoCalc code based on CALPHAD [5,6] , where analyzed cases are shown with three and five red circles, respectively. These eight cases are Zr16, U8Zr8, U16 in Fig.1 and (U16), U12Fe4, U8Fe8, U4Fe12, Fe16 in Fig.2. U16 case is the same in U-Zr and U-Fe. Note that melting points of Zr, U and Fe are 2125K, 1405.5K and 1808K, respectively [ 7 ].

![1_image_0.png](1_image_0.png)

![1_image_1.png](1_image_1.png)

Two-body correlation functions for seven cases are shown in Fig.3-Fig.9. Each case clearly leaves crystal correlation structure at 500K in liquid state at higher temperatures, showing that crystal state does not change so much that it makes difficult to discriminate liquid state from solid one by Lindemann's criterion on melting.

![2_image_0.png](2_image_0.png)

![2_image_1.png](2_image_1.png)

Eigen values of occupied electronic states included in these seven electronic density of states at 500K and 2500K are shown in Fig.10 and Fig.11, respectively. These eigen values are averaged over wave number space since they distribute in the k-space direction. 

Electron configurations of Zr, Fe and U are Zr: [Kr]5s24d2, Fe: [Ar]4s23d6, and U: [Rn]7s25f36d1, respectively, where 
[Ar]=(1s2)(2s22p6**)(3s**23p6), 
[Kr]=(1s2)(2s22p6)(3s23p6)(4s23d104p6**), and** 
[Rn]=(1s2)(2s22p6)(3s23p6)(4s23d104p6)(5s24d105p6**) (6s**24f145d106p6).

With respect to Uranium, VASP considers 6s and 6p orbitals as valence states and the number of valence electrons is 14. **The numbers of valence electrons are 4 in Zr, and 8 in Fe.** Mixing of U with Zr or Fe does not change the number of electron states inside those of 6s and 6p orbitals, which number of states are shown in both Fig.10 and Fig.11. For U12Fe4 and U4Fe12, the numbers of occupied states per 4 atoms are shown to avoiding fractions. Note that two electrons can seat in one state because spin states are contracted. 

From these two figures, it is found that the energy at 2500K (liquid) decreases compared with that at 500K (solid) in U12Fe4 and U4Fe12. On the other hand, energy change in U8Fe8 is clearly smaller than these two systems. Furthermore, energy change in Zr-U is not as significant as that in Fe-U is. That is, we could assume that the energy of electronic states in U12Fe4 and U4Fe12 that cause eutectics decreases at the temperature higher enough than melting point. 

Since FPMD calculations of small number of atoms with finite temperature are often accompanied by large fluctuation, we continued the calculation until the average energy reaches near constant. The following consideration is based on the averaged energy. The energy change without thermal fluctuation at 0K is shown in Ref.[3]. 

![3_image_0.png](3_image_0.png)

![3_image_3.png](3_image_3.png) 

$$s_{i}-{\frac{1}{2}}\int d r F$$

∑ ∫ ∫
= − + − ( )
[ ] E n δ
( ) ( ) [ ]
2
1n r
n
E rd V r n r E n rdXC
H XC
ii
KS v v v v v
δ

ε
**, (1)** 
where the first term in RHS is the band structure energy ( EB
) 
which is the summation of eigen values of electronic states, the second is the Hartree energy ( VH
) of coulomb interaction multiplied by (-1/2), the third and the forth denote the exchange-correlation interaction for valence electrons. 

Phase change from solid to liquid generates energy corresponding to latent heat. Therefore, Kohn-Sham energy as a function of temperature forms an ogive as shown in Fig.12. We assume that melting point is an inflection point of the ogive. 

We scaled the Kohn-Sham energy and the temperature, as 
(2500 ) **(500** )
( ) **(500** )
( )E K E K
E T E K
f E KS KS
KS KS
KS
−
−
=**, (2)** 
and 2500( ) **500(** )
500( )
( )K K
T K
f T−
−
=**, (3)** 
respectively. Then, the melting point is the temperature that the ogive Eq.(2) exceeds Eq.(3), that is when the ogive becomes convex. Estimated melting temperatures are >2125K for Zr16, >1600K for U8Zr8, 1405.5K for U16, 1000K for U12Fe4, 1400-1800K for U8Fe8, 1400K for U4Fe12, and 1808K for Fe16, respectively, which are good estimates. 

![3_image_1.png](3_image_1.png)

![3_image_2.png](3_image_2.png) 
Eq.(4) is the nondimensionalized band structure energy EB
per one valence electron, 
(2500 ) **(500** )
(500 ) ( )
( )E K E K
E K E T
f E
B B
B B
B−
−
=**, (4)** 
which is shown in Fig.13. Comparing ( ) EB
f **of each system,** 
Zr8U8 does not fall below Zr16 and U16. Meanwhile U12Fe4 and U8Fe8 fall below both U16 and Fe16 at 1400K and 14001800K, respectively, which shows the electronic state energy in U-Fe system decreases across the phase change, in contrast that in Zr-U system does not. 

In the same way Hartree energy VH
(positive) is also nondimensionalized as Eq.(5), 
{ (500 ) **(500** )} 2/
( )
( )V K V K
V T
g V
H H
H
H+
=**, (5)** 
which is shown in Fig.14. ( ) VH
g **of each system increases as** 
temperature rises. 

![4_image_0.png](4_image_0.png)

![4_image_1.png](4_image_1.png) 

![4_image_3.png](4_image_3.png)

![4_image_2.png](4_image_2.png)

![4_image_5.png](4_image_5.png)

![4_image_6.png](4_image_6.png) 
$\left(\mathfrak{H}\right)$. 
We also nondimensionalized the exchange-correlation energy ( EXC −VXC
: negative in Zr16, Zr8U8, U16 and positive in U12Fe4, U8Fe8, U4Fe12, Fe16) **as Eq.(6),** 

$$g(E_{\chi_{C}}-V_{\chi_{C}})=\frac{(E_{\chi_{C}}-V_{\chi_{C}})(T)}{\{(E_{\chi_{C}}-V_{\chi_{C}})(500K)+(E_{\chi_{C}}-V_{\chi_{C}})(500K)\}/2},\tag{6}$$  which is shown in Fig.15. $g(E_{\chi_{C}}-V_{\chi_{C}})$ of Zr8U8 has little 
dependence on temperature, meanwhile those of U12Fe4, U8Fe8, and U4Fe12 has clear dependence on temperature. 

We presume the initiation mechanism of eutectics based on these analyses that the Kohn-Sham energy increases around melting point by the latent heat through phase change, the band structure energy decreases, and the exchange-correlation energy changes. Namely, the electronic state energy changes in a certain composition of atoms, which affect the metallic bond. 

## 2.2 Phonon Effect

We statically analyzed optimized **energy states for some UFe systems of 16-atom using VASP with phonon model [8].** 
Since Fe-crystal structure is bcc and U-crystal structure is orthorhombic at 0K, we calculated optimized state in each structure, changing composition ratio. Generally speaking, stability of crystal can be explained by estimating its free energy. Figure 16 shows two free energy curves for bcc and orthorhombic for each atomic composition, and tangent line common to the two curves. As tangent point corresponds to the equilibrium state in the atomic composition, coexistent domain between bcc and orthorhombic, that is eutectic domain, can be estimated. This result roughly reproduces the phase diagram shown in Fig.2. 

![4_image_4.png](4_image_4.png)

The main effect of finite temperature is thermal fluctuation of crystal structure, which fluctuation can be interpreted as phonons. Therefore, we calculated the contribution of phonons to the free energy as well as the entropy of mixing atoms, stopping the ion motion and simulating lattice oscillation with phonons. 

Free energy G **of a system is described by Eq.(7),** 
G(T x) E(x) T S (x) N F (T ) mix + A ph , = − ⋅ **, (7)** 
where the first term in RHS is the cohesive energy that is obtained from optimization analysis at 0K, mix S **is the mixing** 
entropy, 

entropy,  $$S_{mix}\big{(}x\big{)}=-R\big{\{}x\ln x+\big{(}1-x\big{)}\ln(1-x)\big{\}},\tag{8}$$  and $F_{ph}$ is the free energy of phonons,  $$F_{ph}=\frac{1}{2}\sum_{l}\hbar\omega_{l}+\sum_{l}\frac{\hbar\omega_{l}}{e^{\hbar\omega_{l}/k_{B}T}-1}+k_{B}T\sum_{l}\ln(1-e^{-\hbar\omega_{l}/k_{B}T})\,.\tag{9}$$

Here, we used Avogadro number NA **and Boltzmann constant** kB
in [1/mole] and [J/K], respectively, for consistent representation. 

We calculated again similar cases in Fig.16 under finite temperature to estimate dependence of coexistence domain on temperature as shown in Fig.17. The dotted lines in this figure are shown for comparison based on the data shown in Fig.2. Calculated coexistence domain tends to narrow as the temperature rises. 

Although calculated coexistence domain has some shift from empirical data, our procedure to quantum mechanically reproduce phase diagram is found to be appropriate and effective. 

![5_image_2.png](5_image_2.png) 

## 3 Simulation Of Metal Fuel U-Pu-Zr

From a practical viewpoint of metal fuel, U-Pu-Zr is superior to U-Pu because the former has higher melting point and can coexist with stainless steel cladding due to smaller eutectic reaction rate. We calculated melting points of U-Pu-Zr, changing composition as U76%Pu24% (U41, Pu13 atoms), U50%Pu24%Zr26% (U27, Pu13, Zr14 atoms), 
U26%Pu24%Zr50% (U14, Pu13, Zr27 atoms). 

Analytically estimated solidus lines of U-Pu-Zr are shown in Fig.18 [9]. 

Preparing uniformly mixed system for each composition, the system was optimized at each temperature. Two-body correlation functions are shown in Fig.19-Fig.21. 

Each case clearly leaves crystal structure even after melting in the same way in section 2.1. 

![5_image_0.png](5_image_0.png) 

![5_image_1.png](5_image_1.png)

Fig.19 Calculated two-body correlation functions in U76%Pu24% 

![5_image_3.png](5_image_3.png)

![6_image_0.png](6_image_0.png)

The average and standard deviation of both Kohn-Sham energy and band structure energy in each case was calculated and shown in Fig.22-Fig.27, where cases of U100% (U16), U50%Zr50% (U8,Zr8), Zr100% (Zr16) are the same in section 2.1. The deviation of band structure energy is much smaller than that of Kohn-Sham energy. 

Point estimate of melting temperature is not obtained due to the variation of temperature in FPMD. Deviation of KohnSham energy is large enough to form clear ogive curve so that the accuracy of flexion point to give melting temperature is not good. 

The reading of melting temperature in Fig.18 is compared for each case with calculated results, giving appropriate results, as follows. Solidus line Calculation U76%Pu24% **: 1200K 1000-1400K** U50%Pu24%Zr26%: 1400K 1200-1600K U26%Pu24%Zr50%: 1600K 1400-1800K U100%: 1405K 1200-1800K 
U50%Zr50%: 1700K 1400-2100K Zr100%: 2125K 1800-2500K 
Note that broader temperature deviation in U100%, 
U50%Zr50%, and Zr100% is caused by small number of 16 atoms engaged for each case, meanwhile 54 atoms are used in U76%Pu24%, U50%Pu24%Zr26%, and U26%Pu24%Zr50%. 

![6_image_1.png](6_image_1.png) 

 
Fig.22 Average and standard deviation of Kohn-Sham energy and band structure energy in U76%Pu24% 

![6_image_2.png](6_image_2.png) 

 
Fig.23 Average and standard deviation of Kohn-Sham energy and band structure energy in U50%Pu24%Zr26% 

![6_image_3.png](6_image_3.png) 

![7_image_0.png](7_image_0.png) 

![7_image_1.png](7_image_1.png) 

Fig.26 Average and standard deviation of Kohn-Sham energy and band structure energy in U50%Zr50% 

![7_image_2.png](7_image_2.png) 

## 4 Contact Analysis Between Metal Fuel Upu-Zr And Cladding Fe

Contact analysis between metal fuel and cladding Fe is supposed to investigate eutectics formation process in pin failure stage in CDA. 

Melting point (Tm**) of standard metal fuel (U50at%,** 
Pu25at%, Zr25at%) is about 1400K as shown in Fig.18 and that of Fe is about 1808K. We analyzed two cases at 1300K (<Tm) 
and 1500K (>Tm**) of system temperature to examine the** 
difference of electronic states. 

The U-Pu-Zr system is composed of U48, Pu24 and Zr24 atoms, 96 atoms in all. U, Pu and Zr atoms are uniformly contained in the system. 

The Fe system has 150 Fe atoms in bcc, and this system was prepared to have optimized lattice constants with adjusted pressure at both 1300K and 1500K. 

Conforming the size of Fe basic cell (5×5) to U-Pu-Zr basic cell (4×4), Fe system was set upper and U-Pu-Zr system lower to make combined system with gap of one Fe basic cell for both 1300K and 1500K cases. Cyclic boundary conditions are imposed on this structure as a supercell. This calculation was the largest one we had done until FY2007, so we aimed to calculate up to 1ps with time step 3fs to investigate how Fe atoms diffuse into metal fuel through the interface. 

Position of atoms, diffusion coefficient, and the index for Lindemann's criterion of melting [10,11] (we call this Lindemann index, shortly hereafter) at 1300K are shown in Fig.28-Fig.30, and those at 1500K in Fig.31-Fig.33 in the end time of calculation, respectively. 

Diffusion coefficients D in 1300K and 1500K cases are shown in Fig.29 and Fig.30, respectively, where D is defined as 
[ ] ∑
−
= =
→∞ →∞i I I
ion t t t R t R
N
D D t6 1 ( ) )0( lim ( ) lim r r 2
. (10) 
Lindemann index α **in 1300K and 1500K cases are shown** 
in Fig.30 and Fig.33, respectively. Equation (11) describes the relation between α **and D,** 

[ ]a
$$t={\frac{\sqrt{D(t)\cdot6t}}{\sqrt{D(t)\cdot6t}}}$$
t u t a( ) 6
( ) ( ) /
/1 2
2⋅
α = = **. (11)** 
In the beginning of calculation, Zr-atom near the interface starts moving because of its small mass. U- and Pu-atom begin to move affected by Zr-atom displacement. 

In the 1300K case, Ds of U, Pu and Zr approaches to the bulk D. Displacement of Fe-atom is smaller because its melting temperature is higher than 1300K. D converges on a constant and diffusion starts when α **becomes proportional to time. In** 
this case, as the index does not become proportional to time until 1ps, melting through the interface is not judged to occur, which is appropriate because the melting point of metal fuel, around 1400K, is much higher than 1300K. 

In the 1500K case, calculation is much more time consuming than the 1300K case. As shown in Fig.33, time history of the index is not long enough to judge convergence. 

Parallel calculations with more CPUs have been performed in FY2008. 

![8_image_0.png](8_image_0.png)

Fig.28 Atomic configuration in the contact calculation between metal fuel U-Pu-Zr and cladding Fe at 1300K (at 630 fs). 

![8_image_4.png](8_image_4.png) 

 
Fig.29 Diffusion coefficient in the contact calculation between metal fuel U-Pu-Zr and cladding Fe at 1300K. 

![8_image_6.png](8_image_6.png) 

![8_image_1.png](8_image_1.png)

![8_image_2.png](8_image_2.png)

Fig.31 Atomic configuration in the contact calculation between 

![8_image_3.png](8_image_3.png)

metal fuel U-Pu-Zr and cladding Fe at 1500K (at 300 fs). 

![8_image_5.png](8_image_5.png) 

 
Fig.32 Diffusion coefficient in the contact calculation between metal fuel U-Pu-Zr and cladding Fe at 1500K. 

![8_image_7.png](8_image_7.png) 

 
Fig.33 Lindemann index in the contact calculation between metal fuel U-Pu-Zr and cladding Fe at 1500K. 

## 5 Initiation Mechanism Of Eutectics Inferred From Fpmd Analyses

Metal crystals have a larger number of **coordination, that is** 
the number of valence electrons per atom is small so that the distance between ions becomes large, which makes valence electrons be free electrons. As temperature rises, ionic oscillation becomes large disturbing potential configuration, which scatters free electrons, weaken metallic bonds, and giving rise to melting. 

Furthermore, in the eutectic combination of atoms, band structure energy decreases and correlation function changes. Such change in electronic states could affect **metallic bonds.**
More specifically speaking in our [U-Pu-Zr, Fe] system, through above described generic phenomenology, **Fe-ion moves** 
into U changing bondage between Fe and U to form a local molecular structure capturing neighbor free electrons, which thus decreases the number of electrons involved in metallic bond of U to break the bond and to give eutectic melting.

Lindemann **index in high temperature is approximated as** 

k T M k k M s k T t B I B D D I B 2 2 2 2 2 2 ( ) 6.1 6.1Θ ≈ = h α , (12) which by Pines [11] reduces to  2/1 2 2 2/1 2                 Θ = h h 6.1 k T k M k B melt D melt I B D α . (13)  2/1 2 2 2/1                 =     6.1 4.2 a k T M B melt melt I 2 α Thus,  Dsk D / kB Tmelt / a 2/1 Θ = h ∝ , (14)  where D D B Θ = hsk / k is Debye temperature, kD is the wave 

number at Debye temperature. 
Assuming that the sound velocity s **and lattice constant** a be constant, kD **becomes smaller in U75%Fe25% eutectics to** 
vanish fine lattice oscillation and to left course oscillation, which suggests formation of local molecular structure. 6 SUMMARY 
We investigated the initiation mechanism of eutectics between metal fuel and fuel pin cladding in Core Disruptive Accidents in Sodium-cooled Fast Reactors, using first principle molecular dynamics code VASP. 

Comparing U-Fe with U-Zr, in the eutectic combination UFe, the band structure energy decreases and the correlation function changes accompanied by the change of Kohn-Sham energy. Based on this electronic state change, we tried to ascribe the initiation mechanism to the change in metallic bond. 

We also tried to establish the procedure to reproduce phase diagram for the eutectic combination with phonon model statically combined VASP results, which is successful at least qualitatively. Furthermore, we analyzed solid lines for metal fuel U-Pu-Zr changing atomic composition and obtained appropriate estimate compared with empirical data. 

We preliminary analyzed contact configuration of U-Pu-Zr and Fe. Parallel calculations with more CPUs have been performed in FY2008. These analyses aim to provide atomic diffusion coefficient to the atomic diffusion model between mesoscopic particles to be implemented in the COMPASS code. 

Our calculations have to treat much larger number of atoms and much longer physical time to take dynamical aspect of eutectics into account, which would be left to classical molecular dynamics [12]. We continue to make every effort to make potentials between specific combination of atoms such as Pu-Fe. 

## Acknowledgments

The present study was carried out within the task "R & D 
of the Next Generation Safety Analysis Methods for Fast Reactors with New Computational Science and Technology" entrusted from the Ministry of Education, Culture, Sports, Science and Technology of Japan. 

The computation was mainly carried out using the computer facilities at Research Institute for Information Technology, Kyushu University. 

## References

[1] Koshizuka, S., et al., "R & D of the Next Generation Safety Analysis Methods for Fast Reactors with New Computational Science and Technology (1) Brief Introduction of the Project and Development of Structural Mechanics Module of the COMPASS Code," ICONE1648499 (2008). 

[2] Ito, T. et al., "R & D of the Next Generation Safety Analysis Methods for Fast Reactors with New Computational Science and Technology (5) Study of Eutectic Reaction Between Metals: Classical Molecular Dynamics Approach," ICONE16-48500 (2008). 

[3] Himi, M., et al., "R & D of the Next Generation Safety Analysis Methods for Fast Reactors with New Computational Science and Technology (7) Study of Eutectic Reaction Between Metals: First Principle Molecular Dynamics Approach ," ICONE16-48482 (2008). 

[4] Kresse, G. and Furthmüller, J., "VASP the GUIDE," 
http://cms.mpi.univie.ac.at/vasp/. 

[5] http://www.calphad.org/ 
[6] Saunders, N. and Miodownik, A.P., "CALPHAD: A 
Comprehensive Guide," Pergamon Material Series, Vol. 1, Pergamon, Oxford, UK, 1998. 

[7] Metals Handbook, 10th ed., edited by ASM. [8] https://sourceforge.net/project/showfiles.php?group_id= 
161614 
[9] Pultonium fuel technology, edited by AESJ(Jan.1998) [10] Lindemann, F., Phys. Z., 11, 609 (1910). [11] Pines, D., Elementary Excitations in Solids, W.A.Benjamin, inc. (1964). 

[12] Ito, T. et al., "Next Generation Safety Analysis Methods for SFRs (7) Potential Model for Classical Molecular Dynamics on Pu-Fe System," ICONE17-75591 (2009). 