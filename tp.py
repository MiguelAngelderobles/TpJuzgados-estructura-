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

class Estado(Enum):
    Investigacion = 1
    enJuicio = 2

class Expediente:
    def __init__(self,nroExpediente = 0,fuero = Fuero.civil,prioridad = Prioridad.normal,estado = Estado.Investigacion):
        self.nroExpediente = nroExpediente
        self.fuero = fuero
        self.prioridad = prioridad
        self.estado = estado

    def getPrioridad(self):
        return self.prioridad

    def getFuero(self):
        return self.fuero

    def esNormal(self):
        return self.prioridad == Prioridad.normal

    def __repr__(self):
        cadena = 'nro Expediente: ' + str(self.nroExpediente) + '\nfuero de la causa: '+ str(self.fuero.name) + '\nprioridad: ' +  str(self.prioridad.name) +'\nestado de la causa: ' + str(self.estado.name)
        return cadena

class Cola:
    def __init__(self):
        self.cola
    def __init__(self):
        self.cola = []

    def empty(self):
      self.cola.clear()

    def queue(self,item):
      self.cola.insert(0,item)

    def dequeue(self):
      data = None
      if not self.isEmpty():
        data = self.cola.pop()
      else:
        raise Exception('queue isEmpty')
        return data

    def top(self):
      data = None
      if not self.isEmpty():
        data = self.cola[len(self.cola)-1]
      else:
        raise Exception('queque isEmpy')
        return data

    def clonar(self):
      clon = Queue()
      for item in reversed(self.cola):
          clon.queue(item)
      return clon

    def lenQueue(self):
      return len(self.cola)

    def isEmpty(self):
      return len(self.cola) == 0

    def __repr__(self):
      return str(self.cola)

class Juzgado:
    def __init__(self,nombre):
        self.nombre = nombre
        self.urgente = Cola()
        self.normal = Cola()

    def __repr__(self):
        cadena = 'nombre del juzgado: '+ self.nombre + '\n' + 'expedientes prioridad normal: '+str(self.normal) + '\n'+ 'expedientes prioridad urgente: '+str(self.urgente)
        return cadena

    def recibirExpediente(self,expediente):
        if self.urgente.lenQueue() <= 50 and self.normal.lenQueue() <= 50:
            if expediente.getPrioridad() == Prioridad.normal:
                self.normal.queue(expediente)
            else:
                self.urgente.queue(expediente)
        else:
            raise Exception('colas llena')

    def primerExpedienteATratar(self):
        exp = None
        if self.urgente.top() == Prioridad.normal:
            exp = self.urgente.top()
        else:
            exp = self.normal.top()
        return exp






expediente1 = Expediente(125,Fuero.civil,Prioridad.urgente,Estado.Investigacion)
expediente2 = Expediente(120,Fuero.civil,Prioridad.normal,Estado.enJuicio)
juzgado = Juzgado('lopez')

juzgado.recibirExpediente(expediente1)
juzgado.recibirExpediente(expediente2)
print(juzgado)
print(juzgado.primerExpedienteATratar())
