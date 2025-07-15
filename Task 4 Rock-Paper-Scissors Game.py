from tkinter import *
import random 

#=================Main Window==============
win = Tk()
win.title("Rock vs Paper vs Scissors")
win.geometry("520x530")
win.resizable(False, False)
win.configure(bg="#f0f4fc")  # Soft single background colour

#================Global Variables==========
player_score = 0
computer_score = 0
choices = ['Rock', 'Paper', 'Scissors']

#===================Functions==============
def play(player_choice):
    global player_score, computer_score
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "🎯 It's a Tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "🎯 You Won!"
        player_score += 1
    else:
        result = "🎯 You Lose!"
        computer_score += 1
    update(player_choice, computer_choice, result)

def update(player_choice, computer_choice, result):
    player_label.config(text=f'🧑‍💼 Your Choice ➡ {player_choice}')
    computer_label.config(text=f'💻 Computer\'s Choice ➡ {computer_choice}')
    result_label.config(text=result)
    score_label.config(text=f'📊 Score ➡ You: {player_score} | Computer: {computer_score}')

def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    player_label.config(text='🧑‍💼 Your Choice:')
    computer_label.config(text='💻 Computer\'s Choice')
    result_label.config(text='🎯 Result')
    score_label.config(text=f'📊 Score ➡ You: 0 | Computer: 0')

def on_enter(e):
    e.widget.config(bg="#ffe066", fg="#333")

def on_leave(e):
    e.widget.config(bg=e.widget.default_bg, fg=e.widget.default_fg)

#====================Widgets======================
title = Label(win, text='Rock * Paper * Scissors', 
              font=("Georgia", 24, "bold"), bg="#f0f4fc", fg="#1a1a1a")
title.place(x=60, y=30)

# Styled Buttons
def styled_button(text, color, x, command):
    btn = Button(win, text=text, font=("Verdana", 12, "bold"), width=16, height=2,
                 bg=color, fg="#1a1a1a", activebackground="#ffcccb", command=command)
    btn.default_bg = color
    btn.default_fg = "#1a1a1a"
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.place(x=x, y=100)
    return btn

styled_button("Rock", "#d0e1ff", 50, lambda: play("Rock"))
styled_button("Paper", "#d0ffd6", 190, lambda: play("Paper"))
styled_button("Scissors", "#ffd6d6", 330, lambda: play("Scissors"))

player_label = Label(win, text='🧑‍💼 Your Choice:', font=("Helvetica", 13), bg="#f0f4fc", fg="#222")
player_label.place(x=30, y=250)

computer_label = Label(win, text='💻 Computer\'s Choice', font=("Helvetica", 13), bg="#f0f4fc", fg="#222")
computer_label.place(x=30, y=200)

result_label = Label(win, text='🎯 Result', font=("Helvetica", 14, "bold"), bg="#f0f4fc", fg="#005f73")
result_label.place(x=30, y=320)

score_label = Label(win, text='📊 Score ➡ You: 0 | Computer: 0', font=("Helvetica", 13, "bold"), bg="#f0f4fc", fg="#00771e")
score_label.place(x=30, y=360)

reset_btn = Button(win, text='🔄 Reset Game', width=18, font=("Verdana", 12), bg="#ffddaa", fg="#301934", command=reset_game)
reset_btn.default_bg = "#ffddaa"
reset_btn.default_fg = "#301934"
reset_btn.bind("<Enter>", on_enter)
reset_btn.bind("<Leave>", on_leave)
reset_btn.place(x=170, y=410)

win.mainloop()
