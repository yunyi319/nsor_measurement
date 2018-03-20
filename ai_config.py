'''
configure ai_task
'''
from nidaqmx.task import Task
from nidaqmx import constants
import numpy as np
def ai_config(channels, samp_rate, spc, file_path, iteration):
    ai_task = Task('receive_signal_task')
    for channel in channels:
        ai_task.ai_channels.add_ai_voltage_chan(physical_channel = channel,
                    terminal_config = constants.TerminalConfiguration.DIFFERENTIAL)
    ai_task.timing.cfg_samp_clk_timing(rate = samp_rate,
                 #source = '/Dev1/ai/SampleClock',
                 samps_per_chan = spc,
                 sample_mode=constants.AcquisitionType.FINITE)
