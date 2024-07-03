

AIAA-95-2776

# Bimodal System Design Using a Pin-Cermet Reactor and Brayton Power Conversion 

Abraham Weitzberg<br>NUS<br>910 Clopper Road<br>Gaithersburg, MD 20878<br>Alan T. Josloff<br>Martin Marietta Astro Space<br>Bldg B - 2nd Floor<br>720 Vandenberg Road<br>King of Prussia, PA 19101<br>Jack F. Mondt<br>Jet Propulsion Laboratory<br>4800 Oak Grove Drive<br>Pasadena, CA 9109

## 31st AIAA/ASME/SAE/ASEE Joint Propulsion Conference and Exhibit July 10-12, 1995/San Diego, CA

# BIMODAL SYSTEM DESIGN USING A PIN-CERMET REACTOR AND BRAYTON POWER CONVERSION 

Abraham Weitzberg<br>NUS<br>910 Clopper Road<br>Gaithersburg, MD 20878

Alan T. Josloff<br>Martin Marietta Astro Space<br>Bldg B - 2nd Floor<br>720 Vandenberg Road<br>King of Prussia, PA 19101

Jack F. Mondt<br>Jet Propulsion Laboratory<br>4800 Oak Grove Drive<br>Pasadena, CA 9109


#### Abstract

As part of the DOE contribution to the joint Air Force Phillips Laboratory-Department of Energy Bimodal Program, a bimodal (power and propulsion) reactor concept that made use of two different fuel types was studied. With the exception of refractory metal vacuum gaps between the components containing hydrogen propellant and the refractory metal components containing lithium, and high temperature liquid metal-gas heat exchangers, the concept, identified as Nuclear Engine for Bimodal Applications (NEBA) -3 , uses previously developed and demonstrated technologies, including high efficiency closed Brayton cycle turboalternator-compressors for power production. Using near-term technology NEBA-3 can, as an upper stage to an Atlas IIAS launch vehicle, provide propulsion with specific impulse of about 850 seconds at thrusts of 90 to 925 Newtons, and 10 kilowatts of electricity for ten years. Based on previous cost estimates by DOE and NASA, a minimum program could deliver a flight system such as NEBA-3 within six years at a cost of from $\$ 500$ to $\$ 700$ million. The US space reactor power and propulsion community now has the technical capability to deliver such a system early in the next century.


## Introduction

One early objective of the joint Air Force/Department of Energy Bimodal Program was to develop concepts that would minimize the need for costly and time consuming new development programs. Based on this approach the pin and cermet power and propulsion reactor concept was proposed by Weitzberg and Warren ${ }^{1}$ to utilize previously developed propulsion and power fuels. For propulsion, $\mathrm{W}-\mathrm{UO}_{2}$ cermet fuel, as developed in the GE-710 2 and ANL Nuclear Rocket Programs ${ }^{3}$, was selected. This fuel had been demonstrated for tens of hours up to 1.2 atom percent burnup, at temperatures up to about $3000 \mathrm{~K}$. For long term power generation, UN pin fuel with $\mathrm{PWC}-11$ alloy cladding was selected. As part of the recent SP100 Program $^{4}$ this fuel demonstrated seven year equivalent lifetime with greater than six atom percent burnup, at temperatures is the range of $1400-1500 \mathrm{~K}$. For NEBA-3 power conversion, a 100 percent redundant closed Brayton cycle (CBC) turbinealternator subsystem was selected, because of the performance and lifetime data base from commercial and aircraft applications and from prior NASA and DOE programs. The high efficiency of the CBC also allows the reactor to operate at relatively low power levels over its 10 -year life, minimizing the long-term power density and temperature of the cermet fuel.

The NEBA-3 design approach was to assemble components from prior programs and, with minimum change, determine if the system met the requirements of the Bimodal Program. The development status of the major components identified for NEBA-3 is summarized in Table 1. It can be seen that the only new components are the Reactor Interface Attachment and the liquid metal-gas heat exchangers.

## Spacecraft Design

