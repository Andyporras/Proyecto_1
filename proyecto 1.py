"""
nombre:menu
entrada:  no hay 
salidad: ejecucion de la opcion selecionada
retrincciones: solo debe digitar las opciones presente y disponible
"""

def menu():
    print("\n")
    print("\t","\t","\t",">>>>>>>Menu principal<<<<<<<","\n")
    print("1. opciones administrativas. ")
    print("2. opciones de usuario normal. ")
    print("3. salir. ")
    print("\n")

    op=input(" Digite la opcion que necesita: ")
    print("\n")

    if(op=="1"):
        print("\t","\t","\t",">>>>>control de seguridad<<<<<","\n")
        clave=input("Digite la clave de acceso: ")
        print("\n")
        contraseña=almacenarInformacion1("clave.txt")
        if(clave in contraseña):
            return admistrativas()
        else:
            print("\n","Error, la clave de acceso es incorrecto. ")
            return menu()
    elif(op=="2"):
        return usuarioNormal()
    elif(op=="3"):
        return print("\t","\t","\t","fue un placer atenderlo ,vuelva pronto. ")
    else:
        print("\t","\t","\t","Error, dite una de las opciones disponible. ")
        return menu()
#--------------------------------------------------------------------------------
"""
nombre:admistrativas
entrada: no hay 
salidad:  ejcucion de la opcion que digito
retrinccione: solo debe selecionar las opciones disponible

"""

def admistrativas():
    print("\t","\t","\t",">>>>>>>menu Administrativo<<<<<<<","\n")
    print("1. Gestión de empresas. ")
    print("2. Gestión de transporte por empresa. ")
    print("3. Gestion de viaje. ")
    print("4. Consultar historial de reservaciones.")
    print("5. Estadisticas de viaje. ")
    print("9. Devolver al menu princinpal ")
    print("\n")

    op=input("Digite una de las opciones:  ")
    if(op=="1"):
        return Gestion_de_empresas()
    elif(op=="2"):
        return Gestion_de_transporte()
    elif(op=="3"):
        return Gestion_de_viaje()
    elif(op=="4"):
        return Consultar_historial_de_reservaciones()
    elif(op=="5"):
        return Estadisticas_de_viaje()
    elif(op=="9"):
        return menu()
    else:
        print("Error,digite una de las opciones disponible.")
        return admistrativas()
    
#-----------------------------------------------------------------------------
"""
nombre:usuarioNormal
entrada: no hay una difinida
salida: ejecucion de la opcion selecionada
retrincciones: solo debe ser las opciones disponible

"""
    
def usuarioNormal():
    print("\n")
    print("\t","\t","\t",">>>>>menu del usuario normal<<<<<","\n")
    print("1. Consulta de viajes.")
    print("2. Reservación de viaje")
    print("3. Cancelación de reservación.")
    print("9. Salir. ")
    print("\n")
    op=input("Digite una de las opciones disponible: ")
    print("\n")
    if(op=="1"):
        return consulta_de_viajes()
    elif(op=="2"):
        return Reservacion_de_viaje()
    elif(op=="3"):
        return Cancelacion_de_reservacion()
    elif(op=="9"):
        return menu()
    else:
        print("Error, digite una de las opciones disponible.")
        return usuarioNormal()
#---------------------------------------------------------------------
"""
nombre: Gestion_de_empresas
entrada: no hay una entrada definida
salida:ejecucion de la opcion seleccionada
retricciones: solo debe seleccionar las opciones disponible

"""

def Gestion_de_empresas():
    print("\t","\t","\t",">>>>>mantenimiento a las empresas<<<<<","\n")
    print("1. Incluir empresa. ")
    print("2. Eliminar empresa. ")
    print("3. Modificar empresa. ")
    print("4. Mostrar Empresas")
    print("5. Regresar. ")
    print("\n")
    op=input("digite una de las opciones: ")
    print("\n")
    if(op=="1"):
        return incluir_empresa()
    elif(op=="2"):
        return eliminar_empresa()
    elif(op=="3"):
        return Modificar_empresa()
    elif(op=="4"):
        return mostrar_empresas()
    elif(op=="5"):
        return admistrativas()
    else:
        print("Error, digite una de las opciones disponible. ","\n")
        return Gestion_de_empresas()
#----------------------------------------------------------------------
"""
nombre: incluir_empresa
entrada: cedula= numero de la cedula juridica
nombre=nombre de la empresa
ubicacion=ubicacion de la empresa
salida: return del menu de Gestion_de_empresas 
retricciones: la cedula debe tener 10 digito y debe ser caracteres los datos ingresado.
 
"""

def incluir_empresa():
    archivo="Gestion de empresa.txt"
    verificar=almacenarInformacion1(archivo)
    empresas=open(archivo,"a")
    
    cedula=input("digite la cedula: ")
    if(len(cedula)==10):
        nombre=input("Digite el nombre de la empresa: ")
        
        if(cedula+"\n" in verificar)==False:
            ubicacion=input("Escriba la ubicacion de la empresa: ")
            empresas.write(cedula+"\n")
            empresas.write(nombre+"\n")
            empresas.write(ubicacion+"\n")
            empresas.write("---------------------------"+"\n")
            empresas.close()
            print("\t","\t","\t",">>>>empresa agragada exitosamente<<<<")
            print("\n")
            return Gestion_de_empresas() 
        else:
            print("Error,la cedula de la empresa ya existen. ")
            return incluir_empresa()           
    else:
        print("Error,digite una cedula con 10 digitos")
        return incluir_empresa()
#--------------------------------------------------------------------
"""
nombre: almacenarInformacion1
entrada:archivo=el nombre de un archivo ya existente 
salida: los datos del archivo en lista
restrincciones: no hay restrincciones defenida

"""
def almacenarInformacion1(archivo):
    informacion=open(archivo)
    almacenar=informacion.readlines()
    informacion.close()
    
    return almacenar


#-----------------------------------------------------------------------
"""
nombre:eliminar_empresa
entrada:no posee entradas
salida: borrar la empresa seleccionada
retrincciones:debe ingresar una placa existente o guardada en el archivo .txt
"""

def eliminar_empresa():
    cedula=input("Digite el numero de cedula de la empresa: ")
    archivo=open("Gestion de empresa.txt")
    empresas=archivo.readlines()
    if((cedula+"\n") in empresas):
        archivo1=open("Gestion de transporte.txt")
        datos=archivo1.readlines()        
        linea = empresas.index(cedula+"\n")
        verificar=verificar_aux(empresas,linea+1,0,[])
        if(verificar+"\n") in datos:
            print("\n")
            print("Esa empresa esta asociada a un transporte. ")
            print("\n")
            return eliminar_empresa()

        else:
            eliminar=Eliminar_Empresa_aux(empresas,linea,0)
            archivo.close()
            archivo=open("Gestion de empresa.txt","w")
            archivo.write(eliminar)
            archivo.close()
            print(f"La empresa con la cedula {cedula} a sido eliminado exitosamente ")
            print("\n")
            return Gestion_de_empresas()
    else:
        print(f"No se encontro ningúna empresa con la cedula {cedula} ,vuelva a intentarlo. ")
        archivo.close()
        return eliminar_empresa()
        
    
        
    

#------------------------------------------------------------------------------------------------

"""
nombre: verificar_aux
entrada:listaDeEmpresa= la informacion de las empresas
linea= linea en que se encuentra la informacion buscada
cont= un contador para detener la funcion
datos =una lista lista vacia 
salida: la linea buscada 
retrincciones: debe ingresar dos numeros enteros y dos lista una vacia y la otra no.
"""
def verificar_aux(listaDeEmpresa,linea,cont,datos):
    if cont ==1 :#Se hace la debida verificación de la restricción.
        return Convertir_A_String(datos)
    else:#Si la primera restricción no se cumple se retorna a esta.
        datos+=[listaDeEmpresa[linea].rstrip()]
        return verificar_aux(listaDeEmpresa, linea + 1, cont + 1,datos)



