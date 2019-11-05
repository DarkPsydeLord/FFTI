import pandas as pd
import tkinter as tk
from tkinter import filedialog


raiz = tk.Tk()
raiz.withdraw()
nombrearchivo = filedialog.askopenfile()
archivo = pd.read_csv(nombrearchivo, "\t")

archivo.drop(archivo.columns[len(archivo.columns)-1], axis=1, inplace=True)
archivo.rename(columns={'Acumulado Ahorro.1': 'Acumulado Empresa 1'}, inplace=True)
# print(archivo.to_string())
print(archivo.head())

for vueltas in range(3):
    for fila in range(len(archivo.index)):
        datos = str(archivo['codi'].iloc[fila])
        if len(datos) < 4:
            archivo['codi'].iloc[fila] = "0" + datos

for cantidad in range(len(archivo.index)):
    PF = "{0:.2f}".format(archivo['Prestamo Fondo 1'].iloc[cantidad])
    archivo['Prestamo Fondo 1'].iloc[cantidad] = PF
    AH = "{0:.2f}".format(archivo['Acumulado Ahorro'].iloc[cantidad])
    archivo['Acumulado Ahorro'].iloc[cantidad] = AH
    PE = "{0:.2f}".format(archivo['Acumulado Empresa 1'].iloc[cantidad])
    archivo['Acumulado Empresa 1'].iloc[cantidad] = PE

print(archivo.head())

def format_row(row):
    first_line = f"E{row['codi']}" + '\n'
    second_line = [f"A{row[el]}|2019|{el}" for el in ['Acumulado Ahorro', 'Prestamo Fondo 1', 'Acumulado Empresa 1']]
    second_line = '\n'.join(second_line)
    return f"{first_line}{second_line}"


format_text = archivo.apply(format_row, axis=1)
archivosalida = filedialog.asksaveasfilename(defaultextension=".txt")
salida = open(archivosalida, "w+")

for text in format_text:
    salida.write(text + "\n")

salida.close()
