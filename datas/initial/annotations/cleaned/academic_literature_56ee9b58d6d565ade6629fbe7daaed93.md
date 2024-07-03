# Estimating Reactivity Ratios From Triad Fraction Data 

Emma Hauch, Xiaoqin Zhou, Thomas A. Duever," Alexander Penlidis

Summary: Reactivity ratio estimation is a non-linear estimation problem. Typically, reactivity ratios are estimated using the instantaneous copolymer composition equation, otherwise known as the Mayo-Lewis model, based on low conversion $(<5 \%)$ copolymer composition data. However, there are other instantaneous models, which can be used to estimate reactivity ratios, such as the instantaneous triad fraction equations. The aim of this paper is to determine the potential improvement in reactivity ratio estimates when triad fraction data is used in place of and in combination with copolymer composition data. The interest in using triad fraction data in parameter estimation, stems from the fact that there are a greater number of responses measured (six triad fractions) compared to composition leading to data with theoretically more information content. In principle this should lead to reactivity ratio estimates having less uncertainty. In this study, the parameter estimates are obtained by employing the error in variables model (EVM), assuming a multiplicative error structure. Several case studies involving published literature data for different copolymer systems are presented. As the case studies demonstrate in general more precise estimates can be obtained from triad fraction data. Combining the triad fraction with composition data leads to little additional improvement. However, discrepancies arise between reactivity ratios estimated from composition data compared with those obtained from triad fraction data depending upon the copolymer system. Those copolymer systems exhibiting more heterogeneity due to phase separation during polymerization may be showing more discrepancy.

Keywords: copolymerization; error-in-variables model; radical polymerization; reactivity ratios; triad fractions

## Introduction

The justification of using the error in variables model (EVM) approach for parameter estimation, especially with respect to the reactivity ratio estimation problem in copolymerization, has been demonstrated extensively in the literature in the last twenty years or so. ${ }^{[1]}$ In the EVM framework, all variables (dependent and independent) are considered to be subject to error.

Typically, copolymerization reactivity ratios are estimated using the instantaneous[^0]

copolymer composition equation, based on low conversion ( $<5 \%$ ) copolymer composition data. ${ }^{[1,2,3]}$ Compared to methods using copolymer composition data, efforts to directly use triad fraction (sequence length) data for reactivity ratio estimation are far fewer. In part this is explained by the fact that it is more difficult to obtain triad fractions data. Table 1 gives a summary of a recent survey of the literature of papers that report triad fraction data.

In this paper case studies are reported for the systems acylamide/acylonitrile (AN), ${ }^{[30]}$ AN/acrylic acid (AA), ${ }^{[5]} \mathrm{AN} /$ pentyl-methacrylate (PMA), ${ }^{[4]}$ and finally for the system styrene (STY)/AN, and STY/ AN in toluene, ${ }^{[22,23,27]}$ Reactivity ratios are estimated using composition data, triad fraction data and a combination of the two.

Table 1.

Articles with triad fraction /sequence length data and reactivity ratio estimates

