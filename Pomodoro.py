import tkinter as tk
from tkinter import ttk
from tkinter import CENTER, Button, Canvas, Label, PhotoImage

global reps
global paused
global timer_started
reps = 0
paused = False
timer_started = False

work_min = 25
short_break_min = 5
long_break_min = 10

yellow = '#F7F5dd'
red = '#e7305b'

timer1 = None

def popupmsg(msg):
    popup = tk.Tk()
    popup.geometry("1000x800")
    popup.title("Pomodoro Timer")

    if ((reps+1) % 2 == 0) or ((reps+1) % 8 == 0):
        label = ttk.Label(popup, text='PRESS "Start" TO BEGIN YOUR BREAK', background=yellow, font=('Courier',25,'bold'))
        label.config(anchor=CENTER)
        label.pack(side="top", fill="x", pady=10)
        photo = tk.PhotoImage(file='break.png', master=popup)
        image_label = ttk.Label(popup, image=photo, background=yellow)
        image_label.pack()
        timer_started = False
    else:
        label = ttk.Label(popup, text='PRESS "Start" TO WORK AGAIN', background=yellow, font=('Courier',25,'bold'))
        label.config(anchor=CENTER)
        label.pack(side="top", fill="x", pady=10)
        photo = tk.PhotoImage(file='work.png', master=popup)
        image_label = ttk.Label(popup, image=photo, background=yellow)
        image_label.pack()
        timer_started = False

    popup.eval('tk::PlaceWindow . center')
    popup.configure(bg=yellow)
    popup.mainloop()


def count_down(count):
        global timer1
        global timer_started
        
        mins = count // 60
        secs = count % 60

        timer = '{:02d}:{:02d}'.format(mins, secs)
        timer_text = canvas.delete('squa')
        timer_text = canvas.create_text(100, 130, text=timer, fill='#424242', tag="squa", font=('Courier',45,'bold'))
        canvas.place(x=15, y=40)

        if (count == 0):
                timer_started = False
                popupmsg('Press "Start" to begin your break')            
        if (count > 0) and not paused:
            timer1 = window.after(1000, count_down, count - 1)
        elif (count > 0) and paused:
            timer1 = window.after(1000, count_down, count)


def start_timer():
    global reps
    global paused
    global timer_started

    if (not paused) and (timer_started == False):
        reps += 1
        timer_started = True
        work_sec = work_min * 60
        short_break_sec = short_break_min * 60
        long_break_sec = long_break_min * 60

        if reps % 8 == 0:
            count_down(long_break_sec)
            title_label.config(text='Break', fg=red)
        elif reps % 2 == 0:
            count_down(short_break_sec)
            title_label.config(text='Break', fg=red)
        else:
            count_down(work_sec)
            title_label.config(text='Work', fg='#424242')
            title_label.place(x=55, y=5)
    else:
        paused = False


def reset_timer():
    window.after_cancel(timer1)
    timer_text = canvas.delete('squa')
    imer_text = canvas.create_text(100, 130, text='25:00', fill='#424242', tag="squa", font=('Courier',45,'bold'))
    canvas.place(x=15, y=40)
    title_label.config(text='Timer', fg='#424242')
    title_label.place(x=32, y=5)
    global reps
    global paused
    global timer_started 
    reps = 0
    paused = False
    timer_started = False


def stop_timer(is_paused):
    global paused
    paused = is_paused
    if not paused:
        paused = True
    else:
        paused = False


window = tk.Tk()
window.geometry("300x360")
window.resizable(False, False)
window.title('Pomodoro Timer')
window.config(padx=40, pady=10, bg=yellow)
title_label = tk.Label(text='Timer', fg='#424242', bg=yellow, font=('Courier',40,'bold'))
title_label.place(x=32, y=5)

download1_icon = tk.PhotoImage(file='button_start.png')
start_button = tk.Button(window, image=download1_icon, command=start_timer)
start_button.place(x=0, y=270)
download_icon = tk.PhotoImage(file='button_stop.png')
stop_button = tk.Button(window, image=download_icon, command=lambda: stop_timer(paused))
stop_button.place(x=80, y=270)
download2_icon = tk.PhotoImage(file='button_reset.png')
reset_button = tk.Button(window, image=download2_icon, command=reset_timer)
reset_button.place(x=160, y=270)

canvas = Canvas(width=240, height=224, bg=yellow, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='25:00', fill='#424242', tag="squa", font=('Courier',45,'bold'))
canvas.place(x=15, y=40)

window.mainloop()