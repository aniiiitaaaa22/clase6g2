import datetime
class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):
        self.__lista_mascotas = []
    
    def verificarExiste(self,historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
        
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas) 
    
    def ingresarMascota(self,mascota):
        self.__lista_mascotas.append(mascota) 
   

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos() 
        return None
    
    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                self.__lista_mascotas.remove(masc)  #opcion con el pop
                return True  #eliminado con exito
        return False 
    
    def eliminar_medicamento(mascota):
        print("Medicamentos de la mascota:")
        for idx, medicamento in enumerate(mascota.verLista_Medicamentos()):
            print(f"{idx + 1}. {medicamento.verNombre()} - {medicamento.verDosis()}")


def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    diccionario_caninos = {}
    diccionario_felinos = {}
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Eliminar medicamento
                       \n7- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")
                peso=int(input("Ingrese el peso de la mascota: "))

                while True:
                    fecha_str = input("Ingrese la fecha de ingreso (dd/mm/aaaa): ")

                    try:
                        fecha = datetime.datetime.strptime(fecha_str, '%d/%m/%Y').date()
                        break  
                    except ValueError:
                        print("Formato de fecha incorrecto. Ingrese la fecha en formato dd/mm/aaaa.")
                
                nm=int(input("Ingrese cantidad de medicamentos: "))
                lista_med=[]
                nombres_medicamentos_ingresados = []

                for i in range(0,nm):
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    while nombre_medicamentos in nombres_medicamentos_ingresados:
                            print("Este medicamento ya ha sido ingresado. Ingrese otro nombre.")
                            nombre_medicamentos = input("Ingrese un medicamento diferente: ")
                    dosis =int(input("Ingrese la dosis: "))
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)
                    nombres_medicamentos_ingresados.append(nombre_medicamentos)

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)
                
                if tipo == "canino":
                    diccionario_caninos[historia] = mas
                elif tipo == "felino":
                    diccionario_felinos[historia] = mas

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es:", fecha.strftime('%d/%m/%Y'))
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")

        elif menu == 6:  # Eliminar medicamento
            historia = int(input("Ingrese la historia clínica de la mascota: "))
        
            if historia in diccionario_caninos or historia in diccionario_felinos:
                mascota = diccionario_caninos.get(historia) or diccionario_felinos.get(historia)
                
                print("Medicamentos de la mascota:")
                for idx, medicamento in enumerate(mascota.verLista_Medicamentos()):
                    print(f"{idx + 1}. {medicamento.verNombre()} - {medicamento.verDosis()}")
                
                if mascota.verLista_Medicamentos():
                    try:
                        med_eliminar = int(input("Ingrese el número del medicamento a eliminar: ")) - 1
                        
                        if 0 <= med_eliminar < len(mascota.verLista_Medicamentos()):
                            mascota.verLista_Medicamentos().pop(med_eliminar)
                            print("Medicamento eliminado.")
                        else:
                            print("Número de medicamento inválido.")
                    except ValueError:
                        print("Ingrese un número válido.")
                else:
                    print("La mascota no tiene medicamentos para eliminar.")
            else:
                print("No se encontró la mascota con la historia clínica proporcionada.")

                
        elif menu == 7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                