#---------------------------------------------------------------------------------------------------------
    
"""
nombre:Eliminar_Empresa_aux
entrada:empresas= la informacion de las empresas en lista
linea =posicion del dato que se desea eliminar
cont=condicion de parada
salida:las linea 0 indices eliminado y return de una funcion para transformar la nueva lista en caracteres
retrincciones:
"""
def Eliminar_Empresa_aux(empresas,linea,cont):
    if (cont==4):
        return Convertir_A_String(empresas)
    else:
        print(empresas[linea].rstrip())
        empresas.pop(linea)
        return Eliminar_Empresa_aux(empresas,linea,cont+1)


#-------------------------------------------------------------------------------------------------
                #Función que convierte un dato en un string.
"""
Nombre: convertir_a_string(lista)
Entrada:
    lista =lista del dato que se desea convertir.
Salidas:
    Va a convertir el dato en un string.
Retricciones:
    El parámetro debe de ser una lista.
"""
def Convertir_A_String(lista):
    if isinstance(lista, list):#El parámetro de entrada debe de ser una lista(restricción).
        string = ""
        for linea in lista:
            string += linea
        return string
    else:#Se imprime el error en el caso de que el parámetro de entrada no cumple con las restriciones predeterminadas.
        print("Error: No se puede convertir a string, debido a que el tipo de dato de entrada no es una lista.")
 
#-------------------------------------------------------------------------------------------------------------------------------
"""
nombre:Modificar_empresa
entrada: no tiene definida
salida: un mensaje de que la empresa a sido modificada con exito
restricciones:la cedula debe existir en el archivo de empresas
"""


def Modificar_empresa():
    cedula=input("ingrese la cedula de la empresa a modificar: ")
    empresas = ListaDeEmpresas()
    if ((cedula + "\n") in empresas):#Verificamos que el número de cédula se encuetre en el archivo. 
        linea = empresas.index(cedula + "\n")
        Mostrar_Empresa(empresas, linea, 0)
        empresa_Modificada = Modificar_Empresa_Aux(empresas, linea + 1, 0)#Se creo una variable para ingresar los nuevos datos.
        Gestion = open("Gestion de empresa.txt", "w")#Se abre el archivo en el modo que deseamos.
        """
        En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
        que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
        nombre de agenda para que fuera de mejor entendimiento.
        """
        Gestion.write(Convertir_A_String(empresa_Modificada))#Se escribe la modificación de la empresa en el archivo.
        Gestion.close()#Importante cerrar el archivo.
        """
        En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
        nombre de agenda para que fuera de mejor entendimiento.
        """
        print("\n", "\t", "\t", "\t","¡empresa modificado con éxito! ", "\n")
        return Gestion_de_empresas()
    else:
        print(f"No tienes ningúna empresa con el número de cédula {cedula} vuelva a intentarlo de nuevo.")
        return Gestion_de_empresas()#Retorna nuevamente a la función para que el usuario lo vuelva a intentar.
    

#---------------------------------------------------------------------------------------------------------------------------------

#funcion de lista de empresas
"""
Nombre: ListaDeEmpresas()
Entrada:
    Va abrir el archivo.
Salidas:
    Va a leer las líneas del archivo.
Restricciones:
    Abrir el archivo correcto.
"""   
def ListaDeEmpresas():
    agenda = open("Gestion de empresa.txt")#Se abre el archivo en el modo que deseamos.
    """
    En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
    que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
    nombre de agenda para que fuera de mejor entendimiento.
    """
    listaDeEmpresas = agenda.readlines()#Lee el archivo.
    agenda.close()#Importante cerrar el archivo.
    """
    En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
    nombre de agenda para que fuera de mejor entendimiento.
    """
    return listaDeEmpresas

#--------------------------------------------------------------------------------------------------------------------------
#Función que muestra la empresa a modificar.
"""
nombre: Mostrar_Empresa
entrada: listaDeEmpresa=datos de las empresas en lista
indice= indice de donde se ubica la imformacion de la empresa a mostrar
cont= el numero cero
salida: los datos de la empresa que se desea mostrar
restricciones: el cont (contador) debe ser mayor a 3
"""

def Mostrar_Empresa(listaDeEmpresa, indice, cont):
    if cont > 3:#Se hace la debida verificación de la restricción.
        print("\n")
    else:#Si la primera restricción no se cumple se retorna a esta.
        print(listaDeEmpresa[indice].rstrip())
        return Mostrar_Empresa(listaDeEmpresa, indice + 1, cont + 1)#Muestra la empresa que el usuario desea eliminar.




#-----------------------------------------------------------------------------------------------------------------------------------------
#Función de modificar empresa
"""
Nombre: Modificar_Empresa_Aux(agenda, linea, contador)
Entradas: (agenda, linea, contador)
Salida:
    Va a retornar la empresa modificado.
Restricciones:
    Los parámetros de entrada deben de ser verificados.
"""
def Modificar_Empresa_Aux(agenda, linea, contador):
    if contador == 2:
        return agenda#Archivo al cual le se le dió ese nombre.
    else:#Se hacen las modificaciones del contacto respectivamente.
        if contador == 0:
            Empresa_Modificado = input("Ingrese el nuevo nombre de la empresa: ")
            agenda[linea] =Empresa_Modificado + "\n"
            return Modificar_Empresa_Aux(agenda, linea+1, contador+1)
        else:
            Empresa_Modificado=input("Ingrese la ubicacion de la empresa: ")
            agenda[linea]=Empresa_Modificado+"\n"
            return Modificar_Empresa_Aux(agenda, linea+1, contador+1)
#---------------------------------------------------------------------------------------------------------------------------------------------


    
"""
Nombre: mostrar_empresas()
Entradas:
    El archivo en modo de lectura.
Salida:
    Va a dar una lista de todos lo contactos existentes en la agenda.
Restricciones:
    Abrir el archivo de manera correcta.
"""        
def mostrar_empresas():
    archivo="Gestion de empresa.txt"
    agenda= open (archivo,'r')#Se abre el archivo en el modo que deseamos.
    """
    En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
    que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
    nombre de agenda para que fuera de mejor entendimiento.
    """
    contador =1
    for linea in agenda:
        print("linea",contador,":",linea)#Imprimir todos los contactos existentes en la agenda.
        contador+=1 #Agregamos un contador para que el usuario pueda ver en que linea corresponde a cada dato. 
    agenda.close()#Importante cerrar el archivo.
    """
    En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
    nombre de agenda para que fuera de mejor entendimiento.
    """
    return Gestion_de_empresas()


#-------------------------------------------------------------------------------------------------------------------------------------------
"""
nombre:Gestion_de_transporte()
entrada: no hay una definida 
salida:un menu y la opcion solicitada del menu
retrincciones:debe selecionar una de las opciones existente 
"""

def Gestion_de_transporte():
    print("\t","\t","\t",">>>>>Mantenimiento de los transportes<<<<<")
    print("\n","transportes: ","\n")
    print("1. Incluir transporte")
    print("2. Eliminar transporte")
    print("3. Modificar transporte.")
    print("4. Mostrar los transporte")
    print("5. Regresar.")
    print("\n")
    op=input("digite una de las opciones disponible: ")
    if(op=="1"):
        return incluir()
    elif(op=="2"):
        return eliminar_transporte()
    elif(op=="3"):
        return Modificar_transporte()
    elif(op=="4"):
        return mostrar_Transporte()
    elif(op=="5"):
        return admistrativas()
    else:
        print("\n")
        print(f"Digite una de las opciones disponibles, la opcion {op} no existe")
        print("\n")
        return Gestion_de_transporte()
    
    
#----------------------------------------------------------------------------------
#Función que agrega o incluye el transporte.
"""
nombre: incluir
entrada:pide la la matricula de la lista al usuario
salida: un mensaje de que la empresa a sido agregado existosamente.
restrinciones: la placa no debe existir en el archivo de transporte.
"""


