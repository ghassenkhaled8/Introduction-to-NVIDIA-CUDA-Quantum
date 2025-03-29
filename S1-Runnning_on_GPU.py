import cudaq
import sys
import timeit

@cudaq.kernel
def kernel(qubit_count: int):
    q = cudaq.qvector(qubit_count)
    h(q)

# Will time the execution of our sample call.
code_to_time = 'cudaq.sample(kernel, qubit_count, shots_count=1000000)'
qubit_count = int(sys.argv[1]) if 1 < len(sys.argv) else 25
#qubit_count = 25

# Execute on CPU backend.
cudaq.set_target('qpp-cpu')
print('CPU time')  # Example: 27.57462 s.
print(timeit.timeit(stmt=code_to_time, globals=globals(), number=1))

if cudaq.num_available_gpus() > 0:
    # Execute on GPU backend.
    cudaq.set_target('nvidia')
    print('GPU time')  # Example: 0.773286 s.
    print(timeit.timeit(stmt=code_to_time, globals=globals(), number=1))

