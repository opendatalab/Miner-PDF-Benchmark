# HEATS OF FORMATION FOR BORON COMPOUNDS BASED ON QUANTUM CHEMICAL CALCULATIONS 

JIAHENG ZHANG, SHIQIAN WEI, CHAOZHU MAO, LIANG CHEN,<br>HAIXIANG GAO, WENFENG ZHOU* and ZHIQIANG ZHOU*<br>Department of Applied Chemistry<br>China Agricultural University, Beijing, P. R. China<br>*zhouwenfeng@cau.edu.cn

Received 26 May 2009

Accepted 31 May 2010


#### Abstract

We have calculated the heats of formation at $298.15 \mathrm{~K}$ of series of boron compounds including $\mathrm{H}, \mathrm{N}, \mathrm{O}, \mathrm{F}, \mathrm{Cl}$ atoms using the atomization enthalpies analysis based on eleven quantum chemical calculations. The majority of calculated values are in excellent agreement with available experiment values and Gaussian-n methods perform more accurate evaluations than other approaches. As with the existing literature, the following calculations of the heats of formation of borides containing light atoms are recommended as accurate values: $\Delta_{\mathrm{f}} \mathrm{H}_{\mathrm{G} 2,298}(\mathrm{BH})=442.731 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}, \Delta_{\mathrm{f}} \mathrm{H}_{\mathrm{G} 2,298}\left(\mathrm{BF}_{3}\right)=$ $-1135.749 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$, the deviations are respectively $0.031 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$ and $0.251 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$. Furthermore, $a b$ initio calculations of heats of formation of chlorinated boron compounds also show good accuracy and comparisons with previous thermodynamics data are made.


Keywords: Boride; heat of formation; Gaussian-n method; ab initio calculations.

## 1. Introduction

Boron occupies a unique position in the IIIA main group because of its properties, which borderline between metals and nonmetals; crystalline boron is inert chemically, while amorphous boron is a preferred additive to high-energy propellant for its high-volume heat value and is extensively applied in aerospace engineering. Boron has the capacity to form stable covalently bonded molecular networks; some boron compounds have particular thermodynamic characteristics and thus have much potential for commercial applications. For example, the direct borohydride fuel cell is a novel fuel cell that has a high theoretical specific energy and is environmentally benign. ${ }^{1}$ Another example is boron trihalides, which are of considerable recent interest because of their use in radio-frequency ( $\mathrm{rf}$ ) plasmas and the commercial etching of metals and semiconductors. ${ }^{2}$ Despite these examples of commercial use, our understanding of boron chemistry is limited. For instance, boron's element of[^0]atomic heat of formation is associated with uncertainties greater than or equal to about $1 \mathrm{kcal} / \mathrm{mol}{ }^{3}$ Furthermore, there is no consistent and reliable set of thermodynamic data for boron compounds. From a researcher's perspective, the most basic thermodynamic property of a polyatomic molecule is the heat of formation. Due to the lack of accurate knowledge of the thermodynamic properties for most of the molecules involved in modeling atmospheric processes, experiments focused on these processes and combustion are unable to obtain accurate heat of formation data. With this in mind, it is not surprising to find that some of the boron compounds' heats of formation have been studied using computational chemistry techniques. In 1989, Barone and Minichino studied the structure formation enthalpy of $\mathrm{B}_{2} \mathrm{H}_{6}$ using the Hartree-Fock level and employing the 6-21* basis set. ${ }^{4}$ Rablen and Hartwig computed the atomization energies of $\mathrm{BF}_{\mathrm{n}}$ species using the $\mathrm{G} 2$ and CBS4 approaches. ${ }^{5}$ Bauschlicher and Ricca evaluated accurate heats of formation for $\mathrm{BF}_{\mathrm{n}}$ and $\mathrm{BCl}_{\mathrm{n}}(n=1-3)$ optimized by the B3LYP $/ 6-311+\mathrm{G}(2 \mathrm{df})$ approach and used $\operatorname{CCSD}(\mathrm{T})$ results. ${ }^{6}$ Over the last three years, there has been a large number of papers published in this area, and theoretical research found in these literature include thermodynamic equilibrium calculations for mixtures involving $\mathrm{B} / \mathrm{F} / \mathrm{N} / \mathrm{H} .7,8$

