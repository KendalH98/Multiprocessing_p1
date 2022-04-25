import numpy as np
Array1 = np.array([23, 5, 1, 456, 3, 90])
from multiprocessing import shared_memory
shm = shared_memory.SharedMemory(create=True, size=Array1.nbytes)
# Now create a NumPy array backed by shared memory
Array2 = np.ndarray(Array1.shape, dtype=Array1.dtype, buffer=shm.buf)
Array2[:] = Array1[:]  # Copy the original data into shared memory
print(Array1)
print(Array1.shape)
print(Array2)
print(type(Array1))

import numpy as np
from multiprocessing import shared_memory

existing_shm = shared_memory.SharedMemory(name=shm.name)

Array3 = np.ndarray(Array2.shape, dtype=Array2.dtype, buffer=existing_shm.buf)
Array3[-1] = 888

print(Array3)
print(Array2)

shm.close()
shm.unlink()  # Release the shared memory block
# References: <author(s) https://docs.python.org/3/library/multiprocessing.shared_memory.html (2022) multiprocessing.shared_memory Version 3.8
