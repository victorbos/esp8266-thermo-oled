import dht
import machine

class Dht:

    def __init__(self):
        self._dht = dht.DHT22(machine.Pin(2))

    
    def measure(self):
        self._dht.measure()
        return (
            round(self._dht.temperature(), 1), 
            round(self._dht.humidity(), 1)
        )