Taking a wide view of the related questions being researched, there is no system being studied that centers on the boron element and compares the thermodynamic properties of different kinds of borides, especially the heats of formation. Considering the weakness in processing halide-containing systems for Gaussian-n methods, ${ }^{9}$ there are also no series of high-level calculations for chlorinated boron compounds that have been done - in particular the heat of formation for $\mathrm{B}_{2} \mathrm{Cl}_{4}$, despite it being very important for the research of polyboron halide. ${ }^{10}$ Despite the deficiency of Gaussian-n methods, with the development of computer technology, computational quantum chemical calculations have become the most accurate method and can be widely used to predict the heat of formation. The Gaussian-n methods used by Curtiss et al. ${ }^{11,12}$ and the complete basis set (CBS) extrapolation methods ${ }^{13,14}$ are among the most popular theoretical methods for heat of formation calculations. In addition, in this field some modifications of these theoretical approaches have been used frequently, such as G2MP2, G3MP3, ${ }^{15}$ G3MP2B3, ${ }^{16}$ and G3B3. ${ }^{17}$ Therefore, given the interest in these problems, we chose 11 high-level quantum chemical calculations and predicted the heats of formation based on these methods at $298.15 \mathrm{~K}$ for 14 boron compounds including $\mathrm{H}, \mathrm{N}, \mathrm{O}, \mathrm{F}$, and $\mathrm{Cl}$ atoms. Based on these data, we recommend a reliable computational quantum chemical calculation and, more importantly, determine accurate heats of formation for future studies on chlorinated boron compounds.

## 2. Method

### 2.1. Computational methods

Our computational approach for calculating the heats of formation for boron compounds was to use atomization enthalpies. This approach has the advantage of using
the accurately known enthalpies of formation for the common elements $\mathrm{B}, \mathrm{H}, \mathrm{N}, \mathrm{O}$, $\mathrm{F}$, and $\mathrm{Cl}$ and combining them with the computational data. As mentioned above, we used 11 high-level quantum chemical calculations; the Gaussian-n methods and complete basis set methods were our first choice. The general principle of Gaussian$\mathrm{n}$ theory is to perform calculations at a high level of theory, such as $\operatorname{QCISD}(\mathrm{T})$. The theory is based on corrections to energy due to deficiencies of the basis set; these are performed assuming that high-level correlations can be treated separately and combined in an additive manner. Different versions of Gaussian-n theory with different combination schemes has resulted in different accuracies and computational costs. ${ }^{18}$ It should be noted that the G3 suit of computational methods is only a procedure for calculating total electronic energies of atoms and molecules containing atoms with $Z \leq 18$ (hydrogen to argon). The general principle of the CBS method is to extrapolate SCF and correlation energies with the finite one-electron basis set to the complete basis set limit through a series of single point calculations. Various extrapolation schemes for various one-electron basis sets lead to various correlation levels. ${ }^{19}$ Based on this information, we used three Gaussian-n methods (G1, G2, and G3) and four CBS methods (CBS-QB3, CBS-4O, CBS-4M, and CBS-Q). Although Gaussian-n and CBS methods can obtain accurate computational data, both of them have obvious drawbacks, the main one being that these methods are time-consuming. Thus, many modified methods were used in our calculations, such as G3MP2, G2MP2, G3MP2B3, and G3B3. G3MP2 and G2MP2 theory are modifications of G3 and G2 theory; these methods use second-order Moller-Plesset perturbation theory with the basis sets $6-31 \mathrm{G}(\mathrm{d})$ and $6-311+\mathrm{G}(2 \mathrm{df}, 2 \mathrm{p})$ on Li-Ne and $6-311+(3 \mathrm{df}, 2 \mathrm{p})$ on Na-Ar. In addition, a single-point quadratic configuration interaction in these methods was carried out for energy in the QCISD(T)/6-31G(d) set. G3MP2B3 and G3B3 theory are further modifications of G3MP2 and G3 theory; compared to the former methods, these methods use geometries and zero-point vibrational energy (ZPVE) scaled by 0.96 from B3LYP/6-31G(d) calculations. They can be applied to larger systems with more than 150 electrons and are evaluation methods that are economical with regard to time. ${ }^{20}$ All calculations for these 11 methods were performed with the Gaussian 03 package of programs. ${ }^{21}$

### 2.2. Thermodynamic analysis

Calculating heats of formation at $298.15 \mathrm{~K}$ is not a straightforward task; it can be split into three steps. The first is to calculate the nonrelativistic atomization energy $\sum D_{0}$, which is the energy needed to dissociate a molecule into its separate atoms. For any molecule, represented here as $\mathrm{A}_{x} \mathrm{~B}_{y} \mathrm{C}_{z}$, the atomization energy is given by:

