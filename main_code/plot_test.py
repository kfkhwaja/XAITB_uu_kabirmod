import ast
import numpy as np
import matplotlib.pyplot as plt

def read_array_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    arrays = [np.array(ast.literal_eval(line)) for line in lines]
    return arrays

# Read Umean
UUmean, VVmean, WWmean = read_array_file('/scratch/rvinuesa_root/rvinuesa/khwaja/test_data_kabir/strat/data/Umean.txt')
y = np.arange(len(UUmean))

plt.figure()
plt.plot(UUmean, y, label='UUmean')
plt.plot(VVmean, y, label='VVmean')
plt.plot(WWmean, y, label='WWmean')
plt.xlabel('Mean velocity')
plt.ylabel('Wall-normal index')
plt.legend()
plt.show()

# Read Urms
uurms, vvrms, wwrms, uv, vw, uw = read_array_file('/scratch/rvinuesa_root/rvinuesa/khwaja/test_data_kabir/strat/data/Urms.txt')

plt.figure()
plt.plot(uurms, y, label='u rms')
plt.plot(vvrms, y, label='v rms')
plt.plot(wwrms, y, label='w rms')
plt.xlabel('RMS velocity')
plt.ylabel('Wall-normal index')
plt.legend()
plt.show()

plt.figure()
plt.plot(uv, y, label='uv stress')
plt.plot(vw, y, label='vw stress')
plt.plot(uw, y, label='uw stress')
plt.xlabel('Reynolds stress')
plt.ylabel('Wall-normal index')
plt.legend()
plt.show()
