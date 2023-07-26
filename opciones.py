import sqlite3


class options(object):

     

     def __init__(self,codigo,articulo,precio,cantidad) -> None:
          self.codigo=codigo
          self.articulo=articulo
          self.precio=precio
          self.cantidad=cantidad
          self.date=sqlite3.connect("dato.db")
          self.cur=self.date.cursor()

     #borra datos(fila) segun el codigo
     def delete(self,codigo):
          self.cur.execute("DELETE FROM papele WHERE codigo=?",(codigo,)) 
          self.date.commit()
          
     #agrega datos a la base
     def agregar(self,codigo,articulo,precio,cantidad):
          self.cur.execute("INSERT INTO papele VALUES (?,?,?,?)",(codigo,articulo,precio,cantidad))
          self.date.commit()

     #cierra el cursor y la conexion al finalizar el codigo
     def close(self):
          self.cur.close()
          self.date.close()

     #no activar en caso de ser necesario este comando borra toda la base de datos 
     def dead(self):
          self.cur.execute("DELETE FROM papele ")
          self.date.commit()

     #actualiza la base de datos segun solicitando codigo o articulo 
     def actualizar_precio(self,codigo,articulo,precio):
          self.cur.execute("UPDATE papele SET precio=? WHERE codigo= ? OR articulo=? ", (precio,codigo,articulo))
          self.date.commit()

     def actualizar_cantidad(self,codigo,articulo,cantidad):
          self.cur.execute("UPDATE papele SET cantidad=? WHERE codigo= ? OR articulo=? ", (cantidad,codigo,articulo))
          self.date.commit()
     
     def lectura_cantidad(self,codigo,articulo):
          self.cur.execute("SELECT cantidad FROM papele WHERE codigo=? OR articulo=? ",(codigo,articulo))
          info=self.cur.fetchone()
          self.date.commit()
          
          return info
     
     def datos(self):
          dev=self.cur.execute("SELECT * FROM papele ORDER BY articulo ")
          self.date.commit()
          return dev
     
     def buscar(self,codigo,articulo,precio,cantidad):
          ask=self.cur.execute("SELECT * From papele WHERE codigo=? OR articulo=? OR precio=? OR cantidad=?",(codigo,articulo,precio,cantidad))
          self.date.commit()
          return ask