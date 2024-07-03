# Original Article

 Physiology And Impact Of Horizontal Connections

in Rat Neocortex Philipp Schnepel1,2, Arvind Kumar1,2, Mihael Zohar1,2, Ad Aertsen1,2, and Clemens Boucsein1,2 1Bernstein Center Freiburg, Freiburg 79104, Germany, and 2Neurobiology and Biophysics, Faculty of Biology, University of Freiburg, Freiburg 79104, Germany Address correspondence to Philipp Schnepel, Department of Molecular and Cell Biology, University of California Berkeley, 142 Life Sciences Addition, Berkeley, CA, 94520-3200, USA. Email: pschnepel@berkeley.edu

## Abstract

Cortical information processing at the cellular level has predominantly been studied in local networks, which are dominated by strong vertical connectivity between layers. However, recent studies suggest that the bulk of axons targeting pyramidal neurons most likely originate from outside this local range, emphasizing the importance of horizontal connections. We mapped a subset of these connections to L5B pyramidal neurons in rat somatosensory cortex with photostimulation, identifying intact projections up to a lateral distance of 2 mm. Our estimates of the spatial distribution of cells presynaptic to L5B pyramids support the idea that the majority is located outside the local volume. The synaptic physiology of horizontal connections does not differ markedly from that of local connections, whereas the layer and cell-type-dependent pattern of innervation does. Apart from L2/3, L6A provides a strong source of horizontal connections. Implementing our data into a spiking neuronal network model shows that more horizontal connections promote robust asynchronous ongoing activity states and reduce noise correlations in stimulus-induced activity.

Cerebral Cortex, 2014, 1–18 doi: 10.1093/cercor/bhu265 Original Article
  
Key words: cortical network, horizontal connections, laser uncaging, noise correlation, pyramidal neuron

## Introduction

The neocortex of mammals is organized into layers parallel to its surface, each showing distinct anatomical, morphological, and cellular properties (Mountcastle 1998). This organization is believed to help control the input-output flow of the neocortex, and its structural and functional features have been the subject of decades of detailed research, providing sufficient data to formulate general connectivity schemes that suggest major pathways for information transfer and processing across the different layers of the neocortex (Thomson and Bannister 2003; Douglas and Martin 2004). These schemes focus on vertical connectivity and have spawned tremendous efforts in implementing the respective circuits into computational models (Markram 2006). The importance of connectivity along the vertical axis of neocortical networks is suggested by the high connection probability that has been found along this axis (Deuchars et al. 1994; Markram et al. 1997; Holmgren et al. 2003; Song et al.

2005; Yoshimura and Callaway 2005; Thomson and Lamy 2007; Lefort et al. 2009; Kätzel et al. 2011; Levy and Reyes 2012), and which may suggest a dominant role for local information processing within the neocortex. However, over the years, evidence
(mostly from anatomical studies) accumulated showing that nonlocal projections must provide a substantial fraction of inputs to neocortical cells (Burkhalter 1989; Hellwig 2000; Binzegger et al.

2004; Stepanyants et al. 2009). Even though first attempts have been made to characterize the physiology of nonlocal projections in the neocortex (Yoshimura et al. 2000; Berger et al. 2009), as well as in other brain regions, for example, the hippocampus or olfactory bulb (Sayer et al. 1990; Malinow 1991; Pressler and Strowbridge 2006; Atasoy et al. 2008), available data remain very limited, probably due to the low data yield achievable with the available methods.

© The Author 2014. Published by Oxford University Press. All rights reserved. For Permissions, please e-mail: journals.permissions@oup.com 1 In this study, we focus on a subset of nonlocal projections in the neocortical circuit often termed "horizontal projections."
This definition usually includes intra-cortical, intra-areal, longrange projections, which can span several millimeters and mostly run parallel (but also obliquely for cross-layer connections) to the cortical surface. Functionally, horizontal projections within the neocortical network have been implicated in spreading information to motor or higher sensory areas (Wang and Burkhalter 2007; Matyas et al. 2010; De Pasquale and Sherman 2011; Mao et al. 2011), in mechanisms like surround suppression (Adesnik et al. 2012; Sachdev et al. 2012) and as modulators of neural responses, providing "contextual" information from the same and other cortical areas (Behabadi et al. 2012; Petreanu et al.

2012). Furthermore, in carnivores and primates, horizontal projections seem to link populations of cells that share the same stimulus preference over large distances, for example, iso-orientation columns in V1 (Bonhoeffer and Grinvald 1991; Weliky and Katz 1994). Since rodents often lack this clear structural organization, the question arises, whether, in addition to the roles assigned so far, horizontal connections may play a more general role in cortical processing. In the light of recent estimates suggesting that the majority of synaptic connections (∼75%) a neuron receives actually originates from outside the local volume (Stepanyants et al. 2009; Boucsein et al. 2011), it has been hypothesized that horizontal projections could even dominate cortical network dynamics. Finally, these projections may also serve to reduce noise correlations (Cohen and Kohn 2011) and trial-bytrial variability (Arieli et al. 1996; Churchland et al. 2010) and thereby improve signal detection. To elaborate on such a hypothesis, a more detailed description of horizontal projections is warranted in order to advance our understanding of cortical processing.

We show that horizontal projections onto L5B pyramids in rat somatosensory cortex are numerous and exhibit a layer-specific pattern that can depend on postsynaptic cell type. We characterize the physiological properties of these connections and find the strongest projections to L5B pyramids originating in L2/3 as well as L5B and L6A. Including our findings in spiking neuronal network simulations revealed that horizontal projections could, indeed, help to reduce noise correlations and response variability and, thus, improve signal detection in the neocortex.

## Materials And Methods Preparation Of Brain Slices

Parasagittal slices (300 μm thickness) of somatosensory cortex were prepared from Long Evans rats (P25-P35), stored at 33°C for 1 h, and then transferred to a custom-made recording chamber. The cutting angle (10°) was optimized such that apical dendrites were aligned parallel to the slice surface. The slices were constantly superfused at a flow rate of 6 mL/min with artificial cerebro-spinal fluid (ACSF) containing (in m): 125 NaCl, 2.5 KCl, 1 MgCl2, 2 CaCl2, 25 NaHCO3, 1.25 NaH2PO4, and 25 glucose, pH 7.4, gassed with carbogen (95% O2, 5% CO2) at a temperature of 32–35°C. All chemicals were purchased from Sigma–Aldrich if not otherwise noted. Animals were treated according to the University of Freiburg's and German guidelines for the use of animals in research.

## Electrophysiology And Histology

Whole-cell patch-clamp recordings were established from excitatory neurons in all layers of S1 (hind limb/trunk area) using standard procedures. Pipettes pulled from borosilicate glass
(1.5 mm outer diameter, Hilgenberg; 2–5 MΩ) were filled with a solution containing (in m): 125 K-gluconate, 20 KCl, 10 HEPES,
2 MgCl2, 0.5 CaCl2, 2 Na2ATP, 5 EGTA, and 0.4–0.8% Biocytin,



  
adjusted to pH 7.3 with KOH. If not otherwise noted, all recordings were performed in current-clamp mode (AxoClamp2B, Molecular Devices or BVC-700A, Dagan), low-pass filtered at 3 kHz,



and digitized at 20 kHz (CED 1401 Plus, Cambridge Electronic Design). The access resistance was routinely monitored, and the recording was discarded if it surpassed 40 MΩ. The pipette capacitance was compensated for via the capacitance neutralization circuit of the amplifier. The liquid junction potential
(−13 mV) was not corrected for. After recording, slices were fixed in 4% paraformaldehyde overnight. Biocytin-filled cells were visualized using standard procedures (Horikawa and Armstrong 1988). Only cells whose dendritic tree was largely preserved in the slice were included in the analysis and reconstructed with a conventional microscope equipped with a camera lucida module
(Dialux22, Zeiss), if staining quality was sufficient (21 of 49 for excitation profile experiments, see below). In order to classify L5B
pyramidal neurons (L5B-pyr) according to dendritic morphology, basic morphological parameters (number of apical branches, trunk width at 5 µm from the soma, 2D soma size, cf. Gee et al. 2012) from a subset of well-stained neurons (14 of 52) were extracted (cf. Supplementary Fig. 1).

## Imaging And Microscopy

Experiments were performed on an infrared video-microscopy setup (Dodt and Zieglgänsberger 1998) equipped with gradient contrast optics (DGC, Luigs&Neumann) and an infrared-optimized CCD camera (FViewII-IR, Olympus), mounted on a motorized BX-51WI microscope (Olympus). All spatial measurements were acquired from the microscope micromanipulators (LNSM1 or 5, Luigs&Neumann) using a custom written MATLAB
(Mathworks) software package (available from Luigs&Neumann on request). Laminar landmarks were visualized under brightfield illumination (especially the borders of L2/3, L4, L5A, and L5B) at a low magnification (2× objective, NA 0.06, PlanN,
Olympus), and these cytoarchitectonic features were used to define laminar borders for the generation of a layered stimulation pattern covering the visible part of the slice (horizontal extent: ∼±2.5 mm, see Fig. 2B). Since the border between L5B and L6 is not distinguishable at ×2 magnification, it was measured at ×40 magnification (LUMPlanFL N, NA 0.8, Olympus) as the region where the size of cell bodies markedly drops (Tanaka et al.

2011).

  

## Uncaging Experiments

Photostimulation experiments were performed on a laser scanning setup optimized for fast spatio-temporal control (DynamicPhotoStimulation [DPS], Boucsein et al. 2005; Nawrot et al. 2009)
of the UV-laser beam (ENTC II 652, Coherent) via fast, galvanometric scanning mirrors (050 EFT, Laser-Scanning-Kaiser). For uncaging experiments on the physiological properties of synapses, the ACSF contained 400 μ γ-CNB-caged -glutamic acid
(G-7055, Molecular Probes) and 500 μ of the metabotropic glutamate receptor blocker (RS)-MCPG ((RS)-α-Methyl-4-carboxyphenylglycine, Tocris), which decreases the excitotoxic effect of glutamate (Rao et al. 2000) and therefore prolongs recording time. For functional mapping experiments, 80 μ of the NMDA
(-methyl--aspartate) receptor blocker D-AP5 (-2-Amino-5phosphonopentanoic acid, Tocris) was added to prevent bursts of action potentials (APs) in presynaptic cells and increase the resolution of photostimulation (Matsuzaki et al. 2008, cf. their Supplementary Fig. S1). Conversely, the concentration of caged glutamate was increased to 600 μ to retain the effectiveness of photostimulation in eliciting APs.

