
from nidaqmx.task import Task
from nidaqmx import constants
import numpy as np
import time
samp_rate = 31200*16
sample_num = int(31200*0.01)
duration = sample_num/samp_rate
#time_axis = np.linspace(0,duration,sample_num)

test_task = Task('ai_test')


test_task.ai_channels.add_ai_voltage_chan(physical_channel = 'Dev1/ai1',
                terminal_config = constants.TerminalConfiguration.DIFFERENTIAL)

test_task.in_stream.configure_logging("C:\\Users\\Hilty\\Desktop\\python\\test\\file_test4.tdms",
                                    constants.LoggingMode.LOG)

test_task.timing.cfg_samp_clk_timing(rate =samp_rate,
                 #source = '/Dev1/ai/SampleClock', \
                 samps_per_chan = sample_num)

for n in range(3):
    test_task.start()
    test_task.wait_until_done()
    test_task.stop()

test_task.close()
