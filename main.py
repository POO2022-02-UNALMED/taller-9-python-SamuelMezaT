from tkinter import END, Tk, Button, Entry
# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)

root.geometry("280x245")


# Configuración pantalla de salida 
pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)
i=0
def obtener(dato):
    global i
    i+=1
    pantalla.insert(i,dato)

def calcular():
    global i
    resultado=pantalla.get()
    if i != 0:
        resultadofinal = (eval(resultado))
        pantalla.delete(0,END)
        resultadofinal=str(resultadofinal)
        pantalla.insert(i,resultadofinal)
        
        
# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:obtener(1)).grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:obtener(2)).grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:obtener(3)).grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:obtener(4)).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:obtener(5)).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:obtener(6)).grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:obtener(7)).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:obtener(8)).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda:obtener(9)).grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2",command=lambda:calcular()).grid(row=4, column=0, columnspan=2, padx=0, pady=0)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0,command=lambda:obtener(".")).grid(row=4,column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda:obtener("+")).grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda:obtener("-")).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda:obtener("*")).grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda:obtener("/")).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()