def incluir():
    archivo=open("Gestion de transporte.txt","a")
    placa=input("Ingrese la matricula del transporte: ")
    transporte=ListaDeTransporte()
    if(placa in transporte)==False:
        marca=input("Ingrese la marca del transporte: ")
        modelo=input("Ingrese el modelo del transporte: ")
        año=input("Ingrese el año del transporte: ")
        lista=open("Gestion de empresa.txt")
        lista=lista.read()
        print(lista)
        empresas=open("Gestion de empresa.txt")
        empresas=empresas.readlines()
        empresa=input("Ingrese el nombre de una de las empresas exitente: ")
        if (empresa+"\n") in empresas:
            claseVip=input("Ingrese la cantidad de asiento Vip: ")
            claseNormal=input("Ingrese la catidad de asiento de clase normal: ")
            claseEconomica=input("Ingrese la cantidad de asiento de clase economica: ")
            archivo.write(placa+"\n")
            archivo.write(marca+"\n")
            archivo.write(modelo+"\n")
            archivo.write(año+"\n")
            archivo.write(empresa+"\n")
            archivo.write(claseVip+"\n")
            archivo.write(claseNormal+"\n")
            archivo.write(claseEconomica+"\n")
            archivo.write("--------------------------------------")
            archivo.close()
            print(f"transporte agregado existosamente. ")
            print("\n")
            return Gestion_de_transporte()
        else:
            print("No ingresaste una empresa existente. ")
            return Gestion_de_transporte()
        
    else:
        print("\n")
        print("Error,Ingrese una matricula que no exista.")
        print("\n")
        return incluir()
    
    



#------------------------------------------------------------------------------------------
"""

Nombre: listaDeTranporte(listaContactos, indice, cont)
Entrada:
    Va abrir el archivo.
Salidas:
    Va a leer las líneas del archivo.
Restricciones:
    Abrir el archivo correcto.
"""   
def ListaDeTransporte():
    agenda = open("Gestion de transporte.txt")#Se abre el archivo en el modo que deseamos.
    """
    En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
    que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
    nombre de agenda para que fuera de mejor entendimiento.
    """
    listaDeTransporte = agenda.readlines()#Lee el archivo.
    agenda.close()#Importante cerrar el archivo.
    """
    En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
    nombre de agenda para que fuera de mejor entendimiento.
    """
    return listaDeTransporte

#---------------------------------------------------------------------------------------
"""
nombre: eliminar_transporte
entrada: caracteres ingresados por el usuario
salida: mensaje de que indique la eliminacion del transporte.
restricciones: la placa ingresado por el usuario debe existir en el archivo de transporte.
"""


def eliminar_transporte():
    placa=input("Digite el numero de la matricula del transporte a eliminar: ")
    archivo=open("Gestion de transporte.txt")
    transportes=archivo.readlines()
    if((placa+"\n") in transportes):
        archivo1=open("Gestion de viaje.txt")
        viaje=archivo1.readlines()
        linea = transportes.index(placa+"\n")
        if(transportes[linea]) in viaje ==False:
            eliminar=Eliminar_transporte_aux(transportes,linea,0)
            archivo.close()
            archivo=open("Gestion de transporte.txt","w")
            archivo.write(eliminar)
            archivo.close()
            print(f"El transporte con la matricula {placa} a sido eliminado exitosamente ")
            print("\n")
            return Gestion_de_transporte()
        else:
            print("Error, transporte asociado a un viaje.")
            return eliminar_transporte()
    else:
        print(f"No se encontro el transporte con la matricula {placa} ,vuelva a intentarlo. ")
        archivo.close()
        return eliminar_transporte()

#----------------------------------------------------------------------------------------------
"""
nombre:Eliminar_transporte_aux
entrada: transporte=la informacion de los transporte en lista
linea= linea de la lista que se desea eliminar
cont=un numero cero que ira aumentado su valor por uno por cada recursion que se realice hasta que se cumpla la condición.
salida: la lineas o indice de la lista que fue eliminada de la lista.
restricciones: el cont(contador) debe tener el valor de 9 para terminar la recurción 
"""
def Eliminar_transporte_aux(transporte,linea,cont):
    if (cont==9):
        return Convertir_A_String(transporte)
    else:
        print(transporte[linea].rstrip())
        transporte.pop(linea)
        return Eliminar_transporte_aux(transporte,linea,cont+1)


#----------------------------------------------------------------------------------------
"""
nombre: Modificar_transporte
entrada: la entrada no esta definida , ya que es ingresada por el usuario.
salida: mensaje que indica que el transporte a sido modificado exitosamente.
restricciones: la placa debe existir en el archivo de las empresas.
"""



def Modificar_transporte():
    placa=input("Ingrese la placa del transporte a modificar: ")
    transporte = ListaDeTransporte()
    if ((placa + "\n") in transporte):#Verificamos que el dato de la placa se encuetre en el archivo. 
        linea = transporte.index(placa + "\n")
        Mostrar_transporte(transporte, linea, 0)
        transporte_Modificado = Modificar_transporte_Aux(transporte, linea, 0)#Se creo una variable para ingresar los nuevos datos.
        Gestion = open("Gestion de transporte.txt", "w")#Se abre el archivo en el modo que deseamos.
        """
        En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
        que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
        nombre de agenda para que fuera de mejor entendimiento.
        """
        Gestion.write(Convertir_A_String(transporte_Modificado))#Se escribe la modificación de la empresa en el archivo.
        Gestion.close()#Importante cerrar el archivo.
        """
        En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
        nombre de Gestion para que fuera de mejor entendimiento.
        """
        print("\n", "\t", "\t", "\t","¡Transporte modificado con éxito! ", "\n")
        return Gestion_de_transporte()
    else:
        print(f"No tienes ningú transporte con la matricula {placa} vuelva a intentarlo de nuevo.")
        return Gestion_de_transporte()#Retorna nuevamente a la función para que el usuario lo vuelva a intentar.
    
#--------------------------------------------------------------------------------------------------------------------
"""
nombre:Mostrar_transporte
entrada: listaDeTransporte= los datos del archivo de transporte pero en lista.
linea= linea que se desea mostrar
cont= el numero cero que aumentara por cada recursion hasta que se cumpla la condicion de parada.
restricciones: el cont(contador) debe ser mayor a 8
"""
def Mostrar_transporte(listaDeTransporte, linea, cont):
    if cont > 8:#Se hace la debida verificación de la restricción.
        print("\n")
    else:#Si la primera restricción no se cumple se retorna a esta.
        print(listaDeTransporte[linea].rstrip())
        return Mostrar_transporte(listaDeTransporte, linea + 1, cont + 1)


