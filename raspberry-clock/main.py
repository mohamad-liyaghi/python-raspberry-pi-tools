import machine,utime,re
#------------------------------------------------
decimal_h = machine.Pin(16,machine.Pin.OUT)
unity_h = machine.Pin(17,machine.Pin.OUT)
decimal_s = machine.Pin(15,machine.Pin.OUT)
unity_s = machine.Pin(14,machine.Pin.OUT)
red = machine.Pin(18,machine.Pin.OUT)
#------------------------------------------------
while True:
    hour = str(utime.localtime()[3])
    minute = str(utime.localtime()[4])
    #------------------------------------------------
    if int(hour) < 10:
        for a in range(int(hour)):
            unity_h.value(1)
            unity_h.value(0)
            utime.sleep(0.5)
            #------------------------------------------------
    else:
        for b in range (int(hour[0])):
            decimal_h.value(1)
            utime.sleep(0.5)
            decimal_h.value(0)
            utime.sleep(0.5)
            #------------------------------------------------
        utime.sleep(0.5)
        decimal_h.value(1)
        #------------------------------------------------
        for c in range (int(hour[1])):
            unity_h.value(1)
            utime.sleep(0.5)
            unity_h.value(0)
            utime.sleep(0.5)
            #------------------------------------------------
        utime.sleep(0.5)
        unity_h.value(1)
        #------------------------------------------------
    
    if int(minute) < 10:
        for d in range(int(minute[1])):
            unity_s.value(1)
            utime.sleep(0.5)
            unity_s.value(0)
            utime.sleep(0.5)
            #------------------------------------------------
        utime.sleep(0.5)
        unity_s.value(1)
        #------------------------------------------------
    else:
        for e in range(int(minute [0])):
            decimal_s.value(1)
            utime.sleep(0.5)
            decimal_s.value(0)
            utime.sleep(0.5)
            #------------------------------------------------
        utime.sleep(0.5)
        decimal_s.value(1)
        #------------------------------------------------
        for f in range(int(minute[1])):
            unity_s.value(1)
            utime.sleep(0.5)
            unity_s.value(0)
            utime.sleep(0.5)
        utime.sleep(0.5)
        unity_s.value(1)
        utime.sleep(0.5)
        #------------------------------------------------        
        decimal_h.value(0)
        unity_h.value(0)
        red.value(0)
        decimal_s.value(0)
        unity_s.value(0)
        #------------------------------------------------
