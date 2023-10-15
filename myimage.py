import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import time
import os
import random
import math

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


def PrepareIMG(frame):
  global gambar1, gambar2, gambar3,gambar4,gambar5,gambar6,gambar7,gambar8,gambar9,gambar10,gambar11,gambar12,gambar13,gambar14,gambar15,gambar16,gambar17,gambar18,gambar19,gambar20
  
  Kaidou_Data = Image.open('Kaidou.png').convert('RGBA')
  Kaidou_Data = Kaidou_Data.resize((60,60), Image.ANTIALIAS)
  KaidouIMG = ImageTk.PhotoImage(Kaidou_Data)
  
  gambar1 = KaidouIMG
  
  Marshall_Data = Image.open('Marshall.png').convert('RGBA')
  Marshall_Data = Marshall_Data.resize((60,60), Image.ANTIALIAS)
  MarshallIMG = ImageTk.PhotoImage(Marshall_Data)
  
  gambar2 = MarshallIMG
  
  
  Monkey_Data = Image.open('Monkey.png').convert('RGBA')
  Monkey_Data = Monkey_Data.resize((60,60), Image.ANTIALIAS)
  MonkeyIMG = ImageTk.PhotoImage(Monkey_Data)
  
  gambar3 =  MonkeyIMG
  
  
  Nami_Data = Image.open('Nami.png').convert('RGBA')
  Nami_Data = Nami_Data.resize((60,60), Image.ANTIALIAS)
  NamiIMG = ImageTk.PhotoImage(Nami_Data)
  
  gambar4 = NamiIMG
  
  
  Blamenco_Data = Image.open('Blamenco.png').convert('RGBA')
  Blamenco_Data = Blamenco_Data.resize((60,60), Image.ANTIALIAS)
  BlamencoIMG = ImageTk.PhotoImage(Blamenco_Data)
  
  gambar5 = BlamencoIMG

  Blenheim_Data = Image.open('Blenheim.png').convert('RGBA')
  Blenheim_Data = Blenheim_Data.resize((60,60), Image.ANTIALIAS)
  BlenheimIMG = ImageTk.PhotoImage(Blenheim_Data)
  
  gambar6 = BlenheimIMG

  Charlotte_Data = Image.open('Charlotte.png').convert('RGBA')
  Charlotte_Data = Charlotte_Data.resize((60,60), Image.ANTIALIAS)
  CharlotteIMG = ImageTk.PhotoImage(Charlotte_Data)
  
  gambar7 = CharlotteIMG

  Curiel_Data = Image.open('Curiel.png').convert('RGBA')
  Curiel_Data = Curiel_Data.resize((60,60), Image.ANTIALIAS)
  CurielIMG = ImageTk.PhotoImage(Curiel_Data)

  
  gambar8 = CurielIMG

  Edward_Data = Image.open('Edward.png').convert('RGBA')
  Edward_Data = Edward_Data.resize((60,60), Image.ANTIALIAS)
  EdwardIMG = ImageTk.PhotoImage(Edward_Data)


  gambar9 = EdwardIMG

  Jozu_Data = Image.open('Jozu.png').convert('RGBA')
  Jozu_Data = Jozu_Data.resize((60,60), Image.ANTIALIAS)
  JozuIMG = ImageTk.PhotoImage(Jozu_Data)

  gambar10 = JozuIMG 

  Kozuki_Data = Image.open('Kozuki.png').convert('RGBA')
  Kozuki_Data = Kozuki_Data.resize((60,60), Image.ANTIALIAS)
  KozukiIMG = ImageTk.PhotoImage(Kozuki_Data)

  gambar11 = KozukiIMG

  Marco_Data = Image.open('Marco.png').convert('RGBA')
  Marco_Data = Marco_Data.resize((60,60), Image.ANTIALIAS)
  MarcoIMG = ImageTk.PhotoImage(Marco_Data)

  gambar12 = MarcoIMG

  Namur_Data = Image.open('Namur.png').convert('RGBA')
  Namur_Data = Namur_Data.resize((60,60), Image.ANTIALIAS)
  NamurIMG = ImageTk.PhotoImage(Namur_Data)


  gambar13 = NamurIMG

  Portgas_Data = Image.open('Portgas.png').convert('RGBA')
  Portgas_Data = Portgas_Data.resize((60,60), Image.ANTIALIAS)
  PortgasIMG = ImageTk.PhotoImage(Portgas_Data)

  gambar14 = PortgasIMG

  Rakuyo_Data = Image.open('Rakuyo.png').convert('RGBA')
  Rakuyo_Data = Rakuyo_Data.resize((60,60), Image.ANTIALIAS)
  RakuyoIMG = ImageTk.PhotoImage(Rakuyo_Data)


  gambar15 = RakuyoIMG 

  Roronoa_Data = Image.open('Roronoa.png').convert('RGBA')
  Roronoa_Data = Roronoa_Data.resize((60,60), Image.ANTIALIAS)
  RoronoaIMG = ImageTk.PhotoImage(Roronoa_Data)


  gambar16 = RoronoaIMG

  Sanji_Data = Image.open('Sanji.png').convert('RGBA')
  Sanji_Data = Sanji_Data.resize((60,60), Image.ANTIALIAS)
  SanjiIMG = ImageTk.PhotoImage(Sanji_Data)


  gambar17 = SanjiIMG

  Shanks_Data = Image.open('Shanks.png').convert('RGBA')
  Shanks_Data = Shanks_Data.resize((60,60), Image.ANTIALIAS)
  ShanksIMG = ImageTk.PhotoImage(Shanks_Data)


  gambar18 = ShanksIMG

  Thatch_Data = Image.open('Thatch.png').convert('RGBA')
  Thatch_Data = Thatch_Data.resize((60,60), Image.ANTIALIAS)
  ThatchIMG = ImageTk.PhotoImage(Thatch_Data)


  gambar19 = ThatchIMG

  Usopp_Data = Image.open('Usopp.png').convert('RGBA')
  Usopp_Data = Usopp_Data.resize((60,60), Image.ANTIALIAS)
  UsoppIMG = ImageTk.PhotoImage(Usopp_Data)

  gambar20 = UsoppIMG