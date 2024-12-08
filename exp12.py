import tkinter as tk
from tkinter import messagebox

def on_button_click():
    user_input = entry.get()
    messagebox.showinfo("THIS IS HOW IT IS", f"THIS IS WHAT YOU HAVE ENTERED : {user_input}")


root = tk.Tk()
root.title("HOW DO YOU LIKE THIS")
root.geometry("300x300")

label = tk.Label(root, text="Enter something:")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

button = tk.Button(root, text="I AM DONE ENTERING ", command=on_button_click)
button.pack(pady=10)

root.mainloop()
