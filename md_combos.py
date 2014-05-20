#-------------------------------------------------------------------------------
# Name:		Ejemplos Tkinter - Combos
# Copyright:   (c) David Trillo Montero 2014 - Manejando datos
#-------------------------------------------------------------------------------

miVersion = "Ejemplo Combos - version 0.1.0"
from Tkinter import *
import ttk

class colores():
	def __init__(self, id, color):
		self.id = id
		self.color = color
	def __str__(self):
		return self.color

class Aplicacion(Frame):
	def __init__(self, master):
		Frame.__init__(self, master=None)
		self.master.title(miVersion)
		self.idcolor = StringVar(value=1)
		# Cemporadas
		Label(self.master, text="Colores").grid(row=1, sticky=W)
		self.cbotemporadas = ttk.Combobox(self.master, textvariable=self.idcolor, state="readonly" )
		self.cbotemporadas.grid(row=1, sticky=E, column=1, columnspan=3)
		self.cbotemporadas.bind("<<ComboboxSelected>>", self.selecciona)
		self.valores = self._cargaFromObject(o_colores, self.cbotemporadas, "color", "id", seleccionado, self.idcolor)

	def selecciona(self, event):
		val = self.idcolor.get()
		print self.valores[val]

	def _cargaFromObject(self, coleccion, objeto, campodesc, campoid, val2select, variable):
		misc , misv = [] , []
		for vv in coleccion:
			misv.append(getattr(vv,campodesc))
			misc.append(getattr(vv,campoid))
			if getattr(vv,campoid) == val2select: variable.set(getattr(vv,campodesc))  # Selección de Quiniela
		objeto["values"] = misv
		return dict(zip(misv, misc))	# Crea diccionario

def creavalores():
	c = colores(1,"rojo")
	o_colores.append(c)
	c = colores(2,"verde")
	o_colores.append(c)
	c = colores(3,"amarillo")
	o_colores.append(c)

o_colores = []
seleccionado = 2
if __name__ == '__main__':
	creavalores()
	root = Tk()
	a = Aplicacion(root)

	root.mainloop()
