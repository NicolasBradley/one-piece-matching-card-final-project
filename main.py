import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import time
import os
import random
import math
import myimage
from functools import partial



# pics = ['🍸','🌟','🍺','🍟','🍔','✌','🎵','🎸','🚗','⚽','🎁','🎂','🏀','☕','🔥','❄','☔','💍','⌚','❤','🎈','🎹','🎻','🎷','🎺','🎶','♫','⛵','🚴','🌙','🌠']

# pics = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

win = 0
score = 0
global tries
tries = 0
name =''

if not os.path.exists('winscoreboard.txt'):
  f = open('winscoreboard.txt','x')

if not os.path.exists('scorescoreboard.txt'):
  f = open('scorescoreboard.txt','x')
  
if not os.path.exists('tempo.txt'):
  f = open('tempo.txt','x')
  
# pics = [myimage.gambar1,myimage.gambar2,myimage.gambar3,myimage.gambar4,myimage.gambar5,myimage.gambar6,myimage.gambar7,myimage.gambar8,myimage.gambar9,myimage.gambar10,myimage.gambar11,myimage.gambar12,myimage.gambar13,myimage.gambar14,myimage.gambar15,myimage.gambar16,myimage.gambar17,myimage.gambar18,myimage.gambar19,myimage.gambar20]
gambar1 = ""
gambar2 = ""
gambar3 = ""
gambar4 = ''
gambar5 = ''
gambar6 = ""
gambar7 = ""
gambar8 = ""
gambar9 = ''
gambar10 = ''
gambar11 = ""
gambar12 = ""
gambar13 = ""
gambar14 = ''
gambar15 = ''
gambar16 = ""
gambar17 = ""
gambar18 = ""
gambar19 = ''
gambar20 = ''

pics = [gambar1,gambar2,gambar3,gambar4,gambar5,gambar6,gambar7,gambar8,gambar9,gambar10,gambar11,gambar12,gambar13,gambar14,gambar15,gambar16,gambar17,gambar18,gambar19,gambar20]




window = tk.Tk()
window.title("Matching Card Game")
window.geometry("700x600")
window.configure(bg="#5edfff")



def showframe(e):
  e.tkraise()
  resetplay()


entrymenu = tk.Frame(window,bg="#5edfff")
mainmenu = tk.Frame(window,bg="#5edfff")
difficulty = tk.Frame(window,bg="#5edfff")
scoreframe= tk.Frame(window, bg="#5edfff")
easy = tk.Frame(window, bg="#5edfff")
medium = tk.Frame(window, bg="#5edfff")
hard = tk.Frame(window, bg="#5edfff")
EXTREME = tk.Frame(window, bg="#5edfff")
winframe= tk.Frame(window, bg="#5edfff")
infoframe= tk.Frame(window, bg="#5edfff")
dummyframe = tk.Frame(window, bg="#5edfff")
loseframe = tk.Frame(window, bg="#5edfff")

list = [entrymenu,mainmenu, difficulty, scoreframe,easy,medium,hard,EXTREME,winframe,infoframe, loseframe, dummyframe]


for i in range(len(list)):
  list[i].grid(row = 0, column =0, sticky = 'nesw')




  
#entry menu===========================================

  #for scoreboard
# def checkscoreboard(name)
#   if 


GAME1_Data = Image.open('GAME.png').convert('RGBA')
GAME1_Data = GAME1_Data.resize((300,300), Image.ANTIALIAS)
GAME1IMG = ImageTk.PhotoImage(GAME1_Data)

GAME1_label = Label(entrymenu)
GAME1_label['image'] = GAME1IMG

LabelSpasi = tk.Label(entrymenu, text="" ,bg="#5edfff", width = 22)
LabelSpasi.grid(column = 0, row = 0, columnspan = 5 )

GAME1_label.grid(column=5,row = 0, columnspan = 10, sticky = 'n')

maindisplay = tk.Entry(entrymenu, width = 25, font =('Arial',14), justify = 'right')
maindisplay.grid( column = 8, row = 7, columnspan = 4)
  
Labelstart = tk.Label(entrymenu, text="Welcome! Please enter name :",bg="#5edfff")
Labelstart.grid(column=7,row = 6, columnspan = 10,padx = 4, pady = 4)

