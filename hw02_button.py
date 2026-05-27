#hw02_button.py
from gpiozero import LED, Button
from signal import pause

led = LED(14)        
button = Button(4)  

button.when_pressed = led.on
button.when_released = led.off

print("Press the button to turn the LED ON.")
print("Release the button to turn the LED OFF.")

pause()
