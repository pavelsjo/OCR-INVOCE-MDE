from wand.image import Image as Img #convierte un pdf en una imagenes
from PIL import Image #se utiliza para manipular las imagenes generadas
import pytesseract # lector OCR
import json #exportamos nuestra información en un json
import re


#Define la ruta donde esta installado el tesseract
PATH_TESSERACT = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 
pytesseract.pytesseract.tesseract_cmd = PATH_TESSERACT


#1.Covertimos el pdf a una imagen. Este paso es para simular el caso real donde los pdf vienen de una imagen.
PATH_PDF = r'./pdf/factura_001.pdf'
PATH_JPG = r'./img/factura_001.jpg'
with Img(filename=PATH_PDF, resolution=300) as img:
    img.compression_quality = 99
    img
    img.save(filename=PATH_JPG)

    
#2.Extraemos el texto de la factura con el Tesseract
PATH_TXT = r'./txt/factura_001.txt'
text = pytesseract.image_to_string(Image.open(PATH_JPG))
f = open (PATH_TXT,'w') #archivo-salida.py
f.write(text)
f.close()


#3.Extraemos los datos y los integramos en un diccionario
dic_extracted = {'INVOICE' : re.findall(r'INVOICE No.: (\d+)', text),
                 'DATE' : re.findall(r'INV.: (\d+[/]\d+[/]\d+)', text),
                 'TOTAL DUE' : re.findall(r'TOTAL DUE: (\d+[.,]\d+[.,]\d+)', text)}

#4. Exportamos
PATH_JSON = r'./txt/factura_001.json'
with open('./2_json_files/factura_001.json', 'w') as json_file:
  json.dump(dic_extracted, json_file)