#--------------------------------------------------------------------------------------------------
"""
nombre:Modificar_transporte_Aux
entrada: transporte=los datos de el archivo que contiene los transporte en lista
linea= linea o indice de donde se encuentra los datos a modificar de la lista.
cont=el numero cero.
salida:retorna el la varible que contiene los datos ya modificado
restricciones: el cont(contador) debe ser igual a 8
"""
def Modificar_transporte_Aux(transporte, linea , cont):
    if cont == 8:
        return transporte#Archivo al cual le se le dió ese nombre.
    else:#Se hacen las modificaciones del contacto respectivamente.
        if cont == 0:
            transporte_Modificado = input("Ingrese la nueva matricula del transporte: ")
            transporte[linea] =transporte_Modificado + "\n"
            return Modificar_transporte_Aux(transporte, linea+1, cont+1)
        elif(cont==1):
            transporte_Modificado=input("Ingrese la nueva marca del transporte: ")
            transporte[linea]=transporte_Modificado+"\n"
            return Modificar_transporte_Aux(transporte, linea+1, cont+1)
        elif(cont==2):
            transporte_Modificado=input("Ingrese el nuevo modelo del transporte: ")
            transporte[linea]=transporte_Modificado+"\n"
            return Modificar_transporte_Aux(transporte, linea+1, cont+1)
        elif(cont==3):
            transporte_Modificado=input("Ingrese el nuevo año del transporte: ")
            transporte[linea]=transporte_Modificado+"\n"
            return Modificar_transporte_Aux(transporte, linea+2, cont+1)
        elif(cont==4):
            transporte_Modificado=input("Ingrese la nueva empresa del transporte: ")
            transporte[linea]=transporte_Modificado+"\n"
            return Modificar_transporte_Aux(transporte, linea+2, cont+1)

        elif(cont==5):
            transporte_Modificado=input("Ingrese la cantidad de asiento de clase Vip: ")
            transporte[linea]=transporte_Modificado+"\n"
            return Modificar_transporte_Aux(transporte, linea+1, cont+1)
        elif(cont==6):
            transporte_Modificado=input("Ingrese la cantidad de asiento de clase normal: ")
            transporte[linea]=transporte_Modificado+"\n"
            return Modificar_transporte_Aux(transporte, linea+1, cont+1)
        else:
            transporte_Modificado=input("Ingrese la cantidad de asiento de clase económica: ")
            transporte[linea]=transporte_Modificado+"\n"
            return Modificar_transporte_Aux(transporte, linea+1, cont+1)
    
    
#-------------------------------------------------------------------------------------------------
"""
Nombre: mostrar_Transporte()
Entradas:
    El archivo en modo de lectura.
Salida:
    Va a dar una lista de todos lo contactos existentes en la agenda.
Restricciones:
    Abrir el archivo de manera correcta.
"""        
def mostrar_Transporte():
    archivo="Gestion de transporte.txt"
    agenda= open (archivo,'r')#Se abre el archivo en el modo que deseamos.
    """
    En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
    que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
    nombre de agenda para que fuera de mejor entendimiento.
    """
    contador =1
    for linea in agenda:
        print("linea",contador,":",linea)#Imprimir todos los contactos existentes en la agenda.
        contador+=1 #Agregamos un contador para que el usuario pueda ver en que linea corresponde a cada dato. 
    agenda.close()#Importante cerrar el archivo.
    """
    En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
    nombre de agenda para que fuera de mejor entendimiento.
    """
    return Gestion_de_transporte()

#-----------------------------------------------------------------------------------------------------------------------
"""
nombre:Gestion_de_viaje
entrada: un caracter ingresado por el usuario
salida: imprime un menor y despues se ejecuta la opcion que solicito.
restricciones: debe ingresar el usuario unas de las opciones disponible.
"""
def Gestion_de_viaje():
    print("\t","\t","\t",">>>>>Gestion de viaje<<<<<")
    print("1. registrar viajes")
    print("2. eliminar viajes")
    print("3. Modificar viajes ")
    print("4. mostrar viajes")
    print("5. regresar")
    print("\n")
    op=input("Digite una de las opciones disponible: ")
    if(op=="1"):
        return registrar_viajes()
    elif(op=="2"):
        return eliminar_viajes()
    elif(op=="3"):
        return modificar_viaje()
    elif(op=="4"):
        return mostrar_viajes()
    elif(op=="5"):
        return admistrativas()
    else:
        print("\n")
        print("Ingrese una de las opciones disponible,la opcion {op} no existe o no esta disponible")
        print("\n")
        return Gestion_de_viaje()
    

#-----------------------------------------------------------------------------------------------
"""
nombre:registrar_viajes
entrada:diferentes datos ingresados por el usuario
salida:un mensaje de que ek viaje se realizo con existo
restricciones:debe ingresar una placa que exista en el archivo que se almacena las empresas.
"""
def registrar_viajes():
    archivo="Gestion de viaje.txt "
    archivo=open(archivo,"a")
    numero_de_viaje=numero_de_viaje_aux()
    ciudad_de_salida=input("Ingrese la ciudad de salida: ")
    fecha=input("Ingrese la fecha de salida: ")
    hora_de_salida=input("Ingrese la hora de salidad del viaje: ")
    ciudad_de_llegada=input("Ingrese la ciudad de llegada: ")
    fecha_de_llegada=input("Ingrese la fecha de la llegada: ")
    hora_de_llegada=input("Ingrese la hora de la llegada: ")
    transporte=ListaDeTransporte()
    lista=open("Gestion de transporte.txt")
    lista=lista.read()
    print(lista)
    empresa=input("Digite el nombre la empresa de viaje: ")
    placa=input("Digite la placa del transporte de la empresa: ")
    
    if(empresa+"\n")in transporte:
        monto1=input("Ingrese el valor de la clase VIP: ")
        monto2=input("Ingrese el valor de la clase normal: ")
        monto3=input("INgrese el valor de la clase economica: ")
        numero_de_viaje=str(numero_de_viaje)
        archivo.write("numero de viaje: "+numero_de_viaje+"\n")
        archivo.write(ciudad_de_salida+"\n")
        archivo.write(fecha+"\n")
        archivo.write(hora_de_salida+"\n")
        archivo.write(ciudad_de_llegada+"\n")
        archivo.write(fecha_de_llegada+"\n")
        archivo.write(hora_de_llegada+"\n")
        archivo.write(empresa+"\n")
        archivo.write(placa+"\n")
        archivo.write("clase VIP:"+monto1+"\n")
        archivo.write("clase normal:"+monto2+"\n")
        archivo.write("clase economica:"+monto3+"\n")
        archivo.write("--------------------------------"+"\n")
        archivo.close()
        print("\t","\t","\t",">>>>>viaje registado exitosamento<<<<<")
        print("\n")
        return Gestion_de_viaje()
    else:
        print("\n")
        print("Ingrese una empresa existente. ")
        print("\n")
        return registrar_viajes()


#-----------------------------------------------------------------------------
"""
nombre: numero_de_viaje_aux
entrada: no hay una definida
salida: un numero segun la cantida de linea que tenga el archivo de viaje.
restricciones: no hay una definida.
"""
def numero_de_viaje_aux():
    archivo="Gestion de viaje.txt"
    agenda= open (archivo,'r')#Se abre el archivo en el modo que deseamos.
    """
    En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
    que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
    nombre de agenda para que fuera de mejor entendimiento.
    """
    contador=0
    for linea in agenda:
        contador+=1
    agenda.close()
    return contador//11+1
#----------------------------------------------------------------------------------------------------------------------------

"""
nombre:eliminar_viajes
entrada: numero del viaje.
salida: mensaje indicando que el viaje fue eliminado.
restricciones:el numero del viaje debe existir.
"""
def eliminar_viajes():
    numero_de_viaje=input("Ingrese el numero de su viaje: ")
    numero_de_viaje=str(numero_de_viaje)
    archivo=open("Gestion de viaje.txt")
    datos=archivo.readlines()
    if("numero de viaje: "+numero_de_viaje+"\n")in datos:
        linea = datos.index("numero de viaje: "+numero_de_viaje+"\n")
        eliminar=Eliminar_viaje_aux(datos,linea,0)
        archivo.close()
        archivo=open("Gestion de viaje.txt","w")
        archivo.write(eliminar)
        archivo.close()
        print(f"El voleto con el numero de viaje {numero_de_viaje} a sido eliminado exitosamente. ")
        print("\n")
        return Gestion_de_viaje()
    else:
        print("\n")
        print("el numero de viaje {numero_de_viaje} no existe,ingrese otro numero de viaje. ")
        print("\n")
        return Gestion_de_viaje()
        

#------------------------------------------------------------------------------------------------------------------------------
"""
nombre: Eliminar_viaje_aux
entrada: viaje= la informacion de la los viajes en lista
linea= linea o indice de la linea que se desea eliminar.
cont= un contador que inicia desde 0.
salida: las linea o indice de las lista que se eliminaron.
restricciones: el cont(contador) debe tener ser igual a 13

"""
def Eliminar_viaje_aux(viajes,linea,cont):
    if (cont==13):
        return Convertir_A_String(viajes)
    else:
        print(viajes[linea].rstrip())
        viajes.pop(linea)
        return Eliminar_viaje_aux(viajes,linea,cont+1)