## Excitation Profiles

In order to determine the excitation profile of putative presynaptic cells, glutamate was uncaged in a 9 × 9 grid with a spacing of 75 μm (2–5 trials; pause: 2 min), centered on the somata of neurons in different layers (Fig. 1A,B, Supplementary Fig. 2A).

These profiles provided an estimation of the stimulation strength with which presynaptic cells in different layers needed to be stimulated to fire at least 1 AP for the mapping of connectivity
(Fig. 1C). The combination of laser power (LP) and pulse duration
(PD) just reaching AP-threshold at the soma was identified. The effective spatial resolution R of uncaging was estimated by calculating the Euclidean distance d of all AP-evoking pixels to the soma of each cell, weighted by the number of APs n, pooled over all trials: R ¼ Pðd × nÞ=Pn: Since there is a linear relationship between LP and PD (Supplementary Fig. 3C), we re-calculated all PDs for a nominal LP of the UV-laser of 25 mW and derived the values for the layer-dependent PD from the calibration (range: 4–7 ms). Within this range of stimulation strengths, perisomatic stimulation reliably led to spiking in most tested neurons, whereas spiking via photostimulation of distal dendrites or di-synaptic driving of spiking was never observed
(Dantzker and Callaway 2000; Schubert et al. 2001; Shepherd et al. 2003, 2005; cf. Supplementary Material and Supplementary Fig. 4).

## Functional Mapping And Synaptic Physiology Experiments

The whole extent of the slice as visible in the brightfield image
(horizontal: ±2.5 mm; vertical: all layers) was stimulated in a grid-like fashion. From our excitation profile data, we adjusted the stimulation strength separately for each layer (Fig. 1E), and the spacing of the stimulation grid was set to 100 μm, which is well above the mean values for the effective spatial resolution R (mean: 44/60 µm for D-AP5/No D-AP5, respectively, cf. Fig. 1D). To avoid consecutive stimulation of neighboring sites, the mapping sequence was spatio-temporally optimized and the inter-stimulus interval was set to 500 ms to allow for the relaxation of postsynaptic responses to the resting membrane potential.

The sequence was repeated 4–10 times for each cell (pause:
2 min). The recorded cell and the approximated contour of its dendritic tree were spared from photostimulation to minimize confounding effects of glutamate released directly on the dendrites of the postsynaptic cells. Such strong direct responses can bias the detection of synaptic events or mask them entirely, making a proper estimation of connection strength difficult. For synaptic physiology experiments, a previously selected subset of functionally connected presynaptic neurons was stimulated 5–30 times with an interval of 2 min. This time span was allowed to obtain stable responses by ensuring full recovery of the slice tissue between stimulations (cf. Supplementary Fig. 5).

## Normalization For Cortical Depth And Curvature

In order to pool data from all experiments, the coordinates of each flashed location had to be normalized for cortical curvature
(horizontal normalization) and different layer thicknesses (vertical normalization, cf. Supplementary Fig. 2B). For vertical normalization, the shortest distance between the flashed location
(X0) and the adjacent layer borders (represented by secondorder polynomial fits) was determined as the layer thickness.

Then, the distance from the flashed location to the lower layer border divided by this thickness was defined as the relative elevation within the layer. For horizontal normalization, the shortest connection from the flashed position to the somato-dendritic axis of the postsynaptic neuron was determined and then divided into equal steps of 50 µm (or into steps of 10% of the distance X0→axis, if X0 was <50 µm from the axis). After each step, a vertical line as in the vertical normalization procedure was defined, and an anchor point was set at the relative elevation determined for the flashed position (X1,2, . . .). Integrating distances along these anchor points provided an estimation of the horizontal distance for the subsequent analysis. For the estimation of average layer thickness, the mean length of all the shortest lines connecting the opposing layer borders from each step was used.

## Response Detection And Data Analysis

All data analysis was carried out in MATLAB, and results are reported as mean ± SEM (standard error of the mean) unless otherwise specified. For linear fits, multilinear regression with a bisquare weighting function and default tuning constant was used (robustfit function of MATLAB). For the analysis of significance between layers, the Kruskal–Wallis (KW) test with Dunn's correction for multiple comparisons was used. If not otherwise noted, the Wilcoxon rank sum test was used for all other analyses of significance (*P < 0.05, **P < 0.01, ***P < 0.001). Postsynaptic responses were detected in a time window of 5–50 ms after stimulus offset (voltage threshold: 0.15 mV above baseline). The window was determined from all excitation profile experiments
(AP-latency range: 4.4–49.4 ms, mean: 12.4 ms, cf. Supplementary Fig. 6C), taking into account an additional ∼1.5 ms for axonal conduction and synaptic delays. Detection of false-positives in the time window of 50 ms due to spontaneous events (∼0.1 Hz on average) was excluded by averaging several maps (4–10) per recorded cell. Stimulation positions that reliably led to EPSP (excitatory postsynaptic potential)-shaped response (visually con-firmed in single trials) within the time window were classified as "connected". Nonresponding positions were classified as "unconnected". Where postsynaptic dendrites were accidentally stimulated directly, this was mainly identified by the symmetrical appearance and the slow rising phase and onset of the response before the detection time window. Since these responses might contain EPSPs that are masked by the stronger direct component, we considered these positions to be equally likely connected or unconnected and classified them as "ambiguous". For synaptic physiology experiments, the same detection criteria were used but ambiguous responses were excluded since the direct component can skew the estimation of physiological parameters. Furthermore, due to the overall low number of trials (range: 5–30, mean: 8.6) and the inherent inability to absolutely control presynaptic firing in time (presynaptic AP-jitter), we could not generate meaningful average traces of postsynaptic responses. Since this would have been a prerequisite for an automated data analysis, we choose to analyze our data as single trials (at least 5) under visual control. We sorted our data and only included projections that consisted of clearly identifiable single EPSPs or bursts of responses with the first EPSP sufficiently separated from the following EPSPs. For bursts of EPSPs, only the first clearly discernible peak was taken into account. All voltage traces were low-pass-filtered with a third-order Butterworth filter at 500 Hz before analysis. In order to rule out possible phase-lag effects and distortion of the synaptic latency measurement, the filtfiltfunction of MATLAB was used (forward-backward filtering). In order to find the actual EPSP onset, the point of maximal slope change closest to threshold was detected by using the first derivative of the voltage response in a 10-ms time window before the threshold was crossed (slope change threshold: 2 × SD [standard deviation]). In ∼30% of the cases, this simple method of onset-detection failed and had to be corrected for manually.

Only responses with smooth rising phases and clearly identifiable peaks were selected. The amplitude of the EPSPs was determined as the difference between onset and peak of the response.

Rise times were measured as the time from 20% to 80% of the peak amplitude.

## Estimating The Number Of Connected Cells

Our estimations on the number of connected cells are based on several assumptions. First, we assume that the EPSPs detected in our postsynaptic cells are caused by direct connections from cells whose somata were located at the position of laser uncaging. We cannot rule out the possibility that polysynaptic pathways were activated, where a group of cells activated by the uncaging of glutamate drive a single cell somewhere else within the slice to fire an AP, which, in turn, has a functional connection to our postsynaptic cell. For a detailed discussion on this issue, see Section 1 of Supplementary Material. Second, we consider the cortical space as having a cylindrical layout as well as homogeneity and isotropy of projections. Although this second set of assumptions does not hold true in the case of single cells, the pooled innervation pattern of several neurons of a given class can be approximated to be isotropic (Hooks et al. 2011; see also Supplementary Fig. 7). This is also evident in the axonal projection patterns of bulk-injected neurons (Burkhalter 1989). Thus, we pooled data from functional mapping experiments by normalizing each experiment for cortical thickness and curvature
(cf. Supplementary Fig. 2B) and assigning each stimulated position to a layer according to the brightfield images from the experiment (Fig. 2B). All positions were then binned at 100-µm intervals, and the relative connectivity Prel at each distance was estimated as the ratio between tested and connected/ambiguous positions in each bin (Fig. 2E) and subsequently fitted with a mono-exponential function (Fig. 2H). Bins at a lateral distance of <300 µm from the somato-dendritic axis or bins that showed more than 20% of ambiguous responses were excluded from fitting to minimize the number of false-positives. It is important to note that Prel is not a measure of connection probability but constitutes an estimation of "relative" connectivity, which is converted to a measure λ of the horizontal extend of connectivity in each layer. To estimate the number of connected cells (Ncon)
from each layer in the volume, a simplified model was assumed:

 $$\mathbf{N_{\text{con}}=\rho2\pi Dc\int_0^\infty P_0e^{-t}}$$
0P0e- 1λx dx;
where ρ denotes the cell density, D the thickness of each layer, c the fraction of excitatory neurons, and P0e- 1λx our model of exponential decay with the measured values for λ, constrained by fixed starting values P0 ¼ P1001=e- 1 λx100 : Fixing the starting values of P0 according to actual measures of local connection probability from literature and only using the derived values of λ in our calculation allows an estimation of Ncon without measuring the actual connection probability at all distances (see Table 1).

## Spiking Neuronal Network

We simulated a network of 50 000 neurons (80% excitatory, 20%
inhibitory), which were modeled as leaky integrate-and-fire neurons (Kumar et al. 2008). Neurons were located on a uniformly spaced grid and organized on a two-dimensional sheet of 2 × 2 mm2. Each neuron received 2500 excitatory and 500 inhibitory inputs from the recurrent network. The connection probability for both excitatory and inhibitory neurons was set to 0.1 within a distance of 200 µm. Beyond that, the connection probability from excitatory to excitatory and excitatory to inhibitory neurons decayed exponentially with a space constant netspace (Fig. 6A).

