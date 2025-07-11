import tkinter as tk
from tkinter import ttk

answer = None

def get_sword():
    global answer
    answer = "sword"

def get_bow():
    global answer
    answer = "bow"

def sword_or_bow():
    global answer
    root = tk.Tk()
    root.geometry("300x100")
    root.resizable(False, False)
    root.title("Gwent - Get Sword and Bow")

    sword_btn = ttk.Button(root, text="Get Sword", command=lambda: get_sword())
    sword_btn.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )

    bow_btn = ttk.Button(root, text="Get Bow", command=lambda: get_bow())
    bow_btn.pack(
        ipadx=5,
        ipady=10,
        expand=True
    )

    exit_button = ttk.Button(
        root,
        text='Exit',
        command=root.destroy
    )

    exit_button.pack(
        ipadx=5,
        ipady=15,
        expand=True
    )

    root.mainloop()

    return answer