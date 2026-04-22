import tkinter as tk
import os

# Funciones para abrir programas en Windows
def abrir_navegador():
    os.system("start msedge")

def abrir_editor():
    os.system("notepad")

def abrir_terminal():
    os.system("start cmd")

# Crear ventana
ventana = tk.Tk()
ventana.title("Mi Shell Gráfico")
ventana.geometry("300x200")

# Botones
btn1 = tk.Button(ventana, text="🌐 Navegador", command=abrir_navegador)
btn1.pack(pady=10)

btn2 = tk.Button(ventana, text="📝 Editor de Texto", command=abrir_editor)
btn2.pack(pady=10)

btn3 = tk.Button(ventana, text="💻 Terminal", command=abrir_terminal)
btn3.pack(pady=10)

# Ejecutar
ventana.mainloop()