import cudaq
import numpy as np
from cudaq import spin

qubit_count = 2

# Define a quantum kernel function.

@cudaq.kernel
def kernel(qubit_count: int):
    qvector = cudaq.qvector(qubit_count)

    # 2-qubit GHZ state.
    h(qvector[0])
    for i in range(1, qubit_count):
        x.ctrl(qvector[0], qvector[i])

# Set the simulation target to a multi-QPU platform
cudaq.set_target("nvidia", option = 'mqpu')

# Measuring the expectation value of 2 different hamiltonians in parallel
hamiltonian_0 = spin.x(0) + spin.y(1) + spin.z(0)*spin.y(1)
hamiltonian_1 = spin.z(1) + spin.y(0) + spin.x(1)*spin.x(0)
hamiltonian_2 = spin.x(1) + spin.z(0) + spin.y(1)*spin.y(0)
hamiltonian_3 = spin.y(1) + spin.x(0) + spin.z(1)*spin.y(0)

# Asynchronous execution on multiple qpus via nvidia gpus.
result_0 = cudaq.observe_async(kernel, hamiltonian_0, qubit_count, qpu_id=0)
result_1 = cudaq.observe_async(kernel, hamiltonian_1, qubit_count, qpu_id=1)
result_2 = cudaq.observe_async(kernel, hamiltonian_2, qubit_count, qpu_id=2)
result_3 = cudaq.observe_async(kernel, hamiltonian_3, qubit_count, qpu_id=3)

# Retrieve results
print(result_0.get().expectation())
print(result_1.get().expectation())
print(result_2.get().expectation())
print(result_3.get().expectation())
