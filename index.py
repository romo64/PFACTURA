from PyPDF2 import PdfReader
import re

#Intento de buscar cuit por cantidad de numeros seguidos en total 11
def cuit():
    elcuit = []

    for x in re.findall(r".*((?:\b\d{2}[-]\d{8}[-]\d\b))", cadena, re.DOTALL) or re.findall(r'\d{11}', cadena):
        print(x)
    #for x in re.findall(r'\b\d{2}[-]\d{8}[-]\d{1}\b', cadena) or re.findall(r'\d{11}', cadena):
        if len(x) >= 11:
            x = re.sub('-','',x)
            if x != "30500017704":
                elcuit.append(int(x))
                break
        elif len(x) == 11:
            elcuit.append(int(x))
        else:
            elcuit.append("No se encontro el CUIT")
    print(f"Su Nro de cuit es: {elcuit}")

def comp():
    elcomp = []
    for y in re.findall(r'\s\d{8}\n', cadena) or re.findall(r'\s\d{8}\s\n', cadena) or re.findall(r'\d{8}\s\n', cadena) or re.findall(r'\b\d{4}[-]\d{8}\b', cadena):
    #for y in re.findall(r'\b\d{4}[-]\d{8}\b', cadena):
        if len(y) >= 13:
            guion = y.find("-")
            pasado_guion = guion+1
            y = y[pasado_guion:]
            elcomp.append(int(y))
            break
        elif len(y) <= 12:
            elcomp.append(int(y)) #agregar el int
            break
        else:
            elcomp.append("No se encontro el Nro de comp.")
    print(f"Su Nro de comprobante es: {elcomp}")

#Leemos el pdf entero y luego usamos page para leer la pagina deseada.
reader = PdfReader("factura4.pdf")
page = reader.pages[0]

#Extraemos el texto del pdf
informacion = page.extract_text()

#Creamos y abre un txt en modo de escritura y pasamos todo el texto
with open ("pdf.txt", "w") as txt:
    txt.write(informacion)

#Pasamos todo el texto a mayuscula y creamos las palabras claves
cadena = informacion.upper()
subcadena = "CUIT" #la 1ra subcadena que queremos
subcadena2 = "COMP." #la 2da subcadena que queremos

cuit()
comp()
# #Creamos un txt que cotiene el cuit y el nro del comp.
# with open("resultado.txt", "w") as txt:
#     txt.write(f"El numero de cuit es {texto}\n")
#     txt.write(f"El Comprobante Nro es: {texto_comp}\n")