def check(lasttext):
  global name
  if lasttext != '' and lasttext != 'ERROR please enter name':
    name = maindisplay.get()
    # scoreboardlabel = tk.Label(scoreframe, text =f'{name}: wins = {win}, score ={score}', bg="#5edfff")
    # scoreboardlabel.grid(column = 2, row = 0, sticky ='ne')
    # playerdata =f'{name}: wins = {win}, score ={score}'

    Labeltitleinfo= tk.Label(infoframe, text=f"\nHello {name}!" ,font = ('Arial',16), bg="#5edfff", width = 22)
    Labeltitleinfo.grid(column = 5, row = 1, columnspan = 5 )
    
    showframe(mainmenu)
  elif lasttext == '':
    maindisplay.insert(0,'ERROR please enter name')
  elif lasttext =='ERROR please enter name':
    maindisplay.delete(0, END)
    


enterbutton = tk.Button(entrymenu, text = 'Enter',bg="#1bf786", width = 6, command =lambda : check(maindisplay.get()))

enterbutton.grid( column = 8, row = 8, columnspan = 4, pady= 5,padx=5)

#main menu===========================================

GAME_Data = Image.open('GAME.png').convert('RGBA')
GAME_Data = GAME_Data.resize((250,250), Image.ANTIALIAS)
GAMEIMG = ImageTk.PhotoImage(GAME_Data)

GAME_label = Label(mainmenu)
GAME_label['image'] = GAMEIMG

playbtn = tk.Button(mainmenu, text = 'Play',bg="#1bf786",width = 6, command =lambda : showframe(difficulty))
playbtn.grid( column = 8, row = 8, columnspan = 4,  padx = 5, pady = 5)


scorebtn = tk.Button(mainmenu, text = 'Score',bg="#1bf786",width = 6,  command =lambda : scorefunc(scoreframe))
scorebtn.grid( column = 8, row = 9, columnspan = 4,  padx = 5,  pady = 5)



infobtn = tk.Button(mainmenu, text = 'More info',bg="#1bf786",width = 6,  command =lambda : showframe(infoframe))
infobtn.grid( column = 8, row = 10, columnspan = 4,  padx = 5, pady = 5)


GAME_label.grid(column=5,row = 0, columnspan = 10, sticky = 'n')

LabelSpasi = tk.Label(mainmenu, text="" ,bg="#5edfff", width = 22)
LabelSpasi.grid(column = 0, row = 0, columnspan = 5 )


#Play/difficulty ================================================

goodluck_Data = Image.open('goodluck.png').convert('RGBA')
goodluck_Data = goodluck_Data.resize((200,200), Image.ANTIALIAS)
goodluckIMG = ImageTk.PhotoImage(goodluck_Data)

goodluck_label = Label(difficulty)
goodluck_label['image'] = goodluckIMG

goodluck_label.grid(column=5,row = 0, columnspan = 10, sticky = 'n')

LabelSpasi = tk.Label(difficulty, text="" ,bg="#5edfff", width = 22)
LabelSpasi.grid(column = 0, row = 0, columnspan = 5 )

Labeltitle = tk.Label(difficulty, text="Choose difficulty :",bg="#5edfff")
Labeltitle.grid(column = 5, row = 1, columnspan = 10)

easybtn = tk.Button(difficulty, text = 'Easy',bg="#1bf786",width = 6, command =lambda : modenview(1))

easybtn.grid( column = 8, row = 8, columnspan = 4,  padx = 5, pady = 5)

mediumbtn = tk.Button(difficulty, text = 'Medium',bg="#1bf786",width = 6, command =lambda : modenview(2))

mediumbtn.grid( column = 8, row = 9, columnspan = 4,  padx = 5,  pady = 5)

hardbtn = tk.Button(difficulty, text = 'Hard',bg="#1bf786",width = 6, command =lambda : modenview(3))
hardbtn.grid( column = 8, row = 10, columnspan = 4,  padx = 5, pady = 5)

extremebtn = tk.Button(difficulty, text = 'EXTREME',bg="#1bf786",width = 6, command =lambda : modenview(5))
extremebtn.grid( column = 8, row = 11, columnspan = 4,  padx = 5, pady = 5)



