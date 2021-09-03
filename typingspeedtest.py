from tkinter import *
import random
import pygame

root = Tk()
pygame.mixer.init()
root.title("Typing speed test")
root.geometry("1200x900")
root.config(bg="black")

score=0
sec=61
def rese():
    global score
    global sec
    pygame.mixer.music.stop()
    sec=61
    score=0
    t.set("")
    no.config(text="")
    no.update()
    n.config(text="")
    n.update()
    enter.config(state="normal")
    wor.config(state="normal")
    st()


def timpo():
    global sco
    global score
    global sec
    sec-=1
    mlk.config(text=sec)
    if sec==0:
        t.set("")
        mlk.config(text="time up!!")
        sco.config(text="")
        pygame.mixer.music.load("maya.wav")
        pygame.mixer.music.play(loops=2)
        no.config(text="Your Speed is written below in\nWPM\n(WORDS PER MINUTE)")
        no.update()
        n.config(text=score)
        n.update()
        enter.config(state="disable")
        wor.config(state="disable")
    else:
        wor.after(1000, timpo)
def st():
    global sco
    global score
    but.destroy()
    global enter

    def ran():
        global sco
        global score
        global enter

        def bri():
            global sco
            global score
            vbn=enter.get()
            if ch in vbn:
                score+=1
                mat=score
                sco.config(text=mat)
                sco.update()
                t.set("")
                ran()
            else:
                wor.after(1,bri)

        mn = "hello", "font", "intel", "AMD", "honour"
        ch = ("".join(random.sample(mn, 1)))
        wor.config(text=ch)
        bri()

    ran()
    timpo()


mlk=Label(root,text="time left", font="arial 20 bold", bg="black", fg="red")
mlk.pack()
wor = Label(root, text="words will be displayed here", font="arial 60 bold", bg="black", fg="red")
wor.pack()

t = StringVar()
enter = Entry(root, textvar=t, font="arial 40 bold", bg="grey", fg="black", relief=SUNKEN, borderwidth=10)
enter.pack(pady=10)
but = Button(root, text="Start", font="arial 20 bold", bg="black", fg="red", command=st)
but.pack()
sco=Label(root,text="", font="arial 20 bold", bg="black", fg="red")
sco.pack(pady=20)
no=Label(root,text="", font="arial 40 bold", bg="black", fg="red")
no.pack()
n = Label(root, text="", font="arial 40 bold", bg="black", fg="red")
n.pack()
res=Button(root,text="RESET",  font="arial 30 bold", bg="black",fg="red",command=rese)
res.pack(pady=10)
qu=Button(root,text="QUIT", font="arial 30 bold", bg="black",fg="red",command=quit)
qu.pack()
root.mainloop()