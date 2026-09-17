import numpy as np
from math import sqrt
from qiskit.quantum_info import Statevector, Operator

HSH = np.array([[(1+1j)/2, (1-1j)/2],[(1-1j)/2, (1+1j)/2]])

H = Operator.from_label("H")

ZERO = Statevector.from_label("0")
ONE = Statevector.from_label("1")

PLUS = np.array([[1/sqrt(2)],[1/sqrt(2)]])
MINUS = np.array([[1/sqrt(2)],[-1/sqrt(2)]])

X = Operator.from_label("X")
Y = Operator.from_label("Y")
Z = Operator.from_label("Z")

