from tkinter import *
import os

main_dir = os.path.dirname(__file__)
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
reset = False
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps, reset
    timer_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    reps = 0
    canvas.itemconfig(countdown_timer, text="00:00")
    reset = True
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps, reset
    reset = False
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 0:
        check_marks.config(text=check_marks["text"] + "✔", fg=GREEN)
    if not reps % 8:
        timer_label.config(text="Long Break time", fg=RED)
        timer(long_break_sec)
    elif reps % 2 == 1:
        timer_label.config(text="Work Time", fg=GREEN)
        timer(work_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Short Break Time", fg=PINK)
        timer(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def timer(count):
    global reset
    if not reset:
        minutes = count // 60
        seconds = count % 60
        if seconds < 10:
            seconds = f"0{seconds}"
        canvas.itemconfig(countdown_timer, text=f"{minutes}:{seconds}")
        if count > 0:
            window.after(1000, timer, count - 1)
        else:
            start_timer()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file=main_dir+"/tomato.png")
canvas.create_image(100, 112, image=tomato_image)
countdown_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"),
                    highlightthickness=0, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text="", bg=YELLOW, fg=GREEN, highlightthickness=0, font=(FONT_NAME, 10))
check_marks.grid(column=1, row=3)


window.mainloop()
