#Test to export arrays to txt-files

import numpy as np

array = np.arange(10)
np.save("array", array)

loaded = np.load("array.npy")
print(loaded)