The basic system was designed to produce a thrust of slightly over 90 Newtons (called low thrust) for up to 200 hours, together with the net production of ten kilowatts of electricity for ten years. Because the reactor and shield size and mass were found to change very little for different power levels, two other options were examined using the same basic core design. The first option would produce the same $90 \mathrm{Newtons}$ of thrust, but would produce only five kilowatts of electricity as a result of linear scaling of most of the CBC and heat rejection subsystems. The second option would provide a tenfold increase of thrust to

"Copyright (C) 1995 by A. Weitzberg. Published by the American Institute of Aeronautics and

Table 1

STATUS OF MAJOR COMPONENTS

| SUBSYSTEM | COMPONENT | DEVELOPMENT STATUS |
| :---: | :---: | :---: |
| Reactor | Pin Fuel | SP-100 |
|  | Vessel/Internals | SP-100 |
|  | Cermet Thrust Element | Recover from GE-710, ANL |
|  | Interface Attachment | New |
| Shield |  | SP-100 |
| Primary Heat Transport | TEM Pump | SP-100 (cold side) |
|  | Gas Separator/Accumulator | SP-100 |
|  | Annular Linear Induction Pump | STATE-OF-ART, ref. ETEC |
|  | Heat Exchangers <br> E | New |
| Reactor Instrument and Control | Drives, Instruments | SP-100 |
| Brayton Power Conversion | Rotating Unit, Regenerative HX <br> Cooler HX | BRU-F, MINI-BRU, Space Station <br> STATE-OF-ART |
| Radiator | Tube and Fin | Space Station |
|  | Pump | Space Station |
| Power Conditioning and Control | Controller, Inverter | STATE-OF-ART |
|  | Parasitic Load Resistor | STATE-OF-ART |
| Structu: {f57414e1a-cbdf-4415-8612-28ec37c20ea2}  | Power Subsystem Support | STATE-OF-ART |
| Hydrogen Transport | Pumps, Tubing | STATE-OF-ART, ref. JL, RI |

over 900 Newtons (called moderate thrust) for tens of hours, while producing ten kilowatts of electricity. The ten kilowatts is the minimum needed to pump the increased mass flowrates of both the lithium coolant and the hydrogen propellant. The increased flowrates required the optimization of the reactor flow passages, the primary loop, pumps, heat exchangers, and the cermet thrust elements.

The hydraulic flow schematic of the various NEBA-3 working fluids is shown in Figure 1. Lithium, represented by the bold solid line in the figure, removes heat from the reactor and delivers it to the $\mathrm{HeXe}$ working fluid of the Brayton engines via the hot side heat exchangers. Prior to entering the heat exchangers, lithium passes through a Gas Separator/ Accumulator (GSA) which scavenges helium bubbles generated by neutron interactions with lithium within the reactor, and accommodates part of the lithium volume expansion from its frozen state to operating conditions. A surface-tension screen within the GSA captures the bubbles, preventing their flow downstream. The lithium then passes through two series hydrogen preheaters that raise the hydrogen temperature prior to it entering the reactor. The $\mathrm{Li} / \mathrm{HeXe}$ heat exchangers are hydraulically in parallel, each serving one Brayton power converter consisting of a rotating turboalternator, a recuperator and a gas cooler. The system is designed to operate with one Brayton engine at 100 percent full power and the other engine dormant for redundancy. To operate both engines at 50 percent power, a gas management system would be required in the event that one engine fails and the other has to increase its power output to 100 percent. Due to the complexity of the gas management device and its reliability, this approach was not selected for this application.

At the exit of the HeXe heat exchangers, the parallel lithium flows are combined and returned to the reactor through a thermoelectric electromagnetic (TEM) pump that provides the hydraulic power for lithium circulation. The TEM pump is cooled at the cold side of the thermoelectric converter by a sodium heat pipe radiator. For the case of the moderate thrust propulsion system, a separate linear induction pump is utilized upstream of the TEM pump to provide the higher lithium throughput required. The induction pump is cooled by radiative heat transfer to hydrogen lines brazed to the outer casing.