The 2D sheet of neurons was folded as a torus, such that every neuron received an equal number of connections (Kexc→exc = 2500; Kexc→inh = 500; Kinh→exc = 2500; Kinh→inh = 500). To study the effects of excitatory connectivity space constant, the number of synapses per neuron was kept constant as we varied netspace. In addition, each neuron received Poisson-type excitatory input at a rate νext. Together with netspace, νext and the ratio of recurrent inhibition and excitation (g) were free parameters in our simulations, whereas the space constant of all inhibitory connections to both excitatory and inhibitory neurons was fixed to 0.1. Synapses were modeled as α-function-shaped conductance transients
(time constant 0.33 ms for both excitatory and inhibitory synapses). Synaptic weights were chosen such that each excitatory and Table 1 Layer-dependent parameters for the simplified model of cortical space derived from our data and literature

Layer λ [µm] ρ [cells/mm3]

a D [µm] ca Ncon P100

1 NA 5300 270 0.13 NA NA

2/3 352 52 600 393 0.85 3381 0.19b 4 265 85 700 304 0.89 290 0.02e 5A 141 36 100 290 0.83 216 0.1c 5B 217 36 100 402 0.83 562 0.1c 6A 344 54 000 386 0.87 687 0.04d 6B 173 30 900 132 0.86 23 0.02e

Sum/mean 249 43 000 2177 NA 5159 NA

  
inhibitory synapses generated a PSP of amplitude U[0.1, 0.2 mV]
at −70 mV.

## External Stimulus For Network Simulations

To mimic an external stimulus-induced input from cortical or subcortical structures (e.g., sensory input), we created 1000 Poisson-type spike trains (representing 1000 neurons). The external stimulus was modeled as a step-like increase in firing rate of these external inputs. We chose 400 excitatory and 100 inhibitory cells to receive the external stimulus located around an arbitrary chosen point (stimcenter) in the 2D sheet of neurons. The probability for a neuron to receive an external stimulus decreased exponentially with a stimulus space constant stimspace, from the stimcenter (Fig. 6A). Each of the 1000 input spike trains established a synapse on one of the receiving neurons with a constant connection probability of 10%. Thus, each stimulated neuron received input from 100 neurons from the external input spike trains. Each presentation of the external input lasted for 1 s. In each stimulus presentation, the ongoing activity in the network was different whereas the external spiking input was identical. The spatial spread of the receiving neurons in the network
(stimspace) was systematically varied to study its effect on noise correlations.

## Data Analysis Of Simulated Network Activity

We estimated the average firing rate and the global synchrony in the network by calculating the Fano Factor (FF) of the population activity, which is the ratio of the variance over the mean of the population activity rate. To estimate the FF, we used a rectangular bin of 5 ms. A population of independent Poisson processes yields FFpop = 1, whereas positive correlations in the population activity result in an increase of Varpop and, hence, of FFpop. To estimate the relative change in the synchrony as a function of netspace, we defined ΔFF as FFnetspace0:1 FFnetspace¼0:1
: To estimate the trial-bytrail variability, we calculated the standard deviation of the network response to 10 separate presentations of identical inputs.

