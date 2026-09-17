from qiskit.quantum_info import Statevector

from consts import H, PLUS, MINUS, X, Y, Z

def main():
    print(f"Q1.a)\n{H ^ X}")
    print(f"Q1.b)\n{X ^ Y ^ Z}")
    print(f"Q1.c)\n{Statevector(PLUS) ^ Statevector(MINUS)}")
    
if __name__ == "__main__":
    main()