from screeninfo import get_monitors
import tkinter as tk
import pygame as pyg
import sys
import os

sys.setrecursionlimit(10**6)
pyg.mixer.init()

def play_alarm():
    pyg.mixer.music.load(os.getcwd() + r"\alarm.wav")
    pyg.mixer.music.play()

def exit(event) -> None:
    root.destroy()

APP_WIDTH = 960
APP_HEIGHT = 620
MONITOR_WIDTH_OFFSET = int((get_monitors()[0].width/2)-(APP_WIDTH/2))
MONITOR_HEIGHT_OFFSET = int((get_monitors()[0].height/2)-(APP_HEIGHT/2))

root = tk.Tk(); root.configure(bg="red"); root.bind("<Escape>", exit); root.resizable(width=False, height=False)
root.title("Pomodoro Timer")
root.geometry(f"{APP_WIDTH}x{APP_HEIGHT}+{MONITOR_WIDTH_OFFSET}+{MONITOR_HEIGHT_OFFSET}")

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

should_count = False
to_break = False
timer_time = 0

def start_timer() -> None:
    global should_count, timer_time
    should_count = True
    timer_time = ((get_focus()*60)+1) if timer_time == 0 else timer_time

def stop_timer() -> None:
    global should_count
    should_count = False

def timer_count() -> None:
    global should_count, timer_time, to_break
    if should_count:
        timer_time -= 1
        time_var.set(f"{timer_time//60:02}:{timer_time%60:02}")
        if timer_time == 0:
            if to_break:
                to_break = False
                timer_time = ((get_break()*60)+1) if timer_time == 0 else timer_time
            else:
                to_break = True
                timer_time = ((get_focus()*60)+1) if timer_time == 0 else timer_time
            play_alarm()
    else:
        pass
    root.after(1000, timer_count)

def reset_timer() -> None:
    global timer_time
    timer_time = 0
    stop_timer()
    time_var.set("00:00")

title_label = tk.Label(root, text="Pomidoro Timer", justify="center", font=("Times New Roman", 55, "bold"), bg="red")
title_label.place(relx=0.5, rely=0.1, anchor="center")
focus_label = tk.Label(root, text="Focus Time (Minutes)", justify="center", font=("Times New Roman", 25), bg="red")
focus_label.place(relx=1/4, rely=0.275, anchor="center")
focus_option = tk.OptionMenu(root, focus_var, "1", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55", "60")
focus_option.configure(bd=0, justify="center", font=("Times New Roman", 30, "bold"), bg="red")
focus_option.place(relx=1/4, rely=0.375, anchor="center")
break_label = tk.Label(root, text="Break Time (Minutes)", justify="center", font=("Times New Roman", 25), bg="red")
break_label.place(relx=3/4, rely=0.275, anchor="center")
break_option = tk.OptionMenu(root, break_var, "1", "2", "3", "4", "5", "10", "15", "20")
break_option.configure(bd=0, justify="center", font=("Times New Roman", 30, "bold"), bg="red")
break_option.place(relx=3/4, rely=0.375, anchor="center")
timer_label = tk.Label(root, textvariable=time_var, justify="center", font=("Times New Roman", 80, "bold"))
timer_label.place(relx=0.5, rely=0.6, anchor="center")
reset_button = tk.Button(root, text="Reset", justify="center", font=("Times New Roman", 30, "bold"))
reset_button.configure(command=reset_timer)
reset_button.place(relx=1/6, rely=0.85, anchor="center")
start_button = tk.Button(root, text="Start", justify="center", font=("Times New Roman", 30, "bold"))
start_button.configure(command=start_timer)
start_button.place(relx=2/4, rely=0.85, anchor="center")
stop_button = tk.Button(root, text="Stop", justify="center", font=("Times New Roman", 30, "bold"))
stop_button.configure(command=stop_timer)
stop_button.place(relx=5/6, rely=0.85, anchor="center")

root.after(1000, timer_count)
root.mainloop()