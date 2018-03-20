import numpy as np
from numpy import pi
import sys
sys.path.insert(0, r'C:\Users\Hilty\Desktop\python\nsor_measurement')
import matplotlib.pyplot as plt
from nmr_pulses import pulse_interpreter

if __name__ == '__main__':
    file_path = r'C:\Users\Hilty\Desktop\python\nsor_measurement\pulse_sequences\cpmg_sequence.txt'
    pulse = pulse_interpreter(file_path, samp_freq = 1000000 ,iteration=0)
    tm = np.linspace(0,len(pulse)/(1000000),len(pulse))
    print(len(tm))
    plt.plot(tm,pulse)
    plt.show()