| Reference | Year | Method | Description |
| :---: | :---: | :---: | :---: |
| Brar and Dutta ${ }^{[4]}$ | 1998 | KT, EVM | AN-Pentyl methacrylate. |
| Brar and Dutta ${ }^{[5]}$ | 1998 | $\mathrm{KT}, \mathrm{EVM}$ | AN-AA. |
| Brar et al. ${ }^{[6]}$ | 1994 |  | AN-alkyl methacrylate. |
| Brar and Kaur ${ }^{[7]}$ | 2003 | KT, EVM | $\mathrm{N}$-vinylcarbazole and MMA. |
| Brar and Kaur ${ }^{[8]}$ | 2003 | KT, EVM | $\mathrm{N}$-vinylcarbazole and BMA. |
| Brar and Pradhan ${ }^{[9]}$ | 2003 |  | Terpolymer AN-STY-GMA. |
| Brar and Pradhan ${ }^{[10]}$ | 2003 |  | Terpolymer MAN-STY-MMA. |
| Brar et al. ${ }^{[1]}$ | 2003 | KT, EVM | NVP and MAN. |
| Brown and Fujimori ${ }^{[12]}$ | 1994 |  | STY with citraconic anhydride. |
| Burke et al. ${ }^{[13]^{\prime}}$ | 1994 | Box-Draper | STY-AN |
| de la Fuente et al. ${ }^{[14]}$ | 2001 |  | MMA and $B A ;$ sequence distribution. |
| Erol et al. ${ }^{[15]}$ | 2004 | FR, KT | STY with 2-oxo-2-(4-methyl)phenylaminolethylene <br> methacrylate at $65^{\circ} \mathrm{C}$; used infrared, $\mathrm{C}^{13}$ and <br> $\mathrm{H}-\mathrm{NMR}$ techniques. |
| Escher and Galland ${ }^{[16]}$ | 2004 |  | Terpolymerization of ethylene-propylene-1-hexene. |
| Ferando and Aldo ${ }^{[17]}$ | 1997 |  | STY and AN; no parameter estimation. |
| Fernandez-Monreal et al. ${ }^{[18]}$ | 1999 | TM | 2-HEMA/STY in DMF solvent. |
| Galimberti et al. ${ }^{[19]}$ | 1998 |  | Ethene/propene. |
| $\mathrm{Ha}^{[20]}$ | 1998 | NLLS | STY-co-citraconic anhydride-polymers |
| Ha et al. ${ }^{[21]}$ | 1999 | NLLS | STY and citraconic anhydride |
| Hill et al. ${ }^{[22]}$ | 1989 | NLLS | STY-AN |
| Hill et al. ${ }^{[23]}$ | 1992 | NLLS | STY-AN |
| Hooda and Brar ${ }^{[24]}$ | 2003 | KT, EVM | 4-vinyl pyridine with MAN. |
| Kim and Harwood ${ }^{[25]}$ | 2002 |  | MMA with MA. |
| Kim et al. ${ }^{[26]}$ | 2003 |  | Dimethyl(1-ethoxycarbonyl)vinyl phosphate with <br> STY; $C^{13}, P^{31}$ and H-NMR analysis. |
| Klumperman and Kraeger ${ }^{[27]}$ | 1994 | NLLS | STY and AN. |
| Kramer et al. ${ }^{[28]}$ | 1999 |  | STY and EA; high conversion data. |
| Maxwell et al. ${ }^{[29]}$ | 1993 | NLLS | STY-MMA |
| Mukherjee et al. ${ }^{[30]}$ | 1999 | KT, EVM | Acrylamide-AN |
| O'Leary ${ }^{[31]}$ | 2004 |  | Copolymers of poly(n-alkyl acrylates) at <br> low conversion. |
| Pazhanisamy et al. ${ }^{[32]}$ | 1997 | $\mathrm{FR}, \mathrm{KT}$ | AMS with $\mathrm{N}$-cyclohexylacrylamide in toluene <br> at $60^{\circ} \mathrm{C}$; characterized by H-NMR and <br> C-NMR spectroscopy. |
| Rudin et al. ${ }^{[33]}$ | 1981 |  | Vinyl compounds. |
| Selvamalar et al. ${ }^{[34]}$ | 2004 | FR, KT, <br> ex-KT, EVM | BCPA with GMA at $70^{\circ} \mathrm{C}$; FTIR, ${ }^{1} \mathrm{H}-\mathrm{NMR}$, <br> ${ }^{13} \mathrm{C}$-NMR spectrometry. |
| Soykan and Erol ${ }^{[35]}$ | 2004 | FR, KT | $\mathrm{N}$-(4-acetylphenyl)-maleimide and STY; FTIR, <br> ${ }^{1} \mathrm{H}$ and ${ }^{13} \mathrm{C}$ NMR analysis. |
| Sundarrajan et al. ${ }^{[36]}$ | 2003 |  | Ethylene dibromide or methylene dibromide <br> with styrne dibromide and sodium sulfide; <br> ${ }^{1} \mathrm{H}$-NMR and ${ }^{13} \mathrm{C}$-NMR analysis. |
| Wharry $^{[37]}$ | 2004 |  | Ethylene with 1-hexene. |
| Zhao et al. ${ }^{[38]}$ | 2001 |  | N-butyl maleimide with STY. |

## Copolymer Reactivity Ratio Estimation

Obtaining reactivity ratios from triad fraction data is a non-linear multi-response parameter estimation problem. Six triad fractions provide, in principle, more information than does a single copolymer composition measurement; hence the extra information should result in greater precision of the reactivity ratio estimates. Triad fractions are sequences of three consecutive monomer units in a copolymer chain. The fractions are categorized as either monomer-1-centered triads or monomer2-centered triads. The triads are denoted by $A_{i j k}$, where $i, j$ and $k$ are either monomer units 1 or 2 . The six triad fractions can be
related to the reactivity ratios through the following equations: ${ }^{[39]}$ fraction from each set thus leading to an estimation scheme in which the reactivity

$$
\begin{aligned}
& \mathrm{A}_{111}=\frac{\mathrm{r}_{1}^{2} \mathrm{f}_{1}^{2}}{\mathrm{r}_{1}^{2} \mathrm{f}_{1}^{2}+2 \mathrm{r}_{1} \mathrm{f}_{1} \mathrm{f}_{2}+\mathrm{f}_{2}^{2}} \\
& \mathrm{~A}_{211}+\mathrm{A}_{112}=\frac{2 \mathrm{r}_{1} \mathrm{f}_{1} \mathrm{f}_{2}}{\mathrm{r}_{1}^{2} \mathrm{f}_{1}^{2}+2 \mathrm{r}_{1} \mathrm{f}_{1} \mathrm{f}_{2}+\mathrm{f}_{2}^{2}} \\
& \mathrm{~A}_{212}=\frac{\mathrm{f}_{2}^{2}}{\mathrm{r}_{1}^{2} \mathrm{f}_{1}^{2}+2 \mathrm{r}_{1} \mathrm{f}_{1} \mathrm{f}_{2}+\mathrm{f}_{2}^{2}}
\end{aligned}
$$

where $f_{1}$ and $f_{2}$ represent the mole fraction of monomer 1 and 2 in the feed, respectively, and $r_{1}$ and $r_{2}$ are the reactivity ratios. In addition the sum of the monomer1 -centered triad fractions is unity and similarly with the monomer-2-centered fractions. There are therefore two linear dependencies in the data. Linear or nearlinear dependencies in the data will lead to unstable parameter estimates. A solution to the problem is to eliminate one triad

