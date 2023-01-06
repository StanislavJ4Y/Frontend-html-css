from tkinter import *
from tkinter import messagebox 


tk = Tk()
app_running = True

def on_closing():
    global app_running
    if messagebox.askokcancel("quit", "Do you want to quit?"):
        app_running = False
tk.destroy()

tk.protocol("WM_DELETE_WINDOW", on_closing)

tk.title ("Крестики-нолики")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=1280, height=768, bd=0, highlightthickness=0)
canvas.pack()
tk.update()