from tkinter import *
from math import *

ventana = Tk()

#Personalizar ventana
ventana.title("Calculadora")
ventana.config(bg="black")
ventana.resizable(width=False, height=False)

#Entrada desde teclado
display = Entry(ventana, font=("Helvetica", 25, "bold"), bg="#DCE1DA", fg="black", width=15, bd=15, justify=RIGHT)
display.grid(row=1, columnspan=4, sticky=W+E)

i = 0

#Funciones

#Función para obtener los números, los números tecleados
def get_numbers(n):
    global i
    display.insert(i, n)
    i += 1

#Funciones para las operaciones
def get_operation(operator):
    global i
    operator_length = len(operator)
    display.insert(i, operator)
    i += operator_length

def clear_display():
    display.delete(0, END)

def undo():
    #Estado actual de la pantalla
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()
        display.insert(0, "E R R O R")

#Funcion para calcular
def calculate():
    global i
    ecuacion = display.get()
    resultado = str(eval(ecuacion))
    display.delete(0, END)
    display.insert(0, resultado)
    longitud = len(resultado)
    i = longitud


#Botones númericos
Button(ventana, text="7", width=5, height=2, bg="#97C1A9", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_numbers(7)).grid(row=3, column=0, sticky=W+E)
Button(ventana, text="8", width=5, height=2, bg="#97C1A9", fg="white", font=("Helvetica", 12, "bold"),command=lambda:get_numbers(8)).grid(row=3, column=1, sticky=W+E)
Button(ventana, text="9", width=5, height=2, bg="#97C1A9", fg="white", font=("Helvetica", 12, "bold"),command=lambda:get_numbers(9)).grid(row=3, column=2, sticky=W+E)

Button(ventana, text="4", width=5, height=2, bg="#97C1A9", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_numbers(4)).grid(row=4, column=0, sticky=W+E)
Button(ventana, text="5", width=5, height=2, bg="#97C1A9", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_numbers(5)).grid(row=4, column=1, sticky=W+E)
Button(ventana, text="6", width=5, height=2, bg="#97C1A9", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_numbers(6)).grid(row=4, column=2, sticky=W+E)

Button(ventana, text="1", width=5, height=2, bg="#97C1A9", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_numbers(1)).grid(row=5, column=0, sticky=W+E)
Button(ventana, text="2", width=5, height=2, bg="#97C1A9", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_numbers(2)).grid(row=5, column=1, sticky=W+E)
Button(ventana, text="3", width=5, height=2, bg="#97C1A9", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_numbers(3)).grid(row=5, column=2, sticky=W+E)

#Botones para signos
Button(ventana, text="AC", width=5, height=2, bg="#B6CFB6", fg="white", font=("Helvetica", 12, "bold"), command=lambda:clear_display()).grid(row=6, column=0, sticky=W+E)
Button(ventana, text="0", width=5, height=2, bg="#97C1A9", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_numbers(0)).grid(row=6, column=1, sticky=W+E)

Button(ventana, text="+", width=5, height=2, bg="#8E929B", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_operation("+")).grid(row=3, column=3, sticky=W+E)
Button(ventana, text="-", width=5, height=2, bg="#8E929B", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_operation("-")).grid(row=4, column=3, sticky=W+E)
Button(ventana, text="x", width=5, height=2, bg="#8E929B", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_operation("*")).grid(row=5, column=3, sticky=W+E)
Button(ventana, text="÷", width=5, height=2, bg="#8E929B", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_operation("/")).grid(row=6, column=3, sticky=W+E)

Button(ventana, text="⌫", width=5, height=2, bg="#B6CFB6", fg="white", font=("Helvetica", 12, "bold"), command=lambda:undo()).grid(row=2, column=3, sticky=W+E)
Button(ventana, text="x²", width=5, height=2, bg="#F3B0B3", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_operation("**2")).grid(row=2, column=2, sticky=W+E) 
Button(ventana, text="(", width=5, height=2, bg="#F3B0B3", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_operation("(")).grid(row=2, column=0, sticky=W+E)
Button(ventana, text=")", width=5, height=2, bg="#F3B0B3", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_operation(")")).grid(row=2, column=1, sticky=W+E)
Button(ventana, text=".", width=5, height=2, bg="#97C1A9", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_operation(".")).grid(row=6, column=2, sticky=W+E)

Button(ventana, text="ln", width=5, height=2, bg="#F3B0B3", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_operation("log(")).grid(row=7, column=0, sticky=W+E)
Button(ventana, text="√", width=5, height=2, bg="#F3B0B3", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_operation("sqrt(")).grid(row=7, column=1, sticky=W+E)
Button(ventana, text="mod", width=5, height=2, bg="#F3B0B3", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_operation("%")).grid(row=7, column=2, sticky=W+E)
Button(ventana, text="=", width=5, height=2, bg="#B6CFB6", fg="white", font=("Helvetica", 12, "bold"), command=lambda:calculate() ).grid(row=7, column=3, sticky=W+E)

Button(ventana, text="sen", width=5, height=2, bg="#F3B0B3", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_operation("sin(")).grid(row=8, column=0, sticky=W+E)
Button(ventana, text="cos", width=5, height=2, bg="#F3B0B3", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_operation("cos(")).grid(row=8, column=1, sticky=W+E)
Button(ventana, text="tan", width=5, height=2, bg="#F3B0B3", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_operation("tan(")).grid(row=8, column=2, sticky=W+E)
Button(ventana, text="exp", width=5, height=2, bg="#F3B0B3", fg="white", font=("Helvetica", 12, "bold"), command=lambda:get_operation("**")).grid(row=8, column=3, sticky=W+E)

ventana.mainloop()