Abbrevations of monomers/chemicals.

| Abbreviations | Description |
| :--- | :---: |
| AA | Acrylic acid |
| AMS | Alpha-methyl styrene |
| AN | Acrylonitrile |
| BA | Butyl acrylate |
| BCPA | Benzyloxycarbonylphenyl acrylate |
| BMA | Butyl methacrylate |
| DMF | N,N'-dimethylformamide |
| EA | Ethyl acrylate |
| EMA | Ethyl methacrylate |
| GMA | Glycidyl methacrylate |
| HEMA | 2-hydroxyethyl methacrylate |
| MA | Methyl acrylate |
| MAN | Methacrylonitrile |
| MMA | Methyl methacrylate |
| NVP | N-vinyl-2-pyrrolidone |
| STY | Styrene |

Abbreviations of estimation techniques.

| Abbreviations | Description |
| :--- | :---: |
| Box Draper | Box Draper Determinant Criterion |
| EVM | Error in Variables Model |
| ex-KT | Extended Kelen Tudos |
| FR | Fineman-Ross |
| KT | Kelen Tudos |
| TM | Tidwell-Mortimer |

ratios are estimated from four triad fractions. ${ }^{[13]}$ As a result, in our work $\mathrm{A}_{111}$ and $\mathrm{A}_{222}$ were eliminated in order to avoid the issue of linear dependency.

The instantaneous copolymer composition model is often referred to as the MayoLewis model. Copolymer composition is the mole fraction of monomer 1 incorporated in the copolymer. Therefore, the Mayo-Lewis model relates the monomer feed composition with the copolymer composition, $\mathrm{F}_{1}$, via the following equation:

$$
\mathrm{F}_{1}=\frac{\mathrm{r}_{1} \mathrm{f}_{1}^{2}+\mathrm{f}_{1}\left(1-\mathrm{f}_{1}\right)}{\mathrm{r}_{1} \mathrm{f}_{1}^{2}+2 \mathrm{f}_{1}\left(1-\mathrm{f}_{1}\right)+\mathrm{r}_{2}\left(1-\mathrm{f}_{1}\right)^{2}}
$$

The implementation of the above equations in the parameter estimation scheme considered a multiplicative error structure based on previous experience. ${ }^{[1,2]}$ Furthermore, the error associated with the feed composition was assumed to be $\pm 1 \%$, the error for triad fractions was assumed to be $\pm 10 \%$, and the error for the copolymer composition was assumed to be $\pm 5 \%$.

## Error-in-variables Model (EVM)

The error-in-variables model (EVM) method is a relatively recent statistical approach to solving multi-response parameter estimation problems, where the errors in all measured variables are taken into account. The approach is particularly applicable for the estimation of copolymer reactivity ratios because all of the data, on which the estimation is based, are measurements, which contain errors, and some of
the errors can be large. Another benefit of using the EVM method is that the algorithm yields not only estimates of the true parameter values, but also estimates of the true values of the measurements. Additionally, EVM allows the user to assign relative weights to the measured quantities according to their precision, via the input of a measurement covariance matrix. The parameter estimation method also allows confidence intervals to be calculated for the estimated parameters.

The problem is described in detail and algorithms for parameter estimation are given by Reilly and Patino-Leal, ${ }^{[40]}$ while Patino-Leal et al. ${ }^{[41]}$ and Rossignoli and Duever ${ }^{[2]}$ have described in detail the application of EVM to the estimation of reactivity ratios in copolymer systems. An abbreviated version of the approach is presented below.

The EVM model consists of two statements. First, the vxl vector of measurements $\underline{x}_{i}$ is equated to the vxl vector of true values $\bar{\xi}_{\underline{\xi}}$, at the $\mathrm{i}^{\text {th }}$ of $\mathrm{n}$ conditions, plus an additive error $\underline{\varepsilon_{\mathrm{i}}}$

$\underline{\mathrm{x}}_{\underline{i}}=\underline{\xi}_{\underline{i}}+\underline{\varepsilon}_{\underline{i}} \quad$ where $\quad \mathrm{i}=1,2, \ldots, \mathrm{n}$

Here, the elements of $\underline{x}_{i}$ are the measured values of feed composition, triad fractions and copolymer composition. The error vector $\varepsilon_{\mathrm{i}}$ is often assumed to be normally distributed with a mean vector of $\underline{0}$, and a vxv covariance matrix $\underline{V}$, which is nonsingular and may be known or unknown ${ }^{[42]}$ Since the errors of the measurements used in this work are assumed to be multiplicative in nature, a logarithmic transformation is applied resulting in

$$
\ln \left(\underline{x}_{i}\right)=\ln \left(\underline{\xi}_{i}\right)+\underline{\varepsilon}_{i}
$$

The second statement specifies the model, which relates the true values of the parameters and variables,

$\mathrm{f}\left(\underline{\xi_{i}}, \underline{\theta}^{*}\right)=0 \quad$ where $\quad \mathrm{i}=1,2 \ldots, \mathrm{n}$

