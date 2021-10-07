
# -*- coding: cp1252 -*-

##################################################################################################################
#
# SCRIPT PARA CRIAÇÃO DE CERTIFICADOS DE UMA LISTA
#
##################################################################################################################

# Para funcionar precisa do arquivo certificado.png na pasta

# Gera arquivos PDF e PNG.

##################################################################################################################

import string, os, shutil, cgi, sys, re, smtplib, time, PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# colocar aqui a largura e altura da imagem do certificado
W, H = (3508,2480)

nomes = []

newTxtList = []

directory1 = 'certificados-PDF'
directory2 = 'certificados-PNG'

txtFile = open ('nomes.txt')

txtList = txtFile.readlines () 

for row in txtList:

  linha = row

  linha = linha.replace ('\n', '')

  if linha == '':

    continue


  #linha = linha.upper ()

  #linha = linha.title ()

  # ajeita os nomes que o Title estraga, é um while ao invés de if pois pode ter mais de 1 no nome

  while ' Da ' in linha:

    linha = linha.replace (' Da ', ' da ')

  while ' De ' in linha:

    linha = linha.replace (' De ', ' de ')

  while ' Do ' in linha:

    linha = linha.replace (' Do ', ' do ')

  while ' Dos ' in linha:

    linha = linha.replace (' Dos ', ' dos ')

  while ' E ' in linha:

    linha = linha.replace (' E ', ' e ')



  #linha = linha.upper ()

  newTxtList.append (linha)


# cria diretório caso não exista
if not os.path.exists (directory1):

	os.mkdir (directory1)


if not os.path.exists (directory2):

	os.mkdir (directory2)


for i in newTxtList:

  j = i

  j = unicodeText = unicode (j, "utf-8")


  img = Image.open ("certificado.png")


  fontSize = 162
  y = 911


  if len (j) >= 42:

    fontSize = int (round (fontSize * 0.64))

    y = y + 37

  elif len (j) >= 33:

    fontSize = int (round (fontSize * 0.67))

    y = y + 36

  elif len (j) >= 26:

  	fontSize = int (round (fontSize * 0.80))

  	y = y + 19

  else:

    fontSize = int (round (fontSize * 0.95))

    y = y - 12




  # número no final é o tamanho
  font = ImageFont.truetype ("./FiraSans-Black.ttf", fontSize)

  #font = ImageFont.truetype ("./GreatVibes-Regular.otf", fontSize)

  draw = ImageDraw.Draw (img)

  w, h = draw.textsize (j, font)

  color = (255, 255, 255, 255) # (R, G, B, alpha)

  # (x, y), texto, cor, fonte
  draw.text (((W-w)/2, y), j, color, font)


  rgb = Image.new ('RGB', img.size, (255, 255, 255))  # white background
  
  rgb.paste (img, mask = img.split ()[3])             # paste using alpha channel as mask


  rgb.save (directory1 + '/Certificado ' + j + '.pdf', resolution = 300)
  

  newImg = img.resize ((1785, 1278), Image.ANTIALIAS)

  newRgb = Image.new ('RGB', newImg.size, (255, 255, 255))  # white background
  
  newRgb.paste (newImg, mask = newImg.split ()[3]) # cola o alpha channel como mascara


  newRgb.save (directory2 + '/Certificado ' + j + '.png', resolution = 300)

  print ('Criado Certificado - ' + j + '.pdf')

  

print ('')

