

class Control:

    def __init__(self):
        self._tv = None
        

    

    def turnOn(self):
        self._tv.turnOn()

    def turnOff(self):
        self._tv.turnOff()
    
    def canalUp(self):
        self._tv.canalUp()

    def canalDown(self):
        self._tv.canalDonw()

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.volumenDown()

    
    def setCanal(self , i):
        self._tv.setCanal(i)

    
    def enlazar(self, tv):
        self._tv = tv
        tv.setControl(self)

    def getTv(self):
        return self._tv

    def setTv(self, tele):
        self._tv = tele