The vector of functions $\mathbf{f}$ in Equation (4) is $\mathrm{mxl}$, and may be linear or nonlinear in the elements of $\underline{\xi_{i}}$ and $\underline{\theta}$. The vector $\underline{\theta}$ contains the reactivity ratios to be estimated. Here the functions are the triad fraction and composition models specified in Equations (1) and (2). Using a Bayesian approach, that a point estimate $\hat{\theta}$, can be found by minimizing $^{[40]}$

$\phi=\frac{1}{2} \sum_{i=1}^{n} r_{i}\left(\overline{\underline{x}}_{i}-\hat{\underline{\xi}}_{i}\right)^{T} \underline{V}^{-1}\left(\underline{\underline{x}}_{i}-\hat{\underline{\xi}}_{i}\right)$

where $r_{i}$ is the number of replicates at the $\mathrm{i}^{\text {th }}$ trial.

The optimization algorithm uses a Newton's method similar to Fisher's method of scoring to minimize $\phi \cdot{ }^{[43]}$ The routine to solve the EVM problem uses a nestediterative scheme with an inner iteration that estimates the true values of the variables, $\underline{\xi}$, while keeping the parameter values constant, and an outer iteration that estimates the true values of the parameters, $\underline{\theta}$, while keeping the variables, $\underline{\xi}$, constant. The algorithm starts by using the initial parameter estimates (supplied by the user) and the $\underline{\xi}^{0}$ set equal to the measured variables $\underline{\underline{x}}$. The inner scheme uses the following equation iteratively to update the estimates of the variables,

$$
\begin{aligned}
\underline{\xi}_{i}^{(k+1)}= & \bar{x}_{i}-\underline{V B}_{i}^{\prime}\left(\underline{B}_{i} \underline{V B_{i}^{\prime}}\right)^{-1} \\
& \left.\times\left[f\left(\underline{\xi}^{(k)}, \underline{\theta}\right)\right)+\underline{B}_{i}\left(\underline{x}_{i}-\underline{\xi}^{(k)}\right)\right]
\end{aligned}
$$

where $\underline{B}_{i}$ is the vxl vector of partial derivatives of the function with respect to the variables,

$\underline{B}_{i}=\left[\frac{d f\left(\underline{\xi}_{i}, \underline{\theta}\right)}{d\left(\underline{\xi}_{i}\right)_{t}}\right]_{\underline{\xi}_{i}=\xi_{i}^{(k)}}$

for the $t^{\text {th }}$ element

and $\underline{V}$ is the vxv error covariance matrix for the measurements. Note that $\underline{\mathrm{V}}$ must either be supplied by the user or must be estimated from sufficient replicates.

The outer scheme uses the following equation iteratively to update the estimates of the parameters,

$\underline{\theta}^{(\mathbf{u}+1)}=\underline{\theta}^{(\mathbf{u})}-\underline{\mathrm{G}}^{-1} \underline{\mathbf{q}}$
where $\mathrm{G}$ is the pxp expected information matrix given by,

$$
\begin{aligned}
\underline{G} & =E\left[\frac{d^{2} \phi}{d \theta_{i} d \theta_{j}}\right] \quad i, j \text { element } \\
& =\sum_{i=1}^{n} r_{i} \underline{Z}_{i}^{\prime}\left(\underline{B}_{i} \underline{V B}_{i}^{\prime}\right)^{-1} \underline{Z}_{i}
\end{aligned}
$$

and $\mathrm{q}$ is the pxl gradient vector

$$
\begin{aligned}
\underline{q} & =\left[\frac{d \phi}{d \theta_{j}}\right] \quad i^{\text {th }} \text { element } \\
& =\sum_{i=1}^{n} r_{i} \underline{Z}_{i}^{\prime}\left(\underline{B}_{i}{\underline{V B^{\prime}}}_{i}\right)^{-1} \underline{B}_{i}\left(\underline{\bar{x}}_{i}-\hat{\hat{\xi}}_{i}\right)
\end{aligned}
$$

and $\underline{Z}_{i}$ is the lxp vector of partial derivatives with respect to the parameters,

$$
\underline{\underline{Z}}_{i}=\left[\frac{d f\left(\underline{\xi}_{i}, \underline{\theta}\right)}{d \theta_{k}}\right] \quad k^{\text {th }} \text { element }
$$

The only assumption required for EVM is that of model adequacy, while the construction of the confidence regions requires that the errors are independent and identically normally distributed. Generally, to quantify the uncertainty in the parameter estimates the $95 \%$ joint probability contour is determined via either of the following two methods. The first is a relatively rough approximation to the joint posterior probability region for the estimated parameters, and is given by

$(\underline{\theta}-\underline{\hat{\theta}})^{\prime} G(\underline{\theta}-\underline{\hat{\theta}}) \leq \chi_{(p, 1-\alpha)}^{2}$

where the "^" indicates estimates of the parameters $\underline{\theta}, \underline{\mathrm{G}}$ is the expected information matrix of the parameter estimates, and $\chi^{2}$ $(p, 1-\alpha)$ is the value of the chi-squared distribution having $\mathrm{p}$ degrees of freedom, exceeded with probability $\alpha{ }^{[1]}$ Here the assumption of multivariate normality is made and the elliptical posterior probability contour is determined. It is important to note that both the shape and probability content of this contour are approximate.