$$
\begin{aligned}
\sum D_{0}\left(\mathrm{~A}_{x} \mathrm{~B}_{y} \mathrm{C}_{z}\right)= & x \varepsilon 0(\mathrm{~A})+y \varepsilon 0(\mathrm{~B})+0 z \varepsilon 0(C) \\
& -\varepsilon 0\left(\mathrm{~A}_{x} \mathrm{~B}_{y} \mathrm{C}_{z},\right)+\varepsilon \mathrm{ZPE}\left(\mathrm{A}_{x} \mathrm{~B}_{y} \mathrm{C}_{z},\right)
\end{aligned}
$$

where $\varepsilon_{0}$ is the total energy for constituent atoms or molecules and $\varepsilon_{\mathrm{ZPE}}$ is the zeropoint energy of the molecule. The second step is to calculate the heat of formation
at $0 \mathrm{~K} \Delta_{f} H^{0}$, and it is given by:

$$
\begin{aligned}
\Delta_{f} H^{0}\left(\mathrm{~A}_{x} \mathrm{~B}_{y} \mathrm{C}_{z}, 0 \mathrm{~K}\right)= & x \Delta_{f} H^{0}(\mathrm{~A}, 0 \mathrm{~K})+y \Delta_{f} H^{0}(\mathrm{~B}, 0 \mathrm{~K}) \\
& +z \Delta_{f} H^{0}(\mathrm{C}, 0 \mathrm{~K})-\sum \mathrm{D}_{0}\left(\mathrm{~A}_{x} \mathrm{~B}_{y} \mathrm{C}_{z}\right)
\end{aligned}
$$

Theoretical heats of formation at $298.15 \mathrm{~K}$ were calculated by correcting $\Delta_{f} H^{0}$ at $0 \mathrm{~K}$ as follows:

$$
\begin{aligned}
\Delta_{f} H^{0}\left(\mathrm{~A}_{x} \mathrm{~B}_{y} \mathrm{C}_{z}, 298 \mathrm{~K}\right)= & \Delta_{f} H^{0}\left(\mathrm{~A}_{x} \mathrm{~B}_{y} \mathrm{C}_{z}, 0 \mathrm{~K}\right)+H^{0}\left(\mathrm{~A}_{x} \mathrm{~B}_{y} \mathrm{C}_{z}, 298 \mathrm{~K}\right) \\
& -H^{0}\left(\mathrm{~A}_{x} \mathrm{~B}_{y} \mathrm{C}_{z}, 0 \mathrm{~K}\right)-x\left[H^{0}(\mathrm{~A}, 298 \mathrm{~K})-H^{0}(\mathrm{~A}, 0 \mathrm{~K})\right] \\
& -y\left[H^{0}(\mathrm{~B}, 298 \mathrm{~K})-H^{0}(\mathrm{~B}, 0 \mathrm{~K})\right] \\
& -z\left[H^{0}(\mathrm{C}, 298 \mathrm{~K})-H^{0}(\mathrm{C}, 0 \mathrm{~K})\right]
\end{aligned}
$$

In this step, the value of $\left[H^{0}\left(\mathrm{~A}_{x} \mathrm{~B}_{y} \mathrm{C}_{z}, 298 \mathrm{~K}\right)-H^{0}\left(\mathrm{~A}_{x} \mathrm{~B}_{y} \mathrm{C}_{z}, 0 \mathrm{~K}\right)\right]$ can be replaced by $H_{\text {corr }}-\varepsilon_{\text {ZPE }}\left(\mathrm{A}_{x} \mathrm{~B}_{y} \mathrm{C}_{z}\right)$, where $H_{\text {corr }}$ is the correction to enthalpy due to internal energy. We combine the above three equations and integrate as follows:

$$
\begin{aligned}
\Delta_{f} H^{0}\left(\mathrm{~A}_{x} \mathrm{~B}_{y} \mathrm{C}_{z}, 298 K\right)= & x \Delta_{f} H^{0}(\mathrm{~A}, 0 \mathrm{~K})+y \Delta_{f} H^{0}(\mathrm{~B}, 0 \mathrm{~K})+z \Delta_{f} H^{0}(\mathrm{C}, 0 \mathrm{~K}) \\
& -x\left[H^{0}(\mathrm{~A}, 298 \mathrm{~K})-H^{0}(\mathrm{~A}, 0 \mathrm{~K})\right]-y\left[H^{0}(\mathrm{~B}, 298 \mathrm{~K})\right. \\
& \left.-H^{0}(\mathrm{~B}, 0 \mathrm{~K})\right]-z\left[H^{0}(\mathrm{C}, 298 \mathrm{~K})-H^{0}(\mathrm{C}, 0 \mathrm{~K})\right] \\
& +H_{\text {corr }}+\varepsilon_{0}\left(\mathrm{~A}_{x} \mathrm{~B}_{y} \mathrm{C}_{z}\right)+x \varepsilon 0(\mathrm{~A})+y \varepsilon 0(\mathrm{~B})+0 z \varepsilon 0(\mathrm{C})
\end{aligned}
$$

