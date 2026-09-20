# Tkinter — загальна шпаргалка
import time
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog



# 1. ======  Базовий каркас програми  ======
root = tk.Tk()  #Creates main window which will conain all other components

root.title("My Application")  #Set title of the window
root.geometry("800x600")   # Set widht and height of the window
root.minsize(50, 50) #Set minimum size
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



# ====== StringVar / IntVar / BooleanVar / DoubleVar  ======


# Це дуже важливий механізм Tkinter.  
# Прив'язує об'єкт цього типу до значення UI компонента, і змінює 
# значення об'єкта при зміні значення в UI компоненті
# Для отримання значення з об'єкту використовується метод get()

name = tk.StringVar()

# Тепер отримати значення з entry використовується :
name.get()

# а щоб встановити значення використовується:
name.set("Andrew")

# Аналогічно для цілих значень
age = tk.IntVar(value=25)

# Для логічних значень
enabled = tk.BooleanVar(value=False)

# ======  trace_add() — listener на зміну значення  =====
# Це аналог listener-а для StringVar/IntVar.

def value_changed(*args):   #*args - обов'язковий параметр callback для службової інформації
    print("Name has changed to ", name.get())

name.trace_add(
    "write",
    value_changed
)
# "write" означає: викликати колбек, коли значення змінної записується або змінюється.

# Які бувають режими відстеження  trace_add()
# Режим      Коли викликається
# "write"    Значення змінної записали або змінили
# "read"     Значення змінної прочитали
# "unset"    Змінну видалили

# Тепер коллбек викликається при зміні значення name або при зміні елементу до якого вона прив'язана


# ======  Frame — контейнер.  ======


# Один із найважливіших віджетів.
yellow_frame = ttk.Frame(root)
yellow_frame.configure(relief = 'sunken')
yellow_frame.pack()

# ttk.Frame is formatted through the Style
# See separate theme on styling
style = ttk.Style()
style.configure(
     "Blue.TFrame",
     background="#c5eafc"
)

blue_frame = ttk.Frame(root, padding=10)
blue_frame.configure(relief = 'raised', style="Blue.TFrame")
blue_frame.pack(fill="both", expand=True)


# ======  Label  ======


yellow_name = tk.StringVar()
yellow_name.set('Yelow label initial text')

label = tk.Label(yellow_frame,
                  textvariable=yellow_name,
                  font=("arial", 20, 'bold'), 
                  fg='#12edb2', bg ='yellow',  # Color may be specified in HEX as '#12edb2'
                  relief = 'solid') 
label.pack()   #This method is mandatory to see widget in the screen

label2 = ttk.Label(blue_frame, text="Blue frame label:", 
                   font=('times new roman', 18, 'italic')) #ttk doesn't support fg in constructor
label2.place(x = 10, y=10, width= 200, height=30)

# Змінити текст:
# label.configure(text="Yellow frame label edited")

# Отримати текст:
# labeltext = label.cget("text")


# =====  Fonts  ======


# Available fonts
# fonts = font.families()
# print('Available fonts: \n', fonts)


# =====  Button  ======


def save_data():
    #Do something
    t = time.localtime() 
    yellow_name.set('Button clicked at ' + str(t.tm_hour)+ ':' + str(t.tm_min) + '.' + str(t.tm_sec))
    pass

start_button = tk.Button(blue_frame, 
                         text='START',  font=("arial", 16, 'bold'),
                         fg ='violet',
                        #  command=save_data   #This calls on_click method
                        command = lambda: save_data()  #Correct way to set command
                         )
start_button.place(x=220, y=10, height=30)

# Не можна передавати параметри так:
# command=save_data("test") бо функція виконається одразу.
# Потрібно:
# command=lambda: save_data("test")

# або якщо треба передати параметри:
# from functools import partial

# button = ttk.Button(
#     frame,
#     text="Save",
#     command=partial(save_data, "test")
# )


#   =======  Entry  ======
# Поле введення тексту.


entry = ttk.Entry(blue_frame,
    width=75,
    textvariable=name  #Тут ми прив'язуємо StringVar
    )
entry.place(y=50, x=10)

# Отримати текст
value = entry.get()

# Встановити
entry.delete(0, tk.END)
entry.insert(0, "Hello from Entry")

# Очистити
# entry.delete(0, tk.END)


# ======  Checkbutton  ======


