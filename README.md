# Wemos D1 thermometer
Features:
- measure temperature and humidity with DHT22 sensor
- displays on 0.66" oled
- pushes to adafruit.io every minute

# Parts
- Wemos D1 mini, flashed with micropython
- DHT22 temperature/humidity sensor
- Wemos 0.66" oled shield

# Connections DHT22
- DAT to GPIO2 (=wemos D4)
- VCC to 5V
- Ground to ground

# Setup
- prepare Wemos D1 mini with micropython
- solder headers on Wemos D1 mini and oled shield
- place oled shield on D1 mini
- solder connections to DHT22

- signup for account on adafruit.io and create two feeds for temperature and humidity
- fill in settings in settings_template.py, save file as settings.py
- copy files to board
- done

# copy file to board
```ampy -d 0.5 -p /dev/cu.wchusbserial1410 -b 115200 put file.py```

# REPL
```screen /dev/cu.wchusbserial1410 115200```
- exit: ctrl-A + ctrl-\