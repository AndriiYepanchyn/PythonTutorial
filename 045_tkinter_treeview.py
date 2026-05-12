import tkinter as tk
from tkinter import ttk

class TreeviewEdit(ttk.Treeview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Bind mouse clicks
        self.bind("<Double-1>", self.on_double_click)


    def on_double_click(self, event):
        # Identify region name where event caused
        # There are following options enabled: "tree", "cell", "heading", "nothing"
        region = self.identify_region(event.x, event.y)

        # Define exact element clicked on
        # Columns has names like #0 counting from 0
        column = self.identify_column(event.x)

        # Rows named as I001, starts from 001 rows and columns may be identified only inside rows block
        row = self.identify_row(event.y)
        element = self.identify_element(event.x, event.y)

        # Return iid of the row in format I001
        selected_iid = self.focus()

        # Return dict with: text (include name if this tree item), image, values (list of values in columns after text), open, tags
        selected_values = self.item(selected_iid)
        
        if region not in ("tree", "cell"):
            return  
        
        # 1 = number of text columns before values
        col_index = int(column[1:])-1       

        if column == '#0':
            selected_text = selected_values.get("text")
        else:
            selected_text = selected_values.get("values")[col_index]    
        # print("selected text = ", selected_text)    

        # This will return bbox object with [x, y, w, h] of the selected cell
        col_box = self.bbox(selected_iid, column=column)

        # This object will be used to enter new value in cell and placed directly on top of it
        # This object should be disposed after usege otherwise it stay cover the cell
        edit_entry = ttk.Entry(self)
        edit_entry.place(x=col_box[0], y=col_box[1], width=col_box[2], height=col_box[3])

        # Define correct behaviour of the edit_entry while editing
        edit_entry.editing_column_index = col_index
        edit_entry.editing_item_iid = selected_iid

        edit_entry.insert(0, selected_text)
        edit_entry.select_range(0, tk.END)

        edit_entry.focus() #Made the widget selected

        edit_entry.bind("<FocusOut>", self.on_focus_out)
        edit_entry.bind("<Return>", self.on_enter_pressed)


    def on_focus_out(self, event):
        event.widget.destroy()

    def on_enter_pressed(self, event):
        new_text = event.widget.get()
        selected_iid = event.widget.editing_item_iid
        selected_col = event.widget.editing_column_index

        if selected_col == -1:
            self.item(selected_iid, text = new_text)
        else:
           cur_values = self.item(selected_iid).get("values")
           cur_values[selected_col] = new_text 
           self.item(selected_iid, values = cur_values)
        
        event.widget.destroy()







# -----  Methods configuring window  -----
def configure_window(root : tk.Tk):
    root.title("TreeView demo")
    
# ------  Methods configuring TreeView  -----
def define_columns(parent):
    # Define columns
    parent.heading('#0', text = 'Vehicle type', anchor='w')
    parent.heading("vehicle_name", text = "Vehicle name")
    parent.heading("year", text = "Year")
    parent.heading("colour", text = "Colour")

def define_rows(parent):
    # Define Rows
    # Sedan_row variable may be used as parent for the next rows
    sedan_row = parent.insert(parent="",
                             index=tk.END,
                             text = "Sedan")
    
    parent.insert(parent=sedan_row,
                             index=tk.END,
                             values=('Honda civic', '2010', 'White'))
    
    parent.insert(parent=sedan_row,
                             index=tk.END,
                             values=('Honda accord', '2020', 'Grey'))
    parent.insert(parent=sedan_row,
                             index=tk.END,
                             values=('Honda accord', '2020', 'Silver'))
    parent.insert(parent=sedan_row,
                             index=tk.END,
                             values=('Mazda MX6', '2015', 'Red'))
    parent.insert(parent=sedan_row,
                             index=tk.END,
                             values=('Renault megane', '2013', 'Beige'))
    

if __name__ == "__main__":

    root = tk.Tk()
    configure_window(root)
    columns = ('vehicle_name', 'year', 'colour')
    treeview_vehicles = TreeviewEdit(root, columns = columns)

    define_columns(treeview_vehicles)
    define_rows(treeview_vehicles)




    
    
    
    

    treeview_vehicles.pack(fill= tk.BOTH, expand=True)
    root.mainloop()