enabled = tk.BooleanVar(value=False)

check = ttk.Checkbutton(
    blue_frame,
    text="Button Enabled",
    variable=enabled
)
check.place(y= 10, x =320)

# Change value
# enabled.set(True)

def on_enabled_changed(*args): # *args is mandatory for lazy call and not for lambda call 
     if enabled.get():
          start_button["state"] = "normal"
     else:
          start_button["state"] ="disabled"   

enabled.trace_add("write", on_enabled_changed)

# enabled.trace_add("write", lambda *args: on_enabled_changed())
# Не забуваємо *args та get()



# =====  Radiobutton  =====
# ttk не має способу згрупувати кнопки програмно, тому 
# щоб отримати поточне значення використовуємо StringVar
# Якщо потрібно якось згрупувати ці радокнопки і звертатись 
# до них як до єдиного цілого краще їх сгрупувати у колекцію


rb_selected = tk.StringVar(value="USD")

rb_usd = ttk.Radiobutton(
    blue_frame,
    text="USD",
    value="USD",
    variable=rb_selected
)
rb_usd.place(y= 100, x= 10)

rb_eur = ttk.Radiobutton(
    blue_frame,
    text="EUR",
    value="EUR",
    variable=rb_selected
)
rb_eur.place(y = 100, x = 60)

rb_uah = ttk.Radiobutton(
    blue_frame,
    text="UAH",
    value="UAH",
    variable=rb_selected
)
rb_uah.place(y = 100, x = 120)

radiobuttons = [rb_usd, rb_eur, rb_uah]  #This is not necessary in our case

currency_selected_label = tk.Label(blue_frame,
                  text="Radiobutton selection: default",
                  font=("arial", 12, 'bold'), 
                  fg="#08201A", bg ='lightblue',  # Color may be specified in HEX as '#12edb2'
                  relief = 'solid') 
currency_selected_label.place(y= 100, x = 270)

def rb_selection_changed(*args):
     val = "Radiobutton selection: " + rb_selected.get()
     currency_selected_label.config(text=val)


rb_selected.trace_add("write", rb_selection_changed)


# ===== Combobox  =====


currency = tk.StringVar()
currency.trace_add("write", lambda *args: print("Combobox changed to ", currency.get()))


combo = ttk.Combobox(
    blue_frame,
    textvariable=currency,
    values=["USD", "EUR", "GBP"],
    state="readonly"
)
combo.place(y = 130, x = 10, width=160)

# Combobox frequently use the bind()
def on_currency_selected( event):  #Define callback before the binding
    val = "Combobox selection: " + currency.get() + " from binder"
    currency_selected_label.config(text=val)
    

combo.bind(
    "<<ComboboxSelected>>",
    on_currency_selected
)


# =======  Listbox  =================================
# Список елементів


listbox = tk.Listbox(blue_frame)
listbox.place(y = 98, x = 200, height= 55, width=60)

listbox.insert(tk.END, "USD")
listbox.insert(tk.END, "EUR")
listbox.insert(tk.END, "GBP")
listbox.insert(tk.END, "CHF")
listbox.insert(tk.END, "UAH")
listbox.insert(tk.END, "YEN")

# Get selected element
selection = listbox.curselection()

if selection:
    index = selection[0]
    value = listbox.get(index)

def listbox_selection_changed(event):
    selection = listbox.curselection()
    if selection: 
        index = selection[0]
        val = "Listbox selection: " + listbox.get(index) + " from binder"
        currency_selected_label.config(text=val)     

listbox.bind(
   "<<ListboxSelect>>",
   listbox_selection_changed
)


# ======  Text  ===========
# Багаторядковий текст.


text = tk.Text(blue_frame)
text.place(y= 160, x=10, width=230, height=60)

def on_text_selected(event): 
    try:
        val = text.get("sel.first", "sel.last")  #Задаємо перший і останній символи виділення
        name.set("Text selected: " + val)
    except tk.TclError:
        pass


def on_text_changed(event):
    if text.edit_modified():
        try:
                val = text.get("1.0", tk.END)  #Задаємо перший рядок перший сивол - останній символ
                name.set("Text changed: " + val)
        except tk.TclError:
                pass
        text.edit_modified(False)

text.insert("1.0", " Hello World!\nSincerely yours.\nAndrii")

