from cProfile import label
from cgitb import text
from ctypes import pointer
from pickle import FRAME        # Importação da aplicação TKINTER......
from tkinter import *
from tkinter import messagebox
from turtle import heading


#....................Validação de Login
def validar_login():
    usuario = user.get()
    senha   = code_pin.get()

    if (usuario == 'gabriel' and senha == 'gabriel2006'):

        import sqlite3

        banco = sqlite3.connect('bade_dados.db') #inserindo intens no banco
        cursor  = banco.cursor()

        #cursor.execute("CREATE TABLE pessoas (nome text,idade integer,senha text email text)")
        #cursor.execute("INSERT INTO pessoas VALUES('Gabriel',16,'20062006''2424@gabriel')")

        banco.commit()

        cursor.execute("SELECT * FROM pessoas")
        print(cursor.fetchall())

        screen = Toplevel(tela)
        screen.title('SGL - Sistema de Gestão de Lucros')

        screen.geometry('800x500')
        screen.iconbitmap('imagens/iconuser.ico')

        screen['bg'] = 'dodgerblue'

        meuMenu = Menu(screen,)

        FileMenu = Menu(meuMenu, tearoff=0)
        FileMenu.add_command(label='Novo Estoque')
        FileMenu.add_command(label='Salvar Alterações')
        meuMenu.add_cascade(label='Estoque', menu=FileMenu)

        EditMenu = Menu(meuMenu, tearoff=0)
        EditMenu.add_command(label='Ver Banco de Dados')
        EditMenu.add_command(label='Ultimo Login')
        EditMenu.add_command(label='Ver Grafico')
        meuMenu.add_cascade(label='Configurações', menu=EditMenu)

        screen.config(menu=meuMenu)

        Label(screen,
         text="SGL - Sistema de Gestão de Lucros!",
         font='Tahoma 22 bold',
         fg='white',
         bg='dodgerblue').pack(expand=True)
        
        screen.mainloop()
    else:
        messagebox.showerror('SGL - Erro de Login*', 'Sem Permissão de Acesso!')
#......................................................................      

#.............Tela do aplicativo.......................
tela = Tk()
tela.title('SGL - Sistema Lucrativos - Login*')

tela.geometry('925x500+300+200')
tela.resizable(False, False)

tela['bg'] = 'dodgerblue'
tela.iconbitmap('imagens/iconuser.ico')

img = PhotoImage(file='imagens/lugro.png')
Label(tela, image=img,bg='dodgerblue').place(x=50, y=50)
#.............................

#,..............linhas adicionais de input.....
frame = Frame(tela,
    width=350,
    height=350,
    bg='dodgerblue',
    )
frame.place(x=550, y=50)
#.......................Titulo do login................
heading = Label(tela,
    text='Conectar-me',
    fg='white',
    bg='dodgerblue',
    font=('Microsoft YaHei UI Light', 28, 'bold'))
heading.place(x=600, y=100)
#----------------------------------------------------

#----primeiro input == Usuário---------------
user = Entry(tela,
    fg='white',
    bg='dodgerblue',
    font='Tahoma 12 normal',
    border=0,
    width=25)
user.place(x=600, y=160)
user.insert(0, 'Usuário')

frame = Frame(tela,
    width=295,
    height=1,
    bg='white'
    ).place(x=600, y=185)
#-----------------------++++++++++++++++++++++++

#---------Segundo input SENHA..................
code_pin = Entry(tela,
    fg='white',
    bg='dodgerblue',
    font='Tahoma 12 normal',
    border=0,
    width=25)
code_pin.place(x=600, y=230)
code_pin.insert(0, 'Codigo pin')


frame = Frame(tela,
    width=295,
    height=1,
    bg='white'
    ).place(x=600, y=260)
#------------------------------------------------------

#-----------------Botão entrar.......................
Button(frame,
    width=20,
    pady=7,
    text='Conectar-me',
    bg='#57a1f8',
    fg='white',
    border=0,
    font='Calibri 12 bold',
    cursor="mouse",
    command=validar_login).place(x=600, y=280)
#........................................
tela.mainloop()