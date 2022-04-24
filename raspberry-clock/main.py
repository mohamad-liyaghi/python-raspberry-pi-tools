import machine,utime
#---------------------------------------------
decimal_h = machine.Pin(15,machine.Pin.OUT)
unity_h = machine.Pin(14,machine.Pin.OUT)
decimal_s = machine.Pin(17,machine.Pin.OUT)
unity_s = machine.Pin(16,machine.Pin.OUT)
red = machine.Pin(18,machine.Pin.OUT)
#---------------------------------------------
while True:
    decimal_h.value(1)
    unity_h.value(1)
    decimal_s.value(1)
    unity_s.value(1)
    red.value(1)
    utime.sleep(2)
    decimal_h.value(0)
    unity_h.value(0)
    decimal_s.value(0)
    unity_s.value(0)
    red.value(0)
    utime.sleep(2)
#---------------------------------------------

