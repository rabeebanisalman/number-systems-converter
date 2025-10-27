from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from NumSys import Number


# constants

PLACEHOLDER = "Enter number here..."
SUPPORTED_BASES = ['2', '8', '10', '16']
LIGHT_BG = 'white'
LIGHT_FG = 'black'
DARK_BG = 'black'
DARK_FG = 'white'

dark_mode = False

# insert and delete placeholder from entry box

def entry_focus_in(event):
    if entry_box.get() == PLACEHOLDER:
        entry_box.delete(0, END)

def entry_focus_out(event):
    if not entry_box.get():
        entry_box.insert(0, PLACEHOLDER)

# mode switch

def toggle_dark_mode():

    global dark_mode

    labels = [binary_label,
        octal_label,
        decimal_label,
        hex_label,
        binary_value,
        octal_value,
        decimal_value,
        hex_value]

    
    if dark_mode:

        for l in labels:
            l.config(bg=LIGHT_BG,fg=LIGHT_FG)

        mode_switch_button.config(image=switch_off_icon,bg=LIGHT_BG, activebackground=LIGHT_BG)
        window.config(bg=LIGHT_BG)
        cat_logo.config(image=light_cat_icon)
        entry_frame.config(bg=LIGHT_BG)
        output_frame.config(bg=LIGHT_BG)

        dark_mode = False

    else:

        for l in labels:
            l.config(bg=DARK_BG,fg=DARK_FG)

        mode_switch_button.config(image=switch_on_icon,bg=DARK_BG, activebackground=DARK_BG)
        window.config(bg=DARK_BG)
        mode_switch_button.config(image=switch_on_icon,bg=DARK_BG, activebackground=DARK_BG)
        cat_logo.config(image=dark_cat_icon)
        entry_frame.config(bg=DARK_BG)
        output_frame.config(bg=DARK_BG)

        dark_mode = True

# output config

def convert_number():

    try:
        user_input = entry_box.get()

        if user_input == '' or user_input == PLACEHOLDER:
            raise ValueError("Please enter a number.")
        
        selected_base = base.get()

        if not selected_base or selected_base == 'Base':
            raise ValueError("Please select a base.")
        
        selected_base = int(selected_base)

        num = Number(user_input, selected_base)
        
        binary_value.config(text=num.to_bin())
        octal_value.config(text=num.to_oct())
        decimal_value.config(text=num.to_dec())
        hex_value.config(text=num.to_hex())
        
    except ValueError as error:
        messagebox.showerror("Error", str(error))

# window

window = Tk()

window.geometry("500x600")

window.title("Black Cat")

window.config(bg=LIGHT_BG)

window.iconphoto(True, PhotoImage(file='paw.png'))

# load and resize images for Tk using PIL

def load_and_resize_image(filename, size):
    img = Image.open(filename)
    img = img.resize(size)
    return ImageTk.PhotoImage(img)

switch_off_icon = load_and_resize_image('toggle_switch_off.png', (35, 35))
switch_on_icon = load_and_resize_image('toggle_switch_on.png', (35, 35))
light_cat_icon = load_and_resize_image('white_cat.png', (300, 250))
dark_cat_icon = load_and_resize_image('black_cat.png', (300, 250))

# mode switch button

mode_switch_button = Button(window, 
                            image=switch_off_icon, 
                            command=toggle_dark_mode,
                            bg=LIGHT_BG,
                            activebackground=LIGHT_BG,
                            borderwidth=0, 
                            relief='flat', 
                            highlightthickness=0)
mode_switch_button.pack(anchor='e')

# cat logo

cat_logo = Label(window, 
                 image=light_cat_icon, 
                 bg=LIGHT_BG,
                 borderwidth=0, 
                 highlightthickness=0)
cat_logo.pack()

# user input

entry_frame = Frame(window, 
                    bg=LIGHT_BG)
entry_frame.pack()

entry_box = Entry(entry_frame,
                highlightthickness=1,
                font=('',11),
                width=30)

entry_box.insert(0, PLACEHOLDER)
entry_box.bind('<FocusIn>', entry_focus_in)
entry_box.bind('<FocusOut>', entry_focus_out)
entry_box.pack(side='left')

base = StringVar(value='Base')
base_dropdown = OptionMenu(entry_frame, 
                           base, 
                           *SUPPORTED_BASES)

base_dropdown.config(
                    highlightthickness=1,
                    width=4,
                    font=('', 9),
                    pady=2)
base_dropdown.pack(side='left', padx=3)

go_button = Button(entry_frame,
                    highlightthickness=1,
                    text="Go",
                    font=('', 9), 
                    anchor='w',
                    pady=2,
                    command=convert_number)

go_button.pack(side='left', padx=1)

# output

output_frame = Frame(window, bg=LIGHT_BG)
output_frame.pack(anchor='s',pady=10)

binary_label = Label(output_frame, text="Binary:", bg=LIGHT_BG, fg=LIGHT_FG, font=('',10,'bold'))
binary_label.grid(row=0, column=0, sticky='w')

octal_label = Label(output_frame, text="Octal:", bg=LIGHT_BG, fg=LIGHT_FG, font=('',10,'bold'))
octal_label.grid(row=1, column=0, sticky='w')

decimal_label = Label(output_frame, text="Decimal:", bg=LIGHT_BG, fg=LIGHT_FG, font=('',10,'bold'))
decimal_label.grid(row=2, column=0, sticky='w')

hex_label = Label(output_frame, text="Hexadecimal:", bg=LIGHT_BG, fg=LIGHT_FG, font=('',10,'bold'))
hex_label.grid(row=3, column=0, sticky='w')

binary_value = Label(output_frame, bg=LIGHT_BG,  fg=LIGHT_FG,font=('',10))
binary_value.grid(row=0, column=1, sticky='w')

octal_value = Label(output_frame, bg=LIGHT_BG, fg=LIGHT_FG, font=('',10))
octal_value.grid(row=1, column=1, sticky='w')

decimal_value = Label(output_frame, bg=LIGHT_BG, fg=LIGHT_FG, font=('',10))
decimal_value.grid(row=2, column=1, sticky='w')

hex_value = Label(output_frame, bg=LIGHT_BG, fg=LIGHT_FG, font=('',10))
hex_value.grid(row=3, column=1, sticky='w')

window.mainloop()