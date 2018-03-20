from nidaqmx.task import Task
from nidaqmx import constants
import numpy as np
import matplotlib.pylab as plt

samp_rate = 1000000
sample_num = 1000000
duration = 1
time = np.linspace(0,duration,sample_num)

test_task = Task('ai_test')
test_task.ai_channels.add_ai_voltage_chan(physical_channel = '/Dev1/ai1',
                terminal_config = constants.TerminalConfiguration.DIFFERENTIAL)
test_task.timing.cfg_samp_clk_timing(rate =samp_rate,
                 #source = '/Dev1/ai/SampleClock', \
                 samps_per_chan = sample_num, 
                 sample_mode=constants.AcquisitionType.FINITE)
test_task.start()
ai_data = test_task.read(number_of_samples_per_channel  = sample_num)
plt.plot(time,ai_data)
test_task.wait_until_done()
test_task.stop()
test_task.close()

