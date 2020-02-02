from umqtt.robust import MQTTClient

import machine
import ubinascii
import settings
import ujson
import connect

class Client:

    def __init__(self):
        self._client = MQTTClient(
            client_id=ubinascii.hexlify(machine.unique_id()),
            server="io.adafruit.com", 
            user=settings.ADAFRUIT_IO_USERNAME, 
            password=settings.ADAFRUIT_IO_KEY,
            ssl=False
        )
        self._temp_feed = bytes(
            settings.ADAFRUIT_IO_USERNAME + "/feeds/" + settings.ADAFRUIT_TEMP_FEED,
            "utf-8"
        )
        self._hum_feed = bytes(
            settings.ADAFRUIT_IO_USERNAME + "/feeds/" + settings.ADAFRUIT_HUM_FEED,
            "utf-8"
        )

    def publish(self, temp, hum):
        connect.connect()
        self._client.connect()
        self._client.publish(self._temp_feed, bytes(str(temp), 'utf-8'))
        self._client.publish(self._hum_feed, bytes(str(hum), 'utf-8'))
