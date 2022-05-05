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

while True:
    status_led.value(1)
    one_forth.value(1)
    two_forth.value(1)
    three_forth.value(1)
    four_forth.value(1)
    if reset_button.value():
        time.sleep(0.20)
        print("1")
    elif add_button.value():
        time.sleep(0.20)
        print("2")
    elif stop_button.value():
        time.sleep(0.20)
        print("3")
    elif start_button.value():
        time.sleep(0.20)
        print("4")
    else:
        pass
        

