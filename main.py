from screeninfo import get_monitors
import customtkinter as ctk
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

root = ctk.CTk("red")
root.title("Pomodoro Timer")
root.resizable(width=False, height=False)
root.geometry(f"{APP_WIDTH}x{APP_HEIGHT}+{MONITOR_WIDTH_OFFSET}+{MONITOR_HEIGHT_OFFSET}")
root.bind("<Escape>", exit)

def get_focus() -> int:
    return int(focus_var.get())

def get_break() -> int:
    return int(break_var.get())

focus_var = ctk.Variable()
focus_var.set("25")
break_var = ctk.Variable()
break_var.set("5")
time_var = ctk.Variable()
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

title_label = ctk.CTkLabel(root, text="Pomodoro Timer", justify="center", font=("Times New Roman", 55, "bold"), bg_color="red")
title_label.place(relx=0.5, rely=0.1, anchor="center")
focus_label = ctk.CTkLabel(root, text="Focus Time (Minutes)", justify="center", font=("Times New Roman", 25), bg_color="red")
focus_label.place(relx=1/4, rely=0.275, anchor="center")
focus_option = ctk.CTkOptionMenu(master=root, variable=focus_var, font=("Times New Roman", 30, "bold"), bg_color="red", values=["1", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55", "60"])
focus_option.place(relx=1/4, rely=0.375, anchor="center")
break_label = ctk.CTkLabel(root, text="Break Time (Minutes)", font=("Times New Roman", 25), bg_color="red")
break_label.place(relx=3/4, rely=0.275, anchor="center")
break_option = ctk.CTkOptionMenu(master=root, variable=break_var, font=("Times New Roman", 30, "bold"), bg_color="red", values=["1", "2", "3", "4", "5", "10", "15", "20"])
break_option.place(relx=3/4, rely=0.375, anchor="center")
timer_label = ctk.CTkLabel(root, textvariable=time_var, justify="center", font=("Times New Roman", 80, "bold"))
timer_label.place(relx=0.5, rely=0.6, anchor="center")
reset_button = ctk.CTkButton(root, text="Reset", font=("Times New Roman", 30, "bold"))
reset_button.configure(command=reset_timer)
reset_button.place(relx=1/6, rely=0.85, anchor="center")
start_button = ctk.CTkButton(root, text="Start", font=("Times New Roman", 30, "bold"))
start_button.configure(command=start_timer)
start_button.place(relx=2/4, rely=0.85, anchor="center")
stop_button = ctk.CTkButton(root, text="Stop", font=("Times New Roman", 30, "bold"))
stop_button.configure(command=stop_timer)
stop_button.place(relx=5/6, rely=0.85, anchor="center")

root.after(1000, timer_count)
root.mainloop()