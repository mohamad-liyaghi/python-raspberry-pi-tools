import machine,utime
#-----------------------------------------------
sensor_temp = machine.ADC(4)
yellow_led = machine.Pin(15,machine.Pin.OUT)
purple_led = machine.Pin(14,machine.Pin.OUT)
red_led = machine.Pin(16,machine.Pin.OUT)
#-----------------------------------------------
conversion_factor = 3.3 / (65535)
#-----------------------------------------------
while True:
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    if temperature <= 20:
        purple_led.value(1)
        utime.sleep(2)
        purple_led.value(0)
        utime.sleep(2)
    elif 21 <= temperature <= 30:
        purple_led.value(1)
        yellow_led.value(1)
        utime.sleep(2)
        purple_led.value(0)
        yellow_led.value(0)
        utime.sleep(2)
    else:
        red_led.value(1)
        purple_led.value(1)
        yellow_led.value(1)
        utime.sleep(2)
        purple_led.value(0)
        yellow_led.value(0)
        red_led.value(0)
        utime.sleep(2)        
#-----------------------------------------------