In the last two steps, we need a few components of data, both experimental and calculated. The value of $\left[H_{\text {corr }}+\varepsilon_{0}\left(\mathrm{~A}_{x} \mathrm{~B}_{y} \mathrm{C}_{z}\right)\right]$ and $\varepsilon_{0}$ of each atom can be obtained by calculation. The experimental data used are the JANAF values for the heats of formation of $\mathrm{H}, \mathrm{N}, \mathrm{O}, \mathrm{F}$, and $\mathrm{Cl}$ atoms at $0 \mathrm{~K}$, as shown in Table $1 .{ }^{22}$ These heats of formation are recommended because they are well-established in literature and tested to be the most appropriate. However, the experimental value for the heat of formation of the boron atom remains controversial.

Yetter et $a l .{ }^{23}$ and Leroy et al. ${ }^{24}$ used values adopted by JANAF, while Ruscic et al. ${ }^{25}$ and Curvich et al. ${ }^{26}$ concluded that the JANAF value was too small. Curvich et al. recommended a value of $135 \pm 1.2 \mathrm{kcal} / \mathrm{mol}$, which is somewhat smaller than the values used by Storms and Mueller. ${ }^{30}$ Schlegel and Harris ${ }^{27}$ and Curtiss et al. ${ }^{28}$ used the values derived by Storms and Mueller. ${ }^{30}$ Martin and Taylor ${ }^{29}$ recently calculated the atomization energy of gaseous boron at $0 \mathrm{~K}$ as $136.02 \pm 0.4 \mathrm{kcal} / \mathrm{mol}$. A comparison with JANAF shows agreement between about half of the system theory and JANAF, while in the other half they differ significantly. Given the level of theory used in recent work and the agreement between the different theoretical methods, we concluded that the values derived by Storms and Mueller should be used. The adopted experimental heats of formation at $0 \mathrm{~K}$ for gaseous atoms and $\left[H^{0}(298 \mathrm{~K})-H^{0}(0 \mathrm{~K})\right]$ values for elements are presented in Table 1.

Table 1. Experimental heats of formation at $0 \mathrm{~K}$ for gaseous atoms and $\left[H^{0}(298 \mathrm{~K})-H^{0}(0 \mathrm{~K})\right]$ values for elements $\left(\mathrm{kcal} \cdot \mathrm{mol}^{-1}\right) \cdot{ }^{26,30}$

| Element | $\Delta_{f} H^{0}$ | $H^{0}(298 \mathrm{~K})-H^{0}(0 \mathrm{~K})$ |
| :--- | ---: | :---: |
| $\mathrm{B}$ | $136.2 \pm 0.2$ | 0.29 |
| $\mathrm{H}$ | $51.63 \pm 0.001$ | 1.01 |
| $\mathrm{~N}$ | $112.53 \pm 0.02$ | 1.04 |
| $\mathrm{O}$ | $58.99 \pm 0.02$ | 1.04 |
| $\mathrm{~F}$ | $18.47 \pm 0.07$ | 1.05 |
| $\mathrm{Cl}$ | $28.59 \pm 0.001$ | 1.10 |

## 3. Results and Discussion

The total energies for each atom $\left(\varepsilon_{0}\right)$ studied in all of the methods are collected in Table 2. Experimental values were obtained from the NIST Atomic Reference Data for Electronic Structure Calculations. The absolute deviation between the value for each atom with each method and the experimental data is $0.3-1.0$ in Hartree energy units. However, the deviations between different methods are much smaller and within 0.01 Hartree units. Although the deviations between the calculated and experimental values are not in excellent agreement, we consider the calculated values to be usable for practical applications. This is because the experimental values used four separate approximations in successive columns, while local-density approximation (LDA), which has only one single orbital eigenvalue, was adopted for total energy calculation. ${ }^{31}$ Moreover, the goodness of fit with different methods was high, and calculated systematic errors could be canceled by combining with the values for $\left[H_{\text {corr }}+\varepsilon_{0}\left(\mathrm{~A}_{x} \mathrm{~B}_{y} \mathrm{C}_{z}\right)\right]$.

In our research, molecular geometries were fully optimized for each computational method. From the calculated molecular geometries, we concluded that most binary compounds of boron are linear molecules and in the Cinfv point group. The $\mathrm{BX}_{3}$ molecules we calculated were $\mathrm{BH}_{3}, \mathrm{BF}_{3}$, and $\mathrm{BCl}_{3}$; these molecules have the

Table 2. Calculated total energies for each atom and experimental values; all data in the table is given in Hartree energy units.