#-----------------------------------------------------------------------------------------------------------------------------
"""
nombre:modificar_viaje
entrada: dato ingresado por el usuario
salida: mensaje indicando que el viaje fue eliminado
restricciones: el usuario debe ingresar un numero de viaje que existan en el archivo de viajes.
"""

def modificar_viaje():
    numero=input("Ingrese el numero de viaje,del viaje a modificar: ")
    archivo=open("Gestion de viaje.txt")
    datos=archivo.readlines()
    if (("numero de viaje: "+numero + "\n") in datos):#Verificamos que el número de cédula se encuetre en el archivo. 
        linea = datos.index("numero de viaje: "+numero+ "\n")
        Mostrar_viaje(datos, linea, 0)
        viaje_Modificado = Modificar_viaje_Aux(datos, linea, 0)#Se creo una variable para ingresar los nuevos datos.
        Gestion = open("Gestion de viaje.txt", "w")#Se abre el archivo en el modo que deseamos.
        """
        En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
        que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
        nombre de agenda para que fuera de mejor entendimiento.
        """
        Gestion.write(Convertir_A_String(viaje_Modificado))#Se escribe la modificación de la empresa en el archivo.
        Gestion.close()#Importante cerrar el archivo.
        """
        En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
        nombre de agenda para que fuera de mejor entendimiento.
        """
        print("\n", "\t", "\t", "\t","¡Viaje modificado con éxito! ")
        print("\n")
        return Gestion_de_viaje()
    else:
        print(f"No tienes ningú transporte con la matricula {numero} vuelva a intentarlo de nuevo.")
        return modificar_viaje()#Retorna nuevamente a la función para que el usuario lo vuelva a intentar.




#_-------------------------------------------------------------------------------------------------------------------------------------
    
"""
nombre: Mostrar_viaje
entrada: listaDeViaje= informacion de los viaje sen lista.
linea= indice que se desea imprimir
cont=un contador que inicia desde cero
salida: la informacion del viaje que se desea mostrar
restricciones: el contador debe ser mayor a 12 para que termine la recursion
"""
def Mostrar_viaje(listaDeViaje, linea, cont):
    if cont > 12:#Se hace la debida verificación de la restricción.
        print("\n")
    else:#Si la primera restricción no se cumple se retorna a esta.
        print(listaDeViaje[linea].rstrip())
        return Mostrar_viaje(listaDeViaje, linea + 1, cont + 1)

#-------------------------------------------------------------------------------------------
"""
nombre: Modificar_viaje_Aux
entrada: viaje=informacion de los viajes en listas.
linea= indice que se desea modificar
cont=un contador que inicia desde cero
salida: la informacion de los viajes ya editados.
restricciones: el contador debe ser igual a 10 para que termine la recursion
"""

def Modificar_viaje_Aux(viaje, linea , cont):
    if cont == 10:
        return viaje#Archivo al cual le se le dió ese nombre.
    else:#Se hacen las modificaciones del contacto respectivamente.
        if cont == 0:
            viaje_Modificado = input("Ingrese la ciudad de salida: ")
            viaje[linea] =viaje_Modificado + "\n"
            return Modificar_viaje_Aux(viaje, linea+1, cont+1)
        elif(cont==1):
            viaje_Modificado=input("Ingrese la fecha: ")
            viaje[linea]=viaje_Modificado+"\n"
            return Modificar_viaje_Aux(viaje, linea+1, cont+1)
        elif(cont==2):
            viaje_Modificado=input("Ingrese la nueva hora de salida: ")
            viaje[linea]=viaje_Modificado+"\n"
            return Modificar_viaje_Aux(viaje, linea+1, cont+1)
        elif(cont==3):
            viaje_Modificado=input("Ingrese la nueva ciudad de llegada: ")
            viaje[linea]=viaje_Modificado+"\n"
            return Modificar_viaje_Aux(viaje, linea+2, cont+1)
        elif(cont==4):
            viaje_Modificado=input("Ingrese la fecha de llegada nueva: ")
            viaje[linea]=viaje_Modificado+"\n"
            return Modificar_viaje_Aux(viaje, linea+1, cont+1)
        elif(cont==5):
            viaje_Modificado=input("Ingrese la nueva hora de llegada: ")
            viaje[linea]=viaje_Modificado+"\n"
            return Modificar_viaje_Aux(viaje, linea+1, cont+1)
        elif(cont==6):
            lista=open("Gestion de transporte.txt")
            lista=lista.read()
            print(lista)
            empresas=open("Gestion de empresa.txt")
            empresas=empresas.readlines()
        
            viaje_Modificado=input("Ingrese la empresa de transporte: ")
            if(viaje_Modificado+"\n")in empresas:
                viaje[linea]=viaje_Modificado+"\n"
                return Modificar_viaje_Aux(viaje, linea+1, cont+1)
            else:
                print("\n")
                print("Error, Ingrese una de las empresas disponibles")
                print("\n")
                return Modificar_viaje_Aux(viaje, linea, cont)
        elif(cont==7):
            placa:input("Digite la placa del transporte: ")
            viaje[linea]=placa+"\n"
            return Modificar_viaje_Aux(viaje, linea+1, cont+1)
            return 
        elif(cont==8):
            montos=input("Ingrese el valor de la clase VIP: ")
            viaje[linea]="Clase VIP:"+montos+"\n"
            return Modificar_viaje_Aux(viaje, linea+1, cont+1) 
        elif(cont==9):
            montos=input("Ingrese el valor de la clase normal: ")
            viaje[linea]="Clase Normal:"+montos+"\n"
            return Modificar_viaje_Aux(viaje, linea+1, cont+1)

        else:
            montos=input("Ingrese el valor de la clase economica: ")
            viaje[linea]="Clase economico:"+montos+"\n"
            return Modificar_viaje_Aux(viaje, linea+1, cont+1)

            


    

    
    
#--------------------------------------------------------------------------------------------------------------------------
"""
Nombre: mostrar_viajes()
Entradas:
    El archivo en modo de lectura.
Salida:
    Va a dar una lista de todos lo contactos existentes en la agenda.
Restricciones:
    Abrir el archivo de manera correcta.
"""        
def mostrar_viajes():
    archivo="Gestion de viaje.txt"
    agenda= open (archivo,'r')#Se abre el archivo en el modo que deseamos.
    """
    En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
    que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
    nombre de agenda para que fuera de mejor entendimiento.
    """
    contador =1
    for linea in agenda:
        print("linea",contador,":",linea)#Imprimir todos los contactos existentes en la agenda.
        contador+=1 #Agregamos un contador para que el usuario pueda ver en que linea corresponde a cada dato. 
    agenda.close()#Importante cerrar el archivo.
    """
    En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
    nombre de agenda para que fuera de mejor entendimiento.
    """
    return Gestion_de_viaje()
    
        
#-----------------------------------------------------------------------------------------------------------------------------
"""
nombre:consulta_de_viajes
entrada:una opcion seleccionada por el usuario
salida: imprime un menu y despues se ejecuta la opcion seleccionada
restricciones: el usuario debe ingresar una de las opciones presente.
"""

def consulta_de_viajes():
    print("\n")
    print("\t","\t","\t",">>>>>menu de consulta de viajes<<<<<")
    print("\n")
    print("1. Empresa. ")
    print("2. Lugar de salida.")
    print("3. Lugar de llegadda. ")
    print("4. Rango de fecha de salida. ")
    print("5. Rango de fecha de llegada. ")
    print("6. Regresar. ")
    op=input("Seleccione el filtro que necesite: ")
    if(op=="1"):
        return buscar_empresa()
    elif(op=="2"):
        return lugar_de_salida()
    elif(op=="3"):
        return lugar_de_llegada()
    elif(op=="4"):
        return rango_de_salida()
    elif(op=="5"):
        return rango_de_llegada()
    elif(op=="6"):
        return usuarioNormal()
    else:
        print("\n")
        print("Error,Digite una de las opciones disponible,la opcion {op} no existe o no esta disponible.")
        print("\n")
        return consulta_de_viajes()
    
