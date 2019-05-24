import random
p=print
f=False
from random import randrange
from tkinter import *
import math




#under
#work
#please wait gonna comp soon
def pokemon(n):
    score=0
    if n=="do you like pokemon":
        p("ya sir")
    if n=="see there is a pokemon":
        p("i am gonna try to catch it for you than")
    if n=="pokemon" or n=="pokemon game":
        p("if you want to play pokemon game say 'i want to play'")
        p("User : ",end="" )
        n=input()
        if n=="i want to play"or n=="bring it on" or n=="i want to play it":
            p("poke bot  : ",end="" )
            print("type 'help' or 'any tips' if you dont know how to play this game")
            m=True
            while m==True:
                p("User : ",end="" )
                n=input()
                if n=="help" or n=="how to quit" or n=="how to play this shit" or n=="any tips" or n=="i dont know how to play this game" or n=="how to play this game":
                    p("poke bot  : ",end="" )
                    p("this game is verry easy to play \nhere are some tips for you\n       1.just say 'i want to play','ok go ahead','thats gonna be fun' to start the game\n       2.after that sellect some pokeballs")
                    p("       3.a random pokemon gonna apear than\n       4.just say some magical words like 'catch app' or 'aim app' here app is that pokemon name")
                    p("\n       *keep that in mind that pokemon that gonna apear gonna have wrong spellings*")
                    p("\n       to quit say 'fuck off' or 'quit' or 'i am getting bored' or 'leave'")
                    p("User : ",end="" )
                    n=(input())
                    if n=="cool"or n=="awesome":
                        p("poke bot  : ",end="" )
                        p("you bet i am")
                if n=="ok i want to play it" or n=="i want to play" or n=="ok go ahead" or n=="thats gonna be fun":
                    p("poke bot  : ",end="" )
                    p("how many pokeball you want")
                    p("poke bot  : ",end="" )
                    p("select at least 10 pokeballs")
                    p("poke bot  : ",end="" )
                    p("enter 0 to quit")
                    ball=eval(input())
                    if(ball>10):
                        p("poke bot  : ",end="" )
                        p("now you have ",ball,"pokeballs")
                    else:
                        p("poke bot  : ",end="" )
                        p("select at least 10 next time")
                        p("       bye bye for now")
                        m==False
                if n=="how many balls i have now"or n=="no of balls" or n=="no of balls":
                        p(ball)
                if n=="quit" or n=="fuck off" or n=="i am getting bored" or n=="leave" or n==0:
                    m=False
                if n=="start the game" or n=="lemme guess" or n=='let me guess' or n=='gimme another' or n=='next pokemon' or n=="next" and ball>=10:
                    while m==True:
                        root=Tk()
                        root.title('Pokemon')
                        label=Label(root, text="Hope You gonna like it")
                        label.pack()
#############################################################  ADD NAMES OR ANY OTHER POKEMON GIFS U GT HERE ########################################
                        imgs=("jigglypuff.gif","pikachu.gif","squirtle.gif","celebi.gif","eevee.gif","mew.gif","mewtwo.gif","pichu.gif","togepi.gif")
#####################################################################################################################################################
                        a=random.choice(imgs)
                        poke=a

                        photo=PhotoImage(file=a)
                        labelphoto=Label(root,image=photo)
                        labelphoto.pack()

                        root.mainloop()
                        p("enter the name of pokemon u just see\nremember fr correct ans ur pokeball will not be used\nbut fr wrong ans one ball will be deducted")
                        p("\n\n*****I hope u know that pokemon*****\n\n")

                        guess=input()

                        if n=='quit' or n=='exit':
                            m==False

                        if guess+'.gif'==poke:
                            p("wow u guessed correct")
                            p("\nto see score type score")
                            score=score+1
                            p("\nur current score is ",score,'\n')
                            p('you have ',ball,'balls left\n')
                            p("type 'next' for next round")
                        else:
                            ball=ball-1
                            p('now u have ',ball,'balls left\n')
                            p("type 'next' for next round")









while f==False:
    n=input()
    if n=="pokemon":
        p("bot  : ",end="" )
        pokemon(n)


    
