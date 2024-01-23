import random
import tkinter as tk

def generate_random_numbers():
    myList = []
    while len(myList) < 10:
        val = random.randint(1, 100)
        myList.append(val)
    result_label.config(text=myList)

def open_toplevel():
    top = tk.Toplevel(root)
    top.title("Random Numbers")
    
    global result_label  # Make result_label a global variable
    result_label = tk.Label(top, text="", padx=20, pady=20, font=("Helvetica", 60))  # Set font size to 20
    result_label.pack()
    
    generate_random_numbers()

root = tk.Tk()
root.title("Random Number Generator")

label = tk.Label(root, text="Enter a number:")
label.pack()

entry = tk.Entry(root)
entry.pack()

generate_button = tk.Button(root, text="Generate Random Numbers", command=open_toplevel)
generate_button.pack()

root.mainloop()
