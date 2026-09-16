# Tkinter — загальна шпаргалка
import tkinter as tk
from tkinter import ttk
from tkinter import font







# 1. ======  Базовий каркас програми  ======
root = tk.Tk()  #Creates main window which will conain all other components

root.title("My Application")  #Set title of the window
root.geometry("800x600")   # Set widht and height of the window
root.minsize(400, 300) #Set minimum size
# put GUI components here
# root.mainloop()      #This launch the UI window  run it last, when all components are tuned



# Основні методи Tk
# | Метод                    | Призначення                   |
# | ------------------------ | ----------------------------- |
# | `title()`                | Заголовок вікна               |
# | `geometry("800x600")`    | Розмір і позиція              |
# | `minsize(w, h)`          | Мінімальний розмір            |
# | `maxsize(w, h)`          | Максимальний розмір           |
# | `resizable(True, False)` | Дозволити зміну ширини/висоти |
# | `configure()`            | Налаштування вікна            |
# | `destroy()`              | Закрити вікно                 |
# | `after(ms, func)`        | Виконати callback через N мс  |
# | `after_cancel(id)`       | Скасувати `after()`           |
# | `mainloop()`             | Головний цикл GUI             |


# У Tkinter є два основних набори віджетів Tk та ttk

# tk.Button(...), tk.Label(...), tk.Entry(...), tk.Frame(...)

# Для сучасного GUI зазвичай краще використовувати ttk, особливо:

# ttk.Button
# ttk.Label
# ttk.Entry
# ttk.Combobox
# ttk.Checkbutton
# ttk.Radiobutton
# ttk.Treeview
# ttk.Notebook
# ttk.Progressbar
# ttk.Spinbox

# Зазвичай GUI будується ієрархією:
# root
#  ├── frame
#  │    ├── label
#  │    ├── entry
#  │    └── button
#  │
#  └── frame
#       ├── tree
#       └── scrollbar

# ======  Frame — контейнер.  ======

# Один із найважливіших віджетів.
yellow_frame = ttk.Frame(root)
yellow_frame.configure(relief = 'solid')
yellow_frame.pack()

blue_frame = ttk.Frame(root, padding=10)
blue_frame.configure(relief = 'raised')
blue_frame.pack(fill="both", expand=True)


# ======  Label  ======

label = tk.Label(yellow_frame, text="Yellow frame:", 
                  font=("arial", 24, 'bold'), 
                  fg='#12edb2', bg ='yellow',  # Color may be specified in HEX as '#12edb2'
                  relief = 'solid') 
label.pack()   #This method is mandatory to see widget in the screen

label2 = ttk.Label(blue_frame, text="Blue frame:", 
                   font=('times new roman', 20, 'italic')) #ttk doesn't support fg in constructor
label2.pack()

# Змінити текст:
label.configure(text="Yellow frame edited text")

# Отримати текст:
labeltext = label.cget("text")
# print("Yellow label text = ", labeltext)

# Розмістити компонент place(x, y) - method of ttk

label2.place(x = 10, y=50)


# =====  Fonts  ======


# Available fonts
# fonts = font.families()
# print('Available fonts: \n', fonts)

# =====  Button  ======

def save_date():
    #Do something
    pass

start_button = tk.Button(yellow_frame, 
                         text='START',  font=("arial", 24, 'bold'),
                         fg ='magenta',
                        #  command=save_data   #This calls on_click method
                         )
# Не можна передавати параметри так:
# command=save_data("test") бо функція виконається одразу.
# Потрібно:
# command=lambda: save_data("test")

# або:
# from functools import partial

# button = ttk.Button(
#     frame,
#     text="Save",
#     command=partial(save_data, "test")
# )

start_button.place(x=100, y=400)
start_button.pack()

#   =======  Entry  ======
# Поле введення тексту.

entry = ttk.Entry(blue_frame)
entry.pack()

# Отримати текст
value = entry.get()

# Встановити
entry.delete(0, tk.END)
entry.insert(0, "Hello")

# Очистити
# entry.delete(0, tk.END)

root.mainloop() #This launch the UI window


