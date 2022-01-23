from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    """
    If user clicks on Reset button, reset the timer, and remove the tick marks and set the timer to zero
    :return:
    """
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(remaining_time_text, text="00:00")
    timer_label.config(text="TIMER", fg=GREEN)
    tick_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    """
    When Start button is clicked, Pomodoro count down starts
    There are 3 time zones - 1 Work, 2 short break, after 4 such work+short breaks, there is a long break
    :return:
    """
    global reps
    reps += 1
    print(f"REPS::{reps}")
    if reps == 8:
        rem_seconds = LONG_BREAK_MIN * 60
        timer_label.config(text="ON LONG BREAK", fg=RED)
    elif reps % 2 == 0:
        rem_seconds = SHORT_BREAK_MIN * 60
        timer_label.config(text="ON SHORT BREAK", fg=PINK)
    else:
        rem_seconds = WORK_MIN * 60
        timer_label.config(text="WORK TIME REM", fg=GREEN)

    count_down(rem_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(rem_seconds):
    """
    Count down the timer
    :param rem_seconds:
    :return:
    """
    global timer
    minute, sec = divmod(rem_seconds, 60)
    time = "{:02d}:{:02d}".format(minute, sec)
    canvas.itemconfig(remaining_time_text, text=time)
    rem_seconds -= 1
    if rem_seconds > 0:
        timer = window.after(1000, count_down, rem_seconds)
    else:
        start_time()
        if reps % 2 == 0:
            tick_marks["text"] = "✅ " * (reps // 2)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=50, pady=50, bg=YELLOW)

# Timer label on top
timer_label = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
timer_label.grid(row=0, column=1)

# Canvas to add image and text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)

remaining_time_text = canvas.create_text(100, 120, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Start button
start_btn = Button(text="START", relief="sunken", bg=PINK, font=("Arial", 10, "bold"), command=start_time)
start_btn.grid(row=2, column=0)

# Reset button
reset_btn = Button(text="RESET", relief="sunken", bg=PINK, font=("Arial", 10, "bold"), command=reset)
reset_btn.grid(row=2, column=2)

# Tick marks that indicate the number of work sessions that got over
tick_marks = Label(bg=YELLOW, fg=GREEN)
tick_marks.grid(row=3, column=1)

window.mainloop()
