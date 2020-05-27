from enum import Enum

class Fuero(Enum):
    civil = 1
    penal = 2
    laboral = 3
    familiar = 4
    comercial = 5


class Expediente:
    def __init__(self,nroExpediente = 0,fuero = Fuero.civil,prioridad=0,estado=0):
        self.nroExpediente = nroExpediente
        self.fuero = fuero


        if prioridad == 1:
            self.prioridad = 'normal'
        elif prioridad == 2:
            self.prioridad = 'urgente'
        else:
            raise Exception('opcion incorrecta')

        if estado == 1:
            self.estado = 'Investigacion'
        elif estado == 2:
            self.estado = 'en juicio'


    def __repr__(self):
        cadena = 'nro Expediente: ' + str(self.nroExpediente) + '\nfuero de la causa: '+ str(self.fuero.name) + '\nprioridad: ' +  str(self.prioridad) +'\nestado de la causa: ' + str(self.estado)
        return cadena

class ExpedienteNormal:
    def __init__(self):
        self.expedienteNormal
    def __init__(self):
        self.expedienteNormal = []

  def empty(self):
    self.expedienteNormal.clear()

  def queue(self,item):
    self.expedienteNormal.insert(0,item)

  def dequeue(self):
    data = None
    if not self.isEmpty():
      data = self.expedienteNormal.pop()
    else:
      raise Exception('queue isEmpty')
    return data

  def top(self):
    data = None
    if not self.isEmpty():
      data = self.expedienteNormal[len(self.expedienteNormal)-1]
    else:
      raise Exception('queque isEmpy')
    return data

  def clonar(self):
    clon = Queue()
    for item in reversed(self.expedienteNormal):
      clon.queue(item)
    return clon

  def lenQueue(self):
    return len(self.expedienteNormal)

  def isEmpty(self):
    return len(self.expedienteNormal) == 0

  def __repr__(self):
    return str(self.expedienteNormal)




class ExpedienteUrgente:
    def __init__(self):
        self.expedienUrgente

    def __init__(self):
        self.expedienUrgente = []

  def empty(self):
    self.expedienUrgente.clear()

  def queue(self,item):
    self.expedienUrgente.insert(0,item)

  def dequeue(self):
    data = None
    if not self.isEmpty():
      data = self.expedienUrgente.pop()
    else:
      raise Exception('queue isEmpty')
    return data

  def top(self):
    data = None
    if not self.isEmpty():
      data = self.expedienUrgente[len(self.expedienUrgente)-1]
    else:
      raise Exception('queque isEmpy')
    return data

  def clonar(self):
    clon = Queue()
    for item in reversed(self.expedienUrgente):
      clon.queue(item)
    return clon

  def lenQueue(self):
    return len(self.expedienUrgente)

  def isEmpty(self):
    return len(self.expedienUrgente) == 0

  def __repr__(self):
    return str(self.expedienUrgente)


class Juzgado:
    def __init__(self,nombre,normarl,urgente):
        self.nombre = nombre
        self.normal = normal
        self.urgente = urgente



expediente = Expediente(125,Fuero.civil,1,1)

print(expediente)