back = tk.Button(difficulty, text = 'Back', width = 12, command=lambda: showframe(mainmenu), bg = '#ff3333')
back.grid( column = 8, row = 12, columnspan = 4,  padx = 5, pady = 5)


exit = tk.Button(easy, text = 'Exit', width = 12, command=lambda: showframe(difficulty), bg = '#ff3333')
exit.grid( column = 7, row = 12, columnspan = 4,  padx = 5, pady = 5)

exit = tk.Button(medium, text = 'Exit', width = 12, command=lambda: showframe(difficulty), bg = '#ff3333')
exit.grid( column = 7, row = 12, columnspan = 4,  padx = 5, pady = 5)

exit = tk.Button(hard, text = 'Exit', width = 12, command=lambda: showframe(difficulty), bg = '#ff3333')
exit.grid( column = 7, row = 12, columnspan = 4,  padx = 5, pady = 5)

exit = tk.Button(EXTREME, text = 'Exit', width = 12, command=lambda: showframe(difficulty), bg = '#ff3333')
exit.grid( column = 10, row = 12, columnspan = 4,  padx = 5, pady = 5)


#play system*******************************************************


scorelist = []

#question Img
question_Data = Image.open('question.png').convert('RGBA')
question_Data = question_Data.resize((60,60), Image.ANTIALIAS)
questionIMG = ImageTk.PhotoImage(question_Data)


def modenview(k):
  global blind, z,p,kk, tries, pics, score, scorelist

  tries = 10*k
  score = tries*10
  
  
  pics = ['gambar1','gambar2','gambar3','gambar4','gambar5','gambar6','gambar7','gambar8','gambar9','gambar10','gambar11','gambar12','gambar13','gambar14','gambar15','gambar16','gambar17','gambar18','gambar19','gambar20']
  
  # gambar
  x = random.sample(pics, k=4*k)
  y = x
  z = x+y
  random.shuffle(z)

  
  #easy
  LabelSpasi = tk.Label(easy, text="" ,bg="#5edfff", width = 22)
  LabelSpasi.grid(column = 0, row = 0, columnspan = 5 )
  
  trieslabel = tk.Label(easy, text = f'Your number of tries :{tries}', bg="#5edfff")
  trieslabel.grid(column = 0, row = 0)
  
  #medium
  LabelSpasi = tk.Label(medium, text="" ,bg="#5edfff", width = 22)
  LabelSpasi.grid(column = 0, row = 0, columnspan = 5 )
  
  trieslabel = tk.Label(medium, text = f'Your number of tries :{tries}', bg="#5edfff")
  trieslabel.grid(column = 0, row = 0)
  
  #hard 
  LabelSpasi = tk.Label(hard, text="" ,bg="#5edfff", width = 22)
  LabelSpasi.grid(column = 0, row = 0, columnspan = 5 )
  
  trieslabel = tk.Label(hard, text = f'Your number of tries :{tries}', bg="#5edfff")
  trieslabel.grid(column = 0, row = 0)
  
  #Extreme
  LabelSpasi = tk.Label(EXTREME, text="" ,bg="#5edfff", width = 22)
  LabelSpasi.grid(column = 0, row = 0, columnspan = 5 )
  
  trieslabel = tk.Label(EXTREME, text = f'Your number of tries :{tries}', bg="#5edfff")
  trieslabel.grid(column = 0, row = 0)

  
  if k == 1:
      myimage.PrepareIMG(easy)
      generatebutton(k)
      showframe(easy)
      
  elif k == 2:
    myimage.PrepareIMG(medium)
    generatebutton(k)
    showframe(medium)
  elif k == 3:
    myimage.PrepareIMG(hard)
    generatebutton(k)
    showframe(hard)
  elif k == 5:
    myimage.PrepareIMG(EXTREME)
    generatebutton(k)
    showframe(EXTREME)

      
