
## Technical Comments

TECHNICAL COMMENTS are brief discussions of papers previously published in this journal. They should not exceed 1500 words (where a figure or table counts as 200 words). The author of the previous paper is invited to submit a reply for publication in the same issue as the Technical Comment. These discussions are published as quickly as possible after receipt of the manuscripts. Neither AIAA nor its Editors are responsible for the opinions expressed by the authors.

## Comment On "Direct Experimental Evidence Of Electromagnetic Inertia Manipulation Thrusting"

Ricardo L. Marini∗
Instituto Universitario Aeronáutico, 5010 Córdoba, Argentina DOI: 10.2514/1.33196 I N THE paper by Hector H. Brito and Sergio A. Elaskar published in the Journal of Propulsion and Power, Vol. 23, No. 2, March–
April 2007, the fundamentals of a theory about the possibility to obtain a propulsive effect by means of momentum exchange between matter and an electromagnetic field in a closed system are exposed, along with some experimental results. According to this theory, the law of momentum conservation is satisfied by Eq. (4):

$$\int_{V}({\mathbf{g}}^{(m)}+{\mathbf{g}}^{(f)})\mathrm{d}V=\mathrm{const}$$

where g is the momentum density, and the superscripts m and f indicate matter and electromagnetic field, respectively. From this, Eq. (5) is derived:

$${\frac{D}{D t}}\int_{V_{m}}g^{(m)}\mathrm{d}V=-{\frac{D}{D t}}\int_{V_{m}}g^{(f)}\mathrm{d}V$$

which states that the time derivative of the matter momentum is equal to but opposite that of the electromagnetic field. As the time derivative of momentum is the force, after some considerations they arrived at Eq. (8):

$$T\cong-\int_{V_{m}}{\frac{\partial g^{(f)}}{\partial t}}\mathrm{d}V$$

where T is the propulsive force or thrust. For a device composed of an annular capacitor placed inside a toroidal coil, and taking into account the contribution of the Lorenz force into the material, the following final expression for the average thrust was found:

$$\langle T\rangle={\frac{\varepsilon_{r}\varpi n I V d}{2c_{0}^{2}}}\sin\varphi$$

But something seems to be wrong with this theory and the interpretation of the experimental results reported. The electromagnetic momentum (and the force produced by its time variation) is a vector related to the energy flow, and so if the energy is transferred Received 16 July 2007; accepted for publication 28 September 2007.

Copyright © 2007 by the American Institute of Aeronautics and Astronautics, Inc. All rights reserved. Copies of this paper may be made for personal or internal use, on condition that the copier pay the $10.00 per-copy fee to the Copyright Clearance Center, Inc., 222 Rosewood Drive, Danvers, MA 01923; include the code 0748-4658/09 $10.00 in correspondence with the CCC. ∗Aeronautical Engineer, Departamento Vehículos Espaciales, Avenue Fuerza Aérea.

entirely inside the system between the power source and the engine, the energy that leaves the power source produces on it a force equal to but opposite the one exerted on the engine by the energy entering into it, and the same occurs with the energy returned from the engine to the power source if the system operates in a periodical way. So the net average force is null. For this not to occur, the energy must be radiated outside the system, and then if radiation is emitted in a narrow beam, the propulsive force would be equal to the electromagnetic radiation power divided by the speed of light, as is demonstrated by the electromagnetic waves theory.

This situation is analogous to that of a vehicle impelled by a rocket motor. In this case, there is also a momentum exchange now between the vehicle and the working fluid (i.e., combustion gases), and Eqs. (4), (5), and (8) can be rewritten as

$$\int_{V}(g^{(v)}+g^{(g)})\mathrm{d}V=\mathrm{const}$$ $${\frac{D}{D t}}\int_{V}g^{(v)}\mathrm{d}V=-{\frac{D}{D t}}\int_{V}g^{(g)}\mathrm{d}V$$ $${T}=-\int_{V}{\frac{\partial g^{(g)}}{\partial t}}\,\mathrm{d}V$$
Downloaded by WESTERN MICHIGAN UNIVERSITY on February 3, 2015 | http://arc.aiaa.org | DOI: 10.2514/1.B7853TC 
$$(4)$$
$$(\bar{S})$$

