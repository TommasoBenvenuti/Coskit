# Simulating a Simple NMR Experiment with Qiskit

This repository contains a simple Python script to simulate a very basic NMR experiment using **Qiskit**.

I simulated a quantum circuit with two qubits and two classical bits. The idea was to reproduce a simplified **COSY experiment** between $^{13}\mathrm{C}$ and $^{1}\mathrm{H}$.

---

## Pulse Sequence

1. A $\pi/2$ rotation around the x-axis is applied to both spins to prepare transverse magnetization.
   
3. The system evolves under a Hamiltonian containing chemical shifts and isotropic J-coupling:

$$
H = \hbar \omega_H I_{z}^{(H)} + \hbar \omega_C I_{z}^{(C)} 
+ 2\pi J \left(
I_x^{(H)} I_x^{(C)} 
+ I_y^{(H)} I_y^{(C)} 
+ I_z^{(H)} I_z^{(C)}
\right),
$$

where $I_\alpha^{(H/C)}$ are the spin operators of hydrogen and carbon along $\alpha = x, y, z$.

3. The evolution time is chosen as:

$$
t_1 = \frac{1}{2J},
$$

which corresponds to the mixing period in a COSY-like experiment.

4. Another $\pi/2$ rotation around the x-axis is applied to both spins at the end of the sequence.

---

## Density Matrix and Observables

The final density matrix is:

$$
\rho_{\text{final}} = U_{\text{pulse}} \, U(t_1)\, \rho_0\, U^\dagger(t_1) \, U_{\text{pulse}}^\dagger,
$$

with

$$
U(t_1) = e^{-i H t_1 / \hbar}.
$$

The measurable magnetization components can be computed as:

$$
M_\alpha^{(H)} = \mathrm{Tr}\left( \rho_{\text{final}}\, I_\alpha^{(H)} \right), 
\qquad
M_\alpha^{(C)} = \mathrm{Tr}\left( \rho_{\text{final}}\, I_\alpha^{(C)} \right),
$$

with $\alpha = x, y, z$.  

In Qiskit, these measurements are represented as counts on classical bits — not a true FID, but enough to inspect how the system evolves under the pulse sequence.

---

## References / Notes

- $\pi/2$ pulses create transverse magnetization along the chosen axis.  
- The J-coupling term allows coherence transfer between spins in COSY.  
- This is a **very simplified model** for illustrative purposes in quantum simulation.

---
