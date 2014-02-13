#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #The class will create all widgets for UI.
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Ejemplo @Manejandodatos')
        self.master.geometry('312x266')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('TcmdSalir.TButton', font=('MS Sans Serif',8))
        self.cmdSalir = Button(self.top, text='Salir', command=self.cmdSalir_Cmd, style='TcmdSalir.TButton')
        self.cmdSalir.place(relx=0.205, rely=0.782, relwidth=0.516, relheight=0.184)

        self.Text3Var = StringVar(value='Text1')
        self.Text3 = Entry(self.top, textvariable=self.Text3Var, font=('MS Sans Serif',8))
        self.Text3.place(relx=0.359, rely=0.451, relwidth=0.26, relheight=0.094)

        self.Text2Var = StringVar(value='Text1')
        self.Text2 = Entry(self.top, textvariable=self.Text2Var, font=('MS Sans Serif',8))
        self.Text2.place(relx=0.359, rely=0.331, relwidth=0.26, relheight=0.094)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.top, textvariable=self.Text1Var, font=('MS Sans Serif',8))
        self.Text1.place(relx=0.359, rely=0.211, relwidth=0.26, relheight=0.094)

        self.style.configure('TcmdCalcula.TButton', font=('MS Sans Serif',8))
        self.cmdCalcula = Button(self.top, text='Calcular', command=self.cmdCalcula_Cmd, style='TcmdCalcula.TButton')
        self.cmdCalcula.place(relx=0.205, rely=0.571, relwidth=0.516, relheight=0.184)

        self.style.configure('TLabel3.TLabel', anchor='w', foreground='#008000', font=('MS Sans Serif',10,'bold'))
        self.Label3 = Label(self.top, text='Label3', style='TLabel3.TLabel')
        self.Label3.place(relx=0.667, rely=0.451, relwidth=0.234, relheight=0.094)

        self.style.configure('TLabel3.TLabel', anchor='w', foreground='#008000', font=('MS Sans Serif',10,'bold'))
        self.Label3 = Label(self.top, text='Label3', style='TLabel3.TLabel')
        self.Label3.place(relx=0.667, rely=0.331, relwidth=0.234, relheight=0.094)

        self.style.configure('TLabel3.TLabel', anchor='w', foreground='#008000', font=('MS Sans Serif',10,'bold'))
        self.Label3 = Label(self.top, text='Label3', style='TLabel3.TLabel')
        self.Label3.place(relx=0.667, rely=0.211, relwidth=0.234, relheight=0.094)

        self.style.configure('TLabel2.TLabel', anchor='w', font=('MS Sans Serif',8))
        self.Label2 = Label(self.top, text='Cuota Empate', style='TLabel2.TLabel')
        self.Label2.place(relx=0.026, rely=0.361, relwidth=0.311, relheight=0.064)

        self.style.configure('TLabel2.TLabel', anchor='w', font=('MS Sans Serif',8))
        self.Label2 = Label(self.top, text='Cuota Visitante', style='TLabel2.TLabel')
        self.Label2.place(relx=0.026, rely=0.481, relwidth=0.311, relheight=0.064)

        self.style.configure('TLabel2.TLabel', anchor='w', font=('MS Sans Serif',8))
        self.Label2 = Label(self.top, text='Cuota Local', style='TLabel2.TLabel')
        self.Label2.place(relx=0.026, rely=0.241, relwidth=0.337, relheight=0.064)

        self.style.configure('TLabel1.TLabel', anchor='center', foreground='#0000FF', font=('MS Sans Serif',12,'bold'))
        self.Label1 = Label(self.top, text='Ejemplo Manejando datos', style='TLabel1.TLabel')
        self.Label1.place(relx=0.026, rely=0.03, relwidth=0.952, relheight=0.124)


class Application(Application_ui):
    #The class will implement callback function for events and your logical code.
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def cmdSalir_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def cmdCalcula_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()

