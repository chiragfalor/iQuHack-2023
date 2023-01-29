# import packages
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_ionq import IonQProvider
import matplotlib.pyplot as plt

provider = IonQProvider(token='vm05jEWtO7zVGE6laZPtx8jbLM66TaS9')
backend = provider.get_backend("ionq_simulator")
# backend = provider.get_backend("ionq_qpu")

class QuantumPersonalityState:

    NUM_QUBITS = 9

    def __init__(self, personality_traits):
        self.personality_traits = [round(x) for x in personality_traits]
        self.qc = QuantumCircuit(self.NUM_QUBITS, self.NUM_QUBITS)
        self.qc.h(range(3))
        self.apply_personality_gates()

    def apply_personality_gates(self):
        
        for i in range(len(self.personality_traits)):
            if self.personality_traits[i] == 1:
                self.qc.x(i)

        # correlate
        for i in range(len(self.personality_traits)):
            if self.personality_traits[i] == 1:
                self.qc.toffoli(0, 1, i+3)
            else:
                self.qc.cnot(2, i+3)

    def draw(self):
        print(self.qc.draw())

    def get_pfp_reprn(self):
        self.qc.measure(range(self.NUM_QUBITS), range(self.NUM_QUBITS))
        job = backend.run(self.qc, shots=1)
        result = job.result()
        counts = result.get_counts(self.qc)
        # print(result.get_probabilities())
        # get the most common result
        state = max(counts, key=counts.get)
        return list(map(int, reversed(state)))


