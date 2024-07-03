# A systematic database of thin-film measurements by EPMA 

## Part I - Aluminum films

G. F. Bastin* and H. J. M. Heijligers<br>Laboratory of Solid State and Materials Chemistry, University of Technology, P.O. Box 513, NL-5600 MB Eindhoven, The<br>Netherlands


#### Abstract

A systematic database of thin-film measurements on aluminum films by electron probe microanalysis is presented. The measurements were performed between 3 and $30 \mathrm{kV}$ accelerating voltage on films of six different nominal thicknesses, ranging from 100 up to 3200 Å, which were deposited simultaneously on 20 different substrates, ranging between Be and Bi. The purpose of this work was to provide systematic data on which existing and future thin-film analysis programs can be tested. A total of $1060 \mathrm{k}$ ratios for the film element Al were collected and $872 \boldsymbol{k}$ ratios for the various substrate elements from underneath the films. Tests with our own most recent thin-film analysis program, TFA, based on the double Gaussian PROZA96 procedure, on this database showed excellent performance: a mean value of 1.0093 for $\boldsymbol{k}_{\text {calc }} / \boldsymbol{k}_{\text {meas }}$ and a relative root-mean-square deviation of $4.2457 \%$ in the histogram for the film element. Copyright $\odot 2000$ John Wiley \& Sons, Ltd.


## INTRODUCTION

The purpose of thin-film correction procedures in electron probe microanalysis (EPMA) is to convert the measured x-ray intensities from film (and/or substrate) elements into the correct thickness and composition of a film on a substrate. It will be obvious that this conversion can only be made correctly if it is exactly known where the x-rays are being produced as a function of depth in the specimen. This knowledge is commonly presented in terms of socalled $\phi(\rho z)$ curves, in which $\phi$ represents the number of x-ray photons produced and $\rho z$ the mass depth (product of density $\rho$ and linear depth $z$ ).

Although the correct analytical description of $\phi(\rho z)$ curves in pure bulk elements and compounds over a wide range in experimental conditions is difficult enough in itself, it appears that a number of modern $\phi(\rho z)$ models $^{1-7}$ are very successful in this respect. This can be judged from their impressive performance on the most difficult analytical cases, e.g. the bulk analysis of the ultra-light elements B, C, $\mathrm{N}$ and $\mathrm{O} .^{3-8}$

Nevertheless, a typical example of bulk analysis in specimens which are supposed to be homogeneous in depth must be considered as relatively simple compared with cases of thin-film analysis where the geometry is much more complex, and where sharp discontinuities exist at the interfaces between film(s) and substrate. The question arises, therefore, of how the $x$-ray generation as a function of mass depth should be described analytically for each of the elements in a film-substrate combination,[^0]

in the case that such discontinuities are present at each of the interfaces.

A number of approaches have been presented in the literature to deal with this problem. These are either based on (semi-)empirical approaches, ${ }^{9-15}$ in which the $\phi(\rho z)$ curves of each of the film elements are modified empirically according to the specific film-substrate combination at hand, or on more fundamental approaches using Monte Carlo procedures. ${ }^{16,17}$

In a number of previous papers ${ }^{18-20}$ on the subject, we have given a general outline of the approach we developed in our own analytical description of $\phi(\rho z)$ curves for the elements in a film-substrate combination, and the description of this procedure will briefly be repeated here.

The simplest case of a thin film-substrate combination that can be conceived is that of two neighbouring elements in the periodic system. Since the processes of electron scattering and deceleration and those of x-ray generation will be virtually the same in both elements, the $\phi(\rho z)$ curves for film and substrate elements will be almost identical. As a result, either of them could be used to calculate the generated and emitted intensities from film and substrate elements by partial integration between the appropriate limits. This simple approximation is known to work well as long as the difference in atomic number between film and substrate element does not exceed, say, 3-4 units. With increasing difference in atomic number the difference in electron scattering properties between film and substrate elements becomes noticeable and the x-ray production in the film can be influenced substantially. If the substrate element is heavier, then the $x$-ray production in the film will be increased, and vice versa. Therefore, a correction has to be applied in order to deal with such differences.

In our latest $\phi(\rho z)$ bulk correction program (PROZA96 ${ }^{6}$ ), which is based on a double Gaussian description of $\phi(\rho z)$ curves, ${ }^{7}$ we use, as the independent input parameters, the surface ionization $\phi(0)$, the position $\left(\rho z_{\mathrm{m}}\right)$ of the maximum in $\phi(\rho z)$, the exponent $(\alpha)$ in the right-hand descending Gaussian branch, and the value of the integral of $\phi(\rho z)$ (area under the $\phi(\rho z)$ curve, FI). The latter is calculated using the atomic number correction of Pouchou and Pichoir. ${ }^{21}$

Using these four independent shape parameters, the shape of the $\phi(\rho z)$ curve is completely determined; the value of the exponent in the left-hand ascending Gaussian branch $(\beta)$ is calculated as a dependent variable.

Turning back to the case of a thin film on a substrate, we start from the basic assumption that the four independent Gaussian shape parameters for the $\phi(\rho z)$ curves of each of the elements in the film vary between two extremes, which are typical of either extremely thin or extremely thick layers. In the latter case it will be clear that the bulk parameters of the film element in question will be approached. In the former case, on the other hand, the parameters can be approximated by treating the film element as if it were solved in the substrate. In all intermediate cases the parameters will have to be composed from the two extremes, using weighting procedures, in which the Gaussian parameters for each particular element in each of the layers and in the substrate are assigned specific weights, depending upon the distance from the layer examined.

Furthermore, it is assumed that the $\rho z$ scale in each particular $\phi(\rho z)$ curve is continuous across interfaces, and that for each element in the film-substrate system only one continuous $\phi(\rho z)$ curve needs to be calculated.

Finally, it is assumed that only the $\phi(\rho z)$ curves for the film elements are affected by the nature and the thickness of the other films and the substrate, whereas those for the substrate elements are not. Whereas the former assumption seems to be reasonable, experimental evidence will have to show whether the assumption for the substrate elements really holds. This is precisely one of the reasons why, in our opinion, systematic databases of thin-film measurements of the kind we supply here are extremely useful.

It is obvious that the procedure proposed here is based on a number of simplifying assumptions and it is only fair to say that these are not always corroborated by, e.g., Monte Carlo simulations. ${ }^{17}$ These simulations often show that the $\phi(\rho z)$ curves in the vicinity of an interface are not always smoothly varying Gaussians. In fact, they are often not smooth functions at all and they may show strong and rather unpredictable perturbations. It is very interesting, therefore, to find out how well our procedure performs in practice, in spite of the severe simplifications used inside.

The ideal thin-film correction procedure would be expected to calculate the correct emitted x-ray intensities for a given film thickness and composition, regardless of the nature of the substrate and the accelerating voltage used. It is questionable to what extent the existing procedures are indeed capable of such performance, because in our opinion there is a lack of systematic data on which the performance can be tested. An analysis of the available data in the literature ${ }^{9,12-16}$ shows that, in spite of the fairly large number of data, there are only a limited number of film-substrate combinations with extreme differences in atomic number. Besides, there appears to be a strong bias towards films deposited on Si substrates, for obvious reasons. We therefore decided to set up large and systematic databases which contain measurements on a wide variety of film thicknesses of several elements, deposited on a wide range of substrates, ranging from $\mathrm{Be}$ to $\mathrm{Bi}$, and measured over a wide range of accelerating voltages. In this paper, our results on aluminum films of six different thicknesses are reported.

## STRUCTURAL DETAILS OF OUR OWN THIN-FILM APPROACH

Our thin-film treatment is essentially based on our latest PROZA $^{6}$ bulk correction program (PROZA96), in which a double Gaussian procedure is being used for a realistic description of $\phi(\rho z)$ curves. As pointed out before, ${ }^{6}$ however, we use a modified version of the original Merlet ${ }^{7}$ procedure in the sense that we use the quantities $\phi(0)$ (surface ionization), $\rho z_{\mathrm{m}}$ [the position of the maximum in $\phi(\rho z)$ ], FI [the integral of $\phi(\rho z)$, or the area under the $\phi(\rho z)$ curve], and $\alpha$ (the exponent in the right-hand descending Gaussian) as the four necessary independent variables. The dependent variable $\beta$, which is used for the description of the left-hand ascending Gaussian, is calculated through an iterative mathematical procedure.

In the discussion on our thin-film approach that now follows, the superscript $i$ will be used to denote the particular element under consideration, and the subscripts $\mathrm{b}, \mathrm{f}$ and $\mathrm{s}$ will be used to indicate whether we are dealing with bulk, film, or substrate quantities.

The actual thin-film procedure starts with the calculation of the bulk standard intensities for all of the elements in the film-substrate combination. To this end, the $\alpha, \phi(0)$, $\rho z_{\mathrm{m}}$ and FI values for each element $i$ are being calculated according to the bulk PROZA96 program. In the same first step, the $\alpha$-values for element $i$ radiation in all other elements $j$ in film and substrate are also calculated. In the next step, the $\alpha$ values for the film elements are composed on the basis of the bulk compositions in film and substrate to yield the $\alpha_{\mathrm{b}, \mathrm{f}}^{i}$ and $\alpha_{\mathrm{b}, \mathrm{s}}^{i}$ quantities. Both of the latter quantities will be used later in a weighting procedure to establish the final $\alpha^{i}$ value typical of the complete film-substrate combination. In a similar way, composed values of $\phi(0), \rho z_{\mathrm{m}}$ and FI for the bulk compositions of film and substrate are calculated for element $i$ radiation.

The next and crucial step is to establish the depth of penetration $\boldsymbol{R}_{x}$ for each element $i$ radiation. Since there is no strict 'end' to a Gaussian curve, this presents something of a problem. In a previous publication, ${ }^{20}$ where the surface-centered Gaussian model ${ }^{1}$ was used, this was solved by taking $2.5 / \alpha_{\text {final }}^{i}$ for each specific element as a convenient measure, since this ratio was found to represent the depth at which the original surface-centered Gaussian had dropped to less than $0.2 \%$ of its fictitious starting value $\gamma$. In the double Gaussian model, $\alpha$ operates in the right-hand (descending) branch only; it lies at hand, therefore, to suppose that the position $\rho z_{\mathrm{m}}$, at which the maximum in $\phi(\rho z)$ occurs, has to be added to $2.5 / \alpha_{\text {final }}^{i}$ in order to find the 'end' of the $\phi(\rho z)$ curve. However, the final $\alpha^{i}$ value is not known a priori, because it has yet to be calculated from the $\alpha_{\mathrm{b}, \mathrm{f}}^{i}$ and $\alpha_{\mathrm{b}, \mathrm{s}}^{i}$ values, using
weighting laws that are supposed to weight the various contributions over the relevant mass depth region down to $\boldsymbol{R}_{x}$. Since $\boldsymbol{R}_{x}$ is not known either, it is necessary to start an iterative procedure to arrive at the final $\alpha$ value and, hence, $\boldsymbol{R}_{x}$. The first (crude) estimate for $\boldsymbol{R}_{x}$ is obtained by averaging the constituent $\left(\rho z_{\mathrm{m}}^{i}+2.5 / \alpha^{i}\right)$ values in the bulk of the film and the substrate, and this mean value can then be used to generate a first estimate for $\boldsymbol{R}_{x}$. Next, a more accurate weighting procedure is started, in which the weight ( $\boldsymbol{p}$ ) of each contribution as a function of mass depth $(\rho z)$ is described by a fourth-degree polynomial:

$$
\boldsymbol{p}(\rho z)=\boldsymbol{N}(\rho z-\boldsymbol{L})^{2}(\rho z-\boldsymbol{R})^{2}
$$

where $\boldsymbol{L}$ and $\boldsymbol{R}$, which are both functions of $\boldsymbol{R}_{x}$ only, are the double roots on the left- and right-hand sides of the polynomial, and $N$ is a normalization factor that ensures the normalization under the $\boldsymbol{p}(\rho z)$ curve. In fact, this weighting procedure is a variant to the one first used by Pouchou and Pichoir. ${ }^{9}$ However, these authors used the polynomial weighting procedure in order to generate sets of fictitious bulk compositions, one set for each $\phi(\rho z)$ parameter, from which all necessary $\phi(\rho z)$ parameters in their double-parabolic model for each particular element in the film-substrate combination were subsequently calculated. In our approach, on the other hand, the weighting is much more direct since we use the basic Gaussian parameters in a straightforward way.

In the iterative procedure for the determination of $\boldsymbol{R}_{x}$, the roots used are $-0.4 \boldsymbol{R}_{x}$ for $\boldsymbol{L}$ and $\boldsymbol{R}_{x}$ for $\boldsymbol{R}$. Using these roots, a new value for $\boldsymbol{R}_{x}$ is calculated by integration over the $\boldsymbol{p}$ function [Eqn (1)]. The resulting value is normalized by dividing it by the integral of $\boldsymbol{p}(\rho z)$ between 0 and $\boldsymbol{R}$. The newly obtained $\boldsymbol{R}_{x}$ value is now compared with the previous one, and if the relative deviation is smaller than, say, $0.1 \%$, the iteration procedure is stopped. If not, the latest $\boldsymbol{R}_{x}$ value is used to generate new $\boldsymbol{L}$ and $\boldsymbol{R}$ values, and the weighting procedure is repeated until convergence is obtained. This is usually the case in less than three cycles.

The last problem that has to be solved is to find the $\boldsymbol{L}$ and $\boldsymbol{R}$ values, which apply to the weighting procedures aimed at finding the four independent Gaussian parameters, necessary to describe the $\phi(\rho z)$ curves for each of the elements in the film-substrate combination. These roots will be different for each of the Gaussian parameters. Provisional settings were found originally by a process of optimization on the (often conflicting) thin-film data from the literature. Later, these settings were fine-tuned by using our own databases, of which the present one on aluminum films is an example. It must be emphasized, however, that this fine-tuning process is merely necessary to find the proper translation from the old to the new model, where different parameters with their different meanings are involved. It is not possible to 'optimize' a vast database of measurements with the relatively few parameters at hand, certainly not if the experimental conditions vary widely, as in the present case.

The double roots for the four Gaussian parameters can be summarized as in Table 1. It is clear from this table that more weight is assigned to the deeper regions in the specimen as far as $\alpha$ is concerned, whereas $\phi(0)$ is mainly governed by the near-surface regions. Regarding the latter parameter, it is assumed that electrons scattered back from regions deeper than $0.5 \boldsymbol{R}_{x}$ will not be able to make it
Table 1. Double roots for the Gaussian parameters

| Parameter | $\boldsymbol{L}$ | $\boldsymbol{R}$ |
| :--- | :---: | :---: |
| $\alpha$ | $-0.3 \boldsymbol{R}_{x}$ | $\boldsymbol{R}_{x}$ |
| $\rho \boldsymbol{Z}_{\mathrm{m}}$ | $-0.9 \boldsymbol{R}_{x}$ | $0.7 \boldsymbol{R}_{X}$ |
| $\mathrm{FI}$ | $-0.8 \boldsymbol{R}_{x}$ | $\boldsymbol{R}_{x}$ |
| $\phi(0)$ | $-0.5 \boldsymbol{R}_{x}$ | $0.5 \boldsymbol{R}_{x}$ |

back to the surface and, consequently, cannot contribute to $\phi(0)$.

Once the Gaussian parameters for each of the elements in the film have been obtained, the emitted intensities can be calculated by partial integration; 6 those for the film elements between the $\rho z$ limits of zero and $T$ (the film thickness) and for the substrate elements from $T$ down to infinity. Appropriate corrections for absorption have, of course, to be made. Taking the ratios to the intensities emitted from the bulk standards will finally give the calculated $k$ ratios which have to be compared with the measured values. This is, in short, the procedure followed in the present work. Normally, one would try to operate such a thin-film program the other way around, i.e. try to determine the thickness and/or composition of a film from measured $k$ ratios. Full details of this procedure can be found in one of our previous publications. ${ }^{20}$

## EXPERIMENTAL

Aluminum films of six different nominal thicknesses (10, $20,40,80,160$ and $320 \mathrm{~nm}$ ) were deposited by vacuum evaporation on to polished pieces of 20 different substrate elements, ranging from $\mathrm{Be}$ to $\mathrm{Bi}$, mounted in a single specimen mount. In order to avoid problems with simultaneously polishing materials with largely different hardnesses, small pieces of all substrate elements were mounted separately first in copper-filled mounting resin and polished carefully. Next, small rectangular blocks of mounting resin, each containing a polished substrate specimen, were cut out and remounted together to produce the final assembly of 20 polished substrate elements. In total, six such substrate assemblies were manufactured in order to accommodate six different film thicknesses.

During each vacuum deposition run, identical films were also deposited on crystals of rock salt and Si wafers. The former specimens were to be used for independent determination of the film thicknesses by Rutherford backscattering spectroscopy (RBS), whereas the latter served incidentally for transmission electron microscopy (TEM) investigations of cross-sections.

The films deposited on rock salt could be lifted off easily by dissolving the salt in water. These specimens, when picked up on a TEM grid, were eminently suited to perform intensity measurements on unsupported films. In combination with the measurements on the same films on a variety of substrates, this provided the experimental possibility of accessing the surface ionization value $\phi(0)$ by a process of extrapolation towards a film thickness of zero. This will be the subject of a future paper.

The microprobe measurements on the film (Al) and the substrate elements were carried out at accelerating
voltages between 3 and $30 \mathrm{kV}$, using JEOL 733 and 8600 electron probe microanalyzers. Both instruments have $x-$ ray take-off angles of $40^{\circ}$.

## RESULTS

Establishing the real thicknesses of the films turned out to be a major problem; therefore, our primary efforts were concerned with this task. To begin with, there were only two really independent sources of information: RBS (carried out at Philips Research Laboratories, Eindhoven, The Netherlands) and Monte Carlo calculations. ${ }^{17}$ In the latter approach the mass thicknesses are determined by iterative procedures, in which the results of the simulations are compared with the experimental measurements. The results obtained by the two techniques differed markedly, as can be judged from Table 2.

Assuming a bulk density of $2.70 \mathrm{~g} \mathrm{~cm}^{-3}$ for aluminum, the mass thicknesses aimed at would be 2.70, 5.40, 10.80, 21.60, 43.20, and $86.40 \mu \mathrm{g} \mathrm{cm}^{-2}$. It is clear that, e.g., RBS finds much larger thicknesses for the three thinner films, whereas for the thicker films increasingly lower film thicknesses are found. With the Monte Carlo method, very much larger thicknesses are found than either the nominal or the RBS values over the full range.

The following remarks can be made concerning Table 2, where the paragraph letters below correspond to the footnote letters in the table.

(a) The Monte Carlo program, using the measured $k$ ratios for $\mathrm{Al} \mathrm{K} \alpha$, was found to produce a consistent variation of $20 \%$ in the mass thicknesses between 3 and $30 \mathrm{kV}$, starting low and ending high, for both substrates. However, the results for a specific fixed voltage were virtually independent of the atomic number of the substrate, which must be considered as a remarkably good achievement. The mean results over the voltage range have been reported here.

(b) The GMR film program is the computer program written by Waldo. ${ }^{13,22}$ We used the option in this program which is entirely based on the PAP $^{9}$ (doubleparabolic) procedure. This program was found to produce up to $14 \%$ variation in mass thicknesses on going from a $\mathrm{Be}$ to a $\mathrm{Bi}$ substrate for a fixed accelerating voltage. On the other hand, the dependence on accelerating voltage was much better. The results calculated for a Ti substrate, representing only moderate differences in atomic number between film and substrate elements, are presented here.

