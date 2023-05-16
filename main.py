from tkinter import *
from tkinter import ttk
cor1 ='#b51089' #rosa claro 
cor2 = '#e87bcb' #rosa escuro de fundo
cor3 = '#f2e9f0' #branco
cor4 = '#d3ade0' #rosa bebe
cor5 = '#48115c' #roxo
cor6 = '#e0609a' #rosa pink
 

calcu =Tk()
calcu.title('Pink Calculator')
calcu.geometry('353x518')
calcu.config(bg=cor1)

#Frames
frame_painel = Frame(calcu, width= 355, height = 80, bg=cor4)
frame_painel.grid(row=0, column=0)
frame_teclado = Frame(calcu, width= 355, height = 438, bg=cor5)
frame_teclado.grid(row=1, column=0)



#variavel todos valores
todos_valores= ''

#funções
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    
    #valor na tela
    valor_texto.set(todos_valores)

#comandos para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
  

#função clean
def limpar_tela():
    global todos_valores
    todos_valores =''
    valor_texto.set('')

#apresentação da tela (label)
valor_texto = StringVar()
app_label= Label (frame_painel, textvariable= valor_texto, width=16, height=2, padx=7, relief=FLAT,   anchor="e", justify=RIGHT, font=('Ivy 27 '), bg= cor4, fg=cor5)
app_label.place(x=0,y=0)

#Botoes
b1=Button(frame_teclado, command = limpar_tela , text='C' , width=13, height=3, bg= cor2, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2=Button(frame_teclado, command = lambda: entrar_valores('%'),  text='%' , width=6, height=3, bg= cor6, fg= cor3, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=178, y=0)
b3=Button(frame_teclado, command = lambda: entrar_valores('/'),  text='/' , width=6, height=3, bg = cor6, fg= cor3, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE )
b3.place(x=266, y=0)
b4=Button(frame_teclado, command = lambda: entrar_valores('7'),  text='7' , width=6, height=3, bg= cor1, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=2, y=90)
b5=Button(frame_teclado, command = lambda: entrar_valores('8'),  text='8' , width=6, height=3, bg = cor1, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE )
b5.place(x=90, y=90)
b6=Button(frame_teclado, command = lambda: entrar_valores('9'),  text='9' , width=6, height=3, bg = cor1, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE )
b6.place(x=178, y=90)
b7=Button(frame_teclado, command = lambda: entrar_valores('*'),  text='*' , width=6, height=3, bg = cor6, fg= cor3, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE )
b7.place(x=266, y=90)
b8=Button(frame_teclado, command = lambda: entrar_valores('4'),  text='4' , width=6, height=3, bg= cor1, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=2, y=180)
b9=Button(frame_teclado, command = lambda: entrar_valores('5'),  text='5' , width=6, height=3, bg = cor1, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE )
b9.place(x=90, y=180)
b10=Button(frame_teclado, command = lambda: entrar_valores('6'), text= '6', width=6, height=3, bg = cor1, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE )
b10.place(x=178, y=180)
b11=Button(frame_teclado, command = lambda: entrar_valores('-'), text='-' , width=6, height=3, bg = cor6, fg= cor3, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE )
b11.place(x=266, y=180)
b12=Button(frame_teclado, command = lambda: entrar_valores('1'), text='1' , width=6, height=3, bg= cor1, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=2, y=270)
b13=Button(frame_teclado,command = lambda: entrar_valores('2'),  text='2' , width=6, height=3, bg = cor1, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE )
b13.place(x=90, y=270)
b14=Button(frame_teclado, command = lambda: entrar_valores('3'), text='3' , width=6, height=3, bg = cor1, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE )
b14.place(x=178, y=270)
b15=Button(frame_teclado, command = lambda: entrar_valores('+'), text='+' , width=6, height=3, bg = cor6, fg= cor3, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE )
b15.place(x=266, y=270)
b16=Button(frame_teclado, command = lambda: entrar_valores('0'), text='0' , width=13, height=3, bg= cor1, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=360)
b17=Button(frame_teclado, command = lambda: entrar_valores('.'), text='.' , width=6, height=3, bg= cor1, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=178, y=360)
b18=Button(frame_teclado, command = calcular , text='=' , width=6, height=3, bg = cor6, fg= cor3, font=('Ivy 16 bold'), relief=RAISED, overrelief=RIDGE )
b18.place(x=266, y=360)


calcu.mainloop()