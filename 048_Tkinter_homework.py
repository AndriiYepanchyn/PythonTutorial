import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont

BASE_HEIGHT = 150
BASE_FONT_SIZE = 12


def resize_font(event):
    if event.widget == root:
        scale_y = event.height / BASE_HEIGHT
        new_size = min(48,max(8, int(BASE_FONT_SIZE * scale_y)))
        font.configure(size=new_size)

root = tk.Tk()
root.geometry("400x150")
root.title("Temperature convertor")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


frame = tk.Frame(root, bg="lightblue", relief="groove", border=2)
frame.grid(sticky="news", padx=5, pady=5)

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)

frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(3, weight=1)

font = tkfont.Font(
    family="Arial",
    size=12
)




label_calc = tk.Label(frame, font=font, text = "Celsius: ", bg="lightblue")

label_calc.grid(row=0, 
                column=0, 
                padx= 5, 
                pady=5, 
                sticky="w", 
                rowspan=1, 
                columnspan=2)


cels = tk.StringVar()

entry = tk.Entry(frame, font=font, textvariable=cels)
entry.grid(row=0, 
           column=2, 
           padx= 5, 
           pady=5, 
           sticky="news",
           rowspan=1,
           columnspan=2)

label_far = tk.Label(frame, font=font, text="Farenheit: ", bg="lightblue")
label_far.grid(row=1, 
           column=0, 
           padx= 5, 
           pady=5, 
           sticky="w",
           rowspan=1,
           columnspan=2)

result = tk.StringVar()
result.set("Temperature in farenheits...")

label_res  =tk.Label(frame, font=font, textvariable=result, bg="lightblue")
label_res.grid(row=1, 
           column=2, 
           padx= 5, 
           pady=5, 
           sticky="w",
           rowspan=1,
           columnspan=2
)

def on_button_click(event): #For tace_add use *args
    result.set(str(int(cels.get())*1.8 +32))


button = tk.Button(frame, font=font, text="Convert")
button.grid(row=3, 
           column=0, 
           padx= 5, 
           pady=5, 
           sticky="news",
           rowspan=1,
           columnspan=4)
button.bind("<Button-1>", on_button_click)

# cels.trace_add("write", on_button_click)

root.bind("<Configure>", resize_font)
root.mainloop()