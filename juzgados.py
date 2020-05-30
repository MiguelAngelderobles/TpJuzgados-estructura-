from cola import*
from expediente import*


# TDA tipo Juzgado

class Juzgado:
    def __init__(self,nombre):
        self.nombre = nombre
        self.urgente = Cola()
        self.normal =  Cola()

    def __repr__(self):
        cadena = 'nombre del juzgado: '+ self.nombre + '\n' + 'expedientes prioridad normal: '+str(self.normal) + '\n'+ 'expedientes prioridad urgente: '+str(self.urgente)
        return cadena
    def tieneNormal(self):
        return not self.normal.isEmpty()

    def tieneUrgentes(self):
        return not self.urgente.isEmpty()


    def recibirExpediente(self,expediente):
        if self.urgente.lenQueue() <= 50 and self.normal.lenQueue() <= 50:
            if expediente.esNormal():
                self.normal.queue(expediente)
            else:
                self.urgente.queue(expediente)
        else:
            raise Exception('colas llena')

    def primerExpedienteATratar(self):
        exp = None

        if self.tieneUrgentes():
            exp = self.urgente.top()
        elif self.tieneNormal():
            exp = self.normal.top()
        return exp
