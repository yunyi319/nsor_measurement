'''
configure ao_task
'''

from nidaqmx.task import Task
from nidaqmx import constants
import numpy as np
from numpy import pi
from nmr_pulses import pulse_interpreter

def ao_config(channel, samp_rate, pulse_file_path, iteration):
    pulse_data = pulse_interpreter(pulse_file_path, samp_rate, iteration)
    spc = len(pulse_data)
    pulse_task = Task('pulse_task')
    pulse_task.ao_channels.add_ao_voltage_chan(channel)

    pulse_task.timing.cfg_samp_clk_timing(rate =samp_rate,
                    #channel = '/Dev1/ai/SampleClock',
                    samps_per_chan = spc,
                    sample_mode=constants.AcquisitionType.FINITE)
    pulse_task.write(pulse_data)
    return (pulse_task,spc)