| Methods | $\mathrm{B}$ | $\mathrm{H}$ | $\mathrm{N}$ | $\mathrm{O}$ | $\mathrm{F}$ | $\mathrm{Cl}$ |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: |
| G1 | -24.602780 | -0.500000 | -54.517736 | -74.982049 | -99.632747 | -459.676690 |
| G2 | -24.602036 | -0.5000000 | -54.517960 | -74.982030 | -99.632814 | -459.676627 |
| G3 | -24.642568 | -0.501003 | -54.564343 | -75.030991 | -99.684205 | -459.990959 |
| CBS-QB3 | -24.601769 | -0.499818 | -54.520537 | -74.987629 | -99.643075 | -459.683645 |
| CBS-4M | -24.606541 | -0.503351 | -54.524823 | -74.993562 | -99.651755 | -459.676936 |
| CBS-4O | -24.60633 | -0.503351 | -54.524485 | -74.992869 | -99.650682 | -459.675947 |
| CBS-Q | -24.601616 | -0.499818 | -54.520244 | -74.987059 | -99.642202 | -459.682860 |
| G2MP2 | -24.602703 | -0.500000 | -54.516306 | -74.978678 | -99.628941 | -459.666717 |
| G3MP2 | -24.607075 | -0.501839 | -54.525194 | -74.989774 | -99.640939 | -459.687242 |
| G3MP2B3 | -24.60822 | -0.502141 | -54.526943 | -74.992064 | -99.64377 | -459.690073 |
| G3B3 | -24.643219 | -0.501087 | -54.565162 | -75.032293 | -99.68599 | -459.992744 |
| Experimental ${ }^{31}$ | -24.344198 | -0.445671 | -54.025016 | -74.473077 | -99.099648 | -458.664179 |

$\mathrm{sp}^{2}$ boron and are in $D_{3 \mathrm{~h}}$ point group. The molecular geometries of $\mathrm{B}_{2} \mathrm{~F}_{4}$ and $\mathrm{B}_{2} \mathrm{Cl}_{4}$ are planar manifestations of the electron deficiency of boron atoms, ${ }^{32}$ both of them possess a perpendicular $D_{2 \mathrm{~d}}$ equilibrium geometry rather than planar $D_{2 \mathrm{~h}}$ ones. In addition, the point group symmetries of $\mathrm{B}_{2} \mathrm{O}_{2}, \mathrm{BOF}, \mathrm{B}_{2} \mathrm{H}_{6}$, and $\mathrm{BH}_{3} \mathrm{O}_{3}$ are $\mathrm{C}_{2 \mathrm{~V}}$, Cinfv, $D_{2 \mathrm{~h}}$, and $C_{3 \mathrm{~h}}$, respectively. Summing the total electronic and thermal enthalpies of each molecular value of $\left[\mathrm{H}_{\text {corr }}+\varepsilon_{0}\left(\mathrm{~A}_{x} \mathrm{~B}_{y} \mathrm{C}_{z}\right)\right]$ was another important task in our work, and the values can be calculated on the basis of the optimized molecular geometries. Thus, using Eq. 4, the resulting $\Delta_{f} H^{0} 298$ for each compound, calculated by all of the methods, were obtained and are listed in Table 3.

Several theoretically obtained heats of formation can be found in literature for borides containing light atoms, such as $\mathrm{BH}, \mathrm{BH}_{3}, \mathrm{BF}$, and $\mathrm{BF}_{3}$. Takinstov and Golovin ${ }^{8}$ calculated the heats of formation for $\mathrm{BH}_{3}$ and $\mathrm{BF}_{3}$; the same work had been done by Barreto et al., ${ }^{7}$ but they used HF and the G2 and G3 methods to obtain the heats of formation for these four molecules. When we compared their data and experimental data with our research, the deviations were as small as $1^{-10} \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$. In particular, for $\Delta_{f} H_{\mathrm{G} 2,298}(\mathrm{BH})=442.731 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$ and $\Delta_{f} H_{\mathrm{G} 2,298}\left(\mathrm{BF}_{3}\right)=-1135.749 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$, the errors when compared to experimental data were 0.031 and $0.251 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$, respectively. Thus, we consider the $a b$ initio theoretical calculations to be a valid systematic approach towards checking the gas phase heats of formation of borides containing light atoms.