The HeXe working fluid for the Brayton converter, after leaving the hot side heat exchanger, is expanded through the turbine which then drives the compressor and alternator. Upon exiting the turbine, the gas enters the recuperator where its temperature is further reduced by preheating the gas stream exiting the compressor before it enters the $\mathrm{Li} / \mathrm{HeXe}$ heat exchangers. After the turbine outlet stream exits the recuperator, it enters the gas cooler where the cycle waste heat is transferred to the tertiary coolant of the radiator.

## $100 / 0$ CBC DESIGN



Figure 1

NEBA-3 Power and Propulsion Flow Schematic

NEBA-3 Spacecraft Configuration The deployed and stowed configurations of the NEBA-3 spacecraft are shown in Figure 2. The figure illustrates the telescoping radiator concept which has been selected in this conceptual design stage as the baseline configuration. The stowed package is constrained by the diameter of the standard Atlas IIAS shroud, with an added fairing extension to accommodate the required liquid hydrogen propellant for the mission. The hydrogen tank shown in the figure is for the case of the moderate thrust system. and includes a 5 percent ullage.

The payload module is located behind the hydrogen tank and has a separation distance of 17 meters from the base of the reactor. The separation distance is dictated by the 7.5 degree one-half cone angle selected for the reference design and the diameter of the fairing at 4.19 meters.

The heat rejection radiator consists of three cylindrical sections, and when deployed acts as the telescoping boom that separates the reactor module from the rest of the spacecraft. The poor view factor to space of this radiator, which translates into higher radiator mass, is more than compensated for by the elimination of a separation boom and the simplicity in its deployment when compared to other radiator configurations investigated.

The layout of the closed Brayton cycle conversion subsystem is illustrated in Figure 3 for the moderate thrust system which includes a linear induction pump and larger lithium-to-hydrogen preheaters. All the CBC components are located aft of the reactor control drives which require open view to space for radiative cooling of the drive motors. Each $\mathrm{CBC}$ unit with its three heat exchangers is packaged such that the pipe lengths for $\mathrm{HeXe}$ flow between components are minimal in order to reduce pressure drops and increase conversion efficiency. The three cylindrical radiator sections are configured in paralle! hydraulically with fiexible fluid lines stowed between the rotating CBC units and the hydrogen propellant tank, wrapping around the perimeter of the deployment mechanism. The liquid hydrogen required to accomplish the mission is the largest component of the spacecraft from both the mass and volume standpoints. Two approaches to package the hydrogen tank in the Atlas IIAS launch vehicle were considered. The internal tank concept stores the tank inside the fairing skin typical of the conventional approach, while the external approach employs the tank surface as part of the fairing skin, thus allowing a wider tank diameter and a shorter tank length. The use of the external tank concept will reduce the fairing extension requirement by about 1.3 meters.

Nuclear Subsystem Design The principal challenge for the pin and cermet reactor concept was to design the reactor core using the two different fuels. As shown in Figure 4, the NEBA-3 reactor consists of an inner power region of PWC-11 clad UN pins cooled by lithium in a PWC-11 vessel, surrounded by eight $\mathrm{W}-\mathrm{UO}_{2}$ cermet propulsion elements each with its own thrust nozzle. There is a radial $\mathrm{BeO}$ reflector, portions of which slide axially to provide startup and operational control.

The key to the reactor design is the interface between the power region and the propulsion region. The forward portion of the interface is insulated with multifoil to permit the heating of the hydrogen propellant to greater than $2500 \mathrm{~K}$, the aft portion is maintained in good thermal contact to allow the cermet to be cooled during the ten years of power operation. Included in this interface is a saw-toothed vacuum gap to prevent hydrogen from diffusing into the PWC-11 and the lithium coolant, during propulsion.

The design of the UN fuel pins of the lithium-cooled power region is essentially the same as the design of the SP-100 fuel pins ${ }^{4}$ The cermet fueled thrust elements would be fabricated in the manner of the elements of the GE-710 Program. Each thrust element would have a separate inlet plenum that would be sealed into the main annular hydrogen plenum at the time of final reactor fueling. This approach would allow acceptance testing of the individual thrust elements prior to assembly. The portions of the $\mathrm{BeO}$ reflector that are fixed also serve as the attachment points for the portions that slide. Spectral shift poisons, rhenium and $\mathrm{B}_{4} \mathrm{C}$, are strategically placed in the fuel pin liner, inner core baffle, and external to the cermet elements, to provide adequate shutdown in case of accidental immersion in water or wet sand. Small adjustments in the actual dimensions of the poisons or addition of poison discs between the UN fuel pellets and the internal $\mathrm{BeO}$ reflectors in the fuel pin, will allow further optimization during final design.

