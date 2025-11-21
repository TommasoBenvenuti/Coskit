from qiskit import QuantumCircuit, transpile 
from qiskit.quantum_info import Operator, Statevector, DensityMatrix
from qiskit_aer import AerSimulator
import numpy as np
from scipy.linalg import expm
import matplotlib.pyplot as plt
from qiskit.visualization import plot_bloch_multivector, plot_histogram


# =========================
# Parametri
# =========================
w1 = 1          # frequenza Larmor primo qubit  1/s, unità scalate
w2 = w1 / 4     # frequenza Larmor secondo qubit ovvero del carbonio 13C, circa un quarto del protone
J = 1           # accoppiamento J in unità scalate
t1 = 1 / (2*J)  # tempo evoluzione

# =========================
# Inizializzazione circuito
# =========================
qc = QuantumCircuit(2, 2)  # 2 qubit, 2 bit classici

# =========================
# Rotazioni pi/2 intorno a x (entrambi i qubit)
# =========================
qc.rx(np.pi/2, 0) 
qc.rx(np.pi/2, 1)

# =========================
# Hamiltoniane
# =========================
# Operatori singolo qubit (spin-1/2)
I1z_single = 0.5 * np.array([[1, 0],
                             [0, -1]])
I2z_single = 0.5 * np.array([[1, 0],
                             [0, -1]])

I1x_single = 0.5 * np.array([[0, 1],
                             [1, 0]])
I2x_single = 0.5 * np.array([[0, 1],
                             [1, 0]])

I1y_single = 0.5 * np.array([[0, -1j],
                             [1j, 0]])
I2y_single = 0.5 * np.array([[0, -1j],
                             [1j, 0]])

# gli operatori a 2 qubit si ottengono con il prodotto di Kronecker li con l'identità
I1z = np.kron(I1z_single, np.eye(2))
I2z = np.kron(np.eye(2), I2z_single)
# evolve il chemical shift e l'accoppiamento scalare
H_J = 2 * np.pi * J *( np.kron(I1z_single, I2z_single) + np.kron(I1x_single, I2x_single) + np.kron(I1y_single, I2y_single) )
H_tot = w1*I1z + w2*I2z + H_J

# Propagatore unitario
Propagator = expm(-1j * H_tot * t1)
U_gate = Operator(Propagator)

# =========================
# Evoluzione sotto H_tot
# =========================
qc.unitary(U_gate, [0,1], label='U_Htot')

####################################
# Volendo spegnere l'accoppiamento e
#lo shift chimico basta fare un 180 
#intorno ad x per rifocalizzare
####################################

#qc.rx(np.pi,0)
#qc.rx(np.pi,1)

#qc.unitary(U_gate, [0,1], label='U_Htot')


###########################################

# =========================
# Rotazioni pi/2 intorno a x (entrambi i qubit)
# =========================
qc.rx(np.pi/2, 0) #, label='Rx(pi/2)')
qc.rx(np.pi/2, 1) #, label='Rx(pi/2)')

# =========================
# Visualizzazione circuito
# =========================
fig = qc.draw(output='mpl', scale=1.2)
fig.savefig('coskit.png', dpi=300)


# =========================
# Stato finale
# =========================
psi_final = Statevector.from_instruction(qc)
print("Vettore di stato finale (4x1):\n", psi_final.data)

# =========================
# Matrice densità
# =========================
rho = DensityMatrix(psi_final)
print("Matrice densità 4x4:\n", rho.data)

#######################################
# PROVO UNA SIMULAZIONE ( SIATE CLEMENTI )
#######################################

# =========================
# Misura dei qubit
# =========================
qc.measure([0, 1], [0, 1]) # misuro i qubit (0,1) e salvo i risultati nei bit classici (0,1)

# =========================
# Simulazione
# =========================
backend = AerSimulator()
qc_sim = transpile(qc, backend)
result = backend.run(qc_sim).result()
counts = result.get_counts()

print("Conteggi misurati:", counts)

# =========================
# Istogramma dei risultati
# =========================
plot_histogram(counts)
plt.savefig("counts.png")
plt.close()
