from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
time = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(time)
    canvas.itemconfig(timer_text, text="00:00")
    checkmarks.config(text="")
    timer.config(text="Timer", fg=GREEN)
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer.config(text="Long Break", bg=YELLOW, fg=RED, font=(FONT_NAME, 45))
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer.config(text="Short Break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 45))
    else:
        countdown(work_sec)
        timer.config(text="Work...Lessgoo My Dood", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 00:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
        count_min = f"0{count_min}"
    elif count_min == 0:
        count_min = f"0{count_min}"
    elif count_min == 00 and count_sec == 00:
        reps += 1
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global time
        time = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        checkmarks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer Label
timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45))
timer.grid(column=1, row=0)

# Start Button
start_button = Button(text="Start", font=(FONT_NAME, 20), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text="Reset", font=(FONT_NAME, 20), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Checkmark
checkmarks = Label(fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)


window.mainloop()