Simulations were performed using NEST (http://www.nestinitiative.org, last accessed November 1, 2014). The dynamical equations were integrated at a fixed temporal resolution of 0.1 ms. The data were analyzed using Python (http://www. python.org, last accessed November 1, 2014) and MATLAB. For more details, see Kumar et al. (2008).

## Results

In this study, we provide an estimation of the layer-specific, horizontal connectivity profile and the synaptic properties of horizontal, excitatory projections onto L5B pyramidal neurons in rat somatosensory cortex by using a combination of whole-cell patch-clamp recordings in vitro and photostimulation of presynaptic neurons (Boucsein et al. 2005). Additionally, we tested the potential impact of horizontal projections on basic properties of neuronal networks (e.g., trial-by-trial variability, synchrony, and signal/noise correlations) in a simplified network model integrating the connectivity characteristics found in our experiments.

## Calibration Of Photostimulation Experiments

Since the excitability of neurons by glutamate uncaging can vary between layers and cell types (e.g., due to different resting membrane potential or input resistance, cf. Supplementary Fig. 3A,B), the optimal stimulation strength and spatial resolution for excitatory neurons in each layer was established with the help of excitation profiles (Dantzker and Callaway 2000; Shepherd et al. 2003; Hooks et al. 2011). Intracellular recordings were performed from the major excitatory cell types in Layers 2/3, 4, 5A,
5B, and 6 (recording depth: 94 ± 21 μm, cf. Supplementary Fig. 2A), and glutamate was uncaged in a 9 × 9 grid with a spacing of 75 μm, centered on the somata of the neurons (Fig. 1A,B). Separate calibration experiments were conducted without (control; n = 22) and with D-AP5 (n = 27), an NMDA-receptor blocker that has been shown to stabilize the excitability of neurons in uncaging experiments (Matsuzaki et al. 2008). For both conditions, we estimated the spatial resolution R of photostimulation, that is, the effective radius of uncaging around the cell body in terms of AP generation (cf. Materials and Methods). D-AP5 increased the spatial resolution in most layers, especially in L6
(Fig. 1D). The stimulation strength for both conditions was comparable (Fig. 1E, cf. Materials and Methods) since the concentration of caged glutamate was increased for experiments with D-AP5 to compensate for the missing NMDA-dependent depolarization. D-AP5 also reduced the long-lasting depolarization probably mediated by NMDA currents (Hestrin et al. 1990), significantly reduced the number of APs elicited by each light pulse in L5A/B (Fig. 1F, P < 0.05), and abolished a rise in excitability with consecutive trials (Fig. 1G, Supplementary Fig. 3D). Therefore, we used D-AP5 in our functional mapping experiments to increase the resolution and precision of the stimulation. A distortion of the functional maps due to blockade of purely NMDAreceptor-mediated synapses ("silent" synapses) is unlikely, since they are almost absent after P9–11 (Rumpel et al. 1998).

Nonetheless, D-AP5 was omitted in our synaptic physiology experiments to avoid underestimation of the postsynaptic response amplitude, which, even at membrane potentials around −60 mV, might contain slow, NMDA-dependent components (Hestrin et al. 1990). In addition, we observed that the overall excitability of the slice tissue could vary, probably due to slight differences in slice health or age-dependent effects. Hence, the stimulation strength was adjusted in some functional mapping experiments by increasing the values for the PD by 1–2 ms in order to ensure presynaptic AP generation. In a subset of the control experiments (n = 7 cells from all layers), we tested the impact of this slight increase of stimulation strength and found no significant decrease in spatial resolution (Rnorm = 47.2 ± 9.2 µm compared with Rstrong = 44.2 ± 10.9 µm, P = 1). The mean number of elicited APs showed a tendency for increase which was, however, not significant (NAP-norm = 2 ± 0.6 compared with NAP-strong = 3.6 ± 1.0, P = 0.17, cf. Supplementary Fig. 3E). In summary, our data show that the excitability of neurons in different layers can be controlled by adjusting the stimulation strength accordingly. This reduces the occurrence of bursts of presynaptic APs, which can otherwise lead to a strong over-estimation of synaptic impact, since averaged responses will sometimes contain either only 1 or up to several EPSPs.

## Functional Connectivity Of L5B Pyramidal Neurons

We recorded from 28 L5B-pyr (mean recording depth: 116 ± 19 µm SD) in the hind limb/trunk area of rat primary somatosensory cortex S1, while systematically scanning the surrounding tissue for intact projections (Fig. 2A,B). This region in S1 was chosen because it does not show any particular specialization with respect to its structure (cf. to barrel cortex with its strong columnar arrangement). We recorded EPSP-shaped responses to uncaging events at locations of varying distance from the postsynaptic cell and interpreted them as indicators for intact projections from single presynaptic cells according to established criteria for this approach (Fig. 2C, cf. Boucsein et al. 2005; Nawrot et al. 2009). Responses were then classified as connected, unconnected, or ambiguous (Fig. 2D,E; cf. Materials and Methods), resulting in an overall number of 2260 identified projections. After assigning each presynaptic position to a layer of origin, we normalized for cortical thickness and curvature (see Materials and Methods and Supplementary Fig. 2B). We identified intact projections from cells up to 2 mm lateral to the postsynaptic neuron. This seems surprisingly far considering that many axons are cut during the slicing procedure (Stepanyants et al. 2009), which will lead to an underestimation of the connectivity (but not of the spatial profile, cf. Levy and Reyes 2012), especially for long-range projections. Therefore, the following estimations of horizontal connectivity and its impact will constitute a lower bound. In order to estimate the horizontal extent of connectivity with respect to the vertical axis of the postsynaptic neuron's dendritic tree, we binned the number of responding presynaptic locations along the horizontal axis in steps of 100 µm for each layer and computed a relative value of connectivity (Prel) as the ratio of identified connections over the total number of tested sites
(Fig. 2H). Fitting these values with a mono-exponential function yielded a decay space constant λ (in µm) for each layer of: L2/3:
352; L4: 265; L5A: 141; L5B: 217, L6A: 344; and L6B: 173. Since we could not unequivocally assign a border between L6A and L6B, we split the layer proportionally according to anatomical studies (∼3:1, Beaulieu 1993), which corresponds well to our observation of markedly fewer connections in the lower quarter of L6 (cf.

Fig. 2G). Projections identified as belonging to L1 (0.8% of all identified projections) are reported (yellow circles in Fig. 2G) but were excluded from further analysis since their horizontal extend could not be fit reliably. The decay space constant of horizontal connectivity was highest in Layers 2/3 and 6A (Fig. 2I), showing that these layers are the principal sources of horizontal projections to L5B-pyr.

## Synaptic Properties Of Horizontal Projections

Even though the above-mentioned space constants are not to be confused with connection probabilities, the considerable number of connections preserved in the acute slice preparation necessitates the question about their physiological weight (and, thus, their functional role regarding cortical information processing). To assess the basic synaptic properties of horizontal projections, we performed a second set of experiments, which allowed us to determine possible differences to the properties of local projections. Therefore, we repeatedly stimulated a subset of all projections identified with a mapping procedure as described above while recording the resulting EPSPs (Fig. 3A,B). From 24 L5B-pyr, a total of 449 connections were analyzed with respect to their amplitude, rise time, and coefficient of variation (CV) (Fig. 3D,E,
Supplementary Fig. 5A). Against the expectation of finding weaker projections with increasing distance due to the anatomically predicted decrease in axo-dendritic overlap (Binzegger et al.

2004), we found the properties of horizontal projections to be similar to those of local projections. Although the occurrence of EPSPs with larger amplitudes (>1 mV) decreased with increasing distance for all layers, the distribution of amplitudes compares with that of local projections (Fig. 3D, cf. Lefort et al. 2009; Levy and Reyes 2012), showing a heavy tail and a skewedness toward small amplitudes. The mean amplitude for all characterized connections was 0.46 ± 0.4 mV SD whereas the amplitude CV was generally low (range: 0.07–1.04; mean: 0.39) and did not significantly change with distance for most layers (except L6, P < 0.05, Supplementary Fig. 5A). Since our data set has only limited samples for distances <300 µm, we analyzed the distance dependence of all parameters for the range >300 µm, only. The synaptic strength of horizontal projections did not decrease significantly with distance, showing that projections from larger distances can still have substantial impact on the integration in L5B-pyr. The number of samples for L5A-projections was very low (n = 21), and more data would be needed for a conclusive analysis of their distance-dependent properties. However, we reported the values for the sake of completeness. Whether projecting axons specifically target certain regions on the extended dendritic trees of pyramidal neurons is an open question.

To this end, we analyzed the rise times of EPSPs originating from different layers since dendritic filtering will progressively "slow down" the voltage deflection measured at the soma (Rall 1967; Redman and Walmsley 1983; Stuart et al. 2007). Interestingly, EPSP rise times in the layers providing most of the input were significantly decreasing with distance (slope: L2/3: 18%/mm, P < 0.001; L5B: 21%/mm, P < 0.001; L6: 14%/mm, P < 0.05). This hints at the possibility that, with increasing distance, horizontal projections establish their synapses on the proximal dendrites progressively closer to the soma (Fig. 3E, see also Yoshimura et al. 2000; Behabadi et al. 2012). Along these lines, we compared the mean rise times between layers in order to test for layer-dependent differences. We found that EPSPs originating from L6 rose significantly faster than EPSPs from all other layers (except L4, KW-test, P < 0.001), indicating that these synapses are probably even closer to the soma (Letzkus et al. 2006; Sjöström and Häusser 2006). The mean values for amplitude and amplitude CV for each layer were compared in the same manner but showed no statistically significant difference (KW-test, P = 0.52 and P = 0.46, respectively). In summary, horizontal projections and their basic synaptic properties seem to not differ markedly from their local counterparts, except for lacking very high amplitude EPSPs.

## Theoretical Implications Based On Experimental Findings: Number Of Potentially Connected Cells

Connectivity in the neocortex is believed to be dominated by local projections within and across layers, leading to a more or less columnar mode of information processing (Mountcastle 1997; Douglas and Martin 2004; Hirsch and Martinez 2006; Markram 2006; Feldmeyer 2012). We have observed that a large number (see Table 1) of horizontal projections impinge on L5B-pyr and demonstrated that their physiological properties do not differ markedly from their local counterparts. Thus, we sought to obtain a quantitative estimation of the percentage of all synapses of a given cell that horizontal connections account for. Assuming a simplified cylindrical layout of cortical space as well as homogeneity and isotropy (Fig. 4A, see also Supplementary Fig. 7), we derived a model for the number of potentially connected cells from each layer at a given distance from the postsynaptic neuron
(cf. Materials and Methods). Following our estimation of Prel and integrating over a distance from 0 (soma) to ∼2 mm, we calculated the number of cells that are connected to a L5B-pyr. We compared our estimations with known values for the number of excitatory spines on L5B-pyr and the number of synapses per connection to assess whether our estimated values are in a realistic range. The overall number of connected cells was estimated to be 5159 (see Table 1 for parameters of our model). Taking into account that connections can be multi-synaptic, that is, more
  



  
than 1 synaptic contact per connection (Markram et al. 1997), our numbers fit reasonably well to the mean number of asymmetric synapses on L5B-pyr (17 567, Larkman 1991), considering that extra-cortical projections (e.g., inter-hemispheric) and projections to the distal dendrite (between 20% and 35% of all synapses, Larkman 1991) are not accounted for in our experiments. Although the density of found projections close to the postsynaptic neuron is high (Fig. 4B), our calculation suggests that at least 50%
of all projections do not originate within the local volume, due to the quadratic increase in the number of potential presynaptic partners (Fig. 4A, cf. Boucsein et al. 2011). In addition, we found a separation in terms of contribution between layers on a larger spatial scale (Fig. 4C). According to our estimates, the dominant source of input to L5B is Layer L2/3 followed by L5B and L6A (which contribute equally) whereas the other layers provide less input (Fig. 4D).

Although we assumed homogeneity of connectivity in the above-mentioned model for the sake of simplicity, previous studies have stressed striking differences in local projection patterns to L5B-pyr that can depend on subcortical projection targets (Brown and Hestrin 2009; Anderson et al. 2010; Kiritani et al.

2012), pre- and post-synaptic neuron identity (Song et al. 2005; Kampa et al. 2006), vertical position within the layer (Petreanu et al. 2009), and firing pattern/morphological class (Schubert et al. 2001). We investigated the dependence of the pattern of horizontal projections on the firing pattern of L5B-pyr. We divided our data set according to the observed firing behavior in response to depolarizing current injections into regular- and doublet-spiking (RS, DS) as well as intrinsically bursting (IB) neurons (Fig. 5A). Interestingly, the population of L5B-pyr was rather homogeneous with respect to dendritic morphology ("thicktufted" type, Supplementary Fig. 1, cf. Schubert et al. 2001 for barrel cortex). The spatial connectivity patterns of RS- and DS-cells are comparable with the pooled data set (Fig. 5B). In contrast, IB
cells seem to be lacking horizontal projections from L5B/L6A,
while receiving more input from L2/3 than RS/DS-cells. To quantify these differences, we divided the connectivity space of these 3 types of neurons into 3 regions of interests, the supragranular, granular, and subgranular regions, and computed the average number of found horizontal projections for each of these 3 regions (Fig. 5C). We found that, indeed, IB cells received significantly fewer connections from the subgranular layer (P < 0.01,
  



KW-test) as compared with RS- or DS-cells (Fig. 5C). The 3 cell types did not differ, however, in their connectivity from the supragranular and granular layers. These results suggest that IB
cells may be part of a different subnetwork, possibly integrating different streams of information.

## Functional Consequences Of Large Space Constants Of Inter- And Intra-Layer Connectivity

What could be the functional role of the horizontal connections characterized above? Since they seem to be abundant and of considerable synaptic strength, we implemented a spiking network model parameterized with the space constants from our experimental findings and used it to investigate the impact of horizontal connections on key parameters of network activity. Our first hypothesis was that increasing the number of horizontal connections (or, to increase the space constant of connection probability netspace) should have an impact on the spatio-temporal correlations in the network activity, since the most prominent sources of correlations in the spiking activity in a network are shared inputs (Perkel et al. 1967; Shadlen and Newsome 1998) and the available pool of independent presynaptic units should increase. In our network simulations, we kept the total input to a given neuron (and, likewise, the total output) fixed and systematically increased netspace (Fig. 6A), which, indeed, reduced global synchrony (Fig. 6B). Note that an increase in netspace without controlling for total synaptic input to the neurons would have made the comparison of activity dynamics in networks with different netspace difficult. For the smallest netspace of 0.1, we observed typical synchronous and asynchronous activity regimes as the external excitatory input (νext) and the ratio of recurrent inhibition and excitation (g) was varied (Brunel 2000; Kumar et al. 2008). In line with previous results, asynchronous activity states dominated the regimes with a high recurrent inhibition/excitation ratio
(Fig. 6E). In these regimes, a further dilution of the shared input pool cannot be expected to show an effect on noise correlations due to the overall low correlations. However, for a smaller ratio of recurrent inhibition and excitation (g = 2), we observed strong synchronization with increasing νext. Thus, to study the effect of netspace on global synchrony, we fixed g = 2 and varied netspace systematically. Indeed, the global synchrony decreased as a function of netspace (Fig. 6F,G), whereas the overall firing rate did not change (Fig. 6C,D) because we kept the in- and out-degrees of the neurons fixed. For some parameter values where we observed strong synchrony (e.g., FF ≥ 10), increasing netspace reduced the synchrony by up to 30% (Fig. 6F,G). With weak synchrony in the network, changing netspace did not influence network synchrony much (Fig. 6H).

## Trial Variability Decreases With Connectivity Space Constant

An important aspect of synchrony is that it causes large membrane potential fluctuations and, hence, can introduce large variability in the response to external stimuli (Arieli et al. 1996). Thus, our second hypothesis was that a larger netspace should reduce the trial-by-trial variability. To test this, we stimulated 500 neurons within the network described above with an additional external input (cf. Materials and Methods). The external input was modeled as a rate modulation in the activity of a pool of 1000 neurons outside of the network, also arranged on a 2D sheet. The 2D spatial arrangement of neurons allowed us to



connect the input neurons to the receiving neurons in the recurrent network with a connection probability that decayed with distance. For this inter-layer connectivity, the connection probability decreased exponentially as a function of distance with a space constant stim space . In the 6-layered architecture of the sensory neocortex, this extra input can be thought to represent input from a presynaptic layer. Thus, this model allows us to investigate the effect of the local, intra-layer connectivity space 2105 , 91 years t no yiizovinU InnoitsU nailarusuA adT in \go. clarmoibrol xo.109190\\:qtrd morli bebaol two



constant (here modeled as net space ) and the inter-layer connectivity space constant (here modeled as stim space ). This relates to our experimentally measured values of horizontal connectivity in such that net space would refer to λ LSB whereas stim space would refer to λ of a presynaptic layer (e.g., L2/3 or L6A). Therefore, to study the effect of local connectivity and inter-layer or stimulus connectivity space constants, we systematically varied net apace and stimspace while keeping the other parameters constant
(Fig. 7A ). These simulations confirmed our hypothesis that increasing net apace reduced trial-by-trial variability (Fig. 7B - D ).

In these simulations, both net space and stim space were identical.

Interestingly, for a fixed net space, trial-by-trial variability decreased as we increased stim space (Fig. 7E ). These simulations allow us to speculate on the trial-by-trial variability in different layers of the sensory neocortex. For instance, in a layer with small net space , we would expect higher trial-by-trial variability which, however, could be reduced if projections from the presynaptic layers have larger space constant. We note, however,
,91 guanat no gliziovinU hanoimN mileneuA off is \gio.slamno[bro]xo.100190/\:qiird more babno[uw S 102



that the effects of shared connectivity as shaped by netspace could be restricted to the asynchronous-irregular and synchronous-irregular states of the network activity. Oscillatory dynamics of the network may not be affected in a qualitatively similar manner by connectivity space constants (see Yger et al. 2011). In neocortical networks, the space constants of the local, intra-layer connectivity can be different from the inter-layer connectivity (Thomson and Lamy 2007). In our simulations, we observed that while netspace had a stronger effect, stimspace could also reduce the trial-by-trial variability (Fig. 7E). Thus, our simulation results show that large space constants of the excitatory connectivity in the recurrent network and input projections together can create conditions suitable for minimizing noise correlations and reducing trial-by-trial variability.

## Discussion

We have shown that the number of horizontal projections onto L5B-pyr in rat S1 can be large and that the layer-specific connectivity pattern can depend on postsynaptic cell type. The physiological properties of these projections are comparable with those of local ones, with the strongest projections originating in L2/3 as well as L5B and L6A. Incorporating our data into spiking neuronal network simulations suggests that horizontal projections could contribute to reducing noise correlations and response variability and, therefore, improving signal detection in cortical networks.

## The Fraction Of Local Versus Nonlocal Projections

Anatomical data show that the number of nonlocal projections should balance or even outweigh the amount of local projections
(Stepanyants et al. 2009). Functionally, the data presented here support this prediction from anatomy, resulting in a similar estimation that at least 50% of the synapses a neuron receives originate from outside the local network (Boucsein et al. 2011). In very local populations of neurons, connection probability does either not decrease with distance (Song et al. 2005; Berger et al. 2009; Lefort et al. 2009) or is reasonably well approximated by an exponential decay or the falling part of a Gaussian function (Holmgren et al. 2003; Boucsein et al. 2011; Levy and Reyes 2012). In L5B, connections between L5B-pyr and particularly trans-laminar connections from L2/3 to L5B dominate (Thomson and Lamy 2007),
which is also reflected in our data for horizontal projections. Additionally, we identified L6A→L5B horizontal connections as a comparatively large source of synaptic input, which is surprising, since even local, vertical L6→L5B connections have been reported to be very sparse (Mercer et al. 2005; Lefort et al. 2009). Along these lines, L4→L5B projections are usually reported to be sparse and vertically confined (Lübke et al. 2000; Egger et al. 2008; Lefort et al. 2009; Petreanu et al. 2009). The L4-projections found in our study have a surprisingly large horizontal extent (λ = 265 µm),
which is in accordance with findings from sensori-motor cortex such as the hindlimb area (Kaneko 2013). However, our estimations of their contribution to L5B-pyr-connectivity imply a rather small impact of these projections, since the overall number of connections is rather low (∼5% of all connections, cf. Fig. 4D). Furthermore, our qualitative analysis of cell-type-dependent differences in the connectivity profile of L5B-pyr suggests that specificity also exists on larger spatial scales, arguing for the processing of different streams of information in specific subnetworks of neurons (Kampa et al. 2006; Brown and Hestrin 2009; Kiritani et al. 2012). 

## Properties Of Synaptic Connections

Previous studies employing photostimulation have greatly advanced our understanding of the functional connectivity in many areas of the neocortex (Callaway and Katz 1993; Dalva and Katz 1994; Dantzker and Callaway 2000; Schubert et al. 2001; Briggs and Callaway 2005; Shepherd et al. 2005; Wang et al. 2007; Weiler et al. 2008; Anderson et al. 2010; Hooks et al.

2011). However, most of these studies were restricted to local circuits and reported mostly normalized mean activity or mean depolarization values (Schubert et al. 2001; Shepherd et al. 2005; Matsuzaki et al. 2008). Here, we characterized the physiological details of putative monosynaptic connections (for a detailed discussion concerning the possibility of disynaptic activation pathways, see Supplementary material). Our results compare well with known properties of local synaptic connections, such as the shape of the amplitude distribution and the values of the amplitude CV (Mason et al. 1991; Reyes and Sakmann 1999; Levy and Reyes 2012). However, due to the extended dendritic tree of L5B-pyr and the concomitant filtering effects on voltage transients (Rall 1967), our data are probably biased toward responses with fast kinetics (i.e., originating from synapses that were reasonably close to the soma/site of recording). Nonetheless, we found a significant decrease of rise times with distance, which hints at the possibility of a nonuniform distribution of synaptic contacts on the proximal dendrites of L5B-pyr (Behabadi et al. 2012). One crucial point of difference to local projections is the lack of large amplitude events (>4 mV) in our data, which have been proposed to dominate network processing (Lefort et al. 2009). This might be due to the fact that we spared the local area around the postsynaptic cell from stimulation, thereby under-sampling the region where the strongest projections are presumably located. On the other hand, young animals (∼P14–
P20) are often used in paired recording studies, and in early developmental stages, synaptic efficacy is still high (Berger et al. 2009),
leading to EPSP amplitudes of several millivolts. However, the amplitude of unitary EPSPs decreases with age (Reyes and Sakmann 1999), which may have contributed to our distribution tending toward lower values since we used young adult rats
(P25–35). The lack of large amplitude connections, however, is counterbalanced by the relative abundance of horizontal projections, which implies a potentially strong impact on network processing. Furthermore, especially L6-connections produce fast EPSPs, indicating synaptic contacts close to the soma. This hints at the possibility that these projections have a greater influence on the output of L5B-pyr than previously thought.

## The Role Of Layer 6 In Cortical Processing

Layer 6 represents a substantial part of the rodent primary somatosensory cortex (Beaulieu 1993; DeFelipe et al. 2002; Briggs 2010; Thomson 2010) and contains a highly diverse population of pyramidal neurons with heterogeneous axonal projection patterns (Zhang and Deschênes 1997; Kumar and Ohana 2008; Marx and Feldmeyer 2013; Pichon et al. 2012). Although there are strong indications that especially cortico-cortical but also certain types of cortico-thalamic cells in L6 densely project to L5B (Schubert et al. 2001; Weiler et al. 2008; Hooks et al. 2011; Pichon et al. 2012), the literature on detailed physiological properties of these connections remains anecdotal (n = 1 in rat and cat, respectively, Mercer et al. 2005; n = 2 in mouse, Lefort et al. 2009).

Our data show that horizontal L6→L5B projections are numerous and that their synaptic physiology places them in a position to strongly influence integration in L5B-pyr. Thus, together with the well-documented modulatory influence of L6 on L4 as well as its fast feedback projections to thalamus (Bourassa and Deschênes 1995; Sherman and Guillery 1998; Sillito and Jones 2002; Reichova 2004; Lee and Sherman 2008), our results indicate a potentially strong modulatory effect of L6 cells on the principal output neurons of neocortical networks in L5B. An opposing mechanism for L6 projections has recently been proposed
(Olsen et al. 2012), claiming that L6 activation suppresses the activity of other layers, probably via di-synaptic inhibition. How well these two findings can be reconciled will need further investigations.

## The Role Of Horizontal Projections

Anatomical studies have established the notion that "cortex mostly talks to itself" (Braitenberg and Schüz 1991), based on the fact that the external input arriving in primary sensory areas only represents a small fraction of the overall number of synapses established on cortical neurons. This has been shown in most sensory areas for the main thalamo-cortical projections, where only ∼5–20% of all synapses that L4 neurons receive stem from thalamic sources (Peters and Payne 1993; Ahmed et al. 1994; Gil et al. 1999; Bruno and Sakmann 2006). Conversely, a large number of synapses in a given cortical volume is "unaccounted for" (Binzegger et al. 2004). They have mostly been attributed to thalamo-cortical, inter-hemispheric (Cauller et al. 1998; Petreanu et al. 2007; Rubio-Garrido et al. 2009) or cortico-cortical horizontal projections connecting neighboring regions via far reaching axon-collaterals in supra- and sub-granular layers (Tucker and Katz 2003; Buzás et al. 2006; Larsen et al. 2007; Wester and Contreras 2012) but also to intra-areal horizontal projections. On a structural level, these long-range, often patchy projections can simultaneously minimize the wiring length and the average shortest path between a pair of neurons (Voges et al. 2011). On a functional level, these projections are suggested to provide a substrate for spatial integration of stimulus features beyond the classical receptive field perspective (Chavane et al. 2011). Especially, in higher mammals, a clustering of cells that share tuning properties or other stimulus preferences has been regularly observed
(Rockland and Lund 1983; Bonhoeffer and Grinvald 1991; Weliky et al. 1996; Lund et al. 2003). In numerous subsequent studies, the hypothesis that intra-areal horizontal projections preferentially connect clusters of cells with similar tuning properties was confirmed (e.g., Gilbert and Wiesel 1989; Malach et al. 1993; Stettler et al. 2002 in the macaque; Bosking et al. 1997; Chisum et al. 2003 in tree shrews; Buzás et al. 2006 in cats), whereas others did not find clear preferences (Kisvárday et al. 1997; Yousef et al. 1999) or even a negative correlation between connection probability and tuning similarity (Matsubara et al. 1987). These heterogeneous observations were interpreted as evidence for various specific functions of intra-areal horizontal projections, that is, visual segmentation (Gilbert et al. 1996), contour integration (Li 1998), and orientation-specific center-surround interactions in primary visual cortex (for a review, see Angelucci and Bressloff 2006), or spectral integration of sound components in primary auditory cortex (Ojima and Takayanagi 2004). A more general proposition for the functional role of horizontal projections is the mediation of surround suppression via di-synaptic inhibition of adjacent columns (for a review, see Sachdev et al. 2012). In cortical areas where neither a clear columnar arrangement of cells nor any apparent clustering related to tuning properties was observed so far, as in, for example, rat V1 (Ohki et al.

2005), horizontal projections might still be the substrate to link spatially dispersed excitatory neurons belonging to a functional network (Kampa 2011). However, the apparent lack of specificity may also suggest a more general role for horizontal projections, which is probably more accessible through statistical descriptions and modeling of cortical network dynamics. Along these lines of thinking, strong local connectivity will generally lead to strongly correlated activity in subnetworks of the neocortex, whereas a broader dispersion of presynaptic cells tends to reduce correlations and the overall amplitude of membrane potential fluctuations caused by the so-called ongoing activity.

## Impact Of Horizontal Connections On Network Dynamics

The correlations and fluctuations in the ongoing activity introduce trial-by-trial co-variability of the neural responses (i.e.,
"noise correlations") and are considered detrimental for stimulus encoding in a rate-coding framework (Shadlen and Newsome 1998; Cohen and Kohn 2011). In recurrent random networks, correlations are strongly influenced by shared inputs (Perkel et al.

1967) or pooling of correlations (Bedenbaugh and Gerstein 1997; Rosenbaum et al. 2011). Following the results of the simulations presented in the current study, large space constants of recurrent excitatory connectivity in different layers imply weak noise correlations and small trial-by-trial variability. Alternatively, noise correlations at timescales above 100 ms can be reduced if excitation is closely tracked and canceled by recurrent inhibition (Renart et al. 2010). Recently, Hansen et al. (2012) proposed that tuning of local excitatory inputs and their tracking by recurrent inhibition can reduce noise correlations. In addition, Adesnik and colleagues have shown that distant SOM-interneuron activation via excitatory horizontal projections in rat V1 depends on the size of the presented visual stimulus (Adesnik et al. 2012). These are interesting parallels to our prediction that an increase in stimspace as well as netspace will affect stimulus encoding in neuronal populations, hinting at the possibility that an intricate balance between excitation and inhibition is also preserved on larger spatial scales in the neocortex. Thus, the mechanisms proposed by us and Hansen et al. may work together to shape the response correlation structure. Our simulation results further suggest that also the inter-layer connectivity space constants in-fluence the layer-specific noise correlations (Fig. 7E). It is interesting that L5B as the output layer of the local cortical network has a smaller λ (i.e., netspace) compared with most other layers. Hence, the activity reverberating within L5B should have higher noise correlation and trial-by-trial variability. However, the connectivity space constants of projections from other layers (i.e., stimspace),
especially L2/3 and L6A, are fairly large. Since our calculation on the number of connected cells implicates L2/3 as the strongest contributor, we predict that in the absence of L2/3 inputs, L5 noise correlations would be even higher. This could be tested experimentally by specifically silencing L2/3 neurons using optogenetic methods. Conversely, the large space constant of L6A→L5B
is harder to interpret in this respect, since L6 is supposed to provide modulatory feedback to L5B. More detailed simulations are needed, however, to substantiate and further clarify these ideas on the importance of inter-layer connectivity space constants.

## Outlook

In primary sensory systems, horizontal projections have been implicated in several mechanisms, ranging from spatio-temporal information processing over surround suppression to sensorimotor interactions. Since all types of principal neurons as well as interneurons in all layers are possible targets of horizontal projections (Yang et al. 2013), it will be crucial to investigate the horizontal connectivity of other cell types apart from L5B-pyr covered in this study. On the single neuron level, the idea of dendritic computation (London and Häusser 2005) suggests that spatially extended neurons like L5B-pyr employ compartmentalized processing, using multiple mechanisms such as Ca2+-/NMDAspikes, location dependence of synaptic activation, and differential expression of plasticity (Schiller et al. 2000; Sjöström and Häusser 2006; Kampa et al. 2007; Larkum et al. 2009; Branco et al. 2010; Behabadi et al. 2012). Therefore, it will be essential to extend the study of horizontal projections to other compartments of the dendritic tree of L5B-pyr. These and other more detailed investigations of the potentially powerful impact of horizontal projections on neocortical processing will have to be conducted in order to complete the picture of the neocortical circuit on a larger spatial scale.

## Supplementary Material

Supplementary material can be found at: http://www.cercor.

oxfordjournals.org/.

## Funding

This work was supported by the German Federal Ministry of Education and Research (BMBF grant 01GQ0830 to BFNT Freiburg/ Tübingen), by the German Research Council (DFG-SFB 780 and DFG EXC 1086 BrainLinks-BrainTools), and by EU-InterReg (TIGER).

## Notes

We thank M. Pelko for discussions, T. Lieury for helpful discussions and for implementing parts of the data analysis, H. Gavrilova and M. Spelleken for the immunohistochemistry, and D. Hähnke and H. Andert for morphological reconstructions. Conflict of interest: None declared.

## References

Adesnik H, Bruns W, Taniguchi H, Huang ZJ, Scanziani M. 2012. A
neural circuit for spatial summation in visual cortex. Nature.

490:226–231.

Ahmed B, Anderson JC, Douglas RJ, Martin KAC, Nelson JC. 1994.

Polyneuronal innervation of spiny stellate neurons in cat visual cortex. J Comp Neurol. 341:39–49.

Anderson CT, Sheets PL, Kiritani T, Shepherd GMG. 2010. Sublayer-specific microcircuits of corticospinal and corticostriatal neurons in motor cortex. Nat Neurosci. 13:739–744.

Angelucci A, Bressloff PC. 2006. Contribution of feedforward, lateral and feedback connections to the classical receptive field center and extra-classical receptive field surround of primate V1 neurons. Prog Brain Res. 154:93–120.

Arieli A, Sterkin A, Grinvald A, Aertsen A. 1996. Dynamics of ongoing activity: explanation of the large variability in evoked cortical responses. Science. 273:1868–1871.

Atasoy D, Aponte Y, Su HH, Sternson SM. 2008. A FLEX switch targets channelrhodopsin-2 to multiple cell types for imaging and long-range circuit mapping. J Neurosci. 28:7025–7030.

Beaulieu C. 1993. Numerical data on neocortical neurons in adult rat, with special reference to the GABA population. Brain Res.

609:284–292.

Bedenbaugh P, Gerstein GL. 1997. Multiunit normalized cross correlation differs from the average single-unit normalized correlation. Neural Comput. 9:1265–1275.

  
Behabadi BF, Polsky A, Jadi M, Schiller J, Mel BW. 2012. Locationdependent excitatory synaptic interactions in pyramidal neuron dendrites. PLoS Comput Biol. 8:e1002599.

Berger TK, Perin R, Silberberg G, Markram H. 2009. Frequencydependent disynaptic inhibition in the pyramidal network: a ubiquitous pathway in the developing rat neocortex. J Physiol.

587:5411–5425.

Binzegger T, Douglas RJ, Martin KA. 2004. A quantitative map of the circuit of cat primary visual cortex. J Neurosci. 24:8441–8453.

Bonhoeffer T, Grinvald A. 1991. Iso-orientation domains in cat visual cortex are arranged in pinwheel-like patterns. Nature.

353:429–431.

Bosking WH, Zhang Y, Schofield B, Fitzpatrick D. 1997. Orientation selectivity and the arrangement of horizontal connections in tree shrew striate cortex. J. Neurosci. 17:2112–2127.

Boucsein C, Nawrot M, Rotter S, Aertsen A, Heck D. 2005. Controlling synaptic input patterns in vitro by dynamic photo stimulation. J Neurophysiol. 94:2948–2958.

Boucsein C, Nawrot MP, Schnepel P, Aertsen A. 2011. Beyond the cortical column: abundance and physiology of horizontal connections imply a strong role for inputs from the surround. Front Neurosci. 5:32.

Bourassa J, Deschênes M. 1995. Corticothalamic projections from the primary visual cortex in rats: a single fiber study using biocytin as an anterograde tracer. Neuroscience. 66:253–263.

Braitenberg V, Schüz A. 1991. Anatomy of the cortex: statistics and geometry. Berlin, Germany: Springer.

Branco T, Clark BA, Häusser M. 2010. Dendritic discrimination of temporal input sequences in cortical neurons. Science.

329:1671–1675.

Briggs F. 2010. Organizing principles of cortical layer 6. Front Neural Circuits. 4:3.

Briggs F, Callaway EM. 2005. Laminar patterns of local excitatory input to layer 5 neurons in macaque primary visual cortex.

Cereb Cortex. 15:479–488.

Brown SP, Hestrin S. 2009. Intracortical circuits of pyramidal neurons reflect their long-range axonal targets. Nature.

457:1133–1136.

Brunel N. 2000. Dynamics of sparsely connected networks of excitatory and inhibitory spiking neurons. J Comput Neurosci.

8:183–208.

Bruno RM, Sakmann B. 2006. Cortex is driven by weak but synchronously active thalamocortical synapses. Science.

312:1622–1627.

Burkhalter A. 1989. Intrinsic connections of rat primary visual cortex: laminar organization of axonal projections. J Comp Neurol. 279:171–186.

Buzás P, Kovács K, Ferecskó AS, Budd JML, Eysel UT, Kisvárday ZF.

2006. Model-based analysis of excitatory lateral connections in the visual cortex. J Comp Neurol. 499:861–881.

Callaway EM, Katz LC. 1993. Photostimulation using caged glutamate reveals functional circuitry in living brain slices. Proc Natl Acad Sci USA. 90:7661–7665.

Cauller LJ, Clancy B, Connors BW. 1998. Backward cortical projections to primary somatosensory cortex in rats extend long horizontal axons in layer I. J Comp Neurol. 390:297–310.

Chavane F, Sharon D, Jancke D, Marre O, Frégnac Y, Grinvald A.

2011. Lateral spread of orientation selectivity in V1 is controlled by intracortical cooperativity. Front Syst Neurosci.

5(Article 4):1–26.

Chisum HJ, Mooser F, Fitzpatrick D. 2003. Emergent properties of layer 2/3 neurons reflect the collinear arrangement of horizontal connections in tree shrew visual cortex. J Neurosci.

23:2947–2960.

Churchland MM, Yu BM, Cunningham JP, Sugrue LP, Cohen MR,
Corrado GS, Newsome WT, Clark AM, Hosseini P, Scott BB, et al. 2010. Stimulus onset quenches neural variability: a widespread cortical phenomenon. Nat Neurosci. 13:
369–378.

Cohen MR, Kohn A. 2011. Measuring and interpreting neuronal correlations. Nat Neurosci. 14:811–819.

Dalva MB, Katz LC. 1994. Rearrangements of synaptic connections in visual cortex revealed by laser photostimulation.

Science. 265:255–258.

Dantzker JL, Callaway EM. 2000. Laminar sources of synaptic input to cortical inhibitory interneurons and pyramidal neurons. Nat Neurosci. 3:701–707.

DeFelipe J, Alonso-Nanclares L, Arellano JI. 2002. Microstructure of the neocortex: comparative aspects. J Neurocytol. 31:
299–316.

De Pasquale R, Sherman SM. 2011. Synaptic properties of corticocortical connections between the primary and secondary visual cortical areas in the mouse. J Neurosci. 31:16494–16506.

Deuchars J, West DC, Thomson AM. 1994. Relationships between morphology and physiology of pyramid-pyramid single axon connections in rat neocortex in vitro. J Physiol (Lond).

478(Pt 3):423–435.

Dodt HU, Zieglgänsberger W. 1998. Visualization of neuronal form and function in brain slices by infrared videomicroscopy. Histochem J. 30:141–152.

Douglas RJ, Martin KAC. 2004. Neuronal circuits of the neocortex.

Annu Rev Neurosci. 27:419–451.

Egger V, Nevian T, Bruno RM. 2008. Subcolumnar dendritic and axonal organization of spiny stellate and star pyramid neurons within a barrel in rat somatosensory cortex. Cereb Cortex. 18:876–889.

Feldmeyer D. 2012. Excitatory neuronal connectivity in the barrel cortex. Front Neuroanat. 6:24.

Gee S, Ellwood I, Patel T, Luongo F, Deisseroth K, Sohal VS. 2012.

Synaptic activity unmasks dopamine D2 receptor modulation of a specific class of layer V pyramidal neurons in prefrontal cortex. J Neurosci. 32:4959–4971.

Gilbert CD, Das A, Ito M, Kapadia M, Westheimer G. 1996. Spatial integration and cortical dynamics. PNAS. 93:615–622.

Gilbert CD, Wiesel TN. 1989. Columnar specificity of intrinsic horizontal and corticocortical connections in cat visual cortex. J Neurosci. 9:2432.

Gil Z, Connors BW, Amitai Y. 1999. Efficacy of thalamocortical and intracortical synaptic connections: Quanta, innervation, and reliability. Neuron. 23:385–397.

Hansen BJ, Chelaru MI, Dragoi V. 2012. Correlated variability in laminar cortical circuits. Neuron. 76:590–602.

Hedrick T, Waters J. 2012. Effect of temperature on spiking patterns of neocortical layer 2/3 and layer 6 pyramidal neurons.

Front Neural Circuits. 6:28.

Hellwig B. 2000. A quantitative analysis of the local connectivity between pyramidal neurons in layers 2/3 of the rat visual cortex. Biol Cybern. 82:111–121.

Hestrin S, Nicoll RA, Perkel DJ, Sah P. 1990. Analysis of excitatory synaptic action in pyramidal cells using whole-cell recording from rat hippocampal slices. J Physiol. 422:203–225.

Hirsch JA, Martinez LM. 2006. Laminar processing in the visual cortical column. Curr Opin Neurobiol. 16:377–384.

Holmgren C, Harkany T, Svennenfors B, Zilberter Y. 2003. Pyramidal cell communication within local networks in layer 2/3 of rat neocortex. J Physiol. 551:139–153.

Hooks BM, Hires SA, Zhang Y-X, Huber D, Petreanu L, Svoboda K,
Shepherd GMG. 2011. Laminar analysis of excitatory local
  
circuits in vibrissal motor and sensory cortical areas. PLoS Biol. 9:e1000572.

Horikawa K, Armstrong WE. 1988. A versatile means of intracellular labeling: injection of biocytin and its detection with avidin conjugates. J Neurosci Methods. 25:1–11.

Kampa B. 2011. Representation of visual scenes by local neuronal populations in layer 2/3 of mouse visual cortex. Front Neural Circuits. 5(Article 18):1–12.

Kampa BM, Letzkus JJ, Stuart GJ. 2006. Cortical feed-forward networks for binding different streams of sensory information.

Nat Neurosci. 9:1472–1473.

Kampa BM, Letzkus JJ, Stuart GJ. 2007. Dendritic mechanisms controlling spike-timing-dependent synaptic plasticity.

Trends Neurosci. 30:456–463.

Kaneko T. 2013. Local connections of excitatory neurons in motor-associated cortical areas of the rat. Front Neural Circuits. 7:75.

Kätzel D, Zemelman BV, Buetfering C, Wölfel M, Miesenböck G.

2011. The columnar and laminar organization of inhibitory connections to neocortical excitatory cells. Nat Neurosci.

14:100–107.

Kiritani T, Wickersham IR, Seung HS, Shepherd GMG. 2012. Hierarchical connectivity and connection-specific dynamics in the corticospinal–corticostriatal microcircuit in mouse motor cortex. J Neurosci. 32:4992–5001.

Kisvárday ZF, Tóth E, Rausch M, Eysel UT. 1997. Orientation-specific relationship between populations of excitatory and inhibitory lateral connections in the visual cortex of the cat.

Cereb Cortex. 7:605–618.

Kumar A, Rotter S, Aertsen A. 2008. Conditions for propagating synchronous spiking and asynchronous firing rates in a cortical network model. J Neurosci. 28:5268–5280.

Kumar P, Ohana O. 2008. Inter- and intralaminar subcircuits of excitatory and inhibitory neurons in layer 6a of the rat barrel cortex. J Neurophysiol. 100:1909–1922.

Larkman AU. 1991. Dendritic morphology of pyramidal neurones of the visual cortex of the rat: III. Spine distributions. J Comp Neurol. 306:332–343.

Larkum ME, Nevian T, Sandler M, Polsky A, Schiller J. 2009. Synaptic integration in tuft dendrites of layer 5 pyramidal neurons: a new unifying principle. Science. 325:756–760.

Larsen DD, Wickersham IR, Callaway EM. 2007. Retrograde tracing with recombinant rabies virus reveals correlations between projection targets and dendritic architecture in layer 5 of mouse barrel cortex. Front Neural Circuits. 1:5.

Lee CC, Sherman SM. 2008. Synaptic properties of thalamic and intracortical inputs to layer 4 of the first- and higher-order cortical areas in the auditory and somatosensory systems. J
Neurophysiol. 100:317–326.

Lefort S, Tomm C, Floyd Sarria J-C, Petersen CCH. 2009. The excitatory neuronal network of the C2 barrel column in mouse primary somatosensory cortex. Neuron. 61:301–316.

Letzkus JJ, Kampa BM, Stuart GJ. 2006. Learning rules for spike timing-dependent plasticity depend on dendritic synapse location. J Neurosci. 26:10420–10429.

Levy RB, Reyes AD. 2012. Spatial profile of excitatory and inhibitory synaptic connectivity in mouse primary auditory cortex.

J Neurosci. 32:5609–5619.

Li Z. 1998. A neural model of contour integration in the primary visual cortex. Neural Comput. 10:903–940.

London M, Häusser M. 2005. Dendritic computation. Annu Rev Neurosci. 28:503–532.

Lübke J, Egger V, Sakmann B, Feldmeyer D. 2000. Columnar organization of dendrites and axons of single and synaptically coupled excitatory spiny neurons in layer 4 of the rat barrel cortex. J Neurosci. 20:5300–5311.

Lund JS, Angelucci A, Bressloff PC. 2003. Anatomical substrates for functional columns in macaque monkey primary visual cortex. Cereb Cortex. 13:15–24.

Malach R, Amir Y, Harel M, Grinvald A. 1993. Relationship between intrinsic connections and functional architecture revealed by optical imaging and in vivo targeted biocytin injections in primate striate cortex. PNAS. 90:10469–10473.

Malinow R. 1991. Transmission between pairs of hippocampal slice neurons: quantal levels, oscillations, and LTP. Science.

252:722–724.

Mao T, Kusefoglu D, Hooks BM, Huber D, Petreanu L, Svoboda K.

2011. Long-range neuronal circuits underlying the interaction between sensory and motor cortex. Neuron. 72:111–123.

Markram H. 2006. The blue brain project. Nat Rev Neurosci.

7:153–160.

Markram H, Lübke J, Frotscher M, Roth A, Sakmann B. 1997. Physiology and anatomy of synaptic connections between thick tufted pyramidal neurones in the developing rat neocortex.

J Physiol. 500:409–440.

Marx M, Feldmeyer D. 2013. Morphology and physiology of excitatory neurons in layer 6b of the somatosensory rat barrel cortex. Cereb Cortex. 23(12):2803–2817.

Mason A, Nicoll A, Stratford K. 1991. Synaptic transmission between individual pyramidal neurons of the rat visual cortex in vitro. J Neurosci. 11:72–84.

Matsubara JA, Cynader MS, Swindale NV. 1987. Anatomical properties and physiological correlates of the intrinsic connections in cat area 18. J Neurosci. 7:1428–1446.

Matsuzaki M, Ellis-Davies GCR, Kasai H. 2008. Three-dimensional mapping of unitary synaptic connections by two-photon macro photolysis of caged glutamate. J Neurophysiol.

99:1535–1544.

Matyas F, Sreenivasan V, Marbach F, Wacongne C, Barsy B,
Mateo C, Aronoff R, Petersen CCH. 2010. Motor control by sensory cortex. Science. 330:1240–1243.

Mercer A, West DC, Morris OT, Kirchhecker S, Kerkhoff JE,
Thomson AM. 2005. Excitatory connections made by presynaptic cortico-cortical pyramidal cells in layer 6 of the neocortex. Cereb Cortex. 15:1485–1496.

Mountcastle VB. 1997. The columnar organization of the neocortex. Brain. 120:701–722.

Mountcastle VB. 1998. Perceptual neuroscience: the cerebral cortex. Cambridge, MA: Harvard University Press.

Nawrot MP, Schnepel P, Aertsen A, Boucsein C. 2009. Precisely timed signal transmission in neocortical networks with reliable intermediate-range projections. Front Neural Circuits.

3:1.

Ohki K, Chung S, Ch′ng YH, Kara P, Reid RC. 2005. Functional imaging with cellular resolution reveals precise micro-architecture in visual cortex. Nature. 433:597–603.

Ojima H, Takayanagi M. 2004. Cortical convergence from different frequency domains in the cat primary auditory cortex.

Neuroscience. 126:203–212.

Olsen SR, Bortone DS, Adesnik H, Scanziani M. 2012. Gain control by layer six in cortical circuits of vision. Nature. 483:47–52.

Perkel DH, Gerstein GL, Moore GP. 1967. Neuronal spike trains and stochastic point processes. Biophys J. 7:419–440.

Peters A, Payne BR. 1993. Numerical relationships between geniculocortical afferents and pyramidal cell modules in cat primary visual cortex. Cereb Cortex. 3:69–78.

Petreanu L, Gutnisky DA, Huber D, Xu N, O'Connor DH, Tian L,
Looger L, Svoboda K. 2012. Activity in motor-sensory
  
projections reveals distributed coding in somatosensation.

Nature. 489:299–303.

Petreanu L, Huber D, Sobczyk A, Svoboda K. 2007. Channelrhodopsin-2–assisted circuit mapping of long-range callosal projections. Nat Neurosci. 10:663–668.

Petreanu L, Mao T, Sternson SM, Svoboda K. 2009. The subcellular organization of neocortical excitatory connections. Nature.

457:1142–1145.

Pichon F, Nikonenko I, Kraftsik R, Welker E. 2012. Intracortical connectivity of layer VI pyramidal neurons in the somatosensory cortex of normal and barrelless mice. Eur J Neurosci.

35:855–869.

Pressler RT, Strowbridge BW. 2006. Blanes cells mediate persistent feedforward inhibition onto granule cells in the olfactory bulb. Neuron. 49:889–904.

Rall W. 1967. Distinguishing theoretical synaptic potentials computed for different soma-dendritic distributions of synaptic input. J Neurophysiol. 30:1138–1168.

Rao AM, Hatcher J, Dempsey R. 2000. Neuroprotection by group I metabotropic glutamate receptor antagonists in forebrain ischemia of gerbil. Neurosci Lett. 293:1–4.

Redman S, Walmsley B. 1983. The time course of synaptic potentials evoked in cat spinal motoneurones at identified group Ia synapses. J Physiol. 343:117.

Reichova I. 2004. Somatosensory corticothalamic projections:
distinguishing drivers from modulators. J Neurophysiol.

92:2185–2197.

Renart A, De La Rocha J, Bartho P, Hollender L, Parga N, Reyes A,
Harris KD. 2010. The asynchronous state in cortical circuits.

Science. 327:587–590.

Reyes A, Sakmann B. 1999. Developmental switch in the short-term modification of unitary EPSPs evoked in layer 2/3 and layer 5 pyramidal neurons of rat neocortex. J Neurosci. 19:3827–3835.

Rockland KS, Lund JS. 1983. Intrinsic laminar lattice connections in primate visual cortex. J Comp Neurol. 216:303–318.

Rosenbaum R, Trousdale J, Josi⍰ K. 2011. The effects of pooling on spike train correlations. Front Neurosci. 5:58.

Rubio-Garrido P, Perez-de-Manzo F, Porrero C, Galazo MJ, Clasca F.

2009. Thalamic input to distal apical dendrites in neocortical layer 1 is massive and highly convergent. Cereb Cortex.

19:2380–2395.

Rumpel S, Hatt H, Gottmann K. 1998. Silent synapses in the developing rat visual cortex: evidence for postsynaptic expression of synaptic plasticity. J Neurosci. 18:8863–8874.

Sachdev RNS, Krause MR, Mazer JA. 2012. Surround suppression and sparse coding in visual and barrel cortices. Front Neural Circuits. 6:43.

Sayer RJ, Friedlander MJ, Redman SJ. 1990. The time course and amplitude of EPSPs evoked at synapses between pairs of CA3/CA1 neurons in the hippocampal slice. J Neurosci. 10:
826–836.

Schiller J, Major G, Koester HJ, Schiller Y. 2000. NMDA spikes in basal dendrites of cortical pyramidal neurons. Nature.

404:285–288.

Schubert D, Staiger JF, Cho N, Kötter R, Zilles K, Luhmann HJ. 2001.

Layer-specific intracolumnar and transcolumnar functional connectivity of layer V pyramidal cells in rat barrel cortex.

J Neurosci. 21:3580–3592.

Shadlen MN, Newsome WT. 1998. The variable discharge of cortical neurons: implications for connectivity, computation, and information coding. J Neurosci. 18:3870–3896.

Shepherd GM, Pologruto TA, Svoboda K. 2003. Circuit analysis of experience-dependent plasticity in the developing rat barrel cortex. Neuron. 38:277–289.

Shepherd GM, Stepanyants A, Bureau I, Chklovskii D, Svoboda K.

2005. Geometric and functional organization of cortical circuits. Nat Neurosci. 8:782–790.

Sherman SM, Guillery RW. 1998. On the actions that one nerve cell can have on another: distinguishing "drivers" from "modulators." Proc Natl Acad Sci USA. 95:7121–7126.

Sillito AM, Jones HE. 2002. Corticothalamic interactions in the transfer of visual information. Philos Trans R Soc Lond B
Biol Sci. 357:1739–1752.

Sjöström PJ, Häusser M. 2006. A cooperative switch determines the sign of synaptic plasticity in distal dendrites of neocortical pyramidal neurons. Neuron. 51:227–238.

Song S, Sjöström PJ, Reigl M, Nelson S, Chklovskii DB. 2005. Highly nonrandom features of synaptic connectivity in local cortical circuits. Plos Biol. 3:507–519.

Stepanyants A, Martinez LM, Ferecskó AS, Kisvárday ZF. 2009.

The fractions of short- and long-range connections in the visual cortex. Proc Natl Acad Sci USA. 106:3555–3560.

Stettler DD, Das A, Bennett J, Gilbert CD. 2002. Lateral connectivity and contextual interactions in macaque primary visual cortex. Neuron. 36:739–750.

Stuart G, Spruston N, Häusser M. 2007. Dendrites. Oxford, UK:
Oxford University Press.

Tanaka YR, Tanaka YH, Konno M, Fujiyama F, Sonomura T,
Okamoto-Furuta K, Kameda H, Hioki H, Furuta T, Nakamura KC,
et al. 2011. Local connections of excitatory neurons to corticothalamic neurons in the rat barrel cortex. J Neurosci. 31:
18223–18236.

Thomson AM. 2010. Neocortical layer 6, a review. Front Neuroanat.

4:13.

Thomson AM, Bannister AP. 2003. Interlaminar connections in the neocortex. Cereb Cortex. 13:5–14.

Thomson AM, Lamy C. 2007. Functional maps of neocortical local circuitry. Front Neurosci. 1:19.

Thomson AM, West DC, Wang Y, Bannister AP. 2002. Synaptic connections and small circuits involving excitatory and inhibitory neurons in layers 2–5 of adult rat and cat neocortex:
triple intracellular recordings and biocytin labelling in vitro.

Cereb Cortex. 12:936–953.

Tucker TR, Katz LC. 2003. Spatiotemporal patterns of excitation and inhibition evoked by the horizontal network in layer 2/3 of ferret visual cortex. J Neurophysiol. 89:488–500.

Voges N, Aertsen A, Rotter S. 2011. Structural models of cortical networks with long-range connectivity. Math Probl Eng. 2012:e484812.

Wang H, Peca J, Matsuzaki M, Matsuzaki K, Noguchi J, Qiu L,
Wang D, Zhang F, Boyden E, Deisseroth K, et al. 2007.

High-speed mapping of synaptic connectivity using photostimulation in Channelrhodopsin-2 transgenic mice. PNAS.

104:8143–8148.

Wang Q, Burkhalter A. 2007. Area map of mouse visual cortex. J
Comp Neurol. 502:339–357.

Weiler N, Wood L, Yu J, Solla SA, Shepherd GMG. 2008. Top-down laminar organization of the excitatory network in motor cortex. Nat Neurosci. 11:360–366.

Weliky M, Bosking WH, Fitzpatrick D. 1996. A systematic map of direction preference in primary visual cortex. Nature.

379:725–728.

Weliky M, Katz LC. 1994. Functional mapping of horizontal connections in developing ferret visual cortex: experiments and modeling. J Neurosci. 14:7291–7305.

Wester JC, Contreras D. 2012. Columnar interactions determine horizontal propagation of recurrent network activity in neocortex. J Neurosci. 32:5454–5471.

  

Yang W, Carrasquillo Y, Hooks BM, Nerbonne JM, Burkhalter A.

2013. Distinct balance of excitation and inhibition in an interareal feedforward and feedback circuit of mouse visual cortex.

J Neurosci. 33:17373–17384.

Yger P, El Boustani S, Destexhe A, Frégnac Y. 2011. Topologically invariant macroscopic statistics in balanced networks of conductance-based integrate-and-fire neurons. J Comput Neurosci. 31:229–245.

Yoshimura Y, Callaway EM. 2005. Fine-scale specificity of cortical networks depends on inhibitory cell type and connectivity.

Nat Neurosci. 8:1552–1559.

Yoshimura Y, Sato H, Imamura K, Watanabe Y. 2000. Properties of horizontal and vertical inputs to pyramidal cells in the super-ficial layers of the cat visual cortex. J Neurosci. 20:1931–1940.

Yousef T, Bonhoeffer T, Kim D-S, Eysel UT, Tóth É, Kisvárday ZF.

1999. Orientation topography of layer 4 lateral networks revealed by optical imaging in cat visual cortex (area 18). Eur J
Neurosci. 11:4291–4308.

Zhang Z-W, Deschênes M. 1997. Intracortical axonal projections of lamina VI cells of the primary somatosensory cortex in the rat: a single-cell labeling study. J Neurosci. 17:
6365–6379.
  