| Nominal | RBS | Monte Carloa |  | $\mathrm{GMR}^{b}$ <br> film on $\mathrm{Ti}$ | TFA A $^{c}$ <br> program on $\mathrm{Ti}$ | Database $^{d}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  | On Be | On Bi |  |  |  |
| 2.70 | 3.27 | 3.57 | 3.47 | 3.58 | 3.62 | 3.55 |
| 5.40 | 6.14 | 7.20 | 6.96 | 6.95 | 7.06 | 7.04 |
| 10.80 | 11.96 | 14.26 | 13.66 | 13.69 | 13.95 | 13.80 |
| 21.60 | 21.86 | 24.99 | 24.92 | 25.04 | 25.56 | 24.90 |
| 43.20 | 39.46 | 48.84 | 49.23 | 48.54 | 49.84 | 49.20 |
| 86.40 | 81.97 | 88.90 | 88.07 | 84.66 | 87.11 | 85.40 |

${ }^{a-d}$ See the corresponding paragraphs (a)-(d) in the text. (c) The TFA program, based on our own modification ${ }^{2}$ of the surface-centered Gaussian Packwood/Brown approach, ${ }^{1}$ is a predecessor to our present thin-film analysis program. Its results varied by less than $5 \%$ between a $\mathrm{Be}$ and a $\mathrm{Bi}$ substrate and the results as a function of voltage were satisfactory. As was the case with the GMR program, the results calculated for a $\mathrm{Ti}$ substrate are presented here. It is clear that the results from the GMR and TFA programs do not show pronounced differences. In addition, they both show fair agreement with the mean results of the Monte Carlo program, contrary to the RBS results in many cases.

(d) The last column in Table 2 represents the mass thicknesses which were finally adopted in our database. The values are very close to the mean numbers in the other columns.

It is remarkable that, with none of the techniques used, the expected ratio in the mass thicknesses of $1: 2: 4: 8: 16: 32$, which was aimed at during the preparation of the films and which was supposed to be easy to achieve, was in fact attained. With RBS the ratios obtained were 1:1.88:3.66:6.69:12.07:25.07 and with Monte Carlo (mean) 1:2.01:3.97:7.09:13.94:25.14. With the EPMA programs GMR film and TFA sequences of $1: 1.94: 3.82: 6.99: 13.56: 23.65$ and $1: 1.95: 3.85: 7.06$ : 13.77: 24.06 were calculated, respectively.

In an isolated case (nominal $800 \AA$, or $21.60 \mu \mathrm{g} \mathrm{cm}^{-2}$ ), a film on $\mathrm{NaCl}$ was investigated in a cross-section in the transmission electron microscope (JEOL 2000 FX). Thicknesses corresponding to $25 \mu \mathrm{g} \mathrm{cm}{ }^{-2}$ (assuming the bulk density for Al) and slightly higher were thereby found, thus corroborating the Monte Carlo and EPMA (GMR and TFA) results, rather than the RBS data. Apparently, it is extremely difficult to find the 'true' film thicknesses. However, we want to emphasize most strongly that, even if the true film thicknesses will presumably never be known with $100 \%$ certainty, the measurements on such (our present) specimens are still extremely useful because it can safely be assumed that the same mass thickness applies to each of the various substrates.

The EPMA measurements for $\mathrm{Al} \mathrm{K} \alpha$ were carried out as a function of atomic number of the substrate, starting with Be and ending with Bi for each specific accelerating voltage. After calibration of the $\mathrm{Al} \mathrm{K} \alpha$ peak with a TAP analyzer crystal on the Al bulk standard, a minimum of 10 intensity measurements were performed in each case and the mean $k$ ratio was used as the entry in the final database. This measuring procedure has the specific advantage of disclosing immediately any erratic behavior in the variation of the intensity of the $\mathrm{Al} \mathrm{K} \alpha$ peak with atomic number of the substrate, a variation which must be assumed to be smooth. Moreover, one would expect the signal to increase monotonically with the atomic number of the substrate. Any sudden increase in the signal might point to a case of fluorescence, e.g. if the $\mathrm{Al}$ film is on a Si substrate.

