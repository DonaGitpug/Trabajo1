class Animal:
  nombre = str
  raza = str
  sexo = str
  color = str
  tamanio = str
  
  def _init_(self, nombre, raza, sexo, color, tamanio):
    self.nombre = nombre
    self.raza = raza
    self.sexo = sexo
    self.color = color
    self.tamanio = tamanio

  def buscarPorRaza(raza):
    return print('Lista animales por raza')
  def obtenerNombreMascota():
    return print('El nombre de la mascota')
  def modificarAnimal():
    return print('Mascota modificada')
  def modificarEstado():
    return print('Cambia el estado del animal')
  def darNumeroAnimales():
    return print('Numero de animales')
    
class Persona:
  nombre = str
  id = int
  numero = int
  direcion = str
  correo = str
  
  def _init_(self, nombre, id, numero, direcion, correo):
    self.nombre = nombre
    self.id = id
    self.numero = numero
    self.direcion = direcion
    self.correo = correo

  def buscarPersona(id):
    return print('Pesona id')
  def agregarMacota():
    return print('Agrega un animal')
  def modificarPersona():
    return print('Persona modificada')
  def agregarPersona():
    return print('Agrega una nueva persona')
  def buscarPorNombre():
    return print('Datos de persona')

class Factura:
  numeroCarpeata = int
  total = float
  fecha = " "
  codigoAnimal = int
  codigoServicio = int
  
  def _init_(self, numeroCarpeata, total, fecha, codigoAnimal, codigoServicio):
    self.numeroCarpeata = numeroCarpeata
    self.total = total
    self.fecha = fecha
    self.codigoAnimal = codigoAnimal
    self.codigoServicio = codigoServicio

  def buscarFactura(numeroCarpeta):
    return print('Pesona id')
  def buscarPorFecha():
    return print('Facturas por fechas')
  def modificarFactura():
    return print('Factura modificada')
  def promedioMensual():
    return print('Valor Total promedio')
  def imprimirFacturaPorServicio(codigoServicio):
    return print('Factura de un servicio')

class Medicamentos:
  idMedicamento = str
  tipoMedicamento = str
  fechaCaducidad = " "
  numeroDosis = int
  cantidadExistente = int
  
  def _init_(self, idMedicamento, tipoMedicamento, fechaCaducidad, numeroDosis, cantidadExistente):
    self.idMedicamento = idMedicamento
    self.tipoMedicamento = tipoMedicamento
    self.fechaCaducidad = fechaCaducidad
    self.numeroDosis = numeroDosis
    self.cantidadExistente = cantidadExistente

  def buscarMedicamento(idMedicamento):
    return print('Medicamento')
  def darMedicamentoVencido(fechaCaducidad):
    return print('Medicamento vencido')
  def modificarMedicamento():
    return print('Medicamento modificadO')
  def promedioMedicamentos(cantidadExistente):
    return print('Valor Total promedio')
  def buscarCantidadDosis():
    return print('Numero dosis')

class Hopitalizado:
  codigoMascota = str
  numeroHabitacion = int
  fecha = " "
  parteMedico = " "
  numeroReviciones = int
  
  def _init_(self, codigoMascota, numeroHabitacion, fecha, parteMedico, numeroReviciones):
    self.codigoMascota = codigoMascota
    self.numeroHabitacion = numeroHabitacion
    self.fecha = fecha
    self.parteMedico = parteMedico
    self.numeroReviciones = numeroReviciones
    
  def buscarPasiente(codigoMascota):
    return print('Datos Pasiente')
  def imprimirParteMedico():
    return print('Parte Medico')
  def modificarPasiente():
    return print('Pasiente modificadO')
  def promedioReviciones(numeroReviciones):
    return print('Valor Total promedio')
  def fechaDeSalida():
    return print('Fecha que el paciente salio')