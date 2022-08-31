class Veterninaria:
    Lugar =""
    direccion =""
    telefono = 0
    id = 0
    duenio = ""

    def __init__(self, Lugar, direccion, telefono, id, duenio):
        self.Lugar = Lugar
        self.direccion = direccion
        self.telefono = telefono
        self.id = id
        self.duenio = duenio

    def identificarCorrecto(self,pId):
        if self.id == pId:
            return "Id correcta "
        else:
            return "Id incorrecto"
            
    def estadoPuertas (self,pPuertas):
        if pPuertas=="si":
            self.puertas=True
        else:
            self.puertas=False 

    def abrirPuertas(self):
        if self.puertas==True:
            return "Abriendo puertas..."
        else:
            return "No se abrieron puertas"
    def duenioVivo(self):
        return "El dueño esta vivo :)"
class Duenio:

    nombre = ""
    edad = 0
    telefono=""
    genero =""
    id=0

    def __init__(self, nombre, edad, telefono, genero, id):
        self.nombre=nombre
        self.edad = edad
        self.telefono = telefono
        self.genero = genero
        self.id = id 

    def mayorDeEdad(self):
        if self.edad >= 18:
            return self.nombre+"Es mayor de edad."
        else:
            return self.nombre+"No es mayor de edad, comunicarse con un adulto."
    def buscarPorId(self,pId):
        if pId == self.id:
            return "Nombre: "+self.nombre+" edad: "+str(self.edad)+" Telefono: "+str(self.telefono)
        else:
            return "No se encontro dueño con esa id"
    def esCalvo(self, pCalvo):
        if pCalvo == "si":
            return "El dueño es calvo"
        else:
            return "El dueño no es calvo"

class Mascota:
    nombre = ""
    edad = 0
    especie=""
    genero =""
    id = 0

    def __init__(self, nombre, edad, especie, genero, id):
        self.nombre=nombre
        self.edad = edad
        self.especie = especie
        self.genero = genero
        self.id = id 

    def animalViejo(self):
        if self.edad>=12:
            return self.nombre+" el animal es viejo"
        else:
            return self.nombre+" el animal no es viejo"

    def buscarId(self,pId):
        if pId == self.id:
            return "Nombre: "+self.nombre+" especie: "+self.especie+" Genero: "+self.genero
        else: 
            return "No existe el animal con esa Id"

    def tieneExpectativasDeVida(self,pExpectativas):
        if pExpectativas == "si":
            return self.nombre+" puede vivir"
        else:
            return self.nombre+" Es posible que muera ja"
class Remedio:
    id = 0
    nombre = ""
    farmacia = ""
    precio = 0
    cantidad = 0

    def __init__(self,id,nombre,farmacia,precio,cantidad):
        self.id = id
        self.nombre =nombre
        self.farmacia = farmacia
        self.precio = precio
        self.cantidad = cantidad

    def darReporte(self, pId):
        if(self.id == pId):
            return("************REPORTE REMEDIO************"+"\n"+"Nombre medicamento: "+self.nombre +"\n"+ "Farmacia: "+self.farmacia+"\n"+"Precio: "+str(self.precio)
            +"\n"+"cantidad: "+ str(self.cantidad))
    def darRemeido(self, pRemedio):
        if pRemedio == "si":
            return "El paciente necesita remedios"
        else:
            return "El paciente no necesita remedios"
    
class Consultorio:
    especialista =""
    costo = 0
    paciente = ""
    id = 0
    consultorio = ""

    def __init__(self,especialista,costo,paciente,id,consultorio):
        self.especialista = especialista
        self.costo =costo
        self.paciente = paciente
        self.id = id
        self.consultorio = consultorio

    def darCostoTotal(self,pMedicamento,pOperacion):
        medicamento = 25000
        operacion = 50000
        if pMedicamento == "si" and pOperacion == "si":
            return "El costo es de: "+ str(self.costo+medicamento+operacion)
        elif pMedicamento == "si" and pOperacion == "no":
            return "El costo es de: "+ str(self.costo+medicamento)
        elif pMedicamento == "no" and pOperacion == "si":
            return "El costo es de: "+ str(self.costo+operacion)
        else:
            return "El costo es de: "+str(self.costo)

    def buscarId(self,pId):
        if pId == self.id:
            return("************REPORTE************"+"Nombre especialista: "+self.especialista + "Costo consulta: "+str(self.darCostoTotal("si","si"))+"paciente: "+self.paciente+
            "Consultorio: "+ self.consultorio)
        else:
            return ("No existe paciente con ese id")

    def darNombreEspecialista (self):
        return "Nombre especialista: "+self.especialista




    

print("********************VETERINARIA********************")    
veterinaria1 = Veterninaria("Pasto","Castillos del norte",3158869874,5,"Juan Paty")
print(veterinaria1.identificarCorrecto(5))
veterinaria1.estadoPuertas(input("abrir puertas? (Digite si/no)"))
print(veterinaria1.abrirPuertas())
print(veterinaria1.duenioVivo())

print("********************CLASE DUENIO********************") 
duenio1 = Duenio("Donato Patichoy ",19,3145202569,"Hombre",5)
print(duenio1.mayorDeEdad())
print(duenio1.buscarPorId(5))
print(duenio1.esCalvo(input("Es calvo el dueño? Si/no - ")))


print("********************MASCOTA********************")    
primeraMascota = Mascota("Luna",13,"Gato","Hembra",8)
print (primeraMascota.animalViejo())
print (primeraMascota.buscarId(8))
print (primeraMascota.tieneExpectativasDeVida("si"))

print("******************** Remedio********************")    
medic1 = Remedio(1,"Acetaminofen","DrogasEscobar",68500,20)
print(medic1.darReporte(1))
print(medic1.darRemeido("si"))

print("********************CONSULTORIO********************")    
consult1 = Consultorio("Dr. Herrera23",300000,"Pepito",1,"calle 20 #21 - 50")
print(consult1.darCostoTotal("si","si"))
print(consult1.buscarId(1))
print(consult1.darNombreEspecialista())

