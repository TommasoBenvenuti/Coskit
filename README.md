### A Qiskit python script to simulate a nmr experiment 

I simulated a quantum circuit with two qubits and two classical bits. My idea was trying to reproduce a Cosy experiment beetween $^{13}C$ and $^{1}H$.

A first rotation of $\pi /2$ along x-axis is firstly applied to both the spins, then the system evolves under an hamiltonian that contains chemical shifts and J-coupling:

$$ 
H = h\cdot w_{H}\cdotI_{z}+ h\cdot w_{C}\cdot I_{z} + 2\pi J I_{H} \cdot I_{C}
$$

I propagated the system for an interval of $t_1 = \frac{1}{2J}$. At the end another $\pi /2$ rotation is applied along x-axis.

