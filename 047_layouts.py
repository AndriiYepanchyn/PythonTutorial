import tkinter as tk
from tkinter import ttk


# У Tkinter є три geometry managers.

# ----- pack  -----  

# Простий лінійний layout:
# Основні параметри:

# side="top" / "bottom" / "left" / "right"
# fill="x" / "y" / "both"
# expand=True
# padx
# pady
# ipadx
# ipady


#  ------  grid  ------

# Найзручніший для форм.

#  -----  place  -----

# Абсолютне/відносне позиціонування.

# Не використовуй pack() і grid() всередині одного контейнера для віджетів одного рівня.
# Погано:

# frame = ttk.Frame(root)

# label.pack(parent=frame)
# button.grid(parent=frame)  # ❌

# Але можна:

# root
#  ├── frame1 → pack
#  │    └── widgets → grid
#  │
#  └── frame2 → pack
#       └── widgets → pack

root = tk.Tk()
root.title("My Application")  #Set title of the window
root.geometry("600x900")

style1 = ttk.Style()
style1.configure(
     "Blue.TFrame",
     background="#c5eafc"
)

style2 = ttk.Style()
style2.configure(
     "Green.TFrame",
     background="#338006"
)

style3 = ttk.Style()
style3.configure(
     "Rose.TFrame",
     background="#F8586D"
)


frame1 = ttk.Frame(root)
frame1.configure(relief = 'raised', style="Blue.TFrame")
frame1.pack(fill="both", expand=True, padx=5, pady=5)

frame2= ttk.Frame(root)
frame2.configure(relief = 'raised', style="Green.TFrame")
frame2.pack(fill="both", expand=True,  padx=5, pady=5)


frame3 = ttk.Frame(root)
frame3.configure(relief = 'raised', style="Rose.TFrame")
frame3.pack(fill="both", expand=True,  padx=5, pady=5)

# -----  pack -----

label_pack = ttk.Label(frame1, text="Pack geometry manager" )
label_pack.pack(anchor="nw") #Define position of the label in the parent

label_pack_1 = ttk.Label(frame1, text="label_1" )
label_pack_1.pack()

label_pack_2 = ttk.Label(frame1, text="label_2 anchor=w" )
label_pack_2.pack(anchor="w")

label_pack_3 = ttk.Label(frame1, text="label_3" )
label_pack_3.pack()

label_pack_4 = ttk.Label(frame1, text="label_4 anchor=se" )
label_pack_4.pack(anchor="se")


#  -----  Place  -----
label_place = ttk.Label(frame2, text="Place geometry manager")
label_place.place(x = 10, y= 10)

label_place_1 = ttk.Label(frame2, text="label 1 at (50, 50)")
label_place_1.place(x=50, y= 50)

label_place_2 = ttk.Label(frame2, text="label 2 at (250, 50)")
label_place_2.place(x=250, y= 50)

label_place_3 = ttk.Label(frame2, text="label 3 at (50, 150)")
label_place_3.place(x=50, y= 150)


# -----  Grid  ------
label_grid = ttk.Label(frame3,  text="Grid geometry manager")
label_grid.grid(column=0, row=0, padx=5, pady=5)

label_grid_1 = ttk.Label(frame3, text="Grid label 1 row = 2, col=2")
label_grid_1.grid(row=2, column=2, padx=5, pady=5)

label_grid_2 = ttk.Label(frame3, text="Grid label 2 row = 5, col=5")
label_grid_2.grid(row=5, column=5, padx=5, pady=5)

label_grid_3 = ttk.Label(frame3, text="Grid label 3 row = 3, col=0, rowspan=3")
label_grid_3.grid(row=3, column=0,rowspan=3, padx=5, pady=5)

label_grid_4 = ttk.Label(frame3, text="Grid label 4 row = 4, col=5")
label_grid_4.grid(row=4, column=5, padx=5, pady=5)

label_grid_5 = ttk.Label(frame3, text="Grid label 5 row = 3, col=5, colspan=2")
label_grid_5.grid(row=3, column=5, columnspan=2, padx=5, pady=5)


root.mainloop()