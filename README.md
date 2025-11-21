# Simulating a Simple NMR Experiment with Qiskit

This repository contains a simple Python script to simulate a very basic NMR experiment using **Qiskit**.

I simulated a quantum circuit with two qubits and two classical bits. The idea was to reproduce a simplified **COSY experiment** between $^{13}\mathrm{C}$ and $^{1}\mathrm{H}$.

---

## Pulse Sequence


1. A $\pi/2$ rotation around the x-axis is applied to both spins to prepare transverse magnetization.
   
2. The system evolves under a Hamiltonian containing chemical shifts and isotropic J-coupling:

$$
H = \hbar \omega _H I_{z}^{(H)} + \hbar \omega _C I_{z}^{(C)}  + 2\pi J \left(\hat{I}^{(C)}\cdot  \hat{I}^{(H)}\right)
$$

where $I_\alpha ^{(H/C)}$ are the spin operators of hydrogen and carbon along $\alpha = x, y, z$.

3. The evolution time is chosen as:

$$
t_1 = \frac{1}{2J},
$$

which corresponds to the mixing period in a COSY-like experiment.

4. Another $\pi/2$ rotation around the x-axis is applied to both spins at the end of the sequence.

---
# 1. Initial State

For a two-spin-½ system, the initial state is:

$$
|\psi _0 \rangle = |s_1\rangle \otimes |s_2\rangle 
$$

where each single-spin state is a 2-component vector (e.g. eigenstates of $\(I_z\)$).
Thus the full Hilbert space is 4-dimensional, and all operators are constructed as Kronecker products of single-spin operators.

---

# 2. Pulse as a Rotation

A pulse acting on spin $\(k\)$ corresponds to a rotation operator $\(R^{(k)}(\theta,\hat{n})\)$ acting only on that spin:

$$
R^{(k)} =
\begin{cases}
R(\theta ,\hat{n}) \otimes \mathbb{I}, & k = H, \\
\mathbb{I} \otimes R(\theta ,\hat{n}), & k = C,
\end{cases}
$$

where, for example, rotation along x-axis is described as:

$$
R_{x}(\theta) =
\begin{pmatrix}
cos(\theta / 2)  & -i sin(\theta / 2) \\ 
 -i sin(\theta /2) & cos(\theta / 2) 
\end{pmatrix}
$$

The full rotation is again a \(4 \times 4\) operator constructed by Kronecker products.

---

# 3. Density Matrix Evolution

After the pulse, the system evolves freely under the Hamiltonian:

$$
\rho_ {\text{final}} = U(t_1) \cdot \rho _0 \cdot U^\dagger(t_1)
$$

with:

$$
U(t_1) = e^{-i H t_1 / \hbar}.
$$

This is the standard unitary time evolution for closed quantum systems.

---

# 4. Observable Magnetization

It is not recorded a FID, but the final state is studied by counts on two classical bits. For this reason, the model is very simple
