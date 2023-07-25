from tkinter import *                                         #Importing all the Libraries
from tkinter import messagebox
from timeit import default_timer as timer
import random


root = Tk()                                                  #Initializing the Tkinter module
root.geometry("500x500")                                     #Geometry of Typing Test Window
root.configure(bg="Black")                                   #Background Colour to the window
root.title("TYPING SPEED TEST")                              #Title to the Window

window = Tk()                                                #Craeting Window
window.geometry("550x500")                                   #Geometry to the window
window.configure(bg='#37B26C')                               #Background colour to the window
window.withdraw()                                            #Window created has been hide
window.title("Test your ability!")                           #Title to the Window

file = open("Highscore.txt", "r+")
x = 0


def test():
    global x
    if x == 0:
        root.withdraw()
        x = x + 1
    window.deiconify()


def check_result():
    error: int
    j = error = 0
    result = entry.get('1.0', 'end-1c')
    end = timer()                           # WPM = [(No of characters typed/5)-errors]/time taken(in mins)
    time_taken = end - start
    if len(words[word]) >= len(result):
        error = len(words[word]) - len(result)
        for i in result:
            if i == words[word][j]:
                pass
            else:
                error = error + 1
            j = j + 1
    elif len(words[word]) <= len(result):
        error = len(result) - len(words[word])
        for i in words[word]:
            if i == result[j]:
                pass
            else:
                error = error + 1
            j = j + 1

    wpm = len(result) / 5
    wpm = wpm - error
    wpm = int(wpm/(time_taken/60))
    file.seek(0)
    line = int(file.readline())
    if wpm > line:
        file.seek(0)
        file.write(str(wpm))
        answer = "Amazing!!,Your High score is: " + str(wpm) + " WPM"
        messagebox.showinfo("Score", answer)
    else:
        answer = "Your score is: " + str(wpm) + " WPM"
        print("You can do better!!")
        messagebox.showinfo("Score", answer)


def finish():
    file.close()
    window.destroy()
    root.destroy()

def restart():
    b4.destroy()

words = ["Teena is an intelligent girl","Frank Edward McGurrin", "court stenographer from Salt Lake CityUtah", "who taught typing classes reportedly invented touch tyipn 1888.","Jack ia a very intelligent boy.He lives in Japan. He is the manager of a japanese company and has graduated as a software engineer."]        #Widgets
#words = ["Utah who taught typing classes, reportedly invented touch typing in 1888. On a standard keyboard for English speakers the home row keys are: ASDL for the left hand and JKL for the right hand. The ability to touch type on touchscreen phones has been made possible with the use of specialized virtual keyboard software for touch typing."]
word = random.randint(0, (len(words) - 1))

l3 = Label(window, text=words[word], bg='#014444', fg='#E2E5EB', height=7, width=47, wraplength=500,
           font="times 15")  # how many characters in a line - wrap-length
l3.place(x=15, y=10)

b2 = Button(window, text='Submit!', bg='#fc2828', fg='black', font='times 20', command=check_result)
b2.place(x=220, y=340)

entry = Text(window)                                       # Text=used for multiline text input
entry.place(x=100, y=180, height=150, width=350)

b3 = Button(window, text='DONE!', bg='white', fg='black', font='times 13', command=finish)
b3.place(x=210, y=420)

b4 = Button(window, text='Thank You!!', bg='white', fg='black', font='times 13', command=restart)
b4.place(x=290, y=420)

start = timer()

l1 = Label(root, text="Let's test your typing Speed!!", bg="Black", fg="White", font='times 20')
l1.place(x=100, y=50)

b1 = Button(root, text="Start!", width=10, bg="Pink", fg='Black', font='times 15', command=test)
b1.place(x=190, y=120)

l2 = Label(root, text="Highscore", width=10, bg="Yellow", fg="Black", font="times 25")
l2.place(x=160, y=190)


hs = int(file.readline())
hs_val = Label(root, text=str(hs) + " WPM", width=6, bg="Black", fg="#00C2D8", font="times 20")
hs_val.place(x=219, y=242)

root.mainloop()
window.mainloop()