# Щоб реагувати на виділення тексту "<ButtonRelease-1>"
# Щоб реагувати на зміну тексту "<<Modified>>"

text.bind(
    "<ButtonRelease-1>",
    on_text_selected
)

text.bind(
    "<<Modified>>",
    on_text_changed
)

# Очистити:
# text.delete("2.0", tk.END) #Задає 2 рядок спочатку - до кінця тексту


# ======  Scale ( повзунок)  ======


volume = tk.DoubleVar()

scale = ttk.Scale(
    blue_frame,
    from_=0,
    to=100,
    variable=volume
)

scale.place(y = 170, x=265, width=200, bordermode="outside")

def on_volume_changed(*args):
     val = volume.get()
     name.set("Volume changed to: " + str(val))
     progress["value"] = val

volume.trace_add("write",  on_volume_changed)


# ===== Spinbox  =====


spinbox = ttk.Spinbox(
    blue_frame,
    from_=0,
    to=100,
    textvariable=age,
    command=lambda: print_spin()
)
spinbox.place(y=160, x=470, width=80)

def print_spin():
    yellow_name.set('Spin changed age on ' + str(age.get()))


# =====  Progressbar  =====

progress = ttk.Progressbar(
    blue_frame,
    orient="horizontal",
    length=100,
    mode="determinate"  # determinate for operation wit known duration, for unknown "indeterminate"
)
progress.place(y = 190, x = 255, width=200)

# progress.step(5)  - Визначає наскільки відсотків буде приростати індикатор

# For indeterminate use:
# progress.start()
# Some long operation
# progress.stop()

# -----  5 секунд індикатор бігатиме по шкалі
# progress.start(10)
# blue_frame.after(5000, progress.stop)   # DON"T USE time.sleep in GUI this freeses the program

# ----- simple label with progress
# Цей лейбл виводить інформацію про прогресс поверх індікатору прогресу it's NOT Pretty

progress_label = tk.Label(
    blue_frame,
    text="0%"
)
progress_label.place(y = 191, x = 470)    


# -----  Pretty label on the progressbar (Based on Canvas) -----


canvas = tk.Canvas(
    blue_frame,
    width=200,
    height=20,
    highlightthickness=0
)

canvas.place(x=255, y=215)

# Фон прогресбара
canvas.create_rectangle(
    0, 0, 200, 20,
    fill="lightgray",
    outline=""
)

# Заповнення
progress_2_bar = canvas.create_rectangle(
    0, 0, 0, 20,
    fill="green",
    outline=""
)

# Текст
progress_text = canvas.create_text(
    100, 10,
    text="Progress 2: 0%",
    fill="black"
)

def set_progress(value):
    # змінюємо ширину заповненої частини
    canvas.coords(
        progress_2_bar,
        0, 0,
        200 * value / 100, 20
    )

    canvas.itemconfig(
        progress_text,
        text=f"Progress 2: {value}%"
    )


# -----  Emulate progress - manages the progressbar and labels changes
 
def emulate_progress(value=0):
    progress["value"] = value  #Changes the progressbar itself
    progress_label["text"] = f"Progress: {value}%" #changes label on it

    set_progress(value) #Manages the second progressbar

    if value < 100:
        blue_frame.after(750, emulate_progress, value + 5)



emulate_progress()  


# =====  Separator  ======


#For Vertical separator mandatory use height, for Horizontal width
separator = ttk.Separator(
    blue_frame,
    orient="vertical" # Vertical
)
separator.place(bordermode="outside", x= 275, y=105, width=3, height=60) 

separator = ttk.Separator(
    blue_frame,
    orient="horizontal" # Horizontal
)
separator.place(bordermode="outside", x= 20, y=95, width=480, height=3)


# =====  Scrollbar  =====
 
# У Tkinter/ttk Scrollbar можна прив'язати до віджетів, які мають методи xview() / yview().

