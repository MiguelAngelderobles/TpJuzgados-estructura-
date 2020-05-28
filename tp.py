from enum import Enum

class Fuero(Enum):
    civil = 1
    penal = 2
    laboral = 3
    familiar = 4
    comercial = 5

class Prioridad(Enum):
    normal = 1
    urgente = 2

class Expediente:
    def __init__(self,nroExpediente = 0,fuero = Fuero.civil,prioridad = Prioridad.normal,estado=0):
        self.nroExpediente = nroExpediente
        self.fuero = fuero
        self.prioridad = prioridad

        if estado == 1:
            self.estado = 'Investigacion'
        elif estado == 2:
            self.estado = 'en juicio'


    def getPrioridad(self):
        return self.prioridad

    def getFuero(self):
        return self.fuero

    def esNomal(self):
        return True

    def esUrgente():
        return True
    def __repr__(self):
        cadena = 'nro Expediente: ' + str(self.nroExpediente) + '\nfuero de la causa: '+ str(self.fuero.name) + '\nprioridad: ' +  str(self.prioridad.name) +'\nestado de la causa: ' + str(self.estado)
        return cadena

class ColaExpediente:
    def __init__(self):
        self.colaExpediente
    def __init__(self):
        self.colaExpediente = []

    def empty(self):
      self.colaExpediente.clear()

    def queue(self,item):
      self.colaExpediente.insert(0,item)

    def dequeue(self):
      data = None
      if not self.isEmpty():
        data = self.colaExpediente.pop()
      else:
        raise Exception('queue isEmpty')
        return data

    def top(self):
      data = None
      if not self.isEmpty():
        data = self.colaExpediente[len(self.colaExpediente)-1]
      else:
        raise Exception('queque isEmpy')
        return data

    def clonar(self):
      clon = Queue()
      for item in reversed(self.colaExpediente):
          clon.queue(item)
      return clon

    def lenQueue(self):
      return len(self.colaExpediente)

    def isEmpty(self):
      return len(self.colaExpediente) == 0

    def __repr__(self):
      return str(self.colaExpediente)

class Juzgado:
    normal = ColaExpediente()
    urgente = ColaExpediente()

    def __init__(self,nombre):
        self.nombre = nombre
        urgente = ColaExpediente()
        normal = ColaExpediente()

    def __repr__(self):
        cadena = 'nombre del juzgado: '+ self.nombre + '\n' + 'expedientes prioridad normal: '+str(self.normal) + '\n'+ 'expedientes prioridad urgente: '+str(self.urgente)
        return cadena

    def recibirExpediente(self,expediente):
        if expediente.getPrioridad() == Prioridad.normal:
            self.normal.queue(expediente)
        else:
            self.urgente.queue(expediente)




expediente = Expediente(125,Fuero.civil,Prioridad.urgente,1)
juzgado = Juzgado('lopez')
juzgado.recibirExpediente(expediente)
for i in range(10):
    juzgado.recibirExpediente(expediente)
print(juzgado)
