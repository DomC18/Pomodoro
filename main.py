from screeninfo import get_monitors
import tkinter as tk
import sys

sys.setrecursionlimit(10**6)

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
time_var = tk.StringVar()
time_var.set("00:00")

def start_timer() -> None:
    time = get_focus() * 60
    time_var.set(f"{time//60:02d}:{time%60:02d}")
    time -= 1
    root.after(1000, start_timer)

def stop_timer() -> None:
    ...

def reset_timer() -> None:
    ...

title_label = tk.Label(root, text="Pomidoro Timer", justify="center", font=("Times New Roman", 55, "bold"), bg="red")
title_label.place(relx=0.5, rely=0.1, anchor="center")
focus_label = tk.Label(root, text="Focus Time (Minutes)", justify="center", font=("Times New Roman", 25), bg="red")
focus_label.place(relx=1/4, rely=0.275, anchor="center")
focus_option = tk.OptionMenu(root, focus_var, "10", "15", "20", "25", "30", "35", "40", "45", "50", "55", "60")
focus_option.configure(bd=0, justify="center", font=("Times New Roman", 30, "bold"), bg="red")
focus_option.place(relx=1/4, rely=0.375, anchor="center")
break_label = tk.Label(root, text="Break Time (Minutes)", justify="center", font=("Times New Roman", 25), bg="red")
break_label.place(relx=3/4, rely=0.275, anchor="center")
break_option = tk.OptionMenu(root, break_var, "1", "2", "3", "4", "5", "10", "15", "20")
break_option.configure(bd=0, justify="center", font=("Times New Roman", 30, "bold"), bg="red")
break_option.place(relx=3/4, rely=0.375, anchor="center")
timer_label = tk.Label(root, textvariable=time_var, justify="center", font=("Times New Roman", 80, "bold"))
timer_label.place(relx=0.5, rely=0.6, anchor="center")
reset_button = tk.Button(root, text="Reset Timer", justify="center", font=("Times New Roman", 30, "bold"))
reset_button.configure(command=reset_timer)
reset_button.place(relx=1/6, rely=0.85, anchor="center")
start_button = tk.Button(root, text="Start Timer", justify="center", font=("Times New Roman", 30, "bold"))
start_button.configure(command=start_timer)
start_button.place(relx=2/4, rely=0.85, anchor="center")
stop_button = tk.Button(root, text="Stop Timer", justify="center", font=("Times New Roman", 30, "bold"))
stop_button.configure(command=stop_timer)
stop_button.place(relx=5/6, rely=0.85, anchor="center")

root.after(1000, start_timer)

root.mainloop()