Figure 1 shows some of the results which can typically be obtained in the measurements as a function of atomic number of the substrate at an accelerating voltage of $15 \mathrm{kV}$ for the films with nominal thicknesses of 100 (top) and $400 \AA$ (

Figure 2 shows similar results, but now for the film with a nominal thickness of $800 \AA$, at accelerating voltages of 20 (top) and $25 \mathrm{kV}$ (bottom).



Variation $\mathrm{k}$-ratio $\mathrm{Al}-\mathrm{K}_{\alpha}$ as a $\mathrm{f}(\mathrm{Z})$ at $15 \mathrm{kV}$

Nom. $100 \AA$ Al film, $\mathrm{MT}=3.55 \mu \mathrm{g} / \mathrm{cm}^{2}$



Variation k-ratio $\mathrm{Al}-\mathrm{K}_{\alpha}$ as a $\mathrm{f}(\mathrm{Z})$ at $15 \mathrm{kV}$ Nom. $400 \AA$ Al film , MT=13.80 $\mu \mathrm{g} / \mathrm{cm}^{2}$



Figure 1. Variation of the $k$ ratios for $\mathrm{Al} \mathrm{K} \alpha$ as a function of the atomic number of the substrate at $15 \mathrm{kV}$. Top, nominal thickness $100 \AA$, assumed mass thickness $3.55 \mu \mathrm{g} \mathrm{cm}^{-2}$; bottom, nominal thickness $400 \AA$, assumed mass thickness $13.80 \mu \mathrm{g} \mathrm{cm}^{-2}$. Solid circles represent the measurements and the broken curves show the predictions of the TFA program. X-ray take-off angle, $40^{\circ}$.

It is evident from these results that remarkable agreement exists between the measurements and the calculations and that, in general, measurements with a smooth variation can indeed be obtained. The only case where noticeable and persistent deviations exist is where a silicon substrate $(Z=14)$ is involved, and this must be attributed to fluorescence.

Since the $\mathrm{Al} \mathrm{K} \alpha$ intensities emitted from the films are a function not only of the atomic number of the substrate, but also of that of the applied accelerating voltage, it is meaningful to present the results also as a function of the accelerating voltage for the six films for a fixed substrate. This is done in Fig. 3 for the beryllium (top) and titanium (bottom) substrates and in Fig. 4 for the molybdenum (top) and tungsten (bottom) substrates. Again, the agreement between measurements and calculations is remarkably good.

In view of the huge number of measured data collected in the present investigation ( $1060 k$ ratios for $\mathrm{Al} \mathrm{K} \alpha$ from the film element and $872 k$ ratios from the substrate elements), it is impossible to judge the overall performance of the present TFA program (or any other thin-film program, for that matter) by mere inspection of a relatively small number of graphical representations of the measured and calculated results. We chose, therefore, an approach
Variation k-ratio $\mathrm{Al}-\mathrm{K}_{\alpha}$ as a $\mathrm{f}(\mathrm{Z})$ at $20 \mathrm{kV}$

Nom. $800 \AA$ Al film, MT=24.90 $\mu \mathrm{g} / \mathrm{cm}$



Variation k-ratio $\mathrm{Al}-\mathrm{K}_{\alpha}$ as a $\mathrm{f}(\mathrm{Z})$ at $25 \mathrm{kV}$

Nom. $800 \AA$ Al film , MT= $=24.90 \mu \mathrm{g} / \mathrm{cm}^{2}$



Figure 2. Variation of the $k$ ratios for $\mathrm{Al} \mathrm{K} \alpha$ as a function of the atomic number of the substrate for an aluminum film of nominal thickness $800 \AA$, assumed mass thickness $24.90 \mu \mathrm{g} \mathrm{cm}^{-2}$. Top, at $20 \mathrm{kV}$; bottom, at $25 \mathrm{kV}$. Solid circles represent the measurements and the broken curves show the predictions of the TFA program. X-ray take-off angle, $40^{\circ}$.

which is commonly used in tests on the performance of bulk correction programs. In this approach the $k$ ratio $\left(k^{\prime}\right)$ for the given entry in the database under the specific experimental conditions is calculated and compared with the measured value $(k)$. The ratio $k^{\prime} / k$ is then displayed in a histogram, showing the number of analyses vs the value of $k^{\prime} / k$, and the narrowness of the histogram (in terms of the relative root-mean-square value in \%), together with the mean value of the distribution are then used as a final measure of success. Figure 5 shows the results which were obtained in the present case. The results must be regarded as excellent, certainly if one takes into consideration that in a number of cases (which have still been included in the final database) the experimental conditions for thin-film analysis are not suitable at all. Examples of these cases are when the accelerating voltage for a given film thickness is simply too low, so that the $\phi(\rho z)$ curve for the film element barely touches on the substrate. It is evident that the results could become very much better if such cases were eliminated from the database.

As mentioned before, a wide variety of substrate elements was also measured from underneath the films. All possible x-ray lines that could be excited were measured

Variation k-ratio $\mathrm{Al}-\mathrm{K}_{\alpha}$ as a $\mathrm{f}\left(\mathrm{E}_{0}\right)$ on Be substrate for 6 different film thicknesses ( $100-3200 \AA$ )



Variation k-ratio $\mathrm{Al}-\mathrm{K}_{\alpha}$ as a $\mathrm{f}\left(\mathrm{E}_{\alpha}\right)$ on Ti substrate for 6 different film thicknesses ( $100-3200 \AA$ )



Figure 3. Variation of the $k$ ratios for $\mathrm{Al} \mathrm{K} \alpha$ as a function of accelerating voltage for the six aluminum films of nominal thicknesses ranging between 100 and $3200 \AA$ A. Top, for a beryllium substrate; bottom, for a titanium substrate. Symbols represent the measurements and the broken curves show the predictions of the TFA program. X-ray take-off angle, $40^{\circ}$.

and the $k$ ratios were also included in one large data file. Figure 6 shows the results obtained for the silicon (top) and titanium (bottom) substrates, and Fig. 7 gives similar results for the much heavier germanium (top) and molybdenum (bottom) substrates. Again, it appears evident that satisfactory agreement is obtained between calculations and measurements, with very few exceptions. The latter are connected again with those cases where the conditions for thin-film analysis are unsuitable: when the accelerating voltage for the film thickness at hand is low and the $\phi(\rho z)$ curve hardly extends into the substrate. The results of the overall statistical analysis for the substrate elements, similar to the one performed before for the film element, are shown in Fig. 8. After the elimination of the results obtained under totally unsuitable experimental conditions, most satisfactory mean $k^{\prime} / k(1.0125)$ and r.m.s. values $(3.6670 \%)$ are obtained. Full details of the complete database can be found in the Appendix and/or are available from the authors.
Variation k-ratio Al- $\mathrm{K}_{\alpha}$ as a $\mathrm{f}\left(\mathrm{E}_{\mathrm{o}}\right)$ on Mo substrate for 6 different film thicknesses ( $100-3200 \AA$ )



Variation k-ratio $A 1-K_{\alpha}$ as a $f\left(E_{o}\right)$ on $W$ substrate for 6 different film thicknesses ( $100-3200 \AA$ )



Figure 4. Variation of the $k$ ratios for $\mathrm{Al} \mathrm{K} \alpha$ as a function of accelerating voltage for the six aluminum films of nominal thicknesses ranging between 100 and $3200 \AA$. Top, for a molybdenum substrate; bottom, for a tungsten substrate. Symbols represent the measurements and the broken curves show the predictions of the TFA program. X-ray take-off angle, $40^{\circ}$.

TFA 1060 Aluminium Thin-Film analyses Mean $\mathrm{k}^{\prime} / \mathrm{k}=1.0093$, R.M.S. $=4.2457 \%$



Figure 5. Histogram obtained with the TFA thin-film program on $1060 \mathrm{Al} \mathrm{K} \alpha$ analyses, measured between 3 and $30 \mathrm{kV}$, from aluminum films of six different mass thicknesses. The number of analyses is displayed vs the ratio $k^{\prime} / k$ between the calculated $\left(k^{\prime}\right)$ and the measured $k$ ratio $(k)$.



Variation k-ratio $\mathrm{Si}-\mathrm{K}_{\alpha}$ from substrate as a $\mathrm{f}(\mathrm{E})$ under 6 different Al film thicknesses ( $100-3200 \AA$ )



Variation k-ratio Ti- $\mathrm{K}_{\alpha}$ from substrate as a $\mathrm{f}\left(\mathrm{E}_{\mathrm{o}}\right)$ under 6 different $\mathrm{Al}$ film thicknesses $(100-3200 \AA$ )



Figure 6. Variation of the $k$ ratios for the substrate elements as a function of accelerating voltage from underneath the six aluminum films of nominal thicknesses ranging between 100 and $3200 \AA$. Top, silicon substrate; bottom, titanium substrate. Symbols represent the measurements and the broken curves show the predictions of the TFA program. X-ray take-off angle, $40^{\circ}$.

## DISCUSSION

The results presented in this paper clearly show that accurate analysis of thin films over a wide range of experimental conditions is possible, especially if the accelerating voltage used in the measurements is suitable for the specific film thickness at hand. In all cases it is advisable to apply a sufficiently high voltage so that the $\phi(\rho z)$ curve of the film element extends relatively deep into the substrate. In other words, the mass thickness of the film should represent only a minor fraction of the total range of $\phi(\rho z)$.

As Figs 1 and 2 indicate, the calculations of the intensities emitted from a film with given mass thickness for a wide variety of substrates closely follow the measurements. This means that if the TFA program were to be used the other way around, virtually constant thicknesses would be found, irrespective of the atomic number of the substrate. This is, of course, one of the two major goals mentioned in the Introduction.
Variation $k$-ratio Ge- $\mathrm{L}_{\alpha}$ from substrate as a $f\left(E_{o}\right)$ under 6 different $\mathrm{Al}$ film thicknesses $(100-3200 \AA)$



Variation k-ratio Mo- $\mathrm{L}_{\alpha}$ from substrate as a $\mathrm{f}\left(\mathrm{E}_{\mathrm{o}}\right)$ under 6 different Al film thicknesses ( $100-3200 \AA$ )



Figure 7. Variation of the $k$ ratios for the substrate elements as a function of accelerating voltage from underneath the six aluminum films of nominal thicknesses ranging between 100 and $3200 \AA \AA$. Top, germanium substrate; bottom, molybdenum substrate. Symbols represent the measurements and the broken curves show the predictions of the TFA program. X-ray take-off angle, $40^{\circ}$.

The other major goal was that the calculations would closely follow the measurements as a function of accelerating voltage for a given film thickness on a specific substrate. The success of these calculations can be judged from Figs 3 and 4 for a small selection of substrates, ranging from $\mathrm{Be}$ to $\mathrm{Bi}$. The only noticeable deviations can be found in cases where the conditions are not suitable: low accelerating voltage, heavy substrate, e.g. W, and thick film (Fig. 4, bottom). If such results were to be excluded from the histogram in Fig. 5, then, of course, very much improved results could be obtained.

The fact that the mean $k^{\prime} / k$ value comes out closely around 1.0 means, of course, nothing else than that the $k$ ratios that we calculate agree closely with those expected from the mass thicknesses adopted in Table 2. If one were to insist on adopting the RBS values, then systematic shifts in the centering of the histogram would be observed. What we consider of much more importance, however, is the narrowness in the histogram, which reflects the ability of the program to yield a remarkably consistent

TFA 872 Substrate analyses under Aluminium Mean $\mathrm{k}^{\prime} / \mathrm{k}=1.0125$, R.M.S. $=3.6670 \%$ ( 829 analyses)



Figure 8. Histogram obtained with the TFA thin-film program on 872 substrate element analyses, measured between 3 and $30 \mathrm{kV}$, from underneath the aluminum films of six different mass thicknesses. The number of analyses is displayed vs the ratio between the calculated $\left(k^{\prime}\right)$ and the measured $k$ ratio $(k)$. The reported mean $k^{\prime} / k$ and r.m.s. values apply to only 829 analyses because the statistical flyers have been accumulated in the two bars at $k^{\prime} / k=0.75$ ( 7 analyses with $k^{\prime} / k<0.80$ ) and $k^{\prime} / k=1.25$ (36 analyses with $k^{\prime} / k>1.20$ ), and have been excluded from the final evaluation. mass thickness over a wide range of atomic numbers of the substrates and a large range in accelerating voltage. Any statement about a systematic error requires an exact knowledge about the true 'reference' value, which will presumably never be known.

As far as the substrate elements are concerned, similar remarks apply as in the case of the film element: low accelerating voltages for relatively thick films should be avoided, although, surprisingly, there are also problems sometimes with the thinnest films, for no good reason (Figs 6 and 7). Obviously, it can be difficult enough to measure $k$ ratios which differ only very slightly from unity. This observation, in conjunction with the fact that the slightest deviation in the substrate $k$ ratio can produce a large deviation in the mass thickness of the film if the program is run the other way around, can make it somewhat tricky to use the measured $k$ ratio of the substrate element exclusively in order to find the mass thickness of the film. In all cases much more weight should be assigned to the signals emitted by the film elements; after all, the emitted film signals are more or less directly proportional to the film thickness.

## REFERENCES

1. Packwood RH, Brown JD. X-Ray Spectrom. 1981; 10: 138.
2. Bastin GF, van Loo FJJ, Heijligers HJM. X-Ray Spectrom. 1984; 13: 91.
3. Bastin GF, Heijligers HJM. In Electron Probe Quantitation, Workshop at the National Bureau of Standards, Gaithersburg, Maryland, 1988, Heinrich KFJ, Newbury DE (eds). Plenum Press: New York, 1991; 145-161.
4. Pouchou JL, Pichoir F. Rech. Aérospat. 1984; 3: 13.
5. Pouchou JL, Pichoir F, Boivin D. (a) Proceedings of 12th ICXOM, 28 Aug-1 Sep 1989, Cracow, Poland. Jasienska S, Maksymowicz LJ (eds). Cracow Academy of Mining and Metallurgy, 1990; 52; (b) Further Improvements in Quantitation Procedures for X-ray Microanalysis, ONERA Report TP 157, 1989.
6. Bastin GF, Dijkstra JM, Heijligers HJM. X-Ray Spectrom. 1998; 27: 3.
7. Merlet C. Inst. Phys. Conf. Ser. 1992; No. 130; 123.
8. Bastin GF, Heijligers HJM. Scanning 1990; 12: 225.
9. Pouchou JL, Pichoir F. Rech. Aérospat. 1984; 5: 349.
10. Packwood RH, Milliken KS. A general equation for predicting $x$-ray intensitites from stratified samples in the electron microprobe, CANMET Report No. PMRL/85-25 (TR), May 1985.
11. August H-J, Wernisch J. Scanning 1987; 9: 145
12. Hunger H-J. Scanning 1988; 10: 65.
13. Waldo RA. In Microbeam Analysis, Newbury DE (ed). San Francisco Press: San Francisco, 1988; 310-314.
14. Willich P, Obertop D. Surf. Interface Anal. 1988; 13: 20.
15. Willich P, Obertop D. J. Phys. Colloque 1989; C-5: 285.
16. Kyser DF, Murata K. In Proceedings of a Workshop on the Use of Monte Carlo Calculations in Electron Probe Microanalysis and Scanning Electron Microscopy. Heinrich KFJ, Newbury DE, Yakowitz H (eds). NBS Special Publication No. 460. National Bureau of Standards: Washington, DC, 1976; 129-138.
17. Ammann N. Thesis MS, R. W. T. H. Aachen, 1989.
18. Bastin GF, Heijligers HJM, Dijkstra JM. In Proceedings of the XIIth International Congress for Electron Microscopy, Seattle (Washington, USA), August 1990, Peachey LD, Williams DB (eds). San Francisco Press: San Francisco, 1990; 216.
19. Bastin GF, Dijkstra JM, Heijligers HJM. In Proceedings of the 50th Annual Meeting of the Electron Microscopy Society of America/27th Annual Meeting of the Microbeam Analysis Society/19th Annual Meeting of the Microscopical Society of Canada, Baily GW, Bentley J, Small JA (eds). San Francisco Press: San Francisco, 1992; 1648.
20. Bastin GF, Dijkstra JM, Heijligers HJM, Klepper D. Microbeam Anal. 1993; 2: 29-43.
21. Pouchou JL, Pichoir F. In Proceedings of the 11th International Congress on X-Ray Optics and Microanalysis, Brown JD, Packwood RH (eds). Graphic Services, UWO: London, Canada, 1986; 249.
22. Waldo RA. In Microbeam Analysis, Howitt DE (ed). San Francisco Press: San Francisco, 1991; 45-53.

## APPENDIX

Data file for aluminum films (take-off angle $40^{\circ}$ ). Substrate line: $K=0, L=1, M=2$

| No. | $Z_{\text {substrate }}$ | Mass thickness <br> $\left(\mu \mathrm{cm} \mathrm{cm}^{-2}\right)$ | $k(\mathrm{Al} \mathrm{K} \alpha)$ | $k$ (substrate) | Accelerating <br> voltage (kV) | Substrate line |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 4 | 3.55 | 0.18981 | - | 3 | 0 |
| 2 | 4 | 3.55 | 0.09317 | - | 4 | 0 |
| 3 | 4 | 3.55 | 0.03595 | - | 6 | 0 |
| 4 | 4 | 3.55 | 0.01986 | - | 8 | 0 |
| 5 | 4 | 3.55 | 0.01277 | - | 10 | 0 |
| 6 | 4 | 3.55 | 0.00872 | - | 12 | 0 |
| 7 | 4 | 3.55 | 0.00566 | - | 15 | 0 |


| No. | $Z_{\text {substrate }}$ | Mass thickness <br> $\left(\mu \mathrm{g} \mathrm{cm}^{-2}\right)$ | $k(\mathrm{~A} \mid \mathrm{K} \alpha)$ | $k$ (substrate) | Accelerating <br> voltage (kV) | Substrate line |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 8 | 4 | 3.55 | 0.00346 | - | 20 | 0 |
| 9 | 4 | 3.55 | 0.00249 | - | 25 | 0 |
| 10 | 4 | 3.55 | 0.00193 | - | 30 | 0 |
| 11 | 4 | 7.04 | 0.19872 | - | 4 | 0 |
| 12 | 4 | 7.04 | 0.07860 | - | 6 | 0 |
| 13 | 4 | 7.04 | 0.04064 | - | 8 | 0 |
| 14 | 4 | 7.04 | 0.02520 | - | 10 | 0 |
| 15 | 4 | 7.04 | 0.01700 | - | 12 | 0 |
| 16 | 4 | 7.04 | 0.01122 | - | 15 | 0 |
| 17 | 4 | 7.04 | 0.00698 | - | 20 | 0 |
| 18 | 4 | 7.04 | 0.00498 | - | 25 | 0 |
| 19 | 4 | 7.04 | 0.00391 | - | 30 | 0 |
| 20 | 4 | 13.80 | 0.43663 | - | 4 | 0 |
| 21 | 4 | 13.80 | 0.16644 | - | 6 | 0 |
| 22 | 4 | 13.80 | 0.08548 | - | 8 | 0 |
| 23 | 4 | 13.80 | 0.05330 | - | 10 | 0 |
| 24 | 4 | 13.80 | 0.03606 | - | 12 | 0 |
| 25 | 4 | 13.80 | 0.02294 | - | 15 | 0 |
| 26 | 4 | 13.80 | 0.01368 | - | 20 | 0 |
| 27 | 4 | 13.80 | 0.00968 | - | 25 | 0 |
| 28 | 4 | 13.80 | 0.00790 | - | 30 | 0 |
| 29 | 4 | 24.90 | 0.75558 | - | 4 | 0 |
| 30 | 4 | 24.90 | 0.33607 | - | 6 | 0 |
| 31 | 4 | 24.90 | 0.17336 | - | 8 | 0 |
| 32 | 4 | 24.90 | 0.10194 | - | 10 | 0 |
| 33 | 4 | 24.90 | 0.06770 | - | 12 | 0 |
| 34 | 4 | 24.90 | 0.04288 | - | 15 | 0 |
| 35 | 4 | 24.90 | 0.02558 | - | 20 | 0 |
| 36 | 4 | 24.90 | 0.01760 | - | 25 | 0 |
| 37 | 4 | 24.90 | 0.01444 | - | 30 | 0 |
| 38 | 4 | 49.20 | 0.69750 | - | 6 | 0 |
| 39 | 4 | 49.20 | 0.38894 | - | 8 | 0 |
| 40 | 4 | 49.20 | 0.23268 | - | 10 | 0 |
| 41 | 4 | 49.20 | 0.15008 | - | 12 | 0 |
| 42 | 4 | 49.20 | 0.09314 | - | 15 | 0 |
| 43 | 4 | 49.20 | 0.05302 | - | 20 | 0 |
| 44 | 4 | 49.20 | 0.03653 | - | 25 | 0 |
| 45 | 4 | 49.20 | 0.02921 | - | 30 | 0 |
| 46 | 4 | 85.40 | 0.96110 | - | 6 | 0 |
| 47 | 4 | 85.40 | 0.68538 | - | 8 | 0 |
| 48 | 4 | 85.40 | 0.46017 | - | 10 | 0 |
| 49 | 4 | 85.40 | 0.30884 | - | 12 | 0 |
| 50 | 4 | 85.40 | 0.18818 | - | 15 | 0 |
| 51 | 4 | 85.40 | 0.10182 | - | 20 | 0 |
| 52 | 4 | 85.40 | 0.06966 | - | 25 | 0 |
| 53 | 4 | 85.40 | 0.05064 | - | 30 | 0 |
| 54 | 5 | 3.55 | 0.19267 | - | 3 | 0 |
| 55 | 5 | 3.55 | 0.09380 | - | 4 | 0 |
| 56 | 5 | 3.55 | 0.03647 | - | 6 | 0 |
| 57 | 5 | 3.55 | 0.02014 | - | 8 | 0 |
| 58 | 5 | 3.55 | 0.01318 | - | 10 | 0 |
| 59 | 5 | 3.55 | 0.00906 | - | 12 | 0 |
| 60 | 5 | 3.55 | 0.00588 | - | 15 | 0 |
| 61 | 5 | 3.55 | 0.00380 | - | 20 | 0 |
| 62 | 5 | 3.55 | 0.00272 | - | 25 | 0 |
| 63 | 5 | 3.55 | 0.00216 | - | 30 | 0 |
| 64 | 5 | 7.04 | 0.20040 | - | 4 | 0 |
| 65 | 5 | 7.04 | 0.08076 | - | 6 | 0 |
| 66 | 5 | 7.04 | 0.04210 | - | 8 | 0 |
| 67 | 5 | 7.04 | 0.02624 | - | 10 | 0 |
| 68 | 5 | 7.04 | 0.01740 | - | 12 | 0 |
| 69 | 5 | 7.04 | 0.01176 | - | 15 | 0 |
| 70 | 5 | 7.04 | 0.00724 | - | 20 | 0 |
| 71 | 5 | 7.04 | 0.00518 | - | 25 | 0 |
| 72 | 5 | 7.04 | 0.00410 | - | 30 | 0 |
| 73 | 5 | 13.80 | 0.43033 | - | 4 | 0 |
| 74 | 5 | 13.80 | 0.16858 | - | 6 | 0 |
| 75 | 5 | 13.80 | 0.08550 | - | 8 | 0 |


| No. | $Z_{\text {substrate }}$ | Mass thickness <br> $\left(\mu \mathrm{g} \mathrm{cm}^{-2}\right)$ | $k(\mathrm{~A} \mid \mathrm{K} \alpha)$ | $k$ (substrate) | Accelerating <br> voltage (kV) | Substrate line |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 76 | 5 | 13.80 | 0.05382 | - | 10 | 0 |
| 77 | 5 | 13.80 | 0.03618 | - | 12 | 0 |
| 78 | 5 | 13.80 | 0.02326 | - | 15 | 0 |
| 79 | 5 | 13.80 | 0.01410 | - | 20 | 0 |
| 80 | 5 | 13.80 | 0.01020 | - | 25 | 0 |
| 81 | 5 | 13.80 | 0.00782 | - | 30 | 0 |
| 82 | 5 | 24.90 | 0.74330 | - | 4 | 0 |
| 83 | 5 | 24.90 | 0.34012 | - | 6 | 0 |
| 84 | 5 | 24.90 | 0.17774 | - | 8 | 0 |
| 85 | 5 | 24.90 | 0.10538 | - | 10 | 0 |
| 86 | 5 | 24.90 | 0.07052 | - | 12 | 0 |
| 87 | 5 | 24.90 | 0.04482 | - | 15 | 0 |
| 88 | 5 | 24.90 | 0.02620 | - | 20 | 0 |
| 89 | 5 | 24.90 | 0.01860 | - | 25 | 0 |
| 90 | 5 | 24.90 | 0.01446 | - | 30 | 0 |
| 91 | 5 | 49.20 | 0.69536 | - | 6 | 0 |
| 92 | 5 | 49.20 | 0.39180 | - | 8 | 0 |
| 93 | 5 | 49.20 | 0.23654 | - | 10 | 0 |
| 94 | 5 | 49.20 | 0.15214 | - | 12 | 0 |
| 95 | 5 | 49.20 | 0.09728 | - | 15 | 0 |
| 96 | 5 | 49.20 | 0.05542 | - | 20 | 0 |
| 97 | 5 | 49.20 | 0.03838 | - | 25 | 0 |
| 98 | 5 | 49.20 | 0.02944 | - | 30 | 0 |
| 99 | 5 | 85.40 | 0.97070 | - | 6 | 0 |
| 100 | 5 | 85.40 | 0.68598 | - | 8 | 0 |
| 101 | 5 | 85.40 | 0.45740 | - | 10 | 0 |
| 102 | 5 | 85.40 | 0.30778 | - | 12 | 0 |
| 103 | 5 | 85.40 | 0.18986 | - | 15 | 0 |
| 104 | 5 | 85.40 | 0.10368 | - | 20 | 0 |
| 105 | 5 | 85.40 | 0.07078 | - | 25 | 0 |
| 106 | 5 | 85.40 | 0.05358 | - | 30 | 0 |
| 107 | 6 | 3.55 | 0.19178 | - | 3 | 0 |
| 108 | 6 | 3.55 | 0.09175 | - | 4 | 0 |
| 109 | 6 | 3.55 | 0.03594 | - | 6 | 0 |
| 110 | 6 | 3.55 | 0.01884 | - | 8 | 0 |
| 111 | 6 | 3.55 | 0.01216 | - | 10 | 0 |
| 112 | 6 | 3.55 | 0.00928 | - | 12 | 0 |
| 113 | 6 | 3.55 | 0.00644 | - | 15 | 0 |
| 114 | 6 | 3.55 | 0.00391 | - | 20 | 0 |
| 115 | 6 | 3.55 | 0.00273 | - | 25 | 0 |
| 116 | 6 | 3.55 | 0.00205 | - | 30 | 0 |
| 117 | 6 | 7.04 | 0.19378 | - | 4 | 0 |
| 118 | 6 | 7.04 | 0.07876 | - | 6 | 0 |
| 119 | 6 | 7.04 | 0.03944 | - | 8 | 0 |
| 120 | 6 | 7.04 | 0.02474 | - | 10 | 0 |
| 121 | 6 | 7.04 | 0.01761 | - | 12 | 0 |
| 122 | 6 | 7.04 | 0.01187 | - | 15 | 0 |
| 123 | 6 | 7.04 | 0.00740 | - | 20 | 0 |
| 124 | 6 | 7.04 | 0.00520 | - | 25 | 0 |
| 125 | 6 | 7.04 | 0.00406 | - | 30 | 0 |
| 126 | 6 | 13.80 | 0.41722 | - | 4 | 0 |
| 127 | 6 | 13.80 | 0.16378 | - | 6 | 0 |
| 128 | 6 | 13.80 | 0.08436 | - | 8 | 0 |
| 129 | 6 | 13.80 | 0.05404 | - | 10 | 0 |
| 130 | 6 | 13.80 | 0.03602 | - | 12 | 0 |
| 131 | 6 | 13.80 | 0.02334 | - | 15 | 0 |
| 132 | 6 | 13.80 | 0.01462 | - | 20 | 0 |
| 133 | 6 | 13.80 | 0.01067 | - | 25 | 0 |
| 134 | 6 | 13.80 | 0.00812 | - | 30 | 0 |
| 135 | 6 | 24.90 | 0.71248 | - | 4 | 0 |
| 136 | 6 | 24.90 | 0.32984 | - | 6 | 0 |
| 137 | 6 | 24.90 | 0.17750 | - | 8 | 0 |
| 138 | 6 | 24.90 | 0.10596 | - | 10 | 0 |
| 139 | 6 | 24.90 | 0.07134 | - | 12 | 0 |
| 140 | 6 | 24.90 | 0.04538 | - | 15 | 0 |
| 141 | 6 | 24.90 | 0.02803 | - | 20 | 0 |
| 142 | 6 | 24.90 | 0.01977 | - | 25 | 0 |
| 143 | 6 | 24.90 | 0.01520 | - | 30 | 0 |


| No. | $Z_{\text {substrate }}$ | Mass thickness <br> $\left(\mu \mathrm{g} \mathrm{cm}{ }^{-2}\right)$ | $k(\mathrm{~A} \mid \mathrm{K} \alpha)$ | k (substrate) | Accelerating <br> voltage $(\mathrm{kV})$ | Substrate line |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 144 | 6 | 49.20 | 0.66364 | - | 6 | 0 |
| 145 | 6 | 49.20 | 0.37756 | - | 8 | 0 |
| 146 | 6 | 49.20 | 0.22920 | - | 10 | 0 |
| 147 | 6 | 49.20 | 0.14986 | - | 12 | 0 |
| 148 | 6 | 49.20 | 0.09580 | - | 15 | 0 |
| 149 | 6 | 49.20 | 0.05627 | - | 20 | 0 |
| 150 | 6 | 49.20 | 0.03916 | - | 25 | 0 |
| 151 | 6 | 49.20 | 0.03035 | - | 30 | 0 |
| 152 | 6 | 85.40 | 0.94594 | - | 6 | 0 |
| 153 | 6 | 85.40 | 0.67848 | - | 8 | 0 |
| 154 | 6 | 85.40 | 0.45444 | - | 10 | 0 |
| 155 | 6 | 85.40 | 0.30700 | - | 12 | 0 |
| 156 | 6 | 85.40 | 0.18968 | - | 15 | 0 |
| 157 | 6 | 85.40 | 0.10604 | - | 20 | 0 |
| 158 | 6 | 85.40 | 0.07118 | - | 25 | 0 |
| 159 | 6 | 85.40 | 0.05394 | - | 30 | 0 |
| 160 | 14 | 3.55 | 0.20496 | - | 3 | 0 |
| 161 | 14 | 3.55 | 0.10778 | 0.76720 | 4 | 0 |
| 162 | 14 | 3.55 | 0.04493 | 0.91448 | 6 | 0 |
| 163 | 14 | 3.55 | 0.02466 | 0.93778 | 8 | 0 |
| 164 | 14 | 3.55 | 0.01638 | 0.95949 | 10 | 0 |
| 165 | 14 | 3.55 | 0.01121 | 0.96447 | 12 | 0 |
| 166 | 14 | 3.55 | 0.00762 | 0.97109 | 15 | 0 |
| 167 | 14 | 3.55 | 0.00496 | 0.97659 | 20 | 0 |
| 168 | 14 | 3.55 | 0.00361 | 0.97599 | 25 | 0 |
| 169 | 14 | 3.55 | 0.00275 | 0.97560 | 30 | 0 |
| 170 | 14 | 7.04 | 0.21944 | 0.65738 | 4 | 0 |
| 171 | 14 | 7.04 | 0.09397 | 0.85438 | 6 | 0 |
| 172 | 14 | 7.04 | 0.05072 | 0.87690 | 8 | 0 |
| 173 | 14 | 7.04 | 0.03218 | 0.93565 | 10 | 0 |
| 174 | 14 | 7.04 | 0.02224 | 0.92824 | 12 | 0 |
| 175 | 14 | 7.04 | 0.01524 | 0.94795 | 15 | 0 |
| 176 | 14 | 7.04 | 0.00952 | 0.95403 | 20 | 0 |
| 177 | 14 | 7.04 | 0.00682 | 0.94823 | 25 | 0 |
| 178 | 14 | 7.04 | 0.00566 | 0.95631 | 30 | 0 |
| 179 | 14 | 13.80 | 0.45748 | 0.45544 | 4 | 0 |
| 180 | 14 | 13.80 | 0.19246 | 0.73096 | 6 | 0 |
| 181 | 14 | 13.80 | 0.10400 | 0.82135 | 8 | 0 |
| 182 | 14 | 13.80 | 0.06710 | 0.87235 | 10 | 0 |
| 183 | 14 | 13.80 | 0.04620 | 0.87960 | 12 | 0 |
| 184 | 14 | 13.80 | 0.03093 | 0.90364 | 15 | 0 |
| 185 | 14 | 13.80 | 0.01912 | 0.90665 | 20 | 0 |
| 186 | 14 | 13.80 | 0.01410 | 0.90646 | 25 | 0 |
| 187 | 14 | 13.80 | 0.01102 | 0.91137 | 30 | 0 |
| 188 | 14 | 24.90 | 0.78246 | 0.20322 | 4 | 0 |
| 189 | 14 | 24.90 | 0.37372 | 0.53483 | 6 | 0 |
| 190 | 14 | 24.90 | 0.20770 | 0.68748 | 8 | 0 |
| 191 | 14 | 24.90 | 0.12844 | 0.76367 | 10 | 0 |
| 192 | 14 | 24.90 | 0.08842 | 0.79426 | 12 | 0 |
| 193 | 14 | 24.90 | 0.05850 | 0.83358 | 15 | 0 |
| 194 | 14 | 24.90 | 0.03582 | 0.84161 | 20 | 0 |
| 195 | 14 | 24.90 | 0.02556 | 0.85433 | 25 | 0 |
| 196 | 14 | 24.90 | 0.02044 | 0.86942 | 30 | 0 |
| 197 | 14 | 49.20 | 0.72061 | 0.22434 | 6 | 0 |
| 198 | 14 | 49.20 | 0.43088 | 0.43913 | 8 | 0 |
| 199 | 14 | 49.20 | 0.27402 | 0.56333 | 10 | 0 |
| 200 | 14 | 49.20 | 0.18708 | 0.62653 | 12 | 0 |
| 201 | 14 | 49.20 | 0.12256 | 0.69151 | 15 | 0 |
| 202 | 14 | 49.20 | 0.07478 | 0.73887 | 20 | 0 |
| 203 | 14 | 49.20 | 0.05250 | 0.74262 | 25 | 0 |
| 204 | 14 | 49.20 | 0.04152 | 0.77000 | 30 | 0 |
| 205 | 14 | 85.40 | 0.96472 | 0.03730 | 6 | 0 |
| 206 | 14 | 85.40 | 0.71610 | 0.18494 | 8 | 0 |
| 207 | 14 | 85.40 | 0.49914 | 0.32185 | 10 | 0 |
| 208 | 14 | 85.40 | 0.35380 | 0.42538 | 12 | 0 |
| 209 | 14 | 85.40 | 0.22992 | 0.51104 | 15 | 0 |
| 210 | 14 | 85.40 | 0.13518 | 0.58221 | 20 | 0 |
| 211 | 14 | 85.40 | 0.09382 | 0.59740 | 25 | 0 |


| No. | $Z_{\text {substrate }}$ | Mass thickness <br> $\left(\mu \mathrm{cm}^{-2}\right)$ | $k(\mathrm{~A} \mid \mathrm{K} \alpha)$ | $k$ (substrate) | Accelerating <br> voltage $(\mathrm{kV})$ | Substrate line |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 212 | 14 | 85.40 | 0.07394 | 0.62524 | 30 | 0 |
| 213 | 22 | 3.55 | 0.21066 | - | 3 | 0 |
| 214 | 22 | 3.55 | 0.11107 | - | 4 | 0 |
| 215 | 22 | 3.55 | 0.04766 | 0.80955 | 6 | 0 |
| 216 | 22 | 3.55 | 0.02679 | 0.91419 | 8 | 0 |
| 217 | 22 | 3.55 | 0.01762 | 0.93847 | 10 | 0 |
| 218 | 22 | 3.55 | 0.01226 | 0.95888 | 12 | 0 |
| 219 | 22 | 3.55 | 0.00818 | 0.98349 | 15 | 0 |
| 220 | 22 | 3.55 | 0.00534 | 0.99000 | 20 | 0 |
| 221 | 22 | 3.55 | 0.00382 | 0.99337 | 25 | 0 |
| 222 | 22 | 3.55 | 0.00293 | 0.99777 | 30 | 0 |
| 223 | 22 | 7.04 | 0.22875 | - | 4 | 0 |
| 224 | 22 | 7.04 | 0.10053 | 0.69460 | 6 | 0 |
| 225 | 22 | 7.04 | 0.05452 | 0.88046 | 8 | 0 |
| 226 | 22 | 7.04 | 0.03466 | 0.92616 | 10 | 0 |
| 227 | 22 | 7.04 | 0.02398 | 0.94008 | 12 | 0 |
| 228 | 22 | 7.04 | 0.01616 | 0.98089 | 15 | 0 |
| 229 | 22 | 7.04 | 0.01019 | 0.97665 | 20 | 0 |
| 230 | 22 | 7.04 | 0.00741 | 0.98680 | 25 | 0 |
| 231 | 22 | 7.04 | 0.00576 | 0.99399 | 30 | 0 |
| 232 | 22 | 13.80 | 0.46874 | - | 4 | 0 |
| 233 | 22 | 13.80 | 0.20186 | 0.48491 | 6 | 0 |
| 234 | 22 | 13.80 | 0.10816 | 0.76928 | 8 | 0 |
| 235 | 22 | 13.80 | 0.07130 | 0.83718 | 10 | 0 |
| 236 | 22 | 13.80 | 0.05040 | 0.90110 | 12 | 0 |
| 237 | 22 | 13.80 | 0.03324 | 0.94854 | 15 | 0 |
| 238 | 22 | 13.80 | 0.02055 | 0.95736 | 20 | 0 |
| 239 | 22 | 13.80 | 0.01519 | 0.96398 | 25 | 0 |
| 240 | 22 | 13.80 | 0.01161 | 0.98292 | 30 | 0 |
| 241 | 22 | 24.90 | 0.79698 | - | 4 | 0 |
| 242 | 22 | 24.90 | 0.38579 | 0.24122 | 6 | 0 |
| 243 | 22 | 24.90 | 0.21888 | 0.64575 | 8 | 0 |
| 244 | 22 | 24.90 | 0.13926 | 0.78693 | 10 | 0 |
| 245 | 22 | 24.90 | 0.09642 | 0.85127 | 12 | 0 |
| 246 | 22 | 24.90 | 0.06240 | 0.92038 | 15 | 0 |
| 247 | 22 | 24.90 | 0.03860 | 0.94062 | 20 | 0 |
| 248 | 22 | 24.90 | 0.02757 | 0.95999 | 25 | 0 |
| 249 | 22 | 24.90 | 0.02178 | 0.97487 | 30 | 0 |
| 250 | 22 | 49.20 | 0.72795 | 0.03735 | 6 | 0 |
| 251 | 22 | 49.20 | 0.44316 | 0.36589 | 8 | 0 |
| 252 | 22 | 49.20 | 0.29064 | 0.57759 | 10 | 0 |
| 253 | 22 | 49.20 | 0.19992 | 0.70950 | 12 | 0 |
| 254 | 22 | 49.20 | 0.13154 | 0.83966 | 15 | 0 |
| 255 | 22 | 49.20 | 0.07856 | 0.89027 | 20 | 0 |
| 256 | 22 | 49.20 | 0.05512 | 0.93257 | 25 | 0 |
| 257 | 22 | 49.20 | 0.04453 | 0.94416 | 30 | 0 |
| 258 | 22 | 85.40 | 0.97016 | 0.01062 | 6 | 0 |
| 259 | 22 | 85.40 | 0.73124 | 0.12301 | 8 | 0 |
| 260 | 22 | 85.40 | 0.52376 | 0.34172 | 10 | 0 |
| 261 | 22 | 85.40 | 0.37058 | 0.53330 | 12 | 0 |
| 262 | 22 | 85.40 | 0.24850 | 0.70714 | 15 | 0 |
| 263 | 22 | 85.40 | 0.14501 | 0.81991 | 20 | 0 |
| 264 | 22 | 85.40 | 0.10318 | 0.88462 | 25 | 0 |
| 265 | 22 | 85.40 | 0.07794 | 0.91875 | 30 | 0 |
| 266 | 24 | 3.55 | 0.23239 | - | 3 | 0 |
| 267 | 24 | 3.55 | 0.11430 | - | 4 | 0 |
| 268 | 24 | 3.55 | 0.04769 | - | 6 | 0 |
| 269 | 24 | 3.55 | 0.02752 | 0.91047 | 8 | 0 |
| 270 | 24 | 3.55 | 0.01788 | 0.96803 | 10 | 0 |
| 271 | 24 | 3.55 | 0.01221 | 0.96432 | 12 | 0 |
| 272 | 24 | 3.55 | 0.00836 | 0.97180 | 15 | 0 |
| 273 | 24 | 3.55 | 0.00547 | 0.98485 | 20 | 0 |
| 274 | 24 | 3.55 | 0.00386 | 0.98619 | 25 | 0 |
| 275 | 24 | 3.55 | 0.00292 | 0.98997 | 30 | 0 |
| 276 | 24 | 7.04 | 0.23965 | - | 4 | 0 |
| 277 | 24 | 7.04 | 0.10403 | - | 6 | 0 |
| 278 | 24 | 7.04 | 0.05626 | 0.87213 | 8 | 0 |
| 279 | 24 | 7.04 | 0.03456 | 0.92704 | 10 | 0 |


| No. | $Z_{\text {substrate }}$ | Mass thickness <br> $\left(\mu \mathrm{g} \mathrm{cm}^{-2}\right)$ | $k(\mathrm{~A} \mid \mathrm{K} \alpha)$ | $k$ (substrate) | Accelerating <br> voltage (kV) | Substrate line |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 280 | 24 | 7.04 | 0.02484 | 0.94725 | 12 | 0 |
| 281 | 24 | 7.04 | 0.01656 | 0.96321 | 15 | 0 |
| 282 | 24 | 7.04 | 0.01020 | 0.98391 | 20 | 0 |
| 283 | 24 | 7.04 | 0.00728 | 0.98403 | 25 | 0 |
| 284 | 24 | 7.04 | 0.00596 | 0.98000 | 30 | 0 |
| 285 | 24 | 13.80 | 0.47757 | - | 4 | 0 |
| 286 | 24 | 13.80 | 0.20666 | - | 6 | 0 |
| 287 | 24 | 13.80 | 0.11052 | 0.76095 | 8 | 0 |
| 288 | 24 | 13.80 | 0.07344 | 0.86948 | 10 | 0 |
| 289 | 24 | 13.80 | 0.05156 | 0.90768 | 12 | 0 |
| 290 | 24 | 13.80 | 0.03360 | 0.94766 | 15 | 0 |
| 291 | 24 | 13.80 | 0.02110 | 0.96817 | 20 | 0 |
| 292 | 24 | 13.80 | 0.01546 | 0.97610 | 25 | 0 |
| 293 | 24 | 13.80 | 0.01184 | 0.97513 | 30 | 0 |
| 294 | 24 | 24.90 | 0.79310 | - | 4 | 0 |
| 295 | 24 | 24.90 | 0.38855 | - | 6 | 0 |
| 296 | 24 | 24.90 | 0.22476 | 0.57961 | 8 | 0 |
| 297 | 24 | 24.90 | 0.14062 | 0.77402 | 10 | 0 |
| 298 | 24 | 24.90 | 0.09778 | 0.84622 | 12 | 0 |
| 299 | 24 | 24.90 | 0.06438 | 0.90804 | 15 | 0 |
| 300 | 24 | 24.90 | 0.03892 | 0.94819 | 20 | 0 |
| 301 | 24 | 24.90 | 0.02824 | 0.96387 | 25 | 0 |
| 302 | 24 | 24.90 | 0.02203 | 0.97500 | 30 | 0 |
| 303 | 24 | 49.20 | 0.73163 | - | 6 | 0 |
| 304 | 24 | 49.20 | 0.45840 | 0.27440 | 8 | 0 |
| 305 | 24 | 49.20 | 0.29780 | 0.55602 | 10 | 0 |
| 306 | 24 | 49.20 | 0.20384 | 0.70715 | 12 | 0 |
| 307 | 24 | 49.20 | 0.13566 | 0.82365 | 15 | 0 |
| 308 | 24 | 49.20 | 0.08054 | 0.90966 | 20 | 0 |
| 309 | 24 | 49.20 | 0.05855 | 0.93455 | 25 | 0 |
| 310 | 24 | 49.20 | 0.04540 | 0.94539 | 30 | 0 |
| 311 | 24 | 85.40 | 0.97872 | - | 6 | 0 |
| 312 | 24 | 85.40 | 0.72654 | 0.06603 | 8 | 0 |
| 313 | 24 | 85.40 | 0.52608 | 0.29875 | 10 | 0 |
| 314 | 24 | 85.40 | 0.37704 | 0.50430 | 12 | 0 |
| 315 | 24 | 85.40 | 0.25248 | 0.69341 | 15 | 0 |
| 316 | 24 | 85.40 | 0.14850 | 0.83155 | 20 | 0 |
| 317 | 24 | 85.40 | 0.10410 | 0.88987 | 25 | 0 |
| 318 | 24 | 85.40 | 0.08232 | 0.91084 | 30 | 0 |
| 319 | 26 | 3.55 | 0.23224 | - | 3 | 0 |
| 320 | 26 | 3.55 | 0.11327 | - | 4 | 0 |
| 321 | 26 | 3.55 | 0.04987 | - | 6 | 0 |
| 322 | 26 | 3.55 | 0.02745 | 0.81637 | 8 | 0 |
| 323 | 26 | 3.55 | 0.01818 | 0.96713 | 10 | 0 |
| 324 | 26 | 3.55 | 0.01205 | 0.96796 | 12 | 0 |
| 325 | 26 | 3.55 | 0.00854 | 0.97946 | 15 | 0 |
| 326 | 26 | 3.55 | 0.00553 | 0.99453 | 20 | 0 |
| 327 | 26 | 3.55 | 0.00388 | 0.99467 | 25 | 0 |
| 328 | 26 | 3.55 | 0.00295 | 0.99999 | 30 | 0 |
| 329 | 26 | 3.55 | - | 0.91032 | 6 | 1 |
| 330 | 26 | 3.55 | - | 0.92594 | 8 | 1 |
| 331 | 26 | 3.55 | - | 0.94591 | 10 | 1 |
| 332 | 26 | 3.55 | - | 0.95197 | 12 | 1 |
| 333 | 26 | 7.04 | 0.23452 | - | 4 | 0 |
| 334 | 26 | 7.04 | 0.10414 | - | 6 | 0 |
| 335 | 26 | 7.04 | 0.05678 | 0.75662 | 8 | 0 |
| 336 | 26 | 7.04 | 0.03612 | 0.93959 | 10 | 0 |
| 337 | 26 | 7.04 | 0.02490 | 0.98146 | 12 | 0 |
| 338 | 26 | 7.04 | 0.01769 | 0.98300 | 15 | 0 |
| 339 | 26 | 7.04 | 0.01040 | 0.98700 | 20 | 0 |
| 340 | 26 | 7.04 | 0.00746 | 0.99200 | 25 | 0 |
| 341 | 26 | 7.04 | 0.00599 | 0.99500 | 30 | 0 |
| 342 | 26 | 7.04 | - | 0.86684 | 6 | 1 |
| 343 | 26 | 7.04 | - | 0.90022 | 8 | 1 |
| 344 | 26 | 7.04 | - | 0.93265 | 10 | 1 |
| 345 | 26 | 7.04 | - | 0.95637 | 12 | 1 |
| 346 | 26 | 13.80 | 0.48080 | - | 4 | 0 |
| 347 | 26 | 13.80 | 0.20940 | - | 6 | 0 |


| No. | $z_{\text {substrate }}$ | Mass thickness <br> $\left(\mu \mathrm{g} \mathrm{cm}^{-2}\right)$ | $k(\mathrm{~A} \mid \mathrm{K} \alpha)$ | $k$ (substrate) | Accelerating <br> voltage (kV) | Substrate line |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 348 | 26 | 13.80 | 0.11394 | 0.57793 | 8 | 0 |
| 349 | 26 | 13.80 | 0.07512 | 0.86758 | 10 | 0 |
| 350 | 26 | 13.80 | 0.05282 | 0.94376 | 12 | 0 |
| 351 | 26 | 13.80 | 0.03412 | 0.93564 | 15 | 0 |
| 352 | 26 | 13.80 | 0.02091 | 0.94043 | 20 | 0 |
| 353 | 26 | 13.80 | 0.01563 | 0.97845 | 25 | 0 |
| 354 | 26 | 13.80 | 0.01180 | 0.99999 | 30 | 0 |
| 355 | 26 | 13.80 | - | 0.77222 | 6 | 1 |
| 356 | 26 | 13.80 | - | 0.84891 | 8 | 1 |
| 357 | 26 | 13.80 | - | 0.88585 | 10 | 1 |
| 358 | 26 | 13.80 | - | 0.91239 | 12 | 1 |
| 359 | 26 | 24.90 | 0.78920 | - | 4 | 0 |
| 360 | 26 | 24.90 | 0.39604 | - | 6 | 0 |
| 361 | 26 | 24.90 | 0.22558 | 0.34707 | 8 | 0 |
| 362 | 26 | 24.90 | 0.14407 | 0.73640 | 10 | 0 |
| 363 | 26 | 24.90 | 0.09994 | 0.87865 | 12 | 0 |
| 364 | 26 | 24.90 | 0.06538 | 0.89956 | 15 | 0 |
| 365 | 26 | 24.90 | 0.04013 | 0.94004 | 20 | 0 |
| 366 | 26 | 24.90 | 0.02887 | 0.96704 | 25 | 0 |
| 367 | 26 | 24.90 | 0.02248 | 0.99999 | 30 | 0 |
| 368 | 26 | 24.90 | - | 0.58730 | 6 | 1 |
| 369 | 26 | 24.90 | - | 0.74152 | 8 | 1 |
| 370 | 26 | 24.90 | - | 0.80390 | 10 | 1 |
| 371 | 26 | 24.90 | - | 0.84390 | 12 | 1 |
| 372 | 26 | 49.20 | 0.73609 | - | 6 | 0 |
| 373 | 26 | 49.20 | 0.45993 | 0.09354 | 8 | 0 |
| 374 | 26 | 49.20 | 0.30140 | 0.49089 | 10 | 0 |
| 375 | 26 | 49.20 | 0.20834 | 0.71368 | 12 | 0 |
| 376 | 26 | 49.20 | 0.13693 | 0.80922 | 15 | 0 |
| 377 | 26 | 49.20 | 0.08200 | 0.84567 | 20 | 0 |
| 378 | 26 | 49.20 | 0.05718 | 0.91370 | 25 | 0 |
| 379 | 26 | 49.20 | 0.04557 | 0.96844 | 30 | 0 |
| 380 | 26 | 49.20 | - | 0.29215 | 6 | 1 |
| 381 | 26 | 49.20 | - | 0.51745 | 8 | 1 |
| 382 | 26 | 49.20 | - | 0.64521 | 10 | 1 |
| 383 | 26 | 49.20 | - | 0.71490 | 12 | 1 |
| 384 | 26 | 85.40 | 0.97766 | - | 6 | 0 |
| 385 | 26 | 85.40 | 0.73840 | - | 8 | 0 |
| 386 | 26 | 85.40 | 0.52578 | 0.22388 | 10 | 0 |
| 387 | 26 | 85.40 | 0.38546 | 0.48346 | 12 | 0 |
| 388 | 26 | 85.40 | 0.25522 | 0.67988 | 15 | 0 |
| 389 | 26 | 85.40 | 0.15070 | 0.82080 | 20 | 0 |
| 390 | 26 | 85.40 | 0.10494 | 0.88315 | 25 | 0 |
| 391 | 26 | 85.40 | 0.08052 | 0.94174 | 30 | 0 |
| 392 | 26 | 85.40 | - | 0.06428 | 6 | 1 |
| 393 | 26 | 85.40 | - | 0.25603 | 8 | 1 |
| 394 | 26 | 85.40 | - | 0.41962 | 10 | 1 |
| 395 | 26 | 85.40 | - | 0.53518 | 12 | 1 |
| 396 | 28 | 3.55 | 0.23590 | - | 3 | 0 |
| 397 | 28 | 3.55 | 0.11695 | - | 4 | 0 |
| 398 | 28 | 3.55 | 0.04979 | - | 6 | 0 |
| 399 | 28 | 3.55 | 0.02819 | - | 8 | 0 |
| 400 | 28 | 3.55 | 0.01840 | 0.92428 | 10 | 0 |
| 401 | 28 | 3.55 | 0.01282 | 0.97480 | 12 | 0 |
| 402 | 28 | 3.55 | 0.00880 | 0.97550 | 15 | 0 |
| 403 | 28 | 3.55 | 0.00564 | 0.99660 | 20 | 0 |
| 404 | 28 | 3.55 | 0.00402 | 0.98270 | 25 | 0 |
| 405 | 28 | 3.55 | 0.00304 | 0.99900 | 30 | 0 |
| 406 | 28 | 3.55 | - | 0.86817 | 4 | 1 |
| 407 | 28 | 3.55 | - | 0.93934 | 6 | 1 |
| 408 | 28 | 3.55 | - | 0.95785 | 8 | 1 |
| 409 | 28 | 3.55 | - | 0.96660 | 10 | 1 |
| 410 | 28 | 3.55 | - | 0.97370 | 12 | 1 |
| 411 | 28 | 3.55 | - | 0.98040 | 15 | 1 |
| 412 | 28 | 7.04 | 0.24013 | - | 4 | 0 |
| 413 | 28 | 7.04 | 0.10480 | - | 6 | 0 |
| 414 | 28 | 7.04 | 0.05750 | - | 8 | 0 |
| 415 | 28 | 7.04 | 0.03666 | 0.86015 | 10 | 0 |


| No. | $Z_{\text {substrate }}$ | Mass thickness <br> $\left(\mu \mathrm{g} \mathrm{cm}^{-2}\right)$ | $k(\mathrm{~A} \mid \mathrm{K} \alpha)$ | $k$ (substrate) | Accelerating <br> voltage $(\mathrm{kV})$ | Substrate line |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 416 | 28 | 7.04 | 0.02518 | 0.94880 | 12 | 0 |
| 417 | 28 | 7.04 | 0.01764 | 0.96600 | 15 | 0 |
| 418 | 28 | 7.04 | 0.01070 | 0.97000 | 20 | 0 |
| 419 | 28 | 7.04 | 0.00759 | 0.97730 | 25 | 0 |
| 420 | 28 | 7.04 | 0.00612 | 0.99270 | 30 | 0 |
| 421 | 28 | 7.04 | - | 0.74791 | 4 | 1 |
| 422 | 28 | 7.04 | - | 0.89227 | 6 | 1 |
| 423 | 28 | 7.04 | - | 0.91895 | 8 | 1 |
| 424 | 28 | 7.04 | - | 0.92649 | 10 | 1 |
| 425 | 28 | 7.04 | - | 0.94880 | 12 | 1 |
| 426 | 28 | 7.04 | - | 0.95410 | 15 | 1 |
| 427 | 28 | 13.80 | 0.48310 | - | 4 | 0 |
| 428 | 28 | 13.80 | 0.21244 | - | 6 | 0 |
| 429 | 28 | 13.80 | 0.11610 | - | 8 | 0 |
| 430 | 28 | 13.80 | 0.07686 | 0.78162 | 10 | 0 |
| 431 | 28 | 13.80 | 0.05334 | 0.90020 | 12 | 0 |
| 432 | 28 | 13.80 | 0.03528 | 0.91880 | 15 | 0 |
| 433 | 28 | 13.80 | 0.02181 | 0.94820 | 20 | 0 |
| 434 | 28 | 13.80 | 0.01605 | 0.96490 | 25 | 0 |
| 435 | 28 | 13.80 | 0.01227 | 0.97150 | 30 | 0 |
| 436 | 28 | 13.80 | - | 0.60489 | 4 | 1 |
| 437 | 28 | 13.80 | - | 0.84022 | 6 | 1 |
| 438 | 28 | 13.80 | - | 0.90192 | 8 | 1 |
| 439 | 28 | 13.80 | - | 0.91392 | 10 | 1 |
| 440 | 28 | 13.80 | - | 0.94820 | 12 | 1 |
| 441 | 28 | 13.80 | - | 0.95410 | 15 | 1 |
| 442 | 28 | 24.90 | 0.80592 | - | 4 | 0 |
| 443 | 28 | 24.90 | 0.39630 | - | 6 | 0 |
| 444 | 28 | 24.90 | 0.23103 | - | 8 | 0 |
| 445 | 28 | 24.90 | 0.14670 | 0.62058 | 10 | 0 |
| 446 | 28 | 24.90 | 0.10170 | 0.80860 | 12 | 0 |
| 447 | 28 | 24.90 | 0.06760 | 0.89560 | 15 | 0 |
| 448 | 28 | 24.90 | 0.04143 | 0.93440 | 20 | 0 |
| 449 | 28 | 24.90 | 0.02948 | 0.95580 | 25 | 0 |
| 450 | 28 | 24.90 | 0.02290 | 0.96000 | 30 | 0 |
| 451 | 28 | 24.90 | - | 0.32447 | 4 | 1 |
| 452 | 28 | 24.90 | - | 0.67740 | 6 | 1 |
| 453 | 28 | 24.90 | - | 0.81946 | 8 | 1 |
| 454 | 28 | 24.90 | - | 0.88660 | 10 | 1 |
| 455 | 28 | 24.90 | - | 0.90110 | 12 | 1 |
| 456 | 28 | 24.90 | - | 0.92350 | 15 | 1 |
| 457 | 28 | 49.20 | 0.73952 | - | 6 | 0 |
| 458 | 28 | 49.20 | 0.46307 | - | 8 | 0 |
| 459 | 28 | 49.20 | 0.30655 | 0.32144 | 10 | 0 |
| 460 | 28 | 49.20 | 0.21086 | 0.62640 | 12 | 0 |
| 461 | 28 | 49.20 | 0.14090 | 0.80200 | 15 | 0 |
| 462 | 28 | 49.20 | 0.08432 | 0.89350 | 20 | 0 |
| 463 | 28 | 49.20 | 0.06113 | 0.92550 | 25 | 0 |
| 464 | 28 | 49.20 | 0.04698 | 0.93980 | 30 | 0 |
| 465 | 28 | 49.20 | - | 0.04517 | 4 | 1 |
| 466 | 28 | 49.20 | - | 0.35622 | 6 | 1 |
| 467 | 28 | 49.20 | - | 0.61198 | 8 | 1 |
| 468 | 28 | 49.20 | - | 0.73603 | 10 | 1 |
| 469 | 28 | 49.20 | - | 0.80170 | 12 | 1 |
| 470 | 28 | 49.20 | - | 0.85210 | 15 | 1 |
| 471 | 28 | 85.40 | 0.98039 | - | 6 | 0 |
| 472 | 28 | 85.40 | 0.73590 | - | 8 | 0 |
| 473 | 28 | 85.40 | 0.53036 | - | 10 | 0 |
| 474 | 28 | 85.40 | 0.38626 | 0.38510 | 12 | 0 |
| 475 | 28 | 85.40 | 0.26136 | 0.64500 | 15 | 0 |
| 476 | 28 | 85.40 | 0.15410 | 0.82150 | 20 | 0 |
| 477 | 28 | 85.40 | 0.10718 | 0.87100 | 25 | 0 |
| 478 | 28 | 85.40 | 0.08208 | 0.90920 | 30 | 0 |
| 479 | 28 | 85.40 | - | 0.08446 | 6 | 1 |
| 480 | 28 | 85.40 | - | 0.32169 | 8 | 1 |
| 481 | 28 | 85.40 | - | 0.51495 | 10 | 1 |
| 482 | 28 | 85.40 | - | 0.64270 | 12 | 1 |
| 483 | 28 | 85.40 | - | 0.75390 | 15 | 1 |


| No. | $Z_{\text {substrate }}$ | Mass thickness <br> $\left(\mu \mathrm{g} \mathrm{cm}^{-2}\right)$ | $k(\mathrm{~A} \mid \mathrm{K} \alpha)$ | $k$ (substrate) | Accelerating <br> voltage $(\mathrm{kV})$ | Substrate line |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 484 | 29 | 3.55 | 0.23640 | - | 3 | 0 |
| 485 | 29 | 3.55 | 0.11740 | - | 4 | 0 |
| 486 | 29 | 3.55 | 0.05043 | - | 6 | 0 |
| 487 | 29 | 3.55 | 0.02920 | - | 8 | 0 |
| 488 | 29 | 3.55 | 0.01890 | - | 10 | 0 |
| 489 | 29 | 3.55 | 0.01286 | 0.94878 | 12 | 0 |
| 490 | 29 | 3.55 | 0.00884 | 0.97301 | 15 | 0 |
| 491 | 29 | 3.55 | 0.00565 | 0.98319 | 20 | 0 |
| 492 | 29 | 3.55 | 0.00405 | 0.99000 | 25 | 0 |
| 493 | 29 | 3.55 | 0.00311 | 0.99617 | 30 | 0 |
| 494 | 29 | 3.55 | - | 0.85512 | 4 | 1 |
| 495 | 29 | 3.55 | - | 0.93448 | 6 | 1 |
| 496 | 29 | 3.55 | - | 0.97200 | 8 | 1 |
| 497 | 29 | 3.55 | - | 0.95705 | 10 | 1 |
| 498 | 29 | 3.55 | - | 0.97310 | 12 | 1 |
| 499 | 29 | 3.55 | - | 0.97420 | 15 | 1 |
| 500 | 29 | 3.55 | - | 0.98663 | 20 | 1 |
| 501 | 29 | 3.55 | - | 0.99227 | 25 | 1 |
| 502 | 29 | 3.55 | - | 0.97592 | 30 | 1 |
| 503 | 29 | 7.04 | 0.24048 | - | 4 | 0 |
| 504 | 29 | 7.04 | 0.10579 | - | 6 | 0 |
| 505 | 29 | 7.04 | 0.05826 | - | 8 | 0 |
| 506 | 29 | 7.04 | 0.03732 | - | 10 | 0 |
| 507 | 29 | 7.04 | 0.02594 | 0.92677 | 12 | 0 |
| 508 | 29 | 7.04 | 0.01823 | 0.96248 | 15 | 0 |
| 509 | 29 | 7.04 | 0.01105 | 0.95736 | 20 | 0 |
| 510 | 29 | 7.04 | 0.00784 | 0.97979 | 25 | 0 |
| 511 | 29 | 7.04 | 0.00615 | 0.99000 | 30 | 0 |
| 512 | 29 | 7.04 | - | 0.74566 | 4 | 1 |
| 513 | 29 | 7.04 | - | 0.89242 | 6 | 1 |
| 514 | 29 | 7.04 | - | 0.94333 | 8 | 1 |
| 515 | 29 | 7.04 | - | 0.93681 | 10 | 1 |
| 516 | 29 | 7.04 | - | 0.95592 | 12 | 1 |
| 517 | 29 | 7.04 | - | 0.95662 | 15 | 1 |
| 518 | 29 | 7.04 | - | 0.98675 | 20 | 1 |
| 519 | 29 | 7.04 | - | 0.98785 | 25 | 1 |
| 520 | 29 | 7.04 | - | 0.99244 | 30 | 1 |
| 521 | 29 | 13.80 | 0.48384 | - | 4 | 0 |
| 522 | 29 | 13.80 | 0.21368 | - | 6 | 0 |
| 523 | 29 | 13.80 | 0.11748 | - | 8 | 0 |
| 524 | 29 | 13.80 | 0.07694 | - | 10 | 0 |
| 525 | 29 | 13.80 | 0.05312 | 0.92344 | 12 | 0 |
| 526 | 29 | 13.80 | 0.03740 | 0.93486 | 15 | 0 |
| 527 | 29 | 13.80 | 0.02196 | 0.93735 | 20 | 0 |
| 528 | 29 | 13.80 | 0.01628 | 0.98826 | 25 | 0 |
| 529 | 29 | 13.80 | 0.01235 | 0.99999 | 30 | 0 |
| 530 | 29 | 13.80 | - | 0.57197 | 4 | 1 |
| 531 | 29 | 13.80 | - | 0.80859 | 6 | 1 |
| 532 | 29 | 13.80 | - | 0.88203 | 8 | 1 |
| 533 | 29 | 13.80 | - | 0.90673 | 10 | 1 |
| 534 | 29 | 13.80 | - | 0.93856 | 12 | 1 |
| 535 | 29 | 13.80 | - | 0.94743 | 15 | 1 |
| 536 | 29 | 13.80 | - | 0.95955 | 20 | 1 |
| 537 | 29 | 13.80 | - | 0.95420 | 25 | 1 |
| 538 | 29 | 13.80 | - | 0.96708 | 30 | 1 |
| 539 | 29 | 24.90 | 0.80070 | - | 4 | 0 |
| 540 | 29 | 24.90 | 0.39731 | - | 6 | 0 |
| 541 | 29 | 24.90 | 0.23322 | - | 8 | 0 |
| 542 | 29 | 24.90 | 0.14783 | - | 10 | 0 |
| 543 | 29 | 24.90 | 0.10296 | 0.80334 | 12 | 0 |
| 544 | 29 | 24.90 | 0.06939 | 0.88389 | 15 | 0 |
| 545 | 29 | 24.90 | 0.04185 | 0.94048 | 20 | 0 |
| 546 | 29 | 24.90 | 0.02993 | 0.97383 | 25 | 0 |
| 547 | 29 | 24.90 | 0.02319 | 0.99999 | 30 | 0 |
| 548 | 29 | 24.90 | - | 0.31578 | 4 | 1 |
| 549 | 29 | 24.90 | - | 0.65147 | 6 | 1 |
| 550 | 29 | 24.90 | - | 0.78942 | 8 | 1 |
| 551 | 29 | 24.90 | - | 0.85093 | 10 | 1 |


| No. | $Z_{\text {substrate }}$ | Mass thickness <br> $\left(\mu \mathrm{g} \mathrm{cm}^{-2}\right)$ | $k(\mathrm{AI} \mathrm{K} \alpha)$ | k (substrate) | Accelerating <br> voltage $(\mathrm{kV})$ | Substrate line |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 552 | 29 | 24.90 | - | 0.89602 | 12 | 1 |
| 553 | 29 | 24.90 | - | 0.91347 | 15 | 1 |
| 554 | 29 | 24.90 | - | 0.95331 | 20 | 1 |
| 555 | 29 | 24.90 | - | 0.95017 | 25 | 1 |
| 556 | 29 | 24.90 | - | 0.95927 | 30 | 1 |
| 557 | 29 | 49.20 | 0.74348 | - | 6 | 0 |
| 558 | 29 | 49.20 | 0.46362 | - | 8 | 0 |
| 559 | 29 | 49.20 | 0.30638 | - | 10 | 0 |
| 560 | 29 | 49.20 | 0.21122 | 0.58060 | 12 | 0 |
| 561 | 29 | 49.20 | 0.14150 | 0.77922 | 15 | 0 |
| 562 | 29 | 49.20 | 0.08468 | 0.88183 | 20 | 0 |
| 563 | 29 | 49.20 | 0.06197 | 0.93446 | 25 | 0 |
| 564 | 29 | 49.20 | 0.04740 | 0.97656 | 30 | 0 |
| 565 | 29 | 49.20 | - | 0.03806 | 4 | 1 |
| 566 | 29 | 49.20 | - | 0.31838 | 6 | 1 |
| 567 | 29 | 49.20 | - | 0.56396 | 8 | 1 |
| 568 | 29 | 49.20 | - | 0.69030 | 10 | 1 |
| 569 | 29 | 49.20 | - | 0.77435 | 12 | 1 |
| 570 | 29 | 49.20 | - | 0.82359 | 15 | 1 |
| 571 | 29 | 49.20 | - | 0.87402 | 20 | 1 |
| 572 | 29 | 49.20 | - | 0.90751 | 25 | 1 |
| 573 | 29 | 49.20 | - | 0.90851 | 30 | 1 |
| 574 | 29 | 85.40 | 0.98100 | - | 6 | 0 |
| 575 | 29 | 85.40 | 0.74983 | - | 8 | 0 |
| 576 | 29 | 85.40 | 0.53302 | - | 10 | 0 |
| 577 | 29 | 85.40 | 0.38625 | 0.34329 | 12 | 0 |
| 578 | 29 | 85.40 | 0.27614 | 0.63040 | 15 | 0 |
| 579 | 29 | 85.40 | 0.15524 | 0.80689 | 20 | 0 |
| 580 | 29 | 85.40 | 0.10884 | 0.88276 | 25 | 0 |
| 581 | 29 | 85.40 | 0.08657 | 0.95664 | 30 | 0 |
| 582 | 29 | 85.40 | - | 0.07770 | 6 | 1 |
| 583 | 29 | 85.40 | - | 0.29645 | 8 | 1 |
| 584 | 29 | 85.40 | - | 0.48197 | 10 | 1 |
| 585 | 29 | 85.40 | - | 0.62005 | 12 | 1 |
| 586 | 29 | 85.40 | - | 0.72796 | 15 | 1 |
| 587 | 29 | 85.40 | - | 0.82260 | 20 | 1 |
| 588 | 29 | 85.40 | - | 0.85762 | 25 | 1 |
| 589 | 29 | 85.40 | - | 0.85740 | 30 | 1 |
| 590 | 32 | 3.55 | 0.24210 | - | 3 | 1 |
| 591 | 32 | 3.55 | 0.12064 | 0.87360 | 4 | 1 |
| 592 | 32 | 3.55 | 0.05189 | 0.95721 | 6 | 1 |
| 593 | 32 | 3.55 | 0.02891 | 0.96297 | 8 | 1 |
| 594 | 32 | 3.55 | 0.01928 | 0.98982 | 10 | 1 |
| 595 | 32 | 3.55 | 0.01333 | 0.98420 | 12 | 1 |
| 596 | 32 | 3.55 | 0.00916 | 0.99910 | 15 | 1 |
| 597 | 32 | 3.55 | 0.00587 | 0.99999 | 20 | 1 |
| 598 | 32 | 3.55 | 0.00414 | 0.99421 | 25 | 1 |
| 599 | 32 | 3.55 | 0.00308 | 0.99978 | 30 | 1 |
| 600 | 32 | 3.55 | - | 1.01977 | 15 | 0 |
| 601 | 32 | 3.55 | - | 1.00561 | 20 | 0 |
| 602 | 32 | 3.55 | - | 1.00261 | 25 | 0 |
| 603 | 32 | 3.55 | - | 1.01795 | 30 | 0 |
| 604 | 32 | 7.04 | 0.24552 | 0.76802 | 4 | 1 |
| 605 | 32 | 7.04 | 0.10918 | 0.91707 | 6 | 1 |
| 606 | 32 | 7.04 | 0.06004 | 0.93214 | 8 | 1 |
| 607 | 32 | 7.04 | 0.03856 | 0.97758 | 10 | 1 |
| 608 | 32 | 7.04 | 0.02658 | 0.97285 | 12 | 1 |
| 609 | 32 | 7.04 | 0.01825 | 0.99290 | 15 | 1 |
| 610 | 32 | 7.04 | 0.01149 | 0.99821 | 20 | 1 |
| 611 | 32 | 7.04 | 0.00813 | 0.99106 | 25 | 1 |
| 612 | 32 | 7.04 | 0.00618 | 0.99897 | 30 | 1 |
| 613 | 32 | 7.04 | - | 1.00244 | 15 | 0 |
| 614 | 32 | 7.04 | - | 0.99942 | 20 | 0 |
| 615 | 32 | 7.04 | - | 1.01833 | 25 | 0 |
| 616 | 32 | 7.04 | - | 1.01517 | 30 | 0 |
| 617 | 32 | 13.80 | 0.49236 | 0.56967 | 4 | 1 |
| 618 | 32 | 13.80 | 0.21920 | 0.82128 | 6 | 1 |
| 619 | 32 | 13.80 | 0.12086 | 0.87491 | 8 | 1 |


| No. | $Z_{\text {substrate }}$ | Mass thickness <br> $\left(\mu \mathrm{cm}^{-2}\right)$ | $k(\mathrm{~A} \mid \mathrm{K} \alpha)$ | $k$ (substrate) | Accelerating <br> voltage $(\mathrm{kV})$ | Substrate line |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 620 | 32 | 13.80 | 0.07906 | 0.93829 | 10 | 1 |
| 621 | 32 | 13.80 | 0.05468 | 0.94851 | 12 | 1 |
| 622 | 32 | 13.80 | 0.03616 | 0.97775 | 15 | 1 |
| 623 | 32 | 13.80 | 0.02227 | 0.98206 | 20 | 1 |
| 624 | 32 | 13.80 | 0.01656 | 0.99394 | 25 | 1 |
| 625 | 32 | 13.80 | 0.01259 | 0.99999 | 30 | 1 |
| 626 | 32 | 13.80 | - | 0.96794 | 15 | 0 |
| 627 | 32 | 13.80 | - | 0.98933 | 20 | 0 |
| 628 | 32 | 13.80 | - | 0.99346 | 25 | 0 |
| 629 | 32 | 13.80 | - | 1.01233 | 30 | 0 |
| 630 | 32 | 24.90 | 0.80986 | 0.29506 | 4 | 1 |
| 631 | 32 | 24.90 | 0.41186 | 0.65619 | 6 | 1 |
| 632 | 32 | 24.90 | 0.23620 | 0.79279 | 8 | 1 |
| 633 | 32 | 24.90 | 0.14986 | 0.87784 | 10 | 1 |
| 634 | 32 | 24.90 | 0.10544 | 0.90865 | 12 | 1 |
| 635 | 32 | 24.90 | 0.07081 | 0.95099 | 15 | 1 |
| 636 | 32 | 24.90 | 0.04226 | 0.96803 | 20 | 1 |
| 637 | 32 | 24.90 | 0.03024 | 0.98236 | 25 | 1 |
| 638 | 32 | 24.90 | 0.02372 | 0.98582 | 30 | 1 |
| 639 | 32 | 24.90 | - | 0.90592 | 15 | 0 |
| 640 | 32 | 24.90 | - | 0.96277 | 20 | 0 |
| 641 | 32 | 24.90 | - | 0.99311 | 25 | 0 |
| 642 | 32 | 24.90 | - | 0.99788 | 30 | 0 |
| 643 | 32 | 49.20 | 0.74887 | 0.32890 | 6 | 1 |
| 644 | 32 | 49.20 | 0.47498 | 0.57985 | 8 | 1 |
| 645 | 32 | 49.20 | 0.31592 | 0.72741 | 10 | 1 |
| 646 | 32 | 49.20 | 0.22024 | 0.80730 | 12 | 1 |
| 647 | 32 | 49.20 | 0.14558 | 0.89495 | 15 | 1 |
| 648 | 32 | 49.20 | 0.08638 | 0.93358 | 20 | 1 |
| 649 | 32 | 49.20 | 0.06162 | 0.95548 | 25 | 1 |
| 650 | 32 | 49.20 | 0.04865 | 0.95769 | 30 | 1 |
| 651 | 32 | 49.20 | - | 0.76563 | 15 | 0 |
| 652 | 32 | 49.20 | - | 0.91273 | 20 | 0 |
| 653 | 32 | 49.20 | - | 0.95254 | 25 | 0 |
| 654 | 32 | 49.20 | - | 0.97338 | 30 | 0 |
| 655 | 32 | 85.40 | 0.97568 | 0.07653 | 6 | 1 |
| 656 | 32 | 85.40 | 0.74624 | 0.30684 | 8 | 1 |
| 657 | 32 | 85.40 | 0.54814 | 0.51240 | 10 | 1 |
| 658 | 32 | 85.40 | 0.40134 | 0.64701 | 12 | 1 |
| 659 | 32 | 85.40 | 0.28466 | 0.78317 | 15 | 1 |
| 660 | 32 | 85.40 | 0.15866 | 0.87321 | 20 | 1 |
| 661 | 32 | 85.40 | 0.11895 | 0.91821 | 25 | 1 |
| 662 | 32 | 85.40 | 0.08824 | 0.92802 | 30 | 1 |
| 663 | 32 | 85.40 | - | 0.56032 | 15 | 0 |
| 664 | 32 | 85.40 | - | 0.82461 | 20 | 0 |
| 665 | 32 | 85.40 | - | 0.90512 | 25 | 0 |
| 666 | 32 | 85.40 | - | 0.93941 | 30 | 0 |
| 667 | 40 | 3.55 | 0.25204 | - | 3 | 1 |
| 668 | 40 | 3.55 | 0.12324 | 0.76180 | 4 | 1 |
| 669 | 40 | 3.55 | 0.05254 | 0.87800 | 6 | 1 |
| 670 | 40 | 3.55 | 0.03058 | 0.88790 | 8 | 1 |
| 671 | 40 | 3.55 | 0.01956 | 0.95450 | 10 | 1 |
| 672 | 40 | 3.55 | 0.01366 | 0.95380 | 12 | 1 |
| 673 | 40 | 3.55 | 0.00970 | 0.97620 | 15 | 1 |
| 674 | 40 | 3.55 | 0.00629 | 0.98440 | 20 | 1 |
| 675 | 40 | 3.55 | 0.00444 | 0.99230 | 25 | 1 |
| 676 | 40 | 3.55 | 0.00336 | 0.99610 | 30 | 1 |
| 677 | 40 | 7.04 | 0.24800 | 0.62940 | 4 | 1 |
| 678 | 40 | 7.04 | 0.11136 | 0.81840 | 6 | 1 |
| 679 | 40 | 7.04 | 0.06148 | 0.87600 | 8 | 1 |
| 680 | 40 | 7.04 | 0.03950 | 0.92750 | 10 | 1 |
| 681 | 40 | 7.04 | 0.02784 | 0.93650 | 12 | 1 |
| 682 | 40 | 7.04 | 0.01941 | 0.94980 | 15 | 1 |
| 683 | 40 | 7.04 | 0.01194 | 0.96760 | 20 | 1 |
| 684 | 40 | 7.04 | 0.00865 | 0.98010 | 25 | 1 |
| 685 | 40 | 7.04 | 0.00683 | 0.97570 | 30 | 1 |
| 686 | 40 | 13.80 | 0.49426 | 0.41500 | 4 | 1 |
| 687 | 40 | 13.80 | 0.22303 | 0.71250 | 6 | 1 |


| No. | $Z_{\text {substrate }}$ | Mass thickness <br> $\left(\mu \mathrm{g} \mathrm{cm}^{-2}\right)$ | $k(A \mid K \alpha)$ | $k$ (substrate) | Accelerating <br> voltage $(\mathrm{kV})$ | Substrate lin |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 688 | 40 | 13.80 | 0.12316 | 0.80580 | 8 | 1 |
| 689 | 40 | 13.80 | 0.08308 | 0.87390 | 10 | 1 |
| 690 | 40 | 13.80 | 0.05782 | 0.88920 | 12 | 1 |
| 691 | 40 | 13.80 | 0.03933 | 0.92260 | 15 | 1 |
| 692 | 40 | 13.80 | 0.02430 | 0.95220 | 20 | 1 |
| 693 | 40 | 13.80 | 0.01811 | 0.95710 | 25 | 1 |
| 694 | 40 | 13.80 | 0.01375 | 0.95400 | 30 | 1 |
| 695 | 40 | 24.90 | 0.80654 | 0.16580 | 4 | 1 |
| 696 | 40 | 24.90 | 0.41912 | 0.52560 | 6 | 1 |
| 697 | 40 | 24.90 | 0.24331 | 0.69180 | 8 | 1 |
| 698 | 40 | 24.90 | 0.15909 | 0.79780 | 10 | 1 |
| 699 | 40 | 24.90 | 0.11094 | 0.82590 | 12 | 1 |
| 700 | 40 | 24.90 | 0.07749 | 0.87420 | 15 | 1 |
| 701 | 40 | 24.90 | 0.04572 | 0.89720 | 20 | 1 |
| 702 | 40 | 24.90 | 0.03302 | 0.90640 | 25 | 1 |
| 703 | 40 | 24.90 | 0.02580 | 0.91350 | 30 | 1 |
| 704 | 40 | 49.20 | 0.75257 | 0.21960 | 6 | 1 |
| 705 | 40 | 49.20 | 0.48325 | 0.45830 | 8 | 1 |
| 706 | 40 | 49.20 | 0.32296 | 0.60770 | 10 | 1 |
| 707 | 40 | 49.20 | 0.22848 | 0.68550 | 12 | 1 |
| 708 | 40 | 49.20 | 0.15386 | 0.75850 | 15 | 1 |
| 709 | 40 | 49.20 | 0.09228 | 0.81150 | 20 | 1 |
| 710 | 40 | 49.20 | 0.06784 | 0.83680 | 25 | 1 |
| 711 | 40 | 49.20 | 0.05287 | 0.84970 | 30 | 1 |
| 712 | 40 | 85.40 | 0.98987 | 0.03500 | 6 | 1 |
| 713 | 40 | 85.40 | 0.78718 | 0.19910 | 8 | 1 |
| 714 | 40 | 85.40 | 0.56787 | 0.37090 | 10 | 1 |
| 715 | 40 | 85.40 | 0.42383 | 0.48830 | 12 | 1 |
| 716 | 40 | 85.40 | 0.29511 | 0.60050 | 15 | 1 |
| 717 | 40 | 85.40 | 0.16915 | 0.69700 | 20 | 1 |
| 718 | 40 | 85.40 | 0.12714 | 0.72960 | 25 | 1 |
| 719 | 40 | 85.40 | 0.09498 | 0.74150 | 30 | 1 |
| 720 | 42 | 3.55 | 0.26392 | - | 3 | 1 |
| 721 | 42 | 3.55 | 0.12690 | 0.75760 | 4 | 1 |
| 722 | 42 | 3.55 | 0.05420 | 0.89775 | 6 | 1 |
| 723 | 42 | 3.55 | 0.03101 | 0.95313 | 8 | 1 |
| 724 | 42 | 3.55 | 0.02060 | 0.96561 | 10 | 1 |
| 725 | 42 | 3.55 | 0.01446 | 0.97440 | 12 | 1 |
| 726 | 42 | 3.55 | 0.00985 | 0.98619 | 15 | 1 |
| 727 | 42 | 3.55 | 0.00638 | 0.99148 | 20 | 1 |
| 728 | 42 | 3.55 | 0.00455 | 0.99471 | 25 | 1 |
| 729 | 42 | 3.55 | 0.00347 | 0.98904 | 30 | 1 |
| 730 | 42 | 7.04 | 0.25158 | 0.59394 | 4 | 1 |
| 731 | 42 | 7.04 | 0.11266 | 0.81617 | 6 | 1 |
| 732 | 42 | 7.04 | 0.06234 | 0.91305 | 8 | 1 |
| 733 | 42 | 7.04 | 0.04041 | 0.93440 | 10 | 1 |
| 734 | 42 | 7.04 | 0.02909 | 0.95384 | 12 | 1 |
| 735 | 42 | 7.04 | 0.01957 | 0.97092 | 15 | 1 |
| 736 | 42 | 7.04 | 0.01202 | 0.99236 | 20 | 1 |
| 737 | 42 | 7.04 | 0.00851 | 0.98509 | 25 | 1 |
| 738 | 42 | 7.04 | 0.00685 | 0.98915 | 30 | 1 |
| 739 | 42 | 13.80 | 0.49466 | 0.39323 | 4 | 1 |
| 740 | 42 | 13.80 | 0.23088 | 0.73573 | 6 | 1 |
| 741 | 42 | 13.80 | 0.12564 | 0.86316 | 8 | 1 |
| 742 | 42 | 13.80 | 0.08322 | 0.90646 | 10 | 1 |
| 743 | 42 | 13.80 | 0.05820 | 0.92300 | 12 | 1 |
| 744 | 42 | 13.80 | 0.04025 | 0.94704 | 15 | 1 |
| 745 | 42 | 13.80 | 0.02402 | 0.96127 | 20 | 1 |
| 746 | 42 | 13.80 | 0.01794 | 0.96348 | 25 | 1 |
| 747 | 42 | 13.80 | 0.01370 | 0.96221 | 30 | 1 |
| 748 | 42 | 24.90 | 0.80792 | 0.13587 | 4 | 1 |
| 749 | 42 | 24.90 | 0.41974 | 0.53560 | 6 | 1 |
| 750 | 42 | 24.90 | 0.24925 | 0.73172 | 8 | 1 |
| 751 | 42 | 24.90 | 0.16034 | 0.81705 | 10 | 1 |
| 752 | 42 | 24.90 | 0.11267 | 0.86367 | 12 | 1 |
| 753 | 42 | 24.90 | 0.07780 | 0.90203 | 15 | 1 |
| 754 | 42 | 24.90 | 0.04623 | 0.92913 | 20 | 1 |
| 755 | 42 | 24.90 | 0.03316 | 0.93528 | 25 | 1 |


| No. | $z_{\text {substrate }}$ | Mass thickness <br> $\left(\mu \mathrm{g} \mathrm{cm} \mathrm{cm}^{-2}\right)$ | $k(A \mid K \alpha)$ | $k$ (substrate) | Accelerating <br> voltage (kV) | Substrate I |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 756 | 42 | 24.90 | 0.02517 | 0.93495 | 30 | 1 |
| 757 | 42 | 49.20 | 0.75868 | 0.22365 | 6 | 1 |
| 758 | 42 | 49.20 | 0.48500 | 0.49811 | 8 | 1 |
| 759 | 42 | 49.20 | 0.32780 | 0.64294 | 10 | 1 |
| 760 | 42 | 49.20 | 0.22668 | 0.72806 | 12 | 1 |
| 761 | 42 | 49.20 | 0.15262 | 0.79890 | 15 | 1 |
| 762 | 42 | 49.20 | 0.09422 | 0.85791 | 20 | 1 |
| 763 | 42 | 49.20 | 0.06801 | 0.87075 | 25 | 1 |
| 764 | 42 | 49.20 | 0.05279 | 0.87671 | 30 | 1 |
| 765 | 42 | 85.40 | 0.99469 | - | 6 | 1 |
| 766 | 42 | 85.40 | 0.79137 | 0.22597 | 8 | 1 |
| 767 | 42 | 85.40 | 0.56563 | 0.40598 | 10 | 1 |
| 768 | 42 | 85.40 | 0.42250 | 0.53971 | 12 | 1 |
| 769 | 42 | 85.40 | 0.29671 | 0.65725 | 15 | 1 |
| 770 | 42 | 85.40 | 0.17396 | 0.75281 | 20 | 1 |
| 771 | 42 | 85.40 | 0.12771 | 0.79795 | 25 | 1 |
| 772 | 42 | 85.40 | 0.09543 | 0.80574 | 30 | 1 |
| 773 | 44 | 3.55 | 0.27436 | - | 3 | 1 |
| 774 | 44 | 3.55 | 0.13065 | - | 4 | 1 |
| 775 | 44 | 3.55 | 0.05629 | - | 6 | 1 |
| 776 | 44 | 3.55 | 0.03168 | - | 8 | 1 |
| 777 | 44 | 3.55 | 0.02068 | - | 10 | 1 |
| 778 | 44 | 3.55 | 0.01459 | - | 12 | 1 |
| 779 | 44 | 3.55 | 0.00995 | - | 15 | 1 |
| 780 | 44 | 3.55 | 0.00637 | - | 20 | 1 |
| 781 | 44 | 3.55 | 0.00455 | - | 25 | 1 |
| 782 | 44 | 3.55 | 0.00345 | - | 30 | 1 |
| 783 | 44 | 7.04 | 0.25913 | - | 4 | 1 |
| 784 | 44 | 7.04 | 0.11623 | - | 6 | 1 |
| 785 | 44 | 7.04 | 0.06474 | - | 8 | 1 |
| 786 | 44 | 7.04 | 0.04116 | - | 10 | 1 |
| 787 | 44 | 7.04 | 0.03025 | - | 12 | 1 |
| 788 | 44 | 7.04 | 0.02032 | - | 15 | 1 |
| 789 | 44 | 7.04 | 0.01225 | - | 20 | 1 |
| 790 | 44 | 7.04 | 0.00876 | - | 25 | 1 |
| 791 | 44 | 7.04 | 0.00695 | - | 30 | 1 |
| 792 | 44 | 13.80 | 0.50892 | - | 4 | 1 |
| 793 | 44 | 13.80 | 0.23705 | - | 6 | 1 |
| 794 | 44 | 13.80 | 0.12598 | - | 8 | 1 |
| 795 | 44 | 13.80 | 0.08416 | - | 10 | 1 |
| 796 | 44 | 13.80 | 0.06028 | - | 12 | 1 |
| 797 | 44 | 13.80 | 0.03999 | - | 15 | 1 |
| 798 | 44 | 13.80 | 0.02468 | - | 20 | 1 |
| 799 | 44 | 13.80 | 0.01817 | - | 25 | 1 |
| 800 | 44 | 13.80 | 0.01383 | - | 30 | 1 |
| 801 | 44 | 24.90 | 0.81956 | - | 4 | 1 |
| 802 | 44 | 24.90 | 0.43152 | - | 6 | 1 |
| 803 | 44 | 24.90 | 0.25087 | - | 8 | 1 |
| 804 | 44 | 24.90 | 0.16510 | - | 10 | 1 |
| 805 | 44 | 24.90 | 0.11256 | - | 12 | 1 |
| 806 | 44 | 24.90 | 0.07817 | - | 15 | 1 |
| 807 | 44 | 24.90 | 0.04588 | - | 20 | 1 |
| 808 | 44 | 24.90 | 0.03277 | - | 25 | 1 |
| 809 | 44 | 24.90 | 0.02572 | - | 30 | 1 |
| 810 | 44 | 49.20 | 0.77019 | - | 6 | 1 |
| 811 | 44 | 49.20 | 0.48798 | - | 8 | 1 |
| 812 | 44 | 49.20 | 0.32870 | - | 10 | 1 |
| 813 | 44 | 49.20 | 0.23565 | - | 12 | 1 |
| 814 | 44 | 49.20 | 0.15851 | - | 15 | 1 |
| 815 | 44 | 49.20 | 0.09665 | - | 20 | 1 |
| 816 | 44 | 49.20 | 0.06816 | - | 25 | 1 |
| 817 | 44 | 49.20 | 0.05323 | - | 30 | 1 |
| 818 | 44 | 85.40 | 0.98348 | - | 6 | 1 |
| 819 | 44 | 85.40 | 0.79878 | - | 8 | 1 |
| 820 | 44 | 85.40 | 0.57168 | - | 10 | 1 |
| 821 | 44 | 85.40 | 0.42853 | - | 12 | 1 |
| 822 | 44 | 85.40 | 0.30092 | - | 15 | 1 |
| 823 | 44 | 85.40 | 0.18039 | - | 20 | 1 |


| No. | $Z_{\text {substrate }}$ | Mass thickness <br> $\left(\mu \mathrm{g} \mathrm{cm}^{-2}\right)$ | $k(\mathrm{~A} \mid \mathrm{K} \alpha)$ | $k$ (substrate) | Accelerating <br> voltage $(\mathrm{kV})$ | Substrate line |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 824 | 44 | 85.40 | 0.12821 | - | 25 | 1 |
| 825 | 44 | 85.40 | 0.09617 | - | 30 | 1 |
| 826 | 46 | 3.55 | 0.27122 | - | 3 | 1 |
| 827 | 46 | 3.55 | 0.12934 | 0.69041 | 4 | 1 |
| 828 | 46 | 3.55 | 0.05583 | 0.88064 | 6 | 1 |
| 829 | 46 | 3.55 | 0.03129 | 0.92621 | 8 | 1 |
| 830 | 46 | 3.55 | 0.02068 | 0.96125 | 10 | 1 |
| 831 | 46 | 3.55 | 0.01420 | 0.96319 | 12 | 1 |
| 832 | 46 | 3.55 | 0.00983 | 0.97579 | 15 | 1 |
| 833 | 46 | 3.55 | 0.00620 | 0.96861 | 20 | 1 |
| 834 | 46 | 3.55 | 0.00432 | 0.97407 | 25 | 1 |
| 835 | 46 | 3.55 | 0.00335 | 0.98934 | 30 | 1 |
| 836 | 46 | 7.04 | 0.25133 | 0.51512 | 4 | 1 |
| 837 | 46 | 7.04 | 0.11336 | 0.79778 | 6 | 1 |
| 838 | 46 | 7.04 | 0.06332 | 0.87014 | 8 | 1 |
| 839 | 46 | 7.04 | 0.04107 | 0.93024 | 10 | 1 |
| 840 | 46 | 7.04 | 0.02929 | 0.93975 | 12 | 1 |
| 841 | 46 | 7.04 | 0.01989 | 0.97483 | 15 | 1 |
| 842 | 46 | 7.04 | 0.01196 | 0.97966 | 20 | 1 |
| 843 | 46 | 7.04 | 0.00842 | 0.97629 | 25 | 1 |
| 844 | 46 | 7.04 | 0.00676 | 0.99365 | 30 | 1 |
| 845 | 46 | 13.80 | 0.50422 | 0.25224 | 4 | 1 |
| 846 | 46 | 13.80 | 0.23558 | 0.70253 | 6 | 1 |
| 847 | 46 | 13.80 | 0.12660 | 0.82163 | 8 | 1 |
| 848 | 46 | 13.80 | 0.08485 | 0.90280 | 10 | 1 |
| 849 | 46 | 13.80 | 0.05991 | 0.91574 | 12 | 1 |
| 850 | 46 | 13.80 | 0.04103 | 0.93687 | 15 | 1 |
| 851 | 46 | 13.80 | 0.02437 | 0.94595 | 20 | 1 |
| 852 | 46 | 13.80 | 0.01800 | 0.95739 | 25 | 1 |
| 853 | 46 | 13.80 | 0.01384 | 0.97235 | 30 | 1 |
| 854 | 46 | 24.90 | 0.81642 | 0.05594 | 4 | 1 |
| 855 | 46 | 24.90 | 0.42516 | 0.50095 | 6 | 1 |
| 856 | 46 | 24.90 | 0.24858 | 0.71124 | 8 | 1 |
| 857 | 46 | 24.90 | 0.16303 | 0.83757 | 10 | 1 |
| 858 | 46 | 24.90 | 0.11492 | 0.87670 | 12 | 1 |
| 859 | 46 | 24.90 | 0.07775 | 0.91406 | 15 | 1 |
| 860 | 46 | 24.90 | 0.04543 | 0.92447 | 20 | 1 |
| 861 | 46 | 24.90 | 0.03365 | 0.94507 | 25 | 1 |
| 862 | 46 | 24.90 | 0.02555 | 0.96059 | 30 | 1 |
| 863 | 46 | 49.20 | 0.75683 | 0.18682 | 6 | 1 |
| 864 | 46 | 49.20 | 0.49126 | 0.48034 | 8 | 1 |
| 865 | 46 | 49.20 | 0.33152 | 0.67516 | 10 | 1 |
| 866 | 46 | 49.20 | 0.23352 | 0.74883 | 12 | 1 |
| 867 | 46 | 49.20 | 0.15600 | 0.83430 | 15 | 1 |
| 868 | 46 | 49.20 | 0.09696 | 0.87311 | 20 | 1 |
| 869 | 46 | 49.20 | 0.06876 | 0.90872 | 25 | 1 |
| 870 | 46 | 49.20 | 0.05318 | 0.93068 | 30 | 1 |
| 871 | 46 | 85.40 | 0.98271 | - | 6 | 1 |
| 872 | 46 | 85.40 | 0.78414 | 0.20242 | 8 | 1 |
| 873 | 46 | 85.40 | 0.56459 | 0.41761 | 10 | 1 |
| 874 | 46 | 85.40 | 0.42340 | 0.56498 | 12 | 1 |
| 875 | 46 | 85.40 | 0.30022 | 0.70116 | 15 | 1 |
| 876 | 46 | 85.40 | 0.18183 | 0.79555 | 20 | 1 |
| 877 | 46 | 85.40 | 0.12968 | 0.83963 | 25 | 1 |
| 878 | 46 | 85.40 | 0.09742 | 0.85919 | 30 | 1 |
| 879 | 50 | 3.55 | 0.26654 | - | 3 | 1 |
| 880 | 50 | 3.55 | 0.12956 | - | 4 | 1 |
| 881 | 50 | 3.55 | 0.05588 | 0.82236 | 6 | 1 |
| 882 | 50 | 3.55 | 0.03152 | 0.90555 | 8 | 1 |
| 883 | 50 | 3.55 | 0.02059 | 0.92986 | 10 | 1 |
| 884 | 50 | 3.55 | 0.01471 | 0.93743 | 12 | 1 |
| 885 | 50 | 3.55 | 0.01031 | 0.95167 | 15 | 1 |
| 886 | 50 | 3.55 | 0.00660 | 0.96578 | 20 | 1 |
| 887 | 50 | 3.55 | 0.00464 | 0.97362 | 25 | 1 |
| 888 | 50 | 3.55 | 0.00341 | 0.98990 | 30 | 1 |
| 889 | 50 | 7.04 | 0.25584 | - | 4 | 1 |
| 890 | 50 | 7.04 | 0.11594 | 0.74884 | 6 | 1 |
| 891 | 50 | 7.04 | 0.06472 | 0.85336 | 8 | 1 |


| No. | $Z_{\text {substrate }}$ | Mass thickness <br> $\left(\mu \mathrm{g} \mathrm{cm}^{-2}\right)$ | $k(\mathrm{~A} \mid \mathrm{K} \alpha)$ | $k$ (substrate) | Accelerating <br> voltage $(\mathrm{kV})$ | Substrate line |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 892 | 50 | 7.04 | 0.04126 | 0.88861 | 10 | 1 |
| 893 | 50 | 7.04 | 0.02969 | 0.92168 | 12 | 1 |
| 894 | 50 | 7.04 | 0.02057 | 0.94272 | 15 | 1 |
| 895 | 50 | 7.04 | 0.01260 | 0.95546 | 20 | 1 |
| 896 | 50 | 7.04 | 0.00907 | 0.96824 | 25 | 1 |
| 897 | 50 | 7.04 | 0.00698 | 0.98159 | 30 | 1 |
| 898 | 50 | 13.80 | 0.50416 | - | 4 | 1 |
| 899 | 50 | 13.80 | 0.23708 | 0.59419 | 6 | 1 |
| 900 | 50 | 13.80 | 0.12804 | 0.80121 | 8 | 1 |
| 901 | 50 | 13.80 | 0.08573 | 0.83904 | 10 | 1 |
| 902 | 50 | 13.80 | 0.06008 | 0.89992 | 12 | 1 |
| 903 | 50 | 13.80 | 0.04124 | 0.92400 | 15 | 1 |
| 904 | 50 | 13.80 | 0.02447 | 0.94523 | 20 | 1 |
| 905 | 50 | 13.80 | 0.01838 | 0.95999 | 25 | 1 |
| 906 | 50 | 13.80 | 0.01414 | 0.97494 | 30 | 1 |
| 907 | 50 | 24.90 | 0.81764 | - | 4 | 1 |
| 908 | 50 | 24.90 | 0.43128 | 0.40265 | 6 | 1 |
| 909 | 50 | 24.90 | 0.25004 | 0.66827 | 8 | 1 |
| 910 | 50 | 24.90 | 0.16597 | 0.78642 | 10 | 1 |
| 911 | 50 | 24.90 | 0.11766 | 0.86025 | 12 | 1 |
| 912 | 50 | 24.90 | 0.07947 | 0.89165 | 15 | 1 |
| 913 | 50 | 24.90 | 0.04667 | 0.92186 | 20 | 1 |
| 914 | 50 | 24.90 | 0.03366 | 0.95089 | 25 | 1 |
| 915 | 50 | 24.90 | 0.02755 | 0.96763 | 30 | 1 |
| 916 | 50 | 49.20 | 0.75981 | 0.11597 | 6 | 1 |
| 917 | 50 | 49.20 | 0.49385 | 0.42023 | 8 | 1 |
| 918 | 50 | 49.20 | 0.33888 | 0.59281 | 10 | 1 |
| 919 | 50 | 49.20 | 0.23662 | 0.71910 | 12 | 1 |
| 920 | 50 | 49.20 | 0.16276 | 0.79539 | 15 | 1 |
| 921 | 50 | 49.20 | 0.09747 | 0.87948 | 20 | 1 |
| 922 | 50 | 49.20 | 0.06943 | 0.91038 | 25 | 1 |
| 923 | 50 | 49.20 | 0.05405 | 0.93791 | 30 | 1 |
| 924 | 50 | 85.40 | 0.98791 | 0.01060 | 6 | 1 |
| 925 | 50 | 85.40 | 0.79347 | 0.17341 | 8 | 1 |
| 926 | 50 | 85.40 | 0.57306 | 0.38589 | 10 | 1 |
| 927 | 50 | 85.40 | 0.43071 | 0.55331 | 12 | 1 |
| 928 | 50 | 85.40 | 0.30611 | 0.69927 | 15 | 1 |
| 929 | 50 | 85.40 | 0.18653 | 0.81229 | 20 | 1 |
| 930 | 50 | 85.40 | 0.13216 | 0.87045 | 25 | 1 |
| 931 | 50 | 85.40 | 0.10233 | 0.90615 | 30 | 1 |
| 932 | 72 | 3.55 | 0.27510 | - | 3 | 2 |
| 933 | 72 | 3.55 | 0.13310 | - | 4 | 2 |
| 934 | 72 | 3.55 | 0.05782 | - | 6 | 2 |
| 935 | 72 | 3.55 | 0.03336 | - | 8 | 2 |
| 936 | 72 | 3.55 | 0.02213 | - | 10 | 2 |
| 937 | 72 | 3.55 | 0.01582 | - | 12 | 2 |
| 938 | 72 | 3.55 | 0.01075 | - | 15 | 2 |
| 939 | 72 | 3.55 | 0.00686 | - | 20 | 2 |
| 940 | 72 | 3.55 | 0.00485 | - | 25 | 2 |
| 941 | 72 | 3.55 | 0.00362 | - | 30 | 2 |
| 942 | 72 | 7.04 | 0.27060 | - | 4 | 2 |
| 943 | 72 | 7.04 | 0.11973 | - | 6 | 2 |
| 944 | 72 | 7.04 | 0.06808 | - | 8 | 2 |
| 945 | 72 | 7.04 | 0.04408 | - | 10 | 2 |
| 946 | 72 | 7.04 | 0.03167 | - | 12 | 2 |
| 947 | 72 | 7.04 | 0.02159 | - | 15 | 2 |
| 948 | 72 | 7.04 | 0.01345 | - | 20 | 2 |
| 949 | 72 | 7.04 | 0.00959 | - | 25 | 2 |
| 950 | 72 | 7.04 | 0.00722 | - | 30 | 2 |
| 951 | 72 | 13.80 | 0.51252 | - | 4 | 2 |
| 952 | 72 | 13.80 | 0.24728 | - | 6 | 2 |
| 953 | 72 | 13.80 | 0.13910 | - | 8 | 2 |
| 954 | 72 | 13.80 | 0.09128 | - | 10 | 2 |
| 955 | 72 | 13.80 | 0.06482 | - | 12 | 2 |
| 956 | 72 | 13.80 | 0.04409 | - | 15 | 2 |
| 957 | 72 | 13.80 | 0.02653 | - | 20 | 2 |
| 958 | 72 | 13.80 | 0.01977 | - | 25 | 2 |
| 959 | 72 | 13.80 | 0.01512 | - | 30 | 2 |


| No. | $Z_{\text {substrate }}$ | Mass thickness <br> $\left(\mu \mathrm{g} \mathrm{cm}^{-2}\right)$ | $k(\mathrm{~A} \mid \mathrm{K} \alpha)$ | k (substrate) | Accelerating <br> voltage $(\mathrm{kV})$ | Substrate line |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 960 | 72 | 24.90 | 0.83198 | - | 4 | 2 |
| 961 | 72 | 24.90 | 0.44830 | - | 6 | 2 |
| 962 | 72 | 24.90 | 0.26790 | - | 8 | 2 |
| 963 | 72 | 24.90 | 0.17643 | - | 10 | 2 |
| 964 | 72 | 24.90 | 0.12531 | - | 12 | 2 |
| 965 | 72 | 24.90 | 0.08516 | - | 15 | 2 |
| 966 | 72 | 24.90 | 0.04988 | - | 20 | 2 |
| 967 | 72 | 24.90 | 0.03607 | - | 25 | 2 |
| 968 | 72 | 24.90 | 0.02819 | - | 30 | 2 |
| 969 | 72 | 49.20 | 0.77723 | - | 6 | 2 |
| 970 | 72 | 49.20 | 0.51799 | - | 8 | 2 |
| 971 | 72 | 49.20 | 0.35418 | - | 10 | 2 |
| 972 | 72 | 49.20 | 0.25246 | - | 12 | 2 |
| 973 | 72 | 49.20 | 0.17611 | - | 15 | 2 |
| 974 | 72 | 49.20 | 0.10554 | - | 20 | 2 |
| 975 | 72 | 49.20 | 0.07483 | - | 25 | 2 |
| 976 | 72 | 49.20 | 0.05818 | - | 30 | 2 |
| 977 | 72 | 85.40 | 0.98338 | - | 6 | 2 |
| 978 | 72 | 85.40 | 0.80270 | - | 8 | 2 |
| 979 | 72 | 85.40 | 0.59334 | - | 10 | 2 |
| 980 | 72 | 85.40 | 0.45116 | - | 12 | 2 |
| 981 | 72 | 85.40 | 0.32736 | - | 15 | 2 |
| 982 | 72 | 85.40 | 0.19971 | - | 20 | 2 |
| 983 | 72 | 85.40 | 0.14092 | - | 25 | 2 |
| 984 | 72 | 85.40 | 0.10991 | - | 30 | 2 |
| 985 | 74 | 3.55 | 0.27770 | - | 3 | 2 |
| 986 | 74 | 3.55 | 0.13818 | 0.83888 | 4 | 2 |
| 987 | 74 | 3.55 | 0.05859 | 0.91928 | 6 | 2 |
| 988 | 74 | 3.55 | 0.03448 | 0.95856 | 8 | 2 |
| 989 | 74 | 3.55 | 0.02208 | 0.97188 | 10 | 2 |
| 990 | 74 | 3.55 | 0.01600 | 0.97863 | 12 | 2 |
| 991 | 74 | 3.55 | 0.01080 | 0.99768 | 15 | 2 |
| 992 | 74 | 3.55 | 0.00686 | 1.00478 | 20 | 2 |
| 993 | 74 | 3.55 | 0.00485 | 0.99779 | 25 | 2 |
| 994 | 74 | 3.55 | 0.00374 | 0.99354 | 30 | 2 |
| 995 | 74 | 3.55 | - | 0.93353 | 12 | 1 |
| 996 | 74 | 3.55 | - | 0.96911 | 15 | 1 |
| 997 | 74 | 3.55 | - | 0.98804 | 20 | 1 |
| 998 | 74 | 3.55 | - | 0.98065 | 25 | 1 |
| 999 | 74 | 3.55 | - | 1.00204 | 30 | 1 |
| 1000 | 74 | 7.04 | 0.26158 | 0.71677 | 4 | 2 |
| 1001 | 74 | 7.04 | 0.12147 | 0.85968 | 6 | 2 |
| 1002 | 74 | 7.04 | 0.06837 | 0.92176 | 8 | 2 |
| 1003 | 74 | 7.04 | 0.04437 | 0.96127 | 10 | 2 |
| 1004 | 74 | 7.04 | 0.03213 | 0.96503 | 12 | 2 |
| 1005 | 74 | 7.04 | 0.02198 | 0.97252 | 15 | 2 |
| 1006 | 74 | 7.04 | 0.01334 | 0.97797 | 20 | 2 |
| 1007 | 74 | 7.04 | 0.00957 | 0.97127 | 25 | 2 |
| 1008 | 74 | 7.04 | 0.00746 | 0.94785 | 30 | 2 |
| 1009 | 74 | 7.04 | - | 0.88842 | 12 | 1 |
| 1010 | 74 | 7.04 | - | 0.96578 | 15 | 1 |
| 1011 | 74 | 7.04 | - | 0.98724 | 20 | 1 |
| 1012 | 74 | 7.04 | - | 0.97999 | 25 | 1 |
| 1013 | 74 | 7.04 | - | 1.00377 | 30 | 1 |
| 1014 | 74 | 13.80 | 0.51178 | 0.45738 | 4 | 2 |
| 1015 | 74 | 13.80 | 0.24758 | 0.74233 | 6 | 2 |
| 1016 | 74 | 13.80 | 0.13942 | 0.85120 | 8 | 2 |
| 1017 | 74 | 13.80 | 0.09058 | 0.90015 | 10 | 2 |
| 1018 | 74 | 13.80 | 0.06396 | 0.91240 | 12 | 2 |
| 1019 | 74 | 13.80 | 0.04454 | 0.92667 | 15 | 2 |
| 1020 | 74 | 13.80 | 0.02619 | 0.93300 | 20 | 2 |
| 1021 | 74 | 13.80 | 0.01957 | 0.91976 | 25 | 2 |
| 1022 | 74 | 13.80 | 0.01508 | 0.91406 | 30 | 2 |
| 1023 | 74 | 13.80 | - | 0.80056 | 12 | 1 |
| 1024 | 74 | 13.80 | - | 0.92794 | 15 | 1 |
| 1025 | 74 | 13.80 | - | 0.97413 | 20 | 1 |
| 1026 | 74 | 13.80 | - | 0.97793 | 25 | 1 |
| 1027 | 74 | 13.80 | - | 0.99211 | 30 | 1 |


| No. | $Z_{\text {substrate }}$ | Mass thickness <br> $\left(\mu \mathrm{g} \mathrm{cm}{ }^{-2}\right)$ | $k(\mathrm{~A} \mid \mathrm{K} \alpha)$ | $k$ (substrate) | Accelerating <br> voltage $(\mathrm{kV})$ | Substrate line |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1028 | 74 | 24.90 | 0.81579 | 0.20594 | 4 | 2 |
| 1029 | 74 | 24.90 | 0.44546 | 0.56021 | 6 | 2 |
| 1030 | 74 | 24.90 | 0.26424 | 0.72687 | 8 | 2 |
| 1031 | 74 | 24.90 | 0.17422 | 0.81932 | 10 | 2 |
| 1032 | 74 | 24.90 | 0.12333 | 0.84299 | 12 | 2 |
| 1033 | 74 | 24.90 | 0.08399 | 0.87516 | 15 | 2 |
| 1034 | 74 | 24.90 | 0.04902 | 0.89553 | 20 | 2 |
| 1035 | 74 | 24.90 | 0.03564 | 0.88241 | 25 | 2 |
| 1036 | 74 | 24.90 | 0.02890 | 0.89058 | 30 | 2 |
| 1037 | 74 | 24.90 | - | 0.66753 | 12 | 1 |
| 1038 | 74 | 24.90 | - | 0.87677 | 15 | 1 |
| 1039 | 74 | 24.90 | - | 0.94722 | 20 | 1 |
| 1040 | 74 | 24.90 | - | 0.96684 | 25 | 1 |
| 1041 | 74 | 24.90 | - | 0.98918 | 30 | 1 |
| 1042 | 74 | 49.20 | 0.77260 | 0.24310 | 6 | 2 |
| 1043 | 74 | 49.20 | 0.51181 | 0.47747 | 8 | 2 |
| 1044 | 74 | 49.20 | 0.35923 | 0.61869 | 10 | 2 |
| 1045 | 74 | 49.20 | 0.25578 | 0.68521 | 12 | 2 |
| 1046 | 74 | 49.20 | 0.17934 | 0.74526 | 15 | 2 |
| 1047 | 74 | 49.20 | 0.10410 | 0.78880 | 20 | 2 |
| 1048 | 74 | 49.20 | 0.07483 | 0.79064 | 25 | 2 |
| 1049 | 74 | 49.20 | 0.05818 | 0.78084 | 30 | 2 |
| 1050 | 74 | 49.20 | - | 0.41900 | 12 | 1 |
| 1051 | 74 | 49.20 | - | 0.75840 | 15 | 1 |
| 1052 | 74 | 49.20 | - | 0.89708 | 20 | 1 |
| 1053 | 74 | 49.20 | - | 0.94181 | 25 | 1 |
| 1054 | 74 | 49.20 | - | 0.96860 | 30 | 1 |
| 1055 | 74 | 85.40 | 0.97928 | 0.04094 | 6 | 2 |
| 1056 | 74 | 85.40 | 0.79320 | 0.19832 | 8 | 2 |
| 1057 | 74 | 85.40 | 0.58398 | 0.36784 | 10 | 2 |
| 1058 | 74 | 85.40 | 0.45547 | 0.46943 | 12 | 2 |
| 1059 | 74 | 85.40 | 0.32513 | 0.56642 | 15 | 2 |
| 1060 | 74 | 85.40 | 0.19787 | 0.64344 | 20 | 2 |
| 1061 | 74 | 85.40 | 0.14145 | 0.66522 | 25 | 2 |
| 1062 | 74 | 85.40 | 0.10911 | 0.66965 | 30 | 2 |
| 1063 | 74 | 85.40 | - | 0.17018 | 12 | 1 |
| 1064 | 74 | 85.40 | - | 0.57438 | 15 | 1 |
| 1065 | 74 | 85.40 | - | 0.81220 | 20 | 1 |
| 1066 | 74 | 85.40 | - | 0.88889 | 25 | 1 |
| 1067 | 74 | 85.40 | - | 0.92729 | 30 | 1 |
| 1068 | 78 | 3.55 | 0.27216 | - | 3 | 2 |
| 1069 | 78 | 3.55 | 0.13914 | - | 4 | 2 |
| 1070 | 78 | 3.55 | 0.05871 | - | 6 | 2 |
| 1071 | 78 | 3.55 | 0.03410 | - | 8 | 2 |
| 1072 | 78 | 3.55 | 0.02268 | - | 10 | 2 |
| 1073 | 78 | 3.55 | 0.01609 | - | 12 | 2 |
| 1074 | 78 | 3.55 | 0.01113 | - | 15 | 2 |
| 1075 | 78 | 3.55 | 0.00697 | - | 20 | 2 |
| 1076 | 78 | 3.55 | 0.00502 | - | 25 | 2 |
| 1077 | 78 | 3.55 | 0.00383 | - | 30 | 2 |
| 1078 | 78 | 7.04 | 0.26509 | - | 4 | 2 |
| 1079 | 78 | 7.04 | 0.12267 | - | 6 | 2 |
| 1080 | 78 | 7.04 | 0.06866 | - | 8 | 2 |
| 1081 | 78 | 7.04 | 0.04499 | - | 10 | 2 |
| 1082 | 78 | 7.04 | 0.03245 | - | 12 | 2 |
| 1083 | 78 | 7.04 | 0.02215 | - | 15 | 2 |
| 1084 | 78 | 7.04 | 0.01353 | - | 20 | 2 |
| 1085 | 78 | 7.04 | 0.00979 | - | 25 | 2 |
| 1086 | 78 | 7.04 | 0.00759 | - | 30 | 2 |
| 1087 | 78 | 13.80 | 0.51778 | - | 4 | 2 |
| 1088 | 78 | 13.80 | 0.24770 | - | 6 | 2 |
| 1089 | 78 | 13.80 | 0.14008 | - | 8 | 2 |
| 1090 | 78 | 13.80 | 0.09246 | - | 10 | 2 |
| 1091 | 78 | 13.80 | 0.06515 | - | 12 | 2 |
| 1092 | 78 | 13.80 | 0.04445 | - | 15 | 2 |
| 1093 | 78 | 13.80 | 0.02669 | - | 20 | 2 |
| 1094 | 78 | 13.80 | 0.01999 | - | 25 | 2 |
| 1095 | 78 | 13.80 | 0.01547 | - | 30 | 2 |


| No. | $Z_{\text {substrate }}$ | Mass thickness <br> $\left(\mu \mathrm{g} \mathrm{cm}^{-2}\right)$ | $k(\mathrm{~A} \mid \mathrm{K} \alpha)$ | k (substrate) | Accelerating <br> voltage $(\mathrm{kV})$ | Substrate line |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1096 | 78 | 24.90 | 0.83290 | - | 4 | 2 |
| 1097 | 78 | 24.90 | 0.44936 | - | 6 | 2 |
| 1098 | 78 | 24.90 | 0.26587 | - | 8 | 2 |
| 1099 | 78 | 24.90 | 0.17827 | - | 10 | 2 |
| 1100 | 78 | 24.90 | 0.12688 | - | 12 | 2 |
| 1101 | 78 | 24.90 | 0.08658 | - | 15 | 2 |
| 1102 | 78 | 24.90 | 0.05152 | - | 20 | 2 |
| 1103 | 78 | 24.90 | 0.03695 | - | 25 | 2 |
| 1104 | 78 | 24.90 | 0.02864 | - | 30 | 2 |
| 1105 | 78 | 49.20 | 0.78130 | - | 6 | 2 |
| 1106 | 78 | 49.20 | 0.51946 | - | 8 | 2 |
| 1107 | 78 | 49.20 | 0.36380 | - | 10 | 2 |
| 1108 | 78 | 49.20 | 0.26161 | - | 12 | 2 |
| 1109 | 78 | 49.20 | 0.17734 | - | 15 | 2 |
| 1110 | 78 | 49.20 | 0.10651 | - | 20 | 2 |
| 1111 | 78 | 49.20 | 0.07611 | - | 25 | 2 |
| 1112 | 78 | 49.20 | 0.05836 | - | 30 | 2 |
| 1113 | 78 | 85.40 | 0.98166 | - | 6 | 2 |
| 1114 | 78 | 85.40 | 0.79338 | - | 8 | 2 |
| 1115 | 78 | 85.40 | 0.58898 | - | 10 | 2 |
| 1116 | 78 | 85.40 | 0.45892 | - | 12 | 2 |
| 1117 | 78 | 85.40 | 0.32829 | - | 15 | 2 |
| 1118 | 78 | 85.40 | 0.19913 | - | 20 | 2 |
| 1119 | 78 | 85.40 | 0.14283 | - | 25 | 2 |
| 1120 | 78 | 85.40 | 0.10989 | - | 30 | 2 |
| 1121 | 79 | 3.55 | 0.27688 | - | 3 | 2 |
| 1122 | 79 | 3.55 | 0.13914 | 0.80516 | 4 | 2 |
| 1123 | 79 | 3.55 | 0.05935 | 0.94024 | 6 | 2 |
| 1124 | 79 | 3.55 | 0.03414 | 0.98877 | 8 | 2 |
| 1125 | 79 | 3.55 | 0.02292 | 1.00272 | 10 | 2 |
| 1126 | 79 | 3.55 | 0.01616 | 0.99259 | 12 | 2 |
| 1127 | 79 | 3.55 | 0.01108 | 0.99331 | 15 | 2 |
| 1128 | 79 | 3.55 | 0.00704 | 1.00581 | 20 | 2 |
| 1129 | 79 | 3.55 | 0.00504 | 0.98497 | 25 | 2 |
| 1130 | 79 | 3.55 | 0.00379 | 0.99787 | 30 | 2 |
| 1131 | 79 | 3.55 | - | 0.91456 | 15 | 1 |
| 1132 | 79 | 3.55 | - | 0.99044 | 20 | 1 |
| 1133 | 79 | 3.55 | - | 0.98960 | 25 | 1 |
| 1134 | 79 | 3.55 | - | 1.00455 | 30 | 1 |
| 1135 | 79 | 7.04 | 0.26509 | 0.68384 | 4 | 2 |
| 1136 | 79 | 7.04 | 0.12283 | 0.85407 | 6 | 2 |
| 1137 | 79 | 7.04 | 0.06915 | 0.93866 | 8 | 2 |
| 1138 | 79 | 7.04 | 0.04581 | 0.94735 | 10 | 2 |
| 1139 | 79 | 7.04 | 0.03245 | 0.96770 | 12 | 2 |
| 1140 | 79 | 7.04 | 0.02215 | 0.96282 | 15 | 2 |
| 1141 | 79 | 7.04 | 0.01340 | 0.99125 | 20 | 2 |
| 1142 | 79 | 7.04 | 0.00979 | 0.96707 | 25 | 2 |
| 1143 | 79 | 7.04 | 0.00760 | 0.98649 | 30 | 2 |
| 1144 | 79 | 7.04 | - | 0.91106 | 15 | 1 |
| 1145 | 79 | 7.04 | - | 0.97840 | 20 | 1 |
| 1146 | 79 | 7.04 | - | 0.98593 | 25 | 1 |
| 1147 | 79 | 7.04 | - | 0.99691 | 30 | 1 |
| 1148 | 79 | 13.80 | 0.51400 | 0.43285 | 4 | 2 |
| 1149 | 79 | 13.80 | 0.24978 | 0.75303 | 6 | 2 |
| 1150 | 79 | 13.80 | 0.14099 | 0.88205 | 8 | 2 |
| 1151 | 79 | 13.80 | 0.09230 | 0.91696 | 10 | 2 |
| 1152 | 79 | 13.80 | 0.06478 | 0.93927 | 12 | 2 |
| 1153 | 79 | 13.80 | 0.04467 | 0.95280 | 15 | 2 |
| 1154 | 79 | 13.80 | 0.02689 | 0.97021 | 20 | 2 |
| 1155 | 79 | 13.80 | 0.02009 | 0.94365 | 25 | 2 |
| 1156 | 79 | 13.80 | 0.01554 | 0.95862 | 30 | 2 |
| 1157 | 79 | 13.80 | - | 0.87754 | 15 | 1 |
| 1158 | 79 | 13.80 | - | 0.96500 | 20 | 1 |
| 1159 | 79 | 13.80 | - | 0.97757 | 25 | 1 |
| 1160 | 79 | 13.80 | - | 0.99991 | 30 | 1 |
| 1161 | 79 | 24.90 | 0.82396 | 0.17062 | 4 | 2 |
| 1162 | 79 | 24.90 | 0.44922 | 0.57915 | 6 | 2 |
| 1163 | 79 | 24.90 | 0.26566 | 0.78082 | 8 | 2 |


| No. | $Z_{\text {substrate }}$ | Mass thickness <br> $\left(\mu \mathrm{g} \mathrm{cm}^{-2}\right)$ | $k(\mathrm{~A} \mid \mathrm{K} \alpha)$ | k (substrate) | Accelerating <br> voltage $(\mathrm{kV})$ | Substrate line |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1164 | 79 | 24.90 | 0.17975 | 0.85783 | 10 | 2 |
| 1165 | 79 | 24.90 | 0.12572 | 0.86525 | 12 | 2 |
| 1166 | 79 | 24.90 | 0.08578 | 0.91659 | 15 | 2 |
| 1167 | 79 | 24.90 | 0.05033 | 0.93643 | 20 | 2 |
| 1168 | 79 | 24.90 | 0.03626 | 0.91585 | 25 | 2 |
| 1169 | 79 | 24.90 | 0.02854 | 0.93679 | 30 | 2 |
| 1170 | 79 | 24.90 | - | 0.81161 | 15 | 1 |
| 1171 | 79 | 24.90 | - | 0.94061 | 20 | 1 |
| 1172 | 79 | 24.90 | - | 0.96398 | 25 | 1 |
| 1173 | 79 | 24.90 | - | 0.99351 | 30 | 1 |
| 1174 | 79 | 49.20 | 0.77628 | 0.23995 | 6 | 2 |
| 1175 | 79 | 49.20 | 0.51984 | 0.51384 | 8 | 2 |
| 1176 | 79 | 49.20 | 0.36265 | 0.66243 | 10 | 2 |
| 1177 | 79 | 49.20 | 0.25992 | 0.72299 | 12 | 2 |
| 1178 | 79 | 49.20 | 0.18200 | 0.79683 | 15 | 2 |
| 1179 | 79 | 49.20 | 0.10498 | 0.85078 | 20 | 2 |
| 1180 | 79 | 49.20 | 0.07617 | 0.83897 | 25 | 2 |
| 1181 | 79 | 49.20 | 0.05700 | 0.86510 | 30 | 2 |
| 1182 | 79 | 49.20 | - | 0.64187 | 15 | 1 |
| 1183 | 79 | 49.20 | - | 0.88481 | 20 | 1 |
| 1184 | 79 | 49.20 | - | 0.94215 | 25 | 1 |
| 1185 | 79 | 49.20 | - | 0.97066 | 30 | 1 |
| 1186 | 79 | 85.40 | 0.97780 | 0.04013 | 6 | 2 |
| 1187 | 79 | 85.40 | 0.79641 | 0.23740 | 8 | 2 |
| 1188 | 79 | 85.40 | 0.58660 | 0.42053 | 10 | 2 |
| 1189 | 79 | 85.40 | 0.45860 | 0.53788 | 12 | 2 |
| 1190 | 79 | 85.40 | 0.32861 | 0.65998 | 15 | 2 |
| 1191 | 79 | 85.40 | 0.19805 | 0.74521 | 20 | 2 |
| 1192 | 79 | 85.40 | 0.14259 | 0.76208 | 25 | 2 |
| 1193 | 79 | 85.40 | 0.11017 | 0.76851 | 30 | 2 |
| 1194 | 79 | 85.40 | - | 0.43504 | 15 | 1 |
| 1195 | 79 | 85.40 | - | 0.79330 | 20 | 1 |
| 1196 | 79 | 85.40 | - | 0.88851 | 25 | 1 |
| 1197 | 79 | 85.40 | - | 0.94852 | 30 | 1 |
| 1198 | 83 | 3.55 | 0.27697 | - | 3 | 2 |
| 1199 | 83 | 3.55 | 0.14542 | 0.69741 | 4 | 2 |
| 1200 | 83 | 3.55 | 0.05937 | 0.90320 | 6 | 2 |
| 1201 | 83 | 3.55 | 0.03488 | 0.94928 | 8 | 2 |
| 1202 | 83 | 3.55 | 0.02360 | 0.96350 | 10 | 2 |
| 1203 | 83 | 3.55 | 0.01666 | 0.97856 | 12 | 2 |
| 1204 | 83 | 3.55 | 0.01108 | 0.98195 | 15 | 2 |
| 1205 | 83 | 3.55 | 0.00703 | 0.98522 | 20 | 2 |
| 1206 | 83 | 3.55 | 0.00488 | 0.99811 | 25 | 2 |
| 1207 | 83 | 3.55 | 0.00387 | 0.99607 | 30 | 2 |
| 1208 | 83 | 3.55 | - | 0.93699 | 15 | 1 |
| 1209 | 83 | 3.55 | - | 0.96807 | 20 | 1 |
| 1210 | 83 | 3.55 | - | 0.99937 | 25 | 1 |
| 1211 | 83 | 3.55 | - | 0.98542 | 30 | 1 |
| 1212 | 83 | 7.04 | 0.27104 | 0.58641 | 4 | 2 |
| 1213 | 83 | 7.04 | 0.12345 | 0.85675 | 6 | 2 |
| 1214 | 83 | 7.04 | 0.07000 | 0.92134 | 8 | 2 |
| 1215 | 83 | 7.04 | 0.04543 | 0.94287 | 10 | 2 |
| 1216 | 83 | 7.04 | 0.03244 | 0.95824 | 12 | 2 |
| 1217 | 83 | 7.04 | 0.02242 | 0.95478 | 15 | 2 |
| 1218 | 83 | 7.04 | 0.01364 | 0.98135 | 20 | 2 |
| 1219 | 83 | 7.04 | 0.00975 | 0.99559 | 25 | 2 |
| 1220 | 83 | 7.04 | 0.00759 | 0.97883 | 30 | 2 |
| 1221 | 83 | 7.04 | - | 0.89982 | 15 | 1 |
| 1222 | 83 | 7.04 | - | 0.96399 | 20 | 1 |
| 1223 | 83 | 7.04 | - | 0.99001 | 25 | 1 |
| 1224 | 83 | 7.04 | - | 0.98620 | 30 | 1 |
| 1225 | 83 | 13.80 | 0.51922 | 0.34335 | 4 | 2 |
| 1226 | 83 | 13.80 | 0.25102 | 0.72360 | 6 | 2 |
| 1227 | 83 | 13.80 | 0.14138 | 0.86365 | 8 | 2 |
| 1228 | 83 | 13.80 | 0.09286 | 0.90252 | 10 | 2 |
| 1229 | 83 | 13.80 | 0.06551 | 0.92837 | 12 | 2 |
| 1230 | 83 | 13.80 | 0.04472 | 0.94910 | 15 | 2 |
| 1231 | 83 | 13.80 | 0.02703 | 0.95706 | 20 | 2 |


| No. | $Z_{\text {substrate }}$ | Mass thickness <br> $\left(\mu \mathrm{cm}^{-2}\right)$ | $k(\mathrm{~A} \mid \mathrm{K} \alpha)$ | k (substrate) | Accelerating <br> voltage $(\mathrm{kV})$ | Substrate line |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1232 | 83 | 13.80 | 0.02004 | 0.97920 | 25 | 2 |
| 1233 | 83 | 13.80 | 0.01543 | 0.98110 | 30 | 2 |
| 1234 | 83 | 13.80 | - | 0.81189 | 15 | 1 |
| 1235 | 83 | 13.80 | - | 0.94424 | 20 | 1 |
| 1236 | 83 | 13.80 | - | 0.98917 | 25 | 1 |
| 1237 | 83 | 13.80 | - | 0.97723 | 30 | 1 |
| 1238 | 83 | 24.90 | 0.81964 | 0.12205 | 4 | 2 |
| 1239 | 83 | 24.90 | 0.45268 | 0.55337 | 6 | 2 |
| 1240 | 83 | 24.90 | 0.26908 | 0.74913 | 8 | 2 |
| 1241 | 83 | 24.90 | 0.18131 | 0.83141 | 10 | 2 |
| 1242 | 83 | 24.90 | 0.12864 | 0.87177 | 12 | 2 |
| 1243 | 83 | 24.90 | 0.08744 | 0.91376 | 15 | 2 |
| 1244 | 83 | 24.90 | 0.05188 | 0.93655 | 20 | 2 |
| 1245 | 83 | 24.90 | 0.03727 | 0.95159 | 25 | 2 |
| 1246 | 83 | 24.90 | 0.02886 | 0.94426 | 30 | 2 |
| 1247 | 83 | 24.90 | - | 0.70546 | 15 | 1 |
| 1248 | 83 | 24.90 | - | 0.91168 | 20 | 1 |
| 1249 | 83 | 24.90 | - | 0.96633 | 25 | 1 |
| 1250 | 83 | 24.90 | - | 0.98093 | 30 | 1 |
| 1251 | 83 | 49.20 | 0.77970 | 0.22253 | 6 | 2 |
| 1252 | 83 | 49.20 | 0.52052 | 0.50142 | 8 | 2 |
| 1253 | 83 | 49.20 | 0.36346 | 0.66204 | 10 | 2 |
| 1254 | 83 | 49.20 | 0.26178 | 0.74585 | 12 | 2 |
| 1255 | 83 | 49.20 | 0.17878 | 0.83010 | 15 | 2 |
| 1256 | 83 | 49.20 | 0.10473 | 0.86324 | 20 | 2 |
| 1257 | 83 | 49.20 | 0.07596 | 0.90133 | 25 | 2 |
| 1258 | 83 | 49.20 | 0.05678 | 0.90511 | 30 | 2 |
| 1259 | 83 | 49.20 | - | 0.47338 | 15 | 1 |
| 1260 | 83 | 49.20 | - | 0.83610 | 20 | 1 |
| 1261 | 83 | 49.20 | - | 0.94454 | 25 | 1 |
| 1262 | 83 | 49.20 | - | 0.95228 | 30 | 1 |
| 1263 | 83 | 85.40 | 0.98018 | 0.03430 | 6 | 2 |
| 1264 | 83 | 85.40 | 0.79616 | 0.23011 | 8 | 2 |
| 1265 | 83 | 85.40 | 0.58993 | 0.42431 | 10 | 2 |
| 1266 | 83 | 85.40 | 0.45492 | 0.56593 | 12 | 2 |
| 1267 | 83 | 85.40 | 0.33000 | 0.69521 | 15 | 2 |
| 1268 | 83 | 85.40 | 0.19964 | 0.77948 | 20 | 2 |
| 1269 | 83 | 85.40 | 0.14284 | 0.83194 | 25 | 2 |
| 1270 | 83 | 85.40 | 0.11014 | 0.84449 | 30 | 2 |
| 1271 | 83 | 85.40 | - | 0.21649 | 15 | 1 |
| 1272 | 83 | 85.40 | - | 0.73280 | 20 | 1 |
| 1273 | 83 | 85.40 | - | 0.88332 | 25 | 1 |
| 1274 | 83 | 85.40 | - | 0.92594 | 30 | 1 |


[^0]:    * Correspondence to: G. F. Bastin, Laboratory of Solid State and Materials Chemistry, University of Technology, P.O. Box 513, NL-5600 MB Eindhoven, The Netherlands.