The second method is a somewhat better alternative to approximating the joint posterior probability region (JPR), and is given by the equation

$\phi(\underline{\theta})=\phi(\underline{\hat{\theta}})+\frac{1}{2} \chi_{(p, 1-\alpha)}^{2}$

where $\phi$ is given by Equation (6). This approximation gives contours of the correct shape (not a general elliptical shape) but of approximate probability content. ${ }^{[1]}$ All contours shown in this paper are calculated using equation (14).

## Results and Discussion

The following case studies were analyzed in order to: (1) compare reactivity ratio estimates obtained from composition data with those calculated from triad fraction data, (2) determine if triad fractions resulted in less uncertainty in the parameter estimates; and (3) evaluate the potential improvement in the estimates when the triad fractions and composition are combined.

## Copolymer Systems

## Case I: Acrylamide/Acrylonitrile

Mukherjee et al. ${ }^{[30]}$ studied the acrylaminde/acrylonitrile (AN) system at $65^{\circ} \mathrm{C}$ in bulk copolymerization and presented experimental data for both copolymer composition and triad fractions. The JPR's for the different data types can be seen in Figure 1. The JPR based on composition data is much larger than the JPR obtained when using triad fraction data. Furthermore, the JPR obtained from triad fraction analysis, falls within the JPR obtained from analysis of the composition data. For this system composition data and triad fraction data lead to consistent reactivity ratio estimates and triad fraction data leads to estimates with a smaller amount of uncertainty as quantified by the areas of the JPR.

Diagnostic checking was performed in order to determine whether the reactivity ratio estimates in fact model the experimental results accurately. The reactivity ratio estimates, obtained from analyzing the triad fractions and composition data separately, were used in the triad fraction equations (Eq. 1) to compare predicted triad fractions with the published experimental triad fractions. It can be seen in Figures 2 a) - d) that the predicted triad fractions, calculated using either the



Figure 1.

EVM analysis of composition and triad fraction data for the acrylamide/AN bulk system at $65^{\circ} \mathrm{C} .3^{[0]}$


Figure 2.

Comparison of Predicted triad fractions (a-d) and copolymer composition (e) using triad fraction-based and composition-based reactivity ratio estimates with experimental data.


Figure 2.

(Continued)

composition-based or the triad fractionbased reactivity ratio estimates, are in good agreement with the experimental triad fractions results. Furthermore, the copolymer composition can be predicted well with reactivity ratios that are estimated from either composition data or triad fraction data, as seen in Figure 2 e). These results confirm that the estimates obtained from either data type are consistent.

Figure 3 shows the JPR obtained by combining triad fraction with composition data and compares it with the JPR calculated using only triad fractions. This



Figure 3.

EVM analysis of triad fraction and combined composition/triad fraction data for the acrylamide/AN bulk system at $65^{\circ} \mathrm{C} \cdot{ }^{[30]}$

plot was produced to determine if combining triad fractions with composition would produce even better parameter estimates. It can be seen in Figure 3 that the use of composition data in conjunction with the triad fractions data does not result in a significant decrease in uncertainty, compared to simply using triad fraction data. Subsequently, for this system, on might argue that copolymer composition data does not contribute significant additional information to the estimation of reactivity ratios, given that triad fraction data is readily available.

## Case II: Acrylonitrile/Acrylic Acid

Brar and Dutta ${ }^{[5]}$ studied the acrylonitrile (AN)/acrylic acid (AA) system at $27^{\circ}$ in bulk photo-initiated copolymerization and presented experimental data on both copolymer composition and triad fractions. The data are shown in Table 2.

Table 2.

Data set of AN/AA bulk system at $27^{\circ} \mathrm{C} .[]$

| Feed <br> Composition $\mathrm{f} 1$ <br> (mol frac of AN) | Copolymer <br> Composition $\mathrm{F} 1$ <br> (mol frac of AN) | $\mathrm{A}_{111}$ | $\mathrm{~A}_{112+211}$ | $\mathrm{~A}_{212}$ | $\mathrm{~A}_{121}$ | $\mathrm{~A}_{122+221}$ | $\mathrm{~A}_{222}$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  | 0.94 |  |  |  |  |  |  |
| 0.95 | 0.88 |  |  |  |  |  |  |
| 0.9 | 0.82 | 0.704 | 0.242 | 0.054 | 0.371 | 0.456 | 0.173 |
| 0.85 | 0.76 | 0.624 | 0.306 | 0.07 | 0.247 | 0.499 | 0.253 |
| 0.8 | 0.62 | 0.542 | 0.377 | 0.081 | 0.188 | 0.501 | 0.311 |
| 0.75 | 0.57 | 0.462 | 0.413 | 0.125 | 0.16 | 0.467 | 0.373 |
| 0.7 | 0.4 | 0.326 | 0.518 | 0.156 | 0.075 | 0.437 | 0.488 |
| 0.6 |  | 0.284 | 0.477 | 0.238 | 0.084 | 0.328 | 0.588 |
| 0.55 | 0.19 | 0.229 | 0.526 | 0.245 | 0.058 | 0.339 | 0.602 |
| 0.5 |  | 0.153 | 0.507 | 0.339 | 0.064 | 0.286 | 0.65 |
| 0.45 | 0.19 |  |  |  |  |  |  |
| 0.4 | 0.17 |  |  |  |  |  |  |
| 0.3 |  |  |  |  |  |  |  |