The alternating gap and post arrangement of the vacuum gap allows hydrogen a preferential path to escape to space vacuum, rather than to diffuse to the PWC-11 (NbIZr) structure or the lithium coolant during propulsion operations. The basic method of



-FLIGHT CONFIGURAION-



Figure 2

NEBA-3 Moderate Thrust Spacecraft Configuration



Figure 3

CBC Power System Conceptual Layout



Figure 4

NEBA-3 Low Thrust Reactor Cross-Section
fabrication is the same as that developed for the converter heat exchangers of SP-100. The reactor shield design follows the practice of the SP-100 Program, in particular, the design of the shield for a $10 \mathrm{kWe}$ point design study. Lithium hydride is used for the neutron shielding, tungsten for the gamma shielding, and beryllium is used to conduct heat to the shield exterior for radiation to space.

Because the thermal power is split roughly $50-50$ between the two reactor regions, it is both necessary and beneficial to use most of the heat from the power region to preheat the hydrogen to $1250-1350 \mathrm{~K}$ before it enters the propulsion elements. A monolithic lithium-to-gas heat exchanger design is used for both the hydrogen propellant and helium-xenon of the Brayton converter, with a vacuum gap added for the hydrogen. The balance of the lithium loop and reactor subsystems primarily uses technologies developed and demonstrated during the SP-100 Program.

The Primary Heat Transport Subsystem which connects to the inner reactor vessel, consists of the lithium loop piping, lithium-hydrogen and lithiumhelium-xenon heat exchangers, a thermoelectric electromagnetic (TEM) pump, an annular linear induction (ALI) pump only used for the moderate thrust designs, and a gas separator-accumulator. With the exception of the heat exchangers and the ALI pump, the components of this subsystem are the same designs developed by the SP-100 Program, scaled to the requirements of NEBA-3.

The hot hydrogen tubing of the Propulsion Subsystem is Mo41Re and the hot helium-xenon tubing is $\mathrm{Nb} \mathrm{Zr}$ or PWC-11, both with transition joints to stainless steel for the cooler parts of the gas lines.

In the propulsion mode the TEM pump in series with the ALI pump adds a small pumping increment and in the power mode the ALI pump adds a small hydraulic loss to lithium loop. The CBC produces about 11.2 $\mathrm{kW}$ of 110 volt $\mathrm{AC}$ electricity which provides about ten percent extra pumping margin for propulsion. The ALI pump is a standard design from the Handbook of Electromagnetic Pump Technology ${ }^{5}$, scaled but not optimized for NEBA-3. The use of the ALI pump in the moderate propulsion operations requires the dissipation of about four kilowatts of thermal energy, which can be readily accomplished by cooling with cryogenic hydrogen before it flows into the heat exchangers.
The designs and fabrication techniques for the three heat exchangers are similar, but the materials and dimensions differ, as well as the need to incorporate a vacuum gap in the lithium-hydrogen heat exchangers. The heat transfer surfaces are provided by rectangular blocks (matrices) of refractory metal, through which numerous gas flow holes are drilled by electrodischarge machining (EDM). An additional outer gas containment barrier is added using the HIP process, and the gas plena are added using electron beam or tungsten inert gas welding techniques. For the hydrogen heat exchangers a vacuum gap is placed between the lithium and hydrogen sections, also by the HIP process.

## Closed Brayton Cycle Converter The

Brayton power conversion subsystem consists of two redundant engines. Each engine consists of a hot side heat exchanger, a turbine-alternator-compressor rotating unit, a recuperator heat exchanger and a gas cooler. One of the two Brayton engines operates at full power, and the other engine is shut down in standby condition to be started in case of a failure. There are no valves in the gas loop and no pressure regulation or HeXe gas supply module. The system is filled with a predetermined amount of gas, sealwelded and is ready to operate.

