import random
import string

def generar_contrasena(longitud, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True):
    caracteres = string.ascii_lowercase
    if usar_mayusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation
    
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena


import tkinter as tk
from tkinter import messagebox


def generar():
    try:
        longitud = int(entry_longitud.get())
        if longitud <= 0:
            raise ValueError("La longitud debe ser un número entero positivo.")
        usar_mayusculas = var_mayusculas.get()
        usar_numeros = var_numeros.get()
        usar_simbolos = var_simbolos.get()
        contrasena = generar_contrasena(longitud, usar_mayusculas, usar_numeros, usar_simbolos)
        label_resultado.config(text=f"Contraseña: {contrasena}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def iniciar_aplicacion():
    ventana = tk.Tk()
    ventana.title("Generador de Contraseñas")
    ventana.geometry("400x300")

    tk.Label(ventana, text="Longitud de la contraseña:").pack(pady=5)
    global entry_longitud
    entry_longitud = tk.Entry(ventana)
    entry_longitud.pack(pady=5)

    global var_mayusculas
    var_mayusculas = tk.BooleanVar(value=True)
    tk.Checkbutton(ventana, text="Incluir mayúsculas", variable=var_mayusculas).pack()

    global var_numeros
    var_numeros = tk.BooleanVar(value=True)
    tk.Checkbutton(ventana, text="Incluir números", variable=var_numeros).pack()

    global var_simbolos
    var_simbolos = tk.BooleanVar(value=True)
    tk.Checkbutton(ventana, text="Incluir símbolos", variable=var_simbolos).pack()

    tk.Button(ventana, text="Generar Contraseña", command=generar).pack(pady=20)

    global label_resultado
    label_resultado = tk.Label(ventana, text="Contraseña:")
    label_resultado.pack(pady=5)

    ventana.mainloop()

if __name__ == "__main__":
    iniciar_aplicacion()