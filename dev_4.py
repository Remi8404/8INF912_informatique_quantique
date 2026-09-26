from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
from qiskit import transpile
from qiskit_aer.noise import NoiseModel, depolarizing_error
from matplotlib import pyplot as plt


#maj 
qc_maj = QuantumCircuit(3)
qc_maj.cx(2,1)
qc_maj.cx(2,0)
qc_maj.ccx(0,1,2)


#uma
qc_uma = QuantumCircuit(3)
qc_uma.ccx(0,1,2)
qc_uma.cx(2,0)
qc_uma.cx(0,1)

print(qc_maj.draw(output='text'))
print(qc_uma.draw(output='text'))

porte_maj = qc_maj.to_gate()
porte_uma = qc_uma.to_gate()

#----------------------------------------------------------------------------
c0 = QuantumRegister(1, 'c0')
a = QuantumRegister(4, 'a')
b = QuantumRegister(4, 'b')
cout = QuantumRegister(1, 'cout')
c_reg = ClassicalRegister(5, 'mesure')

qc = QuantumCircuit(c0, a, b, cout, c_reg)



#qc.x(a[0])
#qc.x(a[2])

#qc.x(b[0])
#qc.x(b[1])
#qc.x(b[3])

qc.barrier()

#----------------------------------------------------------------------------
qc.append(porte_maj, [c0[0], b[0], a[0]])
qc.append(porte_maj, [a[0], b[1], a[1]])
qc.append(porte_maj, [a[1], b[2], a[2]])
qc.append(porte_maj, [a[2], b[3], a[3]])

qc.cx(a[3], cout[0])

qc.append(porte_uma, [a[2], b[3], a[3]])
qc.append(porte_uma, [a[1], b[2], a[2]])
qc.append(porte_uma, [a[0], b[1], a[1]])
qc.append(porte_uma, [c0[0], b[0], a[0]])

qc.barrier()

#----------------------------------------------------------------------------

print(qc.draw(output='text'))

qc.measure(b, c_reg[0:4]) #résultat de la somme
qc.measure(cout, c_reg[4])


#----------------------------------------------------------------------------
modele_bruit = NoiseModel()

erreur_1q = depolarizing_error(0.02, 1)  # Pour x, h
erreur_2q = depolarizing_error(0.05, 2)  # Pour cx
erreur_3q = depolarizing_error(0.10, 3)

modele_bruit.add_all_qubit_quantum_error(erreur_1q, ['x', 'h'])
modele_bruit.add_all_qubit_quantum_error(erreur_2q, ['cx'])
modele_bruit.add_all_qubit_quantum_error(erreur_3q, ['ccx'])

aer = AerSimulator()
compile = transpile(qc, aer, basis_gates=modele_bruit.basis_gates)
job = aer.run(compile, shots=1000, noise_model=modele_bruit)
result = job.result()
counts = result.get_counts(compile)

print(counts)

#----------------------------------------------------------------------------
plot_histogram(counts)
plt.show()