For the NEBA-3 system concept, a derivative of the Brayton Rotating Unit (BRU) was incorporated as the baseline, designated as BRU-F. It uses foil bearings and requires liquid cooling of the alternator stator. Gas bleed flow from the compressor exit is used for cooling of the bearings and for positive pressure on the labyrinth seals. Instead of the Rice alternator, a two-pole, toothless permanent magnet generator is utilized. This generator provides higher efficiency, lower mass, higher reliability, and better cooling than the Rice alternator, and represents the advancement in generator technology.

The relatively low heat rejection temperatures to space resulted in the selection of a pumped loop honeycomb radiator concept for the CBC system. The honeycomb radiator was used in the Space Shuttle as a means for thermal control of power, avionics, crew cabin environment and payloads. For the current Space Station design, the honeycomb radiator will be employed for thermal controls of the photovoltaic system batteries and habitat modules, as well as being selected as the baseline heat rejection concept for the Solar Dynamic Power Module.

Design Analyses Nuclear, thermal-hydraulic, stress, and shielding analyses were performed using available codes. Neutronics issues included maintaining adequate operating and shutdown reactivities, even under accident conditions, and balancing the power splits between the two regions. Thermal hydraulic issues included fuel and material temperatures, coolant and propellant flows and temperatures, and thermal stresses in the fuel, components and structures.

Mass Summary The mass of the low-thrust NEBA-3 system is summarized in Table 2 . With the exception of the Brayton engine control, power conditioning and parasitic load radiator, all the power conversion component masses have been doubled for the redundant $\mathrm{CBC}$ engines.

Table 2

LOW-THRUST SYSTEM MASS BREAKDOWN



## Performance Summary

The propulsive performance of the NEBA-3 system in the low thrust, moderate thrust, and half-moderate thrust operations is summarized in Table 3. The halfmoderate thrust is a five kilowatt variant of the moderate thrust design, and would provide a higher payload at the cost of 76 impulsive burns as opposed to only 38 for the ten kilowatt moderate thrust design. The initial mass to geosynchronous earth orbit (IMGEO) was calculated from standard equations for the low thrust case, and by Air Force Phillips Laboratory staff for the impulsive burn cases. It can be seen that all of the designs would allow the transport of significant payload instrument masses to GEO from low orbit within the target one weck time period.

## Design Issues

System Thaw Because of the low power level of the NEBA-3 system, the thaw of lithium inventory during the initial start-up can best be accomplished using electrical trace heaters radiatively coupled to piping and components. The reactor is selfthawed at the initiation of the start-up command. A thaw screen accumulator in the reactor head is incorporated to accommodate lithium expansion within the reactor to a temperature level above the lithium melting point. Electrical heaters trace the lithium piping, GSA, TEM pump, and lithium/HeXe heat exchangers to ensure thaw progressivity from the reactor. The GSA is provided in the lithium loop to accommodate lithium expansion during thaw.

Increasing from Low to Moderate Thnust The principal issue in increasing the NEBA-3 capability to moderate thrust is the accommodation of an approximate ten-fold increase in power density and coolant and propellant flows. The increase in pumping power is limited by the nominal ten kilowatts of electricity produced by the CBC converter. The required pumping power is minimized by reducing the pressure drops through increase of core deltatemperature, increasing the fuel pin wire wrap diameter, and increasing the width of the lithium downcomer region. The very small magnitude of these required changes only contribute about $6 \mathrm{~kg}$ of the approximately $130 \mathrm{~kg}$ increase in mass going from the low to moderate thrust designs. The largest contributors are: increased hydrogen heat exchanger size, $45 \mathrm{~kg}$; ALI pump, $50 \mathrm{~kg}$; and increased thaw battery size, $22.5 \mathrm{~kg}$.

Vacuum Gap Effectiveness Thermacore staff performed simple hydrogen diffusion calculations for the inner vessel-cermet interface. Using a conservative model, the results showed that per 100 hours of lowthrust propulsion approximately 0.002 grams of hydrogen would diffuse through the Mo41Re rather than be vented to space through the vacuum gap. Thus only a minute amount of lithium hydride could be formed in the lithium coolant loop in the unlikely event of reactor cooldown below the designed standby power state. Similarly, only a minute amount of hydrogen would be available to interact with the PWC-11 (Nb1Zr) reactor vessel wall.

