from tkinter import * 

window= Tk()
window.title('Calculadora')

i=0

#Entrada
e_texto= Entry(window,font=('Calibri 20'))
e_texto.grid(column=0,row=0,columnspan=4,padx=50,pady=5)

#Funciones
def click(valor):
	global i 
	e_texto.insert(i,valor)
	i+=1

def borrar():
	e_texto.delete(0,END)
	i=0

def operaciones():
	ecuacion=e_texto.get()
	resultado= eval(ecuacion)
	e_texto.delete(0,END)
	e_texto.insert(0,resultado)
	i=0

#Botones
boton1= Button(window,text='1',width=5,height=2,command= lambda:click(1))
boton2= Button(window,text='2',width=5,height=2,command= lambda:click(2))
boton3= Button(window,text='3',width=5,height=2,command=lambda:click(3))
boton4= Button(window,text='4',width=5,height=2,command= lambda:click(4))
boton5= Button(window,text='5',width=5,height=2,command= lambda:click(5))
boton6= Button(window,text='6',width=5,height=2,command= lambda:click(6))
boton7= Button(window,text='7',width=5,height=2,command= lambda:click(7))
boton8= Button(window,text='8',width=5,height=2,command= lambda:click(8))
boton9= Button(window,text='9',width=5,height=2,command= lambda:click(9))
boton0= Button(window,text='0',width=13,height=2,command= lambda:click(0))

boton_borrar=Button(window,text='AC',width=5,height=2,command= lambda:borrar())
boton_parentesis1= Button(window,text='(',width=5,height=2,command= lambda:click('('))
boton_parentesis2= Button(window,text=')',width=5,height=2,command= lambda:click(')'))
boton_decimal= Button(window,text=',',width=5,height=2,command= lambda:click('.'))

boton_div= Button(window,text='/',width=5,height=2,command= lambda:click('/'))
boton_mult= Button(window,text='*',width=5,height=2,command= lambda:click('*'))
boton_suma= Button(window,text='+',width=5,height=2,command= lambda:click('+'))
boton_resta= Button(window,text='-',width=5,height=2,command= lambda:click('-'))
boton_igual= Button(window,text='=',width=5,height=2,command= operaciones)

#Agregar botones en pantalla
boton_borrar.grid(column=0,row=1,padx=5,pady=5)
boton_parentesis1.grid(column=1,row=1,padx=5,pady=5)
boton_parentesis2.grid(column=2,row=1,padx=5,pady=5)
boton_div.grid(column=3,row=1,padx=5,pady=5)

boton7.grid(column=0,row=2,padx=5,pady=5)
boton8.grid(column=1,row=2,padx=5,pady=5)
boton9.grid(column=2,row=2,padx=5,pady=5)
boton_mult.grid(column=3,row=2,padx=5,pady=5)

boton4.grid(column=0,row=3,padx=5,pady=5)
boton5.grid(column=1,row=3,padx=5,pady=5)
boton6.grid(column=2,row=3,padx=5,pady=5)
boton_suma.grid(column=3,row=3,padx=5,pady=5)

boton1.grid(column=0,row=4,padx=5,pady=5)
boton2.grid(column=1,row=4,padx=5,pady=5)
boton3.grid(column=2,row=4,padx=5,pady=5)
boton_resta.grid(column=3,row=4,padx=5,pady=5)

boton0.grid(column=0,columnspan=2,row=5,padx=5,pady=5)
boton_decimal.grid(column=2,row=5,padx=5,pady=5)
boton_igual.grid(column=3,row=5,padx=5,pady=5)

window.mainloop()