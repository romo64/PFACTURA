from PyPDF2 import PdfReader

#Leemos el pdf entero y luego usamos page para leer la pagina deseada.
reader = PdfReader("factura.pdf")
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

#Corroboramos que ambas esten en el string del txt
if subcadena in cadena:
    print("Existe un cuit")
else:
    print("no existe un cuit")

if subcadena2 in cadena:
    print("Existe nro de comprobante")
else:
    print("No existe nro de comprobante")

#Localizamos en que parte del txt esta el index de "cuit" 
resultado = cadena.index("CUIT")
print(f"El numero del indice de CUIT es {resultado}")
final = resultado+17                                    #Ultimo numero del cuit saltando cada caracter
texto = cadena[resultado+6:final]                       #Seleccionamos desde el 1er numero de cuit hasta el ultimo
texto_final = print(f"El cuit es: {texto}")

#Localizamos en que parte del txt esta el index "COMP."
resultado_comp = cadena.index("COMP.")
print(f"El numero del indice de Comp. Nro es {resultado_comp}")
final_comp = resultado_comp+19                                 #Ultimo nro del comprobante
texto_comp = cadena[resultado_comp+9:final_comp]               #Seleccionamos desde el 1er numero del comp hasta el ultimo.
texto_final_comp = print(f"El Comp. Nro es: {texto_comp}")

#Creamos un txt que cotiene el cuit y el nro del comp.
with open("resultado.txt", "w") as txt:
    txt.write(f"El cuit es: {texto}\n")
    txt.write(f"El Comprobante Nro es: {texto_comp}\n")