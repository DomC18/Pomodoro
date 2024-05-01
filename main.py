from screeninfo import get_monitors
import tkinter as tk

def exit(event) -> None:
    root.destroy()

APP_WIDTH = 800
APP_HEIGHT = 500
MONITOR = get_monitors()[0]
MONITOR_WIDTH_OFFSET = int((MONITOR.width/2)-(APP_WIDTH/2))
MONITOR_HEIGHT_OFFSET = int((MONITOR.height/2)-(APP_HEIGHT/2))

root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry(f"{APP_WIDTH}x{APP_HEIGHT}+{MONITOR_WIDTH_OFFSET}+{MONITOR_HEIGHT_OFFSET}")
root.resizable(width=False, height=False)
root.configure(bg="red")
root.bind("<Escape>", exit)

def get_focus() -> int:
    return int(focus_var.get())

def get_break() -> int:
    return int(break_var.get())

focus_var = tk.StringVar()
focus_var.set("25")
break_var = tk.StringVar()
break_var.set("5")

title_label = tk.Label(root, text="Pomodoro Timer")
title_label.place(relx=0.5, rely=0.05, anchor="center")
focus_option = tk.OptionMenu(root, focus_var, "10", "15", "20", "25", "30", "35", "40", "45", "50", "55", "60")
focus_option.configure(bd=0)
focus_option.place(relx=1/4, rely=0.215, anchor="center")
break_option = tk.OptionMenu(root, break_var, "1", "2", "3", "4", "5", "10", "15", "20")
break_option.configure(bd=0)
break_option.place(relx=3/4, rely=0.215, anchor="center")
start_button = tk.Button(root, text="Start Timer")
start_button.place(relx=0.5, rely=0.215, anchor="center")
timer_label = tk.Label(root)
timer_label.place(relx=0.5, rely=0.5, anchor="center")
reset_button = tk.Button(root, text="Reset Timer")
reset_button.place(relx=1/3, rely=0.785, anchor="center")
stop_button = tk.Button(root, text="Stop Timer")
stop_button.place(relx=2/3, rely=0.785, anchor="center")


root.mainloop()