where the superscripts v and g mean vehicle and gases, respectively.

If the vehicle traps its own exhaust and returns the gases to the propellant tank to be used again in a closed circuit, the net momentum change of the working fluid is null and no net propulsive force is produced.

On the other hand, the calculation of the average thrust including the Lorentz force given by Eq. (11) was apparently carried out only considering the capacitor and the coil, but neglecting the rest of the elements of the circuit (power source, connection wires, and so on). If all the interactions between the elements of the whole circuit were taken into account, the resultant Lorentz force should be null.

With respect to the experimental results reported, the setup used to detect and eventually measure the resultant net force, consisting of mounting the device as a seismic mass atop a thin cantilever blade forming a flexion pendulum, does not seem to be appropriate for such a purpose. In fact, the engine would theoretically produce a periodically variable force given by T  T0sin2!t-

$$({\boldsymbol{\delta}})$$
$$(\mathrm{l}\,\mathrm{l})$$

where T0 is the maximum force. This can be put as

$\mathbf{S}$ can be put as $\mathbf{S}$. 
$$T=\frac{T_{0}}{2}[1-\cos(2\omega t)]=\frac{T_{0}}{2}\left[1+\sin(2\omega t-\frac{\pi}{2})\right]$$ $$=\frac{T_{0}}{2}+\frac{T_{0}}{2}\sin(2\omega t-\frac{\pi}{2})$$

which means that the total instantaneous force is composed by a constant term (which is the net average force) and a sinusoidal variable component with zero mean value. When the device is in the condition of thrust off, the mass remains ideally at rest at the equilibrium point (but it would actually oscillate about it, owing to environmental perturbations, producing a spurious output signal). When activated, the sinusoidal component of the force will make the mass oscillate about a point that is displaced from the equilibrium position by the constant (average) component. If only the sinusoidal force were produced, as happens with a simple oscillator, then its mean value is equal to zero and the mass will oscillate about a point coincident with the equilibrium position. In both cases, a sinusoidal output signal would be obtained, although no net force is produced in the second one. Conversely, a mere sinusoidal output signal does not implicate that a net resultant force exists. The way to effectively discriminate if there is a net force or not is to measure the displacement of the mass oscillation center from the equilibrium point. If a displacement exists, then an average net force proportional to the displacement will also exist. If there is no displacement, the average net force is null.

The order of magnitude of the displacement produced by the net average force can be estimated considering the system as an ideal flexion pendulum, because the displacements are very small. For such a pendulum, it is

$$\omega^{2}=(2\pi f)^{2}={\frac{k}{m}}$$

where f is the natural oscillation frequency of the pendulum, m is the seismic mass, and k is the elastic constant of the spring. The displacement of the mass produced by a force F is

$$\delta={\frac{F}{k}}={\frac{F}{(2\pi f)^{2}m}}$$

Assuming that the seismic mass is approximately equal to 1 kg and the natural frequency of the system is nearly 2 Hz for a net force of 5 N, such as the one theoretically produced by the engine according to the paper, the displacement of the oscillation center from the equilibrium point would be of about 0:03 m. To clearly appreciate the significance of this magnitude, it can be pointed out that it is about 5% of the visible-light mean wavelength. In the paper, some reference about the sensibility of the piezoelectric transducer alone is made, but nothing is said about the sensibility of the whole test bench. Nevertheless, it seems improbable that this displacement could be measured, or even discriminated from the ground noise and other perturbations, including the one produced by the sinusoidal component of the force, with the experimental equipment employed. Therefore, care must be taken when the experimental results are interpreted as the evidence of a real net average force.

Last but not least, the capacitor and the coil are both energy accumulators. When driven by a periodical voltage, the energy supplied to them by the power source in a semicycle is entirely restored in the following one, at least when dealing with ideal elements. If a force is produced, then work is done when the engine moves. If the force is produced without energy radiation, because neither the capacitor nor the coil waste energy, the work is performed without spending energy. Then the proposed device would be a perpetual-motion machine, at least in a conceptual sense.

G. Spanjers Associate Editor Downloaded by WESTERN MICHIGAN UNIVERSITY on February 3, 2015 | http://arc.aiaa.org | DOI: 10.2514/1.B7853TC 