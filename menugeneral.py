from cProfile import label
from tkinter import ttk
from tkinter import *
from opciones import options
from tkinter import messagebox





class principal(options):
    def __init__(self, mn):

        
        self.wind = mn
        self.Ventana1(self.wind)
        codigo=0
        articulo=""
        precio=0.0
        cantidad=0  
        self.code = IntVar()    
        self.arti = StringVar()
        self.prec = DoubleVar()
        self.cant = IntVar()
        self.inst=options(codigo,articulo,precio,cantidad)
        self.fr=None
        self.tabla=None
        self.delecod=IntVar()

    def Ventana1(self,wind):
        global ventana1
        self.wind.title('Papeleria-Menu principal')
        panel=Frame(wind)
        
        panel.pack()
        
        lab=Label(panel,text="seleccione la opcion").grid(row=3,column=4,columnspan=3)
        bt1=Button(panel,text="inventario",command=self.Ventana2,font=('',15),height=3).grid(row=4,column=2,padx=2,pady=3)
        bt2=Button(panel,)
    
    def Ventana2(self):
        global Ventana2
        Ventana2=Toplevel(self.wind)
        Ventana2.title('inventario')
        #Ventana2.geometry('600x400')
        Ventana2.state("zoomed")
        Ventana2.resizable(False,False)
        self.fr=Frame(Ventana2)
        self.fr.pack()
        lb=Label(self.fr,text="Inventario",font=("",26)).grid(row=1,column=3,columnspan=4)
        bt1=Button(self.fr,text="atras",command=self.regresar).grid(row=5,column=7)
        lbcode=Label(self.fr,text="codigo").grid(row=2,column=3,pady=4)
        lbart=Label(self.fr,text="articulo").grid(row=2,column=4,pady=4)
        lbpre=Label(self.fr,text="precio").grid(row=2,column=5,pady=4)
        lbcant=Label(self.fr,text="cantidad").grid(row=2,column=6,pady=4)
        Entry(self.fr,textvariable=self.code).grid(row=3,column=3,padx=3)
        Entry(self.fr,textvariable=self.arti).grid(row=3,column=4,padx=3)
        Entry(self.fr,textvariable=self.prec).grid(row=3,column=5,padx=3)
        Entry(self.fr,textvariable=self.cant).grid(row=3,column=6,padx=3)
        save=Button(self.fr,text='Guardar',command=self.guardar,height=5,width=20).grid(row=3,column=7,padx=10)
        delete=Button(self.fr,text="borrar dato de la tabla",command=self.eliminardato,height=3).grid(row=5,column=3)

        self.tabla=ttk.Treeview(self.fr,height=10,columns=('','','',))
        self.tabla.grid(row=4, column=2, columnspan=6, padx=3, pady=2)
        barra=Scrollbar(self.fr,orient=VERTICAL,command=self.tabla.yview)
        barra.grid(row=4,column=8)
        
        
    

    # Configurar la cabecera del Treeview
        self.tabla.heading('#0', text='Codigo')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Precio')
        self.tabla.heading('#3', text='Cantidad')

        self.dattable()

        if True:
            self.wind.withdraw()


    def guardar(self):
        
        if not (self.code.get() and self.arti.get() and self.prec.get() and self.cant.get()):
            messagebox.showinfo(message="ingrese todos los datos",title="datos insuficientes")
            
        else:
            
            self.inst.agregar(self.code.get(),self.arti.get(),self.prec.get(),self.cant.get())
            self.dattable()
            
    def eliminardato(self):
        frdele=Toplevel(self.wind)
        frdele.title('eliminar dato')
        frdele.geometry('300x90')
        panel=Frame(frdele)
        panel.pack
        
        Label(frdele,text="ingrese el codigo:").grid(row=0,column=0)
        Entry(frdele,textvariable=self.delecod).grid(row=0,column=1,padx=2)
        Button(frdele,text='borrar',command=self.borrar).grid(row=0,column=2,pady=2)
    def borrar(self):
        if not self.delecod.get():
            messagebox.showerror(message='falta informacion',title='error-no se puede ejecutar')
        else:    
            self.inst.delete(self.delecod.get())
            self.dattable()
            
    

        
    def dattable(self):
        graba=self.tabla.get_children()
        for element in graba:
            self.tabla.delete(element)

        for rows in self.inst.datos():
            self.tabla.insert('','end',text=rows[0],values=(rows[1],rows[2],rows[3]))

         
         

    def regresar(self):
        
        self.wind.state("normal")
        self.wind.state("zoomed")

        Ventana2.destroy()
        

if __name__=="__main__":
    mn = Tk()
    #mn.geometry('600x400')
    mn.state("zoomed")
    mn.resizable(False,False)
    ventana=principal(mn)
    
    mn.mainloop()