As shown in Table 3, the heats of formation for chlorinated boron compounds also showed good accuracy; $\mathrm{BCl}_{3}$, which was described as difficult to obtain by Bauschlicher, was obtained in our study. The Gaussian-n methods provided great results, with errors of less than $1 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$. The results for $\mathrm{B}_{2} \mathrm{Cl}_{4}$ also agreed well with the experimental data; the G1, G2, G3, and CBS-QB3 methods were more suitable than the other approaches. In particular, $\Delta_{f} H_{\mathrm{CBS}-\mathrm{QB} 3,298}$ $\left(\mathrm{B}_{2} \mathrm{Cl}_{4}\right)=-490.446 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$ was the most precise prediction. Using the same calculations as for $\mathrm{B}_{2} \mathrm{Cl}_{4}$, the heat of formation for $\mathrm{B}_{2} \mathrm{~F}_{4}$ could also be obtained exactly from Gaussian-n methods and their modified methods CBS-QB3 and CBS-Q; the average deviation was about $10 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$. The error between the G1 results and experiment was $3 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$, which is somewhat smaller than for the other methods. One problem was that the results for $\mathrm{BF}_{3}$ and $\mathrm{BCl}_{3}$ were better than for $\mathrm{BF}$ and $\mathrm{BCl}$; it seems that processing systems containing more halogens is much easier. This can be explained in terms of the boron hybridization - boron does not have to hybridize to form the first bond but must $\mathrm{sp}^{2}$ hybridize to form the second bond and the structural stability of $\mathrm{BX}_{3}(\mathrm{X}=\mathrm{F}, \mathrm{Cl})$ is much better than $\mathrm{BX}(\mathrm{X}=$ $\mathrm{F}, \mathrm{Cl}$ ). Thus, further optimization and energy calculation should be correspondingly more accurate. Similar arguments do not apply to the analogous H system, as approximating solutions for the light atom system are easier to achieve.

The calculations for the other boron compounds are in reasonable agreement with the experimental values. $\Delta_{f} H_{\mathrm{CBS}-\mathrm{QB} 3,298}(\mathrm{BO})=22.365 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$ and $\Delta_{f} H_{\mathrm{G} 2 \mathrm{MP} 2,298(\mathrm{~B} 2 \mathrm{O} 2)}=-452.287 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$ are the best predictions for the

