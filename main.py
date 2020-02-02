import connect
import screen
import utime
import ntptime

from dht22 import Dht
from screen import Screen
from adafruit_io_client import Client

dht=Dht()
screen=Screen()
adafruit_client=Client()

connect.connect()
ntptime.settime()

while True:
    t = utime.localtime(utime.time())
    m=dht.measure()
    screen.text('%02d:%02d:%02d' % (t[3], t[4], t[5]), 0)
    screen.text('t: %2.1f' % m[0], 2)
    screen.text('h: %2.1f' % m[1], 4)
    screen.show()
    adafruit_client.publish(m[0], m[1])
    utime.sleep(60)
