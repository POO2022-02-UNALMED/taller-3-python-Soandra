from tv import TV
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