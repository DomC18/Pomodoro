import tkinter as tk

def exit(event) -> None:
    root.destroy()

root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("800x500+560+290")
root.resizable(width=False, height=False)
root.configure(bg="red")
root.bind("<Escape>", exit)



root.mainloop()