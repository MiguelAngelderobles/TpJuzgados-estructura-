
from juzgados import*






expediente1 = Expediente(125,Fuero.civil,Prioridad.urgente,Estado.Investigacion)
expediente2 = Expediente(120,Fuero.civil,Prioridad.normal,Estado.enJuicio)
juzgado = Juzgado('lopez')

juzgado.recibirExpediente(expediente1)
juzgado.recibirExpediente(expediente2)
print(juzgado.primerExpedienteATratar())
