from nidaqmx.task import Task
from nidaqmx import constants
import numpy as np
from numpy import pi
import matplotlib.pylab as plt

samp_rate = 1000000
duration = 1
sample_num = 1000000
time = np.linspace(0,duration,sample_num)
freq = 1000

test_task = Task('ao_test')
test_task.ao_channels.add_ao_voltage_chan('/Dev1/ao1')
test_task.timing.cfg_samp_clk_timing(rate =samp_rate,
                #source = '/Dev1/ai/SampleClock', \
                samps_per_chan = sample_num, 
                sample_mode=constants.AcquisitionType.CONTINUOUS)
pulse_data = np.sin(2*pi*freq*time)
test_task.write(pulse_data)
test_task.start()

#test_task.wait_until_done()
test_task.stop()
test_task.close()
