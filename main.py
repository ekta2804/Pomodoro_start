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
CHECK = "🗸"
reps = 0 
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_lable, text = "00:00")
    timer_lable.config(text= "Timer")
    check_lable.config(text="")
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
        count_down(long_break_sec)
        timer_lable.config(text= "Break Time " ,fg= RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_lable.config(text="Break Time" ,fg= PINK)
    else:
        count_down(work_sec)
        timer_lable.config(text="work" , fg = GREEN)

    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(c_t, text= f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_ses = math.floor(reps/2)
        for _ in range(work_ses):
            marks += CHECK
        check_lable.config(text=marks)
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx= 100 , pady=50, bg= YELLOW )

canvas = Canvas(width= 200 , height= 226, bg = YELLOW, highlightthickness=0)
t_image = PhotoImage(file= "pomodoro-start/tomato.png")
canvas.create_image(100, 112, image = t_image)
c_t = canvas.create_text(100, 130, text= "00:00" , fill= "white", font=(FONT_NAME, 35 , "bold")) #in tkinter the fill = color
canvas.grid(column=1 , row=1)

timer_lable = Label(text="Timer", fg = GREEN, bg = YELLOW , font= (FONT_NAME , 35, "bold"))

timer_lable.grid(column=1, row= 0)

check_lable = Label(bg = YELLOW , fg= RED , font= (20))
check_lable.grid(column=1, row = 4)

s_button = Button(text="Start" ,highlightthickness=0, command= start_timer )
s_button.grid(column=0 , row=3)

r_button = Button(text="Reset" , highlightthickness=0, command= reset)
r_button.grid(column=3 , row=3)



window.mainloop()