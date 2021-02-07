#importing packages
import keyboard
import speech_recognition as speech
from tkinter import *
from tkinter import colorchooser
import pyttsx3
from PIL import Image, ImageTk
#starting the code
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

#helps choosing colour by picking it in tkinter
#color = colorchooser.askcolor()

engine.setProperty("rate",100)
def message():
    global first
    a = text.get()
    if "hi" in a:
        ans = Label(new, text="Hello, I am here to help you.")
        ans.pack()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def record():
    #when the key is pressed it will say that key name.
    speak("Record, mode is started.")
    while True:
        if keyboard.is_pressed("a"):
            speak("a")
        elif keyboard.is_pressed("b"):
            speak("b")
        elif keyboard.is_pressed("c"):
            speak("c")
        elif keyboard.is_pressed("d"):
            speak("d")
        elif keyboard.is_pressed("e"):
            speak("e")
        elif keyboard.is_pressed("f"):
            speak("f")
        elif keyboard.is_pressed("g"):
            speak("g")
        elif keyboard.is_pressed("h"):
            speak("h")
        elif keyboard.is_pressed("i"):
            speak("i")
        elif keyboard.is_pressed("j"):
            speak("j")
        elif keyboard.is_pressed("k"):
            speak("k")
        elif keyboard.is_pressed("l"):
            speak("l")
        elif keyboard.is_pressed("m"):
            speak("m")
        elif keyboard.is_pressed("n"):
            speak("n")
        elif keyboard.is_pressed("o"):
            speak("o")
        elif keyboard.is_pressed("p"):
            speak("p")
        elif keyboard.is_pressed("q"):
            speak("q")
        elif keyboard.is_pressed("r"):
            speak("r")
        elif keyboard.is_pressed("s"):
            speak("s")
        elif keyboard.is_pressed("t"):
            speak("t")
        elif keyboard.is_pressed("u"):
            speak("u")
        elif keyboard.is_pressed("v"):
            speak("v")
        elif keyboard.is_pressed("w"):
            speak("w")
        elif keyboard.is_pressed("x"):
            speak("x")
        elif keyboard.is_pressed("y"):
            speak("y")
        elif keyboard.is_pressed("z"):
            speak("Z")
        elif keyboard.is_pressed("ctrl"):
            speak("control")
        elif keyboard.is_pressed("backspace"):
            speak("backspace")
        elif keyboard.is_pressed("enter"):
            speak("enter")
        elif keyboard.is_pressed("esc"):
            speak("escape")
            speak("you are out of record, mode")
            return
        elif keyboard.is_pressed("shift"):
            speak("shift")
        elif keyboard.is_pressed("alt"):
            speak("alt")
        elif keyboard.is_pressed("spacebar"):
            speak("spacebar")
        elif keyboard.is_pressed("f1"):
            speak("f 1")
        elif keyboard.is_pressed("f2"):
            speak("f 2")
        elif keyboard.is_pressed("f3"):
            speak("f 3")
        elif keyboard.is_pressed("f4"):
            speak("f 4")
        elif keyboard.is_pressed("f5"):
            speak("f 5")
        elif keyboard.is_pressed("f6"):
            speak("f 6")
        elif keyboard.is_pressed("f7"):
            speak("f 7")
        elif keyboard.is_pressed("f8"):
            speak("f 8")
        elif keyboard.is_pressed("f9"):
            speak("f 9")
        elif keyboard.is_pressed("f10"):
            speak("f 10")
        elif keyboard.is_pressed("f11"):
            speak("f 11")
        elif keyboard.is_pressed("f12"):
            speak("f 12")
        elif keyboard.is_pressed("1"):
            speak("1")
        elif keyboard.is_pressed("2"):
            speak("2")
        elif keyboard.is_pressed("3"):
            speak("3")
        elif keyboard.is_pressed("4"):
            speak("4")
        elif keyboard.is_pressed("5"):
            speak("5")
        elif keyboard.is_pressed("6"):
            speak("6")
        elif keyboard.is_pressed("7"):
            speak("7")
        elif keyboard.is_pressed("8"):
            speak("8")
        elif keyboard.is_pressed("9"):
            speak("9")
        elif keyboard.is_pressed("0"):
            speak("0")
        elif keyboard.is_pressed("delete"):
            speak("delete")
        #elif keyboard.is_pressed("right arrow"):
            #speak("right arrow key")
        #elif keyboard.is_pressed("left arrow"):
            #speak("left arrow key")
        #elif keyboard.is_pressed("top"):
            #speak("top arrow key")
        #elif keyboard.is_pressed("bottom"):
            #speak("bottom arrow key")
def robot():
    global text
    global new
    #intializing tkinter module
    new = Tk()
    new.geometry("500x400")
    new.title("Help")
    text = Entry(new, font="times 12 bold",fg="white")
    text.place(x=160,y=350)
    send = Button(new, text="Send",command=message)
    send.place(x=240,y=350)
    new.mainloop()
def recognize():
    while True:
        #intializing the speech_recognition module
        sr = speech.Recognizer()
        try:
            speak("listening")
            with speech.Microphone() as micro:
                audio = sr.listen(micro)
                text = sr.recognize_google(audio,language='eng-in')
                print(text)
                speak(text)
                keyboard.write(text)
                if "gap" in text or "Gap" in text:
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("spacebar")
                elif "new line" in text or "New line" in text:
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("enter")
                elif "delete" in text or "Delete" in text:
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                elif "replace" in text or "Replace" in text:
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    speak("Opening replace")
                    keyboard.press("ctrl")
                    keyboard.press("h")
                    speak("replace is opened")
                elif "close" in text or "Close" in text:
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("alt")
                    keyboard.press("F4")
                elif "don't save" in text or "dont save" in text or "Dont save" in text or "Don't save" in text:
                    keyboard.press("right")
                    keyboard.press("enter")
                elif "save" in text or "Save" in text:
                    keyboard.press("enter")
                elif "cancel" in text or "Cancel" in text:
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("right")
                    keyboard.press("right")
                    keyboard.press("enter")
                elif "terminate" in text or "Terminate" in text:
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    keyboard.press("backspace")
                    speak("recognize mode is terminated now.")
                    return
        except Exception:
            speak("please speak again!")
def close():
    speak("closing")
    root.destroy()
def help():
    menubar.destroy()
    imglabel.destroy()
    record_mode.destroy()
    stop.destroy()
    listen.destroy()
    bot = Button(root, text="Talk with our bot for help.",bg="darkorange",fg="white",font="monospace 15 bold italic",command=robot)
    bot.place(x=170,y=230)
#intializing the tkinter module
root = Tk()
#intializing done
root.title("AUTOMATE-TYPER")
root.geometry("600x500")
root.resizable(width=False,height=False)
img = PhotoImage(file="logo.png")
imglabel = Label(image=img)
imglabel.pack()
record_mode = Button(root, text="Record_mode",font="monospace 12 bold italic",command = record, bg="coral", fg="white")
record_mode.pack()
stop = Button(root, text="Close",font="monospace 12 bold italic",command=close, bg="coral",fg="white")
stop.place(x=400,y=245,width=60,height=30)
listen = Button(root,text="Recognize",font="monospace 12 bold italic",command=recognize, bg="coral", fg="white")
listen.place(x=250,y=270)
#creating menu bar
menubar = Menu(root)
#configuring menu bar
root.config(menu=menubar)
#creating sub-menu's
submenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=submenu)
#adding elements to the submenu which are called drop down menu or cascading menu.
submenu.add_command(label="Need Help!",command=help)

root.mainloop()
