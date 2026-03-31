import ast
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plot_folder = '/scratch/rvinuesa_root/rvinuesa/khwaja/test_data_kabir/strat/plots/'

def read_array_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    arrays = [np.array(ast.literal_eval(line)) for line in lines]
    return arrays

# Read Umean
UUmean, VVmean, WWmean = read_array_file('/scratch/rvinuesa_root/rvinuesa/khwaja/test_data_kabir/strat/data/Umean.txt')
y = np.arange(len(UUmean))
plt.figure()
plt.plot(y, UUmean, label='UUmean')
plt.plot(y, VVmean, label='VVmean')
plt.plot(y, WWmean, label='WWmean')
plt.ylabel('Mean velocity')
plt.xlabel('Wall-normal index')
plt.legend()
plt.savefig(plot_folder + 'Umean.png', dpi=200)
plt.close()

# Read Urms
uurms, vvrms, wwrms, uv, vw, uw = read_array_file('/scratch/rvinuesa_root/rvinuesa/khwaja/test_data_kabir/strat/data/Urms.txt')
plt.figure()
plt.plot(y, uurms, label='u rms')
plt.plot(y, vvrms, label='v rms')
plt.plot(y, wwrms, label='w rms')
plt.ylabel('RMS velocity')
plt.xlabel('Wall-normal index')
plt.legend()
plt.savefig(plot_folder + 'Urms.png', dpi=200)
plt.close()

plt.figure()
plt.plot(y, uv, label='uv stress')
plt.plot(y, vw, label='vw stress')
plt.plot(y, uw, label='uw stress')
plt.ylabel('Reynolds stress')
plt.xlabel('Wall-normal index')
plt.legend()
plt.savefig(plot_folder + 'Reynolds_stress.png', dpi=200)
plt.close()
