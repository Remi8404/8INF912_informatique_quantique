from qiskit.visualization import plot_bloch_vector, plot_bloch_multivector
from qiskit.quantum_info import Statevector
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

from consts import HSH, PLUS


def main()->None:

    # Matricial multiplication
    hshp = HSH @ PLUS

    #plot vector bloch
    plot_bloch_vector((0, 1/sqrt(2), 1/sqrt(2)), title="sphere", coord_type= 'cartesian')

    # plot_bloch_multivector
    plot_bloch_multivector(Statevector(hshp))

    # show graphic
    plt.show()



if __name__ == "__main__":
    main()