Note that a total of 10 experiments are available in which copolymer composition data was measured, eight in which triad fractions were measured and only six for which both composition and triad fractions are available. The different number of data points and the difference in the feed compositions at which data are available complicate the case study somewhat. In the article the composition data was analyzed to obtain reactivity ratio point estimates, which were then used to obtain predicted values for the triad fractions. Model predictions of triad fractions based on compositionbased reactivity ratio estimates were found to be in good agreement with the experimentally determined triad fractions. Here the consistency between the copolymer composition and triad fractions is explored by comparing the resulting reactivity ratio estimates for the two different measurements. From Figure 4 it can be seen that the JPR of the triad fraction analysis is smaller in area than the composition JPR showing again that the use of triad fraction data results in more precise reactivity ratio estimates, compared with those obtained from composition data. In comparison to the previous example the two JPRs do not overlap as much. Diagnostic checking performed for the AN/AA system showed exactly the same results as with the diagnostic checking for the previous case study. In other words, when the compositionbased and triad fraction-based estimates were used to predict the experimental results good agreement was again found. Therefore for this system, the estimates are again consistent.

Figure 5 shows the comparison between the results obtained when combining triad fractions with composition and just using triad fractions. Again the regions are of approximately the same size, indicating no significant difference in parameter precision. Note that the combined data contour lies above that for triad fraction data only. The latter in turn lies above that based on composition data (Figure 4). Normally one would expect the combined contour to fall somewhere between the composition- and triad fraction-based contours. The explanation here is related to the differences in feed compositions between the different data sets.

## Case Study III: Acrylonitrile/Pentyl Methacrylate

Brar and Dutta also studied the acrylonitrile (AN)/ pentyl methacrylate (PMA)



Figure 4.

EVM Analysis of composition and triad fraction data for the AN/AA bulk system at $27^{\circ} \mathrm{C} .[5]$



Figure 5.

EVM analysis of triad fraction and combined composition/triad fraction data for the AN/AA bulk system at $27^{\circ} \mathrm{C}{ }^{[5]}$

system at room temperature in bulk and presented experimental data on both copolymer composition and triad fractions. ${ }^{[4]}$ Figure 6 shows the JPR from the EVM analysis of the composition data to be much larger than the JPR from the EVM analysis of the triad fraction data. That is, this case study is further testimony to the fact that the use of triad fraction data results in less uncertainty in the reactivity ratio parameter estimates. In this case, however, there is a considerable difference in the



Figure 6.

EVM analysis of composition and triad fraction data for the AN/PMA bulk system at room temperature. ${ }^{[4]}$
estimates obtained, in that the compositionbased estimates are considerably larger.

Similar to the procedure in the other case studies, diagnostic checking was then performed to ensure the fit of the model to the experiment results. Figures $7 \mathrm{a}-\mathrm{d}$ show the predicted triad fractions obtained when using the composition-based and triad fraction-based reactivity ratio estimates, while Figure 7 e shows the copolymer composition predicted from the Mayo-Lewis equation. In this case, triad fractions are best predicted using triad-based reactivity ratio estimates. Composition-based estimates do not yield very good triad fraction predictions and triad fraction-based estimates do not yield very good copolymer composition predictions. In addition, triad fraction A121 is not predicted well by either set of reactivity ratios. There is an observed lack of fit present. One possible explanation might be related to the calculation required to convert the actual measurements, namely the NMR normalized peak areas, into triad fractions. These calculations require additional parameters whose values might be inconsistent for this triad fraction. The peak areas and the converting equations are unfortunately not reported. Hence the source for the lack of fit is unknown.

Finally, combining copolymer composition and triad fraction data showed the same trends as seen in previous examples.

## Case Study IV: Styrene/Acrylonitrile

A number of groups have published work on the styrene (STY) - acrylonitrile (AN) system for both bulk and solution copolymerization. Here we analyzed data from the groups of Hill et al. ${ }^{[22,23]}$ and Klumperman and Kraeger ${ }^{[27]}$ Data is reported for both bulk and in toluene solvent.

A clearer picture of the estimates from the different data types can be seen when


Figure 7.

Comparison of predicted triad fractions (a-d) and copolymer composition (e) using triad fraction-based and composition-based reactivity ratio estimates with experimental data.


Figure 7.

(Continued)

the data is grouped together by system (i.e., bulk and toluene solvent) and the JPR's are shown. Note that in the figures of this case study, if the data set used in the analysis is taken from Hill et $\mathrm{al}^{[22]}$, Hill et al. ${ }^{[23]}$ or Klumperman and Kraeger, ${ }^{[27]}$ it is referred to in the figure as (Hill, 1989), (Hill, 1992) or (Klumperman, 1994), respectively. Furthermore, in all cases monomer 1 and 2 refer to styrene and acrylonitrile monomer, respectively.
In Figure 8 the results are shown for the Hill et al. ${ }^{[22,23]}$ triad fractions and composition data sets for bulk copolymerizations. This plot indicates relatively large differences between composition-based results and triad fraction-based estimates similar to the results observed for the AN/PMA system. The two different triad fraction data sets yield results which are relatively close. Furthermore, by considering Figure 9 with the bulk STY/AN studies from Hill



