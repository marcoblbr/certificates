
# -*- coding: cp1252 -*-

##################################################################################################################
#
# SCRIPT TO CREATE CERTIFICATES FROM A LIST
#
##################################################################################################################

# To work, you need a file called certificate.png in the same folder

# It will generate PDFs and PNGs version of each name.

##################################################################################################################

import string, os, shutil, cgi, sys, re, smtplib, time, PIL

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

os.system ('clear')

# put here the exact width and height of the image from the file certificate.png
W, H = (3508,2480)

newTxtList = []

directory1 = 'certificates'

txtFile = open ('names.txt')

txtList = txtFile.readlines () 

for row in txtList:

  linha = row

  linha = linha.replace ('\n', '')

  if linha == '':

    continue


  #linha = linha.upper ()

  #linha = linha.title ()

  # fix the names Title funcion spoils, it's a while instead of the if because it can have more than 1 name

  # while ' Da ' in linha:

  #   linha = linha.replace (' Da ', ' da ')

  # while ' De ' in linha:

  #   linha = linha.replace (' De ', ' de ')

  # while ' Do ' in linha:

  #   linha = linha.replace (' Do ', ' do ')

  # while ' Dos ' in linha:

  #   linha = linha.replace (' Dos ', ' dos ')

  # while ' E ' in linha:

  #   linha = linha.replace (' E ', ' e ')



  #linha = linha.upper ()

  newTxtList.append (linha)


# create a folder if it doesn't exist
if not os.path.exists (directory1):

	os.mkdir (directory1)


for i in newTxtList:

  name = i

  name = unicodeText = unicode (name, "utf-8")

  # remove characters you don't want and sometimes are included in the string

  name = name.replace ('\n', '')
  name = name.replace ('\t', '')
  name = name.replace ('\\', '')
  name = name.replace ('\r', '')
  name = name.replace ('/',  '')

  img = Image.open ("certificate.png")


  fontSize = 162
  y = 981


  if len (name) >= 39:

    fontSize = int (round (fontSize * 0.60))

    y = y + 37

  elif len (name) >= 37:

    fontSize = int (round (fontSize * 0.64))

    y = y + 37

  elif len (name) >= 33:

    fontSize = int (round (fontSize * 0.67))

    y = y + 36

  elif len (name) >= 26:

  	fontSize = int (round (fontSize * 0.80))

  	y = y + 19

  else:

    fontSize = int (round (fontSize * 0.95))

    y = y - 12


  # USE FOR TEAM NAMES ONLY
  #fontSize = int (1.5 * fontSize)


  font = ImageFont.truetype ("./FiraSans-Black.ttf", fontSize)
  #font = ImageFont.truetype ("./GreatVibes-Regular.otf", fontSize)

  img = Image.open ('certificate.png')
  
  draw = ImageDraw.Draw (img)
    
  w, h = draw.textsize (name, font)

  white = (255,255,255)

  # needed if text is not centered on the screen

  # delta name of people, not centered on scren, 2022 model certificate

  deltaX = 393
  deltaY = -70

  # delta name of teams, centered on screen, 2021 model certificate

  # deltaX = 0
  # deltaY = 190

  fixedX = (W-w)/2 + deltaX
  fixedY = y       + deltaY

  draw.text ( (fixedX, fixedY), name, white, font = font)  # (x, y), text, color, font

  img.save (directory1 + '/' + name + '.pdf', resolution = 300)
  img.save (directory1 + '/' + name + '.png', resolution = 72)

  # img.show ()  # to test and see it on screen


  print ('Created Certificate - ' + name)
  

print ('')