#v3
button ='button'
numberofbuttons = 0
def generatebutton(f):
  global mode, blind, rows, columns, button
  
  if f == 1:
    mode = easy
  elif f == 2:
    mode = medium
  elif f == 3:
    mode = hard
  elif f == 5:
    mode = EXTREME
  
  rows = f*2
  columns = 4
  
  numberofbuttons = 0
  blind = []

  rrrow = 0
  cccolumn = 0
  for i in range(0, rows*columns):
  
    
    button = (f'{button}{numberofbuttons}')
    
    button = tk.Button(mode, image = questionIMG ,bg = '#fff833', command= partial(change, i))
    blind.append(button)
    button.grid(row=rrrow+5 , column=cccolumn+5 , padx = 2 ,pady = 2)
    if cccolumn == 3:
      cccolumn = 0
      rrrow+=1
    else:
      cccolumn +=1
    numberofbuttons+=1


compare_image = []
original = []
countercheck = []
numcards=0
lastisMatched=True #Tambahan Mr Andreas
def change(n):
  global blind, z, answer_img, tries, compare_image, original, mode, numcards, win, score, yolo, countercheck, lastisMatched #Tambahan Mr Andreas
  # Ditambahkan MR Andreas untuk jeda gambar yang tidak match
  if not lastisMatched:
    trieslabel = tk.Label(mode, text = f'Your number of tries :{tries}', bg="#5edfff")
    trieslabel.grid(column = 0, row = 0)
    original[0].configure(image = questionIMG)
    original[1].configure(image = questionIMG)
    compare_image.clear()
    original.clear()
  # END Ditambahkan MR Andreas untuk jeda gambar yang tidak match
  if z[n] in countercheck:
    print('card already opened1')
    # Ditambahkan MR Andreas untuk yang gambar bandel
    countercheck.remove(z[n])
    blind[n].configure(image = questionIMG )
    compare_image.clear()
    original.clear()
    # END Ditambahkan MR Andreas untuk yang gambar bandel
    # time.sleep(1)
    # if not len(compare_image) == 2:
    #   bname.configure(image = questionIMG )
    # compare_image.clear()
  else:
    answer_img = eval(f'myimage.{z[n]}')
    bname = (blind[n])

    if bname == answer_img:
      print('card already opened2')
      # time.sleep(1)
      # if not len(compare_image) == 2:
      #   bname.configure(image = questionIMG )
      # compare_image.clear()
    else:
      compare_image.append(z[n])
      original.append(bname)
      bname.configure(image = answer_img )
      play()

 
def play():
  global blind, z, answer_img, tries, compare_image, original, mode, numcards, win,score, winstats,n, bname, lastisMatched #Tambahan Mr Andreas
  lastisMatched = True
  if len(compare_image) == 2:
    if compare_image[0] == compare_image[1]:
      numcards+=1
      countercheck.append(compare_image[0])
      countercheck.append(compare_image[1])
      compare_image.clear()
      original.clear()

      
      if numcards == (len(blind)/2):
        showframe(winframe)
        win+=1
        score = tries*10
        winstats = tk.Label(winframe, text = f'Wins + 1, Your Score :{score}',bg="#5edfff", font =('Arial',15))
        winstats.grid(column = 5, row = 2, columnspan = 5 )
  
        numcards=0
        compare_image.clear()
        original.clear()
      
      
    else:
      
      tries -= 1
      if tries <= 0:
        numcards=0
        showframe(loseframe)
        compare_image.clear()
        original.clear()
      else:
        # Ditambahkan MR Andreas untuk jeda gambar yang tidak match
        lastisMatched = False
        # END Ditambahkan MR Andreas untuk jeda gambar yang tidak match
        
  # elif len(compare_image) == 1:
  #   if bname == answer_img:
  #     print('card already opened')
  #     compare_image.clear()
  #   else:
  #     compare_image.append(z[n])
  #     original.append(bname)
  #     bname.configure(image = answer_img )
     
    
    

def resetplay():
  global blind, z, answer, tries, compare_image, original, mode, numcards, lastisMatched , win,score, countercheck
  # print(win)
  # print(score)
  lastisMatched=True
  countercheck.clear()
  numcards = 0
  compare_image.clear()
  original.clear()



#Scoreframe=======================================================

leaderboard_Data = Image.open('leaderboard.png').convert('RGBA')
leaderboard_Data = leaderboard_Data.resize((210,210), Image.ANTIALIAS)
leaderboardIMG = ImageTk.PhotoImage(leaderboard_Data)

