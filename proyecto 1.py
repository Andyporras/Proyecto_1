"""
nombre:
salidad:
retrincciones:
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
nombre:
salidad:
retrinccione:

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
nombre:
salida:
retrincciones:

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
        return
    elif(op=="3"):
        return
    elif(op=="9"):
        return menu()
    else:
        print("Error, digite una de las opciones disponible.")
        return usuarioNormal()
#---------------------------------------------------------------------
"""
nombre:
salida:
retricciones:

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
nombre:
salida:
retricciones:
 
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
            print("Error,el nombre de la empresa ya existen. ")
            return incluir_empresa()           
    else:
        print("Error,digite una cedula con 10 digitos")
        return incluir_empresa()
#--------------------------------------------------------------------
"""
nombre:
entrada:
salida:
retrincciones:

"""
def almacenarInformacion1(archivo):
    informacion=open(archivo)
    almacenar=informacion.readlines()
    informacion.close()
    
    return almacenar

#----------------------------------------------------------------------


#-----------------------------------------------------------------------
"""
nombre:
entrada:
salida:
retrincciones:
"""

def eliminar_empresa():
    cedula=input("Digite el numero de cedula de la empresa: ")
    archivo=open("Gestion de empresa.txt")
    empresas=archivo.readlines()
    if((cedula+"\n") in empresas):
        archivo1=open("Gestion de viaje.txt")
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
nombre:
entrada:
salida:
retrincciones:
"""
def verificar_aux(listaDeEmpresa,linea,cont,datos):
    if cont ==1 :#Se hace la debida verificación de la restricción.
        return Convertir_A_String(datos)
    else:#Si la primera restricción no se cumple se retorna a esta.
        datos+=[listaDeEmpresa[linea].rstrip()]
        return verificar_aux(listaDeEmpresa, linea + 1, cont + 1,datos)



#---------------------------------------------------------------------------------------------------------
    
"""
nombre:
entrada:
salida:
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
    lista = al dato que se desea convertir.
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

#Funcion de lista de contactos.
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
def Mostrar_Empresa(listaDeEmpresa, indice, cont):
    if cont > 3:#Se hace la debida verificación de la restricción.
        print("\n")
    else:#Si la primera restricción no se cumple se retorna a esta.
        print(listaDeEmpresa[indice].rstrip())
        return Mostrar_Empresa(listaDeEmpresa, indice + 1, cont + 1)#Muestra la empresa que el usuario desea eliminar.




#-----------------------------------------------------------------------------------------------------------------------------------------
#Función de modificar contacto.
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
nombre:
entrada:
salida:
retrincciones:
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


def eliminar_transporte():
    placa=input("Digite el numero de la matricula del transporte a eliminar: ")
    archivo=open("Gestion de transporte.txt")
    transportes=archivo.readlines()
    if((placa+"\n") in transportes):
        linea = transportes.index(placa+"\n")
        eliminar=Eliminar_transporte_aux(transportes,linea,0)
        archivo.close()
        archivo=open("Gestion de transporte.txt","w")
        archivo.write(eliminar)
        archivo.close()
        print(f"El transporte con la matricula {placa} a sido eliminado exitosamente ")
        print("\n")
        return Gestion_de_transporte()
    else:
        print(f"No se encontro el transporte con la matricula {placa} ,vuelva a intentarlo. ")
        archivo.close()
        return eliminar_transporte()

#----------------------------------------------------------------------------------------------

def Eliminar_transporte_aux(transporte,linea,cont):
    if (cont==9):
        return Convertir_A_String(transporte)
    else:
        print(transporte[linea].rstrip())
        transporte.pop(linea)
        return Eliminar_transporte_aux(transporte,linea,cont+1)


#----------------------------------------------------------------------------------------