#-----------------------------------------------------------------------------------------------------------------------------
"""
nombre:buscar_empresa
entrada: caracteres
salida: se retorna una funcion que buscara el dato ingresado por el usuario.
restricciones: no hay una definida.
"""
def buscar_empresa():
    empresa=input("Ingrese la empresa a buscar: ")
    archivo=open("Gestion de viaje.txt")
    lista=archivo.readlines()
    buscar_por_filtro(lista,empresa,7,False,7)
    archivo.close()
    return consulta_de_viajes()    

#-----------------------------------------------------------------------------


    
"""
Nombre: rango_de_salida()
Entrada:
    fecha = fecha que se desea  buscar.
Salidas:
    Retorna una funcion que busca la fecha en el archivo de viaje.
Retricciones:
    no hay una definida
"""    

def rango_de_salida():
    fecha=input("Ingrese la fecha de salida a buscar: ")
    archivo=open("Gestion de viaje.txt")
    lista=archivo.readlines()
    buscar_por_filtro(lista,fecha,2,False,2)
    archivo.close()
    return consulta_de_viajes()

#-----------------------------------------------------------
    """
Nombre: buscar_por_filtro(Contactos, buscar,linea,ExisteElContacto, PrimeraLinea,nombre)
Entrada: (lista,buscar,linea,Existe,linea2,)
Salidas:
    Retornara la búsqueda del viaje según corresponda.
Retricciones:
    Verificacion de los parámetros de entrada.
"""
    
def buscar_por_filtro(lista,buscar,linea,Existe,linea2,):
    if linea > len(lista):
        if Existe:
            print(f"Estos son los viajes encontrados según el dato que ingreso. ")
        else:
            print(f"No se encontro nigún viajes que contenga el dato que ingreso, vuelva a intentarlo de nuevo.")
    else:
        if buscar in lista[linea]:
            Mostrar_viaje(lista,linea -linea2, 0)
            return buscar_por_filtro(lista, buscar, linea + 13, True, linea2)
        else:
            return buscar_por_filtro(lista, buscar, linea + 13, Existe, linea2)



#------------------------------------------------------------------------------------------
"""
nombre:rango_de_llegada
entrada: fecha de llegada dada por el usuario
salida: retorno de la funcion encargada que busca el dato ingresado por el usuario
restricciones: no hay una definida.
"""
def rango_de_llegada():
    llegada=input("Ingrese la fecha de llegada a buscar: ")
    archivo=open("Gestion de viaje.txt")
    lista=archivo.readlines()
    buscar_por_filtro(lista,llegada,5,False,5)
    archivo.close()
    return consulta_de_viajes()


#-----------------------------------------------------------------------------
"""
nombre: lugar_de_salida
entrada:lugar= lugar de salida que ingrese el usuario.
salida: retorno de la funcion encargada de buscar el dato ingresado por el usuario.
restricciones: no hay una definida.
"""
def lugar_de_salida():
    lugar=input("Ingrese el lugar de salida a buscar: ")
    archivo=open("Gestion de viaje.txt")
    lista=archivo.readlines()
    buscar_por_filtro(lista,lugar,1,False,1)
    archivo.close()
    return consulta_de_viajes()

#--------------------------------------------------------------------

"""
nombre:lugar_de_llegada
entrada:lugar= lugar que ingrese el usuario.
salida: retorno de la funcion encargada de buscar el dato ingresado por el usuario.
restricciones: no hay una definida.
"""

def lugar_de_llegada():
    lugar=input("Ingrese el lugar de llegada: ")
    archivo=open("Gestion de viaje.txt")
    lista=archivo.readlines()
    buscar_por_filtro(lista,lugar,4,False,4)
    archivo.close()
    return consulta_de_viajes()

#----------------------------------------------------------------------------------------
                           

"""
nombre:Estadisticas_de_viaje
entrada: op= numero del viaje.
salida: imprime los datos del viaje solicitado.
restricciones: debe ser un numero entero la linea.
"""

def Estadisticas_de_viaje():
    archivo=open("Gestion de viaje.txt")
    viajes=archivo.read()
    print(viajes)
    op=input("Ingrese el numero del viaje: ")
    datos=archivo.readlines()# almacena los datos de los viajes
    linea=buscar_linea_aux(datos,"numero de viaje: "+op+"\n",0)
    print("")
    if(isinstance(linea,int)):
        archivo=open("Gestion de viaje.txt")
        datos=archivo.readlines()
        print(datos[linea])
        print(datos[linea+7])
        print(datos[linea+8])
        print("lugar de salida: "+datos[linea+1])
        print("fecha de salida: "+datos[linea+2])
        print("hora de salida: "+datos[linea+3])
        print("lugar de llegada: "+datos[linea+4])
        print("fecha de llegada: "+datos[linea+5])
        print("hora de llegada: "+datos[linea+6])
        archivo1=open("reservacion de viaje.txt")
        datos2=archivo1.readlines()#almacena los datos de las reservaciones 
        linea2=linea_aux(datos2,datos[linea+7],4)
        print("total de asiento VIP reservado: "+datos2[linea2+11][4:])
        archivo3=open("Gestion de transporte.txt")
        datos3=archivo3.readlines()#almacena los datos de los transportes de los viaje.
        linea3=linea3_aux(datos3,datos[linea+7],0)
        vip=datos2[linea2+11]
        vip=int(vip[4:-1])
        disponible=datos3[linea3+5]
        disponible=disponible[:-1]
        normal=datos2[linea2+12]
        normal=int(normal[7:-1])
        print("total de asiento VIP disponible: "+(str((int(disponible[0:])-(vip)))))
        print("total de asiento Normal reservado: "+datos2[linea2+12][7:-1])
        disponible=datos3[linea3+6]
        disponible=disponible[:-1]
        print("Total de asiento Normal disponible: "+(str(int(disponible[0:])-(normal))))
        economico=datos2[linea2+13]
        economico=int(economico[10:-1])
        print("Total de asiento economico reservado: "+(str(economico)))
        disponible=datos3[linea3+7]
        disponible=disponible[:-1]
        print("Total de asiento economico disponible: "+(str(int(disponible)-(economico))))
        costo_VIP=datos[linea+9][10:-1]
        print("Costo del boleto Vip: "+costo_VIP)
        Costo_normal=datos[linea+10][13:-1]
        print("Costo del boleto Normal: "+Costo_normal)
        Costo_Economico=datos[linea+11][16:-1]
        print("Costo del boleto Normal: "+Costo_Economico)
        print("Monto recaudado por el viaje. "+datos2[linea2+14][15:-1])
        archivo.close()
        archivo1.close()
        archivo3.close()
        return admistrativas()
        
        
        
        
    


#-----------------------------------------------------------------------------------------------------------------

"""
nombre:linea3_aux
entrada: datos= un conjunto de lista.
buscar= dato a buscar en la lista.
linea= indice de donde puede estar el dato a buscar.
salida: False en caso que no se encontro el dato a buscar, o indice de donde esta el dato a buscar.
restrinciones: la variable buscar debe estar en la variable datos. si no se encuentra el dato se retorna False. 
"""
def linea3_aux(datos,buscar,linea):
    if(len(datos))<=linea:
        return False
    else:
        if(buscar in datos[linea]):
            return linea
        else:
            return linea3_aux(datos,buscar,linea+9)





#-------------------------------------------------------------
        
