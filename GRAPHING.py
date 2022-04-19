from tkinter import Tk, Text, Button, END, re
import tkinter
from turtle import width
from unittest import result



class Interfaz:
    def __init__(self, ventana):
        #le ponemos el nombre a la ventana a mostrar
        self.ventana=ventana
        self.ventana.title('Basic Calculator')
        
        #caja de texto como la pantalla de la calculadora
        self.pantalla = Text(ventana, state='disabled', width=40, height=3, background= 'khaki1', foreground='purple', font= ('Helvetica', 16))

        #Gestor de geometría para ubicar la pantalla dentro de la ventanita generada
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=4, pady=4)

        #Bloque reservado para el programa de operaciones
        self.operacion =''
        
        #Generación de los botones de la calcu.

        Boton1=self.crearBoton(7)
        Boton2=self.crearBoton(8)
        Boton3=self.crearBoton(9)
        Boton4=self.crearBoton(u'\u232B', escribir=False)
        Boton5=self.crearBoton(4)
        Boton6=self.crearBoton(5)
        Boton7=self.crearBoton(6)
        Boton8=self.crearBoton(u'\u00F7')
        Boton9=self.crearBoton(1)
        Boton10=self.crearBoton(2)
        Boton11=self.crearBoton(3)
        Boton12=self.crearBoton('*')
        Boton13=self.crearBoton('.')
        Boton14=self.crearBoton(0)
        Boton15=self.crearBoton('+')
        Boton16=self.crearBoton('-')
        Boton17=self.crearBoton('=',escribir=False, ancho=43, alto=2)

        #Ubicación de los botones con el gestor grid:
        botones=[Boton1,Boton2,Boton3,Boton4,Boton5,Boton6,Boton7,Boton8,Boton9,Boton10,Boton11,Boton12,Boton13,Boton14,Boton15,Boton16,Boton17]
        contador=0
        for fila in range (1,5):
            for columna in range(4):
                botones[contador].grid(row=fila, column=columna)
                contador+=1
                #ubicando al último botón al final
        botones[contador].grid(row=5, column=0, columnspan=4)

        return

    #creamos un nuevo método para hacer los botones
    def crearBoton(self, valor, escribir = True, ancho=9, alto=1):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=('Helvetica', 15), command=lambda:self.click(valor, escribir ))                


    #Ahora hacemos el MÉTODO CLICK que controla el evento disparado al hacer CLICK en el botón:
    def click(self, texto, escribir):
        #cuando el parámetro 'escribir=true', se debe mostrar el valor por pantalla, de lo contrario no.
        if not escribir:
        #solo evaluar si existe alguna operación a evaluar o si el usuario presionó '='
         if (texto =='=' and self.operacion !=''):
         #reemplazar el valor unicode de la división por el operador división de python '/',
          self.operacion=re.sub(u'\u00F7', '/', self.operacion)               
          resultado=str(eval(self.operacion))
          self.operacion=''
          self.limpiarPantalla()
          self.mostrarEnPantalla(resultado)
          #limpiar la pantalla si se presionó el botón de borrado
         elif texto == u'\u232B':
            self.operación=''
            self.limpiarPantalla()
        #mostrar texto
        else:
            self.operacion+=str(texto)
            self.mostrarEnPantalla(texto)

        return
    
    def limpiarPantalla(self):
        self.pantalla.configure(state= 'normal')
        self.pantalla.delete('1.0',END)
        self.pantalla.configure(state= 'disabled')
        return

    def mostrarEnPantalla(self, valor):
        self.pantalla.configure(state= 'normal')
        self.pantalla.insert(END,valor)
        self.pantalla.configure(state ='disabled')
        return    


ventana_principal=Tk()
Basic_Calculator=Interfaz(ventana_principal)
ventana_principal.mainloop()