# Основні віджети
# Віджет	    Вертикальний	  Горизонтальний	  Команда
# tk.Text	       ✅	              ✅	        yview / xview
# tk.Listbox	   ✅	              ✅	        yview / xview
# tk.Canvas	       ✅	              ✅	        yview / xview
# ttk.Treeview	   ✅	              ✅	        yview / xview
# tk.Entry	       ❌	              ✅	        xview
# ttk.Entry	       ❌	              ✅	        xview
# ttk.Combobox	   ❌	              ❌*	    —
# tk.Label	       ❌	              ❌	        —
# ttk.Label	       ❌	              ❌	        —
# tk.Button	       ❌	              ❌	        —
# ttk.Button	   ❌	              ❌	        —
# tk.Frame	       ❌	              ❌	        —
# ttk.Frame	       ❌	              ❌	        —
# tk.Checkbutton   ❌	              ❌	        —
# ttk.Checkbutton  ❌	              ❌	        —
# tk.Radiobutton   ❌	              ❌	        —
# ttk.Radiobutton  ❌	              ❌	        —
# tk.Spinbox       ❌	              ❌*	    —

# * Віджет може мати внутрішні механізми прокручування/стрілки, але це не стандартний сценарій для зовнішнього Scrollbar. 


listbox_v_scroll = ttk.Scrollbar(
     listbox,
     orient="vertical",
     command=listbox.yview
)
listbox_v_scroll.pack(side="right", fill="y") #fill x- розтягує по х, у - по у


# =====  Canvas  =====
# Низькорівневий графічний віджет.


pure_canvas = tk.Canvas(
    blue_frame,
    width=200,
    height=200
)
pure_canvas.place(y = 230, x=10)

# Лінія:

pure_canvas.create_line(
    10, 190,
    200, 190
)

# Прямокутник:

pure_canvas.create_rectangle(
    50, 190,
    100, 150
)

# Oval
pure_canvas.create_oval(
    150, 10,
    200, 60
)

# Текст:
pure_canvas.create_text(
    60, 10,
    text="Hello from Canvas"
)


# ======  Menu  ======


menubar = tk.Menu(root)

file_menu = tk.Menu(
    menubar,
    tearoff=False
)

def open_file():
     yellow_name.set("Open File menu clicked")

def save_file():
     yellow_name.set("Save File menu clicked")     

file_menu.add_command(
    label="Open",
    command=open_file
)

file_menu.add_command(
    label="Save",
    command=save_file
)

file_menu.add_separator()

file_menu.add_command(
    label="Exit",
    command=root.destroy
)

menubar.add_cascade(
    label="File",
    menu=file_menu
)

root.config(menu=menubar)


#  ======  Context Menu  =====

context_menu = tk.Menu(
    root,
    tearoff=False
)

def context_command():
     yellow_name.set("Context menu clicked")   

context_menu.add_command(
    label="Context command",
    command=context_command
)

def show_context_menu(event):
    context_menu.tk_popup(
        event.x_root,
        event.y_root
    )

blue_frame.bind(
    "<Button-3>",
    show_context_menu
)


#   =====  MessageBox  =====


def show_info_dialog():
    messagebox.showinfo(
        "Information",
        "Operation completed"
    )

context_menu.add_command(
    label="Show info dialog",
    command=show_info_dialog
)

def show_error_dialog():
    messagebox.showerror(
    "Error",
    "Something went wrong"
)

context_menu.add_command(
    label="Show error dialog",
    command=show_error_dialog
)

def show_warning_dialog():
    messagebox.showwarning(
    "Warning",
    "Are you sure?"
)

context_menu.add_command(
    label="Show warning dialog",
    command=show_warning_dialog
)

def show_yesno_dialog():
    result = messagebox.askyesno(
    "Confirm",
    "Delete item?"
    )

    if result:
        show_info_dialog()

context_menu.add_command(
    label="Show yes/no dialog",
    command=show_yesno_dialog
)


#  =====  File dialogs  =====


def show_openfile_dialog():
    filename = filedialog.askopenfilename()
 

context_menu.add_command(
    label="Show open file dialog",
    command=show_openfile_dialog
)

def show_savefile_dialog():
    filename = filedialog.asksaveasfilename()    

context_menu.add_command(
    label="Show save file dialog",
    command=show_savefile_dialog
)

def show_opendir_dialog():
    directory = filedialog.askdirectory()

context_menu.add_command(
    label="Show open dir dialog",
    command=show_opendir_dialog
)

def show_filtered_dialog():
    filename = filedialog.askopenfilename(
    filetypes=[
        ("CSV files", "*.csv"),
        ("All files", "*.*")
    ]
)

context_menu.add_command(
    label="Show filtered dialog",
    command=show_filtered_dialog
)



root.mainloop() #This launch the UI window


