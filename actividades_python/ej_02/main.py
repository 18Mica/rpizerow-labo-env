from gpiozero import LED
from time import sleep

red = LED(19)
blue = LED(26)
green = LED(13)

while True:
   green.on()
   sleep(1)
   green.off()
   sleep(1)
   blue.on()
   green.on()
   sleep(1)
   green.off()
   sleep(1)
   blue.off()
   sleep(1)
   red.on()
   green.on()
   green.off()
   sleep(1)
   blue.on()
   green.on()
   sleep(1)
   green.off()
   blue.off
   red.off()
   sleep(1)