Reliability and Lifetime Substantial work in prior programs forms the basis for the assumptions of adequate reliability, lifetime, and performance of the major NEBA-3 components. However, despite the

Table 3

PERFORMANCE SUMMARY*

Low Thrust<br>Continuous Burn<br>Moderate Thrust<br>Impulsive Burns( 38 )

Power Level (kWe)

Hydrogen Flow Rate ( $\mathrm{g} / \mathrm{s}$ )

Chamber Temperature (K)

Chamber Pressure (MPa [psi])

Isp to final orbit (s)

Thrust ( $\mathrm{N}$ )

Nozzle Expansion Ratio

IMGEO $(\mathrm{kg})$

$10 \mathrm{kWe}$ Bimodal System Mass (kg)

Balance of Spacecraft Mass $(\mathrm{kg})$, including tankage and on-orbit prop

Payload Instrument Mass ( $\mathrm{kg}$ )

Time to GEO (d)

10
11
2542
$2.07[300]$
844
91.1
$100: 1$
$4097^{* *}$

1461
$\sim 1280$
$\sim 1356^{* *}$

4.5

10
110
2610
$2.07[300]$
858
926
$100: 1$
4810
$\sim 1591$
$\sim 1280$
$\sim 1939$

3

Half-Moderate Thrust

Impulsive Burns(76)

5

53.5

$2.07[300]$ 858 450

$100: 1$

4786

$\sim 1346$

$\sim 1280$

$\sim 2160$

7.5

## *Using Atlas IIAS Launch Vehicle <br> ** Increasing Isp to $858 \mathrm{sec}$ increases payload by $48 \mathrm{~kg}$

data bases for a wide range of conditions, confirmation would be required for any new duty cycles. Consistent with industry practice for primary pressure boundaries, the vessel and piping integrity would be ensured by design, test, and quality assurance. The thaw of lines and pumps is accomplished by reliable electric trace heaters. The SP-100 Program demonstrated that the thaw, freeze and rethaw of a lithium system is not a major feasibility issue. The NEBA-3 system could be restarted after cold shutdown in space, but cold shutdown is a less desirable operating strategy than is hot standby with partial power operation. Lithium expansion during lithium freeze, thaw, and rethaw is accommodated by gas separator/accumulators, designed and tested in simulated water loops during the SP-100 Program.

Perhaps the greatest concern over using a Brayton power conversion system in space has been lifetime, which has been evaluated numerous times in many different design studies over the past 30 years. The Brayton lifetime issues divide into three areas: working fluid containment, thermal management of the TAC, and dynamic (rotating) components. The loss of working fluid containment has caused some ground test failures, and this is always a major concern. It is mitigated by maintaining large design margins to keep creep below one percent over the design lifetime, and by designing all joints to be simple butt welds with $100 \% \times$-ray, dye penetrant, and leak test inspections. As a final confirmation, the HeXe containment system would be helium leak tested, both hot and cold, prior to launch.

Brayton System components very similar to the NEBA-3 components are routinely fabricated and used for many industrial applications. Therefore, the infrastructure to design, fabricate and test the Brayton components is in place and available. The industrial equipment is also designed and fabricated for long life unattended operations. The experience, operating history and industrial improvement of component operating lifetimes provide an excellent database for designing and manufacturing hardware to operate in space for ten years or longer.

The U.S. aircraft industry, civilian and military, use turbo-compressors with foil bearings on 45 different aircraft and, discounting the failures of these aircraft turbo-compressor foil bearings caused by starts and stops, the mean time between failures (MTBF) is 11.5 years. Therefore on average, these foil bearings, similar to space TAC bearings, should run continuously unattended for 11.5 years. Further lifetime data for these foil bearings is obtained from experience with large industrial turbo-expanders, with similar foil bearings. One has run continuously without shutdown or maintenance for greater than cight years. Ten have run continuously for over five
years without shutdown or maintenance and are still operating. There are now over 70 industrial turboexpanders in service, and lifetime data should accumulate rapidly.

