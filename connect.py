import network
import utime

import settings

def connect():
    wlan = network.WLAN(network.STA_IF)
    while not wlan.isconnected():
        print('connecting to network ' + settings.WIFI_SSID + ' ...')
        wlan.active(True)
        wlan.connect(settings.WIFI_SSID, settings.WIFI_PASSWORD)
        utime.sleep(5)

    print('connected to ' + settings.WIFI_SSID)

