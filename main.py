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
LONG_BREAK_MIN = 20
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global REPS
    REPS += 1
    work_sec = 60 * WORK_MIN
    short_break_sec = 60 * SHORT_BREAK_MIN
    long_break_sec = 60 * LONG_BREAK_MIN

    if REPS in [1, 3, 5, 7]:
        timer_label.config(text="Focus Time", fg=GREEN)
        countdown(work_sec)
    elif REPS in [2, 4, 6]:
        timer_label.config(text="Tea Time", fg=PINK)
        countdown(short_break_sec)
    elif REPS == 8:
        timer_label.config(text="Relax",fg=RED)
        countdown(long_break_sec)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):

    count_minute = math.floor(count/60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_minute:02}:{count_sec:02}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ''
        work_sessions = (math.floor(REPS / 2))
        for x in range(work_sessions):
            mark += "✔"
            checkmark_label.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1,row=1)


start_button = Button(text="Start", highlightbackground=YELLOW, highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text='Reset', highlightbackground=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2,row=2)

timer_label = Label(text="Timer", font=("Comic Sans",50,'bold'), fg=GREEN,bg=YELLOW)
timer_label.grid(column=1,row=0)

checkmark_label = Label(font=("Times New Roman", 25, "italic"), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1,row=3)



window.mainloop()