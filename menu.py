from opciones import options
codigo=0
articulo=""
precio=0.0
cantidad=0

op=options(codigo,articulo,precio,cantidad) #instancia de las opciones y el cursor del db
num=input("eliga la opcion:") #seleccion de la operacion a realizar

while num !="0":

    if num == "1":  #agrega datos a la base de datos dando 4 datos
        print("Agregar datos")
        print("-"*5)
        codigo=input("ingrese el codigo: ")
        articulo=input("ingrese el articulo: ")
        precio=input("precio: ")
        cantidad=input("cantidad")
        op.agregar(codigo,articulo,precio,cantidad) #instancia de la funcion de agregar datos
    elif num =="2":
        dato_eliminar=input("ingesa el dato a eliminar") #eliminar dato por codigo
        op.delete(dato_eliminar)
    elif num=="3": #actualizador de precios en la base de datos
        print("actualizar precio")
        print("por codigo=1, por nombre=2") #seleccion por el modo de busqueda ya se por el codigo del articulo o el nombre
        codigoOarti=input("")
        if codigoOarti == "1":
            codigo=input("codigo del articulo")
            precio_nuevo=input("precio_Nuevo= ")
        elif codigoOarti=="2":
            articulo=input("nombre")
            precio_nuevo=input("precio_Nuevo= ")
        op.actualizar_precio(codigo,articulo,precio_nuevo) #instancia de la funcion de actualizar el precio
    elif num=="4":# actualizacion de cantidad en caso de ventas
        print("obtencion de datos")
        infcode=input("ingrese el codigo o nombre del articulo: ")
        infarti=input("ingrese el codigo o nombre del articulo: ")
        infor=op.lectura_cantidad(infcode,infarti) #obtencion de la fila segun el codigo o nombre
        nueva_cantidad=infor[0]-1
        op.actualizar_cantidad(infcode,infarti,nueva_cantidad)#actualizacion de la cantidad
    elif num=="96":
        op.dead()

    
    num=input("eliga la opcion:")
op.close()