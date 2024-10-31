from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(127, 'q')
creg_c0 = ClassicalRegister(1, 'c0')
circuit = QuantumCircuit(qreg_q, creg_c0)

circuit.rz(pi / 2, qreg_q[0])
circuit.sx(qreg_q[0])
circuit.rz(pi / 2, qreg_q[0])
circuit.measure(qreg_q[0], creg_c0[0])