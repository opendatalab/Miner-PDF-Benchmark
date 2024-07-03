# An integrated approach for prioritization of river water quality sampling points using modified Sanders, analytic network process, and hydrodynamic modeling 

Ali Asadi $\cdot$ Alireza Moghaddam Nia $[$ $\cdot$ Bahram Bakhtiari Enayat $\cdot$<br>Hossein Alilou $\cdot$ Ebrahim Ahmadisharaf $\cdot$ Edwin Kimutai Kanda $\cdot$<br>Emmanuel Chessum Kipkorir

Received: 18 January 2021 / Accepted: 29 June 2021

(C) The Author(s), under exclusive licence to Springer Nature Switzerland AG 2021


#### Abstract

Determination of the water quality monitoring network (WQMN) is a vital stage for surveying ecosystem health. Studies have been done in determining the optimal number and location of sampling points, but seasonality of water quality, especially for heavy metals, has been rarely studied. For the first time, this study proposes a framework to determine the optimal location of sampling points to monitor lead $(\mathrm{Pb})$. This study was conducted for the Karoun River, located in southwestern Iran. First, hydraulic characteristics of the river were simulated by implementing of MIKE11 software as well as water quality(variation of $\mathrm{Pb}$ concentration). NashSutcliffe coefficient were 0.91 and 0.91 for discharge


[^0]calibration and validation, respectively. Second, 16 potential sampling points were proposed using modified Sanders' approach considering seasonality. For a better accuracy in the WQMN layout and a more efficient site selection of sampling points, a $1-\mathrm{km}$ buffer is stretched along the river for determining non-point source pollution sources and prioritizing candidate points. This leads to considering different land uses in the study area, while GIS software has been employed. Seasonal changes and land use have a significant impact on the location of optimal sampling points. The presented framework can be used to improve water quality and support watershed protection efforts.[^1]

Keywords Water quality monitoring $\cdot$ Heavy metal $\cdot$ Hydrodynamic modeling

## Introduction

Water quality monitoring is essential to evaluate the health of aquatic ecosystems and plan for protection strategies (Wang et al., 2008). A well-configured water quality monitoring network (WQMN) is one of the essential tools to realize the dynamics of any watershed (Strobl, 2006). One of the most critical keys in designing an effective WQMN is to find suitable locations of sampling points (Sanders, 1983). "If collected samples are not representative of the water mass, the frequency of sampling and the mode of data interpretation and presentation become inconsequential" (Alilou et al., 2018). It is well known that effective management of pollution resources is linked with the locations of sampling points (Behmel et al., 2016). Behmel et al. (2016) and Alilou et al. (2019a, b) emphasized the need for a suitable and accepted unique method of designing a WQMN program based on the seasonal variability in loads of water quality constituents and non-point sources. An example category of pollutants that have harmful impacts on public health is heavy metals. According to the U.S. Environmental Protection Agency (2000), heavy metals have adverse impacts on public health due to their toxicity, with lead being one of the most harmful contaminants. It is therefore critical to develop an effective WQMN by selecting potential monitoring stations and determining optimal ones for heavy metals at a seasonal frequency.

Recently, researchers have shown an increasing interest in the realm of WQMN design. Do et al. (2012) showed how, in the past, research into WQMN design was mainly concerned with mathematical aspects. Multivariate statistical approaches have been used by Ouyang (2005) and Wang et al. (2014) to optimize and select sampling points. In other studies, geostatistical methods and the combination of the geographic information system (GIS) and a fuzzy logic approach (Beveridge et al., 2012; Strobl et al., 2006; Rahmati et al., 2019) were used to select the location of WQMN stations. Other studies have used hydrological simulation and the genetic algorithm to select sampling points (Liyanage et al.,
2016; Telci et al., 2009). Alternate approaches have been also proposed to select the sampling points. An example approach was introduced by Sharp (1971), in which river network, including tributaries, was divided into successive halves by identifying the centroids and proposing them as sampling points. Sharp's method was modified by Sanders (1983), in which pollutant loadings and the number of outfalls were employed instead of tributaries (Varekar et al., 2016). An advantage of Sanders' method is that it considers the absolute potential pollution of each sampling site and budget deficiency for sampling (Do et al., 2011; Sanders, 1983). Although several studies (e.g., Park et al., 2006; Do et al., 2011; Varekar et al., 2016) have used these methods, there are limitations in applying these approaches in rivers without tributaries as well as simple and complex streams (Alilou et al., 2018). Sabzipour et al. (2019) worked on redesigning the Karoun River WQMN, using a geostatistics approach, ordinary kriging, and sequential Gaussian simulation, while focusing on electrical conductivity (EC) and dissolved oxygen (DO), ascertained that the sampling locations should be modified or increase the frequency of samplings. However, the effects of seasonal variation in diffuse pollution loadings, which have a significant impact on WQMN design, have rarely been studied (Varekar et al., 2015).

In the recent decade, measurements of heavy metals in alluvial rivers have been studied (Kashefipour $\&$ Roshanfekr, 2012). Heavy metals may be found dissolved in water or adsorbed to suspended matter and differed from a substance to another MIKE11 (2015). Rauf et al. (2009) and Akan et al. (2010) studied the impact of sedimentations on the transports of heavy metals and Papafilippaki et al. (2008) investigated the seasonal variation of heavy metals. Kashefipour and Roshanfekr (2012) introduced a relationship between $\mathrm{pH}$, salinity, and lead decay coefficient. Therefore, the study of heavy metals in determining water quality would have a significant impact on different aspects of water management, such as WQMN.

A complete and adequate design environment for water resources and water quality management can be provided by MIKE 11 software due to the flexibility and ease of setup (DHI, 2003). This software would provide a convenient approach to study significant factors in water quality management, which can be the amount of heavy metals in water bodies.

The primary sources of heavy metal pollution are mining, sewage irrigation, manufacturing products, smelting, and agrochemicals activities.

Some toxic heavy metals such as lead are discharged into the atmosphere, water, and soil (Hu et al., 2014; Nadal et al., 2005). However, many lead pollution sources are surrounding the study area, which cause enormous problems (Kashefipour \& Roshanfekr, 2012), but heavy metals contamination has not been considered to determine WQMN stations in previous studies in the Karoun River (current study area), where lead is the pollutant of concern.

The abovementioned methods used fully mathematical methods, or the ones applied geostatistical, topographical, and multivariable statistics have not considered a fully dynamic simulation method to illustrate a fuller picture of a given river system in various seasons. There is a need for a simple efficient method to design WQMN and a fully dynamic straightforward tool to manage and operate both simple and complex river systems considering seasonality.

The main objective of this study was to determine the optimal location of sampling points in a WQMN for a lead-impaired river considering seasonal variability. We present a framework to locate sampling sites using the convincing method, which are not advanced and detailed for selection of sampling points, especially for complex rivers. The novel aspect of this study is coupling analytic network process (ANP) and modified Sanders' approach in
WQMN design of a lead-impaired waterbody. As mentioned by Alilou et al. (2019a, b), several "Studies have shown that the ANP is the most appropriate approach among multi-criteria methods (e.g., technique for ordering performance by similarity to ideal solution (TOPSIS) and analytical hierarchy process (AHP)), because it considers the inter-relationship between criteria and also sub-criteria."

Our hypothesis is that the seasonality affects the optimal location of monitoring stations in a WQMN. The proposed framework conceptualizes WQMN in three stages: (i) using a fully dynamic hydrodynamic model, MIKE 11, to simulate seasonal variability of lead; (ii) applying the modified Sanders' method, which is a well-configured approach (Do et al., 2011; Park et al., 2006; Varekar et al., 2015, 2016), to locate sampling points; (iii) prioritization of proposed sampling points for each season based on the potential pollution of diffusive pollution loadings. The proposed method is illustrated on a leadimpaired river southwest of Iran.

## Materials and methods

## Study area

The $67,257-\mathrm{km}^{2}$ Karoon basin contains Dez and Karoon Rivers, $67 \%$ of which includes mountainous and the remaining is mostly plain (Khuzestan plain), where average annual rainfall is $233 \mathrm{~mm}$. Karoon



(a)



(b)

Fig. 1 a Point source pollution and $\mathbf{b}$ study area

River is the longest river in Iran (Fig. 1a). The elevation of Khuzestan plain in Shushtar area, where the Karun River passes through Gotvand dam, is $>50 \mathrm{~m}$ above mean sea level (msl), gradually decreases to the south, until in Band Ghir to about $22 \mathrm{~m} \mathrm{msl}$, in Ahvaz to about $15 \mathrm{~m} \mathrm{msl}$, in sugarcane development area to about 1 to $9 \mathrm{~m} \mathrm{msl}$, in Darkhovin it is about $4 \mathrm{~m} \mathrm{msl}$; at the very downstream, the elevation is $\sim 2 \mathrm{~m} \mathrm{msl}$. The average slope has a similar variability across the floodplain. In upstream areas, it is about $0.08 \%$ along the river; it gradually decreases to about 0.008 per thousand in the downstream parts.

District of Mollasani to Farsiat stations on this river provides water supply to several cities, industrial units, and agricultural lands, as reported by Kashefipour and Roshanfekr (2012). The wastewater withdrawal from various industries and agricultural lands, which consist of a high level of contamination such as chemical fertilizers, heavy metals, pesticides, and other dissolved constituents, is considered as a main point source pollution (Karamouz, 2002). The portion of industrial activities in contaminating the water body is $23 \%$, varying between 12 and $60 \%$ depending on the geographic location and season (Karamouz, 2002).

Datasets used in this study were acquired from Khuzestan Water and Power Authority (KWPA). Mollasani $(0.0 \mathrm{~km})$, Ahvaz $(65.1 \mathrm{~km})$, and Farsiat $(113.9 \mathrm{~km})$ stations are located along Karoon River. Observations used include hydrodynamic data (discharge and water level) and water quality data (dissolved lead) in monitoring stations. In this study, 213 surveyed cross sections covering Mollasani to Farsiat stations were used in the simulations.

## Modeling

Modeling analysis was done in two parts: first, as a core of MIKE 11, hydrodynamic modeling calibration and validation; second, using the calibrated-validated hydrodynamic model results, advection-dispersion module of the model is calibrated and validated to simulate water quality in the river. Ultimately, we determined the optimal WQMN using the modified Sanders approach.

MIKE 11

MIKE 11 was used to for hydrodynamic modeling of river channels. It is a one-dimensional (1D) unsteady model that simulates water level and discharge as well as sediment transport in the rivers (Dutta et al., 2013). A 1D implicit, finite-difference scheme is utilized by MIKE 11 to solve Saint-Venant equations (Dutta et al., 2007; Kabir \& Hasin, 2011; Doulgeris et al., 2012; Chen et al., 2018) and a correction term to reduce the third-order truncation error (MIKE11, 2015). There are two equations: Eq. (1), the mass conservation; and Eq. (2), the momentum conservation (MIKE11, 2015).

Three main assumptions in MIKE11 hydrodynamic module are that water is incompressible and homogenous; the bottom slope is small; and the flow everywhere is parallel to the bottom (MIKE11, 2015).

$\frac{\partial Q}{\partial x}+\frac{\partial A}{\partial t}=q$

$\frac{\partial Q}{\partial t}+\frac{\partial\left(\frac{\alpha Q^{2}}{A}\right)}{\partial x}+g A \frac{\partial h}{\partial x}+\frac{g Q|Q|}{C^{2} A R}=0$

where the independent variables are space $(x)$ and time $(t)$, the dependent variable is discharge $(Q), \propto$ is momentum distribution coefficient, and $g$ is gravitational acceleration and water level $(h)$.

Advection-dispersion module of MIKE 11 simulates transport and dispread of conservation pollutants and constituents as well as heat with linear decay. The following equations are applied:

$\frac{\partial A C}{\partial t}+\frac{\partial Q c}{\partial x}-\frac{\partial}{\partial x}\left(A D \frac{\partial C}{\partial x}\right)=-A K C+C_{2} q$

where, $C$ is the sediment concentration, $D$ is the dispersion coefficient, $A$ is the cross-sectional area, $K$ is the linear decay coefficient, $C_{2}$ is the source/sink concentration, $q$ is the lateral inflow, $x$ is the space coordinate, and $t$ is time (MIKE11, 2015). The equation is based on two transport mechanisms: advocative (or convective) transport with the mean flow and dispersive transport due to concentration gradients.

The fundamental theories in the advection-dispersion equation are (MIKE11, 2015):

- The modeled substance is completely mixed over the cross sections, implying that a source/sink term is considered to mix instantaneously over the cross section;
- The modeled substance is conservative or subject to a first-order reaction (linear decay);
- Fick's diffusion law applies, i.e., the dispersive transport is proportional to the concentration gradient.


## Hydrodynamic model calibration

Model calibration was done for the period of April 21, 2009, through April 21, 2010, and from then to 31/07/2010 for validation. Daily observed discharge was used as an inflow boundary for the upstream and the water level was used for the downstream boundary conditions. A Manning coefficient $(n=1 / M$ ) was used as the calibration parameter. The same $n$ value was used for channels and banks; the river was divided into four segments based on the vegetation and materials of channel bed and banks. A manual calibration was done by manually changing $n$ from 0.026 to 0.035 , and several model runs were performed to optimize the model performance. Nash and Sutcliffe efficiency (Nash \& Sutcliffe, 1970), root-mean-square error (RMSE), and percent bias (PBIAS) were used to quantify the model performance.

The following (Eq. 4) and root-mean-square error (RMSE) (Eq. 5) were used to compare simulations and observations.

$N S E=1-\left[\frac{\sum_{i=1}^{n}\left(O_{i}-P_{i}\right)^{2}}{\sum_{i=1}^{n}\left(O_{i}-P_{\text {avr }}\right)^{2}}\right]$

where $P_{\text {avr }}$ is the mean of observed data, and $P_{i}$ is simulattion at time i. $O_{\mathrm{i}}$ is the observation at time $i$. If NSE is 1 , the results indicate that the model prediction is perfect, while lower NSE values show less satisfactory simulations. RMSE explains the difference between the observed and simulated values (Legates \& McCabe, 1999). The RMSE is computed as:

$R M S E=\sqrt{N-1 \sum_{i=1}^{n}\left(O_{i}-P_{i}\right)^{2}}$

where $N$ is the number of time steps, $O_{i}$ is the observation at time $i$, and $P_{i}$ is the prediction at time $i$. PBIAS describes the average tendency between the simulations and observations (Eq. 6). This means whether the model performance is satisfactory; i.e., the optimal value of PBIAS is 0.0 . If the value is positive, the underestimation bias is shown; on the contrary, the negative value represents the over-estimation bias (Gupta et al., 1997; Choubin et al., 2019).

PBIAS $=\frac{\sum_{i=1}^{n}\left(O_{i}-P_{i}\right) \times 100}{\sum_{i=1}^{n} O_{i}}$
Where $\mathrm{O}_{\mathrm{i}}$ is the observed value, and $\mathrm{P}_{\mathrm{i}}$ is the predicted value. To grade the model performance based on the values of fit measures, we followed the guidelines by Moriasi et al. (2015) and Ahmadisharaf et al. (2019).

## Dissolved heavy metals modeling

The advection-dispersion module of MIKE 11 was utilized to simulate the fate and transport of lead in the water column. Initial lead concentration was assumed to be 0 across the river. The time series of lead concentration in upstream boundaries (Mollasani stream gauge) was fed to the model as an input, while it was assumed that the concentration has a zero gradient in downstream. Lead simulation was done on a daily time step. A local sensitivity on the impact of the dispersion factor on the simulated lead concentration showed that the decay constant of 0.5 results in the best model performance.

## Application of modified Sanders approach

To determine the optimal location of the monitoring station during the validation period, we used the modified Sanders approach introduced by Do et al. (2011). In this approach, pollutant load at the outlet of river is equal to accumulative pollutant load at each cross section along the river and the first centroid is the first hierarchy, the point with a magnitude near $M_{h}$ (Eq. 7):

$M_{h}=\left[\frac{N_{0}+1}{2}\right]$

$N_{0}$ is the total pollution load at the outlet, and $M_{h}$ is the value of the sampling location at the $h^{\text {th }}$ order. It is a point with a value closest to half of the total river pollutants and determines the first priority in sampling with the first hierarchy level. This trend is continuing (Eq. 8) for the next three levels to discover the other potential points with the next priorities.

$M_{h+1}=\left[\frac{M_{h}+1}{2}\right]$

Where $M_{h+1}$ is the value of sampling point at the $(h+1)^{\text {th }}$ level of the hierarchy. The maximum number
of sampling points with a different hierarchy level is calculated by Eq. (9):

$\mathrm{n}=2^{\mathrm{h}}-1$

in which $n$ indicates the number of sampling points at the $h^{\text {th }}$ hierarchy level ( $n=15$ here). We used an average lead concentration in each season for every cross section and then assumed accumulated concentration at the river outlet.

Prioritization of alternate sampling points

After determining alternate sampling points via the modified Sanders approach for the validation period, the next step is prioritizing these alternatives via the criteria analyzed weighted method (Alilou et al., 2018, 2019a, b; Chang \& Lin, 2014a, b). In this approach, potential pollution for non-point source pollution (NPSP) is calculated via Eq. (9):

$N P S P=\sum_{i=1}^{n} W_{i} \times A_{i}$

$W_{i}$ is the potential pollution weight of each nonpoint source/criterion calculated by the ANP method (Alilou et al., 2018; Kordrostami et al., 2021). $A_{i}$ is the percent of area for each non-point source/criterion between candidate sampling points in the buffer zone. For a given alternate sampling point, a lower NPSP means a lower priority and vice versa.

Occasionally, a combination of upper values of NPSP and lower values of the hierarchy obtained from the modified Sanders yields the most appropriate sampling points during different seasons. In areas with high human activities (high NPSP), the sampling points with a higher priority are selected as the monitoring points (Do et al., 2012).

## Contributing area

Routinely, the lands far from rivers cannot have any influence on river pollution (Sivertun \& Prange, 2003). Sivertun and Prange (2003) suggested that pollutants produced outside the distance of $1 \mathrm{~km}$ have no impact on river water quality. Thus, a buffer zone of $1 \mathrm{~km}$ was used across the entire river. A simple buffer zone makes an error in calculating the contributing area of non-point sources; therefore, the flow length of each unit area was considered (Alilou et al., 2019a, b). The flow length, distance from any point in the river basin to the basin outlet, was measured using the digital elevation model (DEM, https://earthexplorer. usgs.gov/) with a spatial resolution of $30 \mathrm{~m}$; the river was divided into multiple points with $~ 30$-m intervals. For each point, the corresponding drainage area and the flow lengths for all the cells inside were measured. The buffer zone of each land unit area (cells) has a distance of less than $1 \mathrm{~km}$. NPSP, which affects the river water quality, was demonstrated by dividing the buffer zone between the alternate points to different catchments (Fig. 1b). A schematic of the proposed approach for determination of optimal monitoring stations in a WQMN is presented in Fig. 2.

## Results and discussion

Hydrodynamic model calibration and validation

MIKE 11 was calibrated against observed data by adjusting the Manning coefficients of the channels. Ahvaz station data in the midstream were used as observed data for both calibration and validation of the model.The optimal Manning coefficients were $0.026,0.04,0.035$, and 0.026 for the four river segments: cross sections $1-12,13-49,50-144$, and 145-213 (from upstream to downstream). The simulated and observed discharge and water level at Ahvaz station are illustrated in Fig. 3. The model could satisfactorily predict the trend of discharge and water level with a good error and bias. Additionally, the simulated peak flow closely matched that observed in most events. NSE for the water level in calibration and validation periods were 0.75 and 0.77 . The PBIAS were -0.01 and -0.19 , respectively, for the calibration and the validation of water level, which means an overestimation of the observations in both calibration and validation periods. The model performance was better for discharge both in calibration and validation, with an NSE of 0.91 . A PBIAS of 0.01 was found for the calibration and for the validation, suggesting an excellent performance of the hydrodynamic simulation (Table 1). Thus, MIKE 11 performance on the prediction of both water level and discharge was judged to be good



Fig. 2 Graphical diagram of the proposed approach for determination of the suitable locations of the water quality monitoring points

according to the criteria by Moriasi et al. (2015) and Ahmadisharaf et al. (2019).

Water quality model calibration and validation

Figure 3 e, $f$ illustrated the observed and simulated lead concentrations at Ahvaz station. Fit measures are provided in Table 1. With PBIAS of $-2.80 \%$ (calibration) and $-1.57 \%$ (validation) and NSE 0.85 (calibration) and 0.80 (validation), the model performance was judged to be satisfactory according to the criteria by Moriasi et al. (2015) and Ahmadisharaf et al. (2019).

There is a relationship between the lead concentration and water discharge; it is evident that there is a variability in the amount of point and non-point pollution sources, exported to the river and seasonal variability, leading to unexpected results. In rainy seasons (here spring and winter), the more contaminants concentrated in surface runoff, the more pollution passes through the river from contributing lands. On the other hand, in dry seasons (summer and fall), inlet pollution seems to be much less, so the lead concentration in the river is low. These imply that the variability of the lead concentration in a dry season is different from that in a wet season, highlighting the importance of seasonality in selection of sampling points.

At the same time, it is expected that natural and artificial drainage systems of farmlands work properly, leading to water pollution. Moreover, having the precise amount of industrial and rural area



(a)



(b)

Validation



(c)

Calibration



(d)

Validation



(e)

$\mathrm{Pb}$ Calibration
(3)
$\odot \odot$
8
Simulated 20 Observed

$\mathrm{Pb}$ Validation



Fig. 3 a Discharge calibration. b Discharge validation. c Water level calibration. d Water level validation. e Lead calibration. f Lead validation at Ahvaz station

swages could lead us to a better understanding of the pollution suppliers. Some of the potential pollution sources including industries and hospitals are presented in Fig. 4 as well as their geographical locations in Table 2.

Determination of water quality monitoring network

Sampling location number by considering hierarchy is calculated via Eq. (7). For ranking the pollutant points (Fig. 5), the four-hierarchy level was assumed and $M_{h}$ values were estimated via Eq. (8) for all seasons. $M_{h}$ and potential points are shown in Table 3. $M_{h}$ values are the result of accumulated lead concentration in the demonstrated 16 potential sampling points on Karoon River, while low values of the hierarchy are considered the most suitable sampling points. The high values of NPSP were also applied to optimize the exact location of sampling points along with the seasonal variability.

The results of optimal location for sampling points depending on the seasons are provided in Table 3 and Fig. 6. Sampling location with hierarchy $h$ has the smallest dissimilarity between the calculated $M_{h}$ values and observed lead loadings. As we can see in Table 3, by combining these values with high NPSP value, P8 and P16 have the greatest potential for sampling sites, followed by P1, P3, P4, and P12. Although the P3 and P4 have the lowest value of $h$, they were considered as the most appropriate sampling points because of high human activities (high NPSP value).

Seasonal sampling points illustrated that the priority of sampling points $\mathrm{P} 1$ and $\mathrm{P} 9$ are different in summer and fall because of a low lead concentration in dry season, although high NPSP values helped to find their exact priority. In contrast, P1 has a low NPSP



but a greater value of $h$. The combination of $h$ and NPSP gives a clear picture of the sampling points' priority (Fig. 7). On the other hand, surface runoff during the wet period (December-May) and cultivation seasons (mainly start in April) and their wastewater are the causes of variabilities in lead concentration and optimal location of the sampling points. Therefore, similar to what Varekar et al. (2015) mentioned, we also found that seasonality has a considerable impact on determining the location of sampling points.

Drainage area and land use are the main factors in the volume of surface and groundwater and pollutant loads since there is only a limited amount of rainfall and subsequently runoff in dry seasons (Varekar et al., 2016). The characteristics of pollutant discharges (mainly exported by industries) for the point sources have a significant effect on pollutant load during the dry seasons. Therefore, the seasonal variability affects the priority order and the number of sampling points. It is more efficient to locate sampling points in the downstream of main pollutant sources where the water quality degrades. Maybe considering all pollutant sources data during the simulation period would reflect the realistic results and more confidence in determining the WQMN.

The results relating to the locations of potential sampling points, where there are higher human activities and potential risks, are in agreement with previous studies, including Do et al. (2011), Park et al. (2006), Varekar et al. (2015), and Varekar et al. (2016).

On the other hand, the findings highlighted that the flow length of each land unit area should be considered to evaluate the contributing drainage areas in the buffer zone between the alternate sampling points (Alilou et al., 2019a, b). That is, the values of NPSP, related to the proportion of the contributing drainage area, for alternate points were precisely figured and priorities of candidate points were meticulously determined. In other words, the high value of NPSP demonstrates the high priority for sampling points (Do et al., 2012), which outlines the anthropogenic activities and natural areas (Table 3). Although this study would enhance the studies that only used geostatistical, topographical, and multivariable statistics, it proposed a novel combination of ordinary methods and coupled hydrodynamic-water quality simulation approach in a large river system.



Fig. 4 The location of some of the neighborhood industries can act as point source pollution

Table 2 The location of potential pollution sources

| Row | Name | Longitude | Longitude |
| :---: | :---: | :---: | :---: |
| 1 | Ramin Power Station | $48^{\circ} 52^{\prime} 27.8^{\prime \prime} \mathrm{E}$ | $31^{\circ} 30^{\prime} 17.2^{\prime \prime} \mathrm{N}$ |
| 2 | Ahvaz Sugar Refinery | $48^{\circ} 45^{\prime} 04.2^{\prime \prime} \mathrm{E}$ | $31^{\circ} 25^{\prime} 23.4^{\prime \prime} \mathrm{N}$ |
| 3 | Zargan Power Station | $48^{\circ} 45^{\prime} 44.6^{\prime \prime} \mathrm{E}$ | $31^{\circ} 22^{\prime} 37.1^{\prime \prime} \mathrm{N}$ |
| 4 | SEWER SERVICES Ahwaz | $48^{\circ} 42^{\prime} 14.2^{\prime \prime} \mathrm{E}$ | $31^{\circ} 21^{\prime} 20.1^{\prime \prime} \mathrm{N}$ |
| 5 | Imam Khomeyni Hospital | $48^{\circ} 41^{\prime} 01.8^{\prime \prime} \mathrm{E}$ | $31^{\circ} 19^{\prime} 53.4^{\prime \prime} \mathrm{N}$ |
| 6 | Mehr Hospital | $48^{\circ} 40^{\prime} 44.8^{\prime \prime} \mathrm{E}$ | $31^{\circ} 20^{\prime} 02.2^{\prime \prime} \mathrm{N}$ |
| 7 | Razi Hospital | $48^{\circ} 40^{\prime} 21.8^{\prime \prime} \mathrm{E}$ | $31^{\circ} 19^{\prime} 37.3^{\prime \prime} \mathrm{N}$ |
| 8 | Fatemeh Zahra Hospital, Ahvaz | $48^{\circ} 40^{\prime} 22.3^{\prime \prime} \mathrm{E}$ | $31^{\circ} 18^{\prime} 45.6^{\prime \prime} \mathrm{N}$ |
| 9 | Water entertainment complexes and restaurants <br> S \& D | $48^{\circ} 39^{\prime} 48.11^{\prime \prime}$ | $31^{\circ} 18^{\prime} 10.9^{\prime \prime} \mathrm{N}$ |
| 10 | Sina Hospital | $48^{\circ} 38^{\prime} 27.3^{\prime \prime} \mathrm{E}$ | $31^{\circ} 14^{\prime} 17.2^{\prime \prime} \mathrm{N}$ |
| 11 | Shahid Baghaei Hospital | $48^{\circ} 35^{\prime} 04.8^{\prime \prime} \mathrm{E}$ | $31^{\circ} 15^{\prime} 58.3^{\prime \prime} \mathrm{N}$ |
| 12 | Southeast Water Company | $48^{\circ} 36^{\prime} 16.7^{\prime \prime} \mathrm{E}$ | $31^{\circ} 13^{\prime} 55.2^{\prime \prime} \mathrm{N}$ |
| 13 | Iran National Steel Industrial Group | $48^{\circ} 35^{\prime} 01.9^{\prime \prime} \mathrm{E}$ | $31^{\circ} 15^{\prime} 57.5^{\prime \prime} \mathrm{N}$ |
| 14 | Ahvaz Pipeline Navard | $48^{\circ} 35^{\prime} 08.0^{\prime \prime} \mathrm{E}$ | $31^{\circ} 15^{\prime} 59.5^{\prime \prime} \mathrm{N}$ |
| 15 | Abattoir | $48^{\circ} 25^{\prime} 52.9^{\prime \prime} \mathrm{E}$ | $31^{\circ} 08^{\prime} 42.6^{\prime \prime} \mathrm{N}$ |
| 16 | Ramin Power Station | $48^{\circ} 52^{\prime} 27.8^{\prime \prime} \mathrm{E}$ | $31^{\circ} 30^{\prime} 17.2^{\prime \prime} \mathrm{N}$ |

Fig. 5 Potential pollution points (P1...P16)



Table 3 Results of $\mathrm{M}_{\mathrm{h}}$ and NPSP methods for potential sampling points' priority

| Alternate sampling <br> point |  | Pl | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | P10 | P11 | P12 | P13 | P14 | P15 | P16 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 2 <br> $\frac{2}{\pi}$ <br> $\sum$ <br> $\sum$ | Spring | 127.6 | 254.2 | 127.6 | 507.4 | 127.6 | 254.2 | 127.6 | 1013.9 | 127.6 | 254.2 | 127.6 | 507.4 | 127.6 | 254.2 | 127.6 | 1013.9 |
|  | Summer | 43 | 85.1 | 43 | 169.3 | 43 | 85.1 | 43 | 337.8 | 43 | 85.1 | 43 | 169.3 | 43 | 85.1 | 43 | 337.8 |
|  | Fall | 87.9 | 174.8 | NA | 348.6 | 87.9 | 174.8 | 87.9 | 696.3 | 87.9 | 174.8 | 87.9 | 348.6 | 87.9 | 174.8 | 87.9 | 696.3 |
|  | Winter | 159.5 | 318 | 159.5 | 635.1 | 159.5 | 318 | 159.5 | 1269.2 | 159.5 | 318 | 159.5 | 635.1 | 159.5 | 318 | 159.5 | 1269.2 |
| $h$ |  | 4 | 3 | 4 | 2 | 4 | 3 | 4 | 1 | 4 | 3 | 4 | 2 | 4 | 3 | 4 | 1 |
| NPSP |  | 23.02 | 22.41 | 24.24 | 24.38 | 22.77 | 22.56 | 23.02 | 21.05 | 22.61 | 22.00 | 21.91 | 21.62 | 21.97 | 21.49 | 21.49 | 21.73 |
| Priority <br> of the <br> sampling <br> point | Spring | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 1 | 2 | 2 | 3 | 1 | 3 | 2 | 3 | 1 |
|  | Summer | 2 | 3 | 1 | 1 | 3 | 2 | 2 | 1 | 3 | 2 | 3 | 1 | 3 | 2 | 3 | 1 |
|  | Fall | 2 | 3 | 1 | 1 | 3 | 2 | 2 | 1 | 3 | 2 | 3 | 1 | 3 | 2 | 3 | 1 |
|  | Winter | 1 | 3 | 1 | 1 | 3 | 2 | 2 | 1 | 2 | 2 | 3 | 1 | 3 | 2 | 3 | 1 |

The red color shows the higher priority of a candidate point and green color shows the low priority in different seasons.



(a)



(c)



(b)



(d)

Fig. 6 Priority of sampling points in different seasons using the modified Sanders approach (a, b, c, and d)


Fig. 7 Priority of sampling points in different seasons using the combination of modified Sanders and NPSP approaches (a, b, c, and $\mathbf{d})$

## Summary and conclusions

In this study, the effect of seasonal variability in selection of optimal locations of a WQMN across a river was investigated. We used MIKE 11 for hydrodynamic and water quality (lead concentration) simulation in a 113-km branch of Karoon River, southwest of Iran, in various seasons. For determining optimal locations of sampling points in the WQMN, we used the modified Sanders approach by an optimal hierarchy level. The NPSP method was used to find the priority of sampling points in different seasons. The results highlighted that 16 potential sampling points (without considering the seasonality effect) were reduced to 5-6 points in various seasons.

The results illustrated that locations and the number of sampling sites could vary seasonally because the concentration of lead could vary across seasons. It was obvious that considering the simulation of in-stream lead concentration, human activities, and contributing area provided more information on how to prioritize the sampling points for an effective design of WQMN.

Although some of the existing stations are already near the optimal locations found in this study, it must be considered that for a more effective water quality monitoring, more sampling points should be implemented in the study area. More comprehensive results would be achieved when all the contributing data such as point source pollution sources, rainfall-runoff, and other pollution element statistics are integrated to the approach presented in the present study. Future research should focus on incorporating these to provide a fuller picture of the location of the sampling points for effective WQMN design.

Acknowledgements We appreciate Dr. Hossein Babazadeh at Science and Research Branch of Islamic Azad University Tehran for his expert advice and encouragement throughout this project and Dr. Samane Abdoveys at Ahvaz Water utility Company for providing valuable data.

Data availability The datasets generated during and/or analyzed during the current study are available from the corresponding author on reasonable request.

## References

Ahmadisharaf, E., Camacho, R. A., Zhang, H. X., Hantush, M. M., \& Mohamoud, Y. M. (2019). Calibration and validation of watershed models and advances in uncertainty analysis in TMDL studies. Journal of Hydrologic Engineering, 24(7), 03119001.

Akan, J., Abdulrahman, F., Sodipo, O., Ochanya, A., \& Askira, Y. (2010). Heavy metals in sediments from River Ngada, Maiduguri Metropolis, Borno State, Nigeria. Journal of Environmental Chemistry and Ecotoxicology, 2(9), 131-140.

Alilou, H., Moghaddam Nia, A. M., Keshtkar, H., Han, D., \& Bray, M. (2018). A cost-effective and efficient framework to determine the water quality monitoring network locations. Science of the Total Environment, 624, 283-293.

Alilou, H., Moghaddam Nia, A. M., Saravi, M. M., Salajegheh, A., Han, D., \& Enayat, B. B. (2019a). A novel approach for selecting sampling points locations to river water quality monitoring in data-scarce regions. Journal of Hydrology, 573, 109-122.

Alilou, H., Rahmati, O., Singh, V. P., Choubin, B., Pradhan, B., Keesstra, S., Ghiasi, S. S., \& Sadeghi, S. H. (2019b). Evaluation of watershed health using Fuzzy-ANP approach considering geo-environmental and topo-hydrological criteria. Journal of Environmental Management, 232, 22-36.

Behmel, S., Damour, M., Ludwig, R., \& Rodriguez, M. (2016). Water quality monitoring strategies - a review and future perspectives. Science of the Total Environment, 571, 1312-1329.

Beveridge, D. L., Cheatham, T. E., \& Mezei, M. (2012). The $\mathrm{ABCs}$ of molecular dynamics simulations on B-DNA, circa 2012. Journal of Biosciences, 37(3), 379-397.

Chang, C. L., \& Lin, Y. T. (2014a). A water quality monitoring network design using fuzzy theory and multiple criteria analysis. Environmental Monitoring and Assessment, 186(10), 6459-6469.

Chang, C. L., \& Lin, Y. T. (2014b). Using the VIKOR method to evaluate the design of a water quality monitoring network in a watershed. International Journal of Environmental Science and Technology, 11(2), 303-310.

Chen, L., Dai, Y., Zhi, X., Xie, H., \& Shen, Z. (2018). Quantifying nonpoint source emissions and their water quality responses in a complex catchment: A case study of a typical urban-rural mixed catchment. Journal of Hydrology, 559, 110-121.

Choubin, B., Rahmati, O., Soleimani, F., Alilou, H., Moradi, E. and Alamdari, N. (2019). Regional groundwater potential analysis using classification and regression trees. In Spatial modeling in GIS and R for earth and environmental sciences, pp. 485-498, Elsevier.

DHI. (2003). 11: A modelling system for rivers and channels, user guide. Horsholm, Denmark7 DHI—Water and Development.

Do, H. T., Lo, S. L., Chiueh, P. T., \& Thi, L. A. P. (2012). Design of sampling locations for mountainous river monitoring. Environmental Modelling \& Software, 27, 62-70.

Do, H. T., Lo, S. L., Chiueh, P. T., Thi, L. A. P., \& Shang, W. T. (2011). Optimal design of river nutrient monitoring points based on an export coefficient model. Journal of Hydrology, 406(1-2), 129-135.

Doulgeris, C., Georgiou, P., Papadimos, D., \& Papamichail, D. (2012). Ecosystem approach to water resources management using the MIKE 11 modeling system in the Strymonas River and Lake Kerkini. Journal of Environmental Management, 94(1), 132-143.

Dutta, D., Alam, J., Umeda, K., Hayashi, M., \& Hironaka, S. (2007). A two-dimensional hydrodynamic model for flood inundation simulation: A case study in the lower Mekong
river basin. Hydrological Processes: An International Journal, 21(9), 1223-1237.

Dutta, D., Karim, F., Ticehurst, C., Marvanek, S., \& Petheram, C. (2013). Floodplain inundation mapping and modelling in the Flinders and Gilbert Catchments. In A Technical Report to the Australian Government from the CSIRO Flinders and Gilbert Agricultural Resource Assessment, Part of the North Queensland Irrigated Agriculture Strategy: CSIRO Water for a Healthy Country and Sustainable Agriculture flagships.

EPA, U. (2000). Arsenic occurrence in public drinking water supplies. Environmental Protection Agency, Office of Ground Water and Drinking Water supplies.

Gupta, A., Stahl, D. O., \& Whinston, A. B. (1997). A stochastic equilibrium model of Internet pricing. Journal of Economic Dynamics and Control, 21(4-5), 697-722.

Hu, H., Jin, Q., \& Kavan, P. (2014). A study of heavy metal pollution in China: Current status, pollution-control policies and countermeasures. Sustainability, 6(9), 5820-5838.

Kabir, G., \& Hasin, M. A. A. (2011). Comparative analysis of AHP and fuzzy AHP models for multicriteria inventory classification. International Journal of Fuzzy Logic Systems, 1(1), 1-16.

Karamouz, M. (2002). A master plan for water pollution reduction of Karoon River in the province of Khuzestan. Khuzestan Department of Environment.

Kashefipour, S. M., \& Roshanfekr, A. (2012). Numerical modeling of heavy metals transport processes in riverine basins. Numerical Modeling, 6(2), 66-69.

Kordrostami, F., Attarod, P., Abbaspour, K. C., Ludwig, R., Etemad, V., Alilou, H., \& Bozorg-Haddad, O. (2021). Identification of optimum afforestation areas considering sustainable management of natural resources, using geo-environmental criteria. Ecological Engineering, 168, 106259.

Legates, D. R., \& McCabe Jr, G. J. (1999). Evaluating the use of "goodness-of-fit" measures in hydrologic and hydroclimatic model validation. Water Resources Research, 35(1), 233-241.

Liyanage, C. P., Marasinghe, A., \& Yamada, K. (2016). Comparison of optimized selection methods of sampling sites network for water quality monitoring in a river. International Journal of Affective Engineering, IJAE-D-15-00043.

MIKE11, D. H. I. (2015). A modelling system for rivers and channels-reference manual. DHI: Hørsholm, Denmark.

Moriasi, D. N., Gitau, M. W., Pai, N., \& Daggupati, P. (2015). Hydrologic and water quality models: Performance measures and evaluation criteria. Transactions of the ASABE, 58(6), 1763-1785.

Nadal, M., Bocio, A., Schuhmacher, M., \& Domingo, J. (2005). Trends in the levels of metals in soils and vegetation samples collected near a hazardous waste incinerator. Archives of Environmental Contamination and Toxicology, 49(3), 290-298.

Nash, J. E., \& Sutcliffe, J. V. (1970). River forecasting using conceptual models, 1. A Discussion of Principles. J. Hydrol, 10, 280-290.

Ouyang, Y. (2005). Evaluation of river water quality monitoring stations by principal component analysis. Water Research, 39(12), 2621-2635.

Papafilippaki, A., Kotti, M., \& Stavroulakis, G. (2008). Seasonal variations in dissolved heavy metals in the Keritis River, Chania. Greece. Global Nest. the International Journal, $10(3), 320-325$.
Park, S. Y., Choi, J. H., Wang, S., \& Park, S. S. (2006). Design of a water quality monitoring network in a large river system using the genetic algorithm. Ecological Modelling, 199(3), 289-297.

Rahmati, O., Samadi, M., Shahabi, H., Azareh, A., Rafiei-Sardooi, E., Alilou, H., et al. (2019). SWPT: An automated GIS-based tool for prioritization of sub-watersheds based on morphometric and topo-hydrological factors. Geoscience Frontiers, 10(6), 2167-2175.

Rauf, A., Javed, M., \& Ubaidullah, M. (2009). Heavy metal levels in three major carps (Catla catla, Labeo rohita and Cirrhina mrigala) from the river Ravi, Pakistan. Pakistan Veterinary Journal, 29(1).

Sabzipour, B., Asghari, O., \& Sarang, A. (2019). Evaluation and optimal redesigning of river water-quality monitoring networks (RWQMN) using geostatistics approach (case study: Karun, Iran). Sustainable Water Resources Management, 5(2), 439-455.

Sanders, T. G. (1983). Design of networks for monitoring water quality. Water Resources Publication.

Sharp, W. (1971). A topologically optimum water-sampling plan for rivers and streams. Water Resources Research, 7(6), 1641-1646.

Sivertun, A., \& Prange, L. (2003). Non-point source critical area analysis in the Gisselö watershed using GIS. Environmental Modelling \& Software, 18(10), 887-898.

Strobl, G. (2006). Crystallization and melting of bulk polymers: New observations, conclusions and a thermodynamic scheme. Progress in Polymer Science, 31(4), 398-442.

Strobl, R., Robillard, P., Day, R. L., Shannon, R. D., \& McDonnell, A. (2006). A water quality monitoring network design methodology for the selection of critical sampling points: Part II. Environmental Monitoring and Assessment, 122(1-3), 319-334.

Telci, I. T., Nam, K., Guan, J., \& Aral, M. M. (2009). Optimal for river systems. Journal of Environmental Management, 90(10), 2987-2998.

Varekar, V., Karmakar, S., \& Jha, R. (2016). Seasonal rationalization of river water quality sampling locations: A comparative study of the modified Sanders and multivariate statistical approaches. Environmental Science and Pollution Research, 23(3), 2308-2328.

Varekar, V., Karmakar, S., Jha, R., \& Ghosh, N. (2015). Design of sampling locations for river water quality monitoring considering seasonal variation of point and diffuse pollution loads. Environmental Monitoring and Assessment, 187(6), 376.

Wang, Q., Zhao, X., Wu, W., Yang, M. S., Ma, Q., \& Liu, K. (2008). Advection-diffusion models establishment of waterpollution accident in middle and lower reaches of Hanjiang river. Advances in Water Science, 19(4), 500-504.

Wang, Y., Jodoin, P. M., Porikli, F., Konrad, J., Benezeth, Y., \& Ishwar, P. (2014). CDnet 2014: an expanded change detection benchmark dataset. Paper presented at the Proceedings of the IEEE conference on computer vision and pattern recognition workshops.

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.


[^0]:    A. Asadi

    Faculty of Agricultural Sciences and Food Industries, Science and Research Branch of Islamic, Azad University, Tehran, Iran

    e-mail: al.asadi@srbiau.ac.ir

    A. Moghaddam Nia $(\boxtimes) \cdot$ B. Bakhtiari Enayat

    Faculty of Natural Resources, University of Tehran, Tehran, Iran

    e-mail: a.moghaddamnia@utac.ir

    B. Bakhtiari Enayat

    e-mail: bakhtiare@ut.ac.ir

    H. Alilou

    Aquatic Ecodynamics, UWA School of Agriculture and Environment, The University of Western Australia, Crawley, WA 6009, Australia

    e-mail: hossein.alilou@research.uwa.edu.au

[^1]:    E. Ahmadisharaf

    Department of Civil and Environmental Engineering, FAMU-FSU College of Engineering, Tallahassee, FL, USA

    e-mail: eahmadisharaf@eng.famu.fsu.edu

    E. Kimutai Kanda

    Department of Civil and Structural Engineering, Masinde Masinde Muliro University of Science and Technology, Kakamega, Kenya

    e-mail: ekanda@mmust.ac.ke

    E. Chessum Kipkorir

    Department of Civil and Structural Engineering, Moi University, Eldoret, Kenya

    e-mail: ekipkorir@mu.ac.ke

