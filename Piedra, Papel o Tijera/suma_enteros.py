# importo la libreria tkinter, con el alias tk
from pydoc import plain
import tkinter as tk
from tkinter import messagebox


#---------------------------
# Funciones operaciones
# --------------------------
def calcular():
    messagebox.showinfo("Suma enteros", "Hizo click en el boton Calcular")
    r = x.get() + y.get()
    at_resultados.insert(tk.INSERT, str(x.get()) + " + " + str(y.get()) + " = " + str(r)+"\n")

def borrar():
    messagebox.showinfo("Suma enteros", "Hizo click en el boton Borrar")
    x.set(0)
    y.set(0)
    at_resultados.delete("1.0","end")

def salir():
    messagebox.showinfo("Suma enteros", "La app se cerrará")
    ventana_principal.destroy()

# -----------------------------
# VENTANA PRINCIPAL
# -----------------------------

# creacion objeto Tk (ventana principal)
ventana_principal = tk.Tk()

# Titulo ventana principal
ventana_principal.title("Suma enteros")

# dimensiones de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton maximizar
ventana_principal.resizable(0,0)

# color de fondo ventana principal
ventana_principal.config(bg="white")

# icono de la ventana
ventana_principal.iconbitmap('maiz.ico')

# -----------------------------
# FRAME ENTRADA DATOS
# -----------------------------
frame_entrada = tk.Frame(ventana_principal)
frame_entrada.config(bg="pink", width=480, height=240)
frame_entrada.place(x=10,y=10)

# etiqueta para el titulo
titulo = tk.Label(frame_entrada,text="SUMA DE ENTEROS")
titulo.config(bg="pink", fg="black", font=("Arial, 12"))
titulo.place(x=200, y=10)

# imagen
logo_uis = tk.PhotoImage(file="s.png")
label_logo = tk.Label(frame_entrada, image=logo_uis)
label_logo.place(x=10, y= 40)

# ----------------
# Def variables
# ----------------
x = tk.TkVersion()
y = tk.TkVersion()
z = tk.TkVersion()

# etiqueta X
label_x = tk.Label(frame_entrada, text = "X =")
label_x.config(bg = "pink", fg="black", font=("Arial", 14))
label_x.place(x=250, y=50)

# caja de texto para X
entry_x = tk.Entry(frame_entrada)
entry_x.config(font=("Arial", 12), textvariable= x)
entry_x.focus_set()
entry_x.place(x=290, y=50)

# etiqueta Y
label_y = tk.Label(frame_entrada, text = "Y =")
label_y.config(bg = "pink", fg="black", font=("Arial", 14))
label_y.place(x=250, y=100)

# caja de texto para Y
entry_y = tk.Entry(frame_entrada, textvariable= y)
entry_y.config(font=("Arial", 12))
entry_y.place(x=290, y=100)

# -----------------------------
# FRAME OPERACIONES
# -----------------------------
frame_operaciones = tk.Frame(ventana_principal)
frame_operaciones.config(bg="pink", width=480, height=120)
frame_operaciones.place(x=10,y=255)

# boton calcular
boton_calcular = tk.Button(frame_operaciones, text="Calcular", command=calcular)
boton_calcular.place(x=10, y=60)

# boton borrar
boton_borrar = tk.Button(frame_operaciones, text="Borrar", command=borrar)
boton_borrar.place(x=160, y=60)

# boton salir
boton_salir = tk.Button(frame_operaciones, text="Salir", command=salir)
boton_salir.place(x=320, y=60)

# -----------------------------
# FRAME RESULTADOS
# -----------------------------
frame_resultados = tk.Frame(ventana_principal)
frame_resultados.config(bg="pink", width=480, height=110)
frame_resultados.place(x=10,y=380)

# area de texto de resultados
at_resultados = tk.Text(frame_resultados)
at_resultados.config(width=57, height=5)
at_resultados.place(x=10,y=10)

# desplegar ventana principal y queda a la espera de eventos del usuario
ventana_principal.mainloop()