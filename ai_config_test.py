'''
test the ai_config file
'''

import sys
sys.path.insert(0, r'C:\Users\Hilty\Desktop\python\nsor_measurement')
from nidaqmx.task import Task
from ai_config import ai_config

if __name__ == '__main__':
    source = '/Dev1/ai1'
    samp_rate = 1000000
    pulse_file_path = r'C:\Users\Hilty\Desktop\python\nsor_measurement\pulse_sequences\simple_sequence.txt'
    iteration = 0
    (ao_task,spc) = ai_config(source, samp_rate, pulse_file_path, iteration)
    ao_task.start()
    ao_task.wait_until_done()
    ao_task.stop()
    ao_task.close()
