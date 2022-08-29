
class Marca:
    
    def __init__(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def serNombre(self, name):
        self._nombre = name


class TV:
    _numTV = 0

    def __init__(self, marca, estado, control):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = control
        self._numTV += 1

    def getMarca(self):
        return self._marca

    def setMarca(self, brand):
        self._marca = brand

    def getControl(self):
        return self._control

    def setControl(self, contrl):
        self._control = contrl

    def getPrecio(self):
        return self._precio

    def setPrecio(self, price):
        self._precio = price

    def getVolumen(self):
        return self._volumen

    def setVolumen(self, volume):
        self._volumen = volume

    def getCanal(self):
        return self._canal

    def setCanal(self, channel):
        self._canal = channel

    
    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False


    def getEstado(self):
        return self._estado


    def getNumTV(self):
        return self._numTV

    def setNumTV(self, num_tv):
        self._numTV = num_tv

    
    def canalUp(self):
        if self._estado and self._canal >= 1 and self._canal < 120:
            self._canal += 1

    def canalDown(self):
        if self._estado and self._canal > 1 and self._canal <= 120:
            self._canal -= 1

    
    def volumenUp(self):
        if self._estado and self._volumen >= 0 and self._volumen < 7:
            self._canal += 1

    def volumenDown(self):
        if self._estado and self._volumen > 0 and self._volumen <= 7:
            self._canal -= 1


class Control:

    _tv = TV

    def turnOn(self):
        self._tv.tv.turnOn()

    def turnOff(self):
        self._tv.tv.turnOff()
    
    def canalUp(self):
        self._tv.tv.canalUp()

    def canalDown(self):
        self._tv.tv.canalDonw()

    def volumenUp(self):
        self._tv.tv.volumenUp()

    def volumenDown(self):
        self._tv.tv.volumenDown()

    
    def setCanal(self , i):
        self._tv.tv.setCanal(i)

    
    def enlazar(self, tv):
        self._tv = tv
        tv.setControl(self)

    def getTv(self):
        return self._tv

    def setTv(self, tele):
        self._t = tele
    


 
        

      

