import tkinter as tk
from tkinter import ttk
from PIL import Image
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

root = tk.Tk()
root.title("Sales Prediction")
root.option_add("*tearOff", False) # This is always a good idea

# Make the app responsive
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)

# Create a style
style = ttk.Style(root)

# Import the tcl file
root.tk.call("source", "forest-dark.tcl")

# Set the theme with the theme_use method
style.theme_use("forest-dark")

# Create lists for the Comboboxes
option_menu_list = ["", "choose model", "RFC", "Logistic"]
combo_list = ["distributor 1","distirubitor 2","distributor 3","distributor 4","distirubitor 5","distributor 6"]
readonly_combo_list = ["Addis Ababa", "Oromia","Amhara","SPPR","Tigray","Dire Dawa"]

# Create control variables
check_box1 = tk.BooleanVar()
check_box2 = tk.BooleanVar()
check_box3 = tk.BooleanVar()
check_box4 = tk.BooleanVar()
radio_box1 = tk.BooleanVar()
radio_box2 = tk.BooleanVar()
radio_box3 = tk.BooleanVar()
radio_box4 = tk.BooleanVar()
sales = tk.IntVar(value=0)
me = tk.IntVar(value=0)
me.set("Enter Mechanical Efficiency")
combo1 = tk.StringVar()
combo2 = tk.StringVar()
price = tk.IntVar()
e = tk.StringVar(value=option_menu_list[1])
f = tk.BooleanVar()
g = tk.DoubleVar(value=75.0)
h = tk.BooleanVar()
i = tk.IntVar(value=3)
month = tk.BooleanVar()

# Create a Frame for the Checkbuttons
check_frame = ttk.LabelFrame(root, text="Season", padding=(20, 10))
check_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

# Checkbuttons
check_1 = ttk.Checkbutton(check_frame, text="Fanta", variable=check_box1)
check_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
check_2 = ttk.Checkbutton(check_frame, text="Coca Cola", variable=check_box2)
check_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
check_3 = ttk.Checkbutton(check_frame, text="Sprite", variable=check_box3)
check_3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
check_4 = ttk.Checkbutton(check_frame, text="Schwepps",variable=check_box4)
check_4.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")
def handle_checkboxs():
    if check_box1:
        return "Fanta"
    elif check_box2:
        return "Coca Cola"
    elif check_box3:
        return "Sprite"
    else:
        return "Schwepps"
# Separator
separator = ttk.Separator(root)
separator.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="ew")

# Create a Frame for the Radiobuttons
radio_frame = ttk.LabelFrame(root, text="Size", padding=(20, 10))
radio_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")

radio_1 = ttk.Radiobutton(radio_frame, text="500 ml", variable=radio_box1)
radio_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
radio_2 = ttk.Radiobutton(radio_frame, text="330 ml", variable=radio_box2)
radio_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
radio_3 = ttk.Radiobutton(radio_frame, text="1.5 liter",variable=radio_box3)
radio_3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
def handle_radiobox():
    if radio_box1:
        return "500 ml"
    elif radio_box2:
        return "330 ml"
    else:
        return "1.5 liter"
# Create a Frame for input widgets
widgets_frame = ttk.Frame(root, padding=(0, 0, 0, 10))
widgets_frame.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3)
widgets_frame.columnconfigure(index=0, weight=1)

# Entry
entry = ttk.Entry(widgets_frame,textvariable=sales)
entry.insert(0, "Enter sales target",)
entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")

# Spinbox
spinbox = ttk.Spinbox(widgets_frame, from_=0, to=100,textvariable=me)
spinbox.insert(0,'0')
spinbox.grid(row=1, column=0, padx=5, pady=10, sticky="ew")
def handle_input(variable):
    return variable.get()
# Combobox
combobox = ttk.Combobox(widgets_frame, values=combo_list)
combobox.current(0)
combobox.grid(row=2, column=0, padx=5, pady=10,  sticky="ew")

# Read-only combobox
readonly_combo = ttk.Combobox(widgets_frame, state="Enter Area", values=readonly_combo_list)
readonly_combo.current(0)
readonly_combo.grid(row=3, column=0, padx=5, pady=10,  sticky="ew")
def handle_combo(combo,combo_list):
    return combo_list[combo.current()]

entry1 = ttk.Entry(widgets_frame,textvariable=price)
entry1.insert(0, "Enter Price per bottle-",)
entry1.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")



# Accentbutton
accentbutton = ttk.Button(widgets_frame, text="Generate Prediction", style="Accent.TButton")
accentbutton.grid(row=10, column=0, padx=5, pady=10, sticky="nsew")



# Panedwindow


# Pane #1

fra = ttk.LabelFrame(root, text="Month", padding=(20, 10))
fra.grid(row=0, column=2, padx=(20, 10), pady=(20, 10), sticky="nsew")
# Create a Frame for the Treeview

checkbox = ttk.Checkbutton(fra, text="1st quarter")
checkbox.grid(row=0, column=2, padx=5, pady=10, sticky="nsew")
checkbox1 = ttk.Checkbutton(fra, text="2nd quarter")
checkbox1.grid(row=1, column=2, padx=5, pady=10, sticky="nsew")
checkbox2 = ttk.Checkbutton(fra, text="3rd quarter")
checkbox2.grid(row=2, column=2, padx=5, pady=10, sticky="nsew")
checkbox3 = ttk.Checkbutton(fra, text="4th quarter")
checkbox3.grid(row=3, column=2, padx=5, pady=10, sticky="nsew")
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May','jun']
estimated_sales = [5000, 6000, 5500, 7000, 6500, 8000]
target_sales = [5500, 6500, 6000, 7500, 7000, 8500]
bar_width = 0.35

# X-axis positions for the bars
x = np.arange(len(months))
fig = plt.figure()
ax = fig.add_subplot()
fig.set_facecolor('#F0F0F0')
ax.set_facecolor('#F0F0F0')
ax.bar(x - bar_width/2, estimated_sales, width=bar_width, color='#1f77b4', label='Estimated Sales')
ax.bar(x + bar_width/2, target_sales, width=bar_width, color='#ff7f0e', label='Target Sales')
ax.set_title('Estimated Sales vs. Target Sales', fontsize=18, fontweight='bold')
ax.set_xlabel('Months', fontsize=14)
ax.set_ylabel('Sales', fontsize=14)
ax.grid(color='lightgray', linestyle='--', linewidth=0.5)
ax.legend(fontsize=12)
plt.xticks(x, months, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
canvas = FigureCanvasTkAgg(fig,master=root)
canvas.draw()
canvas.get_tk_widget().grid(row=0, column=50, padx=60, pady=10, sticky="sw",rowspan=21)
# Treeview

# P

# Lab

# Sizegrip
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))

# Center the window, and set minsize
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

# Start the main loop
root.mainloop()
