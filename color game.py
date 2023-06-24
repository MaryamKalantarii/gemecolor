from tkinter import *
from tkinter import messagebox
import random

color=['yellow','blue','green','black','red','purple','white','Orange','Brown']

score=0
score1 = 0 # Changed this to start from zero
timeleft =30
score_increment = 1 # Added this to control the score change

def startgame(event):
    if timeleft == 30:
        countdown()
    nextcolor()


def nextcolor():
    global score
    global timeleft
    global score1
    global score_increment # Added this to use the score change
    # global score1
    if timeleft > 0:
        e.focus_set()
        if e.get().lower()==color[1].lower():
            score += score_increment # Changed this to use the score change
            
        else: # Added this else clause to handle the wrong answer
            e.get().lower()!=color[1].lower()
            score1 -= score_increment # Changed this to use the score change
            
        e.delete(0,END)
        random.shuffle(color)
        label.config(fg=str(color[1]),text = str(color[0]))
        scorelbl.config(text="Score: " + str(score) , font=('tahoma',12))
        scorelbl1.config(text="Negative score: " + str(score1) , font=('tahoma',12)) # Moved this inside the if clause
    
    

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -=1
        time.config(text='Time:' + str(timeleft), font=('tahoma',12))
        
        if timeleft ==0:
            messagebox.showinfo('end of time','Your time is up')
        time.after(1000,countdown)

win = Tk()
win.geometry('400x300+300+100')
win.title("Color game")
win.config(bg='purple')
lbl = Label(win , text='Enter the color of each word in English',font= 'tahoma 12 bold' , fg='purple')
lbl.pack()

scorelbl=Label(win, text='Press enter to start the game',font= 'tahoma 12 bold' , bg='purple' ,fg='pink')
scorelbl.pack()

scorelbl1=Label(win ,font= 'tahoma 12 bold' , bg='purple' ,fg='pink' )
scorelbl1.pack()

time=Label(win,text='Time'+ str(timeleft), font= 'tahoma 10 bold' , bg='purple')
time.pack()

label = Label(win , font=('comic sans ms',20))
label.pack()

e = Entry(win , width= 20)


win.bind('<Return>' , startgame)
e.pack()
e.focus_set()

win.mainloop()
