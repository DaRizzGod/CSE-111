import tkinter as tk
from tkinter import Frame, Label, Button
import math

def main():
    # Create the Tk root object.
    root = tk.Tk()

    frm_main = Frame(root)
    frm_main.master.title("Area of Circle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    populate_main_window(frm_main)

    root.mainloop()

def populate_main_window(frm_main):
    # Create a label that displays "Radius:"
    lbl_radius = Label(frm_main, text="Radius:")

    # Create an entry box where the user will enter the radius.
    ent_radius = tk.Entry(frm_main, width=4)
    
    # Create a label that displays "Area:"
    lbl_area = Label(frm_main, text="Area:")

    # Create labels that will display the results.
    lbl_result = Label(frm_main, width=10)

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_radius.grid(row=0, column=0, padx=3, pady=3)
    ent_radius.grid(row=0, column=1, padx=3, pady=3)
    lbl_area.grid(row=1, column=0, padx=3, pady=3)
    lbl_result.grid(row=1, column=1, padx=3, pady=3)
    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=2)

    def calculate():
        try:
            radius = float(ent_radius.get())
            area = math.pi * radius ** 2
            lbl_result.config(text=f"{area:.2f}")
        except ValueError:
            lbl_result.config(text="Invalid input!")

    def clear():
        ent_radius.delete(0, 'end')
        lbl_result.config(text="")
        ent_radius.focus()

    ent_radius.bind("<KeyRelease>", lambda event: calculate())
    btn_clear.config(command=clear)
    ent_radius.focus()

if __name__ == "__main__":
    main()
