from gpiozero import LED
from time import sleep

led = LED(17)
timeout = 60   # [seconds]

timeout_start = time.time()

while time.time() < timeout_start + timeout:  
     led.on()
    sleep(1)
    led.off()
    sleep(1)
