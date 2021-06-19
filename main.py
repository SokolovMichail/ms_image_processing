import tkinter as tk
import tkinter.ttk as ttk
from interface import handle_input_folder_selection, handle_output_folder_selection, run_execution_process, \
    handle_icc_profile_selection

OPTIONS = [
"aRGB",
"Grayscale",
] #etc

widgets = {
}

window = tk.Tk()

var = tk.BooleanVar()
state = {
    'in_folder': None,
    'out_folder':None,
    'conversion':'aRGB',
    'new_size': None,
    'quality' : 100,
    'icc_profile': None
}

window.title("Converter v 0.2")
window.geometry("500x500")

label_icc = tk.Label(text = "Current .icc profile: None")
label_icc.pack()

button_icc = tk.Button(command = lambda:handle_icc_profile_selection(state,label_icc),
    text="Select .icc profile",
    width=35,
    height=3
)
button_icc.pack()
widgets['icc_loc_button'] = button_icc

label_cif = tk.Label(text = "Current input folder: None")
label_cif.pack()

button_input = tk.Button(command = lambda:handle_input_folder_selection(state,label_cif),
    text="Select folder with files to be converted",
    width=35,
    height=3
)
button_input.pack()
widgets['input_folder_button'] = button_input


label_cof = tk.Label(text = "Current input folder: None")
label_cof.pack()

button_output = tk.Button(command = lambda:handle_output_folder_selection(state,label_cof),
    text="Select folder where to store converted files",
    width=35,
    height=3
)
button_output.pack()
widgets['output_folder_button'] = button_output

label_width = tk.Label(text = "Input width(integer value) below")
label_width.pack()

entry_width = tk.Entry()
entry_width.pack()
widgets['entry_width'] = entry_width

label_height= tk.Label(text = "Input height(integer value) below")
label_height.pack()

entry_height = tk.Entry()
entry_height.pack()
widgets['entry_height'] = entry_height

label_compression= tk.Label(text = "Input quality value(0 is lowest, 100 is highest) below")
label_compression.pack()

entry_comp = tk.Entry()
entry_comp.pack()
widgets['entry_comp'] = entry_comp

label_conv= tk.Label(text = "Select conversion")
label_conv.pack()

listbox_conversion = tk.Listbox (selectmode = 'SINGLE', height = 2)
i = 0
for opt in OPTIONS:
    listbox_conversion.insert(i,opt)
    i+=1
listbox_conversion.pack()
listbox_conversion.select_set(0)
widgets['listbox_conversion'] = listbox_conversion

checkbox_aspectratio = tk.Checkbutton(text="Keep aspect ratio?",variable = var,
                                      onvalue=True, offvalue=False)
checkbox_aspectratio.pack()
widgets['keep_aspect_ratio'] = var

#progressbar = ttk.Progressbar()
#progressbar['length'] = 100
#progressbar.pack()
#widgets['progressbar'] = progressbar

button_start = tk.Button(command = lambda:run_execution_process(state,widgets),
    text="Start conversion",
    width=35,
    height=3
)
button_start.pack()
widgets['start_button'] = button_start
if __name__ == '__main__':
    window.mainloop()