from qiskit.quantum_info import Statevector

from consts import H, PLUS, MINUS, X, Y, Z

def main():
    print(f"Q1.a)\n{H ^ X}") # same as H.tensor(X)
    print(f"Q1.b)\n{X ^ Y ^ Z}")
    print(f"Q1.c)\n{Statevector(PLUS) ^ Statevector(MINUS)}")
    print(f"Q5)\n{Statevector(MINUS) ^ Statevector(MINUS)}")
    
if __name__ == "__main__":
    main()