"""
nombre:linea_aux
entrada: datos= un conjunto de lista.
buscar= dato a buscar en la lista.
linea= indice de donde puede estar el dato a buscar.
salida: False en caso que no se encontro el dato a buscar, o indice de donde esta el dato a buscar.
restrinciones: la variable buscar debe estar en la variable datos. si no se encuentra el dato se retorna False. 

"""

def linea_aux(datos,buscar,linea):
    if(len(datos))<=linea:
        return False
    else:
        if(buscar in datos[linea]):
            return linea
        else:
            return linea_aux(datos,buscar,linea+17)





#---------------------------------------------------------------------
"""
nombre: buscar_linea_aux
entrada: datos= un conjunto de lista.
buscar= dato a buscar en la lista.
linea= indice de donde puede estar el dato a buscar.
salida: False en caso que no se encontro el dato a buscar, o indice de donde esta el dato a buscar.
restrinciones: la variable buscar debe estar en la variable datos. si no se encuentra el dato se retorna False. 

"""
def buscar_linea_aux(datos,buscar,linea):
    if(len(datos))<=linea:
        return False
    else:
        if(buscar in datos[linea]):
            return linea
        else:
            return buscar_linea_aux(datos,buscar,linea+14)




#----------------------------------------------------------------------------------------------------------------------------------
"""
nombre: Consultar_historial_de_reservaciones
entrada: op=una de las opciones disponible.
salida: imprime un menu y despues retorna la opcion seleccionada por el usuario.
restricciones: debe seleccionar una de las opciones disponible. 
"""
def Consultar_historial_de_reservaciones():
    print("\t","\t","\t",">>>>>Filtra la informacion  por:<<<<<")
    print("\n")
    print("1. Rango de fecha de salida. ")
    print("2. Rango de fecha de llegada. ")
    print("3. Rango de fecha de la reservación. ")
    print("4. lugar de salida. ")
    print("5. lugar de llegada. ")
    print("6. Regresar.")
    print("\n")
    op=input("Digite una de las opciones disponible: ")
    if(op=="1"):
        return rango_de_fecha_de_salida()
    elif(op=="2"):
        return rango_de_fecha_de_llegada()
    elif(op=="3"):
        return rango_de_fecha_de_la_reservacion()
    elif(op=="4"):
        return Buscar_lugar_de_salida()
    elif(op=="5"):
        return Buscar_lugar_de_llegada()
    elif(op=="6"):
        return usuarioNormal()
    else:
        print("\n")
        print("ERROR,Ingrese una de las opciones disponible, la opcion {op} no esta disponible o no existe.")
        print("\n")
        return Consultar_historial_de_reservaciones()
#----------------------------------------------------------------------------------------------------------------------------
"""
nombre: rango_de_fecha_de_salida
entrada: rango= una fecha suministrado por el usuario.
salida:imprime los datos que tenga la misma fecha que ingreso el usuario y posterio a eso retorna la fucion de
consultar_historial_de_reservaciones.
restricciones:no hay una definida.

"""

def rango_de_fecha_de_salida():
    archivo=open("reservacion de viaje.txt")
    lineas=archivo.readlines()
    rango=input("Ingrese el rango de fecha de salida a buscar: ")
    filtrar_por_informacion(lineas,rango,6,False,6)
    archivo.close()
    return Consultar_historial_de_reservaciones()

#--------------------------------------------------------------------------------
"""
nombre: rango_de_fecha_de_llegada.
entrada: rango= una fecha suministrado por el usuario.
salida:imprime los datos que tenga la misma fecha que ingreso el usuario y posterio a eso retorna la fucion de
consultar_historial_de_reservaciones.
restricciones:no hay una definida.

"""
def rango_de_fecha_de_llegada():
    archivo=open("reservacion de viaje.txt")
    lineas=archivo.readlines()
    rango=input("digite el rango de la fecha de llegada a filtar: ")
    filtrar_por_informacion(lineas,rango,9,False,9)
    archivo.close()
    return Consultar_historial_de_reservaciones()

#--------------------------------------------------------------------------------------
"""
nombre:rango_de_fecha_de_la_reservacion.
entrada: rango= una fecha suministrado por el usuario.
salida:imprime los datos que tenga la misma fecha que ingreso el usuario y posterio a eso retorna la fucion de
consultar_historial_de_reservaciones.
restricciones:no hay una definida.

"""
def rango_de_fecha_de_la_reservacion():
    archivo=open("reservacion de viaje.txt")
    lineas=archivo.readlines()
    rango=input("digite el rango de la fecha de reservacion a buscar: ")
    filtrar_por_informacion(lineas,rango,2,False,2)
    return Consultar_historial_de_reservaciones()

#------------------------------------------------------------------------------
"""
nombre: Buscar_lugar_de_salida.
entrada: lugar= un lugar suministrado por el usuario.
salida:imprime los datos que tenga el mismo lugar que ingreso el usuario y posterio a eso retorna la fucion de
consultar_historial_de_reservaciones.
restricciones:no hay una definida.

"""
def Buscar_lugar_de_salida():
    archivo=open("reservacion de viaje.txt")
    lineas=archivo.readlines()
    lugar=input("digite el lugar de salida a buscar: ")
    filtrar_por_informacion(lineas,lugar,5,False,5)
    archivo.close()
    return Consultar_historial_de_reservaciones()

#--------------------------------------------------------------------------------------------
"""
nombre: Buscar_lugar_de_llegada.
entrada: lugar= un lugar suministrado por el usuario.
salida:imprime los datos que tenga el mismo lugar que ingreso el usuario y posterio a eso retorna la fucion de
consultar_historial_de_reservaciones.
restricciones:no hay una definida.

"""
def Buscar_lugar_de_llegada():
    archivo=open("reservacion de viaje.txt")
    lineas=archivo.readlines()
    lugar=input("digite el lugar de llegada a buscar: ")
    filtrar_por_informacion(lineas,lugar,8,False,8)
    return Consultar_historial_de_reservaciones()

    

#-------------------------------------------------------------------------------------------
"""
nombre: filtar_por_informacion.
entrada: lista= varible que contiene los datos del archivo de reservacion
buscar= dato a buscar.
linea= indice de donde se podria ubicar el dato a buscar.
Existe= varible para comprobar si existe la informacion a buscar.
linea2=indice de donde debe iniciar la impresion del dato a buscar.
salida: muestra los datos que se encontro.
restriciones: la linea debe ser menor que la cantidad de listas que contenga la variable lista 
"""
def filtrar_por_informacion(lista,buscar,linea,Existe,linea2):
    if linea > len(lista):
        if Existe:
            print(f"Estos son los viajes encontrados según el dato que ingreso. ")
        else:
            print(f"No se encontro nigún viajes que contenga el dato que ingreso, vuelva a intentarlo de nuevo.")
    else:
        if buscar in lista[linea]:
            print("\n")
            Mostrar_informacion(lista,linea -linea2, 0)
            return filtrar_por_informacion(lista, buscar, linea + 16, True, linea2)
        else:
            return filtrar_por_informacion(lista, buscar, linea + 16, Existe, linea2)


#--------------------------------------------------------------------------------------------------------------------------
"""
nombre:Mostrar_informacion
entrada:datos = un conjunto de lista.
linea= un indice.
cont= un contador.
salida: se imprime las lista solicitadas.
restricciones: el contador debe ser igual a 16 para que termine la recursion.
"""
def Mostrar_informacion(datos,linea,cont):
    if cont ==16:#Se hace la debida verificación de la restricción.
        print("\n")
    else:#Si la primera restricción no se cumple se retorna a esta.
        print(datos[linea].rstrip())
        return Mostrar_informacion(datos, linea + 1, cont + 1)

#---------------------------------------------------------------------------------------------
"""
nombre: Reservacion_de_viaje
entrada:los datos ingresado por el usario.
salida: mensaje de que la reservacion se realizo con exito.
restriccione:el numero del viaje debe estar en el archivo de viaje.

"""