scoreboardtitle = tk.Label(scoreframe, text =f'|Win Leader Board|', bg="#5edfff",font =('Arial',14))
scoreboardtitle.grid(column = 0, row = 1, sticky ='nw')

scorescoreboardtitle = tk.Label(scoreframe, text =f'|Score Leader Board|', bg="#5edfff",font =('Arial',14))
scorescoreboardtitle.grid(column = 1, row = 1, sticky ='nw')


def scorefunc(u):
  global totalscore, winscoreorder, sortedData

  # winscoreorder = []

  # if len(scorelist) != 0 and win != 0:
  #   if len(scorelist) == 1:
  #      f = open('tempo.txt','w')
  #      f.write(f'{[str(name),win,score]}')
  #      f.close
  #   elif len(scorelist) >= 1:
  #     print(scorelist)
  #     f = open('tempo.txt','w')
  #     f.write(f'{[str(name),win,sum(scorelist)]}')
  #     f.close

  # f = open('tempo.txt','r')
  # winscoreorder.append(f.read())
  # f.close


  # with open("winscoreboard.txt") as f:
  #   for line in f:
  #       winscoreorder.append(line.strip())
  # print(winscoreorder)
  
  # # f = open('tempo.txt','r')
  # scoreboardlabel = tk.Label(scoreframe, text =f'{winscoreorder[0][0]}', bg="#5edfff")
  # scoreboardlabel.grid(column = 1, row = 1, sticky ='ne')
  # # f.close
  # LabelSpasi = tk.Label(scoreframe, text="" ,bg="#5edfff", width = 2)
  # LabelSpasi.grid(column = 0, row = 0 )
  score = sum(scorelist)

  
  # with open("winscoreboard.txt", "r") as f:
  #   lines = f.readlines()
  # with open("winscoreboard.txt", "w") as f:
  #   for line in lines:
  #       if line.strip("\n") == 'gojodas':
  #           f.write(line)

#wins-----
  
  f = open('winscoreboard.txt','a')
  f.write(str(win)+','+name+'\n')
  f.close()

  f = open('winscoreboard.txt','r')
  readthefile = f.readlines()
  sortedData = sorted(readthefile, reverse=True)

  for i in range(5):
    winscoreboardlabel = tk.Label(scoreframe, text 
    =f'{str(i+1)}. wins = {str(sortedData[i])}', bg="#5edfff")
    winscoreboardlabel.grid(column = 0, row = i+2, sticky = 'nw')

  #score--------
  
  f = open('scorescoreboard.txt','a')
  f.write(str(score)+','+name+'\n')
  f.close()

  f = open('scorescoreboard.txt','r')
  readthefile = f.readlines()
  sortedData = sorted(readthefile, reverse=True)

  for i in range(5):
    scorescoreboardlabel = tk.Label(scoreframe, text 
    =f'|{str(i+1)}. Score = {str(sortedData[i])}', bg="#5edfff")
    scorescoreboardlabel.grid(column = 1, row = i+2, sticky = 'nw')


  
  showframe(u)
  
  leaderboard_label = Label(scoreframe)
  leaderboard_label['image'] = leaderboardIMG
  
  leaderboard_label.grid(column = 0, row = 0)
  
  back = tk.Button(scoreframe, text = 'Back', width = 12, command=lambda: showframe(mainmenu), bg = '#ff3333')
  back.grid( column = 8, row = 12, columnspan = 4,  padx = 5, pady = 5)

#Info frame=======================================================


infoframeimg_Data = Image.open('infoframeimg.png').convert('RGBA')
infoframeimg_Data = infoframeimg_Data.resize((200,200), Image.ANTIALIAS)
infoframeimgIMG = ImageTk.PhotoImage(infoframeimg_Data)

infoframeimg_label = Label(infoframe)
infoframeimg_label['image'] = infoframeimgIMG

infoframeimg_label.grid(column=5,row = 0, columnspan = 10, sticky = 'n')

LabelSpasi = tk.Label(infoframe, text="" ,bg="#5edfff", width = 5)
LabelSpasi.grid(column = 0, row = 0, columnspan = 5 )

