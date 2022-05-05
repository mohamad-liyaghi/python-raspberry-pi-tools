from machine import Pin
import time

#lights
status_led = Pin(16, Pin.OUT)
one_forth = Pin(17, Pin.OUT)
two_forth = Pin(18, Pin.OUT)
three_forth = Pin(19, Pin.OUT)
four_forth = Pin(20, Pin.OUT)


#buttons
start_button = Pin(12, Pin.IN, Pin.PULL_DOWN)
stop_button = Pin(13, Pin.IN, Pin.PULL_DOWN)
add_button = Pin(14, Pin.IN, Pin.PULL_DOWN)
reset_button = Pin(15, Pin.IN, Pin.PULL_DOWN)
 
# time
minuet = 0
second = 0
status = False

while True:
    
    if reset_button.value():
        time.sleep(0.20)
        minuet = 0
        print(minuet)
        
    elif add_button.value():
        time.sleep(0.20)
        minuet += 1
        print(minuet)
        
    elif start_button.value():
        time.sleep(0.20)
        status = True
        print("Started")
    
    while status:
        status_led.value(1)
        if minuet == 0 and second == 0:
            status = False
            status_led.value(0)
            print("Done")
            break
        
        if minuet != 0 and second == 0:
            second = 60
            minuet -= 1
            
        if stop_button.value():
            time.sleep(0.20)
            status = False
            status_led.value(0)
            print("Stoped")
            break
        
        second -= 1
        time.sleep(1)
        print(f"{minuet}:{second}")