Testability The evaluation of the testability of the NEBA-3 design follows the SP-100 prooflight approach for the lithium loop, pin fuel, vessel and CBC power conversion. This includes a structural development model and a non-nuclear qualification assembly to test power conversion, launch environments, thaw/startup/freeze and rethaw, and a separate non-nuclear qualification of the cermet propulsion thrust elements. The present NEBA-3 approach to attaching the cermet elements to the vacuum gap defers nuclear fueling until late in assembly/test sequence. It would be performed at same time as the pin fuel is loaded and the reactor is tested for cold criticality before final lithium fill.

Acceptance testing of the flight unit includes fulltemperature non-nuclear testing of the lithium primary loop and CBC power conversion, together with $500-$ $550 \mathrm{~K}$ warm zero-power criticality and performance testing of the full-up system subsequent to the final lithium fill. Acceptance testing of the propulsion subsystem would be by means of cold helium flow tests.

Safety The NEBA-3 designs are passively subcritical in water immersion or wet sand burial accident scenarios. Immediate partial shutdown is achieved after a loss of coolant accident (LOCA), as a direct consequence of the negative lithium void coefficient. The use of lower melting point multifoil insulation on the reactor vessel head would permit radiative cooling of pin fuel after LOCA. However, the use of blowdown hydrogen would be needed for post-LOCA cooling for the case when the low probability accident occurred while in the propulsion mode.

## Program Costs

The starting estimate for the costs of a minimum protoflight program, in which a NEBA-3 flight system is developed, qualified, and brought to a launch site ready for mating with a payload, together with the necessary launch approvals was $\$ 392$ million, taken from an evaluation of a $20 \mathrm{kWe}$ power-only SP-100 system using CBC power conversion ${ }^{6}$. The protoflight approach, in which the hardware used to qualify a spacecraft is also used for an initial demonstration/ validation mission, has become the accepted approach both for commercial and military systems. The costs were for a six-year 'Skunk Works' program with peak annual funding of $\$ 100-120 \mathrm{M}$. The starting costs included 20 percent contractor contingency and ten percent contractor fee, and assumed no full-up nuclear ground testing. Only cold and warm zero-power critical nuclear tests, and a full-up electrically heated system test were included. The addition of cermet propulsion element development and testing, plus other required propulsion-related activities, was estimated to bring the total cost of the first NEBA-3 flight system into the range of $\$ 500-700$ million.

## Acknowledgements

The work described in this document was largely performed under three Department of Energy contracts. It represents the cooperative combined efforts of many individuals and different organizations in numerous locations. Without all of their inputs we would have many more unanswered questions. The participating organizations included: Martin Marietta (Valley Forge, San Jose, and Denver), Jet Propulsion Laboratory, Argonne National Laboratory, Los Alamos National Laboratory, NUS, Thermacore, Energy Technology Engineering Center, Advanced Methods and Materials, the Department of Energy, and the Air Force Phillips Laboratory Bimodal Systems Engineering Team.

## References

1. "Pin and Cermet Hybrid Bimodal Reactor", A. Weitzberg and J. W. Warren, Twelfth Symposium on Space Nuclear Power and Propulsion, DOE CONF-950110, AIP Conference No. 325, 2:741-746, New York, 1995.
2. 710 High-Temperature Gas Reactor Program Summary Report, Volumes I through VI, GEMP-600, General Electric Company, 1968.
3. Nuclear Thermal Rocket Program Terminal Report, ANL-7236, Argonne National Laboratory, June 1966.
4. "The SP-100 Power System", V. C. Truscello and L. L. Rutger, Ninth Symposium on Space Nuclear Power and Propulsion, DOE CONF950104, AIP Conference No. 246, 1:1-23, New York, 1992.
5. Handbook of Electromagnetic Pump Technology, R. S. Baker and M. J. Tessier, 1987.
6. Space Nuclear Power and Propulsion, Final Report, Jay H. Greene, NASA, and Alan R. Newhouse, DOE, September 15, 1992.