tkLabelinfo= tk.Label(infoframe, text=f"-In this game,\nyou have to match all the pairs of cards from the blind random cards.\n\n-You can see wins and score at\n 'score section'\nTo get scores you need to get the least amount of tries in a level.\n\n-That is all thankyou! Have fun! (Version 1.2)" ,font = ('Arial',12), bg="#5edfff", width = 57)
tkLabelinfo.grid(column = 5, row = 2, columnspan = 5 )


back = tk.Button(infoframe, text = 'Back', width = 12, command=lambda: showframe(mainmenu), bg = '#ff3333')
back.grid( column = 8, row = 12, columnspan = 4,  padx = 5, pady = 5)


#winframe==========================================================================

LabelSpasi = tk.Label(winframe, text="" ,bg="#5edfff", width = 22)
LabelSpasi.grid(column = 0, row = 0, columnspan = 2 )

winlabel = tk.Label(winframe, text = f'CONGRATULATIONS {name}! YOU WON!',bg="#5edfff")
winlabel.grid(column = 5, row = 1, columnspan = 5,  padx = 2, pady = 5)




winbttn = tk.Button(winframe, text = 'Claim Rewards', width = 15, command=lambda: showframe(mainmenu), bg = '#fff833')
winbttn.grid( column = 6, row = 12, columnspan = 3,  padx = 2, pady = 5)

winimg_Data = Image.open('winimg.png').convert('RGBA')
winimg_Data = winimg_Data.resize((300,300), Image.ANTIALIAS)
winimgIMG = ImageTk.PhotoImage(winimg_Data)

winimg_label = Label(winframe)
winimg_label['image'] = winimgIMG

winimg_label.grid(column=5,row = 0, columnspan = 5, sticky = 'n')


#loseframe=========================================================================

LabelSpasi = tk.Label(loseframe, text="" ,bg="#5edfff", width = 22)
LabelSpasi.grid(column = 0, row = 0, columnspan = 2 )

loselabel = tk.Label(loseframe, text = f'CONGRATULATIONS {name}! YOU LOST!',bg="#5edfff")
loselabel.grid(column = 5, row = 1, columnspan = 5,  padx = 2, pady = 5)

losebttn = tk.Button(loseframe, text = 'Return to Lobby', width = 15, command=lambda: showframe(mainmenu), bg = '#fff833')
losebttn.grid( column = 6, row = 12, columnspan = 3,  padx = 2, pady = 5)

loseimg_Data = Image.open('loseimg.png').convert('RGBA')
loseimg_Data = loseimg_Data.resize((300,300), Image.ANTIALIAS)
loseimgIMG = ImageTk.PhotoImage(loseimg_Data)

loseimg_label = Label(loseframe)
loseimg_label['image'] = loseimgIMG

loseimg_label.grid(column=5,row = 0, columnspan = 5, sticky = 'n')


#------------------------------------------------------

showframe(entrymenu)


tk.mainloop()

#sources: https://stackoverflow.com/questions/39447138/how-can-i-identify-buttons-created-in-a-loop 
#https://www.techrepublic.com/article/partial-function-application-in-python/
#https://towardsdatascience.com/introducing-pythons-functools-module-2c4cba4774e#:~:text=The%20functools%20module%2C%20part%20of,another%20function%20as%20an%20argument%20).
#https://github.com/iamcodefoxx/Switch-Frames-Template/blob/master/switch_frames_template.py
#https://www.tutorialspoint.com/how-to-use-an-image-as-a-button-in-tkinter
#https://www.tutorialspoint.com/how-to-clear-out-a-frame-in-the-tkinter#:~:text=If%20we%20want%20to%20clear,the%20frame%20using%20winfo_children().
#https://docs.replit.com/tutorials/managing-files-using-repl-it
#https://stackoverflow.com/questions/23584325/cannot-use-geometry-manager-pack-inside
#httphttps://www.geeksforgeeks.org/python-tkinter-scrollbar/?ref=lbps://www.geeksforgeeks.org/python-tkinter-scrollbar/?ref=lbp

#https://stackhowto.com/how-to-change-text-of-button-when-clicked-in-tkinter-python/
#https://stackoverflow.com/questions/43731784/tkinter-canvas-scrollbar-with-grid
#https://www.youtube.com/watch?v=HRJRq2r7eL8&ab_channel=MrSuffar