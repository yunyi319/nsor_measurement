from tkinter import *
from tkinter import filedialog
from ao_config import ao_config
from ai_config import ai_config
from nidaqmx.task import Task
'''
A gui for NSOR measurement and data processing
'''

def open_path():
    file_path = filedialog.askdirectory(parent = window,
        initialdir = r'C:\Users\Hilty\Desktop\python\nsor_measurement',
        title = 'Choose file path to save the file')
    l = len(file_path_entry.get())
    file_path_entry.delete(0,l)
    file_path_entry.insert(0,file_path)

def open_pulse_sequence():
    pulse_name = filedialog.askopenfilename(parent = window,
        initialdir = r'C:\Users\Hilty\Desktop\python\nsor_measurement\pulse_sequences',
        filetypes =(("Text File", "*.txt"),("All Files","*.*")),
        title = "Choose a file.")
    l = len(pulse_entry.get())
    pulse_entry.delete(0,l)
    pulse_entry.insert(0,pulse_name)

def start_acquistion():
    samp_rate = int(samp_rate_entry.get())
    iteration = int(iteration_entry.get())
    average = int(avg_entry.get())
    pulse_chan = pulse_channel_entry.get()
    nmr_chan = nmr_channel_entry.get()
    nsor_chan = nsor_channel_entry.get()
    laser_intensity_chan = laser_intensity_channel_entry.get()
    pulse_file_path = pulse_entry.get()
    file_path = file_path_entry.get()
    for current_iter in range(iteration):
        # note: displayed iteration starts with index of 1 while the iteration used in program starts with index of 0
        '''
        need to think of a way of arrange stored files
        two strategies: for single shot experiment, use instream of the nidaqmx
                    for averaged experiments, maybe use pandas?
        '''

        current_iter_label.config(text = f'Current Iteration: {current_iter+1}')
        (ao_task,spc) = ao_config(pulse_chan, samp_rate, pulse_file_path, iteration)
        ai_task = ai_config((nmr_chan, nsor_chan, laser_intensity_chan), samp_rate, spc, file_path, iteration)
        for current_avg in range(average):
            current_avg_label.config(text = f'Current Average: {current_avg+1}')
            ao_task.start()
            ai_task.start()
            ao_task.wait_until_done()
            ai_task.wait_until_done()
            ao_task.stop()
            ai_task.stop()
        ao_task.close()
        ai_task.close()


window = Tk()  #create a window
window.geometry('1440x960') #specify the size of the window


'''
create menus
'''
menu_bar = Menu(window) #create a menu
file_menu = Menu(menu_bar) # create a sub-menu
file_menu.add_command(label = 'File Path', command = open_path) # add items to the sub menu
menu_bar.add_cascade(label = 'File', menu = file_menu) #add submenu to the menu
window.config(menu = menu_bar) # display the menu

'''
create frames to  group things
'''
file_frame = Frame(window, height = 30, width = 200, bd = 1, bg ='#99ffcc')
pulse_frame = Frame(window, height = 30, width = 200, bd = 1, bg ='#ccccff')
parameter_frame  = Frame(window, height = 200, width = 200, bd = 1)
status_frame = Frame(window, height = 200, width = 200, bd = 1, bg ='red')

'''
file path and file name
'''
file_path_entry = Entry(file_frame, font = ('Helvetica', 16))
file_path_entry.insert(0,'C:\\')
file_name_entry = Entry(file_frame, font = ('Helvetica', 16))
file_path_label = Label(file_frame,text = 'File Path:', font = ('Helvetica', 16))
file_name_label = Label(file_frame,text = 'File Name:', font = ('Helvetica', 16))

'''
pulse file selection
'''
pulse_label = Label(pulse_frame,text = 'Pulse:', font = ('Helvetica', 16))
pulse_entry = Entry(pulse_frame, font = ('Helvetica', 16))
pulse_button = Button(pulse_frame, text = 'Choose Pulse', font = ('Helvetica', 16), command = open_pulse_sequence)


'''
parameter set up for ao and ai
'''
samp_rate_label = Label(parameter_frame,text = 'Sampling rate (MS/s):', font = ('Helvetica', 16))
samp_rate_entry = Entry(parameter_frame, font = ('Helvetica', 16), width = 3)
samp_rate_entry.insert(0,'1')