![](https://cdn.mathpix.com/cropped/2024_04_28_cf191030bd24fb9ea116g-07.jpg?height=1889&width=630&top_left_y=240&top_left_x=461)
oxidation of boron. The deviations are 2 and $3 \mathrm{~kJ} \cdot \mathrm{mol}^{-1} \cdot \Delta_{f} H_{\mathrm{G} 3,298}\left(\mathrm{BH}_{3} \mathrm{O}_{3}\right)=$ $-996.227 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$ also offered accurate estimates with errors of less than $2 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$. The deviation in the calculation for BOF was about $20 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$; however, taking into account the fact that the molecule contains oxygen and a halogen, the result is acceptable. Moreover, the calculation for boron nitride was not as accurate as for the other compounds, with an average standard deviation of $33 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$. Such deviations from the experimental value could be the results of several theoretical approximations (harmonic, incomplete basis sets, electron correlation, etc.) or could also come from experimental measurements. The experimental measurement for boron nitride was $114.00 \pm 29.9 \mathrm{kcal} \cdot \mathrm{mol}^{-1}$; since the uncertainty value is almost $30 \mathrm{kcal} \cdot \mathrm{mol}^{-1}$, the deviation is more likely related to the experimental measurements.

To show the reliability of predicted heats of formation values for boron compounds, the G1, CBS-QB3, and G2MP2 methods were chosen for comparisons with the experimental data. Based on the results, the linear correlation equations were defined respectively by $y=1.0005 x-2.1629, y=1.0055 x-4.9813$, and $y=1.0054 x-0.3527$. Correlation coefficients $R^{2}$ of $0.9992,0.9991$, and 0.9991 were obtained when heats of formation from the literature are plotted along the $x$ axis and heats of formation calculated using the present method along the $y$ axis (Figs. 1-3).

By comparing the results, we note that the mean absolute errors between the calculated data and experimental values from the 11 methods are 13.0, 13.9, 14.1, $14.9,23.5,20.5,13.9,14.6,18.4,19.1$, and $16.4 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$. Therefore, it seems that the values obtained with the Gaussian-n methods are the best among the 11 computational quantum chemical calculations; the various best estimations for each molecule we mentioned prove this. On the other hand, the CBS-4M and CBS-4O

![](https://cdn.mathpix.com/cropped/2024_04_28_cf191030bd24fb9ea116g-08.jpg?height=598&width=946&top_left_y=1465&top_left_x=291)

Fig. 1. Calculated values (G1 method) versus experimental data.

![](https://cdn.mathpix.com/cropped/2024_04_28_cf191030bd24fb9ea116g-09.jpg?height=556&width=907&top_left_y=216&top_left_x=311)

Fig. 2. Calculated values (CBS-QB3 method) versus experimental data.

![](https://cdn.mathpix.com/cropped/2024_04_28_cf191030bd24fb9ea116g-09.jpg?height=563&width=895&top_left_y=905&top_left_x=312)

Fig. 3. Calculated values (G2MP2 method) versus experimental data.

had larger mean absolute errors, and the CBS-4M method had the poorest estimation of $\mathrm{B}_{2} \mathrm{~F}_{4}$ with a deviation of up to $56 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$. Although the CBS-4M and CBS-4O methods are popular computational calculations and can provide accurate estimation for some molecules in some theoretical methods, ${ }^{35}$ it is obvious that the CBS-4 method is not suitable to calculating the heats of formation for boron compounds, especially boron halide, from atomization enthalpy analysis.

Moreover, by comparing the mean absolute error for each method, we noted that CBS-Q, G2MP2, and CBS-QB3 are next to the Gaussian-n methods. Each of G2MP2 and CBS-QB3 provide the best prediction for one of the molecules - $\mathrm{B}_{2} \mathrm{O}_{2}$ and BO, respectively - while the average absolute deviation of CBS-Q method was the smallest of the three methods. Recently, Chin et al. employed G2MP2 theory to investigate the energies of $\mathrm{BO}$ and $\mathrm{B}_{2} \mathrm{O}_{2}{ }^{36}$ Since these methods are suitable
for $\mathrm{BO}$ and $\mathrm{B}_{2} \mathrm{O}_{2}$, we recommend that G2MP2 and CBS-QB3 methods be used to produce the heat of formation values for other oxidations of boron.

The accuracy of each method also has a certain relation with the computing time. To give an extensive comparison, excluding CBS-4M and CBS-4O in calculating $\mathrm{BCl}_{3}$, in terms of time consumption, the various methods rank, in descending order, as G1, G3, G3B3, CBS-Q, CBS-QB3, G3MP2B3, G3MP2, G2MP2, and G2. We have previously noted that these methods rank almost the same in terms of accuracy. The G1 method provides the most accurate estimation and has the most computational cost as well. The computational cost of G3 theory is second only to G1 and the accuracy is almost as good. The modifications of Gaussian-n methods greatly reduce the time overhead through second-order Moller-Plesset perturbation theory or further geometry calculation, and the results are acceptable. In addition, we should mention that the G2 method provides the second greatest agreement between the calculated and experimental values with the least time consumption. On the basis of the above analysis, we believe that Gaussian-n methods are suitable for calculating heats of formation based on atomization enthalpy analysis, and G2 is the best choice to predict HOFs for borides in terms of accuracy and time efficiency.

## 4. Conclusions

With the help of computational techniques, we analyzed the molecular geometries of several boron compounds. A variety of theoretical available methods were applied to estimate the heats of formation at $298.15 \mathrm{~K}$ for $\mathrm{BH}, \mathrm{BH}_{3}, \mathrm{~B}_{2} \mathrm{H}_{6}, \mathrm{BF}, \mathrm{BF}_{3}, \mathrm{~B}_{2} \mathrm{~F}_{4}$, $\mathrm{BCl}, \mathrm{BCl}_{3}, \mathrm{~B}_{2} \mathrm{Cl}_{4}, \mathrm{BO}, \mathrm{B}_{2} \mathrm{O}_{2}, \mathrm{BN}$, BOF, and $\mathrm{BH}_{3} \mathrm{O}_{3}$ molecules. Good agreement was found between our calculations and the experimental values for both borohydride and chlorinated boron compounds. For several molecules we analyzed, the deviation was reasonable and within the experimental error bar. We also made comparisons with thermodynamic data taken from other literature and our values. In addition, we recommend some suitable theoretical methods for future work with borides.

## References

1. Stantos DMF, Sequeira CAC, J Electrochem Soc 156:F67, 2009.
2. Lee TM, Hak OJ, Anna DR, Zhennan B, J Amer Chem Soc 131:3733, 2009.
3. Karton A, Martin JML, J Phys Chem A 111:5936, 2007.
4. Barone V, Minichino C, Theor Chim Acta 76:53, 1989.
5. Rablen PR, Hartwig JF, J Am Chem Soc 118, 1996.
6. Bauschlicher CW, Ricca Jr A, J Phys Chem A 103:4313, 1999.
7. Barreto PRP, Vilela AFA, Gargano R, Int J Quant Chem 103:659, 2005.
8. Takhistov VV, Golovin AV, J Mol Struct 784:47, 2006.
9. Ricca A, Bauschlicher CW, J Phys Chem 102:876, 1998.
10. Pardoe JAJ, Norman NC, Timms PL, Polyhedron 21:543, 2002.
11. Curtiss LA, Raghavachari K, Pople JA, J Chem Phys 98:1293, 1993.
12. Curtiss LA, Redfern PC, Raghavachari K, Pople JA, Chem Phys Lett 359:390, 2002.
13. Li XH, Zhang RZ, Zhang XZ, Cheng XL, Yang XD, J Theor Comput Chem 6:675, 2007 .
14. Montgomery JA, Frisch MJ, Ochterski JW, Petersson GA, J Chem Phys 112:6532, 2000 .
15. Verevkin SP, Emel'yanenko VN, Toktonov AV, J Chem Thermodynamics 40:1428, 2008
16. Fabian WMF, Janoschek R, Combustion Flame 145:282, 2006.
17. Stein K, Stian S, Bjornar A, J Phys Chem A 113:1869, 2009.
18. Curtiss LA, Redfern PC, Raghavachari K, J Chem Phy 126:1, 2007.
19. Huh SB, Lee JS, J Chem Phys 118:3035, 2003.
20. Baboul AG, Curtis LA, Redfern PC, Raghavachari K, J Chem Phys 110:7650, 1999.
21. Frisch MJ, Trucks GW, Schlegel HB, Scuseria GE, Robb MA, Cheeseman JR, Montgomery Jr JA, Vreven T, Kudin KN, Burant JC, Millam JM, Iyengar SS, Tomasi J, Barone V, Mennucci B, Cossi M, Scalmani G, Rega N, Petersson GA, Nakatsuji H, Hada M, Ehara M, Toyota K, Fukuda R, Hasegawa J, Ishida M, Nakajima T, Honda Y, Kitao O, Nakai H, Klene M, Li X, Knox JE, Hratchian HP, Cross JB, Bakken V, Adamo C, Jaramillo J, Gomperts R, Stratmann RE, Yazyev O, Austin AJ, Cammi R, Pomelli C, Ochterski JW, Ayala PY, Morokuma K, Voth GA, Salvador P, Dannenberg JJ, Zakrzewski VG, Dapprich S, Daniels AD, Strain MC, Farkas O, Malick DK, Rabuck AD, Raghavachari K, Foresman JB, Ortiz JV, Cui Q, Baboul AG, Clifford S, Cioslowski J, Stefanov BB, Liu G, Liashenko A, Piskorz P, Komaromi I, Martin RL, Fox DJ, Keith T, Al-Laham MA, Peng CY, Nanayakkara A, Challacombe M, Gill PMW, Johnson B, Chen W, Wong MW, Gonzalez C, Pople JA, Gaussian 03, Revision C.02, Gaussian, Inc., Wallingford CT, 2004.
22. Curtiss LA, Raghavachari K, Paul CR, J Chem Phys 106:1063, 1997.
23. Yetter RA, Rabitz H, Dryler FL, Brown C, Kolb CE, Combust Flame 83:43, 1991.
24. Leroy C, Sana M, Wilante C, van Zieleghem MJ, J Mol Struct 247:199, 1991.
25. Ruscic B, Mayhew CA, Berkowitz J, J Chem Phys 88:5580, 1988.
26. Curvich LV, Veyts IV, Alcock CB, Thermodynamic Properties of Individual Substances, Vol. 3, CRC Press: Boca Raton, FL, 1994
27. Schlegel HB, Harris SJ, J Phys Chem 98:11178, 1994.
28. Curtiss LA, Raghavachari KL, Redfern PC, Pople JA, J Chem Phys 106:1063, 1997.
29. Martin JML, Taylor PR, J Phys Chem A 102:2995, 1998.
30. Storms E, Mueller B, J Phys Chem 81:318, 1977.
31. http://physics.nist.gov/PhysRefData/DFTdata/Tables/ptable.html (NIST. Atom Reference Data for Electronic Structure Calculations).
32. Jun-ichi A, Hideaki K, Toshimasa I, J Amer Chem Soc 127:13324, 2995.
33. Gurvich LV, Veyts IV, Alcock CB, Thermodynamic Properties of Individual Substances, 4th edn., Vol. 1, Hermisphere Publishing Corp., New York, 1989.
34. Gurvich LV, Veyts IV, Alcock CB, Thermodynamic Properties of Individual Substances, 4th edn., Vol. 3, CRC Press, Boca Raton, FL, 1994.
35. Li XH, Zhang RZ, Cheng XL, Yang XD, J Theor Comput Chem 6:449, 2007.
36. Chin CH, Mebel AM, Hwang DY, J Phys Chem A 108:473, 2004.

[^0]:    ${ }^{*}$ Corresponding author.