def Modificar_transporte():
    placa=input("Ingrese la placa del transporte a modificar: ")
    transporte = ListaDeTransporte()
    if ((placa + "\n") in transporte):#Verificamos que el número de cédula se encuetre en el archivo. 
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
        nombre de agenda para que fuera de mejor entendimiento.
        """
        print("\n", "\t", "\t", "\t","¡Transporte modificado con éxito! ", "\n")
        return Gestion_de_transporte()
    else:
        print(f"No tienes ningú transporte con la matricula {placa} vuelva a intentarlo de nuevo.")
        return Gestion_de_transporte()#Retorna nuevamente a la función para que el usuario lo vuelva a intentar.
    
#--------------------------------------------------------------------------------------------------------------------

def Mostrar_transporte(listaDeTransporte, linea, cont):
    if cont > 8:#Se hace la debida verificación de la restricción.
        print("\n")
    else:#Si la primera restricción no se cumple se retorna a esta.
        print(listaDeTransporte[linea].rstrip())
        return Mostrar_transporte(listaDeTransporte, linea + 1, cont + 1)


#--------------------------------------------------------------------------------------------------

def Modificar_transporte_Aux(transporte, linea , cont):
    if cont == 7:
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
            transporte_Modificado=input("Ingrese la cantidad de asiento de clase Vip: ")
            transporte[linea]=transporte_Modificado+"\n"
            return Modificar_transporte_Aux(transporte, linea+1, cont+1)
        elif(cont==5):
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
    empresa=input("Digite el nombre la empresa del cual desea viajar: ")
    
    if(empresa+"\n")in transporte:
        monto1=input("Ingrese el valor de la clase VIP: ")
        monto2=input("Ingrese el valor de la clase normal: ")
        monto3=input("INgrese el valro de la clase economica: ")
        numero_de_viaje=str(numero_de_viaje)
        archivo.write("numero de viaje: "+numero_de_viaje+"\n")
        archivo.write(ciudad_de_salida+"\n")
        archivo.write(fecha+"\n")
        archivo.write(hora_de_salida+"\n")
        archivo.write(ciudad_de_llegada+"\n")
        archivo.write(fecha_de_llegada+"\n")
        archivo.write(hora_de_llegada+"\n")
        archivo.write(empresa+"\n")
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

def numero_de_viaje_aux():
    archivo="Gestion de viaje.txt"
    agenda= open (archivo,'r')#Se abre el archivo en el modo que deseamos.
    """
    En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
    que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
    nombre de agenda para que fuera de mejor entendimiento.
    """
    contador =1
    for linea in agenda:
        contador+=1
    agenda.close()
    return contador//10
#----------------------------------------------------------------------------------------------------------------------------

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

def Eliminar_viaje_aux(viajes,linea,cont):
    if (cont==12):
        return Convertir_A_String(viajes)
    else:
        print(viajes[linea].rstrip())
        viajes.pop(linea)
        return Eliminar_viaje_aux(viajes,linea,cont+1)

#-----------------------------------------------------------------------------------------------------------------------------
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
    

def Mostrar_viaje(listaDeViaje, linea, cont):
    if cont > 11:#Se hace la debida verificación de la restricción.
        print("\n")
    else:#Si la primera restricción no se cumple se retorna a esta.
        print(listaDeViaje[linea].rstrip())
        return Mostrar_viaje(listaDeViaje, linea + 1, cont + 1)

#-------------------------------------------------------------------------------------------


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
            montos=input("Ingrese el valor de la clase VIP: ")
            viaje[linea]="Clase VIP:"+montos+"\n"
            return Modificar_viaje_Aux(viaje, linea+1, cont+1) 
        elif(cont==8):
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
        return rango_de_salida()
    elif(op=="2"):
        return rango_de_llegada()
    elif(op=="3"):
        return 
    elif(op=="4"):
        return lugar_de_salida()
    elif(op=="5"):
        return lugar_de_llegada()
    elif(op=="6"):
        return admistrativas()
    else:
        print("\n")
        print("Error,Digite una de las opciones disponible,la opcion {op} no existe o no esta disponible.")
        print("\n")
        return Consultar_historial_de_reservaciones()
    
#-----------------------------------------------------------------------------------------------------------------------------
"""
Nombre: BúsquedasAvanzadas()
Entrada:
    nombre = nombre del contacto que desea buscar.
Salidas:
    Retorna el o los contactos al que pertence que ese nombre.
Retricciones:
    Que nombre cumpliera las restricciones dadas en su función madre *agregarContacto()*
"""    

def rango_de_salida():
    fecha=input("Ingrese la fecha de salida a buscar: ")
    archivo=open("Gestion de viaje.txt")
    lista=archivo.readlines()
    buscar_por_filtro(lista,fecha,2,False,2)
    return Consultar_historial_de_reservaciones()

#-----------------------------------------------------------
    """
Nombre: BuscarContacto(Contactos, buscar,linea,ExisteElContacto, PrimeraLinea,nombre)
Entrada: (Contactos, buscar,linea,ExisteElContacto, PrimeraLinea,nombre)
Salidas:
    Retornara la búsqueda del contacto según corresponda.
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
            return buscar_por_filtro(lista, buscar, linea + 10, True, linea2)
        else:
            return buscar_por_filtro(lista, buscar, linea + 10, Existe, linea2)



#------------------------------------------------------------------------------------------

def rango_de_llegada():
    llegada=input("Ingrese la fecha de llegada a buscar: ")
    archivo=open("Gestion de viaje.txt")
    lista=archivo.readlines()
    buscar_por_filtro(lista,llegada,5,False,5)
    return Consultar_historial_de_reservaciones()


#-----------------------------------------------------------------------------

def lugar_de_salida():
    lugar=input("Ingrese el lugar de salida a buscar: ")
    archivo=open("Gestion de viaje.txt")
    lista=archivo.readlines()
    buscar_por_filtro(lista,lugar,1,False,1)
    return Consultar_historial_de_reservaciones()

#--------------------------------------------------------------------



def lugar_de_llegada():
    lugar=input("Ingrese el lugar de llegada: ")
    archivo=open("Gestion de viaje.txt")
    lista=archivo.readlines()
    buscar_por_filtro(lista,lugar,4,False,4)
    return Consultar_historial_de_reservaciones()

#------------------------------------------------------------------------------


def Estadisticas_de_viaje():
    print()

#----------------------------------------------------------------------------------------------------------------------------------


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
        return
    elif(op=="2"):
        return
    elif(op=="3"):
        return
    elif(op=="4"):
        return
    elif(op=="4"):
        return
    elif(op=="5"):
        return
    elif(op=="6"):
        return usuarioNormal()
    else:
        print("\n")
        print("ERROR,Ingrese una de las opciones disponible, la opcion {op} no esta disponible o no existe.")
        print("\n")
        return consulta_de_viajes()
#----------------------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------------------------

    

    
menu()