def Reservacion_de_viaje():
    from datetime import datetime # importo la bibloteca datetime para obtener la fecha del sistema 
    fecha_de_reservacion=datetime.now()
    archivo=open("Gestion de viaje.txt")
    mostrar=archivo.read()  
    print(mostrar)
    numero=input("Ingrese el numero de viaje a reservar: ")
    archivo=open("Gestion de viaje.txt")
    viaje=archivo.readlines()
    if("numero de viaje: "+numero+"\n")in viaje:
        nombre=input("Ingrese su nombre: ")
        Vip=input("Ingrese la cantidad de asiento VIP a reservar: ")
        Normal=input("Ingrese la cantidad de asienrto Normal a reservar: ")
        Economico=input("Ingrese la cantidad de asiento Economico a reservar: ")
        linea=viaje.index("numero de viaje: "+numero+ "\n")
        mostrar1=Mostrar_viaje1(viaje,linea,0,[])
        archivo1=open("reservacion de viaje.txt")
        archivo1=archivo1.readlines()
        reserva=contar_aux(archivo1)
        reserva=str(reserva)
        
        comprobante="numero de reserva:"+reserva+"\n"
        comprobante+="persona que reserva:"+nombre+"\n"
        fecha_de_reservacion=str(fecha_de_reservacion)
        comprobante+="fecha y hora de la reservacion:"+fecha_de_reservacion[:-6]+"\n"
        empresa=mostrar1[7]+"\n"
        comprobante+="empresa:"+empresa
        transporte=mostrar1[8]
        comprobante+="transporte:"+transporte+"\n"
        lugar_de_salida=mostrar1[1]
        
        
        comprobante+="lugar de salida:"+lugar_de_salida+"\n"
        fecha_de_salida=mostrar1[2]
        comprobante+="fecha de salida:"+fecha_de_salida+"\n"
        hora_de_salida=mostrar1[3]
        comprobante+="hora de salida:"+hora_de_salida+"\n"
        lugar_de_llegada=mostrar1[4]
        comprobante+="lugar de llegada:"+lugar_de_llegada+"\n"
        comprobante+="fecha de llegada:"+mostrar1[5]+"\n"
        comprobante+="hora de llegada:"+mostrar1[6]+"\n"
        comprobante+="VIP:"+Vip+"\n"
        comprobante+="Normal:"+Normal+"\n"
        comprobante+="Economico:"+Economico+"\n"
        presio=mostrar1[9]
        presio=a_entero(presio,10)
        presio=int(presio)
        presio2=mostrar1[10]
        presio2=a_entero(presio2,13)
        presio2=int(presio2)
        presio3=mostrar1[11]
        presio3=a_entero(presio3,16)
        presio3=int(presio3)
        suma=(int(Vip)*presio)+(int(Normal)*presio2)+(int(Economico)*presio3)
        suma1=str(suma)
        comprobante+="presio a pagar:"+suma1
        print(comprobante)
        archivo2=open("reservacion de viaje.txt","a")
        archivo2.write(comprobante+"\n")
        archivo2.write("--------------------------------------"+"\n")
        archivo2.close()
        print("\t","\t","\t","reservacion realizada exitosamente.")
        return usuarioNormal()
    else:
        print("\n")
        print(f"Error,El numero de viaje no existe,vuelvalo a intentar.")
        print("\n")
        return Reservacion_de_viaje()

#_---------------------------------------------------------------------------------------------------

    
"""
nombre:Mostrar_viaje1
entrada: listaDeViaje, linea, cont, result
salida: una nueva lista con los datos que necesitamos
restricciones: el contador debe ser mayor a 11 para que termine la recursion
"""
        
              
    
def Mostrar_viaje1(listaDeViaje, linea, cont,result):
    if cont > 11:#Se hace la debida verificación de la restricción.
        return result
    else:#Si la primera restricción no se cumple se retorna a esta.
        return Mostrar_viaje1(listaDeViaje, linea + 1, cont + 1,result+[(listaDeViaje[linea].rstrip())])




#-------------------------------------------------------------------------------------------------------------------------
"""
nombre:contar_aux
entrada: una lista.
salida: retorno de la funcion reserva_aux
restrinciones: si es una lista vacia retorna un uno
"""
def contar_aux(lista):
    if(lista==[]):
        return 1
    else:
        return reserva_aux(lista,0)
#-------------------------------------------------------------
"""
nombre: reserva_aux
entrada: una lista y un contador.
salida:la cantida de listas que contenia la varible lista dividico entre 11+1
restricciones: debe llegar la lista a un lista vacia para que finalise la recursion.
"""
def reserva_aux(lista,cont):
    if(lista==[]):
        return cont//11+1
    else:
        return reserva_aux(lista[1:],cont+1)


#-------------------------------------------------------------------------
"""
nombre: a_entero
entrada: una lista y un indice
salida: la lista reducida y solo con los datos que necesitamos y otra funciones.
restricciones: no hay una definida.
"""
def a_entero(lista,eliminar):
    return lista[eliminar:]
#---------------------------------------------------------    
"""
nombre: Cancelacion_de_reservacion
entrada:numero de la reservacion
salida: un mensaje de confirmacion de que ya se cancelo la reservacion.
restricciones: el numero de indetificador debe existir en el archivo de reservacion.
"""
def Cancelacion_de_reservacion():
    identificador=input("Digite el numero identificador de la reservacion: ")
    archivo=open("reservacion de viaje.txt")
    reservaciones=archivo.readlines()
    if(comprobar_si_existe(reservaciones,"numero de reserva:"+identificador+"\n")):
        linea=bucar_indece_aux(reservaciones,"numero de reserva:"+identificador+"\n",0)
        cancelar=Cancelacion_de_reservacion_aux(reservaciones,linea,0)
        archivo.close()
        archivo=open("reservacion de viaje.txt","w")
        archivo.write(cancelar)
        archivo.close()
        print("\t","\t","\t","reservacion cancelada con exito.")
        return usuarioNormal()
        
    else:
        print("Error, Ingrese un numero de identificador que exista")
        op=input("desea realizar de nuevo la opcion o desea retornar al menu si desea realizar de nuevo la operacion presione 1 de no ser asi toque cualquier tecla o enter.")
        if(op=="1"):
            return Cancelacion_de_reservacion()
        else:
            return usuarioNormal()

#------------------------------------------------------------------------

"""
nombre: bucar_indece_aux
entrada: lista = un conjunto de lista.
buscar dato a buscar en las listas.
cont= contador qeu inicia desde 0
salida= retorna el indice de donde se encuentra el dato a buscar.
restricciones: la lista no debe estar vacia.
"""

def bucar_indece_aux(lista,buscar,cont):
    if(lista==[]):
        return print("no existe ese dato. ")
    else:
        if(buscar in lista[0]):
            return cont
        else:
            return bucar_indece_aux(lista[1:],buscar,cont+1)

#-------------------------------------------------------------------------------------------------

"""
nombre: comprobar_si_existe
entrada: lista= un conjunto de lista
buscar= que se decea buscar.
salida: True si se encontro el dato y False si no se encontro.
restricciones: si la lista esta vacia se retorna False.
"""

def comprobar_si_existe(lista,buscar):
    if(lista==[]):
        return False
    else:
        if(buscar in lista[0]):
            return True
        else:
            return comprobar_si_existe(lista[1:],buscar)

#-----------------------------------------------------------

"""
nombre: Cancelacion_de_reservacion_aux
entrada: lista= conjunto de listas.
linea=indice.
cont=un contador.
salida: los indice que se va a eliminar.
restricciones: se detiene la rescursion una vez que el contador sea mayor a 15
"""

def Cancelacion_de_reservacion_aux(lista,linea,cont):
    if(cont>15):
        return Convertir_A_String(lista)
    else:
        print(lista[linea])
        lista.pop(linea)
        return Cancelacion_de_reservacion_aux(lista,linea,cont+1)
    

    
#-------------------------------------------------------------------------------------------------



menu()

