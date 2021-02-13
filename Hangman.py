#Dawin Ye
#HW4 Hangman
# I was able to create the game with all the parts necessary, the play again button works and it limits it to one letter per entry

from tkinter import *
import random
def getword():
    global answer
    f = open("f.txt","r")
    mylines = f.readlines()
    answer = mylines[random.randint(0,9904)]
    answer = answer.strip()
    f.close()
game = None
currentLetter = ""
new = ""
guessesleft=6
s = ""
letter = None
def post():
    myCanvas.create_line(200, 200, 200, 550)
    myCanvas.create_line(200, 200, 400, 200)
    myCanvas.create_line(400, 200, 400, 250)
def restart():
    global myCanvas, new, guessesleft, wrong, s, blanks, myText, playagain
##    blanks = []
##    myCanvas.delete("all")
##    getword()
##    post()
##    congrats.set("")
##    new=""
##    print(answer)
##    guessesleft = 6
##    s=""
##    a = ""
##    for x in answer:
##        s = s + "_ "
##    thing.set(new)
##    myText.set(s)
##    wrong = 0
##    letterstried.clear()
##    guesses.set(guessesleft)
    game.destroy()
    game1()
def gettingLetter(event):
    global blanks, s, thing, new, letterstried, guesses,vary, congrats, currentLetter, letter, answer, hidden_word, word, blanks, wrong, wincondition
    guessedright = False
    wincondition = False
    currentLetter = letter.get()
        
    letter.delete(0, END)
    if len(currentLetter) == 1:
        for index,correctletter in enumerate(word):
            if currentLetter == correctletter:
                letterstried.append(currentLetter)
                for x in letterstried:
                    new += x
                blanks[index] = currentLetter
                guessedright = True
        if guessedright == False:
            letterstried.append(currentLetter)
            for x in letterstried:
                new += x
            wrong+=1
            guesses.set(6-wrong)
            check(wrong)
        thing.set(new)
        letterstried.clear()
        temp = "_"
        if temp not in blanks:
            congrats.set("YOU WON!")
            new = ""
        update(blanks)
    else:
        print("Enter one letter only please")
##    if guessedright == False:
##        letterstried.append(currentLetter)
##        for x in letterstried:
##            new += x
##        wrong+=1
##        guesses.set(6-wrong)
##        check(wrong)
##    thing.set(new)
##    letterstried.clear()
##    temp = "_"
##    if temp not in blanks:
##        congrats.set("YOU WON!")
##        new = ""
##    update(blanks)
def update(blanks):            
    global myText
    myText.set(blanks)
def game1():
    global playagain, game, blanks,s, myCanvas, thing, letterstried, vary2, guesses, f, myText, congrats, myCanvas, currentLetter, letter, answer, hidden_word, word, blanks, wrong, wincondition
    getword()
    game = Tk()
    game.title("Hangman")
    word = list(answer)
    blanks = ["_"]*len(word)
    letterstried = []
    s=""
    a= ""
    for x in answer:
        s = s + "_ "
    congrats = StringVar()
    congrats.set("")
    congrats2 = Label(game, textvariable=congrats)
    congrats2.pack()
    wrong = 0
    myText = StringVar()
    myText.set(s)
    hidden_word = Label(game, textvariable=myText)
    letterguessing = Label(game, text = "Enter a letter")
    letterguessing.pack()
    letter = Entry(game)
    game.bind("<Return>", gettingLetter)
    letter.pack()
    hidden_word.pack()
    tries = Label(game, text = "You have")
    tries.pack()
    guessesleft = 6
    guesses = StringVar()
    guesses.set(guessesleft)
    guessesremaining = Label(game, textvariable=guesses)
    guessesremaining.pack()
    stuff = Label(game, text = "guesses remaining")
    stuff.pack()
    triedletters = Label(game, text= "Letters tried:")
    triedletters.pack()
    thing = StringVar()
    new = ""
    thing.set(new)
    material = Label(game, textvariable = thing)
    material.pack()
    myCanvas = Canvas(game, width=800, height=800)
    post()
    playagain = Button(game,text="Play Again",command=restart)
    playagain.pack()
    myCanvas.pack()
    game.mainloop()
def check(wrong):
    global f, vary, vary2
    if wrong == 1:
        post()
        myCanvas.create_oval(360, 250, 440, 330)
    elif wrong == 2:
        post()
        myCanvas.create_oval(360, 250, 440, 330)
        myCanvas.create_line(400, 450, 400, 330)
    elif wrong == 3:
        post()
        myCanvas.create_oval(360, 250, 440, 330)
        myCanvas.create_line(400, 450, 400, 330)
        myCanvas.create_line(400, 360, 365, 410)
        
    elif wrong == 4:
        post()
        myCanvas.create_oval(360, 250, 440, 330)
        myCanvas.create_line(400, 450, 400, 330)
        myCanvas.create_line(400, 360, 365, 410)
        myCanvas.create_line(400, 360, 435, 410)

    elif wrong == 5:
        post()
        myCanvas.create_oval(360, 250, 440, 330)
        myCanvas.create_line(400, 450, 400, 330)
        myCanvas.create_line(400, 360, 365, 410)
        myCanvas.create_line(400, 360, 435, 410)
        myCanvas.create_line(400, 450, 365, 500)
    else:
        post()
        myCanvas.create_oval(360, 250, 440, 330)
        myCanvas.create_line(400, 450, 400, 330)
        myCanvas.create_line(400, 360, 365, 410)
        myCanvas.create_line(400, 360, 435, 410)
        myCanvas.create_line(400, 450, 365, 500)
        myCanvas.create_line(435, 500, 400, 450)
        congrats.set("Sorry, you lost")
        letterguessing.set(answer)
        new = ""
game1()
