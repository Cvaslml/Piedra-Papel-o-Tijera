# Importo la libreria tkinter, con el alias tk
import tkinter as tk
from tkinter import messagebox
import random

# ------------------------------
# Ventana principal
# ------------------------------

computadora= { 
    "0":"Piedra", 
    "1":"Papel", 
    "2":"Tijera"
}

def piedra():
    messagebox.showinfo("Piedra, Papel o Tijera", "Hizo click en el boton Piedra")
    c_v = computadora[str(random.randint(0,2))] 
    if c_v == "Piedra":
        resultado = "Empate"
    elif c_v=="Tijera": 
        resultado = "Ganaste"
    else: 
        resultado = "Perdiste"
    at_resultados.insert(tk.INSERT, str(c_v))

def papel():
    messagebox.showinfo("Piedra, Papel o Tijera", "Hizo click en el boton Papel")
    c_v = computadora[str(random.randint(0, 2))] 
    if c_v == "Papel": 
        resultado = "Empate"
    elif c_v=="Tijera": 
        resultado = "Perdiste"
    else: 
        resultado = "Ganaste"
    at_resultados.insert(tk.INSERT, str(c_v))

def tijera():
    messagebox.showinfo("Piedra, Papel o Tijera", "Hizo click en el boton Tijera")
    c_v = computadora[str(random.randint(0,2))] 
    if c_v == "Piedra": 
        resultado = "Perdiste"
    elif c_v == "Tijera": 
        resultado = "Empate"
    else: 
        resultado = "Ganaste"
    at_resultados.insert(tk.INSERT, str(x.get()) + " + " + str(y.get()) + " = " + str(r)+"\n")

def salir():
    messagebox.showinfo("Piedra, Papel o Tijera", "La app se cerrará")
    ventana_principal.destroy()

def programador():
    messagebox.showinfo("Suma enteros", "Gracias por utilizar mi app." + "\nEl programador de tus sueños soy yo!" + "\nJohan Sebastian Herrera Melgarejo")

def reiniciar():
    messagebox.showinfo("Ups! Comenzamos de nuevo")
    at_resultados.delete("1.0","end")

# Creacion objeto Tk (ventana principal)
ventana_principal = tk.Tk()


# Titulo ventana_principal
ventana_principal.title("Piedra, Papel o Tijera")

# Tamaño o dimensiones de la ventana
ventana_principal.geometry("500x500")

# Deshabilitamos el boton maximizar
ventana_principal.resizable(0,0)

# Color de fondo ventana principal
ventana_principal.config(bg="black")

# Icono de la ventana 
ventana_principal.iconbitmap('miz.ico')

# ------------------------------
# Frame entrada datos
# ------------------------------
frame_entrada = tk.Frame(ventana_principal)
frame_entrada.config(bg="pink", width=480, height=70)
frame_entrada.pack(fill=tk.BOTH)
frame_entrada.place(x=10, y=10)

# Etiqueta para el titulo
titulo = tk.Label(frame_entrada,text="Piedra, Papel o Tijera")
titulo.config(bg="pink", fg="black", font=("Segoe UI black", 20))
titulo.place(x=90, y=10)

# ------------------------------
# Frame operaciones
# ------------------------------
frame_operaciones = tk.Frame(ventana_principal)
frame_operaciones.config(bg="pink", width=480, height=280)
frame_operaciones.pack(fill=tk.BOTH)
frame_operaciones.place(x=10, y=90)

# boton piedra
boton_piedra = tk.Button(frame_operaciones, text="Piedra", command=piedra)
boton_piedra.place(x=40, y=160)

# Imagen Piedra
logo_piedra = tk.PhotoImage(file="piedra.png")
Label_logo = tk.Label(frame_operaciones, image = logo_piedra)
Label_logo.place(x=20, y=70)

# boton papel
boton_papel = tk.Button(frame_operaciones, text="Papel", command=papel)
boton_papel.place(x=200, y=160)

# Imagen Papel
logo_papel = tk.PhotoImage(file="papel.png")
Label_logo = tk.Label(frame_operaciones, image = logo_papel)
Label_logo.place(x=180, y=70)

# boton tijera
boton_tijera = tk.Button(frame_operaciones, text="Tijera", command=tijera)
boton_tijera.place(x=370, y=160)

# Imagen Tijera
logo_tijera = tk.PhotoImage(file="tijera.png")
Label_logo = tk.Label(frame_operaciones, image = logo_tijera)
Label_logo.place(x=350, y=70)

# boton salir
boton_reiniciar = tk.Button(frame_operaciones, text="Reiniciar", command=reiniciar)
boton_reiniciar.place(x=400, y=230)

# ------------------------------
# Frame resultados
# ------------------------------
frame_resultados = tk.Frame(ventana_principal)
frame_resultados.config(bg="pink", width=480, height=110)
frame_resultados.pack(fill=tk.BOTH)
frame_resultados.place(x=10, y=380)

# Area de texto de resultados
at_resultados = tk.Text(frame_resultados)
at_resultados.config(width=57, height=5)
at_resultados.place(x=10,y=10)

# boton salir
boton_salir = tk.Button(frame_resultados, text="Salir", command=salir)
boton_salir.place(x=420, y=70)

# Imagen Programador
logo_maiz = tk.PhotoImage(file="maiz.png")
Label_logo = tk.Button(frame_resultados, image = logo_maiz, command= programador)
Label_logo.place(x=10, y=10)


# Desplegar ventana principal, y queda a la espera de los eventos del usuario
ventana_principal.mainloop()