class TV:
    numTV = 0

    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self._canal = 1
        self._precio = 500
        self._volumen = 1
        self._control = None
        TV.numTV += 1


    def getMarca(self):
        return self.marca

    def setMarca(self, brand):
        self.marca = brand

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

    def setVolumen(self, volumen):
        if volumen >=0 and volumen <= 7 and self.estado == True:
            self._volumen = volumen

    def getCanal(self):
        return self._canal

    def setCanal(self, channel):
        if channel >= 0 and channel <= 120 and self.estado == True:
            self._canal = channel
        

    
    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False


    def getEstado(self):
        return self.estado

    @classmethod
    def getNumTV(cls):
        return cls._numTV

    @classmethod
    def setNumTV(cls, num_tv):
        cls._numTV = num_tv

    
    def canalUp(self):
        if self.estado and self._canal >= 1 and self._canal < 120:
            self._canal += 1

    def canalDown(self):
        if self.estado  and self._canal > 1 and self._canal <= 120:
            self._canal -= 1

    
    def volumenUp(self):
        if self.estado and self._volumen >= 0 and self._volumen < 7:
            self._volumen += 1

    def volumenDown(self):
        if self.estado and self._volumen > 0 and self._volumen <= 7:
            self._volumen -= 1