iteration_label = Label(parameter_frame,text = 'Iteration:', font = ('Helvetica', 16))
iteration_entry = Entry(parameter_frame, font = ('Helvetica', 16), width = 3)
iteration_entry.insert(0,'1')

avg_label = Label(parameter_frame,text = 'Average:', font = ('Helvetica', 16))
avg_entry = Entry(parameter_frame, font = ('Helvetica', 16), width = 3)
avg_entry.insert(0,'1')

pulse_channel_label = Label(parameter_frame,text = 'Pulse Channel:', font = ('Helvetica', 16))
pulse_channel_entry = Entry(parameter_frame, font = ('Helvetica', 16), width = 8)
pulse_channel_entry.insert(0,'Dev1/ao1')

nmr_channel_label = Label(parameter_frame,text = 'NMR Channel:', font = ('Helvetica', 16))
nmr_channel_entry = Entry(parameter_frame, font = ('Helvetica', 16), width = 8)
nmr_channel_entry.insert(0,'Dev1/ai1')

nsor_channel_label = Label(parameter_frame,text = 'NSOR Channel:', font = ('Helvetica', 16))
nsor_channel_entry = Entry(parameter_frame, font = ('Helvetica', 16), width = 8)
nsor_channel_entry.insert(0,'Dev1/ai4')

laser_intensity_channel_label = Label(parameter_frame,text = 'Laser Intensity Channel:', font = ('Helvetica', 16))
laser_intensity_channel_entry = Entry(parameter_frame, font = ('Helvetica', 16), width = 8)
laser_intensity_channel_entry.insert(0,'Dev1/ai7')

'''
current_status
'''
current_iter_label = Label(status_frame, text = 'Current Iteration: 1', font = ('Helvetica', 16))

current_avg_label = Label(status_frame, text = 'Current Average: 1', font = ('Helvetica', 16))


'''
run the program
'''
run_button = Button(window, text = 'Start',font = ('Helvetica', 16), command = start_acquistion,width = 10, height = 2)


'''
arrangement of the widgets
'''
file_frame.grid(row = 0,column = 0,columnspan = 3)
file_path_entry.grid(row = 0, column = 1, ipadx = 160, sticky = W, columnspan = 2)
file_path_label.grid(row = 0, column = 0, sticky = W)
file_name_entry.grid(row = 1, column = 1, sticky = W)
file_name_label.grid(row = 1, column = 0, sticky = W)

pulse_frame.grid(row = 0,column = 3,columnspan  = 3, sticky = W)
pulse_label.grid(row = 0, column = 0, sticky = W)
pulse_entry.grid(row = 0, column = 1, ipadx = 160, sticky = W, columnspan = 2)
pulse_button.grid(row = 1, column = 0)

parameter_frame.grid(row = 1,column = 0,rowspan  = 7, columnspan = 2, sticky = W)
samp_rate_label.grid(row = 0, column = 0, sticky = W)
samp_rate_entry.grid(row = 0, column = 1, padx = 10, sticky = W)
iteration_label.grid(row = 1, column = 0, sticky = W)
iteration_entry.grid(row = 1, column = 1, padx = 10, sticky = W)
avg_label.grid(row = 2, column = 0, sticky = W)
avg_entry.grid(row = 2, column = 1, padx = 10, sticky = W)
pulse_channel_label.grid(row = 3, column = 0, sticky = W)
pulse_channel_entry.grid(row = 3, column = 1, padx = 10, sticky = W)
nmr_channel_label.grid(row = 4, column = 0, sticky = W)
nmr_channel_entry.grid(row = 4, column = 1, padx = 10, sticky = W)
nsor_channel_label.grid(row = 5, column = 0, sticky = W)
nsor_channel_entry.grid(row = 5, column = 1, padx = 10, sticky = W)
laser_intensity_channel_label.grid(row = 6, column = 0, sticky = W)
laser_intensity_channel_entry.grid(row = 6, column = 1, padx = 10, sticky = W)

status_frame.grid(row = 1,column = 3, rowspan  = 2, columnspan = 2, sticky = W)
current_iter_label.grid(row = 0, column = 0, sticky = W)
current_avg_label.grid(row = 1, column = 0, sticky = W)


run_button.grid(row = 9,column = 0, sticky = W)

'''
mainloop
'''
window.mainloop()