Figure 8.

EVM analysis of composition and triad fraction data for the STY/AN bulk system at $60{ }^{\circ} \mathrm{C}{ }^{[22,23]}$

et al. ${ }^{[23]}$ and Klumperman and Kraeger, ${ }^{[27]} \quad$ Similar trends are again seen when it can be seen that the regions from the considering the STY/AN studies in different data sources do not overlap, for toluene ${ }^{[22,27]}$ (see Figure 10). Note however neither composition nor triad fraction data. that the joint probability regions are closer



Figure 9.

EVM analysis of composition and triad fraction data for the STY/AN bulk system at $60{ }^{\circ}{ }^{[}{ }^{[23,27]}$



## Figure 10.

EVM Analysis of composition and triad fraction data for the STY/AN in toluene at $60{ }^{\circ} \mathrm{C}{ }^{[23,27]}$

together than they are in the analysis of the bulk experiments.

A possible explanation for the trends observed over the four different copolymer systems may have to do with the varying degrees of heterogeneity (preferential sorption or solvent effects) exhibited due to phase separation or precipitation during copolymerization. These "heterogeneity" effects became progressively more significant as we moved from case study I to IV. The effects have been documented before by several researchers for several copolymer systems involving AN and carboxylic acids. ${ }^{[44-47]}$ An increasing degree of heterogeneity leads to increased difficulty in obtaining polymer samples that give representative triad fraction measurements that are consistent with composition data. This may explain why reactivity ratio estimates from triad fractions on the one hand and composition on the other compare favourably for the acrylamide/AN and the AN/ AA systems, but do not for the AN/PMA and STY/AN systems. Further support for this hypothesis is seen in Figure 10, where the results are more consistent when STY/ AN is copolymerized in toluene solvent, which will make the system less heterogeneous.

## Concluding Remarks

This paper examined the question of whether or not triad fraction data can lead

Table 3.

Summary of results from the estimation case studies.

|  |  | Triads and <br> composition estimate <br> agrees | Triads has less <br> uncertainty in estimate <br> than composition | Combined has less <br> uncertainty in <br> estimate than triads |
| :---: | :---: | :---: | :---: | :---: |
| Acrylamide-AN |  | $\sqrt{ }$ | $\sqrt{ }$ | $x$ |
| AN-Acrylic Acid |  | $\sqrt{ }$ | $\sqrt{ }$ | $x$ |
| AN-Pentyl Methacrylate |  | $x$ | $\sqrt{ }$ | $x$ |
| STY-AN (bulk) | Hill (1989) | $x$ | $\sqrt{ }$ |  |
|  | Hill (1992) | $x$ | $\sqrt{ }$ | $x$ |
|  | Klump (1994) | $x$ | $\sqrt{ }$ |  |
| STY-AN (toluene) | Hill (1992) | $\sqrt{ }$ | $\sqrt{ }$ | $x$ |
|  | Klump (1994) | $\sqrt{ }$ | $\sqrt{ }$ |  |

NOTE: $\sqrt{ }=$ Yes, $X=$ No.

The following abbreviations are used: Klump $=$ Klumperman and Kraeger ${ }^{[27]}$; Hill $=$ Hill et al. ${ }^{[22,23]}$. Blank spaces in the table indicate that the analysis was not performed for that particular entry.
to reliable reactivity ratio estimates. Several aspects were investigated, namely: (1) Are triad fraction-based estimates consistent with composition-based estimates, (2) Do triad fractions lead to reactivity ratio estimates with less uncertainty, and (3) Is there and advantage to combining triad fraction and copolymer composition data. These questions were explored using four different case studies involving low conversion data from four different copolymer systems. Table 3 summarizes the results of these investigations.

In general triad fraction data did consistently result reactivity ratio estimates having significantly smaller uncertainty compared to those obtained from composition data. Combining triad fractions with copolymer composition did not reduce the uncertainty in the reactivity ratio estimates (therefore leading to higher quality estimates), compared to those obtained only from triad fractions. The reactivity ratio estimates may not agree for the same system, when different data types are used. That is, the parameter estimates obtained from analyzing triad fraction data are not always in agreement with the estimates obtained from analyzing composition data. Heterogeneity in the copolymerization process may provide an explanation for this observation.

Acknowledgements: Financial support from the Natural Science and Engineering Research Council of Canada (NSERC), the Canada Research Chair (CRC) program, and a Province of Ontario Graduate Scholarship (OGS) is gratefully acknowledged.

[1] A. L. Polic, T. Duever, A. Penlidis, J. Poly. Sci. Polym. Chem. 1994, 36, 813.

[2] P. Rossignoli, T. Duever, Polym. React. Eng. 1995, 3, 361.

[3] M. Dube, R. Sanayei, A. Penlidis, K. O’Driscoll, P. Reilly, J. Polym. Sci., Polym. Chem. 1991, 29, 703.

[4] A. Brar, K. Dutta, J. Appl. Polym. Sci. 1998, 69, 2507.

[5] A. Brar, K. Dutta, Eur. Polym. J. 1998, 34, 1585.

[6] A. Brar, B. Jayaram, K. Dutta, J. Polym. Mater. 1994, $11,171$.

[7] A. Brar, M. Kaur, J. Appl. Polym. Sci. 2003, 88, 3005.

[8] A. Brar, M. Kaur, Eur. Polym. J. 2003, 39, 705.
[9] A. Brar, D. Pradhan, J. Appl. Polym. Sci. 2003, 89, 1779.

[10] A. Brar, D. Pradhan, J. Mol. Struct. 2003, 649, 245.

[11] A. Brar, R. Kumar, M. Kaur, J. Mol. Struct. 2003, 650, 85 .

[12] P. Brown, K. Fujimori, Polymer 1994, 35, 2302.

[13] A. Burke, T. Duever, A. Penlidis, Macromol. Theory Simul. 1994, 3, 1005.

[14] J. de la Fuente, M. Fernandez-Garcia, M. FernandezSanz, E. Madruga, Macromolecules 2001, 34, 5833.

[15] I. Erol, F. Yavuz, M. Durgun, Polym. J. 2004, 36, 303.

[16] F. Escher, G. Galland, J. Polym. Sci., Polym. Chem. 2004, 42, 2474.

[17] A. Ferando, A. Longo, Polym. Prepr. 1997, 38, 798.

[18] C. Fernandez-Monreal, M. Sanchez-Chaves, G. Martinez, E. Madruga, Acta Polym. 1999, 50, 408.

[19] M. Galimberti, F. Piemontesi, O. Fusco, I. Camurati, M. Destro, Macromolecules 1998, 31, 3409.

[20] N. Ha, Comp. Theor. Polym. Sci. 1998, 7, 121.

[21] T. Ha, K. Fujimori, D. Tucker, P. Henry, J. Macromol. Sci., Pure Appl. Chem. 1999, A36, 893.

[22] D. Hill, J. O'Donnell, P. O'Sullivan, Eur. Polym. J. 1989, 25, 911.

[23] D. Hill, A. Lang, P. Munro, J. O'Donnell, Eur. Polym. J. 1992, 28, 391.

[24] S. Hooda, A. Brar, J. Appl. Polym. Sci. 2003, 88, 3232.

[25] Y. Kim, H. Harwood, Polymer 2002, 43, 3229.

[26] Y. Kim, D. Priddy, H. Harwood, Polymer 2003, 44, 4165 .

[27] B. Klumperman, I. Kraeger, Macromolecules 1994, 27, 1529 .

[28] I. Kramer, H. Pasch, H. Handel, K. Albert, Macromol. Chem. Phys. 1999, 200, 1734.

[29] I. Maxwell, A. Aerdts, A. German, Macromolecules 1993, 26, 1956.

[30] M. Mukerjee, S. Chatterjee, A. Brar, J. Appl. Polym. Sci. 1999, 73, 55.

[31] K. O'Leary, D. Paul, Polymer, 2004, 45, 6575.

[32] P. Pazhanisamy, M. Ariff, Q. Anwaruddin, J. Macromol. Sci., Pure Appl. Chem. 1997, A34, 1045.

[33] A. Rudin, K. O’Driscoll, M. Rumack, Polymer 1981, 22, 740 .

[34] C. Selvamalar, P. Vijayanand, A. Penlidis, S. Nanjundan, J. Appl. Polym. Sci. 2004, 91, 3604.

[35] C. Soyhan, I. Erol, J. Appl. Polym. Sci. 2004, 91, 964. [36] S. Sundarrajan, K. Ganesh, K. Srinivasan, Polymer, 2003, 44, 61.

[37] S. Wharry, Polymer 2004, 45, 2985.

[38] Y. Zhao, P. Liu, H. Liu, J. Jiang, C. Chen, F. Xi, Macromol Rapid. Commun. 2001, 22, 633.

[39] J. Koenig, "Chemical microstructure of polymer chains", John Wiley \& Sons Ltd, New York 1980.

[40] P. Reilly, H. Patino-Leal, Technometrics 1981, 23, 221.

[41] H. Patino-Leal, P. Reilly, K. O'Driscoll, J. Polym. Sci. Polym. Lett. 1980, 18, 219.

[42] S. Keeler, P. Reilly, Can. J. Chem. Eng. 1991, 69, 27. [45] L. Garcia-Rubio, G. Lord, J. Macgregor, A. [43] P. Reilly, S. Keeler, H. Reilly, Appl. Stat. 1993, 42, Hamielec, Polymer 1985, 26, 2001.

693. 

[44] L. Garcia-Rubio, A. Hamielec, J. Appl. Polym. Sci. 1979, 23, 1397. [46] K. Plochocka, H. Harwood, Polym. Prepr. 1978, 19, 240.

[47] Y. Semchikov, Macromol. Symp. 1996, 111, 317.


[^0]:    Institute for Polymer Research (IPR) Department of Chemical Engineering 200 University Avenue West University of Waterloo, Waterloo, Ontario, Canada N2L 3G1 E-mail